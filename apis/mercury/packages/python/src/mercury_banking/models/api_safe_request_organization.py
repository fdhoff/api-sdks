# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class APISafeRequestOrganization(ApiModel):
    """APISafeRequestOrganization model."""

    legal_entity_name: StrictStr = Field(alias="legalEntityName")
    signatory_email: StrictStr = Field(alias="signatoryEmail")
    signatory_name: StrictStr = Field(alias="signatoryName")
    signatory_title: StrictStr = Field(alias="signatoryTitle")
