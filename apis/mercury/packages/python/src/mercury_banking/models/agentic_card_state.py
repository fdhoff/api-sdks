# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class AgenticCardState(ApiModel):
    """AgenticCardState model."""

    manual_approval_threshold: Optional[float] = Field(default=None, alias="manualApprovalThreshold")
