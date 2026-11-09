# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class STO02Response200(ApiModel):
    """STO02Response200 model."""

    date_created: datetime
    has_error_report: StrictBool
    import_id: StrictStr
    lines_in_error: Optional[StrictInt] = None
    lines_in_success: Optional[StrictInt] = None
    shop_id: StrictInt
    status: StrictStr
