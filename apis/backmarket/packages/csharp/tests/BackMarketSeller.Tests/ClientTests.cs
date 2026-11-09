using System.IO.Compression;
using System.Net;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using BackMarketSeller.Models;
using BackMarketSeller.Runtime;
using Microsoft.Extensions.Logging;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class ClientTests
{
    private const string Token = "synthetic-token";

    private static BackMarketClient Client(ScriptedHandler handler, ILogger? logger = null, int maxRetries = 3) =>
        new(Token, new BackMarketClientOptions
        {
            UserAgent = "BM-Example-Tests;tests@example.com",
            Locale = "fr-fr",
            BaseUrl = new Uri("https://mock.invalid/"),
            RetryBaseDelay = TimeSpan.FromMilliseconds(1),
            RateLimitWait = TimeSpan.FromMilliseconds(1),
            MaxRetries = maxRetries,
            Logger = logger,
            HttpHandler = handler,
        });

    [Fact]
    public async Task SendsTheTokenVerbatimWithTheRequiredHeaders()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.OK, """{"order_id": 1}"""));
        using var client = Client(handler);

        await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);

        var request = Assert.Single(handler.Requests);
        Assert.Equal("https://mock.invalid/ws/orders/1", request.Url);
        Assert.Equal($"Basic {Token}", request.Headers["Authorization"]);
        Assert.Equal("BM-Example-Tests;tests@example.com", request.Headers["User-Agent"]);
        Assert.Equal("fr-fr", request.Headers["Accept-Language"]);
    }

    [Theory]
    [InlineData("")]
    [InlineData(".")]
    [InlineData("..")]
    public async Task RejectsAnEmptyOrDotPathValueBeforeSending(string value)
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.OK, "{}"));
        using var client = Client(handler);
        var cancellationToken = TestContext.Current.CancellationToken;

        var read = await Assert.ThrowsAsync<ArgumentException>(() => client.Buyback.GetOrderAsync(value, cancellationToken));
        var write = await Assert.ThrowsAsync<ArgumentException>(() => client.Listings.UpdateAsync(value, new ListingUpdate(), cancellationToken));
        var missing = await Assert.ThrowsAsync<ArgumentNullException>(() => client.Listings.UpdateAsync(null!, new ListingUpdate(), cancellationToken));

        Assert.Equal("buybackOrderId", read.ParamName);
        Assert.Equal("listingId", write.ParamName);
        Assert.Equal("listingId", missing.ParamName);
        Assert.Empty(handler.Requests);
    }

    [Fact]
    public async Task KeepsValuesThatDoNotFitAndUnknownFieldsInExtra()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.OK, """{"order_id": "not-a-number", "state": 99, "is_backship": null, "surprise": [1]}"""));
        using var client = Client(handler);

        var order = await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);

        Assert.Null(order.OrderId);
        Assert.Equal((OrderState)99, order.State);
        Assert.Equal("not-a-number", order.Extra["order_id"].GetString());
        Assert.Equal(JsonValueKind.Null, order.Extra["is_backship"].ValueKind);
        Assert.Equal("[1]", order.Extra["surprise"].GetRawText());
        var written = JsonDocument.Parse(JsonSerializer.Serialize(order)).RootElement;
        Assert.Equal("not-a-number", written.GetProperty("order_id").GetString());
        Assert.Equal(99, written.GetProperty("state").GetInt32());
        Assert.Equal(JsonValueKind.Null, written.GetProperty("is_backship").ValueKind);
    }

    [Fact]
    public void AnUnlistedEnumValueGoesToExtra()
    {
        var order = JsonSerializer.Deserialize<UpdateOrder>("""{"order_id": 1, "country_code": "xx-xx"}""")!;

        Assert.Equal(1, order.OrderId);
        Assert.Equal("xx-xx", order.Extra["country_code"].GetString());
    }

    [Fact]
    public void AnOptionalReferenceIsTyped()
    {
        var competitor = JsonSerializer.Deserialize<Competitor>("""{"min_price": {"amount": "1.00", "currency": "EUR"}, "market": "FR"}""")!;

        Assert.Equal("1.00", competitor.MinPrice?.Amount);
        Assert.Equal(MarketCode.Fr, competitor.Market);
    }

    [Fact]
    public async Task ASetPropertyWinsOverTheRawValueItReplaced()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.OK, """{"order_id": "bad"}"""));
        using var client = Client(handler);
        var order = await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);

        order.OrderId = 2;

        Assert.Equal("""{"order_id":2}""", JsonSerializer.Serialize(order));
    }

    [Fact]
    public async Task PaginationReadsOnlyThePositionOutOfNext()
    {
        var handler = new ScriptedHandler(
            Json(HttpStatusCode.OK, """{"next": "https://foreign.invalid/ws/orders?page=2&page-size=99", "results": [{"order_id": 1}]}"""),
            Json(HttpStatusCode.OK, """{"next": null, "results": [{"order_id": 2}]}"""));
        using var client = Client(handler);

        var orders = await client.Orders.ListAllAsync(pageSize: 5, cancellationToken: TestContext.Current.CancellationToken).ToListAsync(TestContext.Current.CancellationToken);

        Assert.Equal([1L, 2L], orders.Select(order => order.OrderId!.Value));
        Assert.Equal("https://mock.invalid/ws/orders?page-size=5", handler.Requests[0].Url);
        Assert.Equal("https://mock.invalid/ws/orders?page=2&page-size=5", handler.Requests[1].Url);
    }

    [Fact]
    public async Task AnEmpty204PageEndsIteration()
    {
        var handler = new ScriptedHandler(
            Json(HttpStatusCode.OK, """{"next": "https://mock.invalid/ws/orders?page=2", "results": [{"order_id": 1}]}"""),
            new HttpResponseMessage(HttpStatusCode.NoContent));
        using var client = Client(handler);

        var orders = await client.Orders.ListAllAsync(cancellationToken: TestContext.Current.CancellationToken).ToListAsync(TestContext.Current.CancellationToken);

        Assert.Equal([1L], orders.Select(order => order.OrderId!.Value));
        Assert.Equal(2, handler.Requests.Count);
    }

    private static readonly Operation OffsetList = new(
        "list-items", "GET", "/items", "Items", "ListAsync", "ListAllAsync",
        [new("limit", "limit", ParamLocation.Query), new("start", "start", ParamLocation.Query)],
        ReturnsJson: true,
        Paging: new OffsetPaging("data", "total", "start"));

    private static object?[]? Next(Operation operation, object?[] values, string page, int received) =>
        Transport.NextValues(operation, values, JsonDocument.Parse(page).RootElement, received);

    [Fact]
    public void OffsetPagingAdvancesByTheItemsReceivedUntilTheTotal()
    {
        Assert.Equal([2L, 2L], Next(OffsetList, [2L, null], """{"total": 5, "data": []}""", 2));
        Assert.Equal([2L, 6L], Next(OffsetList, [2L, 4L], """{"total": 7, "data": []}""", 2));
        Assert.Null(Next(OffsetList, [2L, 4L], """{"total": 5, "data": []}""", 1));
    }

    [Fact]
    public void OffsetPagingStartsAtTheCallersOffsetAndStopsAtAnEmptyPage()
    {
        Assert.Equal([null, 4L], Next(OffsetList, [null, 3L], """{"total": null, "data": []}""", 1));
        Assert.Null(Next(OffsetList, [null, 4L], """{"data": []}""", 0));
    }

    [Fact]
    public void OffsetPagingStopsAtATotalThatIsNotAnInteger()
    {
        Assert.Null(Next(OffsetList, [null, null], """{"total": 2.0, "data": []}""", 2));
    }

    [Theory]
    [InlineData("later")]
    [InlineData(2.5)]
    public void OffsetPagingRejectsAnOffsetThatIsNotAnInteger(object start)
    {
        var error = Assert.Throws<ApiDecodeException>(() => Next(OffsetList, [null, start], """{"data": []}""", 1));
        Assert.Contains("`start` parameter is not an integer", error.Message);
    }

    [Theory]
    [InlineData("""{"total": 1}""")]
    [InlineData("""{"data": null}""")]
    [InlineData("""{"data": {}}""")]
    public void OffsetPagingRejectsAPageWithoutAnItemsList(string page)
    {
        Assert.Throws<ApiDecodeException>(() => Next(OffsetList, [null, null], page, 0));
    }

    [Fact]
    public async Task OffsetPagingReadsItemsFromTheConfiguredField()
    {
        var handler = new ScriptedHandler(
            Json(HttpStatusCode.OK, """{"total": 3, "data": [{"n": 0}, {"n": 1}], "results": [{"n": 9}]}"""),
            Json(HttpStatusCode.OK, """{"total": 3, "data": [{"n": 2}]}"""));
        var settings = new Settings
        {
            BaseUrl = "https://mock.invalid",
            Credentials = new StaticCredentials(new Dictionary<string, string>(), [Token]),
            Headers = new Dictionary<string, string>(),
            ToError = context => new ApiException($"status {context.Status}"),
            Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
        };
        using var transport = new Transport(settings, new HttpClient(handler), ownsClient: true);

        var items = await transport.PaginateAsync<JsonElement>(OffsetList, [2L, null], TestContext.Current.CancellationToken)
            .ToListAsync(TestContext.Current.CancellationToken);

        Assert.Equal([0, 1, 2], items.Select(item => item.GetProperty("n").GetInt32()));
        Assert.Equal("https://mock.invalid/items?limit=2", handler.Requests[0].Url);
        Assert.Equal("https://mock.invalid/items?limit=2&start=2", handler.Requests[1].Url);
    }

    private static readonly Operation CursorList = OffsetList with
    {
        Params = [new("limit", "limit", ParamLocation.Query), new("start_after", "startAfter", ParamLocation.Query)],
        Paging = new CursorPaging("data", "page.next_page", "start_after"),
    };

    [Fact]
    public void CursorPagingSendsTheNextValueBackAndKeepsTheCallersParameters()
    {
        Assert.Equal(new object?[] { 2L, "b" }, Next(CursorList, [2L, null], """{"data": [{}], "page": {"next_page": "b"}}""", 1));
        Assert.Equal(new object?[] { 2L, "c" }, Next(CursorList, [2L, "b"], """{"data": [{}], "page": {"next_page": "c"}}""", 1));
    }

    [Theory]
    [InlineData("""{"data": [], "page": {"next_page": null}}""")]
    [InlineData("""{"data": [], "page": {"next_page": ""}}""")]
    [InlineData("""{"data": [], "page": {}}""")]
    [InlineData("""{"data": [], "page": null}""")]
    [InlineData("""{"data": []}""")]
    public void CursorPagingStopsAtANullEmptyOrAbsentNextValue(string page)
    {
        Assert.Null(Next(CursorList, [null, "a"], page, 0));
    }

    [Fact]
    public void CursorPagingSendsAnIntegerNextValueBackAsItsDigits()
    {
        Assert.Equal(new object?[] { null, "0" }, Next(CursorList, [null, null], """{"data": [{}], "page": {"next_page": 0}}""", 1));
        Assert.Equal(new object?[] { null, "7" }, Next(CursorList, [null, "0"], """{"data": [{}], "page": {"next_page": 7}}""", 1));
        Assert.Equal(new object?[] { null, "1" }, Next(CursorList, [null, null], """{"data": [{}], "page": {"next_page": 1.0}}""", 1));
        Assert.Equal(new object?[] { null, "9007199254740991" }, Next(CursorList, [null, null], """{"data": [{}], "page": {"next_page": 9007199254740991}}""", 1));
    }

    [Theory]
    [InlineData("a", """{"data": [{}], "page": {"next_page": "a"}}""")]
    [InlineData("3", """{"data": [{}], "page": {"next_page": 3}}""")]
    [InlineData(3L, """{"data": [{}], "page": {"next_page": 3}}""")]
    public void CursorPagingRejectsANextValueEqualToTheOneSent(object sent, string page)
    {
        var error = Assert.Throws<ApiDecodeException>(() => Next(CursorList, [null, sent], page, 1));
        Assert.Contains("does not advance the iteration", error.Message);
    }

    [Theory]
    [InlineData("""{"page": {"next_page": "b"}}""")]
    [InlineData("""{"data": [{}], "page": {"next_page": 2.5}}""")]
    [InlineData("""{"data": [{}], "page": {"next_page": 9007199254740992}}""")]
    [InlineData("""{"data": [{}], "page": {"next_page": -9223372036854775808}}""")]
    [InlineData("""{"data": [{}], "page": {"next_page": 1e400}}""")]
    [InlineData("""{"data": [{}], "page": {"next_page": true}}""")]
    [InlineData("""{"data": [{}], "page": {"next_page": {"id": "b"}}}""")]
    [InlineData("""{"data": [{}], "page": "b"}""")]
    public void CursorPagingRejectsAMalformedPage(string page)
    {
        Assert.Throws<ApiDecodeException>(() => Next(CursorList, [null, null], page, 1));
    }

    [Fact]
    public void NextLinkPagingReadsTheConfiguredFields()
    {
        var operation = OffsetList with
        {
            Params = [new("token", "token", ParamLocation.Query)],
            Paging = new NextLinkPaging("data", "more", ["token"]),
        };

        Assert.Equal(["b"], Next(operation, [null], """{"data": [], "more": "/items?token=b", "next": "/items?token=c"}""", 1));
        Assert.Null(Next(operation, ["b"], """{"data": [], "more": null, "next": "/items?token=c"}""", 1));
        Assert.Throws<ApiDecodeException>(() => Next(operation, ["b"], """{"results": [], "more": null}""", 1));
    }

    [Fact]
    public async Task ANextLinkThatDoesNotAdvanceIsADecodeError()
    {
        var page = """{"next": "%%not a url", "results": []}""";
        var handler = new ScriptedHandler(Json(HttpStatusCode.OK, page), Json(HttpStatusCode.OK, page));
        using var client = Client(handler);

        await Assert.ThrowsAsync<ApiDecodeException>(async () =>
            await client.Orders.ListAllAsync(cancellationToken: TestContext.Current.CancellationToken).ToListAsync(TestContext.Current.CancellationToken));
    }

    [Fact]
    public async Task ABlankPositionInNextIsADecodeError()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.OK, """{"results": [], "next": "https://mock.invalid/ws/orders?page="}"""));
        using var client = Client(handler);

        await Assert.ThrowsAsync<ApiDecodeException>(async () =>
            await client.Orders.ListAllAsync(cancellationToken: TestContext.Current.CancellationToken).ToListAsync(TestContext.Current.CancellationToken));
    }

    [Theory]
    [InlineData("application/json")]
    [InlineData(null)]
    public async Task AnEmptySuccessIsADecodeErrorWhereTheSpecDeclaresJson(string? contentType)
    {
        var content = new ByteArrayContent([]);
        if (contentType is not null)
        {
            content.Headers.ContentType = new(contentType);
        }
        using var client = Client(new ScriptedHandler(new HttpResponseMessage(HttpStatusCode.OK) { Content = content }));

        var error = await Assert.ThrowsAsync<ApiDecodeException>(() => client.Orders.GetAsync(1, TestContext.Current.CancellationToken));

        Assert.Equal(200, error.Status);
    }

    [Fact]
    public async Task AnEmptySuccessIsADecodeErrorWhereTheSpecDeclaresJsonEvenForAString()
    {
        var options = new BackMarketClientOptions { UserAgent = "BM-Example-Tests;tests@example.com", Locale = "fr-fr", BaseUrl = new Uri("https://mock.invalid/") };
        var handler = new ScriptedHandler(new HttpResponseMessage(HttpStatusCode.OK), new HttpResponseMessage(HttpStatusCode.OK), new HttpResponseMessage(HttpStatusCode.OK));
        using var transport = new Transport(BackMarketClient.CreateSettings(Token, options, null), Transport.OwnClient(handler), ownsClient: true);
        Operation Op(bool returnsJson) => new("op", "GET", "/x", "r", "n", null, [], returnsJson);
        var cancellationToken = TestContext.Current.CancellationToken;

        Assert.Equal("", await transport.CallAsync<string>(Op(false), [], cancellationToken));
        await Assert.ThrowsAsync<ApiDecodeException>(() => transport.CallAsync<string>(Op(true), [], cancellationToken));
        await Assert.ThrowsAsync<ApiDecodeException>(() => transport.SendAsync(Op(true), [], cancellationToken));
    }

    [Fact]
    public async Task AnEmpty204IsNoResultEvenWhereTheSpecDeclaresJson()
    {
        var options = new BackMarketClientOptions { UserAgent = "BM-Example-Tests;tests@example.com", Locale = "fr-fr", BaseUrl = new Uri("https://mock.invalid/") };
        var handler = new ScriptedHandler(new HttpResponseMessage(HttpStatusCode.NoContent), new HttpResponseMessage(HttpStatusCode.NoContent));
        using var transport = new Transport(BackMarketClient.CreateSettings(Token, options, null), Transport.OwnClient(handler), ownsClient: true);
        var operation = new Operation("op", "GET", "/x", "r", "n", null, [], ReturnsJson: true);
        var cancellationToken = TestContext.Current.CancellationToken;

        Assert.Null(await transport.CallAsync<Order>(operation, [], cancellationToken));
        await transport.SendAsync(operation, [], cancellationToken);
    }

    [Fact]
    public async Task AnEmptySuccessIsFineWhereTheSpecDeclaresNoJson()
    {
        using var client = Client(new ScriptedHandler(new HttpResponseMessage(HttpStatusCode.Created), new HttpResponseMessage(HttpStatusCode.Created)));

        await client.Care.TransferItemAsync(1, new PostItemTransferCreateRequest(), TestContext.Current.CancellationToken);
        Assert.Equal("", await client.Care.CreateRefundAsync(new PostRefundCreateRequest(), TestContext.Current.CancellationToken));
    }

    [Theory]
    [InlineData(10)]
    [InlineData(30)]
    [InlineData(-8)]
    public async Task ATruncatedCompressedSuccessIsADecodeError(int cut)
    {
        var body = Gzip("""{"order_id": 1, "delivery_note": "synthetic"}""");
        using var client = Client(new ScriptedHandler(Gzipped(HttpStatusCode.OK, cut < 0 ? body[..^-cut] : body[..cut])));

        var error = await Assert.ThrowsAsync<ApiDecodeException>(() => client.Orders.GetAsync(1, TestContext.Current.CancellationToken));

        Assert.Equal(200, error.Status);
    }

    [Fact]
    public async Task ACompressedSuccessReadsEveryMember()
    {
        byte[] body = [.. Gzip("""{"order_id": 1, """), .. Gzip("\"delivery_note\": \"synthetic\"}")];
        using var client = Client(new ScriptedHandler(Gzipped(HttpStatusCode.OK, body)));

        var order = await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);

        Assert.Equal(1, order.OrderId);
        Assert.Equal("synthetic", order.DeliveryNote);
    }

    [Fact]
    public async Task IterationRejectsANextLinkThatIsNotAUrl()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.OK, """{"next": "http://[", "results": [{"order_id": 1}]}"""));
        using var client = Client(handler);
        var ids = new List<long>();

        var error = await Assert.ThrowsAsync<ApiDecodeException>(async () =>
        {
            await foreach (var order in client.Orders.ListAllAsync(cancellationToken: TestContext.Current.CancellationToken))
            {
                ids.Add(order.OrderId!.Value);
            }
        });

        Assert.Equal([1L], ids);
        Assert.Contains("not a valid URL", error.Message);
        Assert.Single(handler.Requests);
    }

    [Theory]
    [InlineData(403, """{"errors": [{"code": "bot-need-challenge"}]}""", null, typeof(BotChallengeException))]
    [InlineData(403, "<html>blocked</html>", "0000-AAA", typeof(WafBlockedException))]
    [InlineData(403, "{}", null, typeof(PermissionDeniedException))]
    [InlineData(404, "", null, typeof(NotFoundException))]
    [InlineData(418, "", null, typeof(ApiException))]
    public async Task MapsErrorsOnStatusFirst(int status, string body, string? cfRay, Type expected)
    {
        var response = new HttpResponseMessage((HttpStatusCode)status) { Content = new StringContent(body) };
        if (cfRay is not null)
        {
            response.Headers.Add("cf-ray", cfRay);
        }
        using var client = Client(new ScriptedHandler(response));

        var error = await Assert.ThrowsAnyAsync<ApiException>(() => client.Orders.GetAsync(1, TestContext.Current.CancellationToken));

        Assert.IsType(expected, error);
        Assert.Equal(status, error.Status);
        Assert.Equal(cfRay, error.CfRay);
    }

    [Fact]
    public async Task ANumericErrorCodeReadsAsText()
    {
        using var client = Client(new ScriptedHandler(Json(HttpStatusCode.BadRequest, """{"error": {"code": 12}, "requestId": "request-1"}""")));

        var error = await Assert.ThrowsAsync<BadRequestException>(() => client.Orders.GetAsync(1, TestContext.Current.CancellationToken));

        Assert.Equal("12", error.Code);
        Assert.Equal("request-1", error.RequestId);
    }

    [Fact]
    public async Task KeepsTheTokenOutOfErrorsAndLogs()
    {
        var logger = new ListLogger();
        var handler = new ScriptedHandler(
            Json(HttpStatusCode.InternalServerError, $$$"""{"echo": "{{{Token}}}"}"""),
            Json(HttpStatusCode.Unauthorized, $$$"""{"error": {"code": "bad-token", "message": "{{{Token}}}"}}"""));
        using var client = Client(handler, logger);

        var error = await Assert.ThrowsAsync<AuthenticationException>(() => client.Orders.GetAsync(1, TestContext.Current.CancellationToken));

        Assert.DoesNotContain(Token, error.RawBody);
        Assert.NotEmpty(logger.Lines);
        Assert.All(logger.Lines, entry => Assert.DoesNotContain(Token, entry));
    }

    [Fact]
    public async Task ASuccessBodyIsReturnedAsItIs()
    {
        using var client = Client(new ScriptedHandler(Json(HttpStatusCode.OK, $$"""{"order_id": 1, "delivery_note": "{{Token}}"}""")));

        var order = await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);

        Assert.Equal(Token, order.DeliveryNote);
    }

    [Fact]
    public async Task NeverRepeatsAFailedPost()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.InternalServerError, "{}"), Json(HttpStatusCode.OK, "{}"));
        using var client = Client(handler);

        await Assert.ThrowsAsync<ServerException>(() => client.Care.CreateRefundAsync(new PostRefundCreateRequest(), TestContext.Current.CancellationToken));

        Assert.Single(handler.Requests);
    }

    [Fact]
    public async Task CallerCancellationIsNotAnApiError()
    {
        using var cancel = new CancellationTokenSource();
        var handler = new ScriptedHandler(_ =>
        {
            cancel.Cancel();
            throw new TaskCanceledException();
        });
        using var client = Client(handler);

        var error = await Assert.ThrowsAnyAsync<OperationCanceledException>(() => client.Orders.GetAsync(1, cancel.Token));

        Assert.IsNotAssignableFrom<ApiException>(error);
    }

    [Fact]
    public async Task MultipartFieldsAreTextAndFiles()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.Created, """{"id": 1}"""));
        using var client = Client(handler);

        await client.Care.SendMessageAsync(1, "hello", [new UploadFile("note.txt", "body"u8.ToArray())], TestContext.Current.CancellationToken);

        var request = Assert.Single(handler.Requests);
        Assert.StartsWith("multipart/form-data", request.Headers["Content-Type"]);
        Assert.Contains("name=\"message\"", request.Body);
        Assert.Contains("filename=\"note.txt\"", request.Body);
        Assert.DoesNotContain("filename*", request.Body);
    }

    [Fact]
    public async Task MultipartNonAsciiFileNameIsSentAsFileNameStar()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.Created, """{"id": 1}"""));
        using var client = Client(handler);

        await client.Care.SendMessageAsync(1, "hello", [new UploadFile("été.pdf", "body"u8.ToArray())], TestContext.Current.CancellationToken);

        var match = Regex.Match(Assert.Single(handler.Requests).Body, "filename\\*=utf-8''([^;\\r\\n]+)");
        Assert.True(match.Success);
        Assert.Equal("été.pdf", Uri.UnescapeDataString(match.Groups[1].Value));
    }

    [Fact]
    public async Task MultipartFileNameQuoteIsEscaped()
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.Created, """{"id": 1}"""));
        using var client = Client(handler);

        await client.Care.SendMessageAsync(1, "hello", [new UploadFile("a\"b\\c.txt", "body"u8.ToArray())], TestContext.Current.CancellationToken);

        var body = Assert.Single(handler.Requests).Body;
        Assert.Contains("filename=\"a\\\"b\\\\c.txt\"", body);
        Assert.DoesNotContain("filename*", body);
    }

    [Theory]
    [InlineData("a\r\nb.txt")]
    [InlineData("")]
    public async Task MultipartFileNameThatCannotBeAHeaderFailsBeforeSending(string name)
    {
        var handler = new ScriptedHandler(Json(HttpStatusCode.Created, """{"id": 1}"""));
        using var client = Client(handler);

        var error = await Assert.ThrowsAsync<ArgumentException>(
            () => client.Care.SendMessageAsync(1, "hello", [new UploadFile(name, "body"u8.ToArray())], TestContext.Current.CancellationToken));

        Assert.Equal("FileName", error.ParamName);
        Assert.Empty(handler.Requests);
    }

    [Theory]
    [InlineData("2", 2.0)]
    [InlineData("soon", null)]
    [InlineData("Thu, 01 Jan 2015 00:00:00 GMT", null)]
    [InlineData("Sun, 01 Nov 2026 00:00:30 GMT", 30.0)]
    [InlineData("Sunday, 01-Nov-26 00:00:30 GMT", 30.0)]
    [InlineData("Sun Nov  1 00:00:30 2026", 30.0)]
    [InlineData("1 Nov 2026 00:00:30 GMT", 30.0)]
    [InlineData("Mon, 01 Nov 2026 00:00:30 UT", 30.0)]
    [InlineData("Sun, 01 Nov 2026 00:01", 60.0)]
    [InlineData("Sun, 01 Nov 2026 01:00:30 +0100", 30.0)]
    [InlineData("Sat, 31 Oct 2026 19:00:30 EST", 30.0)]
    [InlineData("Sun, 31 Nov 2026 00:00:30 GMT", null)]
    public void ReadsRetryAfterAsSecondsOrADate(string value, double? expected)
    {
        var now = new DateTimeOffset(2026, 11, 1, 0, 0, 0, TimeSpan.Zero);

        Assert.Equal(expected, Transport.RetryAfterSeconds(value, now));
    }

    [Fact]
    public void ARetryAfterTooLongForANumberIsStillANumber()
    {
        Assert.True(Transport.RetryAfterSeconds(new string('9', 400), DateTimeOffset.UtcNow) > 3600);
    }

    [Fact]
    public void RequiresExactlyOneOfRegionAndBaseUrl()
    {
        Assert.Throws<ArgumentException>(() => new BackMarketClient(Token, new BackMarketClientOptions { UserAgent = "BM-A-B;a@example.com", Locale = "fr-fr" }));
        Assert.Throws<ArgumentException>(() => new BackMarketClient("", new BackMarketClientOptions { UserAgent = "BM-A-B;a@example.com", Locale = "fr-fr", Region = Region.EU }));
    }

    private static HttpResponseMessage Json(HttpStatusCode status, string body) =>
        new(status) { Content = new StringContent(body, Encoding.UTF8, "application/json") };

    private static byte[] Gzip(string text)
    {
        using var output = new MemoryStream();
        using (var gzip = new GZipStream(output, CompressionLevel.Optimal))
        {
            gzip.Write(Encoding.UTF8.GetBytes(text));
        }
        return output.ToArray();
    }

    private static HttpResponseMessage Gzipped(HttpStatusCode status, byte[] body)
    {
        var content = new ByteArrayContent(body);
        content.Headers.ContentType = new("application/json");
        content.Headers.ContentEncoding.Add("gzip");
        return new(status) { Content = content };
    }

    private sealed record Sent(string Url, Dictionary<string, string> Headers, string Body);

    private sealed class ScriptedHandler(Func<HttpRequestMessage, HttpResponseMessage> respond) : HttpMessageHandler
    {
        private readonly Queue<HttpResponseMessage> responses = new();

        public ScriptedHandler(params HttpResponseMessage[] responses)
            : this(_ => throw new InvalidOperationException("script exhausted"))
        {
            foreach (var response in responses)
            {
                this.responses.Enqueue(response);
            }
        }

        public List<Sent> Requests { get; } = [];

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var headers = request.Headers.NonValidated.ToDictionary(header => header.Key, header => header.Value.ToString());
            var body = request.Content is null ? string.Empty : await request.Content.ReadAsStringAsync(cancellationToken);
            if (request.Content is not null)
            {
                foreach (var header in request.Content.Headers.NonValidated)
                {
                    headers[header.Key] = header.Value.ToString();
                }
            }
            Requests.Add(new Sent(request.RequestUri!.ToString(), headers, body));
            return responses.TryDequeue(out var response) ? response : respond(request);
        }
    }

    private sealed class ListLogger : ILogger
    {
        public List<string> Lines { get; } = [];

        public IDisposable? BeginScope<TState>(TState state)
            where TState : notnull => null;

        public bool IsEnabled(LogLevel logLevel) => true;

        public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception? exception, Func<TState, Exception?, string> formatter) =>
            Lines.Add(formatter(state, exception));
    }
}
