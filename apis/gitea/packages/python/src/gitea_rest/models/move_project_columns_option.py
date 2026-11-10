# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from gitea_rest._runtime import ApiModel


class MoveProjectColumnsOption(ApiModel):
    """MoveProjectColumnsOption model."""

    column_ids: List[StrictInt]
