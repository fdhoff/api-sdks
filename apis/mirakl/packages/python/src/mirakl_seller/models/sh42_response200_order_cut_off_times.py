# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class SH42Response200OrderCutOffTimes(ApiModel):
    """SH42Response200OrderCutOffTimes model."""

    cut_off_time: StrictStr
    is_required: StrictBool
    set_by: StrictStr
    shipping_type_code: StrictStr
