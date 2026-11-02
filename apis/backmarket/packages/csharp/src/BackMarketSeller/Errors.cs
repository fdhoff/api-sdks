using System.Text.Json;
using BackMarketSeller.Runtime;

namespace BackMarketSeller;

/// <summary>HTTP 400.</summary>
public class BadRequestException(string message) : ApiException(message)
{
    public override string Kind => "bad_request";
}

/// <summary>HTTP 401.</summary>
public class AuthenticationException(string message) : ApiException(message)
{
    public override string Kind => "authentication";
}

/// <summary>HTTP 403 that is neither of the two below.</summary>
public class PermissionDeniedException(string message) : ApiException(message)
{
    public override string Kind => "permission";
}

/// <summary>HTTP 403 HTML block from the firewall. Give <see cref="ApiException.CfRay"/> to your seller contact.</summary>
public class WafBlockedException(string message) : PermissionDeniedException(message)
{
    public override string Kind => "waf_blocked";
}

/// <summary>HTTP 403 from bot management.</summary>
public class BotChallengeException(string message) : PermissionDeniedException(message)
{
    public override string Kind => "bot_challenge";
}

/// <summary>HTTP 404.</summary>
public class NotFoundException(string message) : ApiException(message)
{
    public override string Kind => "not_found";
}

/// <summary>HTTP 422.</summary>
public class UnprocessableException(string message) : ApiException(message)
{
    public override string Kind => "validation";
}

/// <summary>HTTP 429, after retries.</summary>
public class RateLimitedException(string message) : ApiException(message)
{
    public override string Kind => "rate_limited";
}

/// <summary>HTTP 5xx, after retries.</summary>
public class ServerException(string message) : ApiException(message)
{
    public override string Kind => "server";
}

internal static class Errors
{
    private const string BotChallengeCode = "bot-need-challenge";

    private static readonly Dictionary<int, Func<string, ApiException>> ByStatus = new()
    {
        [400] = message => new BadRequestException(message),
        [401] = message => new AuthenticationException(message),
        [404] = message => new NotFoundException(message),
        [422] = message => new UnprocessableException(message),
        [429] = message => new RateLimitedException(message),
    };

    /// <summary>Maps on status first, then reads the body best-effort.</summary>
    public static ApiException ToException(ErrorContext context)
    {
        var body = context.Json;
        var code = Code(body);
        var create = Create(context);
        var error = create($"HTTP {context.Status}" + (code is null ? string.Empty : $": {code}"));
        error.Status = context.Status;
        error.RawBody = context.Text;
        error.Code = code;
        error.RequestId = Property(body, "requestId") is { ValueKind: JsonValueKind.String } id ? id.GetString() : null;
        error.RetryAfter = context.Header("Retry-After");
        error.CfRay = context.Header("cf-ray");
        return error;
    }

    private static Func<string, ApiException> Create(ErrorContext context)
    {
        if (context.Status == 403)
        {
            if (FirstErrorCode(context.Json) == BotChallengeCode)
            {
                return message => new BotChallengeException(message);
            }
            if (!string.IsNullOrEmpty(context.Header("cf-ray")) && context.Json is null)
            {
                return message => new WafBlockedException(message);
            }
            return message => new PermissionDeniedException(message);
        }
        if (context.Status >= 500)
        {
            return message => new ServerException(message);
        }
        return ByStatus.TryGetValue(context.Status, out var create) ? create : message => new ApiException(message);
    }

    private static JsonElement? Property(JsonElement? node, string name) =>
        node is { ValueKind: JsonValueKind.Object } value && value.TryGetProperty(name, out var found) ? found : null;

    private static string? Text(JsonElement? value) => value switch
    {
        null or { ValueKind: JsonValueKind.Null } => null,
        { ValueKind: JsonValueKind.String } text => text.GetString(),
        { } other => other.GetRawText(),
    };

    private static string? FirstErrorCode(JsonElement? body) =>
        Property(body, "errors") is { ValueKind: JsonValueKind.Array } errors && errors.GetArrayLength() > 0
            ? Text(Property(errors[0], "code"))
            : null;

    private static string? Code(JsonElement? body) => Text(Property(Property(body, "error"), "code")) ?? FirstErrorCode(body);
}
