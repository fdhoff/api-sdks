# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from mirakl_seller._runtime import ApiModel


class A02RequestShopAdditionalFields(ApiModel):
    """A02RequestShopAdditionalFields model."""

    code: StrictStr
    type: Optional[StrictStr] = None
