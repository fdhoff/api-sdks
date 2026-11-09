# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class BooksTag(ApiModel):
    """BooksTag model."""

    id: StrictStr
    name: StrictStr
    tag_group_id: StrictStr = Field(alias="tagGroupId")
