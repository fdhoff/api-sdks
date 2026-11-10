from __future__ import annotations

import ast
import asyncio
import inspect
import re
from functools import partial
from pathlib import Path

import httpx
import pytest

import gitea_rest

ROOT = Path(__file__).resolve().parents[5]
README = "apis/gitea/packages/python/README.md"
SNIPPETS = {
    f"{README}#{index}": snippet
    for index, snippet in enumerate(re.findall(r"```python\n(.*?)```", (ROOT / README).read_text(), re.DOTALL))
}
TOKEN = "your-access-token"
BASIC = "Basic eW91ci11c2VybmFtZTp5b3VyLXBhc3N3b3Jk"
BASE = "https://gitea.example.com/api/v1"


def respond(request: httpx.Request) -> httpx.Response:
    path = request.url.path.removeprefix("/api/v1")
    if path == "/user":
        return httpx.Response(200, json={"id": 1, "login": "synthetic-user"})
    if path == "/repos/your-org/your-repo/issues":
        return httpx.Response(200, json=[{"number": 1, "title": "Synthetic issue"}])
    if path == "/user/repos":
        return httpx.Response(200, json=[{"id": 1, "full_name": "synthetic-user/synthetic-repo"}])
    if path == "/users/your-username/tokens":
        return httpx.Response(201, json={"id": 1, "name": "scripts", "sha1": "synthetic-new-token"})
    return httpx.Response(404, json={"message": "synthetic not found"})


def test_readme_has_snippets() -> None:
    assert len(SNIPPETS) >= 3


@pytest.mark.parametrize("key", SNIPPETS)
def test_snippet_runs(key: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert str(request.url).startswith(BASE)
        assert request.headers["authorization"] in (f"token {TOKEN}", BASIC)
        return respond(request)

    transport = httpx.MockTransport(handler)
    for name in ("GiteaClient", "AsyncGiteaClient"):
        client = getattr(gitea_rest, name)
        monkeypatch.setattr(gitea_rest, name, partial(client, http_transport=transport))

    code = compile(SNIPPETS[key], key, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    result = eval(code, {})
    if inspect.iscoroutine(result):
        asyncio.run(result)

    assert requests
    out = capsys.readouterr().out
    assert TOKEN not in out
    assert "your-password" not in out
