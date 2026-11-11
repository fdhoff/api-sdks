# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.task_resolution_method import TaskResolutionMethod
from mercury_banking.models.task_resolution_operation import TaskResolutionOperation
from mercury_banking._runtime import ApiModel


class TaskResolution(ApiModel):
    """TaskResolution model."""

    method: TaskResolutionMethod
    operations: List[TaskResolutionOperation]
