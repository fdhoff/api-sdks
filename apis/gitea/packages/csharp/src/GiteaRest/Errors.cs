using System.Text.Json;
using GiteaRest.Runtime;

namespace GiteaRest;

/// <summary>
/// A response with an error status. <see cref="Detail"/> holds the <c>message</c> of Gitea's JSON error body, and
/// <see cref="ApiException.RawBody"/> the body as text, with your credentials removed from both.
/// </summary>
public class HttpException(string message) : ApiException(message)
{
    /// <summary>The <c>message</c> of Gitea's JSON error body, when it has one.</summary>
    public string? Detail { get; internal set; }
}

/// <summary>HTTP 400.</summary>
public class BadRequestException(string message) : HttpException(message)
{
    public override string Kind => "bad_request";
}

/// <summary>HTTP 401: the credentials are missing or wrong, or a one-time password is needed.</summary>
public class AuthenticationException(string message) : HttpException(message)
{
    public override string Kind => "authentication";
}

/// <summary>HTTP 403: the credentials do not allow the call.</summary>
public class PermissionDeniedException(string message) : HttpException(message)
{
    public override string Kind => "permission";
}

/// <summary>HTTP 404. Gitea also answers 404 for a private repository the credentials cannot see.</summary>
public class NotFoundException(string message) : HttpException(message)
{
    public override string Kind => "not_found";
}

/// <summary>HTTP 409, such as for a repository or branch that already exists.</summary>
public class ConflictException(string message) : HttpException(message)
{
    public override string Kind => "conflict";
}

/// <summary>HTTP 422: Gitea refused the request's fields.</summary>
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

    /// <summary>Maps on status first, then reads the <c>message</c> of Gitea's JSON error body, when it has one.</summary>
    public static ApiException ToException(ErrorContext context)
    {
        Func<string, HttpException> create = ByStatus.TryGetValue(context.Status, out var known) ? known
            : context.Status >= 500 ? message => new ServerException(message)
            : message => new HttpException(message);
        var detail = context.Json is { ValueKind: JsonValueKind.Object } body
            && body.TryGetProperty("message", out var field) && field.ValueKind == JsonValueKind.String
            ? field.GetString()
            : null;
        var error = create(detail is null ? $"HTTP {context.Status}" : $"HTTP {context.Status}: {detail}");
        error.Status = context.Status;
        error.Detail = detail;
        error.RawBody = context.Text;
        error.RetryAfter = context.Header("Retry-After");
        return error;
    }
}
