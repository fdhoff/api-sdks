using System.Collections.Concurrent;
using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using BackMarketSeller.Runtime;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class BinaryTests
{
    private static readonly byte[] NotUtf8 = [0x25, 0x50, 0x44, 0x46, 0x00, 0xff, 0xfe, 0x80, 0x0a, 0xc3, 0x28];

    private static readonly Operation DownloadFile = new(
        "download-file", "GET", "/download", "Files", "DownloadAsync", null, [], Security: [[new("key", [])]], ReturnsBinary: true);

    private static readonly Operation Upload = new(
        "upload-file", "POST", "/upload", "Files", "UploadAsync", null, [new("body", "body", ParamLocation.Raw)], ReturnsJson: true,
        Security: [[new("key", [])]], RawBodyType: "application/octet-stream");

    private static readonly Operation GetReport = new("get-report", "GET", "/report", "Files", "GetAsync", null, [], Security: [[new("key", [])]]);

    [Fact]
    public async Task ADownloadStreamsTheExactBytesWithTheirContentType()
    {
        using var rig = Rig.Create(_ => Bytes(NotUtf8, "application/pdf"));

        await using var download = await rig.Transport.DownloadAsync(DownloadFile, [], TestContext.Current.CancellationToken);

        Assert.Equal("application/pdf", download.ContentType);
        Assert.False(download.Content.CanSeek);
        Assert.Equal(NotUtf8, await download.ReadAllBytesAsync(TestContext.Current.CancellationToken));
        Assert.Equal("identity", Assert.Single(rig.Handler.Sent).Headers["Accept-Encoding"]);
    }

    [Fact]
    public async Task AnOperationThatIsNotBinaryStillAsksForGzip()
    {
        using var rig = Rig.Create(_ => Bytes(Encoding.UTF8.GetBytes("""{"id": 1}"""), "application/json"));

        await rig.Transport.CallAsync<JsonElement>(Upload, [(RawBody)new byte[] { 1 }], TestContext.Current.CancellationToken);

        Assert.Equal("gzip", Assert.Single(rig.Handler.Sent).Headers["Accept-Encoding"]);
    }

    [Fact]
    public async Task AnEmptyDownloadIsAnEmptyStream()
    {
        using var rig = Rig.Create(_ => new HttpResponseMessage(HttpStatusCode.OK) { Content = new ByteArrayContent([]) });

        using var download = await rig.Transport.DownloadAsync(DownloadFile, [], TestContext.Current.CancellationToken);

        Assert.Equal(string.Empty, download.ContentType);
        Assert.Empty(await download.ReadAllBytesAsync(TestContext.Current.CancellationToken));
    }

    [Fact]
    public async Task TheDeadlineKeepsRunningWhileTheDownloadIsRead()
    {
        using var rig = Rig.Create(_ => new HttpResponseMessage(HttpStatusCode.OK) { Content = new StreamContent(new Stalled()) }, TimeSpan.FromMilliseconds(200));

        using var download = await rig.Transport.DownloadAsync(DownloadFile, [], TestContext.Current.CancellationToken);

        await Assert.ThrowsAsync<ApiTimeoutException>(() => download.ReadAllBytesAsync(TestContext.Current.CancellationToken));
    }

    [Fact]
    public async Task AFailedDownloadIsATypedErrorReadAsText()
    {
        using var rig = Rig.Create(_ => new HttpResponseMessage(HttpStatusCode.NotFound) { Content = new StringContent("""{"message": "not found"}""", Encoding.UTF8, "application/json") });

        var error = await Assert.ThrowsAsync<ApiException>(() => rig.Transport.DownloadAsync(DownloadFile, [], TestContext.Current.CancellationToken));

        Assert.Equal(404, error.Status);
        Assert.Equal("""{"message": "not found"}""", error.RawBody);
    }

    [Fact]
    public async Task BytesAreUploadedUnchangedAndSentAgainAfterARateLimit()
    {
        using var rig = Rig.Create(request => request.Count == 1 ? RateLimited() : Bytes(Encoding.UTF8.GetBytes("""{"id": 1}"""), "application/json"), maxRetries: 1);

        var result = await rig.Transport.CallAsync<JsonElement>(Upload, [(RawBody)NotUtf8], TestContext.Current.CancellationToken);

        Assert.Equal(1, result.GetProperty("id").GetInt32());
        Assert.Equal(2, rig.Handler.Sent.Count);
        Assert.All(rig.Handler.Sent, sent =>
        {
            Assert.Equal(NotUtf8, sent.Body);
            Assert.Equal("application/octet-stream", sent.ContentType);
        });
        Assert.All(rig.Credentials.Seen, seen => Assert.Equal(NotUtf8, seen.Body.ToArray()));
    }

    [Fact]
    public async Task AStreamIsUploadedOnceAndARateLimitIsNotRetried()
    {
        using var rig = Rig.Create(_ => RateLimited(), maxRetries: 3);
        using var source = new MemoryStream(NotUtf8);

        var error = await Assert.ThrowsAsync<ApiException>(() => rig.Transport.CallAsync<JsonElement>(Upload, [(RawBody)source], TestContext.Current.CancellationToken));

        Assert.Equal(429, error.Status);
        var sent = Assert.Single(rig.Handler.Sent);
        Assert.Equal(NotUtf8, sent.Body);
        Assert.Equal("application/octet-stream", sent.ContentType);
        Assert.Empty(Assert.Single(rig.Credentials.Seen).Body.ToArray());
        Assert.True(source.CanRead);
    }

    [Fact]
    public async Task ATextResponseThatIsNotJsonIsReturnedAsText()
    {
        const string report = "id\tname\n1\tsynthetic\n";
        using var rig = Rig.Create(_ => Bytes(Encoding.UTF8.GetBytes(report), "text/tab-separated-values"));

        var text = await rig.Transport.CallAsync<string>(GetReport, [], TestContext.Current.CancellationToken);

        Assert.Equal(report, text);
    }

    private static HttpResponseMessage Bytes(byte[] body, string type) =>
        new(HttpStatusCode.OK) { Content = new ByteArrayContent(body) { Headers = { ContentType = MediaTypeHeaderValue.Parse(type) } } };

    private static HttpResponseMessage RateLimited() => new(HttpStatusCode.TooManyRequests) { Headers = { { "Retry-After", "0" } }, Content = new ByteArrayContent([]) };

    /// <summary>A body that never sends a byte.</summary>
    private sealed class Stalled : MemoryStream
    {
        public override async ValueTask<int> ReadAsync(Memory<byte> buffer, CancellationToken cancellationToken = default)
        {
            await Task.Delay(Timeout.Infinite, cancellationToken);
            return 0;
        }

        public override Task<int> ReadAsync(byte[] buffer, int offset, int count, CancellationToken cancellationToken) =>
            ReadAsync(buffer.AsMemory(offset, count), cancellationToken).AsTask();
    }

    private sealed class Rig : IDisposable
    {
        private Rig(Transport transport, Handler handler, Recorder credentials)
        {
            Transport = transport;
            Handler = handler;
            Credentials = credentials;
        }

        public Transport Transport { get; }

        public Handler Handler { get; }

        public Recorder Credentials { get; }

        public static Rig Create(Func<Request, HttpResponseMessage> respond, TimeSpan? timeout = null, int maxRetries = 0)
        {
            var handler = new Handler(respond);
            var credentials = new Recorder();
            var transport = new Transport(
                new Settings
                {
                    BaseUrl = "https://base.mock.invalid",
                    Credentials = credentials,
                    Headers = new Dictionary<string, string>(),
                    ToError = context => new ApiException($"status {context.Status}") { Status = context.Status, RawBody = context.Text },
                    Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
                    Timeout = timeout ?? TimeSpan.FromSeconds(30),
                    MaxRetries = maxRetries,
                },
                new HttpClient(handler),
                ownsClient: true);
            return new Rig(transport, handler, credentials);
        }

        public void Dispose() => Transport.Dispose();
    }

    private sealed class Recorder : ICredentialProvider
    {
        public ConcurrentQueue<AuthRequest> Seen { get; } = new();

        public ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken)
        {
            Seen.Enqueue(request);
            request.Headers["Authorization"] = "synthetic";
            return ValueTask.CompletedTask;
        }

        public IReadOnlyCollection<string> Secrets() => ["synthetic"];
    }

    private sealed record Request(int Count, Dictionary<string, string> Headers, byte[] Body, string? ContentType);

    private sealed class Handler(Func<Request, HttpResponseMessage> respond) : HttpMessageHandler
    {
        private int count;

        public ConcurrentQueue<Request> Sent { get; } = new();

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var headers = request.Headers.NonValidated.ToDictionary(header => header.Key, header => header.Value.ToString(), StringComparer.OrdinalIgnoreCase);
            var body = request.Content is null ? [] : await request.Content.ReadAsByteArrayAsync(cancellationToken);
            var sent = new Request(Interlocked.Increment(ref count), headers, body, request.Content?.Headers.ContentType?.ToString());
            Sent.Enqueue(sent);
            return respond(sent);
        }
    }
}
