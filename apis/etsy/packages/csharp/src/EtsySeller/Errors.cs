using System.Text.Json;
using EtsySeller.Runtime;

namespace EtsySeller;

/// <summary>A response with an error status. <see cref="Detail"/> is the <c>error</c> text of its body, when it has one.</summary>
public class HttpException(string message) : ApiException(message)
{
    /// <summary>The body's <c>error</c> text, with your credentials removed.</summary>
    public string? Detail { get; internal set; }
}

/// <summary>HTTP 400.</summary>
public class BadRequestException(string message) : HttpException(message)
{
    public override string Kind => "bad_request";
}

/// <summary>HTTP 401, after any refresh of the access token.</summary>
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
        var detail = context.Json is { ValueKind: JsonValueKind.Object } body && body.TryGetProperty("error", out var text) && text.ValueKind == JsonValueKind.String
            ? text.GetString()
            : null;
        Func<string, HttpException> create = ByStatus.TryGetValue(context.Status, out var known) ? known
            : context.Status >= 500 ? message => new ServerException(message)
            : message => new HttpException(message);
        var error = create($"HTTP {context.Status}" + (string.IsNullOrEmpty(detail) ? string.Empty : $": {detail}"));
        error.Status = context.Status;
        error.RawBody = context.Text;
        error.Detail = detail;
        error.RetryAfter = context.Header("Retry-After");
        return error;
    }
}
