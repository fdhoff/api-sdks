# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.subscription import Subscription
from ebay_sell._runtime import ApiModel


class SubscriptionResponse(ApiModel):
    """SubscriptionResponse model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    subscriptions: Optional[List[Subscription]] = None
    total: Optional[StrictInt] = None
