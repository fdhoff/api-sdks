# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class CardConfiguration(ApiModel):
    """CardConfiguration model."""

    single_use: StrictBool = Field(alias="singleUse")
