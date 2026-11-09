# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.st41_request_shipments import ST41RequestShipments
from mirakl_seller._runtime import ApiModel


class ST41Request(ApiModel):
    """ST41Request model."""

    shipments: Annotated[List[ST41RequestShipments], Field(min_length=0, max_length=200)]
