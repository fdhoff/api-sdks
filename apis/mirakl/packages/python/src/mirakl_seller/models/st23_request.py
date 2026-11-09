# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.st23_request_shipments import ST23RequestShipments
from mirakl_seller._runtime import ApiModel


class ST23Request(ApiModel):
    """ST23Request model."""

    shipments: Annotated[List[ST23RequestShipments], Field(min_length=1, max_length=1000)]
