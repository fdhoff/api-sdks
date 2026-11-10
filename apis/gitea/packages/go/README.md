# gitearest

Unofficial Go client for the Gitea API. Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.

Gitea is a self-hosted Git service. This client talks to any Gitea instance, your own or [gitea.com](https://gitea.com), at the URL you give it. Its methods and models are generated from the API spec of one pinned Gitea release, v28.3.0, so an older or newer instance may lack an operation or send other fields.

**Alpha.** It is tested against a mock built from the spec, and a disposable Gitea container is next. It has not yet been confirmed against real instances. If you use it, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your instance's URL, such as `https://gitea.example.com`, or `https://example.com/git` for an instance under a sub-path. There is no default. The base URL is the instance's own, not its API's: the client adds `/api/v1`.
* You need your own credentials: an access token, made under Settings → Applications on your instance, or a username and password. This module ships with none.

## How this differs from Gitea's own SDK

Gitea's official SDK is for Go: [`code.gitea.io/sdk/gitea`](https://pkg.go.dev/code.gitea.io/sdk/gitea), written by hand by the Gitea project. Use it if you want the project's own client. This module is different in how it is made and tested, not in what it is for:

* it is generated from the spec of the pinned release, for all 533 current operations, so it follows each release by regenerating;
* it shares one conformance suite with its siblings in other languages in [the same repository](https://github.com/fdhoff/api-sdks), so retries, paging, errors and redaction behave the same in each;
* iterators walk every page by following the `Link` header;
* errors are typed by status and carry Gitea's error message;
* your token, password and one-time password are kept out of every error and log line.

## Install

No version is tagged yet, so take a commit from `main`:

```sh
go get github.com/fdhoff/api-sdks/apis/gitea/packages/go@main
```

Requires Go 1.24 or later.

## Quickstart

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"

	"github.com/fdhoff/api-sdks/apis/gitea/packages/go/gitearest"
)

func main() {
	client, err := gitearest.NewClient("https://gitea.example.com", gitearest.Token(os.Getenv("GITEA_TOKEN")))
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	user, err := client.CurrentUser.Get(ctx)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*user.Login)

	params := &gitearest.IssuesListParams{State: gitearest.Ptr("open"), Limit: gitearest.Ptr[int64](50)}
	for issue, err := range client.Issues.Iter(ctx, "your-org", "your-repo", params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*issue.Number, *issue.Title)
	}

	_, err = client.Repos.Get(ctx, "your-org", "missing-repo")
	var failure *gitearest.APIError
	if errors.Is(err, gitearest.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.Detail)
	}
}
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to your base URL.

## Authentication

Pass one of these to `NewClient`:

* **`Token(token)`**, an access token, sent as `Authorization: token <token>`.
* **`Basic(username, password)`**, sent with Basic authentication.
* **`BasicWithOTP(username, password, otp)`**, Basic with the current one-time password of an account that has two-factor authentication on, sent as `X-GITEA-OTP`. A one-time password expires within a minute, so this suits a short task, such as creating an access token to use from then on.
* **Your own `Credentials`**, for anything else, such as an OAuth2 bearer token. Its `Apply` sets the headers of each attempt, retries included, and `Secrets` lists every value to keep out of logs and errors.

`WithSudo(username)` acts as another user, sent as `Sudo`. That needs an admin's credentials.

```go
client, err := gitearest.NewClient(
	"https://gitea.example.com",
	gitearest.BasicWithOTP("your-username", os.Getenv("GITEA_PASSWORD"), "123456"),
)
if err != nil {
	log.Fatal(err)
}
token, err := client.Users.CreateToken(context.Background(), "your-username", &gitearest.CreateAccessTokenOption{
	Name:   gitearest.Ptr("scripts"),
	Scopes: []string{"read:repository"},
})
if err != nil {
	log.Fatal(err)
}
fmt.Println(*token.SHA1)
```

## Configuration

`NewClient(baseURL, credentials, options...)` takes these options:

| Option | Default | Meaning |
| --- | --- | --- |
| `WithSudo` | None | A user to act as, sent as `Sudo` |
| `WithUserAgent` | None | Sent as `User-Agent` |
| `WithTimeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `WithMaxRetries` | 3 | Retries after the first attempt |
| `WithRetryBaseDelay` | 500 ms | Base of the exponential backoff |
| `WithRateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `WithMaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for |
| `WithHTTPTransport` | `http.DefaultTransport` | An `http.RoundTripper` to use instead of the network |
| `WithLogger` | None | A `*slog.Logger` |

A `Client` is safe for concurrent use.

## Behaviour

* **Methods** are grouped by area: `client.Repos`, `Branches`, `Tags`, `Contents`, `Commits`, `Git`, `Pulls`, `Releases`, `Wiki`, `Issues`, `Labels`, `Milestones`, `Projects`, `Hooks`, `Actions`, `Orgs`, `Teams`, `Users`, `CurrentUser`, `Notifications`, `Packages`, `Admin` and `Misc`. Every method's doc comment ends with its Gitea operationId, such as `(issueListIssues)`, so you can find it in Gitea's API docs. Where an organization or your own account has the same kind of resource as a repository, the method ends in `ForOrg` or `ForUser`, such as `Hooks.ListForOrg` and `Actions.ListRunnersForUser`. The 4 deprecated operations are left out.
* **Context:** every method takes a `context.Context`. Cancelling it stops the call, including any wait before a retry, and the call returns the context's error, not an `APIError`. Use it for an overall deadline; `WithTimeout` applies to each attempt.
* **Pagination:** `List` and `Search` methods return one page, and the matching `Iter` methods return an iterator for `range` over every item. Gitea names the next page only in each response's `Link` header. The iterator copies its `page` and `limit` into its own next request, with your other parameters, and never fetches the link itself, whose host is your instance's configured root URL and may differ from your base URL. A link back to a page already sent returns `ErrDecode`. Iterators stop after yielding an error.
* **Paths:** each path argument is one URL segment, so a file path such as `docs/intro.md` is sent as `docs%2Fintro.md`.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `WithRateLimitWait`. A `Retry-After` longer than `WithMaxRetryWait` returns `ErrRateLimited` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried after those, because a repeat could act twice.
* **Redirects** are never followed. A 3xx returns `ErrAPI`, so your credentials stay on your base URL.
* **Errors** are `*APIError`, with `Kind`, `Status`, `Detail`, Gitea's error message when the body has one, `RetryAfter` and `RawBody`, the body as text. Every credential is removed from all of them. Test the kind with `errors.Is` and a sentinel such as `ErrNotFound`, `ErrConflict` or `ErrValidation`. Gitea also answers 404 for a private repository your credentials cannot see.
* **Logging** goes to your `slog.Logger`, and holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** model and parameter fields are pointers, so a nil field is not sent. Use `Ptr` to set one, including to zero. Types are checked at compile time and nothing more.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against every release. Every field is a pointer because a required field can be missing, so check for nil. A field that does not fit its declared type stays nil and keeps its raw value in the model's `Extra` map, and so do unknown fields and nulls. An empty 204 returns nil. A body whose top level is not the declared type returns `ErrDecode`, with the body in `RawBody`.
* **Files:** raw files, media and archives return a `*Download`; close its `Body`. Diffs, patches and signing keys return a `string`. Attachment uploads take a `File`, with an optional name.

## Limits

* `Git.GetTree` and `Wiki.ListPageRevisions` page differently from the rest, and have no iterator.
* Gitea's error body is the model `ErrorBody`, because `APIError` is this module's error type.
* OAuth2 bearer tokens have no constructor of their own. TODO: add one if users ask; your own `Credentials` can send one meanwhile.

## Testing

Every test runs against a mock built from the spec, with synthetic credentials. The tests never use a real account or call a real instance. A suite that runs against a disposable Gitea container in CI is next.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Gitea's spec, which is fetched at build time and not included, and grants no right to the Gitea name.
