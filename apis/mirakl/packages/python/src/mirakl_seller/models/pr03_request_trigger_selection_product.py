# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pr03_request_trigger_selection import PR03RequestTriggerSelection
from mirakl_seller.models.pr03_request_trigger_selection_product_values import PR03RequestTriggerSelectionProductValues
from mirakl_seller._runtime import ApiModel


class PR03RequestTriggerSelectionProduct(PR03RequestTriggerSelection):
    """PR03RequestTriggerSelectionProduct model."""

    values: List[PR03RequestTriggerSelectionProductValues]
