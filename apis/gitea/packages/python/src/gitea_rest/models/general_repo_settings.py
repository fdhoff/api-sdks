# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class GeneralRepoSettings(ApiModel):
    """GeneralRepoSettings model."""

    http_git_disabled: Optional[StrictBool] = None
    lfs_disabled: Optional[StrictBool] = None
    migrations_disabled: Optional[StrictBool] = None
    mirrors_disabled: Optional[StrictBool] = None
    stars_disabled: Optional[StrictBool] = None
    time_tracking_disabled: Optional[StrictBool] = None
