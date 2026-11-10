# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class IssueFormField(ApiModel):
    """IssueFormField model."""

    attributes: Optional[Dict[str, Any]] = None
    id: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    validations: Optional[Dict[str, Any]] = None
    visible: Optional[List[StrictStr]] = None
