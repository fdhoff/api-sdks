# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class RE01Response200Reasons(ApiModel):
    """RE01Response200Reasons model."""

    code: StrictStr
    is_shop_right: StrictBool
    label: StrictStr
    type: StrictStr
