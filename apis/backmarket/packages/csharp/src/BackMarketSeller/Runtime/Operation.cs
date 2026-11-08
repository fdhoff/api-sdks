using System.Text.Json;
using Microsoft.Extensions.Logging;

namespace BackMarketSeller.Runtime;

/// <summary>Where a parameter goes. <see cref="Form"/> is a multipart part, <see cref="Urlencoded"/> a form-encoded field.</summary>
internal enum ParamLocation
{
    Path,
    Query,
    Form,
    Urlencoded,
    Body,
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

/// <remarks>Any one requirement in <see cref="Security"/> authorizes the call; each lists schemes that must all be satisfied.</remarks>
internal sealed record Operation(string Id, string Method, string Path, string Resource, string Name, string? Iterator, Param[] Params, bool ReturnsJson = false, Paging? Paging = null, Scheme[][]? Security = null);

/// <summary>A failed response, with the credential already removed from <see cref="Text"/> and <see cref="Json"/>.</summary>
internal sealed record ErrorContext(int Status, IReadOnlyDictionary<string, string> Headers, string Text, JsonElement? Json)
{
    public string? Header(string name) => Headers.TryGetValue(name, out var value) ? value : null;
}

internal sealed class Settings
{
    public required string BaseUrl { get; init; }

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
