# gitea-rest

Unofficial async Rust client for the Gitea API. Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.

Gitea is a self-hosted Git service. This client talks to any Gitea instance, your own or [gitea.com](https://gitea.com), at the URL you give it, so the base URL is always your instance's. Its methods and models are generated from the API spec of one pinned Gitea release, v28.3.0, so an older or newer instance may lack an operation or send other fields.

**Alpha.** It is tested against a mock built from the spec, and a suite against a disposable Gitea container is next. It has not yet been confirmed against real instances. If you use it, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your instance's URL, such as `https://gitea.example.com`, or `https://example.com/git` for an instance under a sub-path. There is no default. The client adds `/api/v1`, so leave it out.
* You need your own credentials: an access token, made under Settings → Applications on your instance, or a username and password. This crate ships with none.

## How this differs from other crates

Gitea's only official SDK is for Go, `code.gitea.io/sdk/gitea`. The `gitea` crate, 0.2.0, was last released in 2020, and the newer crates cover a small part of the API. This crate is generated from the spec of the pinned release, as are its siblings in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, errors and redaction behave the same in each. It adds:

* typed models and async methods for all 533 current operations;
* streams that walk every page by following the `Link` header;
* errors typed by status, carrying Gitea's error message;
* your token, password and one-time password kept out of every error and log line.

## Install

The crate is not on crates.io yet. From a clone of this repository, add it by path:

```toml
[dependencies]
gitea-rest = { path = "apis/gitea/packages/rust" }
```

Requires Rust 1.85 or later and a Tokio runtime. TLS is rustls by default. For your platform's TLS library instead, set `default-features = false, features = ["native-tls"]`.

With default features off and neither TLS feature, the crate builds but every `https` call fails with `ErrorKind::Connection`, after the usual retries for a GET. That is only right if you pass an `http_client` whose `reqwest` has TLS enabled through your own dependency.

## Quickstart

```rust,no_run
use futures_util::TryStreamExt;
use gitea_rest::{Client, ErrorKind, IssuesListParams};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .base_url("https://gitea.example.com")
    .token("your-access-token")
    .build()?;

let me = client.current_user().get().await?;
println!("{:?}", me.login);

let params = IssuesListParams {
    state: Some("open".to_owned()),
    limit: Some(50),
    ..Default::default()
};
let mut issues = client.issues().iter("your-org", "your-repo", &params);
while let Some(issue) = issues.try_next().await? {
    println!("{:?} {:?}", issue.number, issue.title);
}

match client.repos().get("your-org", "missing-repo").await {
    Ok(repo) => println!("{:?}", repo.full_name),
    Err(error) if error.kind() == ErrorKind::NotFound => println!("{:?}", error.detail()),
    Err(error) => return Err(error.into()),
}
# Ok(())
# }
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to your base URL.

## Authentication

Set one of these:

* **`token`**, an access token. It is sent as `Authorization: token <token>`.
* **`basic_auth`**, a username and password, sent with Basic authentication. If your account has two-factor authentication on, add the current one-time password with `otp`; it is sent as `X-GITEA-OTP`. A one-time password expires within a minute, so this suits a short task, such as creating an access token to use from then on.

With either, `sudo` acts as another user, sent as `Sudo`. That needs an admin's credentials.

```rust,no_run
use gitea_rest::Client;
use gitea_rest::models::CreateAccessTokenOption;

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .base_url("https://gitea.example.com")
    .basic_auth("your-username", "your-password")
    .otp("123456")
    .build()?;
let option = CreateAccessTokenOption {
    name: Some("scripts".to_owned()),
    scopes: Some(vec!["read:repository".to_owned()]),
    ..Default::default()
};
let token = client.users().create_token("your-username", &option).await?;
println!("{:?}", token.sha1);
# Ok(())
# }
```

## Configuration

`Client::builder()` takes these settings before `build()`:

| Setting | Default | Meaning |
| --- | --- | --- |
| `base_url` | None | Your instance's URL, without `/api/v1`. Required. Your credentials are sent to it |
| `token` | None | An access token. Set this or `basic_auth` |
| `basic_auth` | None | A username and password, instead of a token |
| `otp` | None | A one-time password, sent as `X-GITEA-OTP` with `basic_auth` only |
| `sudo` | None | A user to act as, sent as `Sudo` |
| `user_agent` | None | Sent as `User-Agent` when given |
| `timeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `max_retries` | 3 | Retries after the first attempt |
| `retry_base_delay` | 500 ms | Base of the exponential backoff |
| `rate_limit_wait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | 60 seconds | Longest `Retry-After` to wait for |
| `http_client` | None | Your own `reqwest::Client`, for a proxy, TLS roots or a shared pool |

A `Client` is cheap to clone and safe to share between tasks.

With `http_client`, the client still sends its own headers and applies its timeout and retries, but redirects follow your client's policy. Build it with `reqwest::redirect::Policy::none()` to keep your credentials on your base URL. A retry policy of your client's own, set with `reqwest::ClientBuilder::retry`, can resend any write. The crate re-exports the `reqwest` it uses as `gitea_rest::reqwest`.

## Behaviour

* **Methods** are grouped by area: `repos()`, `branches()`, `tags()`, `contents()`, `commits()`, `git()`, `pulls()`, `releases()`, `wiki()`, `issues()`, `labels()`, `milestones()`, `projects()`, `hooks()`, `actions()`, `orgs()`, `teams()`, `users()`, `current_user()`, `notifications()`, `packages()`, `admin()` and `misc()`, with models in `gitea_rest::models`. Each method's documentation ends with its Gitea operationId, such as `(issueListIssues)`, so you can find it in Gitea's API docs. Where an organization or your own account has the same kind of resource as a repository, the method ends in `_for_org` or `_for_user`, such as `hooks().list_for_org`. Names match the Python package's. The 4 deprecated operations are left out.
* **Pagination:** `list` and `search` methods return one page, and the matching `iter` methods return a `Stream` of every item, on 110 operations. Gitea names the next page only in each response's `Link` header. The stream copies its `page` and `limit` into its own next request, with your other parameters, and never fetches the link itself, whose host is your instance's configured root URL and may differ from your base URL. A link back to a page already sent fails with `ErrorKind::Decode`. Streams end after yielding an error.
* **Paths:** each path parameter is one URL segment, so a file path such as `docs/intro.md` is sent as `docs%2Fintro.md`.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `rate_limit_wait`. A `Retry-After` longer than `max_retry_wait` fails at once with `ErrorKind::RateLimited`, with the header in `Error::retry_after`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried after those, because a repeat could act twice.
* **Cancellation:** dropping a call's future stops it, including any wait before a retry. Wrap a call in `tokio::time::timeout` for an overall deadline; `timeout` applies to each attempt.
* **Redirects** are never followed by the default client. A 3xx fails with `ErrorKind::Api`, so your credentials stay on your base URL.
* **Errors** are one `Error` type. Match on `error.kind()`, an `ErrorKind` such as `NotFound`, `Conflict` or `Validation`, and read `status()`, `detail()`, the `message` of Gitea's JSON error body, `retry_after()` and `raw_body()`, the body as text. Every credential is removed from all of them.
* **Logging** goes through the `log` crate, at debug and info levels, and holds operation names, methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** model and parameter fields are `Option`s, so a `None` field is not sent. Build them with `..Default::default()`. A field the API types in several ways is a `serde_json::Value`.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against every release. Every field is an `Option` because a required field can be missing. A field that does not fit its declared type stays `None` and keeps its raw value in the model's `extra` map, and so do unknown fields and nulls. Serialising a model with `serde_json` gives all of it back with the API's field names. A body whose top level is not the declared type fails with `ErrorKind::Decode`, with the body in `raw_body()`.
* **Files:** raw files, media and archives return a `Download`, read with `chunk()` or `bytes()` within the client's timeout. Diffs, patches and signing keys return a `String`. Attachment uploads take a `File`, with an optional name.

## Limits

* `repos().list_topics` and `admin().list_unadopted_repos` return one page of strings, with no stream yet.
* `git().get_tree` and `wiki().list_page_revisions` page differently from the rest, and have no stream.
* OAuth2 bearer tokens are not built in, and there is no custom credential provider yet. TODO: add one if users ask.

## Testing

Every test runs against a mock built from the spec, with synthetic credentials. The tests never use a real account or call a real instance. A suite that runs against a disposable Gitea container in CI is next.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Gitea's spec, which is fetched at build time and not included, and grants no right to the Gitea name.
