# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersDeliveryDate(ApiModel):
    """OR15Response200ExtFileStructureOrdersDeliveryDate model."""

    earliest: datetime
    latest: datetime
