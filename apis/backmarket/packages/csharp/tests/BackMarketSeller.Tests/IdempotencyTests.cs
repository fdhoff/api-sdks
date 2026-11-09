using System.Collections.Concurrent;
using System.Net;
using System.Text;
using System.Text.Json;
using BackMarketSeller.Runtime;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class IdempotencyTests
{
    private static readonly Operation CreateTransfer = new(
        "create-transfer", "POST", "/transfers", "Transfers", "CreateAsync", null, [new("body", "body", ParamLocation.Body)], ReturnsJson: true,
        Security: [[new("key", [])]], IdempotencyKey: "idempotency_key");

    private static readonly Operation CreateItem = new(
        "create-item", "POST", "/items", "Items", "CreateAsync", null, [new("body", "body", ParamLocation.Body)], ReturnsJson: true,
        Security: [[new("key", [])]]);

    [Fact]
    public async Task AWriteThatSetsItsKeyIsRetriedAfterAServerErrorWithTheSameBody()
    {
        using var rig = Rig.Create(request => request.Count == 1 ? Status(HttpStatusCode.ServiceUnavailable) : Ok());
        var body = new Dictionary<string, object> { ["idempotency_key"] = "k-1", ["amount"] = 5 };

        var result = await rig.Transport.CallAsync<JsonElement>(CreateTransfer, [body], TestContext.Current.CancellationToken);

        Assert.Equal("t-1", result.GetProperty("id").GetString());
        Assert.Equal(2, rig.Handler.Sent.Count);
        var sent = rig.Handler.Sent.Select(request => request.Body).ToArray();
        Assert.Equal(sent[0], sent[1]);
        Assert.Equal("k-1", JsonDocument.Parse(sent[1]).RootElement.GetProperty("idempotency_key").GetString());
    }

    [Fact]
    public async Task AWriteThatSetsItsKeyIsRetriedAfterADroppedConnection()
    {
        using var rig = Rig.Create(request => request.Count == 1 ? throw new HttpRequestException("dropped") : Ok());
        var body = new Dictionary<string, object> { ["idempotency_key"] = "k-2", ["amount"] = 5 };

        await rig.Transport.CallAsync<JsonElement>(CreateTransfer, [body], TestContext.Current.CancellationToken);

        Assert.Equal(2, rig.Handler.Sent.Count);
    }

    [Fact]
    public async Task AWriteWithoutAnIdempotencyKeyIsNotRetried()
    {
        using var rig = Rig.Create(_ => Status(HttpStatusCode.ServiceUnavailable));
        var body = new Dictionary<string, object> { ["idempotency_key"] = "k-3", ["name"] = "widget" };

        var error = await Assert.ThrowsAsync<ApiException>(() => rig.Transport.CallAsync<JsonElement>(CreateItem, [body], TestContext.Current.CancellationToken));

        Assert.Equal(503, error.Status);
        Assert.Single(rig.Handler.Sent);
    }

    [Theory]
    [InlineData("""{"idempotency_key": "", "amount": 5}""")]
    [InlineData("""{"idempotency_key": null, "amount": 5}""")]
    [InlineData("""{"amount": 5}""")]
    public async Task AWriteThatLeavesItsKeyEmptyIsNotRetried(string json)
    {
        using var rig = Rig.Create(_ => Status(HttpStatusCode.ServiceUnavailable));

        var error = await Assert.ThrowsAsync<ApiException>(() => rig.Transport.CallAsync<JsonElement>(CreateTransfer, [JsonDocument.Parse(json).RootElement], TestContext.Current.CancellationToken));

        Assert.Equal(503, error.Status);
        Assert.Single(rig.Handler.Sent);
    }

    [Fact]
    public async Task AWriteThatLeavesItsKeyEmptyIsStillRetriedAfterARateLimit()
    {
        using var rig = Rig.Create(request => request.Count == 1 ? RateLimited() : Ok());

        await rig.Transport.CallAsync<JsonElement>(CreateTransfer, [new Dictionary<string, object> { ["amount"] = 5 }], TestContext.Current.CancellationToken);

        Assert.Equal(2, rig.Handler.Sent.Count);
    }

    private static HttpResponseMessage Ok() =>
        new(HttpStatusCode.OK) { Content = new StringContent("""{"id": "t-1"}""", Encoding.UTF8, "application/json") };

    private static HttpResponseMessage Status(HttpStatusCode status) => new(status) { Content = new ByteArrayContent([]) };

    private static HttpResponseMessage RateLimited() => new(HttpStatusCode.TooManyRequests) { Headers = { { "Retry-After", "0" } }, Content = new ByteArrayContent([]) };

    private sealed class Rig : IDisposable
    {
        private Rig(Transport transport, Handler handler)
        {
            Transport = transport;
            Handler = handler;
        }

        public Transport Transport { get; }

        public Handler Handler { get; }

        public static Rig Create(Func<Request, HttpResponseMessage> respond)
        {
            var handler = new Handler(respond);
            var transport = new Transport(
                new Settings
                {
                    BaseUrl = "https://base.mock.invalid",
                    Credentials = new Synthetic(),
                    Headers = new Dictionary<string, string>(),
                    ToError = context => new ApiException($"status {context.Status}") { Status = context.Status, RawBody = context.Text },
                    Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
                    MaxRetries = 2,
                    RetryBaseDelay = TimeSpan.FromMilliseconds(1),
                },
                new HttpClient(handler),
                ownsClient: true);
            return new Rig(transport, handler);
        }

        public void Dispose() => Transport.Dispose();
    }

    private sealed class Synthetic : ICredentialProvider
    {
        public ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken)
        {
            request.Headers["Authorization"] = "synthetic";
            return ValueTask.CompletedTask;
        }

        public IReadOnlyCollection<string> Secrets() => ["synthetic"];
    }

    private sealed record Request(int Count, byte[] Body);

    private sealed class Handler(Func<Request, HttpResponseMessage> respond) : HttpMessageHandler
    {
        private int count;

        public ConcurrentQueue<Request> Sent { get; } = new();

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var body = request.Content is null ? [] : await request.Content.ReadAsByteArrayAsync(cancellationToken);
            var sent = new Request(Interlocked.Increment(ref count), body);
            Sent.Enqueue(sent);
            return respond(sent);
        }
    }
}
