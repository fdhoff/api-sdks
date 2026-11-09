# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.p11_response200_products_offers_offer_additional_fields import (
    P11Response200ProductsOffersOfferAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class P11Response200ProductsOffersOfferAdditionalFieldsString(P11Response200ProductsOffersOfferAdditionalFields):
    """P11Response200ProductsOffersOfferAdditionalFieldsString model."""

    value: StrictStr
