# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.sh52_response200_configuration import SH52Response200Configuration
from mirakl_seller._runtime import ApiModel


class SH52Response200(ApiModel):
    """SH52Response200 model."""

    configuration: List[SH52Response200Configuration]
    currency_iso_code: StrictStr
    last_updated_date: datetime
    shop_id: StrictInt
