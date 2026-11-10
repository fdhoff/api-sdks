"""Live driver: the conformance driver, with each request sent to the instance unchanged, `/api/v1` included.

Run by `apis/gitea/conformance/live/run.mjs` against a disposable Gitea container. See `apis/gitea/docs/live.md`.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import httpx

CONFORMANCE = Path(__file__).resolve().parent.parent / "conformance" / "driver.py"


def main() -> None:
    spec = importlib.util.spec_from_file_location("gitea_conformance_driver", CONFORMANCE)
    assert spec is not None and spec.loader is not None
    driver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)
    driver.main((httpx.HTTPTransport, httpx.AsyncHTTPTransport))


if __name__ == "__main__":
    main()
