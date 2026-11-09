# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class MainQuestionnaireCompanyStructure(str, Enum):
    """Allowed values of MainQuestionnaireCompanyStructure."""

    CCORP = "CCorp"
    LLC = "LLC"
    LLP = "LLP"
    NONPROFIT = "NonProfit"
    PARTNERSHIP = "Partnership"
    PROFESSIONALASSOCIATION = "ProfessionalAssociation"
    PROFESSIONALCORPORATION = "ProfessionalCorporation"
    SCORP = "SCorp"
    GENERALPARTNERSHIP = "GeneralPartnership"
    LIMITEDPARTNERSHIP = "LimitedPartnership"
    JOINTVENTURE = "JointVenture"
    LLCTAXEDASSOLEPROPRIETORSHIP = "LLCTaxedAsSoleProprietorship"
    SOLEPROPRIETORSHIP = "SoleProprietorship"
    EXEMPTEDCOMPANY = "ExemptedCompany"
    LIMITED = "Limited"
