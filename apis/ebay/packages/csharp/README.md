# EbaySell

Unofficial .NET client for eBay's Sell, Commerce and Developer REST APIs. This project is unofficial.

eBay is a trademark of eBay Inc. This project is not affiliated with, endorsed by or sponsored by eBay Inc.

**Alpha.** It is tested only against a mock built from the public contracts, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own keyset from the eBay Developers Program: an App ID, a Cert ID and, for user tokens, a RuName. This package ships with no keys or tokens.
* A production keyset stays disabled until you either set up the Marketplace Account Deletion notification endpoint or are granted an exemption from it. The sandbox has no such step.
* The [eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement) applies to everything you build with this package, and following it is up to you. Among other things:
  * eBay content may not be used to train AI or machine-learning models (§9.10).
  * Content you show must be refreshed: listings at least every 6 hours, and other content at least every 24 hours (§8.1).
  * eBay content may not be used for price modelling or arbitrage (§9.5, §9.6).
  * Restricted APIs need eBay's approval before you call them.
* Sellers domiciled in the EU or UK must sign some calls with a key from the Key Management API: see [Signing](#signing).

## How this differs from eBay's .NET SDKs

eBay publishes its own .NET SDKs, generated with Kiota, as source on GitHub. This package differs in a few ways:

* **One package:** every contract this project covers is in one package, `EbaySell`, with one client, instead of a project per API.
* **NuGet:** it is meant to be installed from NuGet, once published, rather than built from source.
* **Conformance-tested:** the same language-neutral conformance cases run against it as against this project's Python, Go and Rust packages, on every change.
* **Signer included:** request signing for EU and UK sellers is built in, as an option, rather than left to you.
* **Tokens included:** the client mints application tokens, refreshes user tokens and picks the right one for each operation.

## Install

The package is not on NuGet yet. From a clone of this repository, reference the project:

```sh
dotnet add reference path/to/apis/ebay/packages/csharp/src/EbaySell/EbaySell.csproj
```

Requires .NET 8 or later. It depends on BouncyCastle, for Ed25519 signing keys.

## Quickstart

```csharp
using EbaySell;

using var client = new EbayClient(new EbayClientOptions { ClientId = "your-app-id", ClientSecret = "your-cert-id" });

var tree = await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US");
Console.WriteLine(tree.CategoryTreeId);

try
{
    await client.Taxonomy.CategoryTrees.GetAsync("0");
}
catch (NotFoundException error)
{
    Console.WriteLine($"{error.Status} {error.Code} {error.Detail}");
}
```

With a client ID and secret the client mints application tokens itself, from the client credentials grant, and mints a new one shortly before each expires. Operations that act for a seller need a user token instead:

```csharp
using EbaySell;

using var client = new EbayClient(new EbayClientOptions
{
    ClientId = "your-app-id",
    ClientSecret = "your-cert-id",
    UserToken = "v^1.1#your-user-token",
    RefreshToken = "v^1.1#your-refresh-token",
    // Store the new access token. The refresh token stays the same.
    OnToken = (token, cancellationToken) => SaveAsync(token, cancellationToken),
    MarketplaceId = "EBAY_US",
});

await foreach (var order in client.Fulfillment.Orders.ListAllAsync(filter: "orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}"))
{
    Console.WriteLine(order.OrderId);
}
```

A user token lasts two hours and its refresh token about 18 months. When a call is refused with a 401, the client refreshes the user token once, passes it to `OnToken`, and retries the call. Concurrent calls, and an explicit `OAuth.RefreshAsync`, share one refresh. If the refresh fails, the call throws the refresh's error, such as a `BadRequestException` for `invalid_grant`, not the 401. `OnToken` runs before the refresh is finished, so it must not await `OAuth.RefreshAsync` or a call that could get a 401: those wait for it forever. Store the token and return.

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the environment you selected.

## Getting a user token

eBay uses the OAuth 2 authorization code grant, with your RuName as the redirect URI. The client builds the authorization URL with a fresh state, then trades the code eBay sends to your accept URL for a user token:

```csharp
using System.Security.Cryptography;
using System.Text;
using EbaySell;

using var client = new EbayClient(new EbayClientOptions
{
    ClientId = "your-app-id",
    ClientSecret = "your-cert-id",
    RuName = "your-ru-name",
    OnToken = (token, cancellationToken) => SaveAsync(token, cancellationToken),
});

var request = client.OAuth.CreateAuthorizationRequest(["https://api.ebay.com/oauth/api_scope/sell.fulfillment"]);
// Send the user to request.Url, and keep request.State until they return.

// Read both from the redirect's query.
var (returnedState, code) = (request.State, "code-from-the-redirect");
if (!CryptographicOperations.FixedTimeEquals(Encoding.UTF8.GetBytes(returnedState), Encoding.UTF8.GetBytes(request.State)))
{
    throw new InvalidOperationException("state mismatch");
}
var token = await client.OAuth.ExchangeCodeAsync(code);
Console.WriteLine(token.ExpiresIn);
```

After `ExchangeCodeAsync` the client uses the new token, and `client.OAuth.RefreshAsync()` replaces it on demand. `client.OAuth.GetAppTokenAsync()` mints an application token now. `EbayOAuth.CreateAuthorizationRequest(clientId, ruName, environment, scopes)` also works without a client. `EbayToken` leaves both tokens out of `ToString()`, so it is safe to log.

## Signing

eBay requires sellers domiciled in the EU or UK to sign calls that move money or return financial data, such as those of the Finances API. Create a key pair once with the Key Management API, store its private key, which eBay returns only once, and pass both halves to the client as an `EbaySigningKey`:

```csharp
using EbaySell;
using EbaySell.KeyManagement.Models;

var created = await keys.KeyManagement.SigningKeys.CreateAsync(new CreateSigningKeyRequest { SigningKeyCipher = "ED25519" });
// Store created.PrivateKey and created.Jwe somewhere safe: eBay returns the private key only once.

using var client = new EbayClient(new EbayClientOptions
{
    UserToken = "v^1.1#your-user-token",
    SigningKey = new EbaySigningKey(created.PrivateKey!, created.Jwe!),
});
var summary = await client.Finances.SellerFunds.GetSummaryAsync(marketplaceId: "EBAY_GB");
```

Each request then carries `x-ebay-signature-key`, `Signature-Input`, `Signature` and, when it has a body, `Content-Digest`, as RFC 9421 describes. Ed25519 and RSA keys both work, as PEM or as the bare base64 eBay returns. `EbaySigningKey` leaves its private key out of `ToString()`.

## Configuration

`new EbayClient(options)` needs `ClientId` and `ClientSecret`, a token, or both. Every property of `EbayClientOptions` is optional:

| Property | Default | Meaning |
| --- | --- | --- |
| `ClientId`, `ClientSecret` | None | Your keyset's App ID and Cert ID. Sent together only to the token endpoint |
| `RuName` | None | Your RuName, for the authorization code grant |
| `AppToken` | None | An application token to use instead of minting one |
| `UserToken` | None | A user access token, sent on operations that act for a seller |
| `RefreshToken` | None | Lets the client replace an expired user token itself |
| `OnToken` | None | Called with every new user `EbayToken`, from `ExchangeCodeAsync` and every refresh |
| `AppScopes` | `EbayOAuth.ApiScope` | The scopes of minted application tokens |
| `UserScopes` | None | The scopes to ask for on refresh. eBay keeps the original grant's when this is empty |
| `Environment` | `EbayClient.Production` | `EbayClient.Production` or `EbayClient.Sandbox`. Picks the API hosts and the authorization URL |
| `Hosts` | None | Your own base URL for each of `api`, `apiz` and `apim`, for tests against a mock. Your credentials are sent to them |
| `MarketplaceId` | None | Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call passes its own |
| `ContentLanguage` | None | Sent as `Content-Language` on operations that take it, unless a call passes its own |
| `SigningKey` | None | An `EbaySigningKey` that signs every request |
| `UserAgent` | None | Sent as `User-Agent` when set |
| `Timeout` | 30 seconds | Time allowed for each attempt |
| `MaxRetries` | `3` | Retries after the first attempt |
| `RetryBaseDelay` | 0.5 seconds | Base of the exponential backoff |
| `RateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `MaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for. A longer one throws `RateLimitedException` at once |
| `Logger` | None | An `ILogger` for methods, URLs, statuses and retries |
| `HttpHandler` | None | An `HttpMessageHandler` to use instead of the network. The client does not dispose it |

To send through an `HttpClient` of your own, such as one from `IHttpClientFactory`, pass it as the second argument. The client uses it as it is: it neither changes nor disposes it, and its `Timeout` still applies. Its `DefaultRequestHeaders.ExpectContinue` must not be `true`, because that would let a failed write be resent. A plain `new HttpClient()` follows redirects, unlike the client's own handler; build it over `new SocketsHttpHandler { AllowAutoRedirect = false }` to keep your credentials on the hosts you chose. A handler that retries must skip writes.

A client is safe for concurrent use.

## Behaviour

* **Methods** are grouped by API and then by resource, such as `client.Fulfillment.Orders`, `client.Inventory.InventoryItems`, `client.Account.FulfillmentPolicies` and `client.Taxonomy.CategoryTrees`. Each API has its own namespace, such as `EbaySell.Fulfillment.Models` for its models. 310 of the 317 operations in the 20 contracts have a method; see Limits. Every method is asynchronous and takes a `CancellationToken`.
* **Tokens:** an operation that accepts an application token's scope gets the application token, and every other operation gets the user token. With no application token and no way to mint one, the user token is sent instead. An operation with no token it can use throws `InvalidOperationException` before anything is sent. Basic authentication with your App ID and Cert ID goes only to the token endpoint.
* **Cancellation:** cancelling a call stops it, including any wait before a retry, and throws `OperationCanceledException`. A token request, once sent, finishes even if the call is cancelled, so a new token is not lost.
* **Hosts:** most operations go to `api.ebay.com`. Finances, Identity, Key Management and payment disputes go to `apiz.ebay.com`, and most of Media to `apim.ebay.com`. Each operation goes to its own host in the environment you chose.
* **Pagination:** `List…Async` methods return one page and `ListAll…Async` methods return an `IAsyncEnumerable` over every item, following each page's `next` link on the operation's own host.
* **Timeouts:** `Timeout` is the time allowed for each attempt, including reading the whole response. It throws `ApiTimeoutException`.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `RateLimitWait`. A `Retry-After` longer than `MaxRetryWait` throws `RateLimitedException` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create an offer twice. A 401 is retried once, after a new application token or a refreshed user token.
* **Redirects** are never followed by the client's own handler, so your credentials stay on the hosts you selected.
* **Errors** derive from `ApiException`. Error responses throw an `HttpException` subclass, such as `NotFoundException` or `ConflictException`, with `Kind`, `Status`, `Code` and `Detail` (the first entry of the body's `errors` list, its `errorId` and `message`), `Errors` (the whole list, as `EbayErrorDetail`s), `RetryAfter` and `RawBody`, with every credential removed.
* **Logging** holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** JSON bodies are a generated model, and a null property is not sent. eBay declares many numbers as strings, such as `limit` and `offset`, so they are `string` parameters.
* **Responses** are read tolerantly, because the contracts have not been confirmed against the live API. Every property is nullable. A value that does not fit its property, and any field this version does not know, is kept in the model's `Extra` instead of failing the call. An empty 204 returns `null`.
* **Free-form and union values** are `object`, holding a `JsonElement`.
* **Uploads** take `UploadFile(fileName, bytes)`.

## Limits

* Operations that send or return a raw file are not generated yet: video uploads and document downloads in Media, task input and result files in Feed, dispute evidence files in Fulfillment and report downloads in Marketing. They will follow.
* The Feedback API's list operations have no iterator. Page them with `offset` and `limit`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover eBay's contracts, which are fetched at build time and not included, and grants no right to the eBay name.
