# etsy-seller

Unofficial Python client for the Etsy Open API v3. This project is unofficial and is not affiliated with, endorsed by, or supported by Etsy.

The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own Etsy app, approved by Etsy, and its keystring and shared secret. This package ships with no key, and an app's key may not be shared or transferred.
* Etsy's [API Terms of Use](https://www.etsy.com/legal/api) apply to everything you build with it. Among other things, Etsy content you show must be no more than 6 hours old, and the API may not be used for scraping or to train AI models.

## Install

The package is not on PyPI yet. From a clone of this repository:

```sh
pip install ./apis/etsy/packages/python
```

Requires Python 3.10 or later.

## Quickstart

```python
from etsy_seller import EtsyClient, NotFoundError

with EtsyClient("your-keystring", "your-shared-secret") as client:
    for listing in client.listings.iter_active(keywords="ceramic mug", limit=100):
        print(listing.listing_id, listing.title)

    try:
        client.shops.get(1)
    except NotFoundError as error:
        print(error.status, error.message)
```

Calls that read or change a shop's private data need an OAuth access token as well as your key:

```python
from etsy_seller import EtsyClient, Token


def save(token: Token) -> None:
    """Store both tokens: the old refresh token stops working."""


with EtsyClient(
    "your-keystring",
    "your-shared-secret",
    access_token="12345678.your-access-token",
    refresh_token="12345678.your-refresh-token",
    on_token=save,
) as client:
    me = client.users.get_me()
    for receipt in client.receipts.iter(me.shop_id, was_shipped=False):
        print(receipt.receipt_id)
```

An access token lasts an hour. When a call that needs one is refused with a 401, the client exchanges the refresh token for a new pair once, passes it to `on_token`, and retries the call. Concurrent calls share one refresh.

The async client has the same methods:

```python
from etsy_seller import AsyncEtsyClient

async with AsyncEtsyClient("your-keystring", "your-shared-secret") as client:
    async for listing in client.listings.iter_active(keywords="ceramic mug"):
        print(listing.listing_id)
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the server you selected.

## Getting a token

Etsy uses the OAuth 2 authorization code flow with PKCE. The client builds the authorization URL with a fresh `state` and code verifier, then trades the code Etsy sends back for a token:

```python
import secrets

from etsy_seller import EtsyClient

with EtsyClient("your-keystring", "your-shared-secret", on_token=print) as client:
    request = client.oauth.authorization_url("https://example.com/callback", ["listings_r", "shops_r"])
    # Send the user to request.url, and keep request.state and request.code_verifier until they return.

    returned_state, code = request.state, "code-from-the-redirect"  # read both from the redirect's query
    if not secrets.compare_digest(returned_state, request.state):
        raise RuntimeError("state mismatch")
    token = client.oauth.exchange_code(
        code, code_verifier=request.code_verifier, redirect_uri="https://example.com/callback"
    )
    print(token.user_id)
```

The redirect URI must be one registered for your app. After `exchange_code` the client uses the new token, and `client.oauth.refresh()` replaces it on demand. `authorization_url` and `Token` are also importable on their own.

## Configuration

`EtsyClient` and `AsyncEtsyClient` take the same arguments. `api_key` and `shared_secret` are positional and the rest are keywords.

| Argument | Default | Meaning |
| --- | --- | --- |
| `api_key` | Required | Your app's keystring |
| `shared_secret` | Required | Your app's shared secret. Sent with the keystring as `x-api-key` on every call |
| `access_token` | None | An OAuth access token, sent verbatim as a bearer token on calls that need one |
| `refresh_token` | None | Lets the client replace an expired access token itself |
| `on_token` | None | Called with every new `Token`, from `exchange_code` and every refresh |
| `user_agent` | None | Sent as `User-Agent` when given |
| `base_url` | `https://openapi.etsy.com` | A server root, for tests against a mock. Your credentials are sent to it |
| `timeout` | `30.0` | Seconds to wait on each attempt |
| `max_retries` | `3` | Retries after the first attempt |
| `retry_base_delay` | `0.5` | Base in seconds of the exponential backoff |
| `rate_limit_wait` | `10.0` | Seconds to wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | `60.0` | Longest `Retry-After` to wait for, in seconds. A longer one raises `RateLimitedError` at once |
| `http_transport` | None | An httpx transport to use instead of the network |

## Behaviour

* **Methods** are grouped by resource, such as `listings`, `listing_images`, `listing_inventory`, `receipts`, `transactions`, `shops`, `shipping_profiles` and `users`. Every one of the API's 107 operations has a method.
* **Credentials:** `x-api-key` goes on every call. The access token goes only on calls whose spec asks for OAuth, never on public reads.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them. Each page's `offset` advances by the number of results received, from the `offset` you pass, until an empty page or `count`.
* **Timeouts:** `timeout` is the time allowed for each attempt, including reading the whole response. The async client enforces it exactly. The sync client checks it as data arrives, so a stalled read can overrun by up to one timeout.
* **Retries:** 429 on every method, honouring `Retry-After` up to `max_retry_wait` seconds, otherwise after `rate_limit_wait` seconds. A longer `Retry-After`, such as at the daily limit, raises `RateLimitedError` at once, with the header in `retry_after`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create a listing twice.
* **Errors** derive from `ApiError`. Error responses raise an `HttpError` subclass with `status`, `message` (the body's `error` text) and `raw_body`, with every credential removed.
* **Logging** goes to the `etsy_seller` logger. It holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests** can be a generated model or a plain mapping. Models validate strictly, and send only the fields you set. Form bodies are method arguments, sent form-encoded. Method arguments are checked against their declared types and limits, such as `limit` up to 100, and raise pydantic's `ValidationError` before anything is sent.
* **Responses** are parsed tolerantly, because the spec has not been confirmed against the live API. A field that does not fit its declared type keeps its raw value instead of failing the call, a missing required field reads as `None`, and unknown fields are kept. A body that does not fit its declared type at all raises `DecodeError` with the body in `raw_body`.
* **Uploads** take `bytes` or `(filename, bytes)`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Etsy name.
