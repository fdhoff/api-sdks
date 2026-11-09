# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OR32Response200OrderLinesAdjustedErrors(ApiModel):
    """OR32Response200OrderLinesAdjustedErrors model."""

    code: StrictStr
    var_field: StrictStr = Field(alias="field")
    message: StrictStr
