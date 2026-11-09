# ebay-sell

Unofficial Python client for eBay's Sell, Commerce and Developer REST APIs. This project is unofficial.

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

## Install

The package is not on PyPI yet. From a clone of this repository:

```sh
pip install "./apis/ebay/packages/python[signing]"
```

The `signing` extra adds `cryptography`, which only signing needs. Requires Python 3.10 or later.

## Quickstart

```python
from ebay_sell import EbayClient, NotFoundError

with EbayClient(client_id="your-app-id", client_secret="your-cert-id") as client:
    tree = client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    print(tree.category_tree_id)

    try:
        client.taxonomy.category_trees.get("0")
    except NotFoundError as error:
        print(error.status, error.code, error.message)
```

With a client ID and secret the client mints application tokens itself, from the client credentials grant, and mints a new one shortly before each expires. Operations that act for a seller need a user token instead:

```python
from ebay_sell import EbayClient, Token


def save(token: Token) -> None:
    """Store the new access token. The refresh token stays the same."""


with EbayClient(
    client_id="your-app-id",
    client_secret="your-cert-id",
    user_token="v^1.1#your-user-token",
    refresh_token="v^1.1#your-refresh-token",
    on_token=save,
    marketplace_id="EBAY_US",
) as client:
    for order in client.fulfillment.orders.iter(filter="orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}"):
        print(order.order_id)
```

A user token lasts two hours and its refresh token about 18 months. When a call is refused with a 401, the client refreshes the user token once, passes it to `on_token`, and retries the call. Concurrent calls share one refresh. If the refresh fails, the call raises the refresh's error, such as a `BadRequestError` for `invalid_grant`, not the 401. `on_token` runs while the client holds its token locks, so it must not call `client.oauth.refresh()` or make a call with the client: those wait for it forever. Store the token and return.

The async client has the same methods:

```python
from ebay_sell import AsyncEbayClient

async with AsyncEbayClient(client_id="your-app-id", client_secret="your-cert-id") as client:
    tree = await client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_GB")
    print(tree.category_tree_id)
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the environment you selected.

## Getting a user token

eBay uses the OAuth 2 authorization code grant, with your RuName as the redirect URI. The client builds the authorization URL with a fresh `state`, then trades the code eBay sends to your accept URL for a user token:

```python
import secrets

from ebay_sell import EbayClient

with EbayClient(
    client_id="your-app-id", client_secret="your-cert-id", ru_name="your-ru-name", on_token=print
) as client:
    request = client.oauth.authorization_url(["https://api.ebay.com/oauth/api_scope/sell.fulfillment"])
    # Send the user to request.url, and keep request.state until they return.

    returned_state, code = request.state, "code-from-the-redirect"  # read both from the redirect's query
    if not secrets.compare_digest(returned_state, request.state):
        raise RuntimeError("state mismatch")
    token = client.oauth.exchange_code(code)
    print(token.expires_in)
```

After `exchange_code` the client uses the new token, and `client.oauth.refresh()` replaces it on demand. `client.oauth.app_token()` mints an application token now. `authorization_url` and `Token` are also importable on their own.

## Signing

eBay requires sellers domiciled in the EU or UK to sign calls that move money or return financial data, such as those of the Finances API. Create a key pair once with the Key Management API, store its private key, which eBay returns only once, and pass both halves to the client as a `SigningKey`:

```python
from ebay_sell import EbayClient, SigningKey

with EbayClient(client_id="your-app-id", client_secret="your-cert-id") as client:
    created = client.key_management.signing_keys.create({"signingKeyCipher": "ED25519"})
    print(created.signing_key_id)  # store created.private_key and created.jwe somewhere safe

signing_key = SigningKey(private_key=created.private_key or "", jwe=created.jwe or "")
with EbayClient(user_token="v^1.1#your-user-token", signing_key=signing_key) as client:
    summary = client.finances.seller_funds.get_summary(x_ebay_c_marketplace_id="EBAY_GB")
    print(summary.total_funds)
```

Each request then carries `x-ebay-signature-key`, `Signature-Input`, `Signature` and, when it has a body, `Content-Digest`, as RFC 9421 describes. Ed25519 and RSA keys both work.

## Configuration

`EbayClient` and `AsyncEbayClient` take the same arguments, all keywords. Pass `client_id` and `client_secret`, a token, or both.

| Argument | Default | Meaning |
| --- | --- | --- |
| `client_id` | None | Your keyset's App ID |
| `client_secret` | None | Your keyset's Cert ID. Sent with the App ID only to the token endpoint |
| `ru_name` | None | Your RuName, for the authorization code grant |
| `app_token` | None | An application token to use instead of minting one |
| `user_token` | None | A user access token, sent on operations that act for a seller |
| `refresh_token` | None | Lets the client replace an expired user token itself |
| `on_token` | None | Called with every new user `Token`, from `exchange_code` and every refresh |
| `app_scopes` | `API_SCOPE` | The scopes of minted application tokens |
| `user_scopes` | None | The scopes to ask for on refresh. eBay keeps the original grant's when this is not given |
| `environment` | `production` | `production` or `sandbox`. Picks the API hosts and the authorization URL |
| `hosts` | None | Your own base URL for each of `api`, `apiz` and `apim`, for tests against a mock. Your credentials are sent to them |
| `marketplace_id` | None | Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call passes its own |
| `content_language` | None | Sent as `Content-Language` on operations that take it, unless a call passes its own |
| `signing_key` | None | A `SigningKey` that signs every request |
| `user_agent` | None | Sent as `User-Agent` when given |
| `timeout` | `30.0` | Seconds to wait on each attempt |
| `max_retries` | `3` | Retries after the first attempt |
| `retry_base_delay` | `0.5` | Base in seconds of the exponential backoff |
| `rate_limit_wait` | `10.0` | Seconds to wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | `60.0` | Longest `Retry-After` to wait for, in seconds. A longer one raises `RateLimitedError` at once |
| `http_transport` | None | An httpx transport to use instead of the network |

## Behaviour

* **Methods** are grouped by API and then by resource, such as `client.fulfillment.orders`, `client.inventory.inventory_items`, `client.account.fulfillment_policies` and `client.taxonomy.category_trees`. Each API is also a module, such as `ebay_sell.fulfillment`, with its models in `ebay_sell.fulfillment.models`. 310 of the 317 operations in the 20 contracts have a method; see Limits.
* **Tokens:** an operation that accepts an application token's scope gets the application token, and every other operation gets the user token. With no application token and no way to mint one, the user token is sent instead. Basic authentication with your App ID and Cert ID goes only to the token endpoint.
* **Hosts:** most operations go to `api.ebay.com`. Finances, Identity, Key Management and payment disputes go to `apiz.ebay.com`, and most of Media to `apim.ebay.com`. Each operation goes to its own host in the environment you chose.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them, following each page's `next` link.
* **Timeouts:** `timeout` is the time allowed for each attempt, including reading the whole response. The async client enforces it exactly. The sync client checks it as data arrives, so a stalled read can overrun by up to one timeout.
* **Retries:** 429 on every method, honouring `Retry-After` up to `max_retry_wait` seconds, otherwise after `rate_limit_wait` seconds. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create an offer twice. A 401 is retried once, after a new application token or a refreshed user token.
* **Errors** derive from `ApiError`. Error responses raise an `HttpError` subclass, such as `NotFoundError`, with `status`, `errors` (the body's `errors` list as `ErrorDetail`s), `code` and `message` (the first entry's `errorId` and `message`), `retry_after` and `raw_body`, with every credential removed.
* **Logging** goes to the `ebay_sell` logger. It holds methods, URLs and statuses, never your credentials or response bodies.
* **Requests** can be a generated model or a plain mapping. Models validate strictly, and send only the fields you set. Method arguments are checked against their declared types and raise pydantic's `ValidationError` before anything is sent. eBay declares many numbers as strings, such as `limit` and `offset`, so pass them as strings.
* **Responses** are parsed tolerantly, because the contracts have not been confirmed against the live API. A field that does not fit its declared type keeps its raw value instead of failing the call, a missing required field reads as `None`, and unknown fields are kept. An empty 204 returns `None`. A body that does not fit its declared type at all raises `DecodeError` with the body in `raw_body`.
* **Uploads** take `bytes` or `(filename, bytes)`.

## Limits

* Operations that send or return a raw file are not generated yet: video uploads and document downloads in Media, task input and result files in Feed, dispute evidence files in Fulfillment and report downloads in Marketing. They will follow.
* The Feedback API's list operations have no iterator. Page them with `offset` and `limit`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover eBay's contracts, which are fetched at build time and not included, and grants no right to the eBay name.
