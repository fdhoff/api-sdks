# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class GlAllocation(ApiModel):
    """GlAllocation model."""

    amount: Annotated[float, Field(multiple_of=0.01)]
    class_name: Optional[StrictStr] = Field(default=None, alias="className")
    department_name: Optional[StrictStr] = Field(default=None, alias="departmentName")
    description: Optional[StrictStr] = None
    gl_code_name: StrictStr = Field(alias="glCodeName")
