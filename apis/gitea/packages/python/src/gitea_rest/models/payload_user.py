# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class PayloadUser(ApiModel):
    """PayloadUser model."""

    email: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
