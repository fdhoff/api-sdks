# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from backmarket_seller._runtime import ApiModel


class ListingsBatch(ApiModel):
    """ListingsBatch model."""

    bodymessage: StrictInt
    statuscode: StrictInt
