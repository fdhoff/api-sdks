# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl02_response200_data_entities_channel import TL02Response200DataEntitiesChannel
from mirakl_seller.models.tl02_response200_data_entities_debit import TL02Response200DataEntitiesDebit
from mirakl_seller.models.tl02_response200_data_entities_fee import TL02Response200DataEntitiesFee
from mirakl_seller.models.tl02_response200_data_entities_manual_accounting_document import (
    TL02Response200DataEntitiesManualAccountingDocument,
)
from mirakl_seller.models.tl02_response200_data_entities_one_off_item import TL02Response200DataEntitiesOneOffItem
from mirakl_seller.models.tl02_response200_data_entities_order import TL02Response200DataEntitiesOrder
from mirakl_seller.models.tl02_response200_data_entities_order_fee import TL02Response200DataEntitiesOrderFee
from mirakl_seller.models.tl02_response200_data_entities_order_line import TL02Response200DataEntitiesOrderLine
from mirakl_seller.models.tl02_response200_data_entities_order_tax import TL02Response200DataEntitiesOrderTax
from mirakl_seller.models.tl02_response200_data_entities_refund import TL02Response200DataEntitiesRefund
from mirakl_seller.models.tl02_response200_data_entities_shipment import TL02Response200DataEntitiesShipment
from mirakl_seller.models.tl02_response200_data_entities_shop_tax import TL02Response200DataEntitiesShopTax
from mirakl_seller.models.tl02_response200_data_entities_transaction_info import (
    TL02Response200DataEntitiesTransactionInfo,
)
from mirakl_seller._runtime import ApiModel


class TL02Response200DataEntities(ApiModel):
    """TL02Response200DataEntities model."""

    channel: Optional[TL02Response200DataEntitiesChannel] = None
    debit: Optional[TL02Response200DataEntitiesDebit] = None
    domain: Optional[StrictStr] = None
    fee: Optional[TL02Response200DataEntitiesFee] = None
    manual_accounting_document: Optional[TL02Response200DataEntitiesManualAccountingDocument] = None
    one_off_item: Optional[TL02Response200DataEntitiesOneOffItem] = None
    order: Optional[TL02Response200DataEntitiesOrder] = None
    order_fee: Optional[TL02Response200DataEntitiesOrderFee] = None
    order_line: Optional[TL02Response200DataEntitiesOrderLine] = None
    order_tax: Optional[TL02Response200DataEntitiesOrderTax] = None
    refund: Optional[TL02Response200DataEntitiesRefund] = None
    shipment: Optional[TL02Response200DataEntitiesShipment] = None
    shop_tax: Optional[TL02Response200DataEntitiesShopTax] = None
    transaction_info: Optional[TL02Response200DataEntitiesTransactionInfo] = None
