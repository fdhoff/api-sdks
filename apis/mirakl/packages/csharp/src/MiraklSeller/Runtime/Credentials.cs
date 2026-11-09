namespace MiraklSeller.Runtime;

/// <summary>A security scheme an operation names, with the scopes it needs from it.</summary>
internal sealed record Scheme(string Name, string[] Scopes);

/// <summary>One attempt's request, as it will be sent. <see cref="Headers"/> may be changed; the rest is read-only.</summary>
internal sealed class AuthRequest
{
    public required string Method { get; init; }

    public required Uri Url { get; init; }

    /// <summary>Request and content headers alike, by name, ignoring case.</summary>
    public required Dictionary<string, string> Headers { get; init; }

    public required ReadOnlyMemory<byte> Body { get; init; }

    public required Operation Operation { get; init; }
}

/// <summary>
/// Supplies each request's credentials. <see cref="ApplyAsync"/> runs before every attempt, retries included, so it
/// can sign the final request. <see cref="Secrets"/> lists every value to keep out of logs and errors, and is read
/// again each time, so it may change. <see cref="RefreshAsync"/> runs after a 401, at most once per call and once at a
/// time per client, and returns whether to retry. <see cref="RefreshGroup"/> names the credential an operation sends,
/// where there is more than one: a call skips its own refresh only when another call refreshed the same group since it
/// sent it.
/// </summary>
internal interface ICredentialProvider
{
    ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken);

    IReadOnlyCollection<string> Secrets();

    ValueTask<bool> RefreshAsync(AuthRequest request, CancellationToken cancellationToken) => ValueTask.FromResult(false);

    string RefreshGroup(Operation operation) => string.Empty;
}

/// <summary>The same headers on every request.</summary>
internal sealed class StaticCredentials(IReadOnlyDictionary<string, string> headers, IReadOnlyCollection<string> secrets) : ICredentialProvider
{
    public ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken)
    {
        foreach (var (name, value) in headers)
        {
            request.Headers[name] = value;
        }
        return ValueTask.CompletedTask;
    }

    public IReadOnlyCollection<string> Secrets() => secrets;
}
