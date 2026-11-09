"""Smoke test of the published package, run by the published packages workflow against the mock, never the live API.

Installed from PyPI into a clean environment. Checks the version the package reports, then makes one call.
"""

from __future__ import annotations

import os
import sys

import backmarket_seller
from backmarket_seller import BackMarketClient


def main() -> None:
    expected = os.environ["SMOKE_VERSION"]
    if backmarket_seller.__version__ != expected:
        sys.exit(f"backmarket_seller.__version__ is {backmarket_seller.__version__}, not {expected}")
    with BackMarketClient(
        "smoke-synthetic-token",
        user_agent="BM-Example-Smoke;smoke@example.com",
        locale="en-us",
        base_url=os.environ["SMOKE_BASE_URL"],
    ) as client:
        order = client.orders.get(1)
    if order.order_id is None:
        sys.exit("The order has no order_id")
    print(f"backmarket-seller {expected}: got order {order.order_id}")


if __name__ == "__main__":
    main()
