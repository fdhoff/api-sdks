# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pm11_response200_attributes_roles_parameters import PM11Response200AttributesRolesParameters
from mirakl_seller._runtime import ApiModel


class PM11Response200AttributesRoles(ApiModel):
    """PM11Response200AttributesRoles model."""

    parameters: List[PM11Response200AttributesRolesParameters]
    type: StrictStr
