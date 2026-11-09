# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pm11_response200_attributes_channels import PM11Response200AttributesChannels
from mirakl_seller.models.pm11_response200_attributes_description_translations import (
    PM11Response200AttributesDescriptionTranslations,
)
from mirakl_seller.models.pm11_response200_attributes_label_translations import (
    PM11Response200AttributesLabelTranslations,
)
from mirakl_seller.models.pm11_response200_attributes_roles import PM11Response200AttributesRoles
from mirakl_seller.models.pm11_response200_attributes_type_parameters import PM11Response200AttributesTypeParameters
from mirakl_seller.models.pm11_response200_attributes_values import PM11Response200AttributesValues
from mirakl_seller._runtime import ApiModel


class PM11Response200Attributes(ApiModel):
    """PM11Response200Attributes model."""

    channels: Optional[List[PM11Response200AttributesChannels]] = None
    code: StrictStr
    default_value: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    description_translations: List[PM11Response200AttributesDescriptionTranslations]
    example: Optional[StrictStr] = None
    hierarchy_code: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    label_translations: List[PM11Response200AttributesLabelTranslations]
    locale: Optional[StrictStr] = None
    required: StrictBool
    requirement_level: StrictStr
    roles: List[PM11Response200AttributesRoles]
    transformations: Optional[StrictStr] = None
    type: StrictStr
    type_parameter: StrictStr
    type_parameters: Optional[List[PM11Response200AttributesTypeParameters]] = None
    unique_code: Optional[StrictStr] = None
    validations: Optional[StrictStr] = None
    values: Optional[List[PM11Response200AttributesValues]] = None
    values_list: Optional[StrictStr] = None
    variant: StrictBool
