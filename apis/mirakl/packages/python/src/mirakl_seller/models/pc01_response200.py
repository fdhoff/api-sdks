# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pc01_response200_features import PC01Response200Features
from mirakl_seller.models.pc01_response200_modules import PC01Response200Modules
from mirakl_seller.models.pc01_response200_platform_configuration import PC01Response200PlatformConfiguration
from mirakl_seller._runtime import ApiModel


class PC01Response200(ApiModel):
    """PC01Response200 model."""

    features: PC01Response200Features
    modules: PC01Response200Modules
    platform_configuration: PC01Response200PlatformConfiguration
    platform_name: StrictStr
    tenant_name: StrictStr
    timezone: StrictStr
