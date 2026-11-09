# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.dr11_response200_data_payment_destination import DR11Response200DataPaymentDestination
from mirakl_seller._runtime import ApiModel


class DR11Response200DataPaymentDestinationIban(DR11Response200DataPaymentDestination):
    """DR11Response200DataPaymentDestinationIban model."""

    iban: StrictStr
