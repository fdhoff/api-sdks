# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.mercury_category import MercuryCategory
from mercury_banking.models.standard_icon import StandardIcon
from mercury_banking._runtime import ApiModel


class MercuryCategoryWithDisplay(ApiModel):
    """MercuryCategoryWithDisplay model."""

    category: MercuryCategory
    display: StrictStr
    icon: StandardIcon
