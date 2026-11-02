# Conformance cases

The cases for this API, in the format described in `toolchain/conformance/README.md`. Fixture values are synthetic.

`reference-driver.mjs` is a minimal client in plain JavaScript, used to prove that every case can pass. It is test code, not an SDK. Each language gets its own driver beside its package.

```sh
npm run spec:build
npm run conformance  # runs the reference driver
```

## Error kinds

A driver reports these in `error.kind`, with the HTTP `status` where there was one. The rules come from `apis/backmarket/docs/spec-audit.md`.

| Kind | Meaning |
| --- | --- |
| `bad_request` | 400 |
| `authentication` | 401 |
| `permission` | 403 that is neither of the two below |
| `waf_blocked` | 403 HTML block; `cf_ray` carries the `cf-ray` header |
| `bot_challenge` | 403 with `errors[0].code` of `bot-need-challenge` |
| `not_found` | 404 |
| `validation` | 422 |
| `rate_limited` | 429, after retries |
| `server` | 5xx, after retries |
| `api` | Any other status |
| `timeout` | No response within `timeout_ms`, after retries |
| `connection` | The connection failed or dropped before a full response, after retries |
| `decode` | A success response whose declared JSON body does not parse, or whose compressed body cannot be decompressed; a page whose `next` link is not a valid URL |

Errors also carry these, when present: `request_id` from `requestId`, `code` from `error.code` or `errors[0].code`, and `raw_body` with the token removed. A body that fits no known shape, is not JSON, or cannot be decompressed still produces a typed error.

## Limits

10 of the 40 operations have no case yet, mainly the multipart and message operations and the secondary reads. Scripted cases do not pass through Prism, so `mock.responses` wire traffic is checked only by its `wire` entries; `apis/backmarket/docs/spec-audit.md` explains which statuses Prism cannot serve.

These cases are checked against the mock only. Nothing here has been confirmed against the live API.
