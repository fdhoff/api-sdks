# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class RunDetails(ApiModel):
    """RunDetails model."""

    html_url: Optional[StrictStr] = None
    run_url: Optional[StrictStr] = None
    workflow_run_id: Optional[StrictInt] = None
