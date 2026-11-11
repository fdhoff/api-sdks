using System.Collections.Concurrent;
using System.Net;
using System.Text;
using MiraklSeller.Models;
using MiraklSeller.Runtime;
using Microsoft.Extensions.Logging;
using Xunit;

namespace MiraklSeller.Tests;

public sealed class ClientTests
{
    private const string Base = "https://your-operator.mirakl.net";
    private const string Key = "synthetic-unit-shop-key";
    private const string Shop = """{"shop_id": 2001, "shop_name": "Synthetic shop"}""";

    private static CancellationToken Cancel => TestContext.Current.CancellationToken;

    private static MiraklClient Client(Router handler, long? shopId = null, ILogger? logger = null, string baseUrl = Base) =>
        new(baseUrl, Key, new MiraklClientOptions
        {
            ShopId = shopId,
            UserAgent = "synthetic-agent/1",
            Logger = logger,
            RetryBaseDelay = TimeSpan.FromMilliseconds(1),
            HttpHandler = handler,
        });

    [Fact]
    public void EveryOperationHasAPublicMethod()
    {
        foreach (var operation in ClientResources.Operations)
        {
            var resource = typeof(MiraklClient).GetProperty(operation.Resource);
            Assert.NotNull(resource);
            Assert.NotNull(resource.PropertyType.GetMethod(operation.Name));
            Assert.Contains(operation.Params, param => param.Wire == "shop_id" && param.Defaulted);
            if (operation.Iterator is not null)
            {
                Assert.NotNull(resource.PropertyType.GetMethod(operation.Iterator));
            }
        }
        Assert.Equal(117, ClientResources.Operations.Length);
        Assert.Equal(21, ClientResources.Operations.Count(operation => operation.Iterator is not null));
        Assert.Equal(
            ["OF02", "OF53", "OR14", "P42", "STO02", "TL04"],
            ClientResources.Operations.Where(operation => operation.Job is not null).Select(operation => operation.Id).Order(StringComparer.Ordinal));
    }

    [Fact]
    public async Task SendsTheKeyAsTheWholeAuthorizationHeaderToTheBaseUrl()
    {
        var handler = new Router(_ => Json(Shop));
        using var client = Client(handler, baseUrl: $"{Base}/");

        var shop = await client.Shop.GetAsync(cancellationToken: Cancel);

        var sent = Assert.Single(handler.Sent);
        Assert.Equal($"{Base}/api/account", sent.Url);
        Assert.Equal(Key, sent.Headers["Authorization"]);
        Assert.Equal("application/json", sent.Headers["Accept"]);
        Assert.Equal("synthetic-agent/1", sent.Headers["User-Agent"]);
        Assert.Equal(2001, shop.ShopId);
    }

    [Fact]
    public void RefusesAMissingOrNonHttpBaseUrlAndAnEmptyKey()
    {
        Assert.Throws<ArgumentException>(() => new MiraklClient(string.Empty, Key));
        Assert.Throws<ArgumentException>(() => new MiraklClient("your-operator.mirakl.net", Key));
        Assert.Throws<ArgumentException>(() => new MiraklClient("ftp://your-operator.mirakl.net", Key));
        Assert.Throws<ArgumentException>(() => new MiraklClient(Base, string.Empty));
    }

    [Fact]
    public async Task TheClientShopIdIsSentUnlessACallSetsItsOwn()
    {
        var handler = new Router(_ => Json(Shop));
        using var defaulted = Client(handler, shopId: 2001);
        using var plain = Client(handler);

        await defaulted.Shop.GetAsync(cancellationToken: Cancel);
        await defaulted.Shop.GetAsync(shopId: 2002, cancellationToken: Cancel);
        await plain.Shop.GetAsync(cancellationToken: Cancel);

        Assert.Equal(
            [$"{Base}/api/account?shop_id=2001", $"{Base}/api/account?shop_id=2002", $"{Base}/api/account"],
            handler.Sent.Select(sent => sent.Url));
    }

    [Fact]
    public async Task OffsetPagingKeepsTheShopIdOnEveryPageAndStopsAtTheTotal()
    {
        var handler = new Router(sent => Json(sent.Url.Contains("offset=1", StringComparison.Ordinal)
            ? """{"orders": [{"order_id": "order-2"}], "total_count": 2}"""
            : """{"orders": [{"order_id": "order-1"}], "total_count": 2}"""));
        using var client = Client(handler, shopId: 2001);

        var orders = await client.Orders.ListAllAsync(max: 1, cancellationToken: Cancel).ToListAsync(Cancel);

        Assert.Equal(["order-1", "order-2"], orders.Select(order => order.OrderId));
        Assert.Equal(2, handler.Sent.Count);
        Assert.All(handler.Sent, sent => Assert.Contains("shop_id=2001", sent.Url, StringComparison.Ordinal));
    }

    [Fact]
    public async Task SeekPagingSendsTheNextPageTokenBack()
    {
        var handler = new Router(sent => Json(sent.Url.Contains("page_token=token-2", StringComparison.Ordinal)
            ? """{"data": [{"id": "return-2"}], "next_page_token": null}"""
            : """{"data": [{"id": "return-1"}], "next_page_token": "token-2"}"""));
        using var client = Client(handler);

        var returns = await client.Returns.ListAllAsync(cancellationToken: Cancel).ToListAsync(Cancel);

        Assert.Equal(2, returns.Count);
        Assert.Equal($"{Base}/api/returns?page_token=token-2", handler.Sent.Last().Url);
    }

    [Fact]
    public async Task AWaitPollsUntilTheJobEndsAndReturnsAFailedStatus()
    {
        var calls = 0;
        var handler = new Router(_ => Json(++calls < 3 ? """{"import_id": 41, "status": "RUNNING"}""" : """{"import_id": 41, "status": "FAILED", "has_error_report": true}"""));
        using var client = Client(handler, shopId: 2001);

        var status = await client.Offers.WaitForImportAsync(41, interval: TimeSpan.Zero, cancellationToken: Cancel);

        Assert.Equal("FAILED", status.Status);
        Assert.True(status.HasErrorReport);
        Assert.Equal(3, handler.Sent.Count);
        Assert.All(handler.Sent, sent => Assert.Equal($"{Base}/api/offers/imports/41?shop_id=2001", sent.Url));
    }

    [Fact]
    public async Task AWaitThrowsAtTheDeadlineWithTheLastStatus()
    {
        var handler = new Router(_ => Json("""{"status": "PENDING"}"""));
        using var client = Client(handler);

        var error = await Assert.ThrowsAsync<ApiJobTimeoutException>(() => client.Orders.WaitForExportAsync("tracking-1", timeout: TimeSpan.Zero, cancellationToken: Cancel));

        Assert.Equal("job_timeout", error.Kind);
        Assert.Equal("PENDING", Assert.IsType<OR14Response200>(error.Result).Status);
    }

    [Fact]
    public async Task AWaitStopsWhenCancelled()
    {
        var handler = new Router(_ => Json("""{"status": "PENDING"}"""));
        using var client = Client(handler);
        using var cancel = CancellationTokenSource.CreateLinkedTokenSource(Cancel);
        cancel.CancelAfter(TimeSpan.FromMilliseconds(50));

        await Assert.ThrowsAnyAsync<OperationCanceledException>(() => client.Offers.WaitForExportAsync("tracking-1", interval: TimeSpan.FromMinutes(1), cancellationToken: cancel.Token));

        Assert.Single(handler.Sent);
    }

    [Fact]
    public async Task ADownloadSendsTheKeyOnlyToTheBaseUrlsOrigin()
    {
        var handler = new Router(sent => sent.Url.StartsWith($"{Base}/exports/moved", StringComparison.Ordinal)
            ? Redirect("https://files.example.invalid/exports/offers-1.json")
            : new HttpResponseMessage(HttpStatusCode.OK) { Content = new StringContent("[]", Encoding.UTF8, "application/json") });
        using var client = Client(handler);

        await using (var own = await client.DownloadUrlAsync($"{Base}/exports/offers-1.json", Cancel))
        {
            Assert.Equal("[]", Encoding.UTF8.GetString(await own.ReadAllBytesAsync(Cancel)));
        }
        await using (await client.DownloadUrlAsync("https://files.example.invalid/exports/offers-1.json", Cancel))
        {
        }
        await using (await client.DownloadUrlAsync($"{Base}/exports/moved?signature=synthetic", Cancel))
        {
        }

        Assert.Equal(
            [Key, null, Key, null],
            handler.Sent.Select(sent => sent.Headers.GetValueOrDefault("Authorization")));
        await Assert.ThrowsAsync<ArgumentException>(() => client.DownloadUrlAsync("/exports/offers-1.json", Cancel));
    }

    [Fact]
    public async Task ErrorsAreTypedByStatusAndHoldTheBodyWithoutTheKey()
    {
        var handler = new Router(sent => sent.Path switch
        {
            "/api/account" => Json($"bad key {Key}", HttpStatusCode.Unauthorized),
            "/api/offers/1" => Json("{}", HttpStatusCode.NotFound),
            _ => Json("{}", HttpStatusCode.TooManyRequests, retryAfter: "120"),
        });
        var logs = new Lines();
        using var client = Client(handler, logger: logs);

        var unauthorized = await Assert.ThrowsAsync<AuthenticationException>(() => client.Shop.GetAsync(cancellationToken: Cancel));
        var missing = await Assert.ThrowsAsync<NotFoundException>(() => client.Offers.GetAsync(1, cancellationToken: Cancel));
        var limited = await Assert.ThrowsAsync<RateLimitedException>(() => client.Platform.ListLocalesAsync(cancellationToken: Cancel));

        Assert.Equal("authentication", unauthorized.Kind);
        Assert.Equal(401, unauthorized.Status);
        Assert.DoesNotContain(Key, unauthorized.RawBody!, StringComparison.Ordinal);
        Assert.Equal("not_found", missing.Kind);
        Assert.Equal("120", limited.RetryAfter);
        Assert.NotEmpty(logs.All);
        Assert.DoesNotContain(logs.All, entry => entry.Contains(Key, StringComparison.Ordinal));
    }

    [Fact]
    public async Task UsesAnInjectedHttpClientWithoutDisposingIt()
    {
        var handler = new Router(_ => Json(Shop));
        using var http = new HttpClient(handler);

        using (var client = new MiraklClient(Base, Key, new MiraklClientOptions(), http))
        {
            await client.Shop.GetAsync(cancellationToken: Cancel);
        }
        using var again = await http.GetAsync($"{Base}/api/account", Cancel);

        Assert.Equal(2, handler.Sent.Count);
        Assert.Equal(Key, handler.Sent.First().Headers["Authorization"]);
    }

    private static HttpResponseMessage Json(string body, HttpStatusCode status = HttpStatusCode.OK, string? retryAfter = null)
    {
        var response = new HttpResponseMessage(status) { Content = new StringContent(body, Encoding.UTF8, "application/json") };
        if (retryAfter is not null)
        {
            response.Headers.TryAddWithoutValidation("Retry-After", retryAfter);
        }
        return response;
    }

    private static HttpResponseMessage Redirect(string location)
    {
        var response = new HttpResponseMessage(HttpStatusCode.Found);
        response.Headers.Location = new Uri(location);
        return response;
    }

    private sealed record Sent(string Url, string Path, Dictionary<string, string> Headers, string Body);

    private sealed class Router(Func<Sent, HttpResponseMessage> respond) : HttpMessageHandler
    {
        public ConcurrentQueue<Sent> Sent { get; } = new();

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var headers = request.Headers.NonValidated.ToDictionary(header => header.Key, header => header.Value.ToString(), StringComparer.OrdinalIgnoreCase);
            var body = request.Content is null ? string.Empty : await request.Content.ReadAsStringAsync(cancellationToken);
            foreach (var header in request.Content?.Headers.NonValidated.ToArray() ?? [])
            {
                headers[header.Key] = header.Value.ToString();
            }
            var sent = new Sent(request.RequestUri!.AbsoluteUri, request.RequestUri.AbsolutePath, headers, body);
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
