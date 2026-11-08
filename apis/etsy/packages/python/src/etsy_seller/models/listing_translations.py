# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller.models.listing_translation import ListingTranslation
from etsy_seller._runtime import ApiModel


class ListingTranslations(ApiModel):
    """ListingTranslations model."""

    de: Optional[ListingTranslation] = None
    en_gb: Optional[ListingTranslation] = Field(default=None, alias="en-GB")
    en_in: Optional[ListingTranslation] = Field(default=None, alias="en-IN")
    en_us: Optional[ListingTranslation] = Field(default=None, alias="en-US")
    es: Optional[ListingTranslation] = None
    fr: Optional[ListingTranslation] = None
    it: Optional[ListingTranslation] = None
    ja: Optional[ListingTranslation] = None
    nl: Optional[ListingTranslation] = None
    pl: Optional[ListingTranslation] = None
    pt: Optional[ListingTranslation] = None
    ru: Optional[ListingTranslation] = None
    sv: Optional[ListingTranslation] = None
