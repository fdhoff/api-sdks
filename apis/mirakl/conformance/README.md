# Conformance cases

The cases for this API, in the format described in `toolchain/conformance/README.md`. Fixture values are synthetic.

`reference-driver.mjs` is a minimal client in plain JavaScript, used to prove that every case can pass before any language package exists. It is test code, not an SDK. Each language gets its own driver beside its package.

```sh
API=mirakl npm run spec:build
API=mirakl npm run conformance  # runs the reference driver
```

## Credentials

`token` in `defaults.yaml` is the shop API key, sent as the whole `Authorization` header with no scheme. Every case checks that the key reaches no result, error or log. `query_defaults: { shop_id }` in a case's `client` is the client-level shop; a call's own `shop_id` wins.

## Error kinds

A driver reports these in `error.kind`, with the HTTP `status` where there was one. The docs define no error body, so errors carry `raw_body`, the body as text with the key removed.

| Kind | Meaning |
| --- | --- |
| `bad_request` | 400 |
| `authentication` | 401 |
| `permission` | 403 |
| `not_found` | 404 |
| `rate_limited` | 429, after retries |
| `server` | 5xx, after retries |
| `api` | Any other status, redirects included |
| `timeout` | No response within `timeout_ms`, after retries |
| `connection` | The connection failed or dropped before a full response, after retries |
| `decode` | A success response whose declared JSON body is empty or does not parse, a page with no items list, or a next token that repeats one already sent in the iteration |
| `job_timeout` | A wait reached `poll_timeout_ms` before the job's state was final |

## Retries, paging, jobs and downloads

* A 429 is retried on every method after its `Retry-After` seconds. 5xx, timeouts and dropped connections are retried on GET only.
* Paged operations, the list each page holds and their style are in `sdk.yaml` under `iterators`.
* A wait polls the status operation `sdk.yaml` names under `jobs` and returns the final status, done or failed.
* A URL download sends the key only to the base URL's scheme, host and port, and never again once a redirect leaves it. Logs leave out the URL's query.

## Limits

* Not every operation has a case yet. TODO: cover each operation once a language package names them.

These cases are checked against the mock only. Nothing here has been confirmed against the live API.
