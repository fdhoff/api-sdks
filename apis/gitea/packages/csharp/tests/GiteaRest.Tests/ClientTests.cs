using System.Collections.Concurrent;
using System.Net;
using System.Text;
using GiteaRest.Runtime;
using Microsoft.Extensions.Logging;
using Xunit;

namespace GiteaRest.Tests;

public sealed class ClientTests
{
    private const string Base = "https://gitea.example.test";
    private const string Token = "unit-synthetic-access-token";
    private const string Password = "unit-synthetic-password";
    private const string Otp = "481516";
    private const string User = """{"id": 1, "login": "synthetic-user"}""";

    // Base64 of synthetic-user:unit-synthetic-password.
    private const string Encoded = "c3ludGhldGljLXVzZXI6dW5pdC1zeW50aGV0aWMtcGFzc3dvcmQ=";

    private static CancellationToken Cancel => TestContext.Current.CancellationToken;

    private static GiteaClient Client(Router handler, GiteaCredentials? credentials = null, string? sudo = null, ILogger? logger = null, string baseUrl = Base) =>
        new(baseUrl, credentials ?? GiteaCredentials.Token(Token), new GiteaClientOptions
        {
            Sudo = sudo,
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
            var resource = typeof(GiteaClient).GetProperty(operation.Resource);
            Assert.NotNull(resource);
            Assert.NotNull(resource.PropertyType.GetMethod(operation.Name));
            if (operation.Iterator is not null)
            {
                Assert.NotNull(resource.PropertyType.GetMethod(operation.Iterator));
            }
        }
        Assert.Equal(533, ClientResources.Operations.Length);
        Assert.Equal(112, ClientResources.Operations.Count(operation => operation.Iterator is not null));
    }

    [Fact]
    public async Task SendsTheTokenWithTheTokenSchemeUnderApiV1()
    {
        var handler = new Router(_ => Json(User));
        using var client = Client(handler, baseUrl: $"{Base}/");

        var user = await client.CurrentUser.GetAsync(Cancel);

        var sent = Assert.Single(handler.Sent);
        Assert.Equal($"{Base}/api/v1/user", sent.Url);
        Assert.Equal($"token {Token}", sent.Headers["Authorization"]);
        Assert.Equal("application/json", sent.Headers["Accept"]);
        Assert.Equal("synthetic-agent/1", sent.Headers["User-Agent"]);
        Assert.False(sent.Headers.ContainsKey("X-GITEA-OTP"));
        Assert.False(sent.Headers.ContainsKey("Sudo"));
        Assert.Equal("synthetic-user", user.Login);
    }

    [Fact]
    public async Task AnInstanceUnderASubPathKeepsItsPath()
    {
        var handler = new Router(_ => Json("""{"version": "28.3.0"}"""));
        using var client = Client(handler, baseUrl: "https://example.test/git");

        await client.Misc.GetVersionAsync(Cancel);

        Assert.Equal("https://example.test/git/api/v1/version", Assert.Single(handler.Sent).Url);
    }

    [Fact]
    public async Task BasicSendsTheOneTimePasswordAndSudoWhenGiven()
    {
        var handler = new Router(_ => Json(User));
        using var plain = Client(handler, GiteaCredentials.Basic("synthetic-user", Password));
        using var withOtp = Client(handler, GiteaCredentials.Basic("synthetic-user", Password, Otp), sudo: "synthetic-other-user");

        await plain.CurrentUser.GetAsync(Cancel);
        await withOtp.CurrentUser.GetAsync(Cancel);

        var sent = handler.Sent.ToArray();
        Assert.Equal($"Basic {Encoded}", sent[0].Headers["Authorization"]);
        Assert.False(sent[0].Headers.ContainsKey("X-GITEA-OTP"));
        Assert.Equal($"Basic {Encoded}", sent[1].Headers["Authorization"]);
        Assert.Equal(Otp, sent[1].Headers["X-GITEA-OTP"]);
        Assert.Equal("synthetic-other-user", sent[1].Headers["Sudo"]);
    }

    [Fact]
    public void RefusesABaseUrlThatIsMissingNotHttpOrAlreadyTheApis()
    {
        var token = GiteaCredentials.Token(Token);
        Assert.Throws<ArgumentException>(() => new GiteaClient(string.Empty, token));
        Assert.Throws<ArgumentException>(() => new GiteaClient("gitea.example.test", token));
        Assert.Throws<ArgumentException>(() => new GiteaClient("ftp://gitea.example.test", token));
        Assert.Throws<ArgumentException>(() => new GiteaClient($"{Base}/api/v1", token));
        Assert.Throws<ArgumentException>(() => new GiteaClient($"{Base}/api/v1/", token));
        Assert.Throws<ArgumentNullException>(() => new GiteaClient(Base, null!));
    }

    [Fact]
    public void RefusesEmptyCredentialsAndASudoThatIsNotAUsername()
    {
        Assert.Throws<ArgumentException>(() => GiteaCredentials.Token(string.Empty));
        Assert.Throws<ArgumentException>(() => GiteaCredentials.Basic(string.Empty, Password));
        Assert.Throws<ArgumentException>(() => GiteaCredentials.Basic("synthetic-user", string.Empty));
        Assert.Throws<ArgumentException>(() => GiteaCredentials.Basic("synthetic-user", Password, string.Empty));
        Assert.Throws<ArgumentException>(() => new GiteaClient(Base, GiteaCredentials.Token(Token), new GiteaClientOptions { Sudo = string.Empty }));
        Assert.Throws<ArgumentException>(() => new GiteaClient(Base, GiteaCredentials.Token(Token), new GiteaClientOptions { Sudo = "synthetic\r\nX-Other: 1" }));
    }

    [Fact]
    public void CredentialsNeverShowThemselves()
    {
        var shown = $"{GiteaCredentials.Token(Token)} {GiteaCredentials.Basic("synthetic-user", Password, Otp)}";

        Assert.DoesNotContain(Token, shown, StringComparison.Ordinal);
        Assert.DoesNotContain(Password, shown, StringComparison.Ordinal);
        Assert.DoesNotContain(Otp, shown, StringComparison.Ordinal);
    }

    [Fact]
    public async Task AFilePathIsOneSegment()
    {
        var handler = new Router(_ => Json("""{"name": "notes.md", "path": "docs/notes.md"}"""));
        using var client = Client(handler);

        var file = await client.Contents.GetAsync("synthetic-owner", "synthetic-repo", "docs/notes.md", gitRef: "main", cancellationToken: Cancel);

        Assert.Equal($"{Base}/api/v1/repos/synthetic-owner/synthetic-repo/contents/docs%2Fnotes.md?ref=main", Assert.Single(handler.Sent).Url);
        Assert.Equal("docs/notes.md", file.Path);
    }

    [Fact]
    public async Task LinkPagingCopiesThePositionAndNeverFetchesTheLinksHost()
    {
        var handler = new Router(sent => sent.Url.Contains("page=3", StringComparison.Ordinal)
            ? Json("""[{"number": 5}]""")
            : sent.Url.Contains("page=2", StringComparison.Ordinal)
                ? Json("""[{"number": 3}, {"number": 4}]""", link: """<https://root.example.invalid/api/v1/repos/o/r/issues?limit=2&page=3&state=open>; rel="next", <https://root.example.invalid/api/v1/repos/o/r/issues?limit=2&page=1>; rel="first" """)
                : Json("""[{"number": 1}, {"number": 2}]""", link: """<https://root.example.invalid/api/v1/repos/o/r/issues?limit=2&page=2&state=open>; rel="next last" """));
        using var client = Client(handler);

        var issues = await client.Issues.ListAllAsync("o", "r", state: "open", limit: 2, cancellationToken: Cancel).ToListAsync(Cancel);

        Assert.Equal([1, 2, 3, 4, 5], issues.Select(issue => issue.Number));
        Assert.Equal(
            [$"{Base}/api/v1/repos/o/r/issues?state=open&limit=2", $"{Base}/api/v1/repos/o/r/issues?state=open&page=2&limit=2", $"{Base}/api/v1/repos/o/r/issues?state=open&page=3&limit=2"],
            handler.Sent.Select(sent => sent.Url));
    }

    [Fact]
    public async Task PagesOfStringsAreIterated()
    {
        var handler = new Router(sent => sent.Path.EndsWith("/topics", StringComparison.Ordinal)
            ? Json(sent.Url.Contains("page=2", StringComparison.Ordinal) ? """{"topics": ["rust"]}""" : """{"topics": ["go", "dotnet"]}""", link: sent.Url.Contains("page=2", StringComparison.Ordinal) ? null : "<https://root.example.invalid/api/v1/repos/o/r/topics?page=2>; rel=\"next\"")
            : Json("""["synthetic-owner/orphan-1", "synthetic-owner/orphan-2"]"""));
        using var client = Client(handler);

        var topics = await client.Repos.ListAllTopicsAsync("o", "r", cancellationToken: Cancel).ToListAsync(Cancel);
        var orphans = await client.Admin.ListAllUnadoptedReposAsync(cancellationToken: Cancel).ToListAsync(Cancel);

        Assert.Equal(["go", "dotnet", "rust"], topics);
        Assert.Equal(["synthetic-owner/orphan-1", "synthetic-owner/orphan-2"], orphans);
    }

    [Fact]
    public async Task ALinkBackToAPageAlreadySentFailsToDecode()
    {
        var handler = new Router(_ => Json("""[{"number": 1}]""", link: "<https://gitea.example.test/api/v1/repos/o/r/issues?page=1&limit=1>; rel=\"next\""));
        using var client = Client(handler);

        var error = await Assert.ThrowsAsync<ApiDecodeException>(async () => await client.Issues.ListAllAsync("o", "r", page: 1, limit: 1, cancellationToken: Cancel).ToListAsync(Cancel));

        Assert.Equal("decode", error.Kind);
        Assert.Single(handler.Sent);
    }

    [Fact]
    public async Task ErrorsAreTypedByStatusAndCarryGiteasMessage()
    {
        var handler = new Router(sent => sent.Path switch
        {
            "/api/v1/repos/o/missing" => Json("""{"message": "synthetic repository not found", "url": "https://gitea.example.test/api/swagger"}""", HttpStatusCode.NotFound),
            "/api/v1/repos/o/r/branches" => Json("""{"message": "synthetic branch exists"}""", HttpStatusCode.Conflict),
            "/api/v1/repos/o/r/issues" => Json("""{"message": "[Title]: Required"}""", HttpStatusCode.UnprocessableEntity),
            _ => Json("forbidden", HttpStatusCode.Forbidden),
        });
        using var client = Client(handler);

        var missing = await Assert.ThrowsAsync<NotFoundException>(() => client.Repos.GetAsync("o", "missing", Cancel));
        var conflict = await Assert.ThrowsAsync<ConflictException>(() => client.Branches.CreateAsync("o", "r", new() { NewBranchName = "b" }, Cancel));
        var invalid = await Assert.ThrowsAsync<UnprocessableException>(() => client.Issues.CreateAsync("o", "r", new() { Title = string.Empty }, Cancel));
        var forbidden = await Assert.ThrowsAsync<PermissionDeniedException>(() => client.CurrentUser.GetAsync(Cancel));

        Assert.Equal(("not_found", 404, "synthetic repository not found"), (missing.Kind, missing.Status, missing.Detail));
        Assert.Equal("HTTP 404: synthetic repository not found", missing.Message);
        Assert.StartsWith("""{"message": "synthetic repository not found""", missing.RawBody, StringComparison.Ordinal);
        Assert.Equal(("conflict", 409, "synthetic branch exists"), (conflict.Kind, conflict.Status, conflict.Detail));
        Assert.Equal(("validation", 422, "[Title]: Required"), (invalid.Kind, invalid.Status, invalid.Detail));
        Assert.Equal(("permission", 403, null, "forbidden"), (forbidden.Kind, forbidden.Status, forbidden.Detail, forbidden.RawBody));
    }

    [Fact]
    public async Task CredentialsAreRemovedFromErrorsAndLogs()
    {
        var handler = new Router(_ => Json($$"""{"message": "bad {{Password}} {{Encoded}} {{Otp}}"}""", HttpStatusCode.Unauthorized));
        var logs = new Lines();
        using var client = Client(handler, GiteaCredentials.Basic("synthetic-user", Password, Otp), logger: logs);

        var error = await Assert.ThrowsAsync<AuthenticationException>(() => client.CurrentUser.GetAsync(Cancel));

        Assert.Equal("authentication", error.Kind);
        foreach (var secret in new[] { Password, Encoded, Otp })
        {
            Assert.DoesNotContain(secret, error.RawBody!, StringComparison.Ordinal);
            Assert.DoesNotContain(secret, error.Detail!, StringComparison.Ordinal);
            Assert.DoesNotContain(secret, error.Message, StringComparison.Ordinal);
            Assert.DoesNotContain(logs.All, entry => entry.Contains(secret, StringComparison.Ordinal));
        }
        Assert.NotEmpty(logs.All);
    }

    [Fact]
    public async Task UsesAnInjectedHttpClientWithoutDisposingIt()
    {
        var handler = new Router(_ => Json(User));
        using var http = new HttpClient(handler);

        using (var client = new GiteaClient(Base, GiteaCredentials.Token(Token), new GiteaClientOptions(), http))
        {
            await client.CurrentUser.GetAsync(Cancel);
        }
        using var again = await http.GetAsync($"{Base}/api/v1/user", Cancel);

        Assert.Equal(2, handler.Sent.Count);
        Assert.Equal($"token {Token}", handler.Sent.First().Headers["Authorization"]);
        Assert.Throws<ArgumentException>(() => new GiteaClient(Base, GiteaCredentials.Token(Token), new GiteaClientOptions { HttpHandler = handler }, http));
    }

    private static HttpResponseMessage Json(string body, HttpStatusCode status = HttpStatusCode.OK, string? link = null)
    {
        var response = new HttpResponseMessage(status) { Content = new StringContent(body, Encoding.UTF8, "application/json") };
        if (link is not null)
        {
            response.Headers.TryAddWithoutValidation("Link", link.Trim());
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
