# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class RT25Response200ReturnErrors(ApiModel):
    """RT25Response200ReturnErrors model."""

    code: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
