# mercurybanking

Unofficial Go client for the Mercury API. Not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc.

Mercury is a financial technology company, not a bank. Its banking services are provided through partner banks.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own API token, created in the Mercury dashboard. This module ships with no token. The `secret-token:` prefix is part of the token: pass it whole.
* A read-write token works only from IP addresses you allowlist on Mercury's side. A read-only token needs no allowlist.
* Mercury deletes tokens that go unused for 45 days, and downgrades tokens whose scope is broader than their use. Give each token only what it needs.
* The sandbox at `sandbox.mercury.com` holds dummy data and needs a token created there. A production token does not work in the sandbox, and a sandbox token does not work in production.
* OAuth2 is not supported yet. Mercury approves each OAuth2 integration individually.

## How this differs from Mercury's Go SDK

Mercury maintains an official Go SDK, [mercury-go](https://github.com/MercuryTechnologies/mercury-go). It is supported by Mercury and released often, so if you want the vendor's own client, use it. This module is generated from Mercury's published OpenAPI spec, as are its siblings in Python, TypeScript, C# and Rust in [the same repository](https://github.com/fdhoff/api-sdks), and all of them pass one shared conformance suite. Compared with mercury-go v0.15.0 (2026-11-05):

* **Retries never repeat a write that could act twice.** mercury-go retries connection errors, 408, 409, 429 and 5xx on every method, including writes such as issuing a card or adding a recipient, which carry no idempotency key. This module retries those failures only on GET and on the four money-moving writes when their `idempotencyKey` is set, and other writes only on 429.
* **Webhook verification.** `VerifyWebhook` checks the `Mercury-Signature` header. mercury-go has no helper for it.
* **Coverage:** all 89 operations in Mercury's API reference, against mercury-go's 80.
* **No dependencies** outside the standard library.

## Install

No version is tagged yet, so take a commit from `main`:

```sh
go get github.com/fdhoff/api-sdks/apis/mercury/packages/go@main
```

Requires Go 1.24 or later.

## Quickstart

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"

	"github.com/fdhoff/api-sdks/apis/mercury/packages/go/mercurybanking"
)

func main() {
	client, err := mercurybanking.NewClient("secret-token:your-token")
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	for account, err := range client.Accounts.Iter(ctx, nil) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*account.Name, *account.AvailableBalance)
	}

	params := &mercurybanking.TransactionsListParams{Limit: mercurybanking.Ptr[int64](100), Status: []string{"sent"}}
	for transaction, err := range client.Transactions.Iter(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*transaction.CounterpartyName, *transaction.Amount)
	}

	_, err = client.Recipients.Get(ctx, "00000000-0000-4000-8000-000000000000")
	var failure *mercurybanking.APIError
	if errors.Is(err, mercurybanking.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.RawBody)
	}
}
```

Try it against the sandbox first, with a token created there:

```go
client, err := mercurybanking.NewClient("secret-token:your-sandbox-token", mercurybanking.WithEnvironment(mercurybanking.Sandbox))
if err != nil {
	log.Fatal(err)
}
page, err := client.Recipients.List(ctx, &mercurybanking.RecipientsListParams{Limit: mercurybanking.Ptr[int64](10)})
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the environment you selected.

## Moving money

`Accounts.SendMoney`, `Accounts.RequestSendMoney`, `Accounts.Transfer` and `TransferRequests.Create` require an `IdempotencyKey`. Mercury carries out a request with a given key once, so the client retries these calls after a 5xx, a timeout or a dropped connection, sending the same body and key each time. It never makes up or changes a key. Use a fresh one for each payment you mean to make:

```go
transaction, err := client.Accounts.SendMoney(ctx, "00000000-0000-4000-8000-000000000001", &mercurybanking.PostTransactionAPIRequest{
	RecipientID:    mercurybanking.Ptr("00000000-0000-4000-8000-000000000002"),
	Amount:         mercurybanking.Ptr(12.5),
	PaymentMethod:  mercurybanking.Ptr(mercurybanking.PostTransactionPaymentMethodAch),
	IdempotencyKey: mercurybanking.Ptr(newKey()),
})
if err != nil {
	log.Fatal(err)
}
fmt.Println(*transaction.ID, *transaction.Status)
```

Store the key with the payment, so that a retry of your own, after a crash, sends the same one.

## Webhooks

Mercury signs every webhook with the endpoint's secret, in the `Mercury-Signature` header. Mercury's sandbox sends no webhooks, so check your handler with your own test payloads. Pass the raw body, exactly as it arrived:

```go
http.HandleFunc("/mercury", func(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "unreadable body", http.StatusBadRequest)
		return
	}
	if err := mercurybanking.VerifyWebhook(body, r.Header.Get(mercurybanking.SignatureHeader), secret); err != nil {
		// ErrWebhookMalformedHeader, ErrWebhookTooOld or ErrWebhookBadSignature.
		http.Error(w, "rejected", http.StatusBadRequest)
		return
	}
	w.WriteHeader(http.StatusOK)
})
```

The signature is an HMAC-SHA256 of `<timestamp>.<raw body>`, compared in constant time. A timestamp more than 5 minutes old is rejected, so replays fail: pass `WithWebhookTolerance` to change that. A header may carry several signatures while you rotate a secret; any one that matches is enough. The error never holds the secret or the body.

## Configuration

`NewClient(token, options...)` takes these options:

| Option | Default | Meaning |
| --- | --- | --- |
| `WithEnvironment` | `Production` | `Production` or `Sandbox` |
| `WithHosts` | None | Your own base URL for each of `api` and `vault`, for tests against a mock. Your token is sent to them |
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

* **Methods** are grouped by resource, such as `client.Accounts`, `client.Transactions`, `client.Recipients`, `client.Cards` and `client.Invoices`. All 89 operations in the API reference have a method.
* **Context:** every method takes a `context.Context`. Cancelling it stops the call, including any wait before a retry, and the call returns the context's error, not an `APIError`. Use it for an overall deadline; `WithTimeout` applies to each attempt.
* **Hosts:** every operation goes to `api.mercury.com`, except `Cards.Reveal`, which goes to `vault-api.mercury.com`. In the sandbox both go to `api-sandbox.mercury.com`.
* **Pagination:** `List` methods return one page, and `Iter` methods return an iterator for `range` over every item. Most send each page's `page.nextPage` back as `start_after`. `Accounts.IterTransactions` pages by `offset`, and `Treasury.IterTransactions` by its `cursor`. Iterators start where your own `StartAfter`, `Offset` or `Cursor` says, page forward only, and stop after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `WithRateLimitWait`. A `Retry-After` longer than `WithMaxRetryWait` returns `ErrRateLimited` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET, and on the four money-moving writes when their `IdempotencyKey` is set, with exponential backoff. Other writes are not retried, because a repeat could act twice.
* **Redirects** are never followed. A 3xx returns `ErrAPI`, so your token stays on the hosts you selected.
* **Errors** are `*APIError`, with `Kind`, `Status`, `RetryAfter` and `RawBody`, the body as text with your token removed. Mercury declares no error body, so the client does not parse one. Test the kind with `errors.Is` and a sentinel such as `ErrNotFound`, `ErrPermission` or `ErrConflict`.
* **Logging** goes to your `slog.Logger`, and holds methods, URLs and statuses, never your token or response bodies, so card numbers from `Cards.Reveal` stay out of it.
* **Requests:** model and parameter fields are pointers, so a nil field is not sent. Use `Ptr` to set one, including to zero. IDs are strings. Types are checked at compile time and nothing more.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against the live API. Every field is a pointer because a required field can be missing, so check for nil. A field that does not fit its declared type stays nil and keeps its raw value in the model's `Extra` map, and so do unknown fields and nulls. An empty 204 returns nil. A body whose top level is not the declared type returns `ErrDecode`, with the body in `RawBody`.
* **Files:** `Invoices.DownloadPDF`, `Statements.DownloadPDF` and `Safes.DownloadDocument` return a `*Download`; close its `Body`. Uploads take a `File`, with an optional name.

## Limits

* The optional `Idempotency-Key` header on budget and receipt writes is not exposed yet, so those calls are sent without one and not retried.
* Iterators do not page backward with `end_before`. Call `List` with it instead.
* Some model names keep the spec's spelling, such as `ApiV1SpendBudgetResponse`, rather than Go's initialisms.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mercury's spec, which is fetched at build time and not included, and grants no right to the Mercury name.
