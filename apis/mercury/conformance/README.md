# Conformance cases

The cases for this API, in the format described in `toolchain/conformance/README.md`. Fixture values are synthetic.

`reference-driver.mjs` is a minimal client in plain JavaScript, used to prove that every case can pass before any language package exists. It is test code, not an SDK. Each language gets its own driver beside its package.

```sh
API=mercury npm run spec:build
API=mercury npm run conformance  # runs the reference driver
```

## Credentials

`token` in `defaults.yaml` is sent as `Authorization: Bearer <token>` on every request, verbatim. Mercury tokens begin with `secret-token:`, which is part of the token. Every case checks that the token reaches no result, error or log.

## Error kinds

A driver reports these in `error.kind`, with the HTTP `status` where there was one. Mercury declares no error body, so errors carry `raw_body`, the body as text with the token removed.

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
| `decode` | A success response whose declared JSON body is empty or does not parse, a page with no items list, or a next value that repeats the one sent |

## Retries, paging and hosts

* A 429 is retried on every method. 5xx, timeouts and dropped connections are retried on GET, and on the four writes `sdk.yaml` lists under `idempotency` when their `idempotencyKey` is set, with the same body every time.
* Paged operations, and the list each page holds, are in `sdk.yaml` under `iterators`. Most page by cursor: `page.nextPage` goes back as `start_after`. `listAccountTransactions` pages by offset up to `total`, and `getTreasuryTransactions` sends its top-level integer `cursor` back as `cursor`, as a decimal string; 0 is a position, not the end.
* `revealCardPan` goes to the `vault` host key and every other operation to `api`. With `environment`, a driver sends each key's requests to the hostname that environment in `sdk.yaml` gives it.

## Sensitive responses

The `revealCardPan` cases return a synthetic card number and CVC, and `logs_exclude` checks that neither reaches the logs. A driver should log no response body.

## Webhook vectors

`webhooks/mercury-signature.json` holds synthetic vectors for the `Mercury-Signature` header, in the format of `toolchain/conformance/fixtures/webhooks/`. The runner does not use them; each language's tests run them through its package's verifier, and `apis/mercury/tests/webhooks.test.mjs` runs them through the reference driver's.

## Limits

* Not every operation has a case yet. TODO: cover each operation once a language package names them.
* No language runtime passes the treasury paging cases yet: the toolchain's `cursor` style takes only a string next value. See `apis/mercury/docs/spec-audit.md`.

These cases are checked against the mock only. Nothing here has been confirmed against the live API.
