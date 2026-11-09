"""Smoke test of the published package, run by the published packages workflow against the mock, never the live API.

Installed from PyPI into a clean environment. Checks the version the package reports, then makes one call.
"""

from __future__ import annotations

import os
import sys

import etsy_seller
from etsy_seller import EtsyClient


def main() -> None:
    expected = os.environ["SMOKE_VERSION"]
    if etsy_seller.__version__ != expected:
        sys.exit(f"etsy_seller.__version__ is {etsy_seller.__version__}, not {expected}")
    with EtsyClient(
        "smoke-synthetic-keystring", "smoke-synthetic-shared-secret", base_url=os.environ["SMOKE_BASE_URL"]
    ) as client:
        pong = client.application.ping()
    if pong.application_id is None:
        sys.exit("The ping has no application_id")
    print(f"etsy-seller {expected}: pinged application {pong.application_id}")


if __name__ == "__main__":
    main()
