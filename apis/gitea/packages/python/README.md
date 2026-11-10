# gitea-rest

Unofficial Python client for the Gitea API. Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.

Gitea is a self-hosted Git service. This client talks to any Gitea instance, your own or [gitea.com](https://gitea.com), at the URL you give it. Its methods and models are generated from the API spec of one pinned Gitea release, v28.3.0, so an older or newer instance may lack an operation or send other fields.

**Alpha.** It is tested against a mock built from the spec, and against a disposable Gitea v28.3.0 container in CI. It has not yet been confirmed against real instances. If you use it, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your instance's URL, such as `https://gitea.example.com`, or `https://example.com/git` for an instance under a sub-path. There is no default. The client adds `/api/v1`.
* You need your own credentials: an access token, made under Settings → Applications on your instance, or a username and password. This package ships with none.

## How this differs from other SDKs

Gitea's only official SDK is for Go, `code.gitea.io/sdk/gitea`. The Python package `giteapy` was last released in 2020. This package is generated from the spec of the pinned release, with siblings to follow in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, errors and redaction behave the same in each. It adds:

* sync and async clients with typed models, for all 533 current operations;
* iterators that walk every page by following the `Link` header;
* errors typed by status, carrying Gitea's error message;
* your token, password and one-time password kept out of every error and log line.

## Install

The package is not on PyPI yet. From a clone of this repository:

```sh
pip install ./apis/gitea/packages/python
```

Requires Python 3.10 or later.

## Quickstart

```python
from gitea_rest import GiteaClient, NotFoundError

with GiteaClient("your-access-token", base_url="https://gitea.example.com") as client:
    print(client.current_user.get().login)

    for issue in client.issues.iter("your-org", "your-repo", state="open", limit=50):
        print(issue.number, issue.title)

    try:
        client.repos.get("your-org", "missing-repo")
    except NotFoundError as error:
        print(error.status, error.message)
```

The async client has the same methods:

```python
from gitea_rest import AsyncGiteaClient

async with AsyncGiteaClient("your-access-token", base_url="https://gitea.example.com") as client:
    async for repo in client.current_user.iter_repos(limit=50):
        print(repo.full_name)
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to your `base_url`.

## Authentication

Pass one of these:

* **An access token**, as the first argument. It is sent as `Authorization: token <token>`.
* **A username and password**, sent with Basic authentication. If your account has two-factor authentication on, add the current one-time password as `otp`; it is sent as `X-GITEA-OTP`. A one-time password expires within a minute, so this suits a short task, such as creating an access token to use from then on.
* **A `credentials` provider**, a `Credentials` subclass that sets each request's headers, for anything else, such as an OAuth2 bearer token.

With a token or a username and password, `sudo` acts as another user, sent as `Sudo`. That needs an admin's credentials.

```python
from gitea_rest import GiteaClient

with GiteaClient(
    base_url="https://gitea.example.com", username="your-username", password="your-password", otp="123456"
) as client:
    token = client.users.create_token("your-username", {"name": "scripts", "scopes": ["read:repository"]})
    print(token.sha1)
```

## Configuration

`GiteaClient` and `AsyncGiteaClient` take the access token, then these keywords:

| Argument | Default | Meaning |
| --- | --- | --- |
| `base_url` | Required | Your instance's URL, without `/api/v1`. Your credentials are sent to it |
| `username`, `password` | None | Basic authentication, instead of a token |
| `otp` | None | A one-time password, sent as `X-GITEA-OTP` with Basic only |
| `sudo` | None | A user to act as, sent as `Sudo` |
| `credentials` | None | A `Credentials` provider that sets each request's credentials, instead of the others |
| `user_agent` | None | Sent as `User-Agent` when given |
| `timeout` | `30.0` | Seconds to wait on each attempt |
| `max_retries` | `3` | Retries after the first attempt |
| `retry_base_delay` | `0.5` | Base in seconds of the exponential backoff |
| `rate_limit_wait` | `10.0` | Seconds to wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | `60.0` | Longest `Retry-After` to wait for, in seconds. A longer one raises `RateLimitedError` at once |
| `http_transport` | None | An httpx transport to use instead of the network |

## Behaviour

* **Methods** are grouped by area: `repos`, `branches`, `tags`, `contents`, `commits`, `git`, `pulls`, `releases`, `wiki`, `issues`, `labels`, `milestones`, `projects`, `hooks`, `actions`, `orgs`, `teams`, `users`, `current_user`, `notifications`, `packages`, `admin` and `misc`, with models in `gitea_rest.models`. Every method's docstring ends with its Gitea operationId, such as `(issueListIssues)`, so you can find it in Gitea's API docs. Where an organization or your own account has the same kind of resource as a repository, the method ends in `_for_org` or `_for_user`, such as `hooks.list_for_org` and `actions.list_runners_for_user`. The 4 deprecated operations are left out.
* **Pagination:** `list` and `search` methods return one page, and the matching `iter` methods walk all of them. Gitea names the next page only in each response's `Link` header. The iterator copies its `page` and `limit` into its own next request, with your other arguments, and never fetches the link itself, whose host is your instance's configured root URL and may differ from your `base_url`. A link back to a page already sent raises `DecodeError`.
* **Paths:** each path argument is one URL segment, so a file path such as `docs/intro.md` is sent as `docs%2Fintro.md`.
* **Timeouts:** `timeout` is the time allowed for each attempt, including reading the whole response. The async client enforces it exactly. The sync client checks it as data arrives, so a stalled read can overrun by up to one timeout.
* **Retries:** 429 on every method, honouring `Retry-After` up to `max_retry_wait` seconds, otherwise after `rate_limit_wait` seconds. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried after those, because a repeat could act twice.
* **Errors** derive from `ApiError`. Error responses raise an `HttpError` subclass, such as `NotFoundError`, `ConflictError` or `UnprocessableError`, with `status`, `message`, Gitea's error message when the body has one, `retry_after` and `raw_body`, the body as text. Every credential is removed from all of them.
* **Logging** goes to the `gitea_rest` logger. It holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests** can be a generated model or a plain mapping. Models validate strictly, and send only the fields you set. Method arguments are checked against their declared types and raise pydantic's `ValidationError` before anything is sent.
* **Responses** are parsed tolerantly, because the spec has not been confirmed against every release. A field that does not fit its declared type keeps its raw value instead of failing the call, a missing required field reads as `None`, and unknown fields are kept. An empty 204 returns `None`. A body that does not fit its declared type at all raises `DecodeError` with the body in `raw_body`.
* **Files:** raw files, media and archives return a `Download`; read it in a `with` block. Diffs, patches and signing keys return text. Attachment uploads take `bytes` or `(filename, bytes)`.

## Limits

* `repos.list_topics` and `admin.list_unadopted_repos` return one page of strings, with no iterator yet.
* `git.get_tree` and `wiki.list_page_revisions` page differently from the rest, and have no iterator.
* OAuth2 bearer tokens have no argument of their own. TODO: add one if users ask; a `credentials` provider can send one meanwhile.

## Testing

Every test runs against a mock built from the spec, with synthetic credentials, and a live suite runs against a disposable Gitea container in CI, with users and a token made for that run. The tests never use a real account or call a real instance. See [the live suite](https://github.com/fdhoff/api-sdks/blob/main/apis/gitea/docs/live.md).

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Gitea's spec, which is fetched at build time and not included, and grants no right to the Gitea name.
