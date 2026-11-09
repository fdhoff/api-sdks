using System.Net;

namespace EbaySell.Runtime;

/// <summary>Sends a caller's stream as it is read, and leaves it open.</summary>
internal sealed class StreamBody(Stream source) : HttpContent
{
    protected override Task SerializeToStreamAsync(Stream stream, TransportContext? context) => source.CopyToAsync(stream);

    protected override Task SerializeToStreamAsync(Stream stream, TransportContext? context, CancellationToken cancellationToken) =>
        source.CopyToAsync(stream, cancellationToken);

    protected override bool TryComputeLength(out long length)
    {
        length = source.CanSeek ? source.Length - source.Position : 0;
        return source.CanSeek;
    }
}

/// <summary>
/// A response body that keeps the attempt's deadline while it is read. It owns the response and the deadline, and
/// releases both when disposed.
/// </summary>
internal sealed class DeadlineStream(Stream inner, HttpResponseMessage response, CancellationTokenSource deadline, CancellationToken caller) : Stream
{
    public override bool CanRead => true;

    public override bool CanSeek => false;

    public override bool CanWrite => false;

    public override long Length => throw new NotSupportedException();

    public override long Position
    {
        get => throw new NotSupportedException();
        set => throw new NotSupportedException();
    }

    public override int Read(byte[] buffer, int offset, int count) =>
        ReadAsync(buffer.AsMemory(offset, count), CancellationToken.None).AsTask().GetAwaiter().GetResult();

    public override Task<int> ReadAsync(byte[] buffer, int offset, int count, CancellationToken cancellationToken) =>
        ReadAsync(buffer.AsMemory(offset, count), cancellationToken).AsTask();

    public override async ValueTask<int> ReadAsync(Memory<byte> buffer, CancellationToken cancellationToken = default)
    {
        using var linked = CancellationTokenSource.CreateLinkedTokenSource(deadline.Token, cancellationToken);
        try
        {
            return await inner.ReadAsync(buffer, linked.Token).ConfigureAwait(false);
        }
        catch (Exception error) when (error is OperationCanceledException or HttpRequestException or IOException
            && !cancellationToken.IsCancellationRequested && !caller.IsCancellationRequested)
        {
            if (deadline.IsCancellationRequested)
            {
                throw new ApiTimeoutException("The download timed out", error);
            }
            throw new ApiConnectionException($"The connection failed: {error.GetType().Name}", error);
        }
    }

    public override void Flush()
    {
    }

    public override long Seek(long offset, SeekOrigin origin) => throw new NotSupportedException();

    public override void SetLength(long value) => throw new NotSupportedException();

    public override void Write(byte[] buffer, int offset, int count) => throw new NotSupportedException();

    protected override void Dispose(bool disposing)
    {
        if (disposing)
        {
            inner.Dispose();
            response.Dispose();
            deadline.Dispose();
        }
        base.Dispose(disposing);
    }
}
