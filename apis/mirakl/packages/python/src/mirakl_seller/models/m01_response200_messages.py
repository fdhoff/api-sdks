# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.m01_response200_messages_documents import M01Response200MessagesDocuments
from mirakl_seller._runtime import ApiModel


class M01Response200Messages(ApiModel):
    """M01Response200Messages model."""

    archived: Optional[StrictBool] = None
    body: StrictStr
    commercial_id: StrictStr
    date_created: datetime
    documents: Optional[List[M01Response200MessagesDocuments]] = None
    from_id: StrictStr
    from_name: StrictStr
    from_type: StrictStr
    id: StrictInt
    offer_id: Optional[StrictInt] = None
    order_id: Optional[StrictStr] = None
    read: Optional[StrictBool] = None
    subject: StrictStr
    to_customer_archived: StrictBool
    to_customer_id: StrictStr
    to_customer_name: StrictStr
    to_operator: StrictBool
    to_operator_archived: StrictBool
    to_shop_archived: StrictBool
    to_shop_id: StrictInt
    to_shop_name: StrictStr
    visible: Optional[StrictBool] = None
