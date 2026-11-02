namespace PackageNamespace;

/// <summary>Base class for every error the client throws. Caller cancellation throws <see cref="OperationCanceledException"/> instead.</summary>
public class ApiException : Exception
{
    public ApiException(string message, Exception? innerException = null)
        : base(message, innerException)
    {
    }

    /// <summary>The class of failure, as named by the conformance cases.</summary>
    public virtual string Kind => "api";

    /// <summary>The HTTP status, when there was a response.</summary>
    public int? Status { get; internal set; }

    /// <summary>The response body, with your token removed.</summary>
    public string? RawBody { get; internal set; }

    /// <summary>The API's error code, from <c>error.code</c> or <c>errors[0].code</c>.</summary>
    public string? Code { get; internal set; }

    /// <summary>The API's <c>requestId</c>, when the body has one.</summary>
    public string? RequestId { get; internal set; }

    /// <summary>The <c>Retry-After</c> header as sent, so a caller can reschedule.</summary>
    public string? RetryAfter { get; internal set; }

    /// <summary>The <c>cf-ray</c> header, which support needs for a firewall block.</summary>
    public string? CfRay { get; internal set; }
}

/// <summary>No response arrived in time, after retries.</summary>
public class ApiTimeoutException(string message, Exception? innerException = null) : ApiException(message, innerException)
{
    public override string Kind => "timeout";
}

/// <summary>The connection failed or dropped before a full response, after retries.</summary>
public class ApiConnectionException(string message, Exception? innerException = null) : ApiException(message, innerException)
{
    public override string Kind => "connection";
}

/// <summary>A success response could not be read as the API declares it.</summary>
public class ApiDecodeException(string message, Exception? innerException = null) : ApiException(message, innerException)
{
    public override string Kind => "decode";
}
