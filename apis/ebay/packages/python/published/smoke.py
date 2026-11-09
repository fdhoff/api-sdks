"""Smoke test of the published package, run by the published packages workflow against the mock, never the live API.

Installed from PyPI into a clean environment. Checks the version the package reports, then makes one call.
"""

from __future__ import annotations

import os
import sys

import ebay_sell
from ebay_sell import EbayClient


def main() -> None:
    expected = os.environ["SMOKE_VERSION"]
    if ebay_sell.__version__ != expected:
        sys.exit(f"ebay_sell.__version__ is {ebay_sell.__version__}, not {expected}")
    mock = os.environ["SMOKE_BASE_URL"]
    with EbayClient(
        app_token="smoke-synthetic-app-token",
        hosts={"api": mock, "apiz": mock, "apim": mock},
        marketplace_id="EBAY_US",
    ) as client:
        tree = client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    if tree.category_tree_id is None:
        sys.exit("The category tree has no category_tree_id")
    print(f"ebay-sell {expected}: got category tree {tree.category_tree_id}")


if __name__ == "__main__":
    main()
