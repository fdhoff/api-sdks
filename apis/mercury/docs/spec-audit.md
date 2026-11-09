# Spec audit

Audit of the pinned upstream spec (`apis/mercury/spec/upstream/lock.json`, `info.version` 1.0.0): OpenAPI 3.0.0, 132 operations, 427 schemas, one server plus a second on one operation. It was written from the public spec, the public API reference and the Prism mock only; nothing here has been checked against the live API.

Mercury is a financial technology company, not a bank. This project is not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc.

## Source

Mercury publishes the spec through ReadMe's API registry, at `https://dash.readme.com/api/v1/api-registry/<id>`. The spec carries no `info.license`, so it is never committed: the build fetches it from the URL in `lock.json` and checks its SHA-256. It is served as JSON, which the pipeline reads as YAML, so the cache keeps the `openapi.yaml` name. The overlay quotes no upstream prose.

The registry ID changes when Mercury republishes, and a superseded ID keeps answering with its old copy, so a pin can go stale while every request still succeeds. Each page of the API reference names the current ID in its `oasPublicUrl`. `spec/check-upstream.mjs` runs in the spec drift workflow and fails when:

* the registry URL fails, or answers with an empty body, a body that is not JSON, or JSON that is not an OpenAPI document;
* the reference page names a registry ID other than the pinned one, or none.

The drift job itself fails when upstream removes an operation.

To re-pin, point `lock.json` at the ID the reference names, run `API=mercury npm run spec:pin`, and check the operations against the reference index at `https://docs.mercury.com/llms.txt`: every operation the build keeps should have a page there.

OAuth2 lives in a separate registry file on `oauth2.mercury.com`. Mercury approves each OAuth2 integration individually and offers no test path besides the mock, so it is left out. TODO: add the OAuth2 contract, with PKCE and refresh, if users ask.

## Corrected in the overlay

| ID | Gap | Correction |
| --- | --- | --- |
| M1 | 41 operations carry `x-internal`: Books, reimbursements and the MCP feedback endpoint. None has a page in the API reference. | Removed. The filter matches the key's presence, since its value is the string `true`. |
| M2 | Four operations without `x-internal` have no page in the API reference: `getAccount`, `getInvest`, `getInvestActivity` and `submitOnboardingData`. | Removed, leaving 87 operations. |
| M3 | M1 and M2 leave 31 paths with no operation, whose path parameters then have nothing to declare them. | Removed. |
| M4 | Every operation can answer 401 for a missing, invalid or revoked token, and 429 when rate limited, but none declares either. `listCredit`, `getOrganization` and `getSafeRequests` declare no error response at all. | Shared `Unauthorized` and `RateLimited` responses on every operation. Like Mercury's own error responses, they declare no body, so the typed error keeps the status and the raw body. |
| M5 | The bearer scheme's description embeds a sample token string. | Replaced with our own description, so no token-shaped string reaches the build. |

## Authentication

Runtime: every request sends `Authorization: Bearer <token>`, with the token verbatim. Mercury tokens begin with `secret-token:`, which is part of the token. The root security is `bearerAuth` and no operation overrides it. Users supply the token at runtime; read-write tokens need an IP allowlist on Mercury's side.

## Hosts and environments

`sdk.yaml` maps the spec's server to the `api` host key. `revealCardPan` declares its own server, the Vault host, and gets the `vault` key.

| Environment | `api` | `vault` |
| --- | --- | --- |
| `production` | `https://api.mercury.com/api/v1` | `https://vault-api.mercury.com/api/v1` |
| `sandbox` | `https://api-sandbox.mercury.com/api/v1` | `https://api-sandbox.mercury.com/api/v1` |

The spec lists production only; the sandbox host comes from Mercury's sandbox guide. Mercury documents no sandbox Vault host, so the sandbox sends `revealCardPan` to its own API host, keeping a sandbox token off production hosts.

## Pagination

* **Cursor**, the default in `sdk.yaml`: 24 list operations take `start_after`, an exclusive ID, and answer `page.nextPage`. The iterator sends `page.nextPage` back as `start_after` until it is null or absent. They also take `end_before` and answer `page.previousPage`; iterators page forward only.
* **Offset**: `listAccountTransactions` takes `offset` and answers `total`.
* **Integer cursor**: `getTreasuryTransactions` answers a top-level `cursor`, an integer of 0 or more, and takes it back in the `cursor` query parameter. The toolchain's `cursor` style accepts only a string next value. TODO: accept an integer next value in every runtime, sent as its decimal digits, before any language can pass the treasury paging cases.

## Retries

`requestSendMoney`, `createTransaction`, `requestTransferMoney` and `createInternalTransfer` require an `idempotencyKey` in the JSON body. `sdk.yaml` marks them, so the runtimes retry them on 5xx, timeouts and dropped connections, with the same body, when the key is set. Every operation is retried on 429.

## Files

`getInvoicePdf`, `getStatementPdf` and `getSafeRequestDocument` answer `application/pdf` as binary. `uploadRecipientAttachment` and `uploadTransactionAttachment` take a multipart body with one `file` part.

## Webhooks

Mercury signs webhooks in the `Mercury-Signature` header, as `t=<unix seconds>,v1=<hex>` over `<t>.<raw body>` with HMAC-SHA256 and the endpoint's secret, the scheme the toolchain's verifier checks. `conformance/webhooks/mercury-signature.json` holds synthetic vectors. Webhooks are not available in Mercury's sandbox.

## Sensitive responses

`revealCardPan` answers a full card number and CVC. A client may return them but must never log them; a conformance case checks this.

## Mock limits

* Prism serves each path without the server's `/api/v1` prefix, so cases name paths as the spec declares them.
* Prism answers a declared status with no body for M4's responses, so error cases that check a body script their responses.

## Open

* The 429 response's headers, and whether it sends `Retry-After`.
* The body of Mercury's error responses. Every SDK keeps the raw body until it is known.
* Whether the treasury `cursor` can be 0 on a page that is not the last. The cases treat 0 as a position, not as the end.
* Whether `revealCardPan` works in the sandbox at all, and on which host.
