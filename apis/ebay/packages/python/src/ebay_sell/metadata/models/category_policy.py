# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CategoryPolicy(ApiModel):
    """CategoryPolicy model."""

    auto_pay_enabled: Optional[StrictBool] = Field(default=None, alias="autoPayEnabled")
    b2b_vat_enabled: Optional[StrictBool] = Field(default=None, alias="b2bVatEnabled")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    ean_support: Optional[StrictStr] = Field(default=None, alias="eanSupport")
    expired: Optional[StrictBool] = None
    intangible_enabled: Optional[StrictBool] = Field(default=None, alias="intangibleEnabled")
    isbn_support: Optional[StrictStr] = Field(default=None, alias="isbnSupport")
    lsd: Optional[StrictBool] = None
    minimum_reserve_price: Optional[float] = Field(default=None, alias="minimumReservePrice")
    orpa: Optional[StrictBool] = None
    orra: Optional[StrictBool] = None
    payment_methods: Optional[List[StrictStr]] = Field(default=None, alias="paymentMethods")
    reduce_reserve_allowed: Optional[StrictBool] = Field(default=None, alias="reduceReserveAllowed")
    reserve_price_allowed: Optional[StrictBool] = Field(default=None, alias="reservePriceAllowed")
    upc_support: Optional[StrictStr] = Field(default=None, alias="upcSupport")
    value_category: Optional[StrictBool] = Field(default=None, alias="valueCategory")
    virtual: Optional[StrictBool] = None
