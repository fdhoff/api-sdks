# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.st07_request_shipments import ST07RequestShipments
from mirakl_seller._runtime import ApiModel


class ST07Request(ApiModel):
    """ST07Request model."""

    shipments: Annotated[List[ST07RequestShipments], Field(min_length=1, max_length=100)]
