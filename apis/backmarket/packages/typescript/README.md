# backmarket-seller

Unofficial TypeScript client for the Back Market Seller API. This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Install

```sh
npm install backmarket-seller@alpha
```

Requires Node.js 22 or later. It works from ESM and CommonJS, uses the built-in `fetch`, and has no runtime dependencies.

## Quickstart

```ts
import { BackMarketClient, NotFoundError } from 'backmarket-seller';

const client = new BackMarketClient({
  token: 'your-token',
  userAgent: 'BM-YourCompany-YourIntegration;you@example.com',
  locale: 'fr-fr',
  region: 'eu',
});

for await (const order of client.orders.iter({ pageSize: 50 })) {
  console.log(order.order_id);
}

try {
  await client.listings.get('00000000-0000-4000-8000-000000000001');
} catch (error) {
  if (error instanceof NotFoundError) console.log(error.status, error.requestId);
}
```

CommonJS works the same way:

```js
const { BackMarketClient } = require('backmarket-seller');
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the server you selected.

## Behaviour

* **Methods** are grouped by resource: `categories`, `listings`, `tasks`, `orders`, `buyback`, `shipping`, `care` and `backbox`. Path parameters come first, then the JSON body if there is one, then an object of query or form parameters.
* **Names:** methods, parameters and client options are camelCase. Fields of request and response objects keep the API's own names, such as `order_id`, because they pass through unchanged. That keeps them matching the API's documentation, and lets unknown fields through.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them with `for await`, following `next` only for its position, against your configured server.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `rateLimitWaitMs`. A `Retry-After` longer than `maxRetryWaitMs`, 60 seconds by default, is not waited for: the 429 is thrown at once with the header's value in `retryAfter`, so you can reschedule. A wait longer than a timer can hold, about 24 days, is thrown the same way. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could repeat a refund.
* **Timeouts:** `timeoutMs` covers each attempt, including reading the body.
* **Errors** derive from `ApiError` and carry `kind`, `status`, `code`, `requestId` and `rawBody` with your token removed. `WafBlockedError` also has `cfRay`. If your process loads both the ESM and CommonJS builds, `instanceof` only matches errors from the same build, so compare `kind` instead.
* **Logging** is off unless you pass `logger`, which can be `console`. It receives methods, URLs and statuses, never your token or response bodies.
* **Requests** are checked by the compiler only. There is no runtime validation.
* **Responses** are not checked at all, because the spec has not been confirmed against the live API. The types describe what the spec declares: a field can hold another type, a required field can be missing, an enum can hold a new value, and unknown fields are kept. Check values if you depend on them.
* **Uploads** take a `Blob`, a `File`, a `Uint8Array`, or `{ filename, content }`.
* **Redirects** are not followed: a 3xx is an error.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Back Market name.
