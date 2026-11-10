# GiteaRest

Unofficial .NET client for the Gitea API. Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.

Gitea is a self-hosted Git service. This client talks to any Gitea instance, your own or [gitea.com](https://gitea.com), at the URL you give it, so the base URL is always your instance's. Its methods and models are generated from the API spec of one pinned Gitea release, v28.3.0, so an older or newer instance may lack an operation or send other fields.

**Alpha.** It is tested against a mock built from the spec, and against a disposable Gitea v28.3.0 container in CI. It has not yet been confirmed against real instances. If you use it, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your instance's URL, such as `https://gitea.example.com`, or `https://example.com/git` for an instance under a sub-path. There is no default. The client adds `/api/v1`, so leave it out.
* You need your own credentials: an access token, made under Settings → Applications on your instance, or a username and password. This package ships with none.

## How this differs from other packages

Gitea's only official SDK is for Go, `code.gitea.io/sdk/gitea`. On NuGet, `Gitea.Net.API` is a client generated from Gitea's spec, versioned with Gitea's releases. This package is generated from the spec of the pinned release too, but on a small hand-written runtime it shares with its siblings in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, against a mock and against a real Gitea container, so retries, paging, errors and redaction behave the same in each. It adds:

* retries with backoff, and `Retry-After` handling for 429s;
* `ListAll…Async` iterators that walk every page by following the `Link` header;
* exceptions typed by status, carrying Gitea's error message;
* your token, password and one-time password kept out of every exception and log line.

## Install

The package is not on NuGet yet. From a clone of this repository, reference the project:

```sh
dotnet add reference path/to/apis/gitea/packages/csharp/src/GiteaRest/GiteaRest.csproj
```

Requires .NET 8 or later.

## Quickstart

```csharp
using GiteaRest;

using var client = new GiteaClient("https://gitea.example.com", GiteaCredentials.Token("your-access-token"));

var me = await client.CurrentUser.GetAsync();
Console.WriteLine(me.Login);

await foreach (var issue in client.Issues.ListAllAsync("your-org", "your-repo", state: "open", limit: 50))
{
    Console.WriteLine($"{issue.Number} {issue.Title}");
}

try
{
    await client.Repos.GetAsync("your-org", "missing-repo");
}
catch (NotFoundException error)
{
    Console.WriteLine($"{error.Status} {error.Detail}");
}
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to your base URL.

## Authentication

Pass one of these:

* **`GiteaCredentials.Token(token)`**, an access token. It is sent as `Authorization: token <token>`.
* **`GiteaCredentials.Basic(username, password)`**, sent with Basic authentication. If your account has two-factor authentication on, add the current one-time password as `otp`; it is sent as `X-GITEA-OTP`. A one-time password expires within a minute, so this suits a short task, such as creating an access token to use from then on.

With either, `GiteaClientOptions.Sudo` acts as another user, sent as `Sudo`. That needs an admin's credentials.

```csharp
using GiteaRest;
using GiteaRest.Models;

using var client = new GiteaClient("https://gitea.example.com", GiteaCredentials.Basic("your-username", "your-password", otp: "123456"));
var token = await client.Users.CreateTokenAsync("your-username", new CreateAccessTokenOption { Name = "scripts", Scopes = ["read:repository"] });
Console.WriteLine(token.Sha1);
```

## Configuration

`new GiteaClient(baseUrl, credentials, options)` takes your instance's URL, your credentials and a `GiteaClientOptions`, whose every property is optional:

| Property | Default | Meaning |
| --- | --- | --- |
| `Sudo` | None | A user to act as, sent as `Sudo` |
| `UserAgent` | None | Sent as `User-Agent` when set |
| `Timeout` | 30 seconds | Time allowed for each attempt, including reading the whole response |
| `MaxRetries` | `3` | Retries after the first attempt |
| `RetryBaseDelay` | 0.5 seconds | Base of the exponential backoff |
| `RateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `MaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for. A longer one throws `RateLimitedException` at once |
| `Logger` | None | An `ILogger` for methods, URLs, statuses and retries |
| `HttpHandler` | None | An `HttpMessageHandler` to use instead of the network. The client does not dispose it |

To send through an `HttpClient` of your own, such as one from `IHttpClientFactory`, pass it as the fourth argument. The client uses it as it is: it neither changes nor disposes it, and its `Timeout` still applies. Its `DefaultRequestHeaders.ExpectContinue` must not be `true`, because that would let a failed write be resent. A plain `new HttpClient()` follows redirects, unlike the client's own handler; build it over `new SocketsHttpHandler { AllowAutoRedirect = false }` to keep your credentials on your instance. A handler that retries must skip writes.

A client is safe for concurrent use.

## Behaviour

* **Methods** are grouped by area: `client.Repos`, `client.Branches`, `client.Tags`, `client.Contents`, `client.Commits`, `client.Git`, `client.Pulls`, `client.Releases`, `client.Wiki`, `client.Issues`, `client.Labels`, `client.Milestones`, `client.Projects`, `client.Hooks`, `client.Actions`, `client.Orgs`, `client.Teams`, `client.Users`, `client.CurrentUser`, `client.Notifications`, `client.Packages`, `client.Admin` and `client.Misc`, with models in `GiteaRest.Models`. Each method's XML doc comment ends with its Gitea operationId, such as `(issueListIssues)`, so you can find it in Gitea's API docs. Where an organization or your own account has the same kind of resource as a repository, the method ends in `ForOrg` or `ForUser`, such as `Hooks.ListForOrgAsync`. Names are the Python package's, in .NET case. Every method is asynchronous and takes a `CancellationToken`. The 4 deprecated operations are left out.
* **Parameters** that are C# keywords are renamed: `ref` is `gitRef`, `base` is `baseBranch`, `event` is `eventName`, and repository search's `private` is `includePrivate`.
* **Pagination:** `List…Async` and `Search…Async` methods return one page, and the matching `ListAll…Async` and `SearchAll…Async` methods return an `IAsyncEnumerable` over every item, on 112 operations, including the two whose pages hold strings. Gitea names the next page only in each response's `Link` header. The iterator copies its `page` and `limit` into its own next request, with your other parameters, and never fetches the link itself, whose host is your instance's configured root URL and may differ from your base URL. A link back to a page already sent throws `ApiDecodeException`.
* **Paths:** each path parameter is one URL segment, so a file path such as `docs/intro.md` is sent as `docs%2Fintro.md`.
* **Cancellation:** cancelling a call stops it, including any wait before a retry, and throws `OperationCanceledException`.
* **Timeouts:** `Timeout` is the time allowed for each attempt. It throws `ApiTimeoutException`.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `RateLimitWait`. A `Retry-After` longer than `MaxRetryWait` throws `RateLimitedException` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried after those, because a repeat could act twice.
* **Redirects** are never followed by the client's own handler. A 3xx throws an `HttpException`, so your credentials stay on your base URL.
* **Errors** derive from `ApiException`. Error responses throw an `HttpException` subclass, such as `NotFoundException`, `ConflictException` or `UnprocessableException`, with `Kind`, `Status`, `Detail`, the `message` of Gitea's JSON error body, `RetryAfter` and `RawBody`, the body as text. Every credential is removed from all of them.
* **Logging** holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** JSON bodies are a generated model, and a null property is not sent.
* **Responses** are read tolerantly, because the spec has not been confirmed against every release. Every property is nullable. A value that does not fit its property, and any field this version does not know, is kept in the model's `Extra` instead of failing the call. An empty 204 returns `null`.
* **Free-form and union values** are `object`, holding a `JsonElement`.
* **Files:** raw files, media and archives return a `Download`; dispose it. Diffs, patches, rendered markup and signing keys return a `string`. Attachment uploads take `UploadFile(fileName, bytes)`.

## Limits

* `Git.GetTreeAsync` and `Wiki.ListPageRevisionsAsync` page differently from the rest, and have no iterator.
* OAuth2 bearer tokens are not built in, and there is no custom credential provider yet.
* Webhook signatures are not verified by this package yet.

## Testing

Every test runs against a mock built from the spec, with synthetic credentials, and a live suite runs against a disposable Gitea container in CI, with users and a token made for that run. The tests never use a real account or call a real instance. See [the live suite](https://github.com/fdhoff/api-sdks/blob/main/apis/gitea/docs/live.md).

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Gitea's spec, which is fetched at build time and not included, and grants no right to the Gitea name.
