# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_channel import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesChannel,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_debit import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesDebit,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_fee import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFee,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_manual_accounting_document import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesManualAccountingDocument,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_one_off_item import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItem,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_order import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrder,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_order_fee import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderFee,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_order_line import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderLine,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_order_tax import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderTax,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_refund import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesRefund,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_shipment import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShipment,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_shop_tax import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShopTax,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_transaction_info import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesTransactionInfo,
)
from mirakl_seller._runtime import ApiModel


class TL05Response200ApplicationXNdjsonExtFileStructureEntities(ApiModel):
    """TL05Response200ApplicationXNdjsonExtFileStructureEntities model."""

    channel: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesChannel] = None
    debit: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesDebit] = None
    domain: Optional[StrictStr] = None
    fee: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFee] = None
    manual_accounting_document: Optional[
        TL05Response200ApplicationXNdjsonExtFileStructureEntitiesManualAccountingDocument
    ] = None
    one_off_item: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItem] = None
    order: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrder] = None
    order_fee: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderFee] = None
    order_line: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderLine] = None
    order_tax: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderTax] = None
    refund: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesRefund] = None
    shipment: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShipment] = None
    shop_tax: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShopTax] = None
    transaction_info: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesTransactionInfo] = None
