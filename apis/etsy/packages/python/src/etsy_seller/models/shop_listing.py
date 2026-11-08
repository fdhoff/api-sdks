# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller._runtime import ApiModel


class ShopListing(ApiModel):
    """ShopListing model."""

    listing_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    creation_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    ending_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    original_creation_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    last_modified_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    updated_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    state_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    quantity: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    shop_section_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    featured_rank: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    num_favorers: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    non_taxable: Optional[StrictBool] = None
    is_taxable: Optional[StrictBool] = None
    is_customizable: Optional[StrictBool] = None
    is_personalizable: Optional[StrictBool] = None
    listing_type: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    materials: Optional[List[StrictStr]] = None
    shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    return_policy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    processing_min: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    processing_max: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    who_made: Optional[StrictStr] = None
    when_made: Optional[StrictStr] = None
    is_supply: Optional[StrictBool] = None
    item_weight: Optional[float] = None
    item_weight_unit: Optional[StrictStr] = None
    item_length: Optional[float] = None
    item_width: Optional[float] = None
    item_height: Optional[float] = None
    item_dimensions_unit: Optional[StrictStr] = None
    is_private: Optional[StrictBool] = None
    style: Optional[List[StrictStr]] = None
    file_data: Optional[StrictStr] = None
    has_variations: Optional[StrictBool] = None
    should_auto_renew: Optional[StrictBool] = None
    language: Optional[StrictStr] = None
    price: Optional[Money] = None
    converted_price: Optional[Money] = None
    taxonomy_id: Optional[StrictInt] = None
    readiness_state_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    suggested_title: Optional[StrictStr] = None
    ecgt_garan_brand: Optional[StrictStr] = None
    ecgt_garan_years: Optional[StrictInt] = None
    ecgt_garan_model: Optional[StrictStr] = None
    ecgt_garan_guarantee_details: Optional[StrictStr] = None
    ecgt_other_commercial_guarantee_details: Optional[StrictStr] = None
    ecgt_after_sales_service_info: Optional[StrictStr] = None
    ecgt_software_update_details: Optional[StrictStr] = None
    ecgt_commercial_guarantee_enabled: Optional[StrictBool] = None
    gpsr_manufacturer_type: Optional[StrictStr] = None
    gpsr_manufacturer_id: Optional[StrictInt] = None
    gpsr_responsible_person_type: Optional[StrictStr] = None
    gpsr_responsible_person_id: Optional[StrictInt] = None
    gpsr_serial_number: Optional[StrictStr] = None
    gpsr_safety_warnings: Optional[StrictStr] = None
