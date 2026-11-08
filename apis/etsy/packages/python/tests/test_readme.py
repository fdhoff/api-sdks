from __future__ import annotations

import ast
import asyncio
import inspect
import re
from functools import partial
from pathlib import Path

import httpx
import pytest

import etsy_seller

ROOT = Path(__file__).resolve().parents[5]
README = "apis/etsy/packages/python/README.md"
SNIPPETS = {
    f"{README}#{index}": snippet
    for index, snippet in enumerate(re.findall(r"```python\n(.*?)```", (ROOT / README).read_text(), re.DOTALL))
}
SECRETS = ("your-keystring", "your-shared-secret", "your-access-token", "your-refresh-token", "synthetic-new")


def respond(request: httpx.Request) -> httpx.Response:
    path = request.url.path
    if path == "/v3/public/oauth/token":
        tokens = {"access_token": "12345678.synthetic-new-access", "refresh_token": "12345678.synthetic-new-refresh"}
        return httpx.Response(200, json={**tokens, "expires_in": 3600, "token_type": "Bearer"})
    if path == "/v3/application/users/me":
        return httpx.Response(200, json={"user_id": 12345678, "shop_id": 1})
    if path in ("/v3/application/listings/active", "/v3/application/shops/1/receipts"):
        return httpx.Response(200, json={"count": 1, "results": [{"listing_id": 1, "receipt_id": 1, "title": "Mug"}]})
    return httpx.Response(404, json={"error": "Synthetic missing shop"})


def test_readme_has_snippets() -> None:
    assert len(SNIPPETS) >= 4


@pytest.mark.parametrize("key", SNIPPETS)
def test_snippet_runs(key: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return respond(request)

    transport = httpx.MockTransport(handler)
    for name in ("EtsyClient", "AsyncEtsyClient"):
        client = getattr(etsy_seller, name)
        monkeypatch.setattr(etsy_seller, name, partial(client, http_transport=transport))

    code = compile(SNIPPETS[key], key, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    result = eval(code, {})
    if inspect.iscoroutine(result):
        asyncio.run(result)

    assert requests
    output = capsys.readouterr().out
    assert not [secret for secret in SECRETS if secret in output]
