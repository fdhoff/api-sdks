# Spec audit

Audit of the pinned upstream spec (`apis/mirakl/spec/upstream/lock.json`, retrieved 2026-11-09): OpenAPI 3.1.0, 130 operations, one placeholder server, an empty `info.version`. It covers the seller (shop) API of Mirakl's marketplace platform only. It was written from the public spec, the public API documentation and the Prism mock only; nothing here has been checked against the live API.

This project is not affiliated with, endorsed by or sponsored by Mirakl.

## Source

Mirakl publishes the spec as one JSON file, `https://developer.mirakl.com/_spec/content/product/mmp/rest/seller/openapi3.json`. It carries no `info.license`, so it is never committed: the build fetches it from the URL in `lock.json` and checks its SHA-256. The pipeline reads the JSON as YAML, so the cache keeps the `openapi.yaml` name. The overlay quotes no upstream prose.

`info.version` is empty, so the spec drift job compares content by hash, not version. `spec/check-upstream.mjs` runs in the spec drift workflow and fails when the URL cannot be fetched, or answers with an error status, an empty body, a body that is not JSON, JSON that is not an OpenAPI document, or a document with no operations. The drift job itself fails when upstream removes an operation.

The operator, MCM, services and Connect APIs are separate specs and are out of scope. Operator-specific custom fields are data each operator configures, so the SDK passes them through rather than generating them.

## OpenAPI 3.1

The build stays 3.1; there is no down-conversion step. Spectral lints the 3.1 build with no errors, and the pinned OpenAPI Generator generates the Python, TypeScript, Go, C# and Rust clients from it without errors. The only 3.1-only construct upstream is `$ref` with sibling keys, which `stripProse` mostly removes and the generator's normalizer handles where it does not; the generator logs that 3.1 support is in beta and that it cleared the siblings. TODO: add a generic 3.1 to 3.0 step in `toolchain/pipeline` if a language package hits a generator gap.

## Corrected in the overlay

| ID | Gap | Correction |
| --- | --- | --- |
| M1 | 11 operations are deprecated. | Removed. Their replacements are below. |
| M2 | OF54, OR15 and TL05 have placeholder `/dynamic-url/...` paths for the export URLs that OF53, OR14 and TL04 return. | Removed, leaving 116 operations. Users fetch those URLs through the runtimes' URL download, which sends the key only to the base URL's origin. |
| M3 | M1 and M2 leave paths with no operation. | Removed. |
| M4 | Only OR04, OR07 and OR32 declare an error response (400). The docs list 400, 401, 403, 404, 405, 406, 410, 415, 429 and 500 for every call and define no error body. | Shared body-less `BadRequest`, `Unauthorized`, `Forbidden`, `NotFound`, `RateLimited` and `ServerError` responses as 400, 401, 403, 404, 429 and 5XX on every operation; the three that declare 400 keep theirs. `RateLimited` declares `Retry-After` in seconds, as the docs describe. The typed error keeps the status and raw body; other statuses are `api` errors. |
| M5 | No operation declares its paging parameters. | Shared parameters, added where the docs give an operation a Pagination section; see Pagination. |
| M6 | Every request and response example is wrong for its own schema or unchecked; 71 of the 168 contradict their schemas, which fails lint and Prism's responses. | Removed. The mock generates from the schemas instead. |
| M7 | SBC11's `pay_out_state` list gives its item a default of the whole list as one string, which is outside its own enum. | Removed. |

## Deprecated operations

| Removed | Replacement |
| --- | --- |
| M01 | M10 and M11 |
| OF26 | None named upstream; OF22 returns an offer's `quantity` |
| OF51 | OF52, then OF53 and the URLs it returns |
| OR12 | OR11 with `order_ids` |
| OR26 | OR28 |
| OR41 | M10 and M11 |
| OR42 | OR43 and M12 |
| RE02 | RE01 |
| RE11, RE12, RE14 | RE02 with a `reason_type`, itself replaced by RE01 |

## Authentication

Runtime: every request sends the shop API key as the whole `Authorization` header, with no `Bearer` or other scheme. The spec's one scheme, `Shop-API-Key`, is an `apiKey` header named `Authorization`, set on every operation except V01, the health check. The roles listed beside it are Mirakl permissions, not OAuth scopes. Users supply the key at runtime.

## Base URL and shops

The spec's server is the placeholder `https://your-instance.mirakl.net`. Every operator runs its own instance, so `sdk.yaml` has no hosts or environments and the caller always supplies the base URL.

Every operation takes an optional `shop_id` query parameter, which picks a shop when a key covers several. `sdk.yaml` lists it under `query_defaults`, so it can be set once per client and overridden per call.

## Pagination

* **Offset**: IV01, OF21, OR11, P11, P51 and PR01 take `max` (1 to 100, default 10), `offset`, `sort` and `order` (`asc` or `desc`). Each answers `total_count` except P11, so its iterator stops at an empty page.
* **Seek**: DR11, DR12, M11, OF04, PL11, PRI02, RT11, RT12, RT52, SBC11, ST11, ST12, ST42, ST52 and TL02 take `limit` (1 to 100, SBC11 up to 1,000, TL02 up to 2,000) and `page_token`, and answer `next_page_token`. All but M11 take `sort` as `field,ASC` or `field,DESC`. With `page_token` set, the server ignores the other parameters.
* AF01, OF61, OR72, P31, RE01 and S30 answer `total_count` but have no Pagination section in the docs, so they get no paging parameters or iterator. TODO: page them if users find they truncate.

## Jobs

Imports and exports run in the background. `sdk.yaml` names each start operation's status operation and its final states, from the docs:

| Start | Status | ID | Done | Failed |
| --- | --- | --- | --- | --- |
| OF01 | OF02 | `import_id` | `COMPLETE` | `FAILED` |
| P41 | P42 | `import_id` | `COMPLETE` | `TRANSFORMATION_FAILED`, `CANCELLED`, `FAILED` |
| STO01 | STO02 | `import_id` | `COMPLETE` | `FAILED` |
| OF52 | OF53 | `tracking_id` | `COMPLETED` | `FAILED` |
| OR13 | OR14 | `tracking_id` | `COMPLETED` | `FAILED` |
| TL03 | TL04 | `tracking_id` | `COMPLETED` | `FAILED`, `CANCELED` |

* PRI01 has no job. Its status, PRI02, lists imports filtered by an `import_id` query parameter rather than getting one by a path parameter, so it does not fit the toolchain's jobs. TODO: support a status list filtered by ID if users ask.
* P42's `SENT` means the file went to the operator for integration, which can still fail, so it is not final.
* A failed import's report comes from OF03, P44 and P47, PRI03 or STO03. An export's files are the URLs in OF53's, OR14's or TL04's `urls`.

## Files

* Binary downloads: DR73, IV02, M13, OF03, OR73, P44, P45, P46, P47, PRI03, S31 and STO03, plus PM11's `text/csv` alternative to JSON. Of the 17 upstream, OF51, OF54, OR15 and TL05 are removed by M1 and M2.
* Multipart uploads: DR74, M12, M14, OF01, OR43, OR74, P41, PRI01, S32 and STO01. Their inline bodies get names in `packages/names.yaml`; PRI01 and STO01 send the same one-file body, which generators share under one name.

## Open

* P42's `SENT` state is treated as not final from the docs alone.
* Lint warns about unused upstream components and the roles listed as scopes on an `apiKey` scheme. Neither affects generation.
