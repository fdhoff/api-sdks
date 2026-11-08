from __future__ import annotations

import ast
import asyncio
import inspect
import re
from functools import partial
from pathlib import Path

import httpx
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

import ebay_sell

ROOT = Path(__file__).resolve().parents[5]
README = "apis/ebay/packages/python/README.md"
SNIPPETS = {
    f"{README}#{index}": snippet
    for index, snippet in enumerate(re.findall(r"```python\n(.*?)```", (ROOT / README).read_text(), re.DOTALL))
}
SECRETS = ("your-cert-id", "your-user-token", "your-refresh-token", "synthetic-new")
PRIVATE_KEY = "".join(
    ed25519.Ed25519PrivateKey.generate()
    .private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
    .decode()
    .splitlines()[1:-1]
)


def respond(request: httpx.Request) -> httpx.Response:
    path = request.url.path
    if path == "/identity/v1/oauth2/token":
        token = {
            "access_token": "v^1.1#synthetic-new-token",
            "expires_in": 7200,
            "token_type": "Application Access Token",
        }
        return httpx.Response(200, json=token)
    if path == "/commerce/taxonomy/v1/get_default_category_tree_id":
        return httpx.Response(200, json={"categoryTreeId": "0", "categoryTreeVersion": "1"})
    if path == "/sell/fulfillment/v1/order":
        return httpx.Response(200, json={"orders": [{"orderId": "01-00001-00001"}], "total": 1})
    if path == "/developer/key_management/v1/signing_key":
        key = {"signingKeyId": "synthetic-key-id", "privateKey": PRIVATE_KEY, "jwe": "synthetic.jwe"}
        return httpx.Response(200, json=key)
    if path == "/sell/finances/v1/seller_funds_summary":
        return httpx.Response(200, json={"totalFunds": {"currency": "GBP", "value": "1.00"}})
    errors = [{"errorId": 62004, "domain": "API_TAXONOMY", "message": "Synthetic missing category tree"}]
    return httpx.Response(404, json={"errors": errors})


def test_readme_has_snippets() -> None:
    assert len(SNIPPETS) >= 5


@pytest.mark.parametrize("key", SNIPPETS)
def test_snippet_runs(key: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return respond(request)

    transport = httpx.MockTransport(handler)
    for name in ("EbayClient", "AsyncEbayClient"):
        client = getattr(ebay_sell, name)
        monkeypatch.setattr(ebay_sell, name, partial(client, http_transport=transport))

    code = compile(SNIPPETS[key], key, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    result = eval(code, {})
    if inspect.iscoroutine(result):
        asyncio.run(result)

    assert requests
    output = capsys.readouterr().out
    assert not [secret for secret in SECRETS if secret in output]
    assert PRIVATE_KEY not in output
