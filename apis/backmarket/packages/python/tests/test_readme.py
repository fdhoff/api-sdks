from __future__ import annotations

import ast
import asyncio
import inspect
import re
from functools import partial
from pathlib import Path

import httpx
import pytest

import backmarket_seller

ROOT = Path(__file__).resolve().parents[5]
READMES = ("README.md", "apis/backmarket/packages/python/README.md")
SNIPPETS = {
    f"{name}#{index}": snippet
    for name in READMES
    for index, snippet in enumerate(re.findall(r"```python\n(.*?)```", (ROOT / name).read_text(), re.DOTALL))
}


def test_readmes_have_snippets() -> None:
    assert {key.split("#")[0] for key in SNIPPETS} == set(READMES)


@pytest.mark.parametrize("key", SNIPPETS)
def test_snippet_runs(key: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if "/orders" in request.url.path:
            return httpx.Response(200, json={"count": 1, "next": None, "previous": None, "results": [{"order_id": 1}]})
        return httpx.Response(404, json={"requestId": "synthetic-request"})

    transport = httpx.MockTransport(respond)
    for name in ("BackMarketClient", "AsyncBackMarketClient"):
        client = getattr(backmarket_seller, name)
        monkeypatch.setattr(backmarket_seller, name, partial(client, http_transport=transport))

    code = compile(SNIPPETS[key], key, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    result = eval(code, {})
    if inspect.iscoroutine(result):
        asyncio.run(result)

    assert requests
    assert "your-token" not in capsys.readouterr().out
