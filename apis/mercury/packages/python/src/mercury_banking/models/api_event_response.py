# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.api_event_operation_type import ApiEventOperationType
from mercury_banking.models.api_event_resource_type import ApiEventResourceType
from mercury_banking._runtime import ApiModel


class ApiEventResponse(ApiModel):
    """ApiEventResponse model."""

    changed_paths: List[StrictStr] = Field(alias="changedPaths")
    id: UUID
    merge_patch: Dict[str, Any] = Field(alias="mergePatch")
    occurred_at: StrictStr = Field(alias="occurredAt")
    operation_type: ApiEventOperationType = Field(alias="operationType")
    previous_values: Optional[Dict[str, Any]] = Field(default=None, alias="previousValues")
    resource_id: UUID = Field(alias="resourceId")
    resource_type: ApiEventResourceType = Field(alias="resourceType")
    resource_version: Annotated[int, Field(strict=True, ge=1)] = Field(alias="resourceVersion")
