# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from gitea_rest._runtime import ApiModel


class RenameUserOption(ApiModel):
    """RenameUserOption model."""

    new_username: Annotated[str, Field(strict=True)]
