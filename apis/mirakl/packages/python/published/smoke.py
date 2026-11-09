"""Smoke test of the published package, run by the published packages workflow against the mock, never the live API.

Installed from PyPI into a clean environment. Checks the version the package reports, then makes one call.
"""

from __future__ import annotations

import os
import sys

import mirakl_seller
from mirakl_seller import MiraklClient


def main() -> None:
    expected = os.environ["SMOKE_VERSION"]
    if mirakl_seller.__version__ != expected:
        sys.exit(f"mirakl_seller.__version__ is {mirakl_seller.__version__}, not {expected}")
    with MiraklClient("smoke-synthetic-shop-key", base_url=os.environ["SMOKE_BASE_URL"]) as client:
        page = client.orders.list(max=1)
    print(f"mirakl-seller {expected}: listed {len(page.orders)} orders")


if __name__ == "__main__":
    main()
