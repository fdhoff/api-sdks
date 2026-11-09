using System.Collections.Concurrent;
using System.Diagnostics;
using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using BackMarketSeller.Runtime;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class JobTests
{
    private const string Secret = "synthetic-secret";
    private const string Base = "https://api.example.test";
    private const string Csv = "id;error\n1;none\n";

    // A synthetic start and status pair. Only the status operation is polled.
    private static readonly Operation Start = new(
        "startImport", "POST", "/imports", "Imports", "StartAsync", null, [], ReturnsJson: true, Security: [[new("key", [])]]);

    private static readonly Operation Status = new(
        "getImport", "GET", "/imports/{import_id}", "Imports", "GetAsync", null,
        [new("import_id", "importId", ParamLocation.Path), new("verbose", "verbose", ParamLocation.Query)], ReturnsJson: true,
        Security: [[new("key", [])]], Job: new JobPolling("progress.state", ["COMPLETE"], ["FAILED"]));

    private static CancellationToken Token => TestContext.Current.CancellationToken;

    [Fact]
    public async Task AWaitPollsUntilTheJobIsDoneAndReturnsItsLastStatus()
    {
        using var rig = Rig.Create(Replies(Running("WAITING"), Running("RUNNING"), Running("COMPLETE")));

        var result = await rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.Zero, TimeSpan.FromSeconds(5), Token);

        Assert.Equal("COMPLETE", State(result));
        Assert.Equal(Enumerable.Repeat($"{Base}/imports/7", 3), rig.Handler.Sent.Select(sent => sent.Url.ToString()));
    }

    [Fact]
    public async Task AFailedJobReturnsItsStatusRatherThanThrowing()
    {
        using var rig = Rig.Create(Replies(Running("RUNNING"), Running("FAILED")));

        var result = await rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.Zero, TimeSpan.FromSeconds(5), Token);

        Assert.Equal("FAILED", State(result));
        Assert.Equal(2, rig.Handler.Sent.Count);
    }

    [Fact]
    public async Task AJobThatOutlastsTheDeadlineIsATypedTimeoutWithItsLastStatus()
    {
        using var rig = Rig.Create(_ => Running("RUNNING"));

        var error = await Assert.ThrowsAsync<ApiJobTimeoutException>(
            () => rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.FromMilliseconds(20), TimeSpan.FromMilliseconds(50), Token));

        Assert.Equal("job_timeout", error.Kind);
        Assert.Equal("RUNNING", State(Assert.IsType<JsonElement>(error.Result)));
        Assert.True(rig.Handler.Sent.Count >= 2);
    }

    [Fact]
    public async Task CancellingAWaitInterruptsItsSleep()
    {
        using var cancel = CancellationTokenSource.CreateLinkedTokenSource(Token);
        using var rig = Rig.Create(_ =>
        {
            cancel.CancelAfter(TimeSpan.FromMilliseconds(20));
            return Running("RUNNING");
        });
        var clock = Stopwatch.StartNew();

        await Assert.ThrowsAnyAsync<OperationCanceledException>(
            () => rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.FromSeconds(60), TimeSpan.FromSeconds(600), cancel.Token));

        Assert.True(clock.Elapsed < TimeSpan.FromSeconds(30));
        Assert.Single(rig.Handler.Sent);
    }

    [Fact]
    public async Task ARateLimitWhilePollingIsRetriedAfterItsRetryAfter()
    {
        var limited = new HttpResponseMessage(HttpStatusCode.TooManyRequests) { Headers = { { "Retry-After", "0" } }, Content = new ByteArrayContent([]) };
        using var rig = Rig.Create(Replies(Running("RUNNING"), limited, Running("COMPLETE")));

        var result = await rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.Zero, TimeSpan.FromSeconds(5), Token);

        Assert.Equal("COMPLETE", State(result));
        Assert.Equal(3, rig.Handler.Sent.Count);
    }

    [Fact]
    public async Task AStateThatIsNotAStringIsADecodeError()
    {
        using var rig = Rig.Create(_ => Json("""{"import_id": 7, "progress": {"state": 3}}"""));

        var error = await Assert.ThrowsAsync<ApiDecodeException>(
            () => rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.Zero, TimeSpan.FromSeconds(5), Token));

        Assert.Contains("progress.state", error.Message);
    }

    [Fact]
    public async Task AWaitRefusesANegativeIntervalOrTimeoutAndAnOperationWithoutAJob()
    {
        using var rig = Rig.Create(_ => Running("COMPLETE"));

        var interval = await Assert.ThrowsAsync<ArgumentOutOfRangeException>(
            () => rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.FromSeconds(-1), TimeSpan.FromSeconds(5), Token));
        var timeout = await Assert.ThrowsAsync<ArgumentOutOfRangeException>(
            () => rig.Transport.WaitAsync<JsonElement>(Status, [7L, null], TimeSpan.Zero, TimeSpan.FromSeconds(-1), Token));
        var noJob = await Assert.ThrowsAsync<ArgumentException>(
            () => rig.Transport.WaitAsync<JsonElement>(Start, [], TimeSpan.Zero, TimeSpan.FromSeconds(5), Token));

        Assert.Equal("interval", interval.ParamName);
        Assert.Equal("timeout", timeout.ParamName);
        Assert.Contains("does not report a job", noJob.Message);
        Assert.Empty(rig.Handler.Sent);
    }

    [Theory]
    [InlineData("https://api.example.test/files/report.csv?sig=abc")]
    [InlineData("https://API.Example.test:443/files/report.csv")]
    public async Task ADownloadUrlOnTheBaseOriginSendsCredentials(string url)
    {
        using var rig = Rig.Create(_ => Report());

        await using var download = await rig.Transport.DownloadUrlAsync(url, cancellationToken: Token);

        Assert.Equal("text/csv", download.ContentType);
        Assert.Equal(Csv, Encoding.UTF8.GetString(await download.ReadAllBytesAsync(Token)));
        var sent = Assert.Single(rig.Handler.Sent);
        Assert.Equal(Secret, sent.Headers["Authorization"]);
        Assert.Equal("identity", sent.Headers["Accept-Encoding"]);
    }

    [Theory]
    [InlineData("https://files.example.test/report.csv")]
    [InlineData("http://api.example.test/report.csv")]
    [InlineData("https://api.example.test:8443/report.csv")]
    public async Task ADownloadUrlOnAnotherSchemeHostOrPortSendsNoCredentials(string url)
    {
        using var rig = Rig.Create(_ => Report());

        await using var download = await rig.Transport.DownloadUrlAsync(url, cancellationToken: Token);

        Assert.Equal(Csv, Encoding.UTF8.GetString(await download.ReadAllBytesAsync(Token)));
        Assert.False(Assert.Single(rig.Handler.Sent).Headers.ContainsKey("Authorization"));
        Assert.Empty(rig.Credentials.Seen);
    }

    [Fact]
    public async Task ARedirectToAnotherOriginDropsCredentialsForTheRestOfTheChain()
    {
        using var rig = Rig.Create(request => request.Url.Host switch
        {
            "api.example.test" when request.Url.AbsolutePath == "/files/1" => Redirect("https://files.example.test/signed/1"),
            "files.example.test" => Redirect($"{Base}/files/final"),
            _ => Report(),
        });

        await using var download = await rig.Transport.DownloadUrlAsync($"{Base}/files/1", cancellationToken: Token);

        Assert.Equal(Csv, Encoding.UTF8.GetString(await download.ReadAllBytesAsync(Token)));
        Assert.Equal(
            [$"{Base}/files/1", "https://files.example.test/signed/1", $"{Base}/files/final"],
            rig.Handler.Sent.Select(sent => sent.Url.ToString()));
        Assert.Equal([Secret, null, null], rig.Handler.Sent.Select(sent => sent.Headers.GetValueOrDefault("Authorization")));
    }

    [Fact]
    public async Task ARelativeRedirectOnTheBaseOriginKeepsCredentials()
    {
        using var rig = Rig.Create(request => request.Url.AbsolutePath == "/files/1" ? Redirect("/files/2") : Report());

        await using var download = await rig.Transport.DownloadUrlAsync($"{Base}/files/1", cancellationToken: Token);

        Assert.Equal([$"{Base}/files/1", $"{Base}/files/2"], rig.Handler.Sent.Select(sent => sent.Url.ToString()));
        Assert.Equal([Secret, Secret], rig.Handler.Sent.Select(sent => sent.Headers.GetValueOrDefault("Authorization")));
    }

    [Fact]
    public async Task ADownloadUrlRefusesARelativeUrlAndEndlessRedirects()
    {
        using var rig = Rig.Create(request => Redirect(request.Url.ToString()));

        await Assert.ThrowsAsync<ArgumentException>(() => rig.Transport.DownloadUrlAsync("/files/1", cancellationToken: Token));
        await Assert.ThrowsAsync<ArgumentException>(() => rig.Transport.DownloadUrlAsync("ftp://api.example.test/files/1", cancellationToken: Token));
        Assert.Empty(rig.Handler.Sent);

        var error = await Assert.ThrowsAsync<ApiDecodeException>(() => rig.Transport.DownloadUrlAsync($"{Base}/files/1", cancellationToken: Token));

        Assert.Contains("redirects", error.Message);
        Assert.Equal(6, rig.Handler.Sent.Count);
    }

    [Theory]
    [InlineData(null)]
    [InlineData("ftp://files.example.test/report.csv")]
    public async Task ARedirectWithoutAnHttpLocationIsADecodeError(string? location)
    {
        using var rig = Rig.Create(_ => location is null ? new HttpResponseMessage(HttpStatusCode.Found) : Redirect(location));

        var error = await Assert.ThrowsAsync<ApiDecodeException>(() => rig.Transport.DownloadUrlAsync($"{Base}/files/1", cancellationToken: Token));

        Assert.Equal(302, error.Status);
        Assert.Single(rig.Handler.Sent);
    }

    [Fact]
    public async Task AHandlerThatFollowsARedirectItselfIsRefused()
    {
        using var rig = Rig.Create(_ => Report(), followed: new Uri("https://files.example.test/signed/1"));

        await Assert.ThrowsAsync<InvalidOperationException>(() => rig.Transport.DownloadUrlAsync($"{Base}/files/1", cancellationToken: Token));
    }

    private static string? State(JsonElement status) => status.GetProperty("progress").GetProperty("state").GetString();

    private static HttpResponseMessage Json(string body) =>
        new(HttpStatusCode.OK) { Content = new StringContent(body, Encoding.UTF8, "application/json") };

    private static HttpResponseMessage Running(string state) => Json($$$"""{"import_id": 7, "progress": {"state": "{{{state}}}"}}""");

    private static HttpResponseMessage Report() =>
        new(HttpStatusCode.OK) { Content = new ByteArrayContent(Encoding.UTF8.GetBytes(Csv)) { Headers = { ContentType = MediaTypeHeaderValue.Parse("text/csv") } } };

    private static HttpResponseMessage Redirect(string location) =>
        new(HttpStatusCode.Found) { Headers = { { "Location", location } }, Content = new ByteArrayContent([]) };

    private static Func<Request, HttpResponseMessage> Replies(params HttpResponseMessage[] responses)
    {
        var remaining = new Queue<HttpResponseMessage>(responses);
        return _ => remaining.Dequeue();
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

        public static Rig Create(Func<Request, HttpResponseMessage> respond, Uri? followed = null)
        {
            var handler = new Handler(respond, followed);
            var credentials = new Recorder();
            var transport = new Transport(
                new Settings
                {
                    BaseUrl = Base,
                    Credentials = credentials,
                    Headers = new Dictionary<string, string> { ["User-Agent"] = "test" },
                    ToError = context => new ApiException($"status {context.Status}") { Status = context.Status, RawBody = context.Text },
                    Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
                    MaxRetries = 2,
                    RateLimitWait = TimeSpan.Zero,
                    RetryBaseDelay = TimeSpan.Zero,
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
            request.Headers["Authorization"] = Secret;
            return ValueTask.CompletedTask;
        }

        public IReadOnlyCollection<string> Secrets() => [Secret];
    }

    private sealed record Request(Uri Url, Dictionary<string, string> Headers);

    /// <summary>Records each request. With <c>followed</c>, it moves the request there, as a handler that follows a redirect does.</summary>
    private sealed class Handler(Func<Request, HttpResponseMessage> respond, Uri? followed) : HttpMessageHandler
    {
        public ConcurrentQueue<Request> Sent { get; } = new();

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var headers = request.Headers.NonValidated.ToDictionary(header => header.Key, header => header.Value.ToString(), StringComparer.OrdinalIgnoreCase);
            var sent = new Request(request.RequestUri!, headers);
            Sent.Enqueue(sent);
            if (followed is not null)
            {
                request.RequestUri = followed;
            }
            return Task.FromResult(respond(sent));
        }
    }
}
