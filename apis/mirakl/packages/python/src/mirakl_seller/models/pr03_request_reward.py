# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from mirakl_seller.models.pr03_request_reward_selection import PR03RequestRewardSelection
from mirakl_seller._runtime import ApiModel


class PR03RequestReward(ApiModel):
    """PR03RequestReward model."""

    selection: PR03RequestRewardSelection
    type: StrictStr
