# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.hazard_statement import HazardStatement
from ebay_sell.metadata.models.pictogram import Pictogram
from ebay_sell.metadata.models.signal_word import SignalWord
from ebay_sell._runtime import ApiModel


class HazardousMaterialDetailsResponse(ApiModel):
    """HazardousMaterialDetailsResponse model."""

    signal_words: Optional[List[SignalWord]] = Field(default=None, alias="signalWords")
    statements: Optional[List[HazardStatement]] = None
    pictograms: Optional[List[Pictogram]] = None
