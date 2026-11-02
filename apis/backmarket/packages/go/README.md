# backmarketseller

Unofficial Go client for the Back Market Seller API. This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

**Alpha, and not tagged yet.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Install

From a checkout of this repository, until a version is tagged:

```sh
go mod edit -replace github.com/fdhoff/backmarket-seller-sdk/apis/backmarket/packages/go=../backmarket-seller-sdk/apis/backmarket/packages/go
go get github.com/fdhoff/backmarket-seller-sdk/apis/backmarket/packages/go/backmarketseller
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

	"github.com/fdhoff/backmarket-seller-sdk/apis/backmarket/packages/go/backmarketseller"
)

func main() {
	client, err := backmarketseller.NewClient(
		"your-token",
		"BM-YourCompany-YourIntegration;you@example.com",
		"fr-fr",
		backmarketseller.WithRegion(backmarketseller.RegionEU),
	)
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	params := &backmarketseller.OrdersListParams{PageSize: backmarketseller.Ptr[int64](50)}
	for order, err := range client.Orders.Iter(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*order.OrderID)
	}

	_, err = client.Listings.Get(ctx, "00000000-0000-4000-8000-000000000001")
	var failure *backmarketseller.APIError
	if errors.Is(err, backmarketseller.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.RequestID)
	}
}
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the server you selected.

## Configuration

`NewClient(token, userAgent, locale, options...)` takes the required values in order, and these options:

| Option | Default | Meaning |
| --- | --- | --- |
| `WithRegion` | None | `RegionEU`, `RegionNA` or `RegionAP`. Pass this or `WithBaseURL` |
| `WithEnvironment` | `EnvironmentProduction` | Or `EnvironmentPreprod` |
| `WithBaseURL` | None | A server root, for tests against a mock. Your token is sent to it |
| `WithTimeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `WithMaxRetries` | 3 | Retries after the first attempt |
| `WithRetryBaseDelay` | 500 ms | Base of the exponential backoff |
| `WithRateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `WithMaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for |
| `WithHTTPTransport` | `http.DefaultTransport` | An `http.RoundTripper` to use instead of the network |
| `WithLogger` | None | A `*slog.Logger` |

A `Client` is safe for concurrent use.

## Behaviour

* **Methods** are grouped by resource: `Categories`, `Listings`, `Tasks`, `Orders`, `Buyback`, `Shipping`, `Care` and `Backbox`.
* **Context:** every method takes a `context.Context`. Cancelling it stops the call, including any wait before a retry, and the call returns the context's error, not an `APIError`. Use it for an overall deadline; `WithTimeout` applies to each attempt.
* **Pagination:** `List` methods return one page, and `Iter` methods return an iterator for `range` over every item, following `next` only for its position, against your configured server. An iterator stops after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `WithRateLimitWait`. A `Retry-After` longer than `WithMaxRetryWait` returns `ErrRateLimited` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could repeat a refund.
* **Redirects** are never followed. A 3xx returns `ErrAPI`, so your token stays on the server you selected.
* **Errors** are `*APIError`, with `Kind`, `Status`, `Code`, `RequestID`, `RetryAfter`, `CFRay` and `RawBody` with your token removed. Test the kind with `errors.Is` and a sentinel such as `ErrNotFound`. `ErrPermission` also matches `ErrWAFBlocked` and `ErrBotChallenge`.
* **Logging** goes to your `slog.Logger`, and holds methods, URLs and statuses, never your token or response bodies.
* **Requests:** model and parameter fields are pointers, so a nil field is not sent. Use `Ptr` to set one, including to zero. Types are checked at compile time and nothing more. A field the API types in several ways, such as a price, is `any`.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against the live API. Every field is a pointer because a required field can be missing, so check for nil. A field that does not fit its declared type stays nil and keeps its raw value in the model's `Extra` map, and so do unknown fields and nulls. `json.Marshal` on a model gives all of it back with the API's field names. A body whose top level is not the declared type returns `ErrDecode`, with the body in `RawBody`.
* **Uploads** take `File` values, with an optional name.

## Design

See the [architecture document](https://github.com/fdhoff/backmarket-seller-sdk/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Back Market name.
