using System.Collections.Concurrent;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using EtsySeller.Runtime;
using Microsoft.Extensions.Logging;
using Xunit;

namespace EtsySeller.Tests;

public sealed class ClientTests
{
    private const string Key = "synthetic-keystring";
    private const string Shared = "synthetic-shared-secret";
    private const string Access = "12345678.synthetic-access";
    private const string Refresh = "12345678.synthetic-refresh";
    private const string NewAccess = "12345678.synthetic-new-access";
    private const string NewRefresh = "12345678.synthetic-new-refresh";
    private const string TokenPath = "/v3/public/oauth/token";
    private const string MePath = "/v3/application/users/me";

    private static CancellationToken Cancel => TestContext.Current.CancellationToken;

    private static EtsyClient Client(Router handler, EtsyClientOptions? options = null) =>
        new(Key, Shared, new EtsyClientOptions
        {
            AccessToken = options?.AccessToken,
            RefreshToken = options?.RefreshToken,
            OnToken = options?.OnToken,
            Logger = options?.Logger,
            BaseUrl = new Uri("https://mock.invalid/"),
            RetryBaseDelay = TimeSpan.FromMilliseconds(1),
            HttpHandler = handler,
        });

    [Fact]
    public void EveryOperationHasAPublicMethod()
    {
        Assert.Equal(107, ClientResources.Operations.Length);
        foreach (var operation in ClientResources.Operations)
        {
            var resource = typeof(EtsyClient).GetProperty(operation.Resource);
            Assert.NotNull(resource);
            Assert.NotNull(resource.PropertyType.GetMethod(operation.Name));
            if (operation.Iterator is not null)
            {
                Assert.IsType<OffsetPaging>(operation.Paging);
                Assert.NotNull(resource.PropertyType.GetMethod(operation.Iterator));
            }
        }
    }

    [Fact]
    public async Task KeyOnlyOperationsSendNoAccessToken()
    {
        var handler = new Router(_ => Json("""{"ping_id": 1}"""));
        using var client = Client(handler, new() { AccessToken = Access });

        await client.Application.PingAsync(Cancel);

        var sent = Assert.Single(handler.Sent);
        Assert.Equal($"{Key}:{Shared}", sent.Headers["x-api-key"]);
        Assert.False(sent.Headers.ContainsKey("Authorization"));
    }

    [Fact]
    public async Task OAuthOperationsSendBothHeaders()
    {
        var handler = new Router(_ => Json("""{"user_id": 12345678, "shop_id": 1}"""));
        using var client = Client(handler, new() { AccessToken = Access });

        var me = await client.Users.GetMeAsync(Cancel);

        Assert.Equal(1, me.ShopId);
        var sent = Assert.Single(handler.Sent);
        Assert.Equal($"https://mock.invalid{MePath}", sent.Url);
        Assert.Equal($"{Key}:{Shared}", sent.Headers["x-api-key"]);
        Assert.Equal($"Bearer {Access}", sent.Headers["Authorization"]);
    }

    [Fact]
    public async Task FormBodiesAreUrlEncodedWithRepeatedFields()
    {
        var handler = new Router(_ => Json("""{"listing_id": 9}"""));
        using var client = Client(handler, new() { AccessToken = Access });

        var listing = await client.Listings.CreateDraftAsync(
            1, 2, "Mug & saucer", "Synthetic", 12.5, "i_did", "made_to_order", 3, tags: ["a b", "c"], cancellationToken: Cancel);

        Assert.Equal(9, listing.ListingId);
        var sent = Assert.Single(handler.Sent);
        Assert.Equal("application/x-www-form-urlencoded", sent.Headers["Content-Type"]);
        Assert.Contains("title=Mug+%26+saucer", sent.Body, StringComparison.Ordinal);
        Assert.Contains("price=12.5", sent.Body, StringComparison.Ordinal);
        Assert.Contains("tags=a+b&tags=c", sent.Body, StringComparison.Ordinal);
    }

    [Fact]
    public async Task OffsetIteratorWalksEveryPage()
    {
        var handler = new Router(request =>
        {
            var offset = QueryValue(request.Url, "offset") ?? "0";
            return Json(offset switch
            {
                "5" => """{"count": 9, "results": [{"listing_id": 1}, {"listing_id": 2}]}""",
                "7" => """{"count": 9, "results": [{"listing_id": 3}]}""",
                _ => """{"count": 9, "results": []}""",
            });
        });
        using var client = Client(handler);

        var ids = new List<long?>();
        await foreach (var listing in client.Listings.ListAllActiveAsync(limit: 2, offset: 5, cancellationToken: Cancel))
        {
            ids.Add(listing.ListingId);
        }

        Assert.Equal([1L, 2L, 3L], ids);
        Assert.Equal(["5", "7", "8"], handler.Sent.Select(sent => QueryValue(sent.Url, "offset")));
        Assert.All(handler.Sent, sent => Assert.Equal("2", QueryValue(sent.Url, "limit")));
    }

    [Theory]
    [InlineData(400, typeof(BadRequestException), "bad_request")]
    [InlineData(401, typeof(AuthenticationException), "authentication")]
    [InlineData(403, typeof(PermissionDeniedException), "permission")]
    [InlineData(404, typeof(NotFoundException), "not_found")]
    [InlineData(409, typeof(ConflictException), "conflict")]
    [InlineData(422, typeof(UnprocessableException), "validation")]
    [InlineData(418, typeof(HttpException), "api")]
    public async Task ErrorsCarryTheBodyText(int status, Type type, string kind)
    {
        var handler = new Router(_ => Json("""{"error": "Synthetic failure"}""", (HttpStatusCode)status));
        using var client = Client(handler);

        var error = await Assert.ThrowsAnyAsync<HttpException>(() => client.Shops.GetAsync(1, Cancel));

        Assert.IsType(type, error);
        Assert.Equal(kind, error.Kind);
        Assert.Equal(status, error.Status);
        Assert.Equal("Synthetic failure", error.Detail);
        Assert.Equal($"HTTP {status}: Synthetic failure", error.Message);
    }

    [Fact]
    public async Task A401RefreshesOnceThenRetriesWithTheNewToken()
    {
        var stored = new List<EtsyToken>();
        var handler = new Router(request => request.Path == TokenPath ? Tokens() : Accepts(request, NewAccess));
        using var client = Client(handler, new()
        {
            AccessToken = Access,
            RefreshToken = Refresh,
            OnToken = (token, _) =>
            {
                stored.Add(token);
                return Task.CompletedTask;
            },
        });

        await client.Users.GetMeAsync(Cancel);

        Assert.Equal([MePath, TokenPath, MePath], handler.Sent.Select(sent => sent.Path));
        var refresh = handler.Sent.ElementAt(1);
        Assert.Equal($"grant_type=refresh_token&client_id={Key}&refresh_token={Uri.EscapeDataString(Refresh)}", refresh.Body);
        Assert.False(refresh.Headers.ContainsKey("Authorization"));
        Assert.Equal($"Bearer {NewAccess}", handler.Sent.Last().Headers["Authorization"]);
        var token = Assert.Single(stored);
        Assert.Equal(NewRefresh, token.RefreshToken);
        Assert.Equal(3600, token.ExpiresIn);
    }

    [Fact]
    public async Task ASecond401AfterARefreshIsThrown()
    {
        var handler = new Router(request => request.Path == TokenPath ? Tokens() : Unauthorized());
        using var client = Client(handler, new() { AccessToken = Access, RefreshToken = Refresh });

        await Assert.ThrowsAsync<AuthenticationException>(() => client.Users.GetMeAsync(Cancel));

        Assert.Equal([MePath, TokenPath, MePath], handler.Sent.Select(sent => sent.Path));
    }

    [Fact]
    public async Task A401OnAKeyOnlyOperationDoesNotRefresh()
    {
        var handler = new Router(_ => Unauthorized());
        using var client = Client(handler, new() { AccessToken = Access, RefreshToken = Refresh });

        await Assert.ThrowsAsync<AuthenticationException>(() => client.Application.PingAsync(Cancel));

        Assert.Single(handler.Sent);
    }

    [Fact]
    public async Task WithoutARefreshTokenA401IsThrown()
    {
        var handler = new Router(_ => Unauthorized());
        using var client = Client(handler, new() { AccessToken = Access });

        await Assert.ThrowsAsync<AuthenticationException>(() => client.Users.GetMeAsync(Cancel));
        await Assert.ThrowsAsync<InvalidOperationException>(() => client.OAuth.RefreshAsync(Cancel));

        Assert.Single(handler.Sent);
    }

    [Fact]
    public async Task AFailedRefreshThrowsItsErrorWithoutTheRefreshToken()
    {
        var handler = new Router(request => request.Path == TokenPath
            ? Json($$"""{"error": "invalid_grant", "error_description": "{{Refresh}} expired"}""", HttpStatusCode.BadRequest)
            : Unauthorized());
        using var client = Client(handler, new() { AccessToken = Access, RefreshToken = Refresh });

        var error = await Assert.ThrowsAsync<BadRequestException>(() => client.Users.GetMeAsync(Cancel));

        Assert.Equal("invalid_grant", error.Detail);
        Assert.DoesNotContain(Refresh, error.RawBody, StringComparison.Ordinal);
    }

    [Fact]
    public async Task A401FromTheTokenEndpointIsThrownWithoutAnotherRefresh()
    {
        var handler = new Router(_ => Unauthorized());
        using var client = Client(handler, new() { AccessToken = Access, RefreshToken = Refresh });

        var call = client.Users.GetMeAsync(Cancel);

        Assert.Same(call, await Task.WhenAny(call, Task.Delay(TimeSpan.FromSeconds(10), Cancel)));
        await Assert.ThrowsAsync<AuthenticationException>(() => call);
        Assert.Equal([MePath, TokenPath], handler.Sent.Select(sent => sent.Path));
    }

    [Fact]
    public async Task ATokenResponseWithoutTokensIsADecodeError()
    {
        var handler = new Router(_ => Json("""{"access_token": "only-one"}"""));
        using var client = Client(handler, new() { RefreshToken = Refresh });

        await Assert.ThrowsAsync<ApiDecodeException>(() => client.OAuth.RefreshAsync(Cancel));
    }

    [Fact]
    public async Task ConcurrentCallsShareOneRefresh()
    {
        var refreshes = 0;
        var handler = new Router(request =>
        {
            if (request.Path == TokenPath)
            {
                Interlocked.Increment(ref refreshes);
                Thread.Sleep(20);
                return Tokens();
            }
            return Accepts(request, NewAccess);
        });
        using var client = Client(handler, new() { AccessToken = Access, RefreshToken = Refresh });

        await Task.WhenAll(Enumerable.Range(0, 4).Select(_ => client.Users.GetMeAsync(Cancel)));

        Assert.Equal(1, refreshes);
    }

    [Fact]
    public async Task ExchangeCodeStoresTheTokenForLaterCalls()
    {
        EtsyToken? stored = null;
        var handler = new Router(request => request.Path == TokenPath ? Tokens() : Accepts(request, NewAccess));
        using var client = Client(handler, new()
        {
            OnToken = (token, _) =>
            {
                stored = token;
                return Task.CompletedTask;
            },
        });

        var token = await client.OAuth.ExchangeCodeAsync("synthetic-code", new string('v', 43), "https://example.com/callback", Cancel);
        await client.Users.GetMeAsync(Cancel);

        Assert.Same(token, stored);
        Assert.Equal(12345678, token.UserId);
        var exchange = handler.Sent.First();
        Assert.Equal("application/x-www-form-urlencoded", exchange.Headers["Content-Type"]);
        Assert.Equal(
            $"grant_type=authorization_code&client_id={Key}&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&code=synthetic-code&code_verifier={new string('v', 43)}",
            exchange.Body);
        Assert.False(exchange.Headers.ContainsKey("x-api-key"));
        Assert.Equal($"Bearer {NewAccess}", handler.Sent.Last().Headers["Authorization"]);
    }

    [Fact]
    public async Task LogsAndErrorsNeverHoldASecret()
    {
        var logs = new Lines();
        var echo = $"{Key}:{Shared} {Access} {Refresh} {NewAccess} {NewRefresh} synthetic-code";
        var handler = new Router(request => request.Path == TokenPath ? Tokens() : Json($$"""{"error": "{{echo}}"}""", HttpStatusCode.BadRequest));
        using var client = Client(handler, new() { AccessToken = Access, RefreshToken = Refresh, Logger = logs });

        await client.OAuth.ExchangeCodeAsync("synthetic-code", new string('v', 43), "https://example.com/callback", Cancel);
        var error = await Assert.ThrowsAsync<BadRequestException>(() => client.Users.GetMeAsync(Cancel));

        var output = $"{error.Message} {error.Detail} {error.RawBody} {string.Join(' ', logs.All)}";
        Assert.NotEmpty(logs.All);
        foreach (var secret in new[] { Key, Shared, Access, Refresh, NewAccess, NewRefresh, "synthetic-code", new string('v', 43) })
        {
            Assert.DoesNotContain(secret, output, StringComparison.Ordinal);
        }
    }

    [Fact]
    public void TokenAndRequestStringsHideTheirSecrets()
    {
        var token = new EtsyToken(Access, Refresh, 3600);
        var request = EtsyOAuth.CreateAuthorizationRequest(Key, "https://example.com/callback", ["listings_r"]);

        Assert.DoesNotContain("synthetic", token.ToString(), StringComparison.Ordinal);
        Assert.Contains("12345678", token.ToString(), StringComparison.Ordinal);
        Assert.DoesNotContain(request.CodeVerifier, request.ToString(), StringComparison.Ordinal);
        Assert.Null(new EtsyToken("not-a-user.x", Refresh).UserId);
    }

    [Fact]
    public void AuthorizationRequestUsesPkceS256AndState()
    {
        var request = EtsyOAuth.CreateAuthorizationRequest(Key, "https://example.com/callback", ["listings_r", "shops_r"]);

        Assert.Equal("https://www.etsy.com/oauth/connect", request.Url.GetLeftPart(UriPartial.Path));
        Assert.InRange(request.CodeVerifier.Length, 43, 128);
        Assert.True(request.State.Length >= 32);
        var challenge = Convert.ToBase64String(SHA256.HashData(Encoding.ASCII.GetBytes(request.CodeVerifier))).TrimEnd('=').Replace('+', '-').Replace('/', '_');
        Assert.Equal("code", QueryValue(request.Url.AbsoluteUri, "response_type"));
        Assert.Equal(Key, QueryValue(request.Url.AbsoluteUri, "client_id"));
        Assert.Equal("https://example.com/callback", QueryValue(request.Url.AbsoluteUri, "redirect_uri"));
        Assert.Equal("listings_r shops_r", QueryValue(request.Url.AbsoluteUri, "scope"));
        Assert.Equal(request.State, QueryValue(request.Url.AbsoluteUri, "state"));
        Assert.Equal(challenge, QueryValue(request.Url.AbsoluteUri, "code_challenge"));
        Assert.Equal("S256", QueryValue(request.Url.AbsoluteUri, "code_challenge_method"));
        Assert.NotEqual(request.State, EtsyOAuth.CreateAuthorizationRequest(Key, "https://example.com/callback", ["listings_r"]).State);
    }

    [Fact]
    public void AuthorizationRequestKeepsAGivenStateAndRejectsABadVerifier()
    {
        var verifier = new string('a', 43);

        var request = EtsyOAuth.CreateAuthorizationRequest(Key, "https://example.com/callback", ["listings_r"], state: "given", codeVerifier: verifier);

        Assert.Equal("given", request.State);
        Assert.Equal(verifier, request.CodeVerifier);
        Assert.Equal("uVSCu3qDNirjv0bIeDy6UVP3ug80L3uEE4Xpd6azRLk", EtsyOAuth.CodeChallenge("dBjftJeZ4CVP-mJ92IGLPYV_DuBUyBrXJ33mD6UjN0X"));
        Assert.Throws<ArgumentException>(() => EtsyOAuth.CreateAuthorizationRequest(Key, "https://example.com/callback", ["listings_r"], codeVerifier: "short"));
        Assert.Throws<ArgumentException>(() => EtsyOAuth.CreateAuthorizationRequest(Key, "https://example.com/callback", []));
    }

    [Fact]
    public void CredentialsAreRequired()
    {
        Assert.Throws<ArgumentException>(() => new EtsyClient("", Shared));
        Assert.Throws<ArgumentException>(() => new EtsyClient(Key, ""));
        Assert.Throws<ArgumentException>(() => new EtsyClient(Key, Shared, new EtsyClientOptions { AccessToken = "bad\ntoken" }));
    }

    private static string? QueryValue(string url, string name) => Transport.QueryOf(url).GetValueOrDefault(name);

    private static HttpResponseMessage Json(string body, HttpStatusCode status = HttpStatusCode.OK) =>
        new(status) { Content = new StringContent(body, Encoding.UTF8, "application/json") };

    private static HttpResponseMessage Unauthorized() => Json("""{"error": "invalid_token"}""", HttpStatusCode.Unauthorized);

    private static HttpResponseMessage Tokens() =>
        Json($$"""{"access_token": "{{NewAccess}}", "refresh_token": "{{NewRefresh}}", "expires_in": 3600, "token_type": "Bearer"}""");

    private static HttpResponseMessage Accepts(Sent request, string token) =>
        request.Headers.GetValueOrDefault("Authorization") == $"Bearer {token}" ? Json("""{"user_id": 12345678, "shop_id": 1}""") : Unauthorized();

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
