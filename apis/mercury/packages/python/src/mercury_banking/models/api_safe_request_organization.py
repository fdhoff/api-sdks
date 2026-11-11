# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class APISafeRequestOrganization(ApiModel):
    """APISafeRequestOrganization model."""

    legal_entity_name: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="legalEntityName")
    signatory_email: StrictStr = Field(alias="signatoryEmail")
    signatory_name: Annotated[str, Field(min_length=1, strict=True, max_length=5000)] = Field(alias="signatoryName")
    signatory_title: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="signatoryTitle")
