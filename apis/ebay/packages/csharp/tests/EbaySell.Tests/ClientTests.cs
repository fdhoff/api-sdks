using System.Collections.Concurrent;
using System.Net;
using System.Reflection;
using System.Text;
using EbaySell.Runtime;
using Microsoft.Extensions.Logging;
using Org.BouncyCastle.Crypto.Generators;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Pkcs;
using Org.BouncyCastle.Security;
using Xunit;

namespace EbaySell.Tests;

public sealed class ClientTests
{
    private const string AppId = "synthetic-app-id";
    private const string CertId = "synthetic-cert-id";
    private const string RuName = "synthetic-ru-name";
    private const string App = "synthetic-app-token";
    private const string NewApp = "synthetic-new-app-token";
    private const string User = "synthetic-user-token";
    private const string NewUser = "synthetic-new-user-token";
    private const string Refresh = "synthetic-refresh-token";
    private const string TokenPath = "/identity/v1/oauth2/token";
    private const string TreePath = "/commerce/taxonomy/v1/get_default_category_tree_id";
    private const string OrderPath = "/sell/fulfillment/v1/order/O-1";

    private static readonly string Basic = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{AppId}:{CertId}"));

    private static readonly Dictionary<string, string> MockHosts = new()
    {
        ["api"] = "https://api.mock.invalid",
        ["apiz"] = "https://apiz.mock.invalid",
        ["apim"] = "https://apim.mock.invalid",
    };

    private static CancellationToken Cancel => TestContext.Current.CancellationToken;

    private static EbayClient Client(Router handler, EbayClientOptions options) =>
        new(new EbayClientOptions
        {
            ClientId = options.ClientId,
            ClientSecret = options.ClientSecret,
            RuName = options.RuName,
            AppToken = options.AppToken,
            UserToken = options.UserToken,
            RefreshToken = options.RefreshToken,
            OnToken = options.OnToken,
            UserScopes = options.UserScopes,
            Environment = options.Environment,
            Hosts = options.Hosts ?? (options.Environment == EbayClient.Production ? MockHosts : null),
            MarketplaceId = options.MarketplaceId,
            ContentLanguage = options.ContentLanguage,
            SigningKey = options.SigningKey,
            Logger = options.Logger,
            Clock = options.Clock,
            RetryBaseDelay = TimeSpan.FromMilliseconds(1),
            HttpHandler = handler,
        });

    [Fact]
    public void EveryOperationHasAPublicMethod()
    {
        var total = 0;
        foreach (var api in typeof(EbayClient).GetProperties().Where(property => property.PropertyType.Name == "Resources"))
        {
            var operations = (Operation[])api.PropertyType.GetField("Operations", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null)!;
            Assert.NotNull(api.PropertyType.GetField("Contract", BindingFlags.NonPublic | BindingFlags.Static));
            foreach (var operation in operations)
            {
                var resource = api.PropertyType.GetProperty(operation.Resource);
                Assert.NotNull(resource);
                Assert.NotNull(resource.PropertyType.GetMethod(operation.Name));
                Assert.Contains(operation.Host, MockHosts.Keys);
                if (operation.Iterator is not null)
                {
                    Assert.IsType<NextLinkPaging>(operation.Paging);
                    Assert.NotNull(resource.PropertyType.GetMethod(operation.Iterator));
                }
            }
            total += operations.Length;
        }
        Assert.Equal(339, total);
    }

    [Theory]
    [InlineData(nameof(EbaySell.Inventory.Api.InventoryItemsResource.CreateOrReplaceAsync), NullabilityState.Nullable)]
    [InlineData(nameof(EbaySell.Inventory.Api.InventoryItemsResource.BulkCreateOrReplaceAsync), NullabilityState.NotNull)]
    public void AResultIsNullableOnlyWhereTheOperationDeclaresA204(string method, NullabilityState expected)
    {
        var returned = new NullabilityInfoContext().Create(typeof(EbaySell.Inventory.Api.InventoryItemsResource).GetMethod(method)!.ReturnParameter);

        Assert.Equal(expected, Assert.Single(returned.GenericTypeArguments).ReadState);
    }

    [Fact]
    public async Task ApplicationOperationsGetTheAppTokenAndSellerOperationsTheUserToken()
    {
        var handler = new Router(sent => sent.Path == TreePath ? Json("""{"categoryTreeId": "0"}""") : Json("""{"orderId": "O-1"}"""));
        using var client = Client(handler, new() { AppToken = App, UserToken = User });

        var tree = await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel);
        var order = await client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel);

        Assert.Equal("0", tree?.CategoryTreeId);
        Assert.Equal("O-1", order.OrderId);
        var sent = handler.Sent.ToArray();
        Assert.Equal($"https://api.mock.invalid{TreePath}?marketplace_id=EBAY_US", sent[0].Url);
        Assert.Equal($"Bearer {App}", sent[0].Headers["Authorization"]);
        Assert.Equal($"Bearer {User}", sent[1].Headers["Authorization"]);
    }

    [Fact]
    public async Task TheAppTokenIsMintedOnceAndAgainNearExpiry()
    {
        var clock = new Clock();
        var minted = 0;
        var handler = new Router(sent => sent.Path == TokenPath
            ? Json($$"""{"access_token": "{{(++minted == 1 ? App : NewApp)}}", "expires_in": 7200, "token_type": "Application Access Token"}""")
            : Json("""{"categoryTreeId": "0"}"""));
        using var client = Client(handler, new() { ClientId = AppId, ClientSecret = CertId, Clock = clock });

        await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel);
        await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel);
        clock.Now += TimeSpan.FromSeconds(7200 - 59);
        await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel);

        var sent = handler.Sent.ToArray();
        Assert.Equal([TokenPath, TreePath, TreePath, TokenPath, TreePath], sent.Select(item => item.Path));
        Assert.Equal($"Basic {Basic}", sent[0].Headers["Authorization"]);
        Assert.Equal("grant_type=client_credentials&scope=https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope", sent[0].Body);
        Assert.StartsWith("application/x-www-form-urlencoded", sent[0].Headers["Content-Type"], StringComparison.Ordinal);
        Assert.Equal($"Bearer {App}", sent[2].Headers["Authorization"]);
        Assert.Equal($"Bearer {NewApp}", sent[4].Headers["Authorization"]);
    }

    [Fact]
    public async Task ARefusedAppTokenIsReplacedOnce()
    {
        var handler = new Router(sent => sent.Path == TokenPath ? Json($$"""{"access_token": "{{NewApp}}", "expires_in": 7200}""")
            : sent.Headers["Authorization"] == $"Bearer {NewApp}" ? Json("""{"categoryTreeId": "0"}""") : Unauthorized());
        using var client = Client(handler, new() { ClientId = AppId, ClientSecret = CertId, AppToken = App });

        await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel);

        Assert.Equal([TreePath, TokenPath, TreePath], handler.Sent.Select(item => item.Path));
    }

    [Fact]
    public async Task ARefusedUserTokenIsRefreshedAndStored()
    {
        var stored = new List<EbayToken>();
        var handler = new Router(sent => sent.Path == TokenPath ? Json($$"""{"access_token": "{{NewUser}}", "expires_in": 7200, "token_type": "User Access Token"}""")
            : sent.Headers["Authorization"] == $"Bearer {NewUser}" ? Json("""{"orderId": "O-1"}""") : Unauthorized());
        using var client = Client(handler, new()
        {
            ClientId = AppId,
            ClientSecret = CertId,
            UserToken = User,
            RefreshToken = Refresh,
            UserScopes = ["https://api.ebay.com/oauth/api_scope/sell.fulfillment"],
            OnToken = (token, _) =>
            {
                stored.Add(token);
                return Task.CompletedTask;
            },
        });

        await client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel);

        var sent = handler.Sent.ToArray();
        Assert.Equal([OrderPath, TokenPath, OrderPath], sent.Select(item => item.Path));
        Assert.Equal($"Basic {Basic}", sent[1].Headers["Authorization"]);
        Assert.Equal($"grant_type=refresh_token&refresh_token={Refresh}&scope=https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope%2Fsell.fulfillment", sent[1].Body);
        var token = Assert.Single(stored);
        Assert.Equal(NewUser, token.AccessToken);
        Assert.Equal(Refresh, token.RefreshToken);
        Assert.Equal(7200, token.ExpiresIn);
    }

    [Fact]
    public async Task ConcurrentRefusalsShareOneRefresh()
    {
        var handler = new Router(async sent =>
        {
            if (sent.Path == TokenPath)
            {
                await Task.Delay(50);
                return Json($$"""{"access_token": "{{NewUser}}"}""");
            }
            return sent.Headers["Authorization"] == $"Bearer {NewUser}" ? Json("""{"orderId": "O-1"}""") : Unauthorized();
        });
        using var client = Client(handler, new() { ClientId = AppId, ClientSecret = CertId, UserToken = User, RefreshToken = Refresh });

        await Task.WhenAll(Enumerable.Range(0, 5).Select(_ => client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel)));

        Assert.Single(handler.Sent, item => item.Path == TokenPath);
    }

    [Fact]
    public async Task AnAppRefusalAndAUserRefusalEachRefreshTheirOwnToken()
    {
        var refused = 0;
        var bothRefused = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);
        var handler = new Router(async sent =>
        {
            if (sent.Path == TokenPath)
            {
                return sent.Body.StartsWith("grant_type=client_credentials", StringComparison.Ordinal)
                    ? Json($$"""{"access_token": "{{NewApp}}", "expires_in": 7200}""")
                    : Json($$"""{"access_token": "{{NewUser}}"}""");
            }
            if (sent.Headers["Authorization"] is $"Bearer {NewApp}" or $"Bearer {NewUser}")
            {
                return Json("""{"categoryTreeId": "0", "orderId": "O-1"}""");
            }
            // Both calls are refused before either refreshes, so the second refresh cannot be skipped by accident.
            if (Interlocked.Increment(ref refused) == 2)
            {
                bothRefused.SetResult();
            }
            await bothRefused.Task;
            return Unauthorized();
        });
        using var client = Client(handler, new() { ClientId = AppId, ClientSecret = CertId, AppToken = App, UserToken = User, RefreshToken = Refresh });

        await Task.WhenAll(client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel), client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel));

        Assert.Equal(2, handler.Sent.Count(item => item.Path == TokenPath));
    }

    [Fact]
    public async Task ConcurrentFirstCallsMintOneAppToken()
    {
        var handler = new Router(async sent =>
        {
            if (sent.Path == TokenPath)
            {
                await Task.Delay(50);
                return Json($$"""{"access_token": "{{App}}", "expires_in": 7200}""");
            }
            return Json("""{"categoryTreeId": "0"}""");
        });
        using var client = Client(handler, new() { ClientId = AppId, ClientSecret = CertId });

        await Task.WhenAll(Enumerable.Range(0, 5).Select(_ => client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel)));

        Assert.Single(handler.Sent, item => item.Path == TokenPath);
    }

    [Fact]
    public async Task AnExplicitRefreshAndA401ShareOneTokenRequest()
    {
        var tokenRequested = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);
        var orderRefused = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);
        var handler = new Router(async sent =>
        {
            if (sent.Path == TokenPath)
            {
                tokenRequested.TrySetResult();
                return Json($$"""{"access_token": "{{NewUser}}"}""");
            }
            if (sent.Headers["Authorization"] == $"Bearer {NewUser}")
            {
                return Json("""{"orderId": "O-1"}""");
            }
            await tokenRequested.Task;
            orderRefused.TrySetResult();
            return Unauthorized();
        });
        using var client = Client(handler, new() { ClientId = AppId, ClientSecret = CertId, UserToken = User, RefreshToken = Refresh });

        var order = client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel);
        await client.OAuth.RefreshAsync(cancellationToken: Cancel);
        await orderRefused.Task;
        await order;

        Assert.Single(handler.Sent, item => item.Path == TokenPath);
    }

    [Fact]
    public async Task AUserOperationWithoutAUserTokenSendsNothing()
    {
        var handler = new Router(_ => Json("{}"));
        using var client = Client(handler, new() { ClientId = AppId, ClientSecret = CertId });

        var error = await Assert.ThrowsAsync<InvalidOperationException>(() => client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel));

        Assert.Contains("needs a user token", error.Message, StringComparison.Ordinal);
        Assert.Empty(handler.Sent);
    }

    [Fact]
    public async Task AnAppOperationFallsBackToTheUserToken()
    {
        var handler = new Router(_ => Json("""{"categoryTreeId": "0"}"""));
        using var client = Client(handler, new() { UserToken = User });

        await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel);

        Assert.Equal($"Bearer {User}", Assert.Single(handler.Sent).Headers["Authorization"]);
    }

    [Fact]
    public async Task ExchangingACodeStoresTheUserTokenAndRedactsTheCode()
    {
        const string Code = "synthetic-authorization-code";
        var lines = new Lines();
        EbayToken? stored = null;
        var handler = new Router(sent => sent.Path == TokenPath
            ? Json($$"""{"access_token": "{{NewUser}}", "expires_in": 7200, "refresh_token": "{{Refresh}}", "refresh_token_expires_in": 47304000}""")
            : Json($$"""{"errors": [{"errorId": 1, "message": "echo {{Code}} {{NewUser}}"}]}""", HttpStatusCode.BadRequest));
        using var client = Client(handler, new()
        {
            ClientId = AppId,
            ClientSecret = CertId,
            RuName = RuName,
            Logger = lines,
            OnToken = (token, _) =>
            {
                stored = token;
                return Task.CompletedTask;
            },
        });

        var token = await client.OAuth.ExchangeCodeAsync(Code, Cancel);
        var error = await Assert.ThrowsAsync<BadRequestException>(() => client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel));

        var sent = handler.Sent.ToArray();
        Assert.Equal($"grant_type=authorization_code&code={Code}&redirect_uri={RuName}", sent[0].Body);
        Assert.Equal($"Bearer {NewUser}", sent[1].Headers["Authorization"]);
        Assert.Equal(token, stored);
        Assert.Equal(47304000, token.RefreshTokenExpiresIn);
        Assert.DoesNotContain(Code, error.RawBody, StringComparison.Ordinal);
        Assert.DoesNotContain(NewUser, error.RawBody, StringComparison.Ordinal);
        Assert.DoesNotContain(NewUser, token.ToString(), StringComparison.Ordinal);
        Assert.DoesNotContain(Refresh, token.ToString(), StringComparison.Ordinal);
        Assert.All(lines.All, line => Assert.DoesNotContain(CertId, line, StringComparison.Ordinal));
    }

    [Fact]
    public async Task TheUserGrantNeedsAKeysetAndARuName()
    {
        using var noRuName = Client(new Router(_ => Json("{}")), new() { ClientId = AppId, ClientSecret = CertId });
        using var noKeyset = Client(new Router(_ => Json("{}")), new() { UserToken = User });

        Assert.Throws<InvalidOperationException>(() => noRuName.OAuth.CreateAuthorizationRequest(["scope"]));
        Assert.Throws<InvalidOperationException>(() => noKeyset.OAuth.CreateAuthorizationRequest(["scope"]));
        await Assert.ThrowsAsync<InvalidOperationException>(() => noKeyset.OAuth.GetAppTokenAsync(Cancel));
        await Assert.ThrowsAsync<InvalidOperationException>(() => noKeyset.OAuth.RefreshAsync(cancellationToken: Cancel));
    }

    [Fact]
    public void AuthorizationRequestsUseTheEnvironmentsEndpoint()
    {
        using var client = Client(new Router(_ => Json("{}")), new() { ClientId = AppId, ClientSecret = CertId, RuName = RuName, Environment = EbayClient.Sandbox });

        var request = client.OAuth.CreateAuthorizationRequest(["https://api.ebay.com/oauth/api_scope/sell.inventory", "https://api.ebay.com/oauth/api_scope/sell.account"], prompt: "login");
        var production = EbayOAuth.CreateAuthorizationRequest(AppId, RuName, EbayClient.Production, ["scope"], state: "given");

        Assert.Equal("https://auth.sandbox.ebay.com/oauth2/authorize", request.Url.GetLeftPart(UriPartial.Path));
        var query = Transport.QueryOf(request.Url.AbsoluteUri);
        Assert.Equal(AppId, query["client_id"]);
        Assert.Equal(RuName, query["redirect_uri"]);
        Assert.Equal("code", query["response_type"]);
        Assert.Equal("https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account", query["scope"]);
        Assert.Equal("login", query["prompt"]);
        Assert.Equal(request.State, query["state"]);
        Assert.True(request.State.Length >= 32);
        Assert.Equal("https://auth.ebay.com/oauth2/authorize", production.Url.GetLeftPart(UriPartial.Path));
        Assert.Equal("given", production.State);
        Assert.Throws<ArgumentException>(() => EbayOAuth.CreateAuthorizationRequest(AppId, RuName, "staging", ["scope"]));
        Assert.Throws<ArgumentException>(() => EbayOAuth.CreateAuthorizationRequest(AppId, RuName, EbayClient.Production, []));
    }

    [Fact]
    public async Task EachOperationGoesToItsHostInTheEnvironment()
    {
        var handler = new Router(_ => Json("{}"));
        using var client = Client(handler, new() { AppToken = App, UserToken = User, Environment = EbayClient.Sandbox });

        await client.Finances.SellerFunds.GetSummaryAsync(cancellationToken: Cancel);
        await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US", Cancel);

        var sent = handler.Sent.ToArray();
        Assert.Equal("https://apiz.sandbox.ebay.com/sell/finances/v1/seller_funds_summary", sent[0].Url);
        Assert.StartsWith("https://api.sandbox.ebay.com/", sent[1].Url, StringComparison.Ordinal);
        Assert.Equal("https://apim.ebay.com", EbayClient.Environments[EbayClient.Production]["apim"]);
    }

    [Fact]
    public void BadSettingsAreRejected()
    {
        Assert.Throws<ArgumentException>(() => new EbayClient(new EbayClientOptions()));
        Assert.Throws<ArgumentException>(() => new EbayClient(new EbayClientOptions { ClientId = AppId }));
        Assert.Throws<ArgumentException>(() => new EbayClient(new EbayClientOptions { UserToken = "bad\ntoken" }));
        Assert.Throws<ArgumentException>(() => new EbayClient(new EbayClientOptions { ClientId = AppId, ClientSecret = CertId, AppScopes = [] }));
        Assert.Throws<ArgumentException>(() => new EbayClient(new EbayClientOptions { ClientId = AppId, ClientSecret = CertId, AppScopes = [" "] }));
        Assert.Throws<ArgumentException>(() => new EbayClient(new EbayClientOptions { UserToken = User, Environment = "staging" }));
        Assert.Throws<ArgumentException>(() => new EbayClient(new EbayClientOptions { UserToken = User, Hosts = new Dictionary<string, string> { ["api"] = "https://mock.invalid" } }));
    }

    [Fact]
    public async Task HeaderDefaultsGoOnlyToOperationsThatDeclareThemAndACallsOwnValueWins()
    {
        var handler = new Router(_ => Json("{}"));
        using var client = Client(handler, new() { AppToken = App, UserToken = User, MarketplaceId = "EBAY_US", ContentLanguage = "en-US" });

        await client.Finances.SellerFunds.GetSummaryAsync(cancellationToken: Cancel);
        await client.Finances.SellerFunds.GetSummaryAsync(marketplaceId: "EBAY_GB", cancellationToken: Cancel);
        await client.Inventory.InventoryItems.CreateOrReplaceAsync("SKU-1", new Inventory.Models.InventoryItem(), cancellationToken: Cancel);
        await client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel);

        var sent = handler.Sent.ToArray();
        Assert.Equal("EBAY_US", sent[0].Headers["X-EBAY-C-MARKETPLACE-ID"]);
        Assert.Equal("EBAY_GB", sent[1].Headers["X-EBAY-C-MARKETPLACE-ID"]);
        Assert.Equal("en-US", sent[2].Headers["Content-Language"]);
        Assert.False(sent[3].Headers.ContainsKey("X-EBAY-C-MARKETPLACE-ID"));
        Assert.False(sent[3].Headers.ContainsKey("Content-Language"));
    }

    [Fact]
    public async Task ASigningKeySignsEveryRequest()
    {
        var (pem, body) = Ed25519Key();
        const string Jwe = "synthetic-public-key-jwe";
        var handler = new Router(_ => Json("""{"errors": [{"message": "echo"}]}""", HttpStatusCode.BadRequest));
        using var client = Client(handler, new() { UserToken = User, SigningKey = new EbaySigningKey(body, Jwe) });

        var error = await Assert.ThrowsAsync<BadRequestException>(() => client.Fulfillment.Orders.IssueRefundAsync("O-1", new Fulfillment.Models.IssueRefundRequest { ReasonForRefund = "BUYER_CANCEL" }, Cancel));
        await Assert.ThrowsAsync<BadRequestException>(() => client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel));

        var sent = handler.Sent.ToArray();
        Assert.Equal(Jwe, sent[0].Headers["x-ebay-signature-key"]);
        Assert.Equal(MessageSigner.ContentDigest(Encoding.UTF8.GetBytes(sent[0].Body)), sent[0].Headers["Content-Digest"]);
        Assert.Matches("""^sig1=\("content-digest" "x-ebay-signature-key" "@method" "@path" "@authority"\);created=[0-9]+$""", sent[0].Headers["Signature-Input"]);
        Assert.Matches("^sig1=:[A-Za-z0-9+/]+=*:$", sent[0].Headers["Signature"]);
        Assert.Matches("""^sig1=\("x-ebay-signature-key" "@method" "@path" "@authority"\);created=[0-9]+$""", sent[1].Headers["Signature-Input"]);
        Assert.False(sent[1].Headers.ContainsKey("Content-Digest"));
        Assert.Equal(pem, EbaySigningKey.Pem(body));
        Assert.Equal(pem, EbaySigningKey.Pem(pem));
        Assert.DoesNotContain(body, new EbaySigningKey(body, Jwe).ToString(), StringComparison.Ordinal);
        Assert.NotNull(error.Status);
    }

    [Fact]
    public async Task AFileGoesAsAnOctetStreamPart()
    {
        var handler = new Router(_ => Json("""{"fileId": "F-1"}"""));
        using var client = Client(handler, new() { UserToken = User });

        var evidence = await client.Fulfillment.PaymentDisputes.UploadEvidenceFileAsync("D-1", new UploadFile("evidence.jpg", "synthetic-evidence"u8.ToArray()), Cancel);

        var sent = Assert.Single(handler.Sent);
        Assert.Equal("F-1", evidence.FileId);
        Assert.StartsWith("https://apiz.mock.invalid/", sent.Url, StringComparison.Ordinal);
        Assert.StartsWith("multipart/form-data; boundary=", sent.Headers["Content-Type"], StringComparison.Ordinal);
        Assert.Contains("Content-Type: application/octet-stream", sent.Body, StringComparison.Ordinal);
        Assert.Contains("synthetic-evidence", sent.Body, StringComparison.Ordinal);
    }

    [Fact]
    public async Task APostOrderUploadSendsTheUserTokenTheMarketplaceAndAJsonFile()
    {
        var handler = new Router(_ => Json("""{"fileId": "F-1"}"""));
        using var client = Client(handler, new() { AppToken = App, UserToken = User, MarketplaceId = "EBAY_GB" });

        var file = await client.PostOrder.Returns.UploadFileAsync("5000000001", new PostOrder.Models.UploadFileRequest { Data = "c3ludGhldGlj", FilePurpose = PostOrder.Models.FilePurposeEnum.LabelRelated }, cancellationToken: Cancel);

        var sent = Assert.Single(handler.Sent);
        Assert.Equal("F-1", file.FileId);
        Assert.Equal("https://api.mock.invalid/post-order/v2/return/5000000001/file/upload", sent.Url);
        Assert.Equal($"Bearer {User}", sent.Headers["Authorization"]);
        Assert.Equal("EBAY_GB", sent.Headers["X-EBAY-C-MARKETPLACE-ID"]);
        Assert.StartsWith("application/json", sent.Headers["Content-Type"], StringComparison.Ordinal);
        using var body = System.Text.Json.JsonDocument.Parse(sent.Body);
        Assert.Equal("c3ludGhldGlj", body.RootElement.GetProperty("data").GetString());
        Assert.Equal("LABEL_RELATED", body.RootElement.GetProperty("filePurpose").GetString());
    }

    [Fact]
    public async Task ALinkPageWithoutItsItemsIsADecodeError()
    {
        var handler = new Router(_ => Json("""{"total": 0}"""));
        using var client = Client(handler, new() { UserToken = User });

        await Assert.ThrowsAsync<ApiDecodeException>(async () => await client.Fulfillment.Orders.ListAllAsync(cancellationToken: Cancel).ToListAsync(Cancel));
    }

    [Fact]
    public async Task ErrorsCarryTheFirstErrorAndTheWholeList()
    {
        var handler = new Router(_ => Json(
            """{"errors": [{"errorId": 32100, "domain": "API_FULFILLMENT", "category": "REQUEST", "message": "Invalid order ID", "parameters": [{"name": "orderId", "value": "O-1"}]}, "not an object", {"errorId": "x"}]}""",
            HttpStatusCode.NotFound));
        using var client = Client(handler, new() { UserToken = User });

        var error = await Assert.ThrowsAsync<NotFoundException>(() => client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel));

        Assert.Equal("not_found", error.Kind);
        Assert.Equal(404, error.Status);
        Assert.Equal("32100", error.Code);
        Assert.Equal("Invalid order ID", error.Detail);
        Assert.Equal("HTTP 404: Invalid order ID", error.Message);
        Assert.Equal(2, error.Errors.Count);
        Assert.Equal("API_FULFILLMENT", error.Errors[0].Domain);
        Assert.Equal(KeyValuePair.Create<string?, string?>("orderId", "O-1"), Assert.Single(error.Errors[0].Parameters));
        Assert.Null(error.Errors[1].ErrorId);
    }

    [Theory]
    [InlineData(400, typeof(BadRequestException))]
    [InlineData(401, typeof(AuthenticationException))]
    [InlineData(403, typeof(PermissionDeniedException))]
    [InlineData(409, typeof(ConflictException))]
    [InlineData(422, typeof(UnprocessableException))]
    [InlineData(418, typeof(HttpException))]
    public async Task StatusesMapToExceptions(int status, Type type)
    {
        var handler = new Router(_ => Json("{}", (HttpStatusCode)status));
        using var client = Client(handler, new() { UserToken = User });

        var error = await Assert.ThrowsAnyAsync<HttpException>(() => client.Fulfillment.Orders.GetAsync("O-1", cancellationToken: Cancel));

        Assert.Equal(type, error.GetType());
        Assert.Null(error.Code);
        Assert.Empty(error.Errors);
    }

    private static (string Pem, string Body) Ed25519Key()
    {
        var generator = new Ed25519KeyPairGenerator();
        generator.Init(new Ed25519KeyGenerationParameters(new SecureRandom()));
        var body = Convert.ToBase64String(PrivateKeyInfoFactory.CreatePrivateKeyInfo(generator.GenerateKeyPair().Private).GetEncoded());
        var lines = body.Chunk(64).Select(line => new string(line));
        return (string.Join('\n', ["-----BEGIN PRIVATE KEY-----", .. lines, "-----END PRIVATE KEY-----"]), body);
    }

    private static HttpResponseMessage Json(string body, HttpStatusCode status = HttpStatusCode.OK) =>
        new(status) { Content = new StringContent(body, Encoding.UTF8, "application/json") };

    private static HttpResponseMessage Unauthorized() =>
        Json("""{"errors": [{"errorId": 1001, "message": "Invalid access token"}]}""", HttpStatusCode.Unauthorized);

    private sealed record Sent(string Url, string Path, Dictionary<string, string> Headers, string Body);

    private sealed class Clock : TimeProvider
    {
        public DateTimeOffset Now { get; set; } = new(2026, 1, 1, 0, 0, 0, TimeSpan.Zero);

        public override DateTimeOffset GetUtcNow() => Now;
    }

    private sealed class Router(Func<Sent, Task<HttpResponseMessage>> respond) : HttpMessageHandler
    {
        public Router(Func<Sent, HttpResponseMessage> respond)
            : this(sent => Task.FromResult(respond(sent)))
        {
        }

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
            return await respond(sent);
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
