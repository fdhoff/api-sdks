# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_channel import (
    TL05Response200ExtFileStructureEntitiesChannel,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_debit import (
    TL05Response200ExtFileStructureEntitiesDebit,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_fee import (
    TL05Response200ExtFileStructureEntitiesFee,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_manual_accounting_document import (
    TL05Response200ExtFileStructureEntitiesManualAccountingDocument,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_one_off_item import (
    TL05Response200ExtFileStructureEntitiesOneOffItem,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_order import (
    TL05Response200ExtFileStructureEntitiesOrder,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_order_fee import (
    TL05Response200ExtFileStructureEntitiesOrderFee,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_order_line import (
    TL05Response200ExtFileStructureEntitiesOrderLine,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_order_tax import (
    TL05Response200ExtFileStructureEntitiesOrderTax,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_refund import (
    TL05Response200ExtFileStructureEntitiesRefund,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_shipment import (
    TL05Response200ExtFileStructureEntitiesShipment,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_shop_tax import (
    TL05Response200ExtFileStructureEntitiesShopTax,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_transaction_info import (
    TL05Response200ExtFileStructureEntitiesTransactionInfo,
)
from mirakl_seller._runtime import ApiModel


class TL05Response200ExtFileStructureEntities(ApiModel):
    """TL05Response200ExtFileStructureEntities model."""

    channel: Optional[TL05Response200ExtFileStructureEntitiesChannel] = None
    debit: Optional[TL05Response200ExtFileStructureEntitiesDebit] = None
    domain: Optional[StrictStr] = None
    fee: Optional[TL05Response200ExtFileStructureEntitiesFee] = None
    manual_accounting_document: Optional[TL05Response200ExtFileStructureEntitiesManualAccountingDocument] = None
    one_off_item: Optional[TL05Response200ExtFileStructureEntitiesOneOffItem] = None
    order: Optional[TL05Response200ExtFileStructureEntitiesOrder] = None
    order_fee: Optional[TL05Response200ExtFileStructureEntitiesOrderFee] = None
    order_line: Optional[TL05Response200ExtFileStructureEntitiesOrderLine] = None
    order_tax: Optional[TL05Response200ExtFileStructureEntitiesOrderTax] = None
    refund: Optional[TL05Response200ExtFileStructureEntitiesRefund] = None
    shipment: Optional[TL05Response200ExtFileStructureEntitiesShipment] = None
    shop_tax: Optional[TL05Response200ExtFileStructureEntitiesShopTax] = None
    transaction_info: Optional[TL05Response200ExtFileStructureEntitiesTransactionInfo] = None
