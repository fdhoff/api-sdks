# Spec audit

Audit of the 21 pinned eBay contracts (`apis/ebay/spec/upstream/lock.json`, retrieved 2026-11-08): OpenAPI 3.0.0, 346 operations on 279 paths, 945 schemas once merged. It was written from the public contracts, eBay's public developer documentation and eBay's own public SDK repositories, and checked against the Prism mock only; nothing here has been checked against the live API.

| Group | Contracts |
| --- | --- |
| Sell, 287 operations | Account v1 and v2, Analytics, Feed, Finances, Fulfillment, Inventory, Marketing, Metadata, Negotiation, Recommendation, Stores, Post-Order |
| Commerce, 54 | Taxonomy, Notification, Media, Identity, Feedback, Message |
| Developer, 5 | Key Management, Analytics |

Left out of the first release: Logistics and eDelivery International Shipping (limited release), Catalog, Charity, Translation, VeRO, Client Registration, and every Buy API.

Every contract's `info.license` names the eBay API License Agreement, which grants no right to redistribute it, so no contract is committed. The build fetches each from the URL in `lock.json` and checks its SHA-256.

Post-Order is the exception to where the contracts come from. developer.ebay.com publishes no contract for it, and eBay's order management SDKs for .NET, Java and PHP each carry the same file, `specs/openapi/post-order-api.json` (version 2.10.0, 38 operations). The lock pins the .NET copy at commit `9c536e45041ddae4fb2701b9123fca94b2abd530`, so the drift job never sees a change. TODO: have the drift job compare that pin with the newest commit that touches the file. If eBay removes the file, we will write our own contract from the public Post-Order reference. They are served as JSON, which the pipeline reads as YAML. A missing contract is served as HTTP 200 with an empty body, which the fetch refuses, so a contract eBay withdraws fails the spec drift job. The overlays quote no upstream prose.

Each gap is handled in one place: the shared overlay (`spec/overlay.yaml`), a contract's overlay (`spec/overlay/<contract>.yaml`), `sdk.yaml`, the runtime, or left open.

## Corrected in the shared overlay

| ID | Gap | Correction |
| --- | --- | --- |
| B1 | 513 descriptions sit beside a `$ref`, which OpenAPI 3.0 ignores and Spectral rejects. | Removed. |
| B2 | 112 operations declare a required `Content-Type` header parameter. The client sets it from the body, and Prism refuses a call without a body that does not send one. | Removed. |
| B3 | Any call can answer 429 once a call limit is reached, but no operation declares it. | A `RateLimited` response with eBay's error body, declared on every operation. |
| B4 | 34 Inventory and Marketing operations declare eBay's error object as their 204 body. The 26 with no other success body were typed as returning an error, such as `inventory_items().delete` returning `Option<Error>` in Rust. | The 204 bodies removed. Those 26 return nothing. |

## Corrected in a contract's overlay

| ID | Contract | Gap | Correction |
| --- | --- | --- | --- |
| C1 | `sell_account_v2` | `setUserPreferences` refers to `SetUserPreferencesRequest`, which the contract does not define. | An open object. |
| C2 | `sell_feed` | `uploadFile` sends multipart form data, but declares no request body. | `file` (required), `fileName`, `name` and `type`, the fields eBay's example shows. |
| C3 | `sell_fulfillment` | `uploadEvidenceFile` sends multipart form data, but declares no request body. | `file` (required). |
| C4 | `commerce_media` | `createImageFromFile`, `uploadDocument` and `uploadPostOrderDocument` send multipart form data, and `uploadVideo` raw bytes, but none declares a request body. | `image`; `file`; `file`, `documentUsageType`, `entityType` and `entityId`, all required; and an `application/octet-stream` body. |
| C5 | `sell_finances`, `sell_fulfillment` | EU and UK sellers must sign every Finances call and `issueRefund`. No contract says so. | `x-ebay-signature-required: true` on those 12 operations. eBay ignores signatures elsewhere, so a client with a key signs every call; the mark is for documentation. |
| C6 | `sell_finances`, `commerce_media` | Three Finances operations need `sell.finances.earnings.read`, and three Media operations `commerce.post_order.document`, scopes no flow declares. | Added to the authorization code flow. |
| C7 | `sell_stores`, `commerce_feedback`, `commerce_message` | The security scheme declares no OAuth flow, so the scopes the operations need are undeclared. | An authorization code flow with those scopes. |
| C8 | `sell_feed`, `sell_fulfillment`, `commerce_media`, `sell_marketing` | Feed file downloads and `fetchEvidenceContent` return `application/octet-stream`, and `downloadPostOrderDocument` a PDF, but their schemas are an object or a list of strings. `getReport` returns tab-separated text with an object schema. | A binary string, and a plain string for the report. |
| C9 | `commerce_media` | `uploadPostOrderDocument` answers 201 with the document's location and no body, but declares a JSON body. | The 201 body removed. |
| C10 | `sell_marketing` | `createReportTask` answers 202 with the task's location and no body, but declares eBay's error object as one. | The 202 body removed. |

## Corrected in Post-Order's overlay

All in `spec/overlay/sell_post_order.yaml`. The shared overlay's B1 to B3 apply too, so every Post-Order call declares 429.

| ID | Gap | Correction |
| --- | --- | --- |
| P1 | Nine operations are still declared, though eBay's API deprecation status page lists them as decommissioned in 2026. Five went on 2026-03-02: Close Case, Issue Case Refund, Provide Case Shipment Info, Provide Return Address and Confirm Cancellation Refund. Four went on 2026-03-16: Close Inquiry, Confirm Inquiry Refund, Create Inquiry and Provide Inquiry Refund Info. eBay's Post-Order endpoint list has the other 29. | Removed. The schemas only they used are left in place. |
| P2 | The server is `https://api.ebay.com{basePath}` with `basePath` defaulting to `/post-order/v2`, and every path also starts `/post-order/v2`, so calls would go to `/post-order/v2/post-order/v2/...`. | The server is `https://api.ebay.com`. |
| P3 | The top-level security requirement is `[{}]`, so 19 operations read as anonymous. Eleven ask for a `sell@user` scope that no flow declares, and the scheme lists a client credentials flow that no call accepts. | Every call takes the seller's user token, `Authorization: Bearer <token>`, which is what eBay's order management guide and REST request reference show. The old Post-Order "Making a Call" page still describes `IAF <token>`. We do not send it, and have not verified whether eBay still accepts it. The client credentials flow and the unused `bearerAuth` scheme are removed. |
| P4 | Post-Order's call guide requires `X-EBAY-C-MARKETPLACE-ID` on every call, but no operation declares it. | Declared and required on every path. It takes the client's marketplace default. |
| P5 | Eleven `caseId` and `inquiryId` path parameters are marked optional, which OpenAPI forbids. Five of them are on calls that remain. | Required. |
| P6 | Post-Order sends and accepts JSON, but 4 request bodies and 19 responses are declared as XML, so a client would ask for XML. | JSON, with the same schemas. |
| P7 | All 83 enumerations are typed `object`, though their values are strings. | `string`. |
| P8 | `RefundInfoType` refers to `ActualRefundDetailType`, and `ReturnFileType` and `UploadFileRequest` to `FilePurposeEnum`. The contract defines neither. | Defined from eBay's public type reference: four file purposes, and the seven refund detail fields. |
| P9 | All 17 remaining request bodies are optional. | Required for the 13 calls that cannot do without one. The bodies of `rejectCancellation`, `appealCaseDecision`, `issueInquiryRefund` and `markItemReceived` hold only optional fields, so they stay optional. `uploadReturnFile` also requires `data` and `filePurpose`. |
| P10 | EU and UK sellers must sign six Post-Order calls, according to eBay's digital signature guide. One of them, Issue Case Refund, has been decommissioned. No operation says so. | `x-ebay-signature-required: true` on `createCancellationRequest`, `approveCancellation`, `issueInquiryRefund`, `processReturnRequest` and `issueReturnRefund`. |

`uploadReturnFile` stays JSON, with the file base64-encoded in `data`. That is what both the contract and eBay's call reference say. It is not a multipart upload.

eBay's modern API migration guide names GraphQL replacements for the seller's cancellation, return and inquiry flows. It sets no removal date for the 29 remaining operations, and eBay's deprecation status page lists none.

## Hosts

Operations are served from three hosts. `hosts` in `sdk.yaml` gives each a key, and each operation goes to its first server's key: 314 operations to `api`, 26 to `apiz`, 6 to `apim`.

* Finances lists `apiz` first and serves `getBillingActivities` from `api` through that path's own server. That is what eBay documents, so it needs no correction.
* Fulfillment's payment dispute operations, Identity and Key Management are on `apiz`. Media lists `apim` first and moves seven operations to `api` or `apiz`.

No contract lists the sandbox. `environments` in `sdk.yaml` maps each key to its sandbox host by prefixing `sandbox.`: `api.sandbox.ebay.com`, `apiz.sandbox.ebay.com` and `apim.sandbox.ebay.com`. Each appears in eBay's public material: `api.sandbox` throughout the developer documentation and eBay's OAuth clients, `apiz.sandbox` in the Finances example of eBay's digital signature SDK, and `apim.sandbox` for Media in eBay's listing management SDK.

## Authentication

Runtime:

* Every operation needs `Authorization: Bearer <token>`. There are two kinds of token: an application token from the client credentials grant, and a seller's user token from the authorization code grant, which is refreshed with its refresh token. The token endpoint is not in the contracts; minting and refreshing are each package's job.
* eBay lists the scopes an operation accepts in one requirement, any one of which is enough, where OpenAPI would read them as all required. An operation takes the application token when any of its scopes is in its scheme's client credentials flow: 63 operations, all of Metadata, Taxonomy, Notification and Key Management, two Marketing report metadata calls and Developer Analytics' `getRateLimits`. The other 283 take the user token, every Post-Order call included.

## Headers

* `X-EBAY-C-MARKETPLACE-ID` is required by 61 operations, 29 of them Post-Order's, and `Content-Language` by 7 of the 13 that declare it. Both take a client-level default from `header_defaults` in `sdk.yaml`, sent only where declared, and a call can pass its own.
* `Accept-Language`, `Accept-Encoding`, `Content-Length` and `Content-Range` are declared on a few operations. The runtime owns the encoding and length headers. TODO: expose `Accept-Language` and `Content-Range` as method arguments once a package needs them.

## Pagination

35 operations page with `limit` and `offset`, or `limit` and `continuation_token`, and answer `next` until the last page. The iterator copies the position out of `next`, the toolchain's `next_link` style, and `iterators` in `sdk.yaml` names each operation's list. Feedback's `getFeedback` and `getItemsAwaitingFeedback` are not iterated. Their `next` link sits under `pagination`, and reading it there would change every runtime's iterator for two operations, so callers page them with `offset` and `limit`.

## Rate limits

Limits are per API and per day, published in prose. eBay documents no `Retry-After` on 429, so the runtime waits its rate-limit wait. Developer Analytics reports the limits and usage.

## Mock limits

* Prism checks that a bearer token is present, not which kind, so token choice is checked on the wire only.
* Prism answers a binary or text success with a generated string.

## Open

* Whether `SetUserPreferencesRequest` has the shape of `GetUserPreferencesResponse`. Its error codes name fields, such as `excludedUsers`, that the response does not have.
* Whether Feed's `uploadFile` needs the `name` and `type` fields its example shows.
* Identity: the contract serves it from `apiz`, and eBay's PHP SDK uses `apiz.sandbox`, but eBay's .NET SDK documents `apim.sandbox`.
* Whether any operation besides `uploadPostOrderDocument` answers 201 without its declared body.
* Which OAuth scope Post-Order needs. Neither the contract nor eBay's Post-Order pages name one, so its calls list none and only require a user token.
* Whether Post-Order's error bodies have the `errors` list the other contracts use. Its 500 response is a bare `Error`, and the 429 added by B3 assumes the shared shape.
* Which fields inside Post-Order's request bodies are required, beyond `uploadReturnFile`'s.
