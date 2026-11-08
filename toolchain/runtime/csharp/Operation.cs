using System.Text.Json;
using Microsoft.Extensions.Logging;

namespace PackageNamespace.Runtime;

/// <summary>
/// Where a parameter goes. <see cref="Form"/> is a multipart part, <see cref="Urlencoded"/> a form-encoded field, and
/// <see cref="Header"/> a header that falls back to <see cref="Settings.HeaderDefaults"/>.
/// </summary>
internal enum ParamLocation
{
    Path,
    Query,
    Form,
    Urlencoded,
    Body,
    Header,
}

internal sealed record Param(string Wire, string Name, ParamLocation Location);

/// <summary>How an iterator walks pages: a <see cref="NextLinkPaging"/> or an <see cref="OffsetPaging"/>.</summary>
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

/// <remarks>
/// Any one requirement in <see cref="Security"/> authorizes the call; each lists schemes that must all be satisfied.
/// <see cref="Host"/> is a key in <see cref="Settings.Hosts"/>; without one the call goes to <see cref="Settings.BaseUrl"/>.
/// </remarks>
internal sealed record Operation(string Id, string Method, string Path, string Resource, string Name, string? Iterator, Param[] Params, bool ReturnsJson = false, Paging? Paging = null, Scheme[][]? Security = null, string? Host = null);

/// <summary>A failed response, with the credential already removed from <see cref="Text"/> and <see cref="Json"/>.</summary>
internal sealed record ErrorContext(int Status, IReadOnlyDictionary<string, string> Headers, string Text, JsonElement? Json)
{
    public string? Header(string name) => Headers.TryGetValue(name, out var value) ? value : null;
}

internal sealed class Settings
{
    public required string BaseUrl { get; init; }

    /// <summary>The base URL for each host key an operation may name.</summary>
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
                throw new ArgumentException($"The hosts lack: {string.Join(", ", missing)}", nameof(hosts));
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
