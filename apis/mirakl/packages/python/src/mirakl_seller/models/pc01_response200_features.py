# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pc01_response200_features_catalog import PC01Response200FeaturesCatalog
from mirakl_seller.models.pc01_response200_features_direct_payment_customer_store import (
    PC01Response200FeaturesDirectPaymentCustomerStore,
)
from mirakl_seller.models.pc01_response200_features_dropship import PC01Response200FeaturesDropship
from mirakl_seller.models.pc01_response200_features_order_conditions import PC01Response200FeaturesOrderConditions
from mirakl_seller.models.pc01_response200_features_order_workflows import PC01Response200FeaturesOrderWorkflows
from mirakl_seller.models.pc01_response200_features_pricing import PC01Response200FeaturesPricing
from mirakl_seller.models.pc01_response200_features_promotion import PC01Response200FeaturesPromotion
from mirakl_seller.models.pc01_response200_features_returns import PC01Response200FeaturesReturns
from mirakl_seller.models.pc01_response200_features_shipment import PC01Response200FeaturesShipment
from mirakl_seller.models.pc01_response200_features_shop_tax_options import PC01Response200FeaturesShopTaxOptions
from mirakl_seller.models.pc01_response200_features_tax_collection import PC01Response200FeaturesTaxCollection
from mirakl_seller.models.pc01_response200_features_tax_id_number import PC01Response200FeaturesTaxIdNumber
from mirakl_seller.models.pc01_response200_features_warehouses import PC01Response200FeaturesWarehouses
from mirakl_seller._runtime import ApiModel


class PC01Response200Features(ApiModel):
    """PC01Response200Features model."""

    catalog: PC01Response200FeaturesCatalog
    circular_economy_data_collection: StrictBool
    competitive_pricing_tool: StrictBool
    direct_payment_customer_store: PC01Response200FeaturesDirectPaymentCustomerStore
    disable_seller_alternative_carrier: StrictBool
    dropship: PC01Response200FeaturesDropship
    kyc_status_per_seller: StrictBool
    lead_time_to_ship_by_sellers_enabled: StrictStr
    multi_currency: StrictBool
    multi_payout_psp_per_seller: StrictBool
    no_reply_needed: StrictBool
    offer_prices_decimals: StrictStr
    operator_csv_delimiter: StrictStr
    order_conditions: PC01Response200FeaturesOrderConditions
    order_tax_mode: StrictStr
    order_workflows: PC01Response200FeaturesOrderWorkflows
    payment_confirmation: StrictBool
    pricing: PC01Response200FeaturesPricing
    product_data_validation_by_channel: StrictBool
    promotion: PC01Response200FeaturesPromotion
    returns: PC01Response200FeaturesReturns
    shipment: PC01Response200FeaturesShipment
    shop_tax_options: PC01Response200FeaturesShopTaxOptions
    tax_collection: PC01Response200FeaturesTaxCollection
    tax_id_number: PC01Response200FeaturesTaxIdNumber
    warehouses: PC01Response200FeaturesWarehouses
