using MiraklSeller.Runtime;

namespace MiraklSeller;

/// <summary>
/// A response with an error status. Mirakl's docs define no error body, so <see cref="ApiException.RawBody"/> holds it
/// as text, with your key removed.
/// </summary>
public class HttpException(string message) : ApiException(message)
{
}

/// <summary>HTTP 400.</summary>
public class BadRequestException(string message) : HttpException(message)
{
    public override string Kind => "bad_request";
}

/// <summary>HTTP 401: the key is missing, wrong or revoked.</summary>
public class AuthenticationException(string message) : HttpException(message)
{
    public override string Kind => "authentication";
}

/// <summary>HTTP 403: the key's role does not allow the call, or the shop is not one the key covers.</summary>
public class PermissionDeniedException(string message) : HttpException(message)
{
    public override string Kind => "permission";
}

/// <summary>HTTP 404.</summary>
public class NotFoundException(string message) : HttpException(message)
{
    public override string Kind => "not_found";
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
