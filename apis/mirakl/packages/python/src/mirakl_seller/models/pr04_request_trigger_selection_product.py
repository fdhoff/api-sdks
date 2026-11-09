# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pr04_request_trigger_selection import PR04RequestTriggerSelection
from mirakl_seller.models.pr04_request_trigger_selection_product_values import PR04RequestTriggerSelectionProductValues
from mirakl_seller._runtime import ApiModel


class PR04RequestTriggerSelectionProduct(PR04RequestTriggerSelection):
    """PR04RequestTriggerSelectionProduct model."""

    values: List[PR04RequestTriggerSelectionProductValues]
