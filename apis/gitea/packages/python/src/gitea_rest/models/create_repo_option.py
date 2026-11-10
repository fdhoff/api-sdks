# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gitea_rest.models.object_format_name import ObjectFormatName
from gitea_rest._runtime import ApiModel


class CreateRepoOption(ApiModel):
    """CreateRepoOption model."""

    auto_init: Optional[StrictBool] = None
    default_branch: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    gitignores: Optional[StrictStr] = None
    issue_labels: Optional[StrictStr] = None
    license: Optional[StrictStr] = None
    name: Annotated[str, Field(strict=True)]
    object_format_name: Optional[ObjectFormatName] = None
    private: Optional[StrictBool] = None
    readme: Optional[StrictStr] = None
    template: Optional[StrictBool] = None
    trust_model: Optional[StrictStr] = None
