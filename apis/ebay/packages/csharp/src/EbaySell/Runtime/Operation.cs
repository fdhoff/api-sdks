using System.Text.Json;
using Microsoft.Extensions.Logging;

namespace EbaySell.Runtime;

/// <summary>
/// Where a parameter goes. <see cref="Form"/> is a multipart part, <see cref="Urlencoded"/> a form-encoded field,
/// <see cref="Header"/> a header that falls back to <see cref="Settings.HeaderDefaults"/>, and <see cref="Raw"/> a
/// <see cref="RawBody"/> sent as the whole body.
/// </summary>
internal enum ParamLocation
{
    Path,
    Query,
    Form,
    Urlencoded,
    Body,
    Header,
    Raw,
}

internal sealed record Param(string Wire, string Name, ParamLocation Location);

/// <summary>
/// How an iterator walks pages: a <see cref="NextLinkPaging"/>, an <see cref="OffsetPaging"/> or a <see cref="CursorPaging"/>.
/// </summary>
internal abstract record Paging(string Items);

/// <summary>Pages that link to the next one. Only <see cref="Params"/> are read from the link: it is never fetched.</summary>
internal sealed record NextLinkPaging(string Items, string Link, string[] Params) : Paging(Items)
{
    public static readonly NextLinkPaging Default = new("results", "next", ["page", "cursor"]);
}

/// <summary>
/// Pages addressed by an offset, which advances by the number of items received. Iteration ends at an empty page
/// or once the offset reaches the page's <see cref="Total"/>.
/// </summary>
internal sealed record OffsetPaging(string Items, string Total, string Offset) : Paging(Items);

/// <summary>
/// Pages that carry the next position as a value at the dotted <see cref="Next"/> path, sent back in the
/// <see cref="Param"/> query parameter. Iteration ends when that value is null, empty or absent.
/// </summary>
internal sealed record CursorPaging(string Items, string Next, string Param) : Paging(Items);

/// <summary>
/// How a wait polls an operation that reports an asynchronous job's progress. The job has ended once the string at the
/// dotted <see cref="State"/> path of its response is one of <see cref="Done"/> or <see cref="Failed"/>.
/// </summary>
internal sealed record JobPolling(string State, string[] Done, string[] Failed);

/// <remarks>
/// Any one requirement in <see cref="Security"/> authorizes the call; each lists schemes that must all be satisfied.
/// <see cref="Host"/> is a key in <see cref="Settings.Hosts"/>; without one the call goes to <see cref="Settings.BaseUrl"/>.
/// <see cref="ReturnsBinary"/> marks a success body that is a <see cref="Download"/>, which asks for the media types in
/// <see cref="Accept"/> instead of the client's default <c>Accept</c> header, and <see cref="RawBodyType"/> is the
/// media type of a <see cref="RawBody"/> request body. <see cref="IdempotencyKey"/> names the JSON body field the API
/// deduplicates a write by, so a write that sets it is retried as a GET is. <see cref="Job"/> is set when the operation
/// reports a job's progress, for a wait to poll.
/// </remarks>
internal sealed record Operation(string Id, string Method, string Path, string Resource, string Name, string? Iterator, Param[] Params, bool ReturnsJson = false, Paging? Paging = null, Scheme[][]? Security = null, string? Host = null, bool ReturnsBinary = false, string? RawBodyType = null, string? IdempotencyKey = null, string? Accept = null, JobPolling? Job = null);

/// <summary>A failed response, with the credential already removed from <see cref="Text"/> and <see cref="Json"/>.</summary>
internal sealed record ErrorContext(int Status, IReadOnlyDictionary<string, string> Headers, string Text, JsonElement? Json)
{
    public string? Header(string name) => Headers.TryGetValue(name, out var value) ? value : null;
}

internal sealed class Settings
{
    /// <summary>Where an operation with no host key is sent, without a trailing slash.</summary>
    public required string BaseUrl { get; init; }

    /// <summary>The base URL for each host key an operation may name, without a trailing slash, as <see cref="HostMap.Select"/> returns them.</summary>
    public IReadOnlyDictionary<string, string> Hosts { get; init; } = new Dictionary<string, string>();

    /// <summary>Values for header parameters a call leaves unset, by header name in any case.</summary>
    public IReadOnlyDictionary<string, string> HeaderDefaults { get; init; } = new Dictionary<string, string>();

    public required ICredentialProvider Credentials { get; init; }

    public required IReadOnlyDictionary<string, string> Headers { get; init; }

    public required Func<ErrorContext, ApiException> ToError { get; init; }

    public required ILogger Logger { get; init; }

    public TimeSpan Timeout { get; init; } = TimeSpan.FromSeconds(30);

    public int MaxRetries { get; init; } = 3;

    public TimeSpan RetryBaseDelay { get; init; } = TimeSpan.FromSeconds(0.5);

    public TimeSpan RateLimitWait { get; init; } = TimeSpan.FromSeconds(10);

    public TimeSpan MaxRetryWait { get; init; } = TimeSpan.FromSeconds(60);
}

/// <summary>Chooses the host map for a client from a package's named environments.</summary>
internal static class HostMap
{
    /// <summary>
    /// The caller's own <paramref name="hosts"/> when given, which must name exactly the keys the environments use,
    /// or else a copy of the named <paramref name="environment"/>. Trailing slashes are removed from every URL.
    /// </summary>
    public static IReadOnlyDictionary<string, string> Select(
        IReadOnlyDictionary<string, IReadOnlyDictionary<string, string>> environments,
        string environment,
        IReadOnlyDictionary<string, string>? hosts = null)
    {
        if (hosts is { Count: > 0 })
        {
            var keys = environments.Values.SelectMany(map => map.Keys).ToHashSet(StringComparer.Ordinal);
            var missing = keys.Where(key => !hosts.ContainsKey(key)).Order(StringComparer.Ordinal).ToArray();
            if (missing.Length > 0)
            {
                throw new ArgumentException($"The hosts lack keys: {string.Join(", ", missing)}", nameof(hosts));
            }
            var unknown = hosts.Keys.Where(key => !keys.Contains(key)).Order(StringComparer.Ordinal).ToArray();
            if (unknown.Length > 0)
            {
                throw new ArgumentException($"The hosts have unknown keys: {string.Join(", ", unknown)}", nameof(hosts));
            }
            return Trimmed(hosts);
        }
        if (!environments.TryGetValue(environment, out var chosen))
        {
            var known = string.Join(", ", environments.Keys.Order(StringComparer.Ordinal));
            throw new ArgumentException($"Unknown environment \"{environment}\"; expected one of: {known}", nameof(environment));
        }
        return Trimmed(chosen);
    }

    private static Dictionary<string, string> Trimmed(IReadOnlyDictionary<string, string> hosts) =>
        hosts.ToDictionary(pair => pair.Key, pair => pair.Value.TrimEnd('/'), StringComparer.Ordinal);
}
