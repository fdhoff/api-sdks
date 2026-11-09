# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OR31Response200OrderUpdateErrorsErrors(ApiModel):
    """OR31Response200OrderUpdateErrorsErrors model."""

    code: StrictStr
    var_field: StrictStr = Field(alias="field")
    message: StrictStr
