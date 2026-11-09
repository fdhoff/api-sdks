# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class CUR01Response200Currencies(ApiModel):
    """CUR01Response200Currencies model."""

    code: StrictStr
    label: StrictStr
    platform_default: Optional[StrictBool] = None
