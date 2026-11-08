# etsyseller

Unofficial Go client for the Etsy Open API v3. This project is unofficial and is not affiliated with, endorsed by, or supported by Etsy.

The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own Etsy app, approved by Etsy, and its keystring and shared secret. This module ships with no key, and an app's key may not be shared or transferred.
* Etsy's [API Terms of Use](https://www.etsy.com/legal/api) apply to everything you build with it. Among other things, Etsy content you show must be no more than 6 hours old, and the API may not be used for scraping or to train AI models.

## Install

No version is tagged yet, so take a commit from `main`:

```sh
go get github.com/fdhoff/api-sdks/apis/etsy/packages/go@main
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

	"github.com/fdhoff/api-sdks/apis/etsy/packages/go/etsyseller"
)

func main() {
	client, err := etsyseller.NewClient("your-keystring", "your-shared-secret")
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	params := &etsyseller.ListingsListActiveParams{Keywords: etsyseller.Ptr("ceramic mug"), Limit: etsyseller.Ptr[int64](100)}
	for listing, err := range client.Listings.IterActive(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*listing.ListingID, *listing.Title)
	}

	_, err = client.Shops.Get(ctx, 1)
	var failure *etsyseller.APIError
	if errors.Is(err, etsyseller.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.Detail)
	}
}
```

Calls that read or change a shop's private data need an OAuth access token as well as your key:

```go
client, err := etsyseller.NewClient(
	"your-keystring",
	"your-shared-secret",
	etsyseller.WithAccessToken("12345678.your-access-token"),
	etsyseller.WithRefreshToken("12345678.your-refresh-token"),
	// Store both tokens: the old refresh token stops working.
	etsyseller.WithOnToken(func(token etsyseller.Token) { save(token) }),
)
if err != nil {
	log.Fatal(err)
}
me, err := client.Users.GetMe(ctx)
if err != nil {
	log.Fatal(err)
}
for receipt, err := range client.Receipts.Iter(ctx, *me.ShopID, &etsyseller.ReceiptsListParams{WasShipped: etsyseller.Ptr(false)}) {
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*receipt.ReceiptID)
}
```

An access token lasts an hour. When a call that needs one is refused with a 401, the client exchanges the refresh token for a new pair once, passes it to the `WithOnToken` function, and retries the call. Concurrent calls share one refresh.

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the server you selected.

## Getting a token

Etsy uses the OAuth 2 authorization code flow with PKCE. The client builds the authorization request with a fresh state and code verifier, then trades the code Etsy sends back for a token:

```go
request, err := client.OAuth.AuthorizationRequest(etsyseller.AuthorizationParams{
	RedirectURI: "https://example.com/callback",
	Scopes:      []string{"listings_r", "shops_r"},
})
if err != nil {
	log.Fatal(err)
}
// Send the user to request.URL, and keep request.State and request.CodeVerifier until they return.

returnedState, code := redirect.Query().Get("state"), redirect.Query().Get("code")
if subtle.ConstantTimeCompare([]byte(returnedState), []byte(request.State)) != 1 {
	log.Fatal("state mismatch")
}
token, err := client.OAuth.ExchangeCode(ctx, code, request.CodeVerifier, "https://example.com/callback")
if err != nil {
	log.Fatal(err)
}
userID, _ := token.UserID()
fmt.Println(userID)
```

The redirect URI must be one registered for your app. After `ExchangeCode` the client uses the new token, and `client.OAuth.Refresh` replaces it on demand. `NewAuthorizationRequest` and `CodeChallenge` also work without a client. Printing or logging a `Token` shows neither token.

## Configuration

`NewClient(apiKey, sharedSecret, options...)` takes your app's keystring and shared secret, which are sent together as `x-api-key` on every call, and these options:

| Option | Default | Meaning |
| --- | --- | --- |
| `WithAccessToken` | None | An OAuth access token, sent verbatim as a bearer token on calls that need one |
| `WithRefreshToken` | None | Lets the client replace an expired access token itself |
| `WithOnToken` | None | Called with every new `Token`, from `ExchangeCode` and every refresh |
| `WithUserAgent` | None | Sent as `User-Agent` |
| `WithBaseURL` | `https://openapi.etsy.com` | A server root, for tests against a mock. Your credentials are sent to it |
| `WithTimeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `WithMaxRetries` | 3 | Retries after the first attempt |
| `WithRetryBaseDelay` | 500 ms | Base of the exponential backoff |
| `WithRateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `WithMaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for |
| `WithHTTPTransport` | `http.DefaultTransport` | An `http.RoundTripper` to use instead of the network |
| `WithLogger` | None | A `*slog.Logger` |

A `Client` is safe for concurrent use.

## Behaviour

* **Methods** are grouped by resource, such as `Listings`, `ListingImages`, `ListingInventory`, `Receipts`, `Transactions`, `Shops`, `ShippingProfiles` and `Users`. Every one of the API's 107 operations has a method.
* **Context:** every method takes a `context.Context`. Cancelling it stops the call, including any wait before a retry, and the call returns the context's error, not an `APIError`. Use it for an overall deadline; `WithTimeout` applies to each attempt.
* **Credentials:** `x-api-key` goes on every call. The access token goes only on calls whose spec asks for OAuth, never on public reads.
* **Pagination:** `List` methods return one page, and `Iter` methods return an iterator for `range` over every item. Each page's `offset` advances by the number of results received, from the `Offset` you pass, until an empty page or `count`. An iterator stops after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `WithRateLimitWait`. A `Retry-After` longer than `WithMaxRetryWait`, such as at the daily limit, returns `ErrRateLimited` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create a listing twice.
* **Redirects** are never followed. A 3xx returns `ErrAPI`, so your credentials stay on the server you selected.
* **Errors** are `*APIError`, with `Kind`, `Status`, `Detail` (the body's `error` text), `RetryAfter` and `RawBody`, with every credential removed. Test the kind with `errors.Is` and a sentinel such as `ErrNotFound` or `ErrConflict`. A request that cannot be encoded, such as a body holding NaN, is not sent and returns an error wrapping the encoder's own instead.
* **Logging** goes to your `slog.Logger`, and holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** model and parameter fields are pointers, so a nil field is not sent. Use `Ptr` to set one, including to zero. Form bodies are fields of the method's params struct, sent form-encoded, with a list sent as one field per item. Types are checked at compile time and nothing more.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against the live API. Every field is a pointer because a required field can be missing, so check for nil. A field that does not fit its declared type stays nil and keeps its raw value in the model's `Extra` map, and so do unknown fields and nulls. A body whose top level is not the declared type returns `ErrDecode`, with the body in `RawBody`.
* **Uploads** take `File` values, with an optional name.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Etsy name.
