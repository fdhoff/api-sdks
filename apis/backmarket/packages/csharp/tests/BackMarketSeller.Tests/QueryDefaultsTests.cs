using System.Collections.Concurrent;
using System.Net;
using System.Text;
using System.Text.Json;
using BackMarketSeller.Runtime;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class QueryDefaultsTests
{
    private static readonly Operation GetItem = new(
        "get-item", "GET", "/items/{id}", "Items", "GetAsync", null,
        [new("id", "id", ParamLocation.Path), new("site", "site", ParamLocation.Query, Defaulted: true)], ReturnsJson: true);

    private static readonly Operation ListItems = new(
        "list-items", "GET", "/items", "Items", "ListAsync", "ListAllAsync",
        [new("site", "site", ParamLocation.Query, Defaulted: true), new("after", "after", ParamLocation.Query)], ReturnsJson: true,
        Paging: new CursorPaging("results", "next", "after"));

    private static readonly Operation ListFiles = new(
        "list-files", "GET", "/files", "Files", "ListAsync", null, [new("site", "site", ParamLocation.Query)], ReturnsJson: true);

    private static readonly Dictionary<string, string> North = new() { ["site"] = "north" };

    [Fact]
    public async Task AQueryDefaultIsSentUnlessTheCallGivesAValue()
    {
        var (transport, sent) = Create(North);
        using var _ = transport;

        await transport.CallAsync<JsonElement>(GetItem, ["1", null], TestContext.Current.CancellationToken);
        await transport.CallAsync<JsonElement>(GetItem, ["1", "south"], TestContext.Current.CancellationToken);

        Assert.Equal(["https://base.mock.invalid/items/1?site=north", "https://base.mock.invalid/items/1?site=south"], sent);
    }

    [Fact]
    public async Task AQueryParameterWithNeitherAValueNorADefaultIsNotSent()
    {
        var (transport, sent) = Create(new Dictionary<string, string>());
        using var _ = transport;

        await transport.CallAsync<JsonElement>(GetItem, ["1", null], TestContext.Current.CancellationToken);

        Assert.Equal("https://base.mock.invalid/items/1", Assert.Single(sent));
    }

    [Fact]
    public async Task QueryDefaultNamesMatchExactly()
    {
        var (transport, sent) = Create(new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase) { ["Site"] = "north" });
        using var _ = transport;

        await transport.CallAsync<JsonElement>(GetItem, ["1", null], TestContext.Current.CancellationToken);

        Assert.Equal("https://base.mock.invalid/items/1", Assert.Single(sent));
    }

    [Fact]
    public async Task AQueryDefaultNeverReachesAParameterThatDoesNotTakeOne()
    {
        var (transport, sent) = Create(North);
        using var _ = transport;

        await transport.CallAsync<JsonElement>(ListFiles, [null], TestContext.Current.CancellationToken);

        Assert.Equal("https://base.mock.invalid/files", Assert.Single(sent));
    }

    [Fact]
    public async Task AnIteratorSendsTheQueryDefaultOnEveryPage()
    {
        var pages = new[] { """{"results": [{"id": 1}], "next": "b"}""", """{"results": [{"id": 2}], "next": null}""" };
        var (transport, sent) = Create(North, count => pages[count - 1]);
        using var _ = transport;

        var items = new List<JsonElement>();
        await foreach (var item in transport.PaginateAsync<JsonElement>(ListItems, [null, null], TestContext.Current.CancellationToken))
        {
            items.Add(item);
        }

        Assert.Equal(2, items.Count);
        Assert.Equal(["https://base.mock.invalid/items?site=north", "https://base.mock.invalid/items?site=north&after=b"], sent);
    }

    private static (Transport Transport, ConcurrentQueue<string> Sent) Create(Dictionary<string, string> queryDefaults, Func<int, string>? respond = null)
    {
        var handler = new Handler(respond ?? (_ => "{}"));
        var transport = new Transport(
            new Settings
            {
                BaseUrl = "https://base.mock.invalid",
                QueryDefaults = queryDefaults,
                Credentials = new Anonymous(),
                Headers = new Dictionary<string, string>(),
                ToError = context => new ApiException($"status {context.Status}") { Status = context.Status },
                Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
                MaxRetries = 0,
            },
            new HttpClient(handler),
            ownsClient: true);
        return (transport, handler.Sent);
    }

    private sealed class Anonymous : ICredentialProvider
    {
        public ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken) => ValueTask.CompletedTask;

        public IReadOnlyCollection<string> Secrets() => [];
    }

    private sealed class Handler(Func<int, string> respond) : HttpMessageHandler
    {
        private int count;

        public ConcurrentQueue<string> Sent { get; } = new();

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            Sent.Enqueue(request.RequestUri!.AbsoluteUri);
            var body = respond(Interlocked.Increment(ref count));
            return Task.FromResult(new HttpResponseMessage(HttpStatusCode.OK) { Content = new StringContent(body, Encoding.UTF8, "application/json") });
        }
    }
}
