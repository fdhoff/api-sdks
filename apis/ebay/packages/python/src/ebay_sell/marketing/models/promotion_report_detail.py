# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell._runtime import ApiModel


class PromotionReportDetail(ApiModel):
    """PromotionReportDetail model."""

    average_item_discount: Optional[Amount] = Field(default=None, alias="averageItemDiscount")
    average_item_revenue: Optional[Amount] = Field(default=None, alias="averageItemRevenue")
    average_order_discount: Optional[Amount] = Field(default=None, alias="averageOrderDiscount")
    average_order_revenue: Optional[Amount] = Field(default=None, alias="averageOrderRevenue")
    average_order_size: Optional[StrictStr] = Field(default=None, alias="averageOrderSize")
    base_sale: Optional[Amount] = Field(default=None, alias="baseSale")
    items_sold_quantity: Optional[StrictInt] = Field(default=None, alias="itemsSoldQuantity")
    number_of_orders_sold: Optional[StrictInt] = Field(default=None, alias="numberOfOrdersSold")
    percentage_sales_lift: Optional[StrictStr] = Field(default=None, alias="percentageSalesLift")
    promotion_href: Optional[StrictStr] = Field(default=None, alias="promotionHref")
    promotion_id: Optional[StrictStr] = Field(default=None, alias="promotionId")
    promotion_report_id: Optional[StrictStr] = Field(default=None, alias="promotionReportId")
    promotion_sale: Optional[Amount] = Field(default=None, alias="promotionSale")
    promotion_type: Optional[StrictStr] = Field(default=None, alias="promotionType")
    total_discount: Optional[Amount] = Field(default=None, alias="totalDiscount")
    total_sale: Optional[Amount] = Field(default=None, alias="totalSale")
