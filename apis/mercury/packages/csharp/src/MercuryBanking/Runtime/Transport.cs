using System.Buffers.Binary;
using System.Collections;
using System.Collections.Concurrent;
using System.Diagnostics;
using System.Globalization;
using System.IO.Compression;
using System.Net;
using System.Net.Http.Headers;
using System.Net.Sockets;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using Microsoft.Extensions.Logging;
using MercuryBanking.Models;

namespace MercuryBanking.Runtime;

internal sealed class Transport : IDisposable
{
    private const string Redacted = "***";
    // The largest integer a JavaScript number holds exactly, so every runtime accepts the same numeric cursors.
    private const double MaxSafeInteger = 9007199254740991;
    private const int MaxRedirects = 5;
    private static readonly int[] Redirects = [301, 302, 303, 307, 308];
    private static readonly TimeSpan DefaultJobInterval = TimeSpan.FromSeconds(60);
    private static readonly TimeSpan DefaultJobTimeout = TimeSpan.FromHours(1);
    private static readonly Operation UrlDownload = new("downloadUrl", "GET", string.Empty, string.Empty, "DownloadUrlAsync", null, [], Security: [], ReturnsBinary: true);
    private static readonly string[] Months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];

    /// <summary>RFC 5322, RFC 850 and asctime dates, as leniently as Python's <c>email.utils</c>.</summary>
    private static readonly Regex HttpDate = new(
        @"^(?:[a-z]+,?\s*)?(?:(?<day>[0-9]{1,2})[\s-]+(?<month>[a-z]{3})[a-z]*[\s-]+(?<year>[0-9]{4}|[0-9]{2})\s+(?<time>[0-9]{1,2}:[0-9]{2}(?::[0-9]{2})?)(?:\s*(?<zone>[a-z]+|[+-][0-9]{4}))?"
        + @"|(?<month>[a-z]{3})\s+(?<day>[0-9]{1,2})\s+(?<time>[0-9]{1,2}:[0-9]{2}:[0-9]{2})\s+(?<year>[0-9]{4}))$",
        RegexOptions.IgnoreCase | RegexOptions.CultureInvariant);

    private static readonly Dictionary<string, int> ZoneHours = new(StringComparer.OrdinalIgnoreCase)
    {
        ["EST"] = -5,
        ["EDT"] = -4,
        ["CST"] = -6,
        ["CDT"] = -5,
        ["MST"] = -7,
        ["MDT"] = -6,
        ["PST"] = -8,
        ["PDT"] = -7,
    };

    private static readonly HttpRequestOptionsKey<bool> Connected = new("Connected");

    private readonly Settings settings;
    private readonly Dictionary<string, string> headerDefaults;
    private readonly Dictionary<string, string> queryDefaults;
    private readonly HttpClient http;
    private readonly bool ownsClient;
    private readonly SemaphoreSlim refreshing = new(1, 1);
    private readonly ConcurrentDictionary<string, long> generations = new();

    /// <remarks>Reads and writes share one pool of connections. <see cref="AttemptAsync"/> shapes each write so the handler never resends it.</remarks>
    /// <exception cref="ArgumentException">Two header defaults have names that differ only by case. A client it owns is disposed.</exception>
    public Transport(Settings settings, HttpClient http, bool ownsClient)
    {
        this.settings = settings;
        try
        {
            headerDefaults = ByName(settings.HeaderDefaults);
            queryDefaults = new Dictionary<string, string>(settings.QueryDefaults, StringComparer.Ordinal);
        }
        catch
        {
            if (ownsClient)
            {
                http.Dispose();
            }
            throw;
        }
        this.http = http;
        this.ownsClient = ownsClient;
    }

    /// <summary>A client of our own, over <paramref name="handler"/> or, by default, <see cref="CreateHandler"/>.</summary>
    public static HttpClient OwnClient(HttpMessageHandler? handler) =>
        new(handler ?? CreateHandler(), disposeHandler: handler is null) { Timeout = System.Threading.Timeout.InfiniteTimeSpan };

    public void Dispose()
    {
        refreshing.Dispose();
        if (ownsClient)
        {
            http.Dispose();
        }
    }

    public static SocketsHttpHandler CreateHandler() => new()
    {
        AllowAutoRedirect = false,
        AutomaticDecompression = DecompressionMethods.None,
        PooledConnectionLifetime = TimeSpan.FromMinutes(5),
        ConnectCallback = ConnectOnceAsync,
    };

    /// <summary>
    /// Opens at most one connection per request. The handler otherwise resends a request whose connection
    /// closes before any response, which would repeat a write and turn one attempt into several.
    /// </summary>
    private static async ValueTask<Stream> ConnectOnceAsync(SocketsHttpConnectionContext context, CancellationToken cancellationToken)
    {
        var options = context.InitialRequestMessage.Options;
        if (options.TryGetValue(Connected, out _))
        {
            throw new HttpRequestException(HttpRequestError.ConnectionError, "The connection closed before a response");
        }
        options.Set(Connected, true);
        var socket = new Socket(SocketType.Stream, ProtocolType.Tcp) { NoDelay = true };
        try
        {
            await socket.ConnectAsync(context.DnsEndPoint, cancellationToken).ConfigureAwait(false);
            return new NetworkStream(socket, ownsSocket: true);
        }
        catch
        {
            socket.Dispose();
            throw;
        }
    }

    public async Task<T> CallAsync<T>(Operation operation, object?[] values, CancellationToken cancellationToken) =>
        Parse<T>(operation, await FetchAsync(operation, values, cancellationToken).ConfigureAwait(false));

    private static T Parse<T>(Operation operation, Reply reply)
    {
        RejectEmpty(operation, reply);
        if (typeof(T) == typeof(string))
        {
            return (T)(object)(reply.Json is { ValueKind: JsonValueKind.String } text ? text.GetString()! : reply.Text);
        }
        if (reply.Json is { } json)
        {
            return Json.Read<T>(json, reply.Status, reply.Clean);
        }
        if (reply.Text.Length == 0 && reply.Status == 204)
        {
            return default!;
        }
        if (reply.Text.Length == 0)
        {
            throw new ApiDecodeException($"The response body is empty, so it cannot be a {typeof(T).Name}") { Status = reply.Status, RawBody = reply.Clean };
        }
        throw new ApiDecodeException($"The response is not JSON, so it cannot be a {typeof(T).Name}") { Status = reply.Status, RawBody = reply.Clean };
    }

    /// <summary>A binary response, streamed. Nothing is retried once it is returned.</summary>
    public Task<Download> DownloadAsync(Operation operation, object?[] values, CancellationToken cancellationToken) =>
        FetchAsync(operation, values, async (auth, stream, token) => (await OpenAsync(auth, stream, redirects: false, token).ConfigureAwait(false)).Download!, cancellationToken);

    /// <summary>
    /// Polls a job's status operation until the job ends, and returns its last status, done or failed. Each poll is an
    /// ordinary call, retried as usual, and the wait between polls is cut short by the deadline or by cancellation.
    /// </summary>
    /// <exception cref="ArgumentException">The operation reports no job, or the interval or timeout is negative. Nothing is sent.</exception>
    /// <exception cref="ApiJobTimeoutException">The job had not ended by the deadline.</exception>
    public async Task<T> WaitAsync<T>(Operation operation, object?[] values, TimeSpan? interval, TimeSpan? timeout, CancellationToken cancellationToken)
    {
        var job = operation.Job ?? throw new ArgumentException($"{operation.Id} does not report a job", nameof(operation));
        var every = interval ?? DefaultJobInterval;
        var limit = timeout ?? DefaultJobTimeout;
        if (every < TimeSpan.Zero)
        {
            throw new ArgumentOutOfRangeException(nameof(interval), every, "The interval must not be negative");
        }
        if (limit < TimeSpan.Zero)
        {
            throw new ArgumentOutOfRangeException(nameof(timeout), limit, "The timeout must not be negative");
        }
        var started = Stopwatch.GetTimestamp();
        while (true)
        {
            var reply = await FetchAsync(operation, values, cancellationToken).ConfigureAwait(false);
            var result = Parse<T>(operation, reply);
            if (JobEnded(job, reply))
            {
                return result;
            }
            var remaining = limit - Stopwatch.GetElapsedTime(started);
            if (remaining <= TimeSpan.Zero)
            {
                throw new ApiJobTimeoutException($"The job did not end within {limit}", result);
            }
            await Task.Delay(every < remaining ? every : remaining, cancellationToken).ConfigureAwait(false);
        }
    }

    private static bool JobEnded(JobPolling job, Reply reply)
    {
        var value = reply.Json;
        foreach (var key in job.State.Split('.'))
        {
            value = value is { ValueKind: JsonValueKind.Object } node && node.TryGetProperty(key, out var next) ? next : null;
        }
        if (value is not { ValueKind: JsonValueKind.String } state)
        {
            throw new ApiDecodeException($"The `{job.State}` state of a job is not a string") { Status = reply.Status, RawBody = reply.Clean };
        }
        var text = state.GetString()!;
        return job.Done.Contains(text) || job.Failed.Contains(text);
    }

    /// <summary>
    /// GETs an absolute URL that a response returned, as a download, following up to five redirects. Credentials go
    /// only to the base URL's scheme, host and port, and never again once a redirect leaves them. <paramref name="security"/>
    /// is what the credentials see as the operation's requirements. Each request is retried as usual.
    /// </summary>
    /// <remarks>
    /// The client's own handler never follows redirects, so they are followed here.
    /// TODO: a caller's handler that follows redirects itself drops only <c>Authorization</c> on the way, and sends any
    /// other credential header on to wherever they point. Such a download is refused, but only once it has happened.
    /// </remarks>
    /// <exception cref="ArgumentException">The URL is not an absolute http or https URL. Nothing is sent.</exception>
    public async Task<Download> DownloadUrlAsync(string url, Scheme[][]? security = null, CancellationToken cancellationToken = default)
    {
        var target = Absolute(url) ?? throw new ArgumentException("The URL is not an absolute http or https URL", nameof(url));
        var trusted = Origin(new Uri(settings.BaseUrl));
        var operation = UrlDownload with { Security = security ?? [] };
        var signed = true;
        for (var hop = 0; hop <= MaxRedirects; hop++)
        {
            signed = signed && Origin(target) == trusted;
            var opened = await ExchangeAsync(
                operation, target, () => null, null, [], signed, target.GetLeftPart(UriPartial.Path),
                (auth, _, token) => OpenAsync(auth, null, redirects: true, token), cancellationToken).ConfigureAwait(false);
            if (opened.Download is { } download)
            {
                return download;
            }
            target = opened.Location!;
        }
        throw new ApiDecodeException($"More than {MaxRedirects} redirects");
    }

    private static Uri? Absolute(string? url) =>
        Uri.TryCreate(url, UriKind.Absolute, out var parsed) && parsed.Scheme is "http" or "https" && parsed.Host.Length > 0 ? parsed : null;

    /// <remarks><see cref="Uri.Port"/> is already the scheme's default when the URL names none.</remarks>
    private static (string Scheme, string Host, int Port) Origin(Uri url) => (url.Scheme, url.Host.ToLowerInvariant(), url.Port);

    /// <summary>Where a redirect points, resolved against the request, or null for any other response.</summary>
    private static Uri? Redirect(int status, Dictionary<string, string> headers, Uri current)
    {
        if (!Redirects.Contains(status))
        {
            return null;
        }
        if (!headers.TryGetValue("Location", out var location) || location.Length == 0)
        {
            throw new ApiDecodeException("A redirect has no Location") { Status = status };
        }
        return Uri.TryCreate(current, location, out var resolved) && Absolute(resolved.AbsoluteUri) is { } next
            ? next
            : throw new ApiDecodeException("A redirect's Location is not an http or https URL") { Status = status };
    }

    public async Task SendAsync(Operation operation, object?[] values, CancellationToken cancellationToken) =>
        RejectEmpty(operation, await FetchAsync(operation, values, cancellationToken).ConfigureAwait(false));

    private static void RejectEmpty(Operation operation, Reply reply)
    {
        if (operation.ReturnsJson && reply.Text.Length == 0 && reply.Status != 204)
        {
            throw new ApiDecodeException("The response body is empty") { Status = reply.Status, RawBody = reply.Clean };
        }
    }

    public async IAsyncEnumerable<T> PaginateAsync<T>(
        Operation operation, object?[] values, [EnumeratorCancellation] CancellationToken cancellationToken = default)
    {
        var paging = operation.Paging ?? NextLinkPaging.Default;
        object?[]? current = values;
        while (current is not null)
        {
            var reply = await FetchAsync(operation, current, cancellationToken).ConfigureAwait(false);
            if (reply.Json is not { ValueKind: JsonValueKind.Object } page)
            {
                throw new ApiDecodeException("A page is not a JSON object") { Status = reply.Status, RawBody = reply.Clean };
            }
            var received = 0;
            if (page.TryGetProperty(paging.Items, out var results) && results.ValueKind == JsonValueKind.Array)
            {
                foreach (var item in results.EnumerateArray())
                {
                    received++;
                    yield return Json.Read<T>(item, reply.Status, reply.Clean);
                }
            }
            current = NextValues(operation, current, page, received);
        }
    }

    /// <summary>The values of the page after this one, or null after the last.</summary>
    internal static object?[]? NextValues(Operation operation, object?[] values, JsonElement page, int received) =>
        operation.Paging switch
        {
            OffsetPaging offset => NextOffset(operation, offset, values, page, received),
            CursorPaging cursor => NextCursor(operation, cursor, values, page),
            NextLinkPaging link => NextLink(operation, link, values, page),
            _ => NextLink(operation, NextLinkPaging.Default, values, page),
        };

    /// <summary>
    /// Reads the position out of the link and applies it to our own request. The link is never fetched:
    /// it could send the credential to another host.
    /// </summary>
    private static object?[]? NextLink(Operation operation, NextLinkPaging paging, object?[] values, JsonElement page)
    {
        if (!page.TryGetProperty(paging.Items, out var items) || items.ValueKind != JsonValueKind.Array)
        {
            throw new ApiDecodeException($"The `{paging.Items}` field of a page is not a list");
        }
        if (!page.TryGetProperty(paging.Link, out var next) || next.ValueKind is JsonValueKind.Null or JsonValueKind.False)
        {
            return null;
        }
        var link = next.ValueKind == JsonValueKind.String ? next.GetString()! : next.GetRawText();
        if (link.Length == 0)
        {
            return null;
        }
        if (!Uri.TryCreate(link, UriKind.RelativeOrAbsolute, out _))
        {
            throw new ApiDecodeException($"The `{paging.Link}` link is not a valid URL");
        }
        var position = QueryOf(link);
        var updated = (object?[])values.Clone();
        for (var index = 0; index < operation.Params.Length; index++)
        {
            var param = operation.Params[index];
            if (param.Location == ParamLocation.Query && paging.Params.Contains(param.Wire) && position.TryGetValue(param.Wire, out var value))
            {
                updated[index] = value;
            }
        }
        var same = operation.Params
            .Select((param, index) => (param, index))
            .Where(item => item.param.Location == ParamLocation.Query)
            .All(item => TextOrNull(updated[item.index]) == TextOrNull(values[item.index]));
        if (same)
        {
            throw new ApiDecodeException($"The `{paging.Link}` link does not advance the iteration");
        }
        return updated;
    }

    private static object?[]? NextOffset(Operation operation, OffsetPaging paging, object?[] values, JsonElement page, int received)
    {
        if (!page.TryGetProperty(paging.Items, out var items) || items.ValueKind != JsonValueKind.Array)
        {
            throw new ApiDecodeException($"The `{paging.Items}` field of a page is not a list");
        }
        if (received == 0)
        {
            return null;
        }
        var index = Array.FindIndex(operation.Params, param => param.Location == ParamLocation.Query && param.Wire == paging.Offset);
        var start = 0L;
        if (values[index] is { } current && !long.TryParse(Json.Text(current), NumberStyles.AllowLeadingSign, CultureInfo.InvariantCulture, out start))
        {
            throw new ApiDecodeException($"The `{paging.Offset}` parameter is not an integer");
        }
        var position = start + received;
        if (page.TryGetProperty(paging.Total, out var total) && total.ValueKind == JsonValueKind.Number && position >= total.GetDouble())
        {
            return null;
        }
        var updated = (object?[])values.Clone();
        updated[index] = position;
        return updated;
    }

    private static object?[]? NextCursor(Operation operation, CursorPaging paging, object?[] values, JsonElement page)
    {
        if (!page.TryGetProperty(paging.Items, out var items) || items.ValueKind != JsonValueKind.Array)
        {
            throw new ApiDecodeException($"The `{paging.Items}` field of a page is not a list");
        }
        var value = page;
        foreach (var key in paging.Next.Split('.'))
        {
            if (value.ValueKind == JsonValueKind.Null)
            {
                break;
            }
            if (value.ValueKind != JsonValueKind.Object)
            {
                throw new ApiDecodeException($"The `{paging.Next}` value of a page is not inside an object");
            }
            if (!value.TryGetProperty(key, out value))
            {
                return null;
            }
        }
        if (value.ValueKind == JsonValueKind.Null)
        {
            return null;
        }
        string position;
        if (value.ValueKind == JsonValueKind.Number && value.TryGetDouble(out var whole) && Math.Abs(whole) <= MaxSafeInteger && Math.Floor(whole) == whole)
        {
            position = ((long)whole).ToString(CultureInfo.InvariantCulture);
        }
        else if (value.ValueKind == JsonValueKind.String)
        {
            position = value.GetString()!;
        }
        else
        {
            throw new ApiDecodeException($"The `{paging.Next}` value of a page is not a string or an integer");
        }
        if (position.Length == 0)
        {
            return null;
        }
        var index = Array.FindIndex(operation.Params, param => param.Location == ParamLocation.Query && param.Wire == paging.Param);
        if (TextOrNull(values[index]) == position)
        {
            throw new ApiDecodeException($"The `{paging.Next}` value does not advance the iteration");
        }
        var updated = (object?[])values.Clone();
        updated[index] = position;
        return updated;
    }

    internal static Dictionary<string, string> QueryOf(string link)
    {
        var query = new Dictionary<string, string>();
        var start = link.IndexOf('?');
        if (start < 0)
        {
            return query;
        }
        var end = link.IndexOf('#', start);
        var text = end < 0 ? link[(start + 1)..] : link[(start + 1)..end];
        foreach (var pair in text.Split('&', StringSplitOptions.RemoveEmptyEntries))
        {
            var parts = pair.Split('=', 2);
            var value = parts.Length > 1 ? Unescape(parts[1]) : string.Empty;
            if (value.Length > 0)
            {
                query.TryAdd(Unescape(parts[0]), value);
            }
        }
        return query;
    }

    internal static double? RetryAfterSeconds(string? value, DateTimeOffset now)
    {
        if (value is null)
        {
            return null;
        }
        value = value.Trim();
        if (value.Length > 0 && value.All(char.IsAsciiDigit))
        {
            return double.Parse(value, CultureInfo.InvariantCulture);
        }
        var when = ParseHttpDate(value);
        if (when is null)
        {
            return null;
        }
        var wait = (when.Value - now).TotalSeconds;
        return wait > 0 ? wait : null;
    }

    /// <summary>A date with an unknown zone or none is read as UTC.</summary>
    private static DateTimeOffset? ParseHttpDate(string value)
    {
        var match = HttpDate.Match(value);
        if (!match.Success)
        {
            return null;
        }
        var month = Array.IndexOf(Months, match.Groups["month"].Value.ToLowerInvariant()) + 1;
        var year = int.Parse(match.Groups["year"].Value, CultureInfo.InvariantCulture);
        if (year < 100)
        {
            year += year > 68 ? 1900 : 2000;
        }
        var time = match.Groups["time"].Value.Split(':').Select(part => int.Parse(part, CultureInfo.InvariantCulture)).ToArray();
        var zone = match.Groups["zone"].Value;
        var offset = TimeSpan.Zero;
        if (zone.Length == 5 && zone[0] is '+' or '-')
        {
            var minutes = (int.Parse(zone[1..3], CultureInfo.InvariantCulture) * 60) + int.Parse(zone[3..], CultureInfo.InvariantCulture);
            offset = TimeSpan.FromMinutes(zone[0] == '-' ? -minutes : minutes);
        }
        else if (ZoneHours.TryGetValue(zone, out var hours))
        {
            offset = TimeSpan.FromHours(hours);
        }
        try
        {
            var day = int.Parse(match.Groups["day"].Value, CultureInfo.InvariantCulture);
            return new DateTimeOffset(year, month, day, time[0], time[1], time.Length > 2 ? time[2] : 0, offset);
        }
        catch (ArgumentException)
        {
            return null;
        }
    }

    private static string Unescape(string text) => Uri.UnescapeDataString(text.Replace('+', ' '));

    private static string? TextOrNull(object? value) => value is null ? null : Json.Text(value);

    private static IEnumerable<object> Items(object value) =>
        value is IEnumerable items and not string and not byte[]? items.OfType<object>() : [value];

    private static string Quote(string text) => $"\"{text.Replace("\\", "\\\\").Replace("\"", "\\\"")}\"";

    /// <summary>
    /// A GET may be sent again after a 5xx, a timeout or a dropped connection, and so may a write whose JSON body sets
    /// the operation's idempotency key. A write without the key could act twice.
    /// </summary>
    private static bool Repeatable(Operation operation, ReadOnlyMemory<byte> body)
    {
        if (operation.Method == "GET")
        {
            return true;
        }
        if (operation.IdempotencyKey is null || body.IsEmpty)
        {
            return false;
        }
        try
        {
            using var document = JsonDocument.Parse(body);
            return document.RootElement.ValueKind == JsonValueKind.Object
                && document.RootElement.TryGetProperty(operation.IdempotencyKey, out var key)
                && key.ValueKind != JsonValueKind.Null
                && !(key.ValueKind == JsonValueKind.String && key.GetString() == string.Empty);
        }
        catch (JsonException)
        {
            return false;
        }
    }

    private TimeSpan? RetryDelay(ApiException error, bool repeatable, int tries)
    {
        if (tries >= settings.MaxRetries)
        {
            return null;
        }
        if (error.Status == 429)
        {
            var wait = RetryAfterSeconds(error.RetryAfter, DateTimeOffset.UtcNow);
            if (wait is null)
            {
                return settings.RateLimitWait;
            }
            return wait <= settings.MaxRetryWait.TotalSeconds ? TimeSpan.FromSeconds(wait.Value) : null;
        }
        var failed = error is ApiTimeoutException or ApiConnectionException || error.Status >= 500;
        return repeatable && failed ? settings.RetryBaseDelay * Math.Pow(2, tries) : null;
    }

    private void Log(LogLevel level, string message)
    {
        if (settings.Logger.IsEnabled(level))
        {
            settings.Logger.Log(level, "{Message}", Redact(message));
        }
    }

    private string BaseUrlOf(Operation operation)
    {
        if (string.IsNullOrEmpty(operation.Host))
        {
            return settings.BaseUrl;
        }
        return settings.Hosts.TryGetValue(operation.Host, out var url)
            ? url
            : throw new InvalidOperationException($"No base URL for host \"{operation.Host}\" in the client's hosts");
    }

    private static Dictionary<string, string> ByName(IReadOnlyDictionary<string, string> defaults)
    {
        var clashes = defaults.Keys
            .GroupBy(name => name, StringComparer.OrdinalIgnoreCase)
            .Where(group => group.Count() > 1)
            .SelectMany(group => group)
            .Order(StringComparer.Ordinal)
            .ToArray();
        if (clashes.Length > 0)
        {
            throw new ArgumentException(
                $"HeaderDefaults has names that differ only by case: {string.Join(", ", clashes)}", nameof(settings));
        }
        return new Dictionary<string, string>(defaults, StringComparer.OrdinalIgnoreCase);
    }

    /// <summary>The value for each header parameter: the call's own, or else the client's default for that name.</summary>
    private List<KeyValuePair<string, string>> HeadersOf(Operation operation, object?[] values)
    {
        var headers = new List<KeyValuePair<string, string>>();
        for (var index = 0; index < operation.Params.Length; index++)
        {
            var param = operation.Params[index];
            if (param.Location != ParamLocation.Header)
            {
                continue;
            }
            if (values[index] is { } value)
            {
                headers.Add(KeyValuePair.Create(param.Wire, Json.Text(value)));
            }
            else if (headerDefaults.TryGetValue(param.Wire, out var fallback))
            {
                headers.Add(KeyValuePair.Create(param.Wire, fallback));
            }
        }
        return headers;
    }

    /// <remarks>A <see cref="RawBody"/> stream is returned apart, to be sent once; its content here only carries its type.</remarks>
    private (Uri Url, Func<HttpContent?> Content, Stream? Stream) Build(Operation operation, object?[] values)
    {
        var baseUrl = BaseUrlOf(operation);
        var path = operation.Path;
        var query = new List<string>();
        var parts = new List<(string Wire, object Value)>();
        var fields = new List<KeyValuePair<string, string>>();
        object? body = null;
        RawBody? raw = null;
        for (var index = 0; index < operation.Params.Length; index++)
        {
            var param = operation.Params[index];
            var value = values[index];
            if (value is null && param.Defaulted && queryDefaults.TryGetValue(param.Wire, out var fallback))
            {
                value = fallback;
            }
            if (value is null)
            {
                continue;
            }
            switch (param.Location)
            {
                case ParamLocation.Path:
                    path = path.Replace($"{{{param.Wire}}}", Uri.EscapeDataString(Json.Text(value)), StringComparison.Ordinal);
                    break;
                case ParamLocation.Query:
                    query.AddRange(Items(value).Select(item => $"{Uri.EscapeDataString(param.Wire)}={Uri.EscapeDataString(Json.Text(item))}"));
                    break;
                case ParamLocation.Form:
                    parts.AddRange(Items(value).Select(item => (param.Wire, item)));
                    break;
                case ParamLocation.Urlencoded:
                    fields.AddRange(Items(value).Select(item => KeyValuePair.Create(param.Wire, Json.Text(item))));
                    break;
                case ParamLocation.Header:
                    break;
                case ParamLocation.Raw:
                    raw = (RawBody)value;
                    break;
                default:
                    body = value;
                    break;
            }
        }
        var url = new Uri($"{baseUrl}{path}{(query.Count > 0 ? "?" + string.Join('&', query) : string.Empty)}");
        if (raw is not null)
        {
            var type = MediaTypeHeaderValue.Parse(operation.RawBodyType ?? "application/octet-stream");
            var sent = raw.Bytes ?? [];
            return (url, () => new ByteArrayContent(sent) { Headers = { ContentType = type } }, raw.Stream);
        }
        if (parts.Count > 0)
        {
            return (url, () => Multipart(parts), null);
        }
        if (fields.Count > 0)
        {
            return (url, () => new FormUrlEncodedContent(fields), null);
        }
        if (body is null)
        {
            return (url, () => null, null);
        }
        var bytes = JsonSerializer.SerializeToUtf8Bytes(body, body.GetType(), Json.Options);
        return (url, () => new ByteArrayContent(bytes) { Headers = { ContentType = new MediaTypeHeaderValue("application/json") } }, null);
    }

    private static MultipartFormDataContent Multipart(List<(string Wire, object Value)> parts)
    {
        var form = new MultipartFormDataContent();
        foreach (var (wire, value) in parts)
        {
            if (value is UploadFile file)
            {
                var bytes = new ByteArrayContent(file.Content);
                bytes.Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");
                bytes.Headers.ContentDisposition = Disposition(wire, file.FileName);
                form.Add(bytes);
                continue;
            }
            var text = value is ApiModel or IDictionary ? JsonSerializer.Serialize(value, value.GetType(), Json.Options) : Json.Text(value);
            var part = new StringContent(text);
            part.Headers.ContentType = null;
            form.Add(part, Quote(wire));
        }
        return form;
    }

    /// <summary>
    /// Sets <c>filename*</c> only for a name that is not ASCII, with <c>filename</c> as the fallback for servers that
    /// ignore it. The name is set as a parameter because the property setter rejects a quote mark inside it.
    /// </summary>
    private static ContentDispositionHeaderValue Disposition(string wire, string fileName)
    {
        if (fileName.Length == 0 || fileName.Any(char.IsControl))
        {
            throw new ArgumentException("A file name must be non-empty and contain no control characters", nameof(UploadFile.FileName));
        }
        var disposition = new ContentDispositionHeaderValue("form-data") { Name = Quote(wire) };
        var ascii = Ascii.IsValid(fileName);
        var fallback = ascii ? fileName : $"=?utf-8?B?{Convert.ToBase64String(Encoding.UTF8.GetBytes(fileName))}?=";
        disposition.Parameters.Add(new NameValueHeaderValue("filename", Quote(fallback)));
        if (!ascii)
        {
            disposition.FileNameStar = fileName;
        }
        return disposition;
    }

    private Task<Reply> FetchAsync(Operation operation, object?[] values, CancellationToken cancellationToken) =>
        FetchAsync(
            operation,
            values,
            async (auth, stream, token) => Read(operation.Method, await AttemptAsync(auth, stream, token).ConfigureAwait(false)),
            cancellationToken);

    private async Task<TResult> FetchAsync<TResult>(
        Operation operation, object?[] values, Func<AuthRequest, Stream?, CancellationToken, Task<TResult>> attempt, CancellationToken cancellationToken)
    {
        var (url, content, stream) = Build(operation, values);
        return await ExchangeAsync(operation, url, content, stream, HeadersOf(operation, values), signed: true, url.ToString(), attempt, cancellationToken).ConfigureAwait(false);
    }

    /// <summary>Sends a request, with credentials when <paramref name="signed"/>, retrying as the settings allow. <paramref name="shown"/> is the URL as logged.</summary>
    private async Task<TResult> ExchangeAsync<TResult>(
        Operation operation,
        Uri url,
        Func<HttpContent?> content,
        Stream? stream,
        List<KeyValuePair<string, string>> extra,
        bool signed,
        string shown,
        Func<AuthRequest, Stream?, CancellationToken, Task<TResult>> attempt,
        CancellationToken cancellationToken)
    {
        var refreshed = false;
        for (var tries = 0; ;)
        {
            Log(LogLevel.Debug, $"-> {operation.Method} {shown}");
            var group = settings.Credentials.RefreshGroup(operation);
            var seen = generations.GetValueOrDefault(group);
            var auth = await AuthorizeAsync(operation, url, content, extra, signed, cancellationToken).ConfigureAwait(false);
            try
            {
                return await attempt(auth, stream, cancellationToken).ConfigureAwait(false);
            }
            catch (ApiException error)
            {
                // A stream body has been read, so it cannot be sent again.
                if (stream is not null)
                {
                    throw;
                }
                // An operation with no security sends no credentials, such as a token request made during a refresh.
                if (signed && error.Status == 401 && !refreshed && operation.Security is { Length: > 0 })
                {
                    refreshed = true;
                    if (await RefreshAsync(auth, group, seen, cancellationToken).ConfigureAwait(false))
                    {
                        Log(LogLevel.Information, "retrying after refreshing credentials");
                        continue;
                    }
                }
                var delay = RetryDelay(error, Repeatable(operation, auth.Body), tries);
                if (delay is null)
                {
                    throw;
                }
                Log(LogLevel.Information, $"retrying after {delay.Value.TotalSeconds}s: {error.Kind}");
                await Task.Delay(delay.Value, cancellationToken).ConfigureAwait(false);
                tries++;
            }
        }
    }

    /// <summary>Encodes one attempt's request and, when <paramref name="signed"/>, lets the credentials sign the bytes that will be sent.</summary>
    private async Task<AuthRequest> AuthorizeAsync(
        Operation operation, Uri url, Func<HttpContent?> content, List<KeyValuePair<string, string>> extra, bool signed, CancellationToken cancellationToken)
    {
        using var draft = content();
        var body = draft is null ? [] : await draft.ReadAsByteArrayAsync(cancellationToken).ConfigureAwait(false);
        // A binary body is passed on as received, so it is asked for uncompressed.
        var encoding = operation.ReturnsBinary ? "identity" : "gzip";
        var headers = new Dictionary<string, string>(settings.Headers, StringComparer.OrdinalIgnoreCase) { ["Accept-Encoding"] = encoding };
        if (operation.Accept is not null)
        {
            headers["Accept"] = operation.Accept;
        }
        foreach (var (name, value) in extra)
        {
            // Removed first, so the header goes out under the name the operation declares.
            headers.Remove(name);
            headers[name] = value;
        }
        foreach (var (name, value) in draft?.Headers.NonValidated.ToArray() ?? [])
        {
            if (!name.Equals("Content-Length", StringComparison.OrdinalIgnoreCase))
            {
                headers[name] = value.ToString();
            }
        }
        var auth = new AuthRequest { Method = operation.Method, Url = url, Headers = headers, Body = body, Operation = operation };
        if (signed)
        {
            await settings.Credentials.ApplyAsync(auth, cancellationToken).ConfigureAwait(false);
        }
        return auth;
    }

    /// <summary>
    /// Calls waiting on a refresh of the same group share it, and a call whose credentials were refreshed since it sent
    /// them retries without another.
    /// </summary>
    private async Task<bool> RefreshAsync(AuthRequest auth, string group, long seen, CancellationToken cancellationToken)
    {
        await refreshing.WaitAsync(cancellationToken).ConfigureAwait(false);
        try
        {
            if (generations.GetValueOrDefault(group) != seen)
            {
                return true;
            }
            var refreshed = await settings.Credentials.RefreshAsync(auth, cancellationToken).ConfigureAwait(false);
            if (refreshed)
            {
                generations[group] = seen + 1;
            }
            return refreshed;
        }
        finally
        {
            refreshing.Release();
        }
    }

    /// <summary>One attempt, from sending the request to reading the last byte, under one deadline.</summary>
    private async Task<RawReply> AttemptAsync(AuthRequest auth, Stream? stream, CancellationToken cancellationToken)
    {
        using var deadline = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
        deadline.CancelAfter(settings.Timeout);
        using var request = Message(auth, stream);
        try
        {
            using var response = await http.SendAsync(request, HttpCompletionOption.ResponseHeadersRead, deadline.Token).ConfigureAwait(false);
            var body = await response.Content.ReadAsByteArrayAsync(deadline.Token).ConfigureAwait(false);
            return new RawReply((int)response.StatusCode, ResponseHeaders(response), body);
        }
        catch (Exception error) when (error is OperationCanceledException or HttpRequestException or IOException && !cancellationToken.IsCancellationRequested)
        {
            throw Translate(error, deadline);
        }
    }

    /// <summary>
    /// One attempt that hands a success body over as a stream, still under the attempt's deadline. A failure is read
    /// whole, as for any other operation. With <paramref name="redirects"/>, a redirect is returned as where it points.
    /// </summary>
    /// <exception cref="InvalidOperationException">With <paramref name="redirects"/>, the handler followed a redirect itself.</exception>
    private async Task<Opened> OpenAsync(AuthRequest auth, Stream? stream, bool redirects, CancellationToken cancellationToken)
    {
        var deadline = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
        deadline.CancelAfter(settings.Timeout);
        using var request = Message(auth, stream);
        HttpResponseMessage? response = null;
        try
        {
            response = await http.SendAsync(request, HttpCompletionOption.ResponseHeadersRead, deadline.Token).ConfigureAwait(false);
            var status = (int)response.StatusCode;
            if (redirects)
            {
                if (request.RequestUri != auth.Url)
                {
                    throw new InvalidOperationException("The HTTP handler followed a redirect itself; downloading a URL needs AllowAutoRedirect off");
                }
                if (Redirect(status, ResponseHeaders(response), auth.Url) is { } location)
                {
                    Log(LogLevel.Debug, $"<- {auth.Method} {status} (redirect)");
                    return new Opened(null, location);
                }
            }
            if (status is < 200 or >= 300)
            {
                var body = await response.Content.ReadAsByteArrayAsync(deadline.Token).ConfigureAwait(false);
                Read(auth.Method, new RawReply(status, ResponseHeaders(response), body));
                throw new InvalidOperationException($"Status {status} raised no error");
            }
            var contentType = response.Content.Headers.ContentType?.ToString() ?? string.Empty;
            var content = await response.Content.ReadAsStreamAsync(deadline.Token).ConfigureAwait(false);
            Log(LogLevel.Debug, $"<- {auth.Method} {status} (streamed)");
            var download = new Download(contentType, new DeadlineStream(content, response, deadline, cancellationToken));
            response = null;
            deadline = null;
            return new Opened(download, null);
        }
        catch (Exception error) when (error is OperationCanceledException or HttpRequestException or IOException && !cancellationToken.IsCancellationRequested)
        {
            throw Translate(error, deadline!);
        }
        finally
        {
            response?.Dispose();
            deadline?.Dispose();
        }
    }

    /// <summary>Whether a request with no body still carries empty content, so <c>Content-Length: 0</c>, as every write does.</summary>
    public static bool SendsEmptyContent(string method) => method != "GET";

    private static HttpRequestMessage Message(AuthRequest auth, Stream? stream)
    {
        var method = auth.Method;
        var request = new HttpRequestMessage(new HttpMethod(method), auth.Url);
        if (stream is not null)
        {
            request.Content = new StreamBody(stream);
            request.Headers.ExpectContinue = false;
        }
        else if (auth.Body.Length > 0 || SendsEmptyContent(method))
        {
            // The HTTP/1.1 handler resends a request when a reused connection closes before any response, but only
            // one with no content or with Expect: 100-continue. A write has neither, so it can reuse connections.
            request.Content = new ByteArrayContent(auth.Body.ToArray());
            request.Headers.ExpectContinue = false;
        }
        foreach (var (name, value) in auth.Headers)
        {
            if (!request.Headers.TryAddWithoutValidation(name, value))
            {
                request.Content ??= new ByteArrayContent([]);
                request.Content.Headers.TryAddWithoutValidation(name, value);
            }
        }
        return request;
    }

    private static ApiException Translate(Exception error, CancellationTokenSource deadline)
    {
        if (deadline.IsCancellationRequested || error.InnerException is TimeoutException)
        {
            return new ApiTimeoutException("The request timed out", error);
        }
        return new ApiConnectionException($"The connection failed: {error.GetType().Name}", error);
    }

    private static Dictionary<string, string> ResponseHeaders(HttpResponseMessage response)
    {
        var headers = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        foreach (var (name, value) in response.Headers.NonValidated.Concat(response.Content.Headers.NonValidated))
        {
            headers[name] = value.ToString();
        }
        return headers;
    }

    private Reply Read(string method, RawReply raw)
    {
        var success = raw.Status is >= 200 and < 300;
        var body = raw.Body;
        if (body.Length > 0 && raw.Headers.TryGetValue("Content-Encoding", out var encoding) && encoding.Trim().Equals("gzip", StringComparison.OrdinalIgnoreCase))
        {
            try
            {
                using var input = new GZipStream(new MemoryStream(body), CompressionMode.Decompress);
                using var output = new MemoryStream();
                input.CopyTo(output);
                var decompressed = output.ToArray();
                if (!MatchesTrailer(body, decompressed))
                {
                    throw new InvalidDataException("The gzip body ends early");
                }
                body = decompressed;
            }
            catch (InvalidDataException error)
            {
                if (success)
                {
                    throw new ApiDecodeException("The response body could not be decompressed", error) { Status = raw.Status };
                }
                body = [];
            }
        }
        var text = Encoding.UTF8.GetString(body);
        Log(LogLevel.Debug, $"<- {method} {raw.Status} ({text.Length} chars)");
        if (!success)
        {
            var clean = Redact(text);
            throw settings.ToError(new ErrorContext(raw.Status, raw.Headers, clean, Json.TryParse(clean)));
        }
        if (text.Length == 0 || !(raw.Headers.TryGetValue("Content-Type", out var type) && type.Contains("json", StringComparison.OrdinalIgnoreCase)))
        {
            return new Reply(raw.Status, text, Redact(text), null);
        }
        return new Reply(raw.Status, text, Redact(text), Json.TryParse(text) ?? throw new ApiDecodeException("The response body is not valid JSON") { Status = raw.Status });
    }

    /// <summary>
    /// GZipStream accepts a body cut short, so check the last member's trailer: the CRC-32 and length of the output's tail.
    /// </summary>
    private static bool MatchesTrailer(byte[] compressed, byte[] output)
    {
        if (compressed.Length < 18)
        {
            return false;
        }
        var crc = BinaryPrimitives.ReadUInt32LittleEndian(compressed.AsSpan(^8));
        var size = BinaryPrimitives.ReadUInt32LittleEndian(compressed.AsSpan(^4));
        return size <= output.Length && Crc32(output.AsSpan(output.Length - (int)size)) == crc;
    }

    private static uint Crc32(ReadOnlySpan<byte> data)
    {
        var crc = uint.MaxValue;
        foreach (var value in data)
        {
            crc ^= value;
            for (var bit = 0; bit < 8; bit++)
            {
                crc = (crc >> 1) ^ (0xEDB88320u & (0u - (crc & 1)));
            }
        }
        return ~crc;
    }

    /// <summary>Longest first, so a secret that contains another is removed whole.</summary>
    private string Redact(string text)
    {
        foreach (var secret in settings.Credentials.Secrets().Where(secret => secret.Length > 0).Distinct().OrderByDescending(secret => secret.Length))
        {
            text = text.Replace(secret, Redacted, StringComparison.Ordinal);
        }
        return text;
    }

    private sealed record RawReply(int Status, Dictionary<string, string> Headers, byte[] Body);

    /// <summary>A download, or where a redirect points.</summary>
    private sealed record Opened(Download? Download, Uri? Location);

    // Text is returned as it is. Clean has the token removed, for exceptions.
    private sealed record Reply(int Status, string Text, string Clean, JsonElement? Json);
}
