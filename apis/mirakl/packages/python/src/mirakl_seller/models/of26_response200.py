# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OF26Response200(ApiModel):
    """OF26Response200 model."""

    offer_id: StrictInt
    quantity: StrictInt
