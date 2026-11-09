# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pr03_request_trigger_selection import PR03RequestTriggerSelection
from mirakl_seller._runtime import ApiModel


class PR03RequestTriggerSelectionBrand(PR03RequestTriggerSelection):
    """PR03RequestTriggerSelectionBrand model."""

    values: List[StrictStr]
