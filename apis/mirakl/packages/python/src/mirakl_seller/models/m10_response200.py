# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.m10_response200_authorized_participants import M10Response200AuthorizedParticipants
from mirakl_seller.models.m10_response200_current_participants import M10Response200CurrentParticipants
from mirakl_seller.models.m10_response200_customer_organization import M10Response200CustomerOrganization
from mirakl_seller.models.m10_response200_entities import M10Response200Entities
from mirakl_seller.models.m10_response200_messages import M10Response200Messages
from mirakl_seller.models.m10_response200_metadata import M10Response200Metadata
from mirakl_seller.models.m10_response200_no_store_reply_needed import M10Response200NoStoreReplyNeeded
from mirakl_seller.models.m10_response200_topic import M10Response200Topic
from mirakl_seller._runtime import ApiModel


class M10Response200(ApiModel):
    """M10Response200 model."""

    authorized_participants: List[M10Response200AuthorizedParticipants]
    current_participants: List[M10Response200CurrentParticipants]
    customer_organization: Optional[M10Response200CustomerOrganization] = None
    date_created: datetime
    date_updated: datetime
    entities: Optional[List[M10Response200Entities]] = None
    id: StrictStr
    messages: List[M10Response200Messages]
    metadata: M10Response200Metadata
    no_store_reply_needed: Optional[List[M10Response200NoStoreReplyNeeded]] = None
    topic: M10Response200Topic
