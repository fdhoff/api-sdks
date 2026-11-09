# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pr03_request_trigger import PR03RequestTrigger
from mirakl_seller.models.pr03_request_trigger_selection import PR03RequestTriggerSelection
from mirakl_seller._runtime import ApiModel


class PR03RequestTriggerEveryQuantity(PR03RequestTrigger):
    """PR03RequestTriggerEveryQuantity model."""

    quantity_purchased: StrictInt
    same_item_purchased: Optional[StrictBool] = None
