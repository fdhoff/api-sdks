# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OR33RequestOrderLines(ApiModel):
    """OR33RequestOrderLines model."""

    id: StrictStr
    reason_code: StrictStr
