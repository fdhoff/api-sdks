from __future__ import annotations

import ast
import asyncio
import inspect
import re
from functools import partial
from pathlib import Path

import httpx
import pytest

import mercury_banking

ROOT = Path(__file__).resolve().parents[5]
README = "apis/mercury/packages/python/README.md"
SNIPPETS = {
    f"{README}#{index}": snippet
    for index, snippet in enumerate(re.findall(r"```python\n(.*?)```", (ROOT / README).read_text(), re.DOTALL))
}
SECRETS = ("secret-token:your-token", "secret-token:your-sandbox-token")


def respond(request: httpx.Request) -> httpx.Response:
    path = request.url.path.removeprefix("/api/v1")
    account = {"id": "00000000-0000-4000-8000-acc000000001", "name": "Synthetic Checking", "availableBalance": 10.5}
    transaction = {"id": "00000000-0000-4000-8000-7a4000000001", "counterpartyName": "Synthetic Co", "amount": -2.5}
    if path == "/accounts":
        return httpx.Response(200, json={"accounts": [account], "page": {"nextPage": None}})
    if path == "/transactions":
        return httpx.Response(200, json={"transactions": [transaction], "page": {}})
    if path == "/recipients":
        return httpx.Response(200, json={"recipients": [{"name": "Synthetic Supplier"}], "page": {}})
    if path.endswith("/transactions") and request.method == "POST":
        return httpx.Response(200, json={**transaction, "status": "pending"})
    return httpx.Response(404, text="synthetic not found")


def test_readme_has_snippets() -> None:
    assert len(SNIPPETS) >= 5


@pytest.mark.parametrize("key", SNIPPETS)
def test_snippet_runs(key: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return respond(request)

    transport = httpx.MockTransport(handler)
    for name in ("MercuryClient", "AsyncMercuryClient"):
        client = getattr(mercury_banking, name)
        monkeypatch.setattr(mercury_banking, name, partial(client, http_transport=transport))

    code = compile(SNIPPETS[key], key, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    namespace: dict[str, object] = {}
    result = eval(code, namespace)
    if inspect.iscoroutine(result):
        asyncio.run(result)

    # The webhook snippet only defines a handler, so it is called here with a body it must reject.
    handle = namespace.get("handle")
    if callable(handle):
        assert handle(b"{}", {"Mercury-Signature": "t=1,v1=00"}, "synthetic-secret") == 400
    else:
        assert requests
    output = capsys.readouterr().out
    assert not [secret for secret in SECRETS if secret in output]
