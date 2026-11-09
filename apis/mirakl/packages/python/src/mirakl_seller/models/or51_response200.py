# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or51_response200_assessments import OR51Response200Assessments
from mirakl_seller.models.or51_response200_reply import OR51Response200Reply
from mirakl_seller._runtime import ApiModel


class OR51Response200(ApiModel):
    """OR51Response200 model."""

    assessments: List[OR51Response200Assessments]
    comment: Optional[StrictStr] = None
    customer_id: StrictStr
    var_date: datetime = Field(alias="date")
    firstname: StrictStr
    grade: StrictInt
    last_updated_date: datetime
    lastname: StrictStr
    reply: Optional[OR51Response200Reply] = None
    visible: StrictBool
