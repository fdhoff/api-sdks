# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OF02Response200(ApiModel):
    """OF02Response200 model."""

    date_created: datetime
    has_error_report: StrictBool
    import_id: StrictInt
    lines_in_error: StrictInt
    lines_in_pending: StrictInt
    lines_in_success: StrictInt
    lines_read: StrictInt
    mode: StrictStr
    offer_deleted: StrictInt
    offer_inserted: StrictInt
    offer_updated: StrictInt
    reason_status: StrictStr
    status: StrictStr
    type: StrictStr
