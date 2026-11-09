namespace MiraklSeller;

/// <summary>
/// A binary response. <see cref="Content"/> streams the body as received, and the call's timeout keeps running while
/// it is read, so it must cover the whole transfer. Dispose it to release the connection.
/// </summary>
public sealed class Download : IDisposable, IAsyncDisposable
{
    internal Download(string contentType, Stream content)
    {
        ContentType = contentType;
        Content = content;
    }

    /// <summary>The response's <c>Content-Type</c>, or empty if it has none.</summary>
    public string ContentType { get; }

    /// <summary>The body. Reading past the timeout throws <see cref="ApiTimeoutException"/>, and a dropped connection <see cref="ApiConnectionException"/>.</summary>
    public Stream Content { get; }

    /// <summary>Reads the whole body into memory.</summary>
    public async Task<byte[]> ReadAllBytesAsync(CancellationToken cancellationToken = default)
    {
        using var buffer = new MemoryStream();
        await Content.CopyToAsync(buffer, cancellationToken).ConfigureAwait(false);
        return buffer.ToArray();
    }

    public void Dispose() => Content.Dispose();

    public ValueTask DisposeAsync() => Content.DisposeAsync();
}

/// <summary>
/// A raw request body, sent unchanged. Bytes can be sent again, so a call that sends them is retried as usual. A
/// stream is sent once and never disposed by the client: a failure that would resend it throws instead, and the
/// credential provider sees an empty body.
/// </summary>
public sealed class RawBody
{
    private RawBody(byte[]? bytes, Stream? stream)
    {
        Bytes = bytes;
        Stream = stream;
    }

    internal byte[]? Bytes { get; }

    internal Stream? Stream { get; }

    public static RawBody FromBytes(byte[] bytes) => new(bytes ?? throw new ArgumentNullException(nameof(bytes)), null);

    public static RawBody FromStream(Stream stream) => new(null, stream ?? throw new ArgumentNullException(nameof(stream)));

    public static implicit operator RawBody(byte[] bytes) => FromBytes(bytes);

    public static implicit operator RawBody(Stream stream) => FromStream(stream);
}
