# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from mirakl_seller.models.pr03_request_trigger_selection import PR03RequestTriggerSelection
from mirakl_seller._runtime import ApiModel


class PR03RequestTrigger(ApiModel):
    """PR03RequestTrigger model."""

    selection: Optional[PR03RequestTriggerSelection] = None
    type: StrictStr
