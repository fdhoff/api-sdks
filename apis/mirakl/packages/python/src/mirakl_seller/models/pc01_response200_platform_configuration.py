# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pc01_response200_platform_configuration_customer_model import (
    PC01Response200PlatformConfigurationCustomerModel,
)
from mirakl_seller.models.pc01_response200_platform_configuration_enhanced_seller_invoicing import (
    PC01Response200PlatformConfigurationEnhancedSellerInvoicing,
)
from mirakl_seller.models.pc01_response200_platform_configuration_platform_model import (
    PC01Response200PlatformConfigurationPlatformModel,
)
from mirakl_seller._runtime import ApiModel


class PC01Response200PlatformConfiguration(ApiModel):
    """PC01Response200PlatformConfiguration model."""

    customer_model: PC01Response200PlatformConfigurationCustomerModel
    enhanced_seller_invoicing: PC01Response200PlatformConfigurationEnhancedSellerInvoicing
    platform_model: PC01Response200PlatformConfigurationPlatformModel
