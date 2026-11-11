# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.task_kind import TaskKind
from mercury_banking.models.task_notification_status import TaskNotificationStatus
from mercury_banking.models.task_related_resource import TaskRelatedResource
from mercury_banking.models.task_resolution import TaskResolution
from mercury_banking._runtime import ApiModel


class UserTask(ApiModel):
    """UserTask model."""

    amount: Optional[Annotated[float, Field(ge=0.01)]] = None
    category: StrictStr
    completed_at: Optional[StrictStr] = Field(default=None, alias="completedAt")
    created_at: StrictStr = Field(alias="createdAt")
    description: StrictStr
    due_date: Optional[StrictStr] = Field(default=None, alias="dueDate")
    id: UUID
    kind: TaskKind
    product: StrictStr
    related_resource: Optional[TaskRelatedResource] = Field(default=None, alias="relatedResource")
    resolution: TaskResolution
    status: TaskNotificationStatus
    title: StrictStr
    urgency: StrictStr
    web_url: StrictStr = Field(alias="webUrl")
