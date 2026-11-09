# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.st31_request_shipments import ST31RequestShipments
from mirakl_seller._runtime import ApiModel


class ST31Request(ApiModel):
    """ST31Request model."""

    shipments: Annotated[List[ST31RequestShipments], Field(min_length=1, max_length=100)]
