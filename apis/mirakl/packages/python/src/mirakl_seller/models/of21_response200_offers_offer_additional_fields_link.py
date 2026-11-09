# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.of21_response200_offers_offer_additional_fields import (
    OF21Response200OffersOfferAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OF21Response200OffersOfferAdditionalFieldsLink(OF21Response200OffersOfferAdditionalFields):
    """OF21Response200OffersOfferAdditionalFieldsLink model."""

    value: StrictStr
