using System.Text.Json;
using EbaySell.Runtime;

namespace EbaySell;

/// <summary>One entry of an eBay error response's <c>errors</c> list.</summary>
/// <param name="ErrorId">The entry's <c>errorId</c>, when it has one.</param>
/// <param name="Domain">The system that raised the error, such as <c>API_FULFILLMENT</c>.</param>
/// <param name="Subdomain">The part of that system.</param>
/// <param name="Category"><c>REQUEST</c>, <c>APPLICATION</c> or <c>BUSINESS</c>.</param>
/// <param name="Message">A short description.</param>
/// <param name="LongMessage">A longer description.</param>
/// <param name="Parameters">The entry's <c>parameters</c>, by name and value.</param>
public sealed record EbayErrorDetail(
    long? ErrorId, string? Domain, string? Subdomain, string? Category, string? Message, string? LongMessage, IReadOnlyList<KeyValuePair<string?, string?>> Parameters);

/// <summary>
/// A response with an error status. <see cref="ApiException.Code"/> and <see cref="Detail"/> are the <c>errorId</c> and
/// <c>message</c> of the first entry of the body's <c>errors</c> list, when it has one.
/// </summary>
public class HttpException(string message) : ApiException(message)
{
    /// <summary>The first error's <c>message</c>, with your credentials removed.</summary>
    public string? Detail { get; internal set; }

    /// <summary>The body's whole <c>errors</c> list, read best-effort: an entry that is not an object is skipped, and a field of the wrong type is null.</summary>
    public IReadOnlyList<EbayErrorDetail> Errors { get; internal set; } = [];
}

/// <summary>HTTP 400.</summary>
public class BadRequestException(string message) : HttpException(message)
{
    public override string Kind => "bad_request";
}

/// <summary>HTTP 401, after any new application token or refreshed user token.</summary>
public class AuthenticationException(string message) : HttpException(message)
{
    public override string Kind => "authentication";
}

/// <summary>HTTP 403.</summary>
public class PermissionDeniedException(string message) : HttpException(message)
{
    public override string Kind => "permission";
}

/// <summary>HTTP 404.</summary>
public class NotFoundException(string message) : HttpException(message)
{
    public override string Kind => "not_found";
}

/// <summary>HTTP 409.</summary>
public class ConflictException(string message) : HttpException(message)
{
    public override string Kind => "conflict";
}

/// <summary>HTTP 422.</summary>
public class UnprocessableException(string message) : HttpException(message)
{
    public override string Kind => "validation";
}

/// <summary>HTTP 429, after retries. <see cref="ApiException.RetryAfter"/> says when to try again.</summary>
public class RateLimitedException(string message) : HttpException(message)
{
    public override string Kind => "rate_limited";
}

/// <summary>HTTP 5xx, after retries.</summary>
public class ServerException(string message) : HttpException(message)
{
    public override string Kind => "server";
}

internal static class Errors
{
    private static readonly Dictionary<int, Func<string, HttpException>> ByStatus = new()
    {
        [400] = message => new BadRequestException(message),
        [401] = message => new AuthenticationException(message),
        [403] = message => new PermissionDeniedException(message),
        [404] = message => new NotFoundException(message),
        [409] = message => new ConflictException(message),
        [422] = message => new UnprocessableException(message),
        [429] = message => new RateLimitedException(message),
    };

    /// <summary>Maps on status first, then reads the body best-effort.</summary>
    public static ApiException ToException(ErrorContext context)
    {
        var details = Details(context.Json);
        var first = details.Count > 0 ? details[0] : null;
        Func<string, HttpException> create = ByStatus.TryGetValue(context.Status, out var known) ? known
            : context.Status >= 500 ? message => new ServerException(message)
            : message => new HttpException(message);
        var error = create($"HTTP {context.Status}" + (string.IsNullOrEmpty(first?.Message) ? string.Empty : $": {first.Message}"));
        error.Status = context.Status;
        error.RawBody = context.Text;
        error.Code = first?.ErrorId?.ToString(System.Globalization.CultureInfo.InvariantCulture);
        error.Detail = string.IsNullOrEmpty(first?.Message) ? null : first.Message;
        error.Errors = details;
        error.RetryAfter = context.Header("Retry-After");
        return error;
    }

    private static List<EbayErrorDetail> Details(JsonElement? body)
    {
        if (body is not { ValueKind: JsonValueKind.Object } json || !json.TryGetProperty("errors", out var list) || list.ValueKind != JsonValueKind.Array)
        {
            return [];
        }
        return [.. list.EnumerateArray().Where(entry => entry.ValueKind == JsonValueKind.Object).Select(Detail)];
    }

    private static EbayErrorDetail Detail(JsonElement entry)
    {
        var parameters = entry.TryGetProperty("parameters", out var list) && list.ValueKind == JsonValueKind.Array
            ? list.EnumerateArray().Where(item => item.ValueKind == JsonValueKind.Object).Select(item => KeyValuePair.Create(Text(item, "name"), Text(item, "value"))).ToList()
            : [];
        long? id = entry.TryGetProperty("errorId", out var value) && value.ValueKind == JsonValueKind.Number && value.TryGetInt64(out var number) ? number : null;
        return new EbayErrorDetail(id, Text(entry, "domain"), Text(entry, "subdomain"), Text(entry, "category"), Text(entry, "message"), Text(entry, "longMessage"), parameters);
    }

    private static string? Text(JsonElement entry, string name) =>
        entry.TryGetProperty(name, out var value) && value.ValueKind == JsonValueKind.String ? value.GetString() : null;
}
