using System.Collections;
using System.Globalization;
using System.IO.Compression;
using System.Net;
using System.Net.Http.Headers;
using System.Net.Sockets;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.Json;
using Microsoft.Extensions.Logging;
using PackageNamespace.Models;

namespace PackageNamespace.Runtime;

internal sealed class Transport : IDisposable
{
    private const string Redacted = "***";
    private static readonly string[] PageMarkers = ["page", "cursor"];
    private static readonly string[] HttpDates = ["r", "dddd, dd-MMM-yy HH:mm:ss 'GMT'", "ddd MMM d HH:mm:ss yyyy"];

    private static readonly HttpRequestOptionsKey<bool> Connected = new("Connected");

    private readonly Settings settings;
    private readonly HttpClient reads;
    private readonly HttpClient writes;

    /// <remarks>
    /// Writes use their own handler and close their connection, so a write never rides a pooled connection
    /// that the handler would silently resend it on.
    /// </remarks>
    public Transport(Settings settings, HttpMessageHandler? handler)
    {
        this.settings = settings;
        reads = handler is null ? new HttpClient(Sockets()) : new HttpClient(handler, disposeHandler: false);
        writes = handler is null ? new HttpClient(Sockets()) : reads;
        foreach (var http in Clients())
        {
            http.Timeout = System.Threading.Timeout.InfiniteTimeSpan;
            foreach (var (name, value) in settings.Headers)
            {
                http.DefaultRequestHeaders.TryAddWithoutValidation(name, value);
            }
            http.DefaultRequestHeaders.TryAddWithoutValidation("Accept-Encoding", "gzip");
        }
    }

    public void Dispose()
    {
        foreach (var http in Clients())
        {
            http.Dispose();
        }
    }

    private IEnumerable<HttpClient> Clients() => ReferenceEquals(reads, writes) ? [reads] : [reads, writes];

    private static SocketsHttpHandler Sockets() => new()
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

    public async Task<T> CallAsync<T>(Operation operation, object?[] values, CancellationToken cancellationToken)
    {
        var reply = await FetchAsync(operation, values, cancellationToken).ConfigureAwait(false);
        if (typeof(T) == typeof(string))
        {
            return (T)(object)(reply.Json is { ValueKind: JsonValueKind.String } text ? text.GetString()! : reply.Text);
        }
        if (reply.Json is { } json)
        {
            return Json.Read<T>(json, reply.Status, reply.Text);
        }
        if (reply.Text.Length == 0)
        {
            return Json.Empty<T>();
        }
        throw new ApiDecodeException($"The response is not JSON, so it cannot be a {typeof(T).Name}") { Status = reply.Status, RawBody = reply.Text };
    }

    public Task SendAsync(Operation operation, object?[] values, CancellationToken cancellationToken) =>
        FetchAsync(operation, values, cancellationToken);

    public async IAsyncEnumerable<T> PaginateAsync<T>(
        Operation operation, object?[] values, [EnumeratorCancellation] CancellationToken cancellationToken = default)
    {
        object?[]? current = values;
        while (current is not null)
        {
            var reply = await FetchAsync(operation, current, cancellationToken).ConfigureAwait(false);
            if (reply.Json is not { ValueKind: JsonValueKind.Object } page)
            {
                throw new ApiDecodeException("A page is not a JSON object") { Status = reply.Status, RawBody = reply.Text };
            }
            if (page.TryGetProperty("results", out var results) && results.ValueKind == JsonValueKind.Array)
            {
                foreach (var item in results.EnumerateArray())
                {
                    yield return Json.Read<T>(item, reply.Status, reply.Text);
                }
            }
            current = NextValues(operation, current, page);
        }
    }

    /// <summary>
    /// Reads the position out of <c>next</c> and applies it to our own request. <c>next</c> is never fetched:
    /// it could send the credential to another host.
    /// </summary>
    internal static object?[]? NextValues(Operation operation, object?[] values, JsonElement page)
    {
        if (!page.TryGetProperty("next", out var next) || next.ValueKind is JsonValueKind.Null or JsonValueKind.False)
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
            throw new ApiDecodeException("The `next` link is not a valid URL");
        }
        var position = QueryOf(link);
        var updated = (object?[])values.Clone();
        for (var index = 0; index < operation.Params.Length; index++)
        {
            var param = operation.Params[index];
            if (param.Location == ParamLocation.Query && PageMarkers.Contains(param.Wire) && position.TryGetValue(param.Wire, out var value))
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
            throw new ApiDecodeException("The `next` link does not advance the iteration");
        }
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
            var name = Unescape(parts[0]);
            query.TryAdd(name, parts.Length > 1 ? Unescape(parts[1]) : string.Empty);
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
        var styles = DateTimeStyles.AdjustToUniversal | DateTimeStyles.AssumeUniversal | DateTimeStyles.AllowInnerWhite;
        if (!DateTimeOffset.TryParseExact(value, HttpDates, CultureInfo.InvariantCulture, styles, out var when))
        {
            return null;
        }
        var wait = (when - now).TotalSeconds;
        return wait > 0 ? wait : null;
    }

    private static string Unescape(string text) => Uri.UnescapeDataString(text.Replace('+', ' '));

    private static string? TextOrNull(object? value) => value is null ? null : Json.Text(value);

    private static IEnumerable<object> Items(object value) =>
        value is IEnumerable items and not string and not byte[] ? items.Cast<object>() : [value];

    private static string Quote(string text) => $"\"{text.Replace("\"", "\\\"")}\"";

    private TimeSpan? RetryDelay(ApiException error, string method, int tries)
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
        return method == "GET" && failed ? settings.RetryBaseDelay * Math.Pow(2, tries) : null;
    }

    private void Log(LogLevel level, string message)
    {
        if (settings.Logger.IsEnabled(level))
        {
            settings.Logger.Log(level, "{Message}", message.Replace(settings.Secret, Redacted, StringComparison.Ordinal));
        }
    }

    private (Uri Url, Func<HttpContent?> Content) Build(Operation operation, object?[] values)
    {
        var path = operation.Path;
        var query = new List<string>();
        var parts = new List<(string Wire, object Value)>();
        object? body = null;
        for (var index = 0; index < operation.Params.Length; index++)
        {
            var param = operation.Params[index];
            var value = values[index];
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
                default:
                    body = value;
                    break;
            }
        }
        var url = new Uri($"{settings.BaseUrl}{path}{(query.Count > 0 ? "?" + string.Join('&', query) : string.Empty)}");
        if (parts.Count > 0)
        {
            return (url, () => Multipart(parts));
        }
        if (body is null)
        {
            return (url, () => null);
        }
        var bytes = JsonSerializer.SerializeToUtf8Bytes(body, body.GetType(), Json.Options);
        return (url, () => new ByteArrayContent(bytes) { Headers = { ContentType = new MediaTypeHeaderValue("application/json") } });
    }

    private static MultipartFormDataContent Multipart(List<(string Wire, object Value)> parts)
    {
        var form = new MultipartFormDataContent();
        foreach (var (wire, value) in parts)
        {
            if (value is UploadFile file)
            {
                form.Add(new ByteArrayContent(file.Content), Quote(wire), Quote(file.FileName));
                continue;
            }
            var text = value is ApiModel or IDictionary ? JsonSerializer.Serialize(value, value.GetType(), Json.Options) : Json.Text(value);
            var part = new StringContent(text);
            part.Headers.ContentType = null;
            form.Add(part, Quote(wire));
        }
        return form;
    }

    private async Task<Reply> FetchAsync(Operation operation, object?[] values, CancellationToken cancellationToken)
    {
        var (url, content) = Build(operation, values);
        for (var tries = 0; ; tries++)
        {
            Log(LogLevel.Debug, $"-> {operation.Method} {url}");
            try
            {
                var reply = await AttemptAsync(operation.Method, url, content, cancellationToken).ConfigureAwait(false);
                return Read(operation.Method, reply);
            }
            catch (ApiException error)
            {
                var delay = RetryDelay(error, operation.Method, tries);
                if (delay is null)
                {
                    throw;
                }
                Log(LogLevel.Information, $"retrying after {delay.Value.TotalSeconds}s: {error.Kind}");
                await Task.Delay(delay.Value, cancellationToken).ConfigureAwait(false);
            }
        }
    }

    /// <summary>One attempt, from sending the request to reading the last byte, under one deadline.</summary>
    private async Task<RawReply> AttemptAsync(string method, Uri url, Func<HttpContent?> content, CancellationToken cancellationToken)
    {
        using var deadline = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
        deadline.CancelAfter(settings.Timeout);
        using var request = new HttpRequestMessage(new HttpMethod(method), url) { Content = content() };
        var http = method == "GET" ? reads : writes;
        if (!ReferenceEquals(http, reads))
        {
            request.Headers.ConnectionClose = true;
        }
        try
        {
            using var response = await http.SendAsync(request, HttpCompletionOption.ResponseHeadersRead, deadline.Token).ConfigureAwait(false);
            var body = await response.Content.ReadAsByteArrayAsync(deadline.Token).ConfigureAwait(false);
            var headers = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            foreach (var (name, value) in response.Headers.NonValidated.Concat(response.Content.Headers.NonValidated))
            {
                headers[name] = value.ToString();
            }
            return new RawReply((int)response.StatusCode, headers, body);
        }
        catch (Exception error) when (error is OperationCanceledException or HttpRequestException or IOException && !cancellationToken.IsCancellationRequested)
        {
            if (deadline.IsCancellationRequested)
            {
                throw new ApiTimeoutException("The request timed out", error);
            }
            throw new ApiConnectionException($"The connection failed: {error.GetType().Name}", error);
        }
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
                body = output.ToArray();
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
        var text = Encoding.UTF8.GetString(body).Replace(settings.Secret, Redacted, StringComparison.Ordinal);
        Log(LogLevel.Debug, $"<- {method} {raw.Status} ({text.Length} chars)");
        if (!success)
        {
            throw settings.ToError(new ErrorContext(raw.Status, raw.Headers, text, Json.TryParse(text)));
        }
        if (text.Length == 0 || !(raw.Headers.TryGetValue("Content-Type", out var type) && type.Contains("json", StringComparison.OrdinalIgnoreCase)))
        {
            return new Reply(raw.Status, text, null);
        }
        return new Reply(raw.Status, text, Json.TryParse(text) ?? throw new ApiDecodeException("The response body is not valid JSON") { Status = raw.Status });
    }

    private sealed record RawReply(int Status, Dictionary<string, string> Headers, byte[] Body);

    private sealed record Reply(int Status, string Text, JsonElement? Json);
}
