# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.st24_request_shipments import ST24RequestShipments
from mirakl_seller._runtime import ApiModel


class ST24Request(ApiModel):
    """ST24Request model."""

    shipments: Annotated[List[ST24RequestShipments], Field(min_length=1, max_length=1000)]
