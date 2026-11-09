# mirakl-seller

Unofficial TypeScript client for the Mirakl seller API. Not affiliated with, endorsed by or sponsored by Mirakl SAS.

Mirakl runs marketplaces for operators, such as Best Buy. Each operator has its own Mirakl instance, and this client talks to the seller (shop) API of the one you sell on.

**Alpha.** There is no public sandbox, so it is tested only against a mock built from the public spec, never against a live instance. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your operator's base URL and your own shop API key. Both come from that operator's seller back office. This package ships with neither.
* Features, roles and custom fields vary by operator. An operation your operator has not enabled fails with an error from its instance.
* Only shop API keys are supported. A custom credential provider can send anything else.
* Keep the key on a server. Never ship it to a browser.

## How this differs from Mirakl's SDKs

Mirakl's own SDKs are for PHP (`mirakl/sdk-php-shop`, under a proprietary licence) and Java, for its customers. There is none for TypeScript. This package is generated from Mirakl's published OpenAPI spec, as are its siblings in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, jobs, errors and redaction behave the same in each. It adds:

* typed models and methods for all 116 current operations, with no runtime dependencies;
* iterators that walk every page;
* wait methods that poll an import or export until it ends;
* `downloadUrl` for export files, which sends your key only to your operator's instance;
* your key kept out of every error and log line.

## Install

The package is not on npm yet. From a clone of this repository:

```sh
cd apis/mirakl/packages/typescript
npm ci && npm run build && npm pack
npm install /path/to/mirakl-seller-0.1.0-alpha.1.tgz
```

Requires Node.js 22 or later. It ships as ESM and CommonJS.

## Quickstart

```ts
import { MiraklClient, NotFoundError } from 'mirakl-seller';

const client = new MiraklClient({ baseUrl: 'https://your-operator.mirakl.net', apiKey: 'your-shop-api-key' });

const shop = await client.shop.get();
console.log(shop.shop_id, shop.shop_name);

for await (const order of client.orders.iter({ orderStateCodes: 'SHIPPING' })) {
  console.log(order.order_id, order.order_state);
}

try {
  await client.offers.get(1);
} catch (error) {
  if (!(error instanceof NotFoundError)) throw error;
  console.log(error.status, error.rawBody);
}
```

Your key is read from nowhere and stored nowhere: you pass it in, and the client sends it only to `baseUrl`.

## Shops

A key that covers several shops picks one with `shop_id`. Set it once on the client, and override it on any call:

```ts
import { MiraklClient } from 'mirakl-seller';

const client = new MiraklClient({ baseUrl: 'https://your-operator.mirakl.net', apiKey: 'your-shop-api-key', shopId: 2001 });
const own = await client.shop.get();
const other = await client.shop.get({ shopId: 2002 });
console.log(own.shop_id, other.shop_id);
```

## Imports and exports

Imports and exports run in the background. Start one, then wait for it: a wait polls the status every minute by default, since Mirakl allows about one status call a minute, and returns the final status, whether the job completed or failed. A failed import still returns its status, so you can fetch its error report:

```ts
import { MiraklClient } from 'mirakl-seller';

const client = new MiraklClient({ baseUrl: 'https://your-operator.mirakl.net', apiKey: 'your-shop-api-key' });
const csv = new TextEncoder().encode('sku;product-id;product-id-type;price;quantity;state\n');
const { import_id } = await client.offers.import({ file: { filename: 'offers.csv', content: csv }, importMode: 'NORMAL' });
const status = await client.offers.waitForImport(import_id, { intervalMs: 60_000, timeoutMs: 3_600_000 });
if (status.has_error_report) {
  const report = await client.offers.downloadImportErrorReport(import_id);
  console.log(new TextDecoder().decode(await report.bytes()));
}
console.log(status.status);
```

An export's status lists the URLs of its files. Fetch each with `downloadUrl`. Your key goes only to `baseUrl`'s scheme, host and port, and never again once a redirect leaves them, so files stored elsewhere are fetched without it:

```ts
import { MiraklClient } from 'mirakl-seller';

const client = new MiraklClient({ baseUrl: 'https://your-operator.mirakl.net', apiKey: 'your-shop-api-key' });
const { tracking_id } = await client.offers.export({ export_type: 'application/json' });
const status = await client.offers.waitForExport(tracking_id);
for (const url of status.urls ?? []) {
  const file = await client.downloadUrl(url);
  console.log(file.contentType, (await file.bytes()).length);
}
```

| Starts | Waits | Status |
| --- | --- | --- |
| `offers.import` (OF01) | `offers.waitForImport` | OF02 |
| `offers.importStock` (STO01) | `offers.waitForStockImport` | STO02 |
| `products.import` (P41) | `products.waitForImport` | P42 |
| `offers.export` (OF52) | `offers.waitForExport` | OF53 |
| `orders.export` (OR13) | `orders.waitForExport` | OR14 |
| `accounting.exportTransactions` (TL03) | `accounting.waitForTransactionExport` | TL04 |

A wait that reaches `timeoutMs` throws `JobTimeoutError`, whose `result` holds the last status. Price imports (PRI01) have no wait, because their status is a list to filter, not one import to fetch: call `offers.listPriceImports`.

## Configuration

`new MiraklClient(options)` takes:

| Option | Default | Meaning |
| --- | --- | --- |
| `baseUrl` | required | Your operator's Mirakl instance. Your key is sent to it |
| `apiKey` | none | Your shop API key, sent as the whole `Authorization` header, with no scheme. Pass this or `credentials` |
| `credentials` | none | Your own `Credentials` provider, instead of `apiKey` |
| `shopId` | none | Sent as `shop_id` on every call that leaves it unset |
| `userAgent` | none | Sent as `User-Agent` when given |
| `timeoutMs` | `30000` | Milliseconds to wait on each attempt |
| `maxRetries` | `3` | Retries after the first attempt |
| `retryBaseDelayMs` | `500` | Base in milliseconds of the exponential backoff |
| `rateLimitWaitMs` | `10000` | Milliseconds to wait after a 429 with no usable `Retry-After` |
| `maxRetryWaitMs` | `60000` | Longest `Retry-After` to wait for, in milliseconds. A longer one throws `RateLimitedError` at once |
| `fetch` | global `fetch` | A `fetch` to use instead. It must return a redirect as it is under `redirect: 'manual'` |
| `logger` | none | Receives `debug` and `info` lines |

Every method also takes `{ signal }`, an `AbortSignal` that cancels the call. Wait methods take it beside `intervalMs` and `timeoutMs`, and stop between polls when it aborts.

## Behaviour

* **Methods** are grouped by resource: `client.shop`, `client.platform`, `client.offers`, `client.orders`, `client.products`, `client.shipments`, `client.returns`, `client.messages`, `client.accounting`, `client.promotions`, `client.picklists` and `client.users`. Each method's comment ends with Mirakl's API code, such as OR11, so you can find it in Mirakl's docs. Model types are exported from the package root, named after those codes.
* **Not included:** the 11 deprecated operations, and the three placeholder paths for export files, which `downloadUrl` replaces.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them. Six operations page by `offset` and `max` up to `total_count`; the others send each page's `next_page_token` back as `page_token`. Iterators start where your own `offset` or `pageToken` says, and keep `shop_id` on every page.
* **Timeouts:** `timeoutMs` is the time allowed for each attempt, including reading the whole response.
* **Retries:** 429 on every method, honouring `Retry-After` up to `maxRetryWaitMs`, otherwise after `rateLimitWaitMs`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried, because a repeat could act twice.
* **Errors** derive from `ApiError`. Error responses throw an `HttpError` subclass, such as `NotFoundError` or `PermissionDeniedError`, with `status`, `retryAfter` and `rawBody`, the body as text with your key removed. Mirakl's docs define no error body, so the client does not parse one. Compare `error.kind` to narrow the type.
* **Logging** goes only to the `logger` you pass. It holds methods, URLs and statuses, never your key or response bodies, and leaves out the query of a `downloadUrl` URL, which may hold a signature.
* **Responses** are not checked at all, because the spec has not been confirmed against a live instance. The types describe what the spec declares: a field can hold another type, a required field can be missing, and unknown fields are kept. Check values if you depend on them. An empty 204 resolves to `undefined`, and a JSON body that does not parse throws `DecodeError`.
* **Files:** error reports, documents and invoices resolve to a `Download`; read it once with `bytes()` or `body`. Uploads take a `Blob`, a `Uint8Array` or `{ filename, content }`.

## Limits

* Partner OAuth2 tokens are not built in.
* Wait methods send only the job's ID and the client's `shopId`, not a per-call `shopId`.
* Model names follow Mirakl's API codes, such as `OR11Response200Orders`, rather than names of their own.

## Testing

Every test runs against a mock built from the spec. No test uses a real key or calls a Mirakl instance.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mirakl's spec, which is fetched at build time and not included, and grants no right to the Mirakl name.
