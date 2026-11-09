# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.main_questionnaire_company_structure import MainQuestionnaireCompanyStructure
from mercury_banking.models.main_questionnaire_entity_formation_document_type import (
    MainQuestionnaireEntityFormationDocumentType,
)
from mercury_banking._runtime import ApiModel


class APIFormationDetails(ApiModel):
    """APIFormationDetails model."""

    company_origin_country: Optional[StrictStr] = Field(default=None, alias="companyOriginCountry")
    company_structure: Optional[MainQuestionnaireCompanyStructure] = Field(default=None, alias="companyStructure")
    e_in_document_file_blob: Optional[StrictStr] = Field(default=None, alias="eINDocumentFileBlob")
    ein_document_file_blob: Optional[StrictStr] = Field(default=None, alias="einDocumentFileBlob")
    federal_ein: Optional[StrictStr] = Field(default=None, alias="federalEin")
    foreign_business_number: Optional[StrictStr] = Field(default=None, alias="foreignBusinessNumber")
    formation_document_file_blob: Optional[StrictStr] = Field(default=None, alias="formationDocumentFileBlob")
    formation_document_type: Optional[MainQuestionnaireEntityFormationDocumentType] = Field(
        default=None, alias="formationDocumentType"
    )
