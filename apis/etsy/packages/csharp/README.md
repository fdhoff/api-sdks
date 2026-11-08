# EtsySeller

Unofficial .NET client for the Etsy Open API v3. This project is unofficial and is not affiliated with, endorsed by, or supported by Etsy.

The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own Etsy app, approved by Etsy, and its keystring and shared secret. This package ships with no key, and an app's key may not be shared or transferred.
* Etsy's [API Terms of Use](https://www.etsy.com/legal/api) apply to everything you build with it. Among other things, Etsy content you show must be no more than 6 hours old, and the API may not be used for scraping or to train AI models.

## Install

The package is not on NuGet yet. From a clone of this repository, reference the project:

```sh
dotnet add reference path/to/apis/etsy/packages/csharp/src/EtsySeller/EtsySeller.csproj
```

Requires .NET 8 or later.

## Quickstart

```csharp
using EtsySeller;

using var client = new EtsyClient("your-keystring", "your-shared-secret");

await foreach (var listing in client.Listings.ListAllActiveAsync(keywords: "ceramic mug", limit: 100))
{
    Console.WriteLine($"{listing.ListingId} {listing.Title}");
}

try
{
    await client.Shops.GetAsync(1);
}
catch (NotFoundException error)
{
    Console.WriteLine($"{error.Status} {error.Detail}");
}
```

Calls that read or change a shop's private data need an OAuth access token as well as your key:

```csharp
using EtsySeller;

using var client = new EtsyClient("your-keystring", "your-shared-secret", new EtsyClientOptions
{
    AccessToken = "12345678.your-access-token",
    RefreshToken = "12345678.your-refresh-token",
    // Store both tokens: the old refresh token stops working.
    OnToken = (token, cancellationToken) => SaveAsync(token, cancellationToken),
});

var me = await client.Users.GetMeAsync();
await foreach (var receipt in client.Receipts.ListAllAsync(me.ShopId!.Value, wasShipped: false))
{
    Console.WriteLine(receipt.ReceiptId);
}
```

An access token lasts an hour. When a call that needs one is refused with a 401, the client exchanges the refresh token for a new pair once, passes it to `OnToken`, and retries the call. Concurrent calls share one refresh.

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the server you selected.

## Getting a token

Etsy uses the OAuth 2 authorization code flow with PKCE. The client builds the authorization URL with a fresh `state` and code verifier, then trades the code Etsy sends back for a token:

```csharp
using System.Security.Cryptography;
using System.Text;
using EtsySeller;

using var client = new EtsyClient("your-keystring", "your-shared-secret");

var request = client.OAuth.CreateAuthorizationRequest("https://example.com/callback", ["listings_r", "shops_r"]);
// Send the user to request.Url, and keep request.State and request.CodeVerifier until they return.

// Read both from the redirect's query.
var (returnedState, code) = (request.State, "code-from-the-redirect");
if (!CryptographicOperations.FixedTimeEquals(Encoding.UTF8.GetBytes(returnedState), Encoding.UTF8.GetBytes(request.State)))
{
    throw new InvalidOperationException("state mismatch");
}
var token = await client.OAuth.ExchangeCodeAsync(code, request.CodeVerifier, "https://example.com/callback");
Console.WriteLine(token.UserId);
```

The redirect URI must be one registered for your app. After `ExchangeCodeAsync` the client uses the new token, and `client.OAuth.RefreshAsync()` replaces it on demand. `EtsyOAuth.CreateAuthorizationRequest(apiKey, ...)` and `EtsyOAuth.CodeChallenge(verifier)` also work without a client. `EtsyToken` and `AuthorizationRequest` leave the tokens and verifier out of `ToString()`, so they are safe to log.

## Configuration

`new EtsyClient(apiKey, sharedSecret, options)`. `apiKey` is your app's keystring and `sharedSecret` its shared secret; both are sent as `x-api-key` on every call. Every property of `EtsyClientOptions` is optional:

| Property | Default | Meaning |
| --- | --- | --- |
| `AccessToken` | None | An OAuth access token, sent verbatim as a bearer token on calls that need one |
| `RefreshToken` | None | Lets the client replace an expired access token itself |
| `OnToken` | None | Called with every new `EtsyToken`, from `ExchangeCodeAsync` and every refresh |
| `UserAgent` | None | Sent as `User-Agent` when set |
| `BaseUrl` | `https://openapi.etsy.com` | A server root, for tests against a mock. Your credentials are sent to it |
| `Timeout` | 30 seconds | Time allowed for each attempt |
| `MaxRetries` | `3` | Retries after the first attempt |
| `RetryBaseDelay` | 0.5 seconds | Base of the exponential backoff |
| `RateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `MaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for. A longer one throws `RateLimitedException` at once |
| `Logger` | None | An `ILogger` for methods, URLs, statuses and retries |
| `HttpHandler` | None | An `HttpMessageHandler` to use instead of the network. The client does not dispose it |

To send through an `HttpClient` of your own, such as one from `IHttpClientFactory`, pass it as the fourth argument. The client uses it as it is: it neither changes nor disposes it, and its `Timeout` still applies. Its `DefaultRequestHeaders.ExpectContinue` must not be `true`, because that would let a failed write be resent. A plain `new HttpClient()` follows redirects, unlike the client's own handler; build it over `new SocketsHttpHandler { AllowAutoRedirect = false }` to keep your credentials on the server you chose. A handler that retries must skip writes.

## Behaviour

* **Methods** are grouped by resource, such as `Listings`, `ListingImages`, `ListingInventory`, `Receipts`, `Transactions`, `Shops`, `ShippingProfiles` and `Users`. Every one of the API's 107 operations has a method. Every method is asynchronous and takes a `CancellationToken`.
* **Credentials:** `x-api-key` goes on every call. The access token goes only on calls whose spec asks for OAuth, never on public reads.
* **Pagination:** `List…Async` methods return one page and `ListAll…Async` methods return an `IAsyncEnumerable` over all of them. Each page's `offset` advances by the number of results received, from the `offset` you pass, until an empty page or `count`.
* **Timeouts:** `Timeout` is the time allowed for each attempt, including reading the whole response. It throws `ApiTimeoutException`. Cancelling your own token throws `OperationCanceledException` instead.
* **Retries:** 429 on every method, honouring `Retry-After` up to `MaxRetryWait`, otherwise after `RateLimitWait`. A longer `Retry-After`, such as at the daily limit, throws `RateLimitedException` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create a listing twice.
* **Errors** derive from `ApiException`. Error responses throw an `HttpException` subclass with `Kind`, `Status`, `Detail` (the body's `error` text) and `RawBody`, with every credential removed.
* **Logging** holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** form bodies are method arguments, sent form-encoded; a list sends its field once per item. JSON bodies are a generated model.
* **Responses** are read tolerantly, because the spec has not been confirmed against the live API. Every property is nullable. A value that does not fit its property, and any field this version does not know, is kept in the model's `Extra` instead of failing the call. An empty successful body where the spec declares JSON throws `ApiDecodeException`.
* **Free-form and union values** are `object`, holding a `JsonElement`.
* **Uploads** take `UploadFile(fileName, bytes)`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Etsy name.
