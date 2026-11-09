# mercury-banking

Unofficial Python client for the Mercury API. Not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc.

Mercury is a financial technology company, not a bank. Its banking services are provided through partner banks.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own API token, created in the Mercury dashboard. This package ships with no token. The `secret-token:` prefix is part of the token: pass it whole.
* A read-write token works only from IP addresses you allowlist on Mercury's side. A read-only token needs no allowlist.
* Mercury deletes tokens that go unused for 45 days, and downgrades tokens whose scope is broader than their use. Give each token only what it needs.
* The sandbox at `sandbox.mercury.com` holds dummy data and needs a token created there. A production token does not work in the sandbox, and a sandbox token does not work in production.
* OAuth2 is not supported yet. Mercury approves each OAuth2 integration individually.

## How this differs from Mercury's SDKs

Mercury publishes an official Go SDK, and none for Python. This package is generated from Mercury's published OpenAPI spec, as are its siblings in TypeScript, Go, C# and Rust in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, errors and redaction behave the same in each. It adds:

* sync and async clients with typed models;
* retries for the four money-moving writes, safe because each carries your `idempotencyKey`;
* iterators that walk every page;
* a verifier for the `Mercury-Signature` webhook header;
* your token kept out of every error and log line.

If you write Go, [this repository's Go module](https://github.com/fdhoff/api-sdks/tree/main/apis/mercury/packages/go) explains how it differs from Mercury's official SDK.

## Install

The package is not on PyPI yet. From a clone of this repository:

```sh
pip install ./apis/mercury/packages/python
```

Requires Python 3.10 or later.

## Quickstart

```python
from uuid import UUID

from mercury_banking import MercuryClient, NotFoundError

with MercuryClient("secret-token:your-token") as client:
    for account in client.accounts.iter():
        print(account.name, account.available_balance)

    for transaction in client.transactions.iter(limit=100, status=["sent"]):
        print(transaction.counterparty_name, transaction.amount)

    try:
        client.recipients.get(UUID("00000000-0000-4000-8000-000000000000"))
    except NotFoundError as error:
        print(error.status, error.raw_body)
```

Try it against the sandbox first, with a token created there:

```python
from mercury_banking import MercuryClient

with MercuryClient("secret-token:your-sandbox-token", environment="sandbox") as client:
    page = client.recipients.list(limit=10)
    print([recipient.name for recipient in page.recipients])
```

The async client has the same methods:

```python
from mercury_banking import AsyncMercuryClient

async with AsyncMercuryClient("secret-token:your-token") as client:
    async for account in client.accounts.iter():
        print(account.name)
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the environment you selected.

## Moving money

`accounts.send_money`, `accounts.request_send_money`, `accounts.transfer` and `transfer_requests.create` require an `idempotencyKey`. Mercury carries out a request with a given key once, so the client retries these calls after a 5xx, a timeout or a dropped connection, sending the same body and key each time. It never makes up or changes a key. Use a fresh one for each payment you mean to make:

```python
import uuid

from mercury_banking import MercuryClient

with MercuryClient("secret-token:your-token") as client:
    transaction = client.accounts.send_money(
        uuid.UUID("00000000-0000-4000-8000-000000000001"),  # your account's ID
        {
            "recipientId": "00000000-0000-4000-8000-000000000002",
            "amount": 12.5,
            "paymentMethod": "ach",
            "idempotencyKey": str(uuid.uuid4()),
        },
    )
    print(transaction.id, transaction.status)
```

Store the key with the payment, so that a retry of your own, after a crash, sends the same one.

## Webhooks

Mercury signs every webhook with the endpoint's secret, in the `Mercury-Signature` header. Mercury's sandbox sends no webhooks, so check your handler with your own test payloads. Pass the raw body, exactly as it arrived:

```python
from mercury_banking import SIGNATURE_HEADER, WebhookSignatureError, verify_webhook


def handle(body: bytes, headers: dict[str, str], secret: str) -> int:
    try:
        verify_webhook(body, headers.get(SIGNATURE_HEADER), secret)
    except WebhookSignatureError as error:
        print("rejected:", error.reason)  # malformed_header, too_old or bad_signature
        return 400
    return 200
```

The signature is an HMAC-SHA256 of `<timestamp>.<raw body>`, compared in constant time. A timestamp more than 5 minutes old is rejected, so replays fail: pass `tolerance` in seconds to change that. A header may carry several signatures while you rotate a secret; any one that matches is enough. The error never holds the secret or the body.

## Configuration

`MercuryClient` and `AsyncMercuryClient` take the token, then these keywords:

| Argument | Default | Meaning |
| --- | --- | --- |
| `environment` | `production` | `production` or `sandbox` |
| `hosts` | None | Your own base URL for each of `api` and `vault`, for tests against a mock. The token is sent to them |
| `user_agent` | None | Sent as `User-Agent` when given |
| `timeout` | `30.0` | Seconds to wait on each attempt |
| `max_retries` | `3` | Retries after the first attempt |
| `retry_base_delay` | `0.5` | Base in seconds of the exponential backoff |
| `rate_limit_wait` | `10.0` | Seconds to wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | `60.0` | Longest `Retry-After` to wait for, in seconds. A longer one raises `RateLimitedError` at once |
| `http_transport` | None | An httpx transport to use instead of the network |

## Behaviour

* **Methods** are grouped by resource, such as `client.accounts`, `client.transactions`, `client.recipients`, `client.cards` and `client.invoices`, with models in `mercury_banking.models`. All 87 operations in the API reference have a method.
* **Hosts:** every operation goes to `api.mercury.com`, except `cards.reveal`, which goes to `vault-api.mercury.com`. In the sandbox both go to `api-sandbox.mercury.com`.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them. Most send each page's `page.nextPage` back as `start_after`. `accounts.iter_transactions` pages by `offset`, and `treasury.iter_transactions` by its `cursor`. Iterators start where your own `start_after`, `offset` or `cursor` says, and page forward only.
* **Timeouts:** `timeout` is the time allowed for each attempt, including reading the whole response. The async client enforces it exactly. The sync client checks it as data arrives, so a stalled read can overrun by up to one timeout.
* **Retries:** 429 on every method, honouring `Retry-After` up to `max_retry_wait` seconds, otherwise after `rate_limit_wait` seconds. 5xx, timeouts and connection failures on GET, and on the four money-moving writes when their `idempotencyKey` is set, with exponential backoff. Other writes are not retried, because a repeat could act twice.
* **Errors** derive from `ApiError`. Error responses raise an `HttpError` subclass, such as `NotFoundError` or `PermissionDeniedError`, with `status`, `retry_after` and `raw_body`, the body as text with your token removed. Mercury declares no error body, so the client does not parse one.
* **Logging** goes to the `mercury_banking` logger. It holds methods, URLs and statuses, never your token or response bodies, so card numbers from `cards.reveal` stay out of it.
* **IDs** the spec declares as UUIDs are typed `uuid.UUID`, in arguments and in responses. A UUID string works too, but a type checker will flag it.
* **Requests** can be a generated model or a plain mapping. Models validate strictly, and send only the fields you set. Method arguments are checked against their declared types and raise pydantic's `ValidationError` before anything is sent.
* **Responses** are parsed tolerantly, because the spec has not been confirmed against the live API. A field that does not fit its declared type keeps its raw value instead of failing the call, a missing required field reads as `None`, and unknown fields are kept. An empty 204 returns `None`. A body that does not fit its declared type at all raises `DecodeError` with the body in `raw_body`.
* **Files:** `invoices.download_pdf`, `statements.download_pdf` and `safes.download_document` return a `Download`; read it in a `with` block. Uploads take `bytes` or `(filename, bytes)`.

## Limits

* The optional `Idempotency-Key` header on budget and receipt writes is not exposed yet, so those calls are sent without one and not retried.
* Iterators do not page backward with `end_before`. Call `list` with it instead.

## Testing

Every test runs against a mock built from the spec. The repository's Mercury sandbox workflow also makes read-only calls to Mercury's sandbox, which holds only dummy data, with a read-only sandbox token: `sandbox/smoke.py` lists accounts, transactions and recipients a page at a time. It never runs on pull requests, and never with a production token.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mercury's spec, which is fetched at build time and not included, and grants no right to the Mercury name.
