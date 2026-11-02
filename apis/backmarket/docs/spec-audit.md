# Spec audit

Audit of the pinned upstream spec (`apis/backmarket/spec/upstream/lock.json`, `info.version` 0.1.1): OpenAPI 3.0.3, 40 operations on 35 paths, 75 schemas. It was written from the public spec and the Prism mock only; nothing here has been checked against the live API, so anything about real behaviour is inferred from the spec's own prose.

Each gap is handled in one place:

* **Overlay**: the spec is wrong and its own text shows the fix. Listed under [Corrected](#corrected-in-the-overlay).
* **Runtime**: the spec cannot express it, so each language's hand-written runtime does it.
* **Generator config**: naming and shape problems, solved when a language is generated.
* **Open**: only live access or Back Market can settle it. No guess is encoded.

## Corrected in the overlay

| ID | Gap | Correction |
| --- | --- | --- |
| A1 | Prose requires `Authorization: Basic <token>` on every call. 9 operations declare no security, and 5 (all of Orders and Orderline) declare only `BasicAuth`, which means base64 `user:password`. A real token fails that check, and Prism returned 401 for it. | One `ApiKeyAuth` scheme at the root; per-operation security and `BasicAuth` removed. |
| A2 | 9 operations have no `operationId`. | Added, named after their neighbours. |
| A3 | `CategoryTree` requires `childrens` without declaring it, though the docs and examples use it. | Declared as a recursive array. |
| A4 | `buybackCompetitor` requires `winner_price` without declaring it. | Declared, copied from `Competitor`. |
| A5 | `UpdateOrder` requires `id`; the field is `order_id`. | Requires `order_id`. |
| A6 | `Backbox` requires `current`; the field is `currency`. | Requires `currency`. |
| A7 | `next` and `previous` on `GET /ws/sav` are non-nullable, unlike the other 9 paginated endpoints. Upstream's example for `previous` is the string `"null"`. | Both nullable. |
| A8 | `count` on Buyback lists is `number`. | `integer`, matching other lists. |
| A9 | `claim.warnings` is an array without `items`. | Empty `items`; the field is deprecated and untyped. |
| A10 | `category_3.parent` puts `description` and `deprecated` beside a `$ref`, where 3.0 ignores them. | Siblings removed. |

## Authentication and headers

Runtime:

* `Basic` is followed by the token verbatim, with no username and no base64 step. Generated Basic-auth helpers must not be used.
* `User-Agent` is mandatory ("might be refused" otherwise) and is not in the spec. The documented format is `BM-{CompanyName}-{IntegrationName};company@companydomain.com`. Make it required client configuration, because no default can be correct.
* `Accept-Language` is declared on 7 of 40 operations, but prose lists it for every call. Send it on all of them from a client-level locale.
* Do not force `Content-type: application/json` on the 4 multipart operations (invoice, counter-offer, Care problem, Care message).
* Six servers cover three regions (AP, EU, NA), each with prod and preprod. Offer region and environment rather than a raw URL. Accepted locales differ by region.

## Pagination

Four shapes, none of them shared by a common schema name:

| Style | Parameters | Operations |
| --- | --- | --- |
| Page and size | `page`, `page-size` (default 10, max 50) | `/ws/listings`, `/ws/orders`, `/ws/listings_bi` |
| Page only | `page` | Buyback orders, pending-reply and messages; shipping deliveries and returns |
| Page, or ID floor | `page` (10 per page), `last_id` | `/ws/sav` |
| Cursor | `cursor`, `pageSize` (default and max 100), no `count` or `previous` | `/ws/buyback/v1/listings` |

Runtime:

* Iterate until `next` is null. It is the only end signal all four share.
* Read the `page` or `cursor` value out of `next` and reissue the request against the configured server. Do not fetch `next` directly: `next` is a full URL, the `/ws/sav` example uses a different host (`backmarket.fr`, no `www`), and following it would send the token wherever the URL points.
* `count` is the total on most lists but "on the current page" on `/ws/sav`, so it must not drive iteration.

## Rate limits

No limit is machine-readable. `Retry-After` and `X-RateLimit-*` appear nowhere in the spec.

* Cloudflare answers 429 "usually" above 200 requests in 10 seconds, blocking for 10 seconds; "sensible" endpoints such as catalog trip at 20 in 10 seconds.
* Listing updates may be refused with 429 above 2,000 SKU lines per hour.
* Care endpoints document their own limits in prose:

| Operation | Per minute | Per day |
| --- | --- | --- |
| `GET /ws/sav` | 520 | 4,000 |
| `GET /ws/sav/{careFolderId}` | 600 | 40,000 |
| `POST /ws/sav/{careFolderId}/problem` | 750 | 1,000 |
| `POST /ws/sav/refund` | not stated | 500 |
| `POST /ws/sav/{careFolderId}/msg` | 560 | 40,000 |
| `POST /ws/sav/{careFolderId}/item-transfer` | 292 | 500 |

429 is declared on only 4 operations, and on none of those Care endpoints.

Runtime:

* Handle 429 on every operation. Honour `Retry-After` if present, otherwise wait at least 10 seconds, the only documented block length.
* Retry 429 for every method, since the request was refused. Retry 5xx and timeouts only for GET: no idempotency key is documented, and a repeated `POST /ws/sav/refund` could refund twice.

## Errors

Seven JSON shapes, plus plain text, and 51 error responses declare no body at all:

| Shape | Declared on (responses) |
| --- | --- |
| No body declared | 51 |
| `ErrorResponseV3` (`application/problem+json`) | 39 |
| `ErrorResponseV1` | 22 |
| `ProblemValidation` | 6 |
| `Problem` | 6 |
| Plain string (`text/plain`) | 6 |
| `ValidationErrorResponseV3` (`application/problem+json`) | 3 |
| `ErrorResponseV2` | 2 |
| Plain string (`application/json`) | 2 |
| `OrderIdValidationError` | 2 |

401 is missing from 13 operations and 5xx from 29.

Runtime:

* Map on status first, then parse the body best-effort. A body that fits no shape, or is not JSON, must still produce a typed error carrying the status and raw text.
* Distinguish the two 403s prose describes: a Cloudflare WAF block is HTML and carries `cf-ray`, which support needs, and bot management returns `{"errors": [{"code": "bot-need-challenge", ...}]}`.
* Surface `requestId` when present.

## Schemas

Generator config:

* `Address`/`address`, `Order`/`order` and `OrderLine`/`orderline` differ only by case and collide on case-insensitive filesystems and in several languages. Map the lowercase Care models to distinct names.
* Schema names mix kebab, camel and Pascal case, and the existing `operationId`s mix three conventions. Set public names per language rather than inheriting them.
* `listingId` on `/ws/listings/{listingId}` is `oneOf` UUID or integer. Prefer a plain string parameter in public signatures; the docs prefer the UUID.

Each package holds these in its `generate.yaml` and `operations.yaml`.

Open:

* 6 Buyback date filters use the invalid format `datetime`, with date-only examples. Generators will treat them as plain strings; whether a full timestamp is accepted is unknown.
* `/ws/tasks/{taskId}` has an untyped `result` that "depends on the task action". `action_status` allows 0, 2, 3, 7, 8 and 9, but 3 and 7 are undefined, and the `TaskStatus` enum the text cites does not exist.
* 8 of 14 request bodies omit `requestBody.required`. Each may be genuinely optional or an omission, so none was changed.
* `POST /ws/orders/{order_id}/invoice`, `POST /ws/sav/{careFolderId}/problem` and `POST /ws/sav/{careFolderId}/item-transfer` declare no success body. `POST /ws/sav/refund` returns `text/plain` with undocumented content.
* Prose uses trailing slashes (`/ws/listings/`, `/ws/sav/?page=2`) while paths have none. Whether both work is unknown; use the spec's form.
* `#best-practices`, which the data limits refer to, has no target in the document, along with other dangling anchors. The advice it points to is not available to this project.

## Metadata

* The spec has no licence statement. It is fetched at build time and not redistributed, so this does not block publishing.
* `info.contact.email` is the placeholder `NA@NA.com`, and `info.version` is not a reliable change signal, so the pin is the SHA-256.
* No top-level `tags` block; every operation's tag is undefined. The linter rule is off in `toolchain/spectral.yaml`.
* 3 operations have no description. These remain as lint warnings.

## Mock limits

Prism only returns statuses the spec declares; `Prefer: code=429` on any other operation returns 404. With `Accept: application/json`, which the docs require, it also ignores a status declared only as `application/problem+json` and returns 200. For conformance cases:

* 429 is available from Prism on `POST /ws/listings` and `POST /ws/listings/{listingId}`.
* 5xx is not available from Prism on the operations probed; they declare it as `application/problem+json`.
* `POST /ws/sav/refund` declares only `text/plain` and gets a 406.
* Prism cannot simulate a timeout, a response sequence or a Cloudflare HTML body.

The conformance harness in `toolchain/conformance/` scripts all of these. See `apis/backmarket/conformance/README.md`.
