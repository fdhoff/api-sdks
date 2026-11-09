from __future__ import annotations

import ast
import asyncio
import inspect
import re
from functools import partial
from pathlib import Path

import httpx
import pytest

import mirakl_seller

ROOT = Path(__file__).resolve().parents[5]
README = "apis/mirakl/packages/python/README.md"
SNIPPETS = {
    f"{README}#{index}": snippet
    for index, snippet in enumerate(re.findall(r"```python\n(.*?)```", (ROOT / README).read_text(), re.DOTALL))
}
KEY = "your-shop-api-key"
BASE = "https://marketplace.example.com"


def respond(request: httpx.Request) -> httpx.Response:
    path = request.url.path
    if path == "/api/orders":
        order = {"order_id": "order-1", "order_state": "SHIPPING", "total_price": 10.5}
        return httpx.Response(200, json={"orders": [order], "total_count": 1})
    if path == "/api/offers":
        return httpx.Response(200, json={"offers": [{"shop_sku": "sku-1", "quantity": 5}], "total_count": 1})
    if path == "/api/account":
        return httpx.Response(
            200, json={"shop_id": int(request.url.params.get("shop_id", 2001)), "shop_name": "Synthetic"}
        )
    if path == "/api/offers/stock/imports":
        return httpx.Response(201, json={"import_id": "stock-import-1"})
    if path == "/api/offers/stock/imports/stock-import-1/status":
        status = {"import_id": "stock-import-1", "status": "COMPLETE", "has_error_report": True, "lines_in_success": 1}
        return httpx.Response(200, json=status)
    if path == "/api/offers/stock/imports/stock-import-1/error_report":
        return httpx.Response(200, headers={"content-type": "text/csv"}, content=b"offer-sku;error\n")
    if path == "/api/orders/async-export":
        return httpx.Response(200, json={"tracking_id": "tracking-1"})
    if path == "/api/orders/async-export/status/tracking-1":
        urls = [f"{BASE}/exports/orders-1.json"]
        return httpx.Response(200, json={"status": "COMPLETED", "last_updated": "2026-01-01T00:00:00Z", "urls": urls})
    if path == "/exports/orders-1.json":
        return httpx.Response(200, headers={"content-type": "application/json"}, content=b"[]")
    return httpx.Response(404, text="synthetic not found")


def test_readme_has_snippets() -> None:
    assert len(SNIPPETS) >= 5


@pytest.mark.parametrize("key", SNIPPETS)
def test_snippet_runs(key: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert str(request.url).startswith(BASE)
        assert request.headers["authorization"] == KEY
        return respond(request)

    transport = httpx.MockTransport(handler)
    for name in ("MiraklClient", "AsyncMiraklClient"):
        client = getattr(mirakl_seller, name)
        monkeypatch.setattr(mirakl_seller, name, partial(client, http_transport=transport))

    code = compile(SNIPPETS[key], key, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    result = eval(code, {})
    if inspect.iscoroutine(result):
        asyncio.run(result)

    assert requests
    assert KEY not in capsys.readouterr().out
