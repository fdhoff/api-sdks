# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.m11_response200_data_authorized_participants import M11Response200DataAuthorizedParticipants
from mirakl_seller.models.m11_response200_data_current_participants import M11Response200DataCurrentParticipants
from mirakl_seller.models.m11_response200_data_customer_organization import M11Response200DataCustomerOrganization
from mirakl_seller.models.m11_response200_data_entities import M11Response200DataEntities
from mirakl_seller.models.m11_response200_data_messages import M11Response200DataMessages
from mirakl_seller.models.m11_response200_data_metadata import M11Response200DataMetadata
from mirakl_seller.models.m11_response200_data_no_store_reply_needed import M11Response200DataNoStoreReplyNeeded
from mirakl_seller.models.m11_response200_data_topic import M11Response200DataTopic
from mirakl_seller._runtime import ApiModel


class M11Response200Data(ApiModel):
    """M11Response200Data model."""

    authorized_participants: List[M11Response200DataAuthorizedParticipants]
    current_participants: List[M11Response200DataCurrentParticipants]
    customer_organization: Optional[M11Response200DataCustomerOrganization] = None
    date_created: datetime
    date_updated: datetime
    entities: Optional[List[M11Response200DataEntities]] = None
    id: StrictStr
    messages: Optional[List[M11Response200DataMessages]] = None
    metadata: M11Response200DataMetadata
    no_store_reply_needed: Optional[List[M11Response200DataNoStoreReplyNeeded]] = None
    topic: M11Response200DataTopic
