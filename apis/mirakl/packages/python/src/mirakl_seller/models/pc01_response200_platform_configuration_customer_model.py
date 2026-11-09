# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PC01Response200PlatformConfigurationCustomerModel(ApiModel):
    """PC01Response200PlatformConfigurationCustomerModel model."""

    b2b: StrictBool
    b2c: StrictBool
