using MercuryBanking.Runtime;

namespace MercuryBanking;

/// <summary>A response with an error status. Mercury declares no error body, so <see cref="ApiException.RawBody"/> holds it as text.</summary>
public class HttpException(string message) : ApiException(message)
{
}

/// <summary>HTTP 400.</summary>
public class BadRequestException(string message) : HttpException(message)
{
    public override string Kind => "bad_request";
}

/// <summary>HTTP 401: the token is missing, wrong or revoked.</summary>
public class AuthenticationException(string message) : HttpException(message)
{
    public override string Kind => "authentication";
}

/// <summary>HTTP 403: the token lacks the scope, or the request did not come from an allowed IP address.</summary>
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

    /// <summary>Maps on status alone.</summary>
    public static ApiException ToException(ErrorContext context)
    {
        Func<string, HttpException> create = ByStatus.TryGetValue(context.Status, out var known) ? known
            : context.Status >= 500 ? message => new ServerException(message)
            : message => new HttpException(message);
        var error = create($"HTTP {context.Status}");
        error.Status = context.Status;
        error.RawBody = context.Text;
        error.RetryAfter = context.Header("Retry-After");
        return error;
    }
}
