# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class M10Response200NoStoreReplyNeeded(ApiModel):
    """M10Response200NoStoreReplyNeeded model."""

    var_date: datetime = Field(alias="date")
    user_type: StrictStr
