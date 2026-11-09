# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class IdentificationType(str, Enum):
    """Allowed values of IdentificationType."""

    PASSPORT = "Passport"
    DRIVERSLICENSE = "DriversLicense"
    STATEID = "StateID"
    ALIENREGISTRATIONCARD = "AlienRegistrationCard"
    EMPLOYEEAUTHORIZATIONDOCUMENT = "EmployeeAuthorizationDocument"
    VERIFIEDBYTHIRDPARTY = "VerifiedByThirdParty"
    NATIONALID = "NationalID"
    RESIDENCEPERMIT = "ResidencePermit"
    VISA = "Visa"
