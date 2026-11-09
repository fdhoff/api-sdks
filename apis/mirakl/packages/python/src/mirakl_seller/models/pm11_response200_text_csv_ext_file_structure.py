# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class PM11Response200TextCsvExtFileStructure(ApiModel):
    """PM11Response200TextCsvExtFileStructure model."""

    channels: Optional[StrictStr] = None
    code: StrictStr
    default_value: Optional[StrictStr] = Field(default=None, alias="default-value")
    description: Optional[StrictStr] = None
    description_xx: StrictStr = Field(alias="description[xx]")
    example: Optional[StrictStr] = None
    hierarchy_code: Optional[StrictStr] = Field(default=None, alias="hierarchy-code")
    label: Optional[StrictStr] = None
    label_xx: StrictStr = Field(alias="label[xx]")
    locale: Optional[StrictStr] = None
    required: StrictBool
    requirement_level: StrictStr = Field(alias="requirement-level")
    roles: StrictStr
    transformations: Optional[StrictStr] = None
    type: StrictStr
    type_parameter: StrictStr = Field(alias="type-parameter")
    type_parameters: Optional[StrictStr] = Field(default=None, alias="type-parameters")
    unique_code: Optional[StrictStr] = Field(default=None, alias="unique-code")
    validations: Optional[StrictStr] = None
    values: Optional[StrictStr] = None
    values_list: Optional[StrictStr] = Field(default=None, alias="values-list")
    variant: StrictBool
