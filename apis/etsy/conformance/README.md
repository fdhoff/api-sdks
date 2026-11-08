# Conformance cases

The cases for this API, in the format described in `toolchain/conformance/README.md`. Fixture values are synthetic.

`reference-driver.mjs` is a minimal client in plain JavaScript, used to prove that every case can pass before any language package exists. It is test code, not an SDK. Each language gets its own driver beside its package.

```sh
API=etsy npm run spec:build
API=etsy npm run conformance  # runs the reference driver
```

## Credentials

`defaults.yaml` names three synthetic secrets, and every case checks that none of them reaches the driver's result, error or logs:

| Setting | Sent as |
| --- | --- |
| `api_key` and `shared_secret` | `x-api-key: <api_key>:<shared_secret>` on every request |
| `token` | `Authorization: Bearer <token>`, only on operations whose security includes `oauth2` |

The token is sent verbatim. Etsy's access tokens already start with the user's numeric ID and a dot.

## Error kinds

A driver reports these in `error.kind`, with the HTTP `status` where there was one. Errors also carry `raw_body` with every secret removed, and `message` from the body's `error` string when there is one.

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
| `decode` | A success response whose declared JSON body is empty or does not parse, or a page with no `results` list |

## Retries and paging

Retries follow the toolchain runtime: a 429 is retried on every method, after `retry-after` seconds when it is usable, and 5xx, timeouts and dropped connections on GET only. Paged operations take `limit` and `offset` and answer `{count, results}`. The iterator advances `offset` by the number of results received, and stops at an empty page or once `offset` reaches `count`.

## Limits

* Not every operation has a case yet. TODO: cover each operation once a language package names them.
* There are no cases for refreshing an expired access token. TODO: add refresh-once cases with the credential provider.
* Wire checks can compare JSON and multipart bodies, not form bodies, and Prism cannot validate array fields in form bodies (see `apis/etsy/docs/spec-audit.md`). TODO: add a wire check for form bodies.

These cases are checked against the mock only. Nothing here has been confirmed against the live API.
