# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class M10Response200Entities(ApiModel):
    """M10Response200Entities model."""

    id: StrictStr
    label: StrictStr
    type: StrictStr
