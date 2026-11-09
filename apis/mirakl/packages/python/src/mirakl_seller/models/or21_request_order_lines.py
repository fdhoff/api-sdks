# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OR21RequestOrderLines(ApiModel):
    """OR21RequestOrderLines model."""

    accepted: StrictBool
    id: StrictStr
