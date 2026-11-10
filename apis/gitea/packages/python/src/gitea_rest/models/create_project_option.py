# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreateProjectOption(ApiModel):
    """CreateProjectOption model."""

    card_type: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    template_type: Optional[StrictStr] = None
    title: StrictStr
