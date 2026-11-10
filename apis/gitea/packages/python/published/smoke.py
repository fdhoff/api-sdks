"""Smoke test of the published package, run by the published packages workflow against the mock, never a real instance.

Installed from PyPI into a clean environment. Checks the version the package reports, then makes one call. The mock
serves the spec's paths without the `/api/v1` the client adds, so the transport removes it.
"""

from __future__ import annotations

import os
import sys

import httpx

import gitea_rest
from gitea_rest import GiteaClient


class Unprefixed(httpx.HTTPTransport):
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.url = request.url.copy_with(raw_path=request.url.raw_path.removeprefix(b"/api/v1"))
        return super().handle_request(request)


def main() -> None:
    expected = os.environ["SMOKE_VERSION"]
    if gitea_rest.__version__ != expected:
        sys.exit(f"gitea_rest.__version__ is {gitea_rest.__version__}, not {expected}")
    with GiteaClient(
        "smoke-synthetic-access-token", base_url=os.environ["SMOKE_BASE_URL"], http_transport=Unprefixed()
    ) as client:
        version = client.misc.get_version()
    print(f"gitea-rest {expected}: the mock reports version {version.version}")


if __name__ == "__main__":
    main()
