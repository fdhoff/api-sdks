"""Read-only smoke test against eBay's sandbox. Run by the eBay sandbox workflow.

Mints an application token from `EBAY_SANDBOX_CLIENT_ID` and `EBAY_SANDBOX_CLIENT_SECRET` with the client
credentials grant, makes GET calls that accept it, and prints counts, never data. No user token, no writes.
"""

from __future__ import annotations

import os
import sys

from ebay_sell import EbayClient

MARKETPLACE = "EBAY_US"


def main() -> None:
    client_id = os.environ.get("EBAY_SANDBOX_CLIENT_ID", "")
    client_secret = os.environ.get("EBAY_SANDBOX_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        sys.exit("EBAY_SANDBOX_CLIENT_ID and EBAY_SANDBOX_CLIENT_SECRET must both be set")
    with EbayClient(
        client_id=client_id,
        client_secret=client_secret,
        environment="sandbox",
        user_agent="ebay-sell-sandbox-smoke",
    ) as client:
        token = client.oauth.app_token()
        print(f"application token expires in: {token.expires_in}s")
        tree_id = client.taxonomy.category_trees.get_default_id(marketplace_id=MARKETPLACE).category_tree_id
        if not tree_id:
            sys.exit(f"The sandbox returned no default category tree for {MARKETPLACE}")
        suggestions = client.taxonomy.category_trees.get_suggestions(tree_id, q="laptop").category_suggestions or []
        print(f"category suggestions: {len(suggestions)}")
        category_id = suggestions[0].category.category_id if suggestions and suggestions[0].category else None
        if not category_id:
            sys.exit("The sandbox returned no suggested category")
        aspects = client.taxonomy.category_trees.get_item_aspects(tree_id, category_id=category_id).aspects or []
        print(f"item aspects of the first suggestion: {len(aspects)}")
        currency = client.metadata.marketplaces.get_currencies(MARKETPLACE).default_currency
        print(f"default currency set: {currency is not None}")


if __name__ == "__main__":
    main()
