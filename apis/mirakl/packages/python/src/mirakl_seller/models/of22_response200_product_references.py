# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OF22Response200ProductReferences(ApiModel):
    """OF22Response200ProductReferences model."""

    reference: StrictStr
    reference_type: StrictStr
