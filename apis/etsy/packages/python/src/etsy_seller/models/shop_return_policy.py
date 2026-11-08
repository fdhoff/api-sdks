# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ShopReturnPolicy(ApiModel):
    """ShopReturnPolicy model."""

    return_policy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    accepts_returns: Optional[StrictBool] = None
    accepts_exchanges: Optional[StrictBool] = None
    return_deadline: Optional[StrictInt] = None
