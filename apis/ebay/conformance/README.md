# Conformance cases

The cases for eBay's APIs, in the format described in `toolchain/conformance/README.md`. Operations are named `<contract>.<operationId>`, as in the merged mock spec. Fixture values are synthetic.

`reference-driver.mjs` is a minimal client in plain JavaScript, used to prove that every case can pass before any language package exists. It is test code, not an SDK. Each language gets its own driver beside its package.

```sh
API=ebay npm run spec:build
API=ebay npm run conformance  # runs the reference driver
```

## Credentials

`defaults.yaml` names two synthetic secrets, and every case checks that neither reaches the driver's result, error or logs:

| Setting | Sent as |
| --- | --- |
| `app_token` | `Authorization: Bearer <app_token>` on operations that accept an application token |
| `user_token` | `Authorization: Bearer <user_token>` on every other operation |

An operation accepts an application token when any scope it lists is one its scheme's client credentials flow declares. eBay lists the scopes an operation accepts, any one of which is enough, so an operation that lists both kinds, such as `sell_metadata.getItemConditionPolicies`, takes the application token.

## Settings

| Setting | Meaning |
| --- | --- |
| `header_defaults` | Values for `X-EBAY-C-MARKETPLACE-ID` and `Content-Language`, by header name. Sent only by operations that declare the header. A call's own value, passed in `params` by header name, wins |
| `signature_key` | The public key JWE from the Key Management API. When set, every request is signed as described below |

## Signatures

With a `signature_key`, the driver adds `x-ebay-signature-key` and signs the request (RFC 9421) over `content-digest`, `x-ebay-signature-key`, `@method`, `@path` and `@authority`, with a `created` time, under the label `sig1`. A request with a body also carries `Content-Digest: sha-256=:<base64>:` (RFC 9530) over the exact bytes sent, and a request without one leaves `content-digest` out of the covered components. Each attempt is signed again. Drivers sign with an Ed25519 key they generate, so no private key is stored here.

## Error kinds

A driver reports these in `error.kind`, with the HTTP `status` where there was one. Errors also carry `raw_body` with every secret removed, and, from the first entry of the body's `errors` list, its `message` as `message` and its `errorId` as `code`.

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
| `decode` | A success response other than 204 whose declared JSON body is empty or does not parse, or a page without its items list or whose `next` does not advance |

## Retries and paging

Retries follow the toolchain runtime: a 429 is retried on every method, and 5xx, timeouts and dropped connections on GET only. eBay documents no `Retry-After`, so a 429 without one waits the rate-limit wait.

Paged operations answer `next` until their last page. The iterator copies `offset`, `limit` and `continuation_token` out of `next` into its own request, against its own host, and never fetches the link. `iterators` in `apis/ebay/sdk.yaml` names the list each operation's pages hold.

## Limits

* Every case goes to one base URL. TODO: add host routing and sandbox cases once the harness records each request's host key.
* No case downloads a binary body: the case format has no way to state bytes. TODO: add Feed file, evidence and document downloads once runtimes return binary bodies.
* The raw video upload has no case, for the same reason.
* Signature cases check the headers' form and the digest's shape, not the signature itself. TODO: assert the digest exactly once the harness checks it.
* Feedback's two paged operations have no iterator, so no paging case.

These cases are checked against the mock only. Nothing here has been confirmed against the live API.
