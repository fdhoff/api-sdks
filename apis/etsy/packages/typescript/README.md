# etsy-seller

Unofficial TypeScript client for the Etsy Open API v3. This project is unofficial and is not affiliated with, endorsed by, or supported by Etsy.

The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own Etsy app, approved by Etsy, and its keystring and shared secret. This package ships with no key, and an app's key may not be shared or transferred.
* Etsy's [API Terms of Use](https://www.etsy.com/legal/api) apply to everything you build with it. Among other things, Etsy content you show must be no more than 6 hours old, and the API may not be used for scraping or to train AI models.

## Install

The package is not on npm yet. From a clone of this repository:

```sh
cd apis/etsy/packages/typescript
npm ci && npm run build && npm pack
npm install /path/to/etsy-seller-0.1.0-alpha.1.tgz
```

Requires Node.js 22 or later. It works from ESM and CommonJS, uses the built-in `fetch` and Web Crypto, and has no runtime dependencies.

## Quickstart

```ts
import { EtsyClient, NotFoundError } from 'etsy-seller';

const client = new EtsyClient({ apiKey: 'your-keystring', sharedSecret: 'your-shared-secret' });

for await (const listing of client.listings.iterActive({ keywords: 'ceramic mug', limit: 100 })) {
  console.log(listing.listing_id, listing.title);
}

try {
  await client.shops.get(1);
} catch (error) {
  if (error instanceof NotFoundError) console.log(error.status, error.detail);
}
```

Calls that read or change a shop's private data need an OAuth access token as well as your key:

```ts
import { EtsyClient } from 'etsy-seller';

const client = new EtsyClient({
  apiKey: 'your-keystring',
  sharedSecret: 'your-shared-secret',
  accessToken: '12345678.your-access-token',
  refreshToken: '12345678.your-refresh-token',
  onToken: async (token) => {
    // Store both tokens: the old refresh token stops working.
  },
});

const { shop_id: shopId } = await client.users.getMe();
if (shopId === undefined) throw new Error('This user has no shop');
for await (const receipt of client.receipts.iter(shopId, { wasShipped: false })) {
  console.log(receipt.receipt_id);
}
```

An access token lasts an hour. When a call that needs one is refused with a 401, the client exchanges the refresh token for a new pair once, waits for `onToken`, and retries the call. Concurrent calls share one refresh.

CommonJS works the same way:

```js
const { EtsyClient } = require('etsy-seller');
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the server you selected.

## Getting a token

Etsy uses the OAuth 2 authorization code flow with PKCE. The client builds the authorization URL with a fresh `state` and S256 code verifier, then trades the code Etsy sends back for a token:

```ts
import { EtsyClient } from 'etsy-seller';

const redirectUri = 'https://example.com/callback';
const client = new EtsyClient({ apiKey: 'your-keystring', sharedSecret: 'your-shared-secret' });

const request = await client.oauth.authorizationUrl(redirectUri, ['listings_r', 'shops_r']);
// Send the user to request.url, and keep request.state and request.codeVerifier until they return.

// The URL Etsy redirects back to, as your callback receives it:
const returned = new URL(`${redirectUri}?code=code-from-the-redirect&state=${request.state}`);
const code = returned.searchParams.get('code');
if (code === null || returned.searchParams.get('state') !== request.state) throw new Error('Bad redirect');
const token = await client.oauth.exchangeCode(code, { codeVerifier: request.codeVerifier, redirectUri });
console.log(token.userId);
```

The redirect URI must be one registered for your app. After `exchangeCode` the client uses the new token, and `client.oauth.refresh()` replaces it on demand. `authorizationUrl` is also exported on its own.

## Configuration

| Option | Default | Meaning |
| --- | --- | --- |
| `apiKey` | Required | Your app's keystring |
| `sharedSecret` | Required | Your app's shared secret. Sent with the keystring as `x-api-key` on every call |
| `accessToken` | None | An OAuth access token, sent verbatim as a bearer token on calls that need one |
| `refreshToken` | None | Lets the client replace an expired access token itself |
| `onToken` | None | Called with every new `Token`, from `exchangeCode` and every refresh. May return a promise |
| `userAgent` | None | Sent as `User-Agent` when given |
| `baseUrl` | `https://openapi.etsy.com` | A server root, for tests against a mock. Your credentials are sent to it |
| `timeoutMs` | `30000` | Milliseconds to wait on each attempt, including reading the body |
| `maxRetries` | `3` | Retries after the first attempt |
| `retryBaseDelayMs` | `500` | Base in milliseconds of the exponential backoff |
| `rateLimitWaitMs` | `10000` | Milliseconds to wait after a 429 with no usable `Retry-After` |
| `maxRetryWaitMs` | `60000` | Longest `Retry-After` to wait for. A longer one throws `RateLimitedError` at once |
| `fetch` | Global `fetch` | A `fetch` to use instead |
| `logger` | None | Receives methods, URLs and statuses. `console` fits |

## Behaviour

* **Methods** are grouped by resource, such as `listings`, `listingImages`, `listingInventory`, `receipts`, `transactions`, `shops`, `shippingProfiles` and `users`. Every one of the API's 107 operations has a method. Path parameters come first, then the JSON body if there is one, then an object of query or form parameters, then options for that call.
* **Names:** methods, parameters and client options are camelCase. Fields of request and response objects keep the API's own names, such as `listing_id`, because they pass through unchanged.
* **Credentials:** `x-api-key` goes on every call. The access token goes only on calls whose spec asks for OAuth, never on public reads.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them with `for await`. Each page's `offset` advances by the number of results received, from the `offset` you pass, until an empty page or `count`.
* **Retries:** 429 on every method, honouring `Retry-After` up to `maxRetryWaitMs`, otherwise after `rateLimitWaitMs`. A longer `Retry-After`, such as at the daily limit, throws `RateLimitedError` at once, with the header in `retryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create a listing twice.
* **Cancellation:** pass `{ signal }` as a call's last argument. Aborting it stops the request and any wait before a retry, and the call rejects with the signal's reason.
* **Errors** derive from `ApiError`. Error responses throw an `HttpError` subclass with `kind`, `status`, `detail` (the body's `error` text) and `rawBody`, with every credential removed. If your process loads both the ESM and CommonJS builds, `instanceof` only matches errors from the same build, so compare `kind` instead. Cast to `ClientError`, and comparing `kind` narrows it to one class.
* **Logging** is off unless you pass `logger`. It never receives your credentials or response bodies.
* **Requests** are checked by the compiler only. Form bodies are named parameters, sent form-encoded.
* **Responses** are not checked at all, because the spec has not been confirmed against the live API. The types describe what the spec declares: a field can hold another type, a required field can be missing, and unknown fields are kept. Check values if you depend on them.
* **Uploads** take a `Blob`, a `File`, a `Uint8Array`, or `{ filename, content }`.
* **Redirects** are not followed: a 3xx is an error.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Etsy name.
