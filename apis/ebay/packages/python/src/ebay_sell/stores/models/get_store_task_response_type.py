# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.stores.models.store_task_type import StoreTaskType
from ebay_sell._runtime import ApiModel


class GetStoreTaskResponseType(ApiModel):
    """GetStoreTaskResponseType model."""

    task: Optional[StoreTaskType] = None
