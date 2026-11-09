# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class SH21Response200Carriers(ApiModel):
    """SH21Response200Carriers model."""

    code: StrictStr
    label: StrictStr
    standard_code: Optional[StrictStr] = None
    tracking_url: Optional[StrictStr] = None
