# Conformance cases

The cases for this API, in the format described in `toolchain/conformance/README.md`. Fixture values are synthetic.

`reference-driver.mjs` is a minimal client in plain JavaScript, used to prove that every case can pass before any language package exists. It is test code, not an SDK. Each language gets its own driver beside its package.

```sh
API=gitea npm run spec:build
API=gitea npm run conformance  # runs the reference driver
```

## Base URL

Prism serves each path without the server's `/api/v1` prefix, so cases name paths as the spec declares them. A package takes the instance's URL and adds `/api/v1` itself, so its driver passes `base_url` as the instance URL and removes the prefix from each request on its way to the harness. A request without the prefix goes out unchanged and fails the case's path check, so the cases also pin it. Each package's unit tests pin the full path, sub-path installs included.

## Credentials

`defaults.yaml` holds a synthetic access token, password and one-time password.

| Setting | Meaning |
| --- | --- |
| `token` | An access token, sent as `Authorization: token <token>` |
| `username` | When set, the client uses Basic with `username` and `password` instead of the token |
| `password` | The Basic password, a secret |
| `otp` | A one-time password, sent as `X-GITEA-OTP` with Basic only. `otp: null` in a case sends none |
| `sudo` | A username to act as, sent as `Sudo` with either credential |

Every case checks that the token, password and one-time password reach no result, error or log. The cases that use Basic also check that its encoded header value is not logged, and a server error that echoes it has it removed.

## Error kinds

A driver reports these in `error.kind`, with the HTTP `status` where there was one. Gitea's errors are JSON with a `message`, which the error carries when the body has one, and every error carries `raw_body`, the body as text with every credential removed.

| Kind | Meaning |
| --- | --- |
| `bad_request` | 400 |
| `authentication` | 401 |
| `permission` | 403 |
| `not_found` | 404 |
| `conflict` | 409 |
| `validation` | 422 |
| `rate_limited` | 429, after retries |
| `server` | 5xx, after retries |
| `api` | Any other status, redirects included |
| `timeout` | No response within `timeout_ms`, after retries |
| `connection` | The connection failed or dropped before a full response, after retries |
| `decode` | A success response whose declared JSON body is empty or does not parse, a page that does not hold its items list, or a `next` link to a position already sent in the iteration |

## Retries, paging, paths and files

* A 429 is retried on every method after its `Retry-After` seconds. 5xx, timeouts and dropped connections are retried on GET only.
* Paged operations and the list each page holds are in `sdk.yaml` under `iterators`. The iterator copies `page` and `limit` out of the `rel="next"` link of each response's `Link` header into its own next request, and never fetches the link.
* Every path parameter is one segment, so a `/` in a file path is sent as `%2F`.
* Raw files and archives are binary downloads, diffs and patches are text, and attachments are a multipart `attachment` part.

## Limits

* Not every operation has a case yet. TODO: cover each operation once a language package names them.

These cases are checked against the mock only. A later stage runs live scenarios against a disposable Gitea container.
