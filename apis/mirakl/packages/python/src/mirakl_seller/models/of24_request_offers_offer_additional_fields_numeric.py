# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.of24_request_offers_offer_additional_fields import OF24RequestOffersOfferAdditionalFields
from mirakl_seller._runtime import ApiModel


class OF24RequestOffersOfferAdditionalFieldsNumeric(OF24RequestOffersOfferAdditionalFields):
    """OF24RequestOffersOfferAdditionalFieldsNumeric model."""

    value: StrictStr
