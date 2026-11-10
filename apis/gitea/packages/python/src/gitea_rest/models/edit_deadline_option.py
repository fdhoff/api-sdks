# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from gitea_rest._runtime import ApiModel


class EditDeadlineOption(ApiModel):
    """EditDeadlineOption model."""

    due_date: datetime
