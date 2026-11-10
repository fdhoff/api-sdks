# mercury-banking

Unofficial TypeScript client for the Mercury API. Not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc.

Mercury is a financial technology company, not a bank. Its banking services are provided through partner banks.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own API token, created in the Mercury dashboard. This package ships with no token. The `secret-token:` prefix is part of the token: pass it whole.
* A read-write token works only from IP addresses you allowlist on Mercury's side. A read-only token needs no allowlist.
* Mercury deletes tokens that go unused for 45 days, and downgrades tokens whose scope is broader than their use. Give each token only what it needs.
* The sandbox at `sandbox.mercury.com` holds dummy data and needs a token created there. A production token does not work in the sandbox, and a sandbox token does not work in production.
* OAuth2 is not supported yet. Mercury approves each OAuth2 integration individually.
* Keep the token on a server. Never ship it to a browser.

## How this differs from Mercury's SDKs

Mercury publishes an official Go SDK, and none for TypeScript. This package is generated from Mercury's published OpenAPI spec, as are its siblings in Python, Go, C# and Rust in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, errors and redaction behave the same in each. It adds:

* typed models and methods for every operation, with no runtime dependencies;
* retries for the four money-moving writes, safe because each carries your `idempotencyKey`;
* iterators that walk every page;
* a verifier for the `Mercury-Signature` webhook header;
* your token kept out of every error and log line.

## Install

The package is not on npm yet. From a clone of this repository:

```sh
cd apis/mercury/packages/typescript
npm ci && npm run build && npm pack
npm install /path/to/mercury-banking-0.1.0-alpha.1.tgz
```

Requires Node.js 22 or later. It ships as ESM and CommonJS.

## Quickstart

```ts
import { MercuryClient, NotFoundError } from 'mercury-banking';

const client = new MercuryClient({ token: 'secret-token:your-token' });

for await (const account of client.accounts.iter()) {
  console.log(account.name, account.availableBalance);
}

for await (const transaction of client.transactions.iter({ limit: 100, status: ['sent'] })) {
  console.log(transaction.counterpartyName, transaction.amount);
}

try {
  await client.recipients.get('00000000-0000-4000-8000-000000000000');
} catch (error) {
  if (!(error instanceof NotFoundError)) throw error;
  console.log(error.status, error.rawBody);
}
```

Try it against the sandbox first, with a token created there:

```ts
import { MercuryClient } from 'mercury-banking';

const client = new MercuryClient({ token: 'secret-token:your-sandbox-token', environment: 'sandbox' });
const page = await client.recipients.list({ limit: 10 });
console.log(page.recipients.map((recipient) => recipient.name));
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the environment you selected.

## Moving money

`accounts.sendMoney`, `accounts.requestSendMoney`, `accounts.transfer` and `transferRequests.create` require an `idempotencyKey`. Mercury carries out a request with a given key once, so the client retries these calls after a 5xx, a timeout or a dropped connection, sending the same body and key each time. It never makes up or changes a key. Use a fresh one for each payment you mean to make:

```ts
import { MercuryClient } from 'mercury-banking';

const client = new MercuryClient({ token: 'secret-token:your-token' });
const transaction = await client.accounts.sendMoney('00000000-0000-4000-8000-000000000001', {
  recipientId: '00000000-0000-4000-8000-000000000002',
  amount: 12.5,
  paymentMethod: 'ach',
  idempotencyKey: crypto.randomUUID(),
});
console.log(transaction.id, transaction.status);
```

Store the key with the payment, so that a retry of your own, after a crash, sends the same one.

## Webhooks

Mercury signs every webhook with the endpoint's secret, in the `Mercury-Signature` header. Mercury's sandbox sends no webhooks, so check your handler with your own test payloads. Pass the raw body, exactly as it arrived:

```ts
import { SIGNATURE_HEADER, verifyWebhook, WebhookSignatureError } from 'mercury-banking';

async function handle(body, headers, secret) {
  try {
    await verifyWebhook(body, headers.get(SIGNATURE_HEADER), secret);
  } catch (error) {
    if (!(error instanceof WebhookSignatureError)) throw error;
    console.log('rejected:', error.reason); // malformed-header, too-old or bad-signature
    return 400;
  }
  return 200;
}

console.log(await handle(new Uint8Array(), new Headers(), 'your-webhook-secret'));
```

The signature is an HMAC-SHA256 of `<timestamp>.<raw body>`, compared in constant time. A timestamp more than 5 minutes old is rejected, so replays fail: pass `{ toleranceSeconds }` to change that. A header may carry several signatures while you rotate a secret; any one that matches is enough. The error never holds the secret or the body.

## Configuration

`new MercuryClient(options)` takes:

| Option | Default | Meaning |
| --- | --- | --- |
| `token` | required | Your API token, sent as `Authorization: Bearer <token>` |
| `environment` | `production` | `production` or `sandbox` |
| `hosts` | none | Your own base URL for each of `api` and `vault`, for tests against a mock. The token is sent to them |
| `userAgent` | none | Sent as `User-Agent` when given |
| `timeoutMs` | `30000` | Milliseconds to wait on each attempt |
| `maxRetries` | `3` | Retries after the first attempt |
| `retryBaseDelayMs` | `500` | Base in milliseconds of the exponential backoff |
| `rateLimitWaitMs` | `10000` | Milliseconds to wait after a 429 with no usable `Retry-After` |
| `maxRetryWaitMs` | `60000` | Longest `Retry-After` to wait for, in milliseconds. A longer one throws `RateLimitedError` at once |
| `fetch` | global `fetch` | A `fetch` to use instead |
| `logger` | none | Receives `debug` and `info` lines |

Every method also takes `{ signal }`, an `AbortSignal` that cancels the call.

## Behaviour

* **Methods** are grouped by resource, such as `client.accounts`, `client.transactions`, `client.recipients`, `client.cards` and `client.invoices`. All 89 operations in the API reference have a method. Model types are exported from the package root.
* **Hosts:** every operation goes to `api.mercury.com`, except `cards.reveal`, which goes to `vault-api.mercury.com`. In the sandbox both go to `api-sandbox.mercury.com`.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them. Most send each page's `page.nextPage` back as `start_after`. `accounts.iterTransactions` pages by `offset`, and `treasury.iterTransactions` by its `cursor`. Iterators start where your own `startAfter`, `offset` or `cursor` says, and page forward only.
* **Timeouts:** `timeoutMs` is the time allowed for each attempt, including reading the whole response.
* **Retries:** 429 on every method, honouring `Retry-After` up to `maxRetryWaitMs`, otherwise after `rateLimitWaitMs`. 5xx, timeouts and connection failures on GET, and on the four money-moving writes when their `idempotencyKey` is set, with exponential backoff. Other writes are not retried, because a repeat could act twice.
* **Errors** derive from `ApiError`. Error responses throw an `HttpError` subclass, such as `NotFoundError` or `PermissionDeniedError`, with `status`, `retryAfter` and `rawBody`, the body as text with your token removed. Mercury declares no error body, so the client does not parse one. Compare `error.kind` to narrow the type.
* **Logging** goes only to the `logger` you pass. It holds methods, URLs and statuses, never your token or response bodies, so card numbers from `cards.reveal` stay out of it.
* **Responses** are not checked at all, because the spec has not been confirmed against the live API. The types describe what the spec declares: a field can hold another type, a required field can be missing, and unknown fields are kept. Check values if you depend on them. An empty 204 resolves to `undefined`, and a JSON body that does not parse throws `DecodeError`.
* **Files:** `invoices.downloadPdf`, `statements.downloadPdf` and `safes.downloadDocument` resolve to a `Download`; read it once with `bytes()` or `body`. Uploads take a `Blob`, a `Uint8Array` or `{ filename, content }`.

## Limits

* The optional `Idempotency-Key` header on budget and receipt writes is not exposed yet, so those calls are sent without one and not retried.
* Iterators do not page backward with `endBefore`. Call `list` with it instead.

## Testing

Every test runs against a mock built from the spec. No test uses a real token or calls Mercury.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mercury's spec, which is fetched at build time and not included, and grants no right to the Mercury name.
