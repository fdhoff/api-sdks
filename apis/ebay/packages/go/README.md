# ebaysell

Unofficial Go client for eBay's Sell, Commerce and Developer REST APIs. This project is unofficial.

eBay is a trademark of eBay Inc. This project is not affiliated with, endorsed by or sponsored by eBay Inc.

**Alpha.** It is tested only against a mock built from the public contracts, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own keyset from the eBay Developers Program: an App ID, a Cert ID and, for user tokens, a RuName. This module ships with no keys or tokens.
* A production keyset stays disabled until you either set up the Marketplace Account Deletion notification endpoint or are granted an exemption from it. The sandbox has no such step.
* The [eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement) applies to everything you build with this module, and following it is up to you. Among other things:
  * eBay content may not be used to train AI or machine-learning models (§9.10).
  * Content you show must be refreshed: listings at least every 6 hours, and other content at least every 24 hours (§8.1).
  * eBay content may not be used for price modelling or arbitrage (§9.5, §9.6).
  * Restricted APIs need eBay's approval before you call them.
* Sellers domiciled in the EU or UK must sign some calls with a key from the Key Management API: see [Signing](#signing).

## Install

No version is tagged yet, so take a commit from `main`:

```sh
go get github.com/fdhoff/api-sdks/apis/ebay/packages/go@main
```

Requires Go 1.24 or later. The module has no dependencies outside the standard library.

## Quickstart

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/taxonomy"
)

func main() {
	client, err := ebaysell.NewClient(ebaysell.WithClientCredentials("your-app-id", "your-cert-id"))
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	tree, err := client.Taxonomy.CategoryTrees.GetDefaultID(ctx, &taxonomy.CategoryTreesGetDefaultIDParams{MarketplaceID: ebaysell.Ptr("EBAY_US")})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*tree.CategoryTreeID)

	_, err = client.Taxonomy.CategoryTrees.Get(ctx, "0")
	var failure *ebaysell.APIError
	if errors.Is(err, ebaysell.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.Code, failure.Detail)
	}
}
```

With a client ID and secret the client mints application tokens itself, from the client credentials grant, and mints a new one shortly before each expires. Operations that act for a seller need a user token instead:

```go
client, err := ebaysell.NewClient(
	ebaysell.WithClientCredentials("your-app-id", "your-cert-id"),
	ebaysell.WithUserToken("v^1.1#your-user-token"),
	ebaysell.WithRefreshToken("v^1.1#your-refresh-token"),
	// Store the new access token. The refresh token stays the same.
	ebaysell.WithOnToken(func(token ebaysell.Token) { save(token) }),
	ebaysell.WithMarketplaceID("EBAY_US"),
)
if err != nil {
	log.Fatal(err)
}
params := &fulfillment.OrdersListParams{Filter: ebaysell.Ptr("orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}")}
for order, err := range client.Fulfillment.Orders.Iter(ctx, params) {
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*order.OrderID)
}
```

A user token lasts two hours and its refresh token about 18 months. When a call is refused with a 401, the client refreshes the user token once, passes it to the `WithOnToken` function, and retries the call. Concurrent calls, and an explicit `client.OAuth.Refresh`, share one refresh. If the refresh fails, the call returns the refresh's error, such as `ErrBadRequest` for `invalid_grant`, not the 401. The `WithOnToken` function runs before the refresh is finished, so it must not call `client.OAuth.Refresh` or make a call that could get a 401: those wait for it forever. Store the token and return.

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the environment you selected.

## Getting a user token

eBay uses the OAuth 2 authorization code grant, with your RuName as the redirect URI. The client builds the authorization URL with a fresh state, then trades the code eBay sends to your accept URL for a user token:

```go
client, err := ebaysell.NewClient(
	ebaysell.WithClientCredentials("your-app-id", "your-cert-id"),
	ebaysell.WithRuName("your-ru-name"),
	ebaysell.WithOnToken(func(token ebaysell.Token) { save(token) }),
)
if err != nil {
	log.Fatal(err)
}
request, err := client.OAuth.AuthorizationRequest(ebaysell.AuthorizationParams{
	Scopes: []string{"https://api.ebay.com/oauth/api_scope/sell.fulfillment"},
})
if err != nil {
	log.Fatal(err)
}
// Send the user to request.URL, and keep request.State until they return.

returnedState, code := redirect.Query().Get("state"), redirect.Query().Get("code")
if subtle.ConstantTimeCompare([]byte(returnedState), []byte(request.State)) != 1 {
	log.Fatal("state mismatch")
}
token, err := client.OAuth.ExchangeCode(ctx, code)
if err != nil {
	log.Fatal(err)
}
fmt.Println(token.ExpiresIn)
```

After `ExchangeCode` the client uses the new token, and `client.OAuth.Refresh` replaces it on demand. `client.OAuth.AppToken` mints an application token now. `NewAuthorizationRequest` also works without a client. Printing or logging a `Token` shows neither token.

## Signing

eBay requires sellers domiciled in the EU or UK to sign calls that move money or return financial data, such as those of the Finances API. Create a key pair once with the Key Management API, store its private key, which eBay returns only once, and pass both halves to the client as a `SigningKey`:

```go
created, err := keys.KeyManagement.SigningKeys.Create(ctx, &keymanagement.CreateSigningKeyRequest{SigningKeyCipher: ebaysell.Ptr("ED25519")})
if err != nil {
	log.Fatal(err)
}
// Store *created.PrivateKey and *created.Jwe somewhere safe: eBay returns the private key only once.

client, err := ebaysell.NewClient(
	ebaysell.WithUserToken("v^1.1#your-user-token"),
	ebaysell.WithSigningKey(ebaysell.SigningKey{PrivateKey: *created.PrivateKey, JWE: *created.Jwe}),
)
if err != nil {
	log.Fatal(err)
}
summary, err := client.Finances.SellerFunds.GetSummary(ctx, &finances.SellerFundsGetSummaryParams{MarketplaceID: ebaysell.Ptr("EBAY_GB")})
```

Each request then carries `x-ebay-signature-key`, `Signature-Input`, `Signature` and, when it has a body, `Content-Digest`, as RFC 9421 describes. Ed25519 and RSA keys both work, as PEM or as the bare base64 eBay returns. Printing a `SigningKey` hides its private key.

## Configuration

`NewClient(options...)` needs `WithClientCredentials`, a token, or both, and takes these options:

| Option | Default | Meaning |
| --- | --- | --- |
| `WithClientCredentials` | None | Your keyset's App ID and Cert ID. Sent together only to the token endpoint |
| `WithRuName` | None | Your RuName, for the authorization code grant |
| `WithAppToken` | None | An application token to use instead of minting one |
| `WithUserToken` | None | A user access token, sent on operations that act for a seller |
| `WithRefreshToken` | None | Lets the client replace an expired user token itself |
| `WithOnToken` | None | Called with every new user `Token`, from `ExchangeCode` and every refresh |
| `WithAppScopes` | `APIScope` | The scopes of minted application tokens, at least one |
| `WithUserScopes` | None | The scopes to ask for on refresh. eBay keeps the original grant's when this is not given |
| `WithEnvironment` | `Production` | `Production` or `Sandbox`. Picks the API hosts and the authorization URL |
| `WithHosts` | None | Your own base URL for each of `api`, `apiz` and `apim`, for tests against a mock. Your credentials are sent to them |
| `WithMarketplaceID` | None | Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call passes its own |
| `WithContentLanguage` | None | Sent as `Content-Language` on operations that take it, unless a call passes its own |
| `WithSigningKey` | None | A `SigningKey` that signs every request |
| `WithUserAgent` | None | Sent as `User-Agent` |
| `WithTimeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `WithMaxRetries` | 3 | Retries after the first attempt |
| `WithRetryBaseDelay` | 500 ms | Base of the exponential backoff |
| `WithRateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `WithMaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for |
| `WithHTTPTransport` | `http.DefaultTransport` | An `http.RoundTripper` to use instead of the network |
| `WithLogger` | None | A `*slog.Logger` |

A `Client` is safe for concurrent use.

## Behaviour

* **Methods** are grouped by API and then by resource, such as `client.Fulfillment.Orders`, `client.Inventory.InventoryItems`, `client.PostOrder.Returns`, `client.Account.FulfillmentPolicies` and `client.Taxonomy.CategoryTrees`. Each API is a sub-package, such as `ebaysell/fulfillment`, holding its models and params structs. 339 of the 346 operations in the 21 contracts have a method; see Limits.
* **Context:** every method takes a `context.Context`. Cancelling it stops the call, including any wait before a retry, and the call returns the context's error, not an `APIError`. Use it for an overall deadline; `WithTimeout` applies to each attempt. A token request, once sent, finishes even if the context is cancelled, so a new token is not lost.
* **Tokens:** an operation that accepts an application token's scope gets the application token, and every other operation gets the user token. With no application token and no way to mint one, the user token is sent instead. An operation with no token it can use returns an error before anything is sent. Basic authentication with your App ID and Cert ID goes only to the token endpoint.
* **Hosts:** most operations go to `api.ebay.com`. Finances, Identity, Key Management and payment disputes go to `apiz.ebay.com`, and most of Media to `apim.ebay.com`. Each operation goes to its own host in the environment you chose.
* **Pagination:** `List` methods return one page, and `Iter` methods return an iterator for `range` over every item, following each page's `next` link on the operation's own host. An iterator stops after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `WithRateLimitWait`. A `Retry-After` longer than `WithMaxRetryWait` returns `ErrRateLimited` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create an offer twice. A 401 is retried once, after a new application token or a refreshed user token.
* **Redirects** are never followed. A 3xx returns `ErrAPI`, so your credentials stay on the hosts you selected.
* **Errors** are `*APIError`, with `Kind`, `Status`, `Code` and `Detail` (the first entry of the body's `errors` list, its `errorId` and `message`), `RetryAfter` and `RawBody`, with every credential removed. Test the kind with `errors.Is` and a sentinel such as `ErrNotFound` or `ErrConflict`. `ErrorDetails(err)` returns the whole `errors` list as `ErrorDetail`s.
* **Logging** goes to your `slog.Logger`, and holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** model and parameter fields are pointers, so a nil field is not sent. Use `Ptr` to set one, including to zero. eBay declares many numbers as strings, such as `limit` and `offset`, so they are `*string`. Types are checked at compile time and nothing more.
* **Responses** are decoded tolerantly, because the contracts have not been confirmed against the live API. Every field is a pointer because a required field can be missing, so check for nil. A field that does not fit its declared type stays nil and keeps its raw value in the model's `Extra` map, and so do unknown fields and nulls. An empty 204 returns nil. A body whose top level is not the declared type returns `ErrDecode`, with the body in `RawBody`.
* **Uploads** take `File` values, with an optional name.

## Limits

* Operations that send or return a raw file are not generated yet: video uploads and document downloads in Media, task input and result files in Feed, dispute evidence files in Fulfillment and report downloads in Marketing. They will follow.
* The Feedback API's list operations have no iterator. Page them with `Offset` and `Limit`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover eBay's contracts, which are fetched at build time and not included, and grants no right to the eBay name.
