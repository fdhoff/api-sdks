# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gitea_rest._runtime import ApiModel


class CreateDeployKeyTokenOption(ApiModel):
    """CreateDeployKeyTokenOption model."""

    read_only: Optional[StrictBool] = None
    title: Annotated[str, Field(strict=True)]
