# ebay-sell

Unofficial TypeScript client for eBay's Sell, Commerce and Developer REST APIs. This project is unofficial.

eBay is a trademark of eBay Inc. This project is not affiliated with, endorsed by or sponsored by eBay Inc.

**Alpha.** It is tested only against a mock built from the public contracts, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## How it differs from `ebay-api`

[`ebay-api`](https://www.npmjs.com/package/ebay-api) is the established TypeScript client for eBay, and covers far more: the Traditional APIs and the Buy APIs, with years of use against the live API. If you need any of those, or a client that real sellers already rely on, use it.

This package is narrower, and differs in how it is built:

* **Generated from eBay's own contracts.** Every method, parameter and model comes from the OpenAPI contracts eBay publishes for 20 Sell, Commerce and Developer APIs, pinned by SHA-256 and corrected in a reviewed overlay. When eBay changes a contract, a scheduled job opens a pull request with the difference.
* **Typed per API.** Each API is a subpath export, such as `ebay-sell/fulfillment`, with its own request and response types, so a model name that two APIs share never collides.
* **Checked on the wire.** A conformance suite, shared with this project's Python, Go and Rust packages, asserts the exact requests the client sends against a mock built from the contracts: hosts, tokens, headers, signatures, pagination, retries and errors.
* **No runtime dependencies.** It uses Node's built-in `fetch` and Web Crypto, and ships as ESM and CommonJS.

## Before you start

* You need your own keyset from the eBay Developers Program: an App ID, a Cert ID and, for user tokens, a RuName. This package ships with no keys or tokens.
* A production keyset stays disabled until you either set up the Marketplace Account Deletion notification endpoint or are granted an exemption from it. The sandbox has no such step.
* The [eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement) applies to everything you build with this package, and following it is up to you. Among other things:
  * eBay content may not be used to train AI or machine-learning models (§9.10).
  * Content you show must be refreshed: listings at least every 6 hours, and other content at least every 24 hours (§8.1).
  * eBay content may not be used for price modelling or arbitrage (§9.5, §9.6).
  * Restricted APIs need eBay's approval before you call them.
* Sellers domiciled in the EU or UK must sign some calls with a key from the Key Management API: see [Signing](#signing).

## Install

The package is not on npm yet. From a clone of this repository:

```sh
cd apis/ebay/packages/typescript
npm ci && npm run build && npm pack
npm install /path/to/ebay-sell-0.1.0-alpha.1.tgz
```

Requires Node.js 22 or later.

## Quickstart

```ts
import { EbayClient, NotFoundError } from 'ebay-sell';

const client = new EbayClient({ clientId: 'your-app-id', clientSecret: 'your-cert-id' });

const tree = await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' });
console.log(tree?.categoryTreeId);

try {
  await client.taxonomy.categoryTrees.get('0');
} catch (error) {
  if (error instanceof NotFoundError) console.log(error.status, error.code, error.detail);
}
```

With a client ID and secret the client mints application tokens itself, from the client credentials grant, and mints a new one shortly before each expires. Operations that act for a seller need a user token instead:

```ts
import { EbayClient } from 'ebay-sell';

const client = new EbayClient({
  clientId: 'your-app-id',
  clientSecret: 'your-cert-id',
  userToken: 'v^1.1#your-user-token',
  refreshToken: 'v^1.1#your-refresh-token',
  onToken: async (token) => {
    // Store the new access token. The refresh token stays the same.
  },
  marketplaceId: 'EBAY_US',
});

for await (const order of client.fulfillment.orders.iter({ filter: 'orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}' })) {
  console.log(order.orderId);
}
```

A user token lasts two hours and its refresh token about 18 months. When a call is refused with a 401, the client refreshes the user token once, waits for `onToken`, and retries the call. Concurrent calls share one refresh. If the refresh fails, the call rejects with the refresh's error, such as a `BadRequestError` for `invalid_grant`, not the 401. The refresh waits for `onToken`, so it must not call `client.oauth.refresh()` or make a call with the client: those never settle. Store the token and return.

Each API's types are in its own subpath:

```typescript
import type { Order } from 'ebay-sell/fulfillment';
import type { InventoryItem } from 'ebay-sell/inventory';
```

CommonJS works the same way:

```js
const { EbayClient } = require('ebay-sell');
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the environment you selected.

## Getting a user token

eBay uses the OAuth 2 authorization code grant, with your RuName as the redirect URI. The client builds the authorization URL with a fresh `state`, then trades the code eBay sends to your accept URL for a user token:

```ts
import { EbayClient } from 'ebay-sell';

const client = new EbayClient({ clientId: 'your-app-id', clientSecret: 'your-cert-id', ruName: 'your-ru-name' });

const request = client.oauth.authorizationUrl(['https://api.ebay.com/oauth/api_scope/sell.fulfillment']);
// Send the user to request.url, and keep request.state until they return.

// The accept URL eBay redirects to, as your callback receives it:
const returned = new URL(`https://example.com/accept?code=code-from-the-redirect&state=${request.state}`);
const code = returned.searchParams.get('code');
if (code === null || returned.searchParams.get('state') !== request.state) throw new Error('Bad redirect');
const token = await client.oauth.exchangeCode(code);
console.log(token.expiresIn);
```

After `exchangeCode` the client uses the new token, and `client.oauth.refresh()` replaces it on demand. `client.oauth.appToken()` mints an application token now. `authorizationUrl` is also exported on its own.

## Signing

eBay requires sellers domiciled in the EU or UK to sign calls that move money or return financial data, such as those of the Finances API. Create a key pair once with the Key Management API, store its private key, which eBay returns only once, and pass both halves to the client as a `SigningKey`:

```ts
import { EbayClient, SigningKey } from 'ebay-sell';

const admin = new EbayClient({ clientId: 'your-app-id', clientSecret: 'your-cert-id' });
const created = await admin.keyManagement.signingKeys.create({ signingKeyCipher: 'ED25519' });
console.log(created.signingKeyId); // store created.privateKey and created.jwe somewhere safe

const signingKey = await SigningKey.create({ privateKey: created.privateKey ?? '', jwe: created.jwe ?? '' });
const client = new EbayClient({ userToken: 'v^1.1#your-user-token', signingKey });
const summary = await client.finances.sellerFunds.getSummary({ marketplaceId: 'EBAY_GB' });
console.log(summary.totalFunds?.value);
```

Each request then carries `x-ebay-signature-key`, `Signature-Input`, `Signature` and, when it has a body, `Content-Digest`, as RFC 9421 describes. Ed25519 and RSA keys both work. `SigningKey.create` takes the key as Key Management returns it or as a PKCS #8 PEM, and rejects one it cannot use.

## Configuration

Pass `clientId` and `clientSecret`, a token, or both.

| Option | Default | Meaning |
| --- | --- | --- |
| `clientId` | None | Your keyset's App ID |
| `clientSecret` | None | Your keyset's Cert ID. Sent with the App ID only to the token endpoint |
| `ruName` | None | Your RuName, for the authorization code grant |
| `appToken` | None | An application token to use instead of minting one |
| `userToken` | None | A user access token, sent on operations that act for a seller |
| `refreshToken` | None | Lets the client replace an expired user token itself |
| `onToken` | None | Called with every new user `Token`, from `exchangeCode` and every refresh. May return a promise |
| `appScopes` | `[API_SCOPE]` | The scopes of minted application tokens, at least one |
| `userScopes` | None | The scopes to ask for on refresh. eBay keeps the original grant's when this is not given |
| `environment` | `'production'` | `'production'` or `'sandbox'`. Picks the API hosts and the authorization URL |
| `hosts` | None | Your own base URL for each of `api`, `apiz` and `apim`, for tests against a mock. Your credentials are sent to them |
| `marketplaceId` | None | Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call passes its own |
| `contentLanguage` | None | Sent as `Content-Language` on operations that take it, unless a call passes its own |
| `signingKey` | None | A `SigningKey` that signs every request |
| `userAgent` | None | Sent as `User-Agent` when given |
| `timeoutMs` | `30000` | Milliseconds to wait on each attempt, including reading the body |
| `maxRetries` | `3` | Retries after the first attempt |
| `retryBaseDelayMs` | `500` | Base in milliseconds of the exponential backoff |
| `rateLimitWaitMs` | `10000` | Milliseconds to wait after a 429 with no usable `Retry-After` |
| `maxRetryWaitMs` | `60000` | Longest `Retry-After` to wait for. A longer one throws `RateLimitedError` at once |
| `fetch` | Global `fetch` | A `fetch` to use instead |
| `logger` | None | Receives methods, URLs and statuses. `console` fits |

## Behaviour

* **Methods** are grouped by API and then by resource, such as `client.fulfillment.orders`, `client.inventory.inventoryItems`, `client.postOrder.returns`, `client.account.fulfillmentPolicies` and `client.taxonomy.categoryTrees`. 339 of the 346 operations in the 21 contracts have a method; see Limits. Path parameters come first, then the JSON body if there is one, then an object of query, form and header parameters, then options for that call.
* **Names:** methods, parameters and client options are camelCase. Fields of request and response objects keep the API's own names, because they pass through unchanged.
* **Tokens:** an operation that accepts an application token's scope gets the application token, and every other operation gets the user token. With no application token and no way to mint one, the user token is sent instead. Basic authentication with your App ID and Cert ID goes only to the token endpoint.
* **Hosts:** most operations go to `api.ebay.com`. Finances, Identity, Key Management and payment disputes go to `apiz.ebay.com`, and most of Media to `apim.ebay.com`. Each operation goes to its own host in the environment you chose.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them with `for await`, reading the position from each page's `next` link. The link itself is never fetched, so every page goes to the operation's own host.
* **Retries:** 429 on every method, honouring `Retry-After` up to `maxRetryWaitMs`, otherwise after `rateLimitWaitMs`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create an offer twice. A 401 is retried once, after a new application token or a refreshed user token.
* **Cancellation:** pass `{ signal }` as a call's last argument. Aborting it stops the request and any wait before a retry, and the call rejects with the signal's reason.
* **Errors** derive from `ApiError`. Error responses throw an `HttpError` subclass, such as `NotFoundError`, with `kind`, `status`, `errors` (the body's `errors` list as `ErrorDetail`s), `code` and `detail` (the first entry's `errorId` and `message`), `retryAfter` and `rawBody`, with every credential removed. If your process loads both the ESM and CommonJS builds, `instanceof` only matches errors from the same build, so compare `kind` instead. Cast to `ClientError`, and comparing `kind` narrows it to one class.
* **Logging** is off unless you pass `logger`. It never receives your credentials or response bodies.
* **Requests** are checked by the compiler only. eBay declares many numbers as strings, such as `limit` and `offset`, so pass them as strings.
* **Responses** are not checked at all, because the contracts have not been confirmed against the live API. The types describe what the contracts declare: a field can hold another type, a required field can be missing, and unknown fields are kept. Check values if you depend on them. Where an operation may answer an empty 204, its method resolves to `undefined` and its type says so.
* **Uploads** take a `Blob`, a `File`, a `Uint8Array`, or `{ filename, content }`.
* **Redirects** are not followed: a 3xx is an error.

## Limits

* Operations that send or return a raw file are not generated yet: video uploads and document downloads in Media, task input and result files in Feed, dispute evidence files in Fulfillment and report downloads in Marketing. They will follow.
* The Feedback API's list operations have no iterator. Page them with `offset` and `limit`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover eBay's contracts, which are fetched at build time and not included, and grants no right to the eBay name.
