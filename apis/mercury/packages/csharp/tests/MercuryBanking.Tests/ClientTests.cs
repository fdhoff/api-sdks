using System.Collections.Concurrent;
using System.Net;
using System.Text;
using MercuryBanking.Models;
using MercuryBanking.Runtime;
using Microsoft.Extensions.Logging;
using Xunit;

namespace MercuryBanking.Tests;

public sealed class ClientTests
{
    private const string Token = "secret-token:synthetic-unit-token";
    private const string Page = """{"accounts": [], "page": {}}""";

    private static readonly Guid AccountA = Guid.Parse("00000000-0000-4000-8000-acc000000001");
    private static readonly Guid AccountB = Guid.Parse("00000000-0000-4000-8000-acc000000002");
    private static readonly Guid Card = Guid.Parse("00000000-0000-4000-8000-ca4d00000001");

    private static CancellationToken Cancel => TestContext.Current.CancellationToken;

    private static MercuryClient Client(Router handler, MercuryClientOptions? options = null) =>
        new(Token, new MercuryClientOptions
        {
            Environment = options?.Environment ?? MercuryClient.Production,
            Hosts = options?.Hosts,
            UserAgent = options?.UserAgent,
            Logger = options?.Logger,
            RetryBaseDelay = TimeSpan.FromMilliseconds(1),
            HttpHandler = handler,
        });

    [Fact]
    public void EveryOperationHasAPublicMethod()
    {
        foreach (var operation in ClientResources.Operations)
        {
            var resource = typeof(MercuryClient).GetProperty(operation.Resource);
            Assert.NotNull(resource);
            Assert.NotNull(resource.PropertyType.GetMethod(operation.Name));
            Assert.Equal(operation.Id == "revealCardPan" ? "vault" : "api", operation.Host);
            if (operation.Iterator is not null)
            {
                Assert.NotNull(resource.PropertyType.GetMethod(operation.Iterator));
            }
        }
        Assert.Equal(90, ClientResources.Operations.Length);
        Assert.Equal(27, ClientResources.Operations.Count(operation => operation.Iterator is not null));
        Assert.Equal(
            ["createInternalTransfer", "createTransaction", "requestSendMoney", "requestTransferMoney"],
            ClientResources.Operations.Where(operation => operation.IdempotencyKey == "idempotencyKey").Select(operation => operation.Id).Order(StringComparer.Ordinal));
    }

    [Fact]
    public async Task SendsTheTokenVerbatimAsABearerToken()
    {
        var handler = new Router(_ => Json(Page));
        using var client = Client(handler, new() { UserAgent = "synthetic-agent/1" });

        await client.Accounts.ListAsync(cancellationToken: Cancel);

        var sent = Assert.Single(handler.Sent);
        Assert.Equal("https://api.mercury.com/api/v1/accounts", sent.Url);
        Assert.Equal($"Bearer {Token}", sent.Headers["Authorization"]);
        Assert.Equal("application/json", sent.Headers["Accept"]);
        Assert.Equal("synthetic-agent/1", sent.Headers["User-Agent"]);
    }

    [Fact]
    public async Task TheSandboxHasItsOwnHostsAndCardDetailsGoToTheVault()
    {
        var handler = new Router(sent => Json(sent.Path.EndsWith("/reveal", StringComparison.Ordinal) ? "{}" : Page));
        using var production = Client(handler);
        using var sandbox = Client(handler, new() { Environment = MercuryClient.Sandbox });

        await production.Cards.RevealAsync(Card, Cancel);
        await sandbox.Accounts.ListAsync(cancellationToken: Cancel);
        await sandbox.Cards.RevealAsync(Card, Cancel);

        Assert.Equal(
            [$"https://vault-api.mercury.com/api/v1/cards/{Card}/reveal", "https://api-sandbox.mercury.com/api/v1/accounts", $"https://api-sandbox.mercury.com/api/v1/cards/{Card}/reveal"],
            handler.Sent.Select(sent => sent.Url));
    }

    [Fact]
    public async Task APdfDownloadAsksForAPdf()
    {
        var handler = new Router(_ => new HttpResponseMessage(HttpStatusCode.OK) { Content = new ByteArrayContent([0x25, 0x50, 0x44, 0x46]) });
        using var client = Client(handler);

        await using var download = await client.Invoices.DownloadPdfAsync(AccountA, Cancel);

        Assert.Equal("application/pdf", Assert.Single(handler.Sent).Headers["Accept"]);
        Assert.Equal([0x25, 0x50, 0x44, 0x46], await download.ReadAllBytesAsync(Cancel));
    }

    [Fact]
    public void RefusesAnEmptyTokenAnUnknownEnvironmentAndPartialHosts()
    {
        Assert.Throws<ArgumentException>(() => new MercuryClient(string.Empty));
        Assert.Throws<ArgumentException>(() => new MercuryClient(Token, new() { Environment = "staging" }));
        Assert.Throws<ArgumentException>(() => new MercuryClient(Token, new() { Hosts = new Dictionary<string, string> { ["api"] = "https://mock.invalid" } }));
    }

    [Fact]
    public void EnvironmentsIsACopy()
    {
        var copy = (Dictionary<string, string>)MercuryClient.Environments[MercuryClient.Production];
        copy["api"] = "https://changed.invalid";

        Assert.Equal("https://api.mercury.com/api/v1", MercuryClient.Environments[MercuryClient.Production]["api"]);
        Assert.Equal(["production", "sandbox"], MercuryClient.Environments.Keys.Order(StringComparer.Ordinal));
    }

    [Fact]
    public async Task AMoneyMovingWriteWithAKeyIsRetriedWithTheSameBody()
    {
        var calls = 0;
        var handler = new Router(_ => ++calls == 1 ? Json("{}", HttpStatusCode.ServiceUnavailable) : Json("""{"id": "transfer-1"}"""));
        using var client = Client(handler);

        await client.Accounts.TransferAsync(new InternalTransferAPIRequest { SourceAccountId = AccountA, DestinationAccountId = AccountB, Amount = 12.5, IdempotencyKey = "synthetic-key-1" }, Cancel);

        var sent = handler.Sent.ToArray();
        Assert.Equal(2, sent.Length);
        Assert.Equal(sent[0].Body, sent[1].Body);
        Assert.Contains("\"idempotencyKey\":\"synthetic-key-1\"", sent[0].Body, StringComparison.Ordinal);
    }

    [Fact]
    public async Task AMoneyMovingWriteWithoutAKeyIsNotRetried()
    {
        var handler = new Router(_ => Json("{}", HttpStatusCode.ServiceUnavailable));
        using var client = Client(handler);

        var error = await Assert.ThrowsAsync<ServerException>(() => client.Accounts.TransferAsync(new InternalTransferAPIRequest { SourceAccountId = AccountA, DestinationAccountId = AccountB, Amount = 12.5 }, Cancel));

        Assert.Equal(503, error.Status);
        Assert.Single(handler.Sent);
    }

    [Fact]
    public async Task ErrorsAreTypedByStatusAndHoldTheBodyWithoutTheToken()
    {
        var handler = new Router(sent => sent.Path.EndsWith("/accounts", StringComparison.Ordinal)
            ? Json($"bad token {Token}", HttpStatusCode.Unauthorized)
            : Json("{}", HttpStatusCode.TooManyRequests, retryAfter: "120"));
        var logs = new Lines();
        using var client = Client(handler, new() { Logger = logs });

        var unauthorized = await Assert.ThrowsAsync<AuthenticationException>(() => client.Accounts.ListAsync(cancellationToken: Cancel));
        var limited = await Assert.ThrowsAsync<RateLimitedException>(() => client.Users.ListAsync(cancellationToken: Cancel));

        Assert.Equal("authentication", unauthorized.Kind);
        Assert.Equal(401, unauthorized.Status);
        Assert.DoesNotContain(Token, unauthorized.RawBody!, StringComparison.Ordinal);
        Assert.DoesNotContain(Token, unauthorized.Message, StringComparison.Ordinal);
        Assert.Equal("120", limited.RetryAfter);
        Assert.NotEmpty(logs.All);
        Assert.DoesNotContain(logs.All, entry => entry.Contains(Token, StringComparison.Ordinal));
    }

    [Fact]
    public async Task ListAllFollowsTheNextPageUntilItIsNull()
    {
        var handler = new Router(sent => Json(sent.Url.Contains("start_after", StringComparison.Ordinal)
            ? $$$"""{"accounts": [{"id": "{{{AccountB}}}"}], "page": {"nextPage": null}}"""
            : $$$"""{"accounts": [{"id": "{{{AccountA}}}"}], "page": {"nextPage": "{{{AccountA}}}"}}"""));
        using var client = Client(handler);

        var accounts = await client.Accounts.ListAllAsync(limit: 1, cancellationToken: Cancel).ToListAsync(Cancel);

        Assert.Equal([AccountA, AccountB], accounts.Select(account => account.Id));
        Assert.Equal($"https://api.mercury.com/api/v1/accounts?limit=1&start_after={AccountA}", handler.Sent.Last().Url);
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
