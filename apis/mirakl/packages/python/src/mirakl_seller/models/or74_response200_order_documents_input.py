# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR74Response200OrderDocumentsInput(ApiModel):
    """OR74Response200OrderDocumentsInput model."""

    file_name: Optional[StrictStr] = None
    type_code: Optional[StrictStr] = None
