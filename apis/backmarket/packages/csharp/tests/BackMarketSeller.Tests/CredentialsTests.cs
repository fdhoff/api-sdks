using System.Collections.Concurrent;
using System.Net;
using System.Text;
using System.Text.Json;
using BackMarketSeller.Runtime;
using Microsoft.Extensions.Logging;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class CredentialsTests
{
    private const string Key = "synthetic-key";
    private const string Shared = "synthetic-shared-secret";

    private static readonly Operation GetItem = new(
        "get-item", "GET", "/items/{id}", "Items", "GetAsync", null, [new("id", "id", ParamLocation.Path)], ReturnsJson: true,
        Security: [[new("key", []), new("user", ["items_r"])]]);

    private static readonly Operation Upload = new(
        "upload", "POST", "/files", "Files", "UploadAsync", null, [new("file", "file", ParamLocation.Form)], Security: [[new("key", [])]]);

    [Fact]
    public async Task ApplySeesTheFinalRequestOnEveryAttempt()
    {
        var credentials = new Tokens();
        var handler = new Handler(request => request.Count == 1 ? new HttpResponseMessage(HttpStatusCode.ServiceUnavailable) : Ok());
        using var transport = TransportFor(credentials, handler);

        await transport.CallAsync<JsonElement>(GetItem, ["a b"], TestContext.Current.CancellationToken);

        Assert.Equal(2, credentials.Seen.Count);
        var first = credentials.Seen.First();
        Assert.Equal("GET", first.Method);
        Assert.Equal("https://mock.invalid/items/a%20b", first.Url.AbsoluteUri);
        Assert.True(first.Body.IsEmpty);
        Assert.Equal("test", first.Headers["user-agent"]);
        Assert.Same(GetItem, first.Operation);
        Assert.All(handler.Sent, sent => Assert.Equal("Bearer synthetic-access-1", sent.Headers["Authorization"]));
        Assert.All(handler.Sent, sent => Assert.Equal($"{Key}:{Shared}", sent.Headers["x-api-key"]));
    }

    [Fact]
    public async Task ApplyGetsTheMultipartBytesThatAreSent()
    {
        var credentials = new Tokens();
        var handler = new Handler(_ => Ok());
        using var transport = TransportFor(credentials, handler);

        await transport.CallAsync<JsonElement>(Upload, [new UploadFile("a.txt", Encoding.UTF8.GetBytes("hello"))], TestContext.Current.CancellationToken);

        var seen = Assert.Single(credentials.Seen);
        var sent = Assert.Single(handler.Sent);
        Assert.Equal(seen.Body.ToArray(), sent.Body);
        Assert.Contains("hello", Encoding.UTF8.GetString(sent.Body), StringComparison.Ordinal);
        Assert.Equal(seen.Headers["Content-Type"], sent.Headers["Content-Type"]);
        Assert.False(sent.Headers.ContainsKey("Authorization"));
    }

    [Fact]
    public async Task A401RefreshesOnceAndRetriesOnce()
    {
        var credentials = new Tokens();
        using (var transport = TransportFor(credentials, Accepts("synthetic-access-2")))
        {
            await transport.CallAsync<JsonElement>(GetItem, [1], TestContext.Current.CancellationToken);
        }
        Assert.Equal(1, credentials.Refreshes);

        var stale = new Tokens();
        using var failing = TransportFor(stale, Accepts("never"));
        var error = await Assert.ThrowsAnyAsync<ApiException>(() => failing.CallAsync<JsonElement>(GetItem, [1], TestContext.Current.CancellationToken));
        Assert.Equal(401, error.Status);
        Assert.Equal(1, stale.Refreshes);
        Assert.Equal(2, stale.Seen.Count);
    }

    [Fact]
    public async Task A401IsFinalWhenTheCredentialsCannotRefresh()
    {
        var handler = new Handler(_ => new HttpResponseMessage(HttpStatusCode.Unauthorized));
        var credentials = new StaticCredentials(new Dictionary<string, string> { ["Authorization"] = "Basic synthetic" }, ["synthetic"]);
        using var transport = TransportFor(credentials, handler);

        await Assert.ThrowsAnyAsync<ApiException>(() => transport.CallAsync<JsonElement>(GetItem, [1], TestContext.Current.CancellationToken));

        Assert.Single(handler.Sent);
    }

    [Fact]
    public async Task ConcurrentCallsShareOneRefresh()
    {
        var credentials = new Tokens();
        using var transport = TransportFor(credentials, Accepts("synthetic-access-2"));

        await Task.WhenAll(Enumerable.Range(0, 4).Select(id => transport.CallAsync<JsonElement>(GetItem, [id], TestContext.Current.CancellationToken)));

        Assert.Equal(1, credentials.Refreshes);
    }

    [Fact]
    public async Task EverySecretIsKeptOutOfErrorsAndLogs()
    {
        var credentials = new Tokens();
        var logs = new Lines();
        var body = $"bad {Key}:{Shared} and synthetic-access-1 and synthetic-refresh";
        var handler = new Handler(_ => new HttpResponseMessage(HttpStatusCode.BadRequest) { Content = new StringContent(body) });
        using var transport = TransportFor(credentials, handler, logs);

        var error = await Assert.ThrowsAnyAsync<ApiException>(() => transport.CallAsync<JsonElement>(GetItem, [Shared], TestContext.Current.CancellationToken));

        Assert.Equal("bad ***:*** and *** and ***", error.RawBody);
        var output = $"{error.Message} {error.RawBody} {string.Join(' ', logs.All)}";
        Assert.All(credentials.Secrets(), secret => Assert.DoesNotContain(secret, output, StringComparison.Ordinal));
    }

    private static Transport TransportFor(ICredentialProvider credentials, Handler handler, ILogger? logger = null) =>
        new(
            new Settings
            {
                BaseUrl = "https://mock.invalid",
                Credentials = credentials,
                Headers = new Dictionary<string, string> { ["User-Agent"] = "test" },
                ToError = context => new ApiException($"status {context.Status}: {context.Text}") { Status = context.Status, RawBody = context.Text },
                Logger = logger ?? Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
                MaxRetries = 1,
                RetryBaseDelay = TimeSpan.FromMilliseconds(1),
            },
            new HttpClient(handler),
            ownsClient: true);

    private static HttpResponseMessage Ok() => new(HttpStatusCode.OK) { Content = new StringContent("""{"id": 1}""", Encoding.UTF8, "application/json") };

    private static Handler Accepts(string token) =>
        new(request => request.Headers.TryGetValue("Authorization", out var sent) && sent == $"Bearer {token}" ? Ok() : new HttpResponseMessage(HttpStatusCode.Unauthorized));

    /// <summary>A synthetic bearer token that changes on each refresh, beside a fixed key.</summary>
    private sealed class Tokens : ICredentialProvider
    {
        private int version = 1;
        private int refreshes;

        public ConcurrentQueue<AuthRequest> Seen { get; } = new();

        public int Refreshes => refreshes;

        private string Token => $"synthetic-access-{Volatile.Read(ref version)}";

        public ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken)
        {
            Seen.Enqueue(request);
            request.Headers["x-api-key"] = $"{Key}:{Shared}";
            if (request.Operation.Security?.Any(requirement => requirement.Any(scheme => scheme.Name == "user")) == true)
            {
                request.Headers["Authorization"] = $"Bearer {Token}";
            }
            return ValueTask.CompletedTask;
        }

        public IReadOnlyCollection<string> Secrets() => [Key, Shared, Token, "synthetic-refresh"];

        public async ValueTask<bool> RefreshAsync(AuthRequest request, CancellationToken cancellationToken)
        {
            Interlocked.Increment(ref refreshes);
            await Task.Delay(10, cancellationToken);
            Interlocked.Increment(ref version);
            return true;
        }
    }

    private sealed record Request(int Count, Dictionary<string, string> Headers, byte[] Body);

    private sealed class Handler(Func<Request, HttpResponseMessage> respond) : HttpMessageHandler
    {
        private int count;

        public ConcurrentQueue<Request> Sent { get; } = new();

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var headers = request.Headers.NonValidated.ToDictionary(header => header.Key, header => header.Value.ToString(), StringComparer.OrdinalIgnoreCase);
            var body = request.Content is null ? [] : await request.Content.ReadAsByteArrayAsync(cancellationToken);
            foreach (var header in request.Content?.Headers.NonValidated.ToArray() ?? [])
            {
                headers[header.Key] = header.Value.ToString();
            }
            var sent = new Request(Interlocked.Increment(ref count), headers, body);
            Sent.Enqueue(sent);
            return respond(sent);
        }
    }

    private sealed class Lines : ILogger
    {
        public ConcurrentQueue<string> All { get; } = new();

        public IDisposable? BeginScope<TState>(TState state)
            where TState : notnull => null;

        public bool IsEnabled(LogLevel logLevel) => true;

        public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception? exception, Func<TState, Exception?, string> formatter) =>
            All.Enqueue(formatter(state, exception));
    }
}
