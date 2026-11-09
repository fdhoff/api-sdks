# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class OrganizationDBA(ApiModel):
    """OrganizationDBA model."""

    dba_is_default: StrictBool = Field(alias="dbaIsDefault")
    dba_name: StrictStr = Field(alias="dbaName")
