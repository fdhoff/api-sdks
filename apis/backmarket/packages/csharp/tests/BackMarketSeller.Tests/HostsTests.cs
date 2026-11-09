using System.Collections.Concurrent;
using System.Net;
using System.Text;
using System.Text.Json;
using BackMarketSeller.Runtime;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class HostsTests
{
    private static readonly Operation ListItems = new(
        "list-items", "GET", "/items", "Items", "ListAsync", "ListAllAsync",
        [new("offset", "offset", ParamLocation.Query), new("X-Tenant", "xTenant", ParamLocation.Header)], ReturnsJson: true,
        Paging: new OffsetPaging("results", "count", "offset"), Security: [[new("key", [])]]);

    private static readonly Operation ListFiles = new(
        "list-files", "GET", "/files", "Files", "ListAsync", "ListAllAsync", [new("offset", "offset", ParamLocation.Query)], ReturnsJson: true,
        Paging: new OffsetPaging("results", "count", "offset"), Security: [[new("key", [])]], Host: "files");

    private static readonly Operation Unrouted = new(
        "list-other", "GET", "/other", "Other", "ListAsync", null, [], ReturnsJson: true, Security: [[new("key", [])]], Host: "other");

    private static readonly Dictionary<string, string> Hosts = new()
    {
        ["main"] = "https://main.mock.invalid",
        ["files"] = "https://files.mock.invalid",
    };

    private static readonly Dictionary<string, IReadOnlyDictionary<string, string>> Environments = new()
    {
        ["production"] = new Dictionary<string, string> { ["main"] = "https://main.mock.invalid/", ["files"] = "https://files.mock.invalid" },
        ["sandbox"] = new Dictionary<string, string> { ["main"] = "https://main.sandbox.mock.invalid", ["files"] = "https://files.sandbox.mock.invalid" },
    };

    [Fact]
    public async Task AnOperationWithoutAHostKeyGoesToTheBaseUrl()
    {
        using var rig = Rig.Create();

        await rig.Transport.CallAsync<JsonElement>(ListItems, [null, null], TestContext.Current.CancellationToken);

        Assert.Equal("https://base.mock.invalid/items", Assert.Single(rig.Handler.Sent).Url);
    }

    [Fact]
    public async Task AnOperationWithAHostKeyGoesToThatHost()
    {
        using var rig = Rig.Create();

        await rig.Transport.CallAsync<JsonElement>(ListFiles, [null], TestContext.Current.CancellationToken);

        Assert.Equal("https://files.mock.invalid/files", Assert.Single(rig.Handler.Sent).Url);
        Assert.Equal("synthetic", Assert.Single(rig.Handler.Sent).Headers["Authorization"]);
        Assert.Single(rig.Credentials.Seen);
    }

    [Fact]
    public async Task AnIteratorReissuesEveryPageAgainstTheOperationsHost()
    {
        var pages = new[] { """{"count": 2, "results": [{"id": 1}]}""", """{"count": 2, "results": [{"id": 2}]}""" };
        using var rig = Rig.Create(request => Ok(pages[request.Count - 1]));

        var items = new List<JsonElement>();
        await foreach (var item in rig.Transport.PaginateAsync<JsonElement>(ListFiles, [null], TestContext.Current.CancellationToken))
        {
            items.Add(item);
        }

        Assert.Equal(2, items.Count);
        Assert.Equal(["https://files.mock.invalid/files", "https://files.mock.invalid/files?offset=1"], rig.Handler.Sent.Select(sent => sent.Url));
    }

    [Fact]
    public async Task AnUnknownHostKeyFailsBeforeCredentialsOrSending()
    {
        using var rig = Rig.Create();

        var error = await Assert.ThrowsAsync<InvalidOperationException>(() => rig.Transport.CallAsync<JsonElement>(Unrouted, [], TestContext.Current.CancellationToken));

        Assert.Contains("\"other\"", error.Message, StringComparison.Ordinal);
        Assert.Empty(rig.Credentials.Seen);
        Assert.Empty(rig.Handler.Sent);
    }

    [Fact]
    public void SelectHostsPicksTheNamedEnvironment()
    {
        var hosts = HostMap.Select(Environments, "production");

        Assert.Equal("https://main.mock.invalid", hosts["main"]);
        Assert.Equal("https://files.sandbox.mock.invalid", HostMap.Select(Environments, "sandbox")["files"]);
    }

    [Fact]
    public void SelectHostsRejectsAnUnknownEnvironment()
    {
        var error = Assert.Throws<ArgumentException>(() => HostMap.Select(Environments, "staging"));

        Assert.Contains("\"staging\"", error.Message, StringComparison.Ordinal);
        Assert.Contains("production, sandbox", error.Message, StringComparison.Ordinal);
    }

    [Fact]
    public void SelectHostsTakesTheCallersOwnMapWhenItNamesEveryKey()
    {
        var own = new Dictionary<string, string> { ["main"] = "http://127.0.0.1:1/", ["files"] = "http://127.0.0.1:2" };

        var hosts = HostMap.Select(Environments, "production", own);

        Assert.Equal("http://127.0.0.1:1", hosts["main"]);
        Assert.Equal("http://127.0.0.1:2", hosts["files"]);
    }

    [Fact]
    public void SelectHostsRejectsACallersMapWithMissingOrUnknownKeys()
    {
        var missing = Assert.Throws<ArgumentException>(() => HostMap.Select(Environments, "production", new Dictionary<string, string> { ["main"] = "http://a" }));
        Assert.Contains("lack keys: files", missing.Message, StringComparison.Ordinal);

        var extra = new Dictionary<string, string> { ["main"] = "http://a", ["files"] = "http://b", ["zeta"] = "http://c", ["alpha"] = "http://d" };
        var unknown = Assert.Throws<ArgumentException>(() => HostMap.Select(Environments, "production", extra));
        Assert.Contains("unknown keys: alpha, zeta", unknown.Message, StringComparison.Ordinal);
    }

    [Fact]
    public async Task AHeaderDefaultIsSentUnderTheDeclaredNameAndReplacesAClientWideHeader()
    {
        var defaults = new Dictionary<string, string> { ["x-tenant"] = "acme" };
        using var rig = Rig.Create(headerDefaults: defaults, headers: new Dictionary<string, string> { ["X-TENANT"] = "client-wide" });

        await rig.Transport.CallAsync<JsonElement>(ListItems, [null, null], TestContext.Current.CancellationToken);

        Assert.Equal("acme", Assert.Single(rig.Handler.Sent).Headers["X-Tenant"]);
        var seen = Assert.Single(rig.Credentials.Seen);
        Assert.Contains("X-Tenant", seen.Headers.Keys);
        Assert.DoesNotContain("X-TENANT", seen.Headers.Keys);
    }

    [Fact]
    public async Task AValuePassedToTheCallOverridesTheDefault()
    {
        using var rig = Rig.Create(headerDefaults: new Dictionary<string, string> { ["X-Tenant"] = "acme" });

        await rig.Transport.CallAsync<JsonElement>(ListItems, [null, "other"], TestContext.Current.CancellationToken);

        Assert.Equal("other", Assert.Single(rig.Handler.Sent).Headers["X-Tenant"]);
    }

    [Fact]
    public async Task ADefaultNeverReachesAnOperationThatDoesNotDeclareTheHeader()
    {
        using var rig = Rig.Create(headerDefaults: new Dictionary<string, string> { ["X-Tenant"] = "acme" });

        await rig.Transport.CallAsync<JsonElement>(ListFiles, [null], TestContext.Current.CancellationToken);

        Assert.False(Assert.Single(rig.Handler.Sent).Headers.ContainsKey("X-Tenant"));
    }

    [Fact]
    public void HeaderDefaultsThatDifferOnlyByCaseAreRejectedAtConstruction()
    {
        var defaults = new Dictionary<string, string> { ["x-tenant"] = "acme", ["X-Tenant"] = "other", ["X-Other"] = "unused" };
        var handler = new Handler(_ => Ok("{}"));

        var error = Assert.Throws<ArgumentException>(() => Rig.Create(headerDefaults: defaults, handler: handler));

        Assert.StartsWith("HeaderDefaults has names that differ only by case: X-Tenant, x-tenant", error.Message, StringComparison.Ordinal);
        Assert.True(handler.Disposed);
    }

    [Fact]
    public async Task TheHeaderIsAbsentWithNeitherAValueNorADefault()
    {
        using var rig = Rig.Create();

        await rig.Transport.CallAsync<JsonElement>(ListItems, [null, null], TestContext.Current.CancellationToken);

        Assert.False(Assert.Single(rig.Handler.Sent).Headers.ContainsKey("X-Tenant"));
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

        public static Rig Create(
            Func<Request, HttpResponseMessage>? respond = null,
            Dictionary<string, string>? headerDefaults = null,
            Dictionary<string, string>? headers = null,
            Handler? handler = null)
        {
            handler ??= new Handler(respond ?? (_ => Ok("""{"count": 0, "results": []}""")));
            var credentials = new Recorder();
            var transport = new Transport(
                new Settings
                {
                    BaseUrl = "https://base.mock.invalid",
                    Hosts = Hosts,
                    HeaderDefaults = headerDefaults ?? new Dictionary<string, string>(),
                    Credentials = credentials,
                    Headers = headers ?? new Dictionary<string, string>(),
                    ToError = context => new ApiException($"status {context.Status}") { Status = context.Status },
                    Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
                    MaxRetries = 0,
                },
                new HttpClient(handler),
                ownsClient: true);
            return new Rig(transport, handler, credentials);
        }

        public void Dispose() => Transport.Dispose();
    }

    private static HttpResponseMessage Ok(string body) => new(HttpStatusCode.OK) { Content = new StringContent(body, Encoding.UTF8, "application/json") };

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

    private sealed record Request(int Count, string Url, Dictionary<string, string> Headers);

    private sealed class Handler(Func<Request, HttpResponseMessage> respond) : HttpMessageHandler
    {
        private int count;

        public ConcurrentQueue<Request> Sent { get; } = new();

        public bool Disposed { get; private set; }

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var headers = request.Headers.NonValidated.ToDictionary(header => header.Key, header => header.Value.ToString(), StringComparer.OrdinalIgnoreCase);
            var sent = new Request(Interlocked.Increment(ref count), request.RequestUri!.AbsoluteUri, headers);
            Sent.Enqueue(sent);
            return Task.FromResult(respond(sent));
        }

        protected override void Dispose(bool disposing)
        {
            Disposed = true;
            base.Dispose(disposing);
        }
    }
}
