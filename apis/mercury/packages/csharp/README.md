# MercuryBanking

Unofficial .NET client for the Mercury API. Not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc.

Mercury is a financial technology company, not a bank. Its banking services are provided through partner banks.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own API token, created in the Mercury dashboard. This package ships with no token. The `secret-token:` prefix is part of the token: pass it whole.
* A read-write token works only from IP addresses you allowlist on Mercury's side. A read-only token needs no allowlist.
* Mercury deletes tokens that go unused for 45 days, and downgrades tokens whose scope is broader than their use. Give each token only what it needs.
* The sandbox at `sandbox.mercury.com` holds dummy data and needs a token created there. A production token does not work in the sandbox, and a sandbox token does not work in production.
* OAuth2 is not supported yet. Mercury approves each OAuth2 integration individually.

Mercury publishes no official .NET SDK. This package is generated from Mercury's published OpenAPI spec, as are its siblings in Python, TypeScript, Go and Rust in [the same repository](https://github.com/fdhoff/api-sdks), and all of them pass one shared conformance suite.

## Install

The package is not on NuGet yet. From a clone of this repository, reference the project:

```sh
dotnet add reference path/to/apis/mercury/packages/csharp/src/MercuryBanking/MercuryBanking.csproj
```

Requires .NET 8 or later.

## Quickstart

```csharp
using MercuryBanking;

using var client = new MercuryClient("secret-token:your-token");

await foreach (var account in client.Accounts.ListAllAsync())
{
    Console.WriteLine($"{account.Name} {account.AvailableBalance}");
}

await foreach (var transaction in client.Transactions.ListAllAsync(status: ["sent"], limit: 100))
{
    Console.WriteLine($"{transaction.CounterpartyName} {transaction.Amount}");
}

try
{
    await client.Recipients.GetAsync(Guid.Parse("00000000-0000-4000-8000-000000000000"));
}
catch (NotFoundException error)
{
    Console.WriteLine($"{error.Status} {error.RawBody}");
}
```

Try it against the sandbox first, with a token created there:

```csharp
using var sandbox = new MercuryClient("secret-token:your-sandbox-token", new MercuryClientOptions { Environment = MercuryClient.Sandbox });
var page = await sandbox.Recipients.ListAsync(limit: 10);
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the environment you selected.

## Moving money

`Accounts.SendMoneyAsync`, `Accounts.RequestSendMoneyAsync`, `Accounts.TransferAsync` and `TransferRequests.CreateAsync` require an `IdempotencyKey`. Mercury carries out a request with a given key once, so the client retries these calls after a 5xx, a timeout or a dropped connection, sending the same body and key each time. It never makes up or changes a key. Use a fresh one for each payment you mean to make:

```csharp
using MercuryBanking.Models;

var transaction = await client.Accounts.SendMoneyAsync(accountId, new PostTransactionAPIRequest
{
    RecipientId = recipientId,
    Amount = 12.5,
    PaymentMethod = PostTransactionPaymentMethod.Ach,
    IdempotencyKey = Guid.NewGuid().ToString(),
});
Console.WriteLine($"{transaction.Id} {transaction.Status}");
```

Store the key with the payment, so that a retry of your own, after a crash, sends the same one.

## Webhooks

Mercury signs every webhook with the endpoint's secret, in the `Mercury-Signature` header. Mercury's sandbox sends no webhooks, so check your handler with your own test payloads. Pass the raw body, exactly as it arrived:

```csharp
app.MapPost("/mercury", async (HttpRequest request) =>
{
    using var buffer = new MemoryStream();
    await request.Body.CopyToAsync(buffer);
    try
    {
        MercuryWebhooks.Verify(buffer.ToArray(), request.Headers[MercuryWebhooks.SignatureHeader], secret);
    }
    catch (WebhookSignatureException error)
    {
        // error.Reason is MalformedHeader, TooOld or BadSignature.
        return Results.BadRequest();
    }
    return Results.Ok();
});
```

The signature is an HMAC-SHA256 of `<timestamp>.<raw body>`, compared in constant time. A timestamp more than 5 minutes old is rejected, so replays fail: pass `tolerance` to change that. A header may carry several signatures while you rotate a secret; any one that matches is enough. The exception never holds the secret or the body.

## Configuration

`new MercuryClient(token, options)` takes a `MercuryClientOptions`, whose every property is optional:

| Property | Default | Meaning |
| --- | --- | --- |
| `Environment` | `MercuryClient.Production` | `MercuryClient.Production` or `MercuryClient.Sandbox` |
| `Hosts` | None | Your own base URL for each of `api` and `vault`, for tests against a mock. Your token is sent to them |
| `UserAgent` | None | Sent as `User-Agent` when set |
| `Timeout` | 30 seconds | Time allowed for each attempt, including reading the whole response |
| `MaxRetries` | `3` | Retries after the first attempt |
| `RetryBaseDelay` | 0.5 seconds | Base of the exponential backoff |
| `RateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `MaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for. A longer one throws `RateLimitedException` at once |
| `Logger` | None | An `ILogger` for methods, URLs, statuses and retries |
| `HttpHandler` | None | An `HttpMessageHandler` to use instead of the network. The client does not dispose it |

To send through an `HttpClient` of your own, such as one from `IHttpClientFactory`, pass it as the third argument. The client uses it as it is: it neither changes nor disposes it, and its `Timeout` still applies. Its `DefaultRequestHeaders.ExpectContinue` must not be `true`, because that would let a failed write be resent. A plain `new HttpClient()` follows redirects, unlike the client's own handler; build it over `new SocketsHttpHandler { AllowAutoRedirect = false }` to keep your token on the hosts you chose. A handler that retries must skip writes.

A client is safe for concurrent use.

## Behaviour

* **Methods** are grouped by resource, such as `client.Accounts`, `client.Transactions`, `client.Recipients`, `client.Cards` and `client.Invoices`. All 87 operations in the API reference have a method. Every method is asynchronous and takes a `CancellationToken`.
* **Cancellation:** cancelling a call stops it, including any wait before a retry, and throws `OperationCanceledException`.
* **Hosts:** every operation goes to `api.mercury.com`, except `Cards.RevealAsync`, which goes to `vault-api.mercury.com`. In the sandbox both go to `api-sandbox.mercury.com`.
* **Pagination:** `List…Async` methods return one page and `ListAll…Async` methods return an `IAsyncEnumerable` over every item. Most send each page's `page.nextPage` back as `start_after`. `Accounts.ListAllTransactionsAsync` pages by `offset`, and `Treasury.ListAllTransactionsAsync` by its `cursor`. They start where your own `startAfter`, `offset` or `cursor` says, and page forward only.
* **Timeouts:** `Timeout` is the time allowed for each attempt. It throws `ApiTimeoutException`.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `RateLimitWait`. A `Retry-After` longer than `MaxRetryWait` throws `RateLimitedException` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET, and on the four money-moving writes when their `IdempotencyKey` is set, with exponential backoff. Other writes are not retried, because a repeat could act twice.
* **Redirects** are never followed by the client's own handler, so your token stays on the hosts you selected.
* **Errors** derive from `ApiException`. Error responses throw an `HttpException` subclass, such as `NotFoundException`, `PermissionDeniedException` or `ConflictException`, with `Kind`, `Status`, `RetryAfter` and `RawBody`, the body as text with your token removed. Mercury declares no error body, so the client does not parse one.
* **Logging** holds methods, URLs and statuses, never your token or response bodies, so card numbers from `Cards.RevealAsync` stay out of it.
* **Requests:** JSON bodies are a generated model, and a null property is not sent. IDs the spec declares as UUIDs are `Guid`.
* **Responses** are read tolerantly, because the spec has not been confirmed against the live API. Every property is nullable. A value that does not fit its property, and any field this version does not know, is kept in the model's `Extra` instead of failing the call. An empty 204 returns `null`.
* **Free-form and union values** are `object`, holding a `JsonElement`.
* **Files:** `Invoices.DownloadPdfAsync`, `Statements.DownloadPdfAsync` and `Safes.DownloadDocumentAsync` return a `Download`; dispose it. Uploads take `UploadFile(fileName, bytes)`.

## Limits

* The optional `Idempotency-Key` header on budget and receipt writes is not exposed yet, so those calls are sent without one and not retried.
* Iterators do not page backward with `endBefore`. Call `List…Async` with it instead.
* Some model names keep the spec's spelling, such as `ApiV1SpendBudgetResponse`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mercury's spec, which is fetched at build time and not included, and grants no right to the Mercury name.
