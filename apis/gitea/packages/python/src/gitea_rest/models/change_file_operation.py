# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class ChangeFileOperation(ApiModel):
    """ChangeFileOperation model."""

    content: Optional[StrictStr] = None
    from_path: Optional[StrictStr] = None
    operation: StrictStr
    path: StrictStr
    sha: Optional[StrictStr] = None
