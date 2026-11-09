# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PRI02Response200Data(ApiModel):
    """PRI02Response200Data model."""

    date_created: datetime
    has_error_report: StrictBool
    import_id: StrictStr
    lines_in_error: StrictInt
    lines_in_success: StrictInt
    offers_in_error: StrictInt
    offers_updated: StrictInt
    origin: StrictStr
    reason_status: StrictStr
    shop_id: StrictInt
    status: StrictStr
