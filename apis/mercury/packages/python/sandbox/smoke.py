"""Read-only smoke test against Mercury's sandbox, which holds only dummy data. Run by the Mercury sandbox workflow.

Takes a read-only sandbox token from `MERCURY_SANDBOX_TOKEN`, makes GET calls only, and prints counts, never data.
"""

from __future__ import annotations

import os
import sys
from itertools import islice

from mercury_banking import MercuryClient

PAGES = 3


def main() -> None:
    token = os.environ.get("MERCURY_SANDBOX_TOKEN", "")
    if not token:
        sys.exit("MERCURY_SANDBOX_TOKEN is not set")
    with MercuryClient(token, environment="sandbox", user_agent="mercury-banking-sandbox-smoke") as client:
        client.organization.get()
        # A page size of 1 walks several pages, so each iterator follows the cursor.
        accounts = list(islice(client.accounts.iter(limit=1), PAGES))
        if not accounts:
            sys.exit("The sandbox returned no accounts")
        print(f"accounts: {len(accounts)}")
        account_id = accounts[0].id
        page = client.accounts.list_transactions(account_id, limit=PAGES)
        print(f"account transactions on the first page: {len(page.transactions or [])}")
        print(f"transactions: {len(list(islice(client.transactions.iter(limit=1), PAGES)))}")
        print(f"recipients: {len(list(islice(client.recipients.iter(limit=1), PAGES)))}")


if __name__ == "__main__":
    main()
