"""Smoke test of the published package, run by the published packages workflow against the mock, never the live API.

Installed from PyPI into a clean environment. Checks the version the package reports, then makes one call.
"""

from __future__ import annotations

import os
import sys

import mercury_banking
from mercury_banking import MercuryClient


def main() -> None:
    expected = os.environ["SMOKE_VERSION"]
    if mercury_banking.__version__ != expected:
        sys.exit(f"mercury_banking.__version__ is {mercury_banking.__version__}, not {expected}")
    mock = os.environ["SMOKE_BASE_URL"]
    with MercuryClient("secret-token:smoke-synthetic-token", hosts={"api": mock, "vault": mock}) as client:
        page = client.accounts.list()
    print(f"mercury-banking {expected}: listed {len(page.accounts)} accounts")


if __name__ == "__main__":
    main()
