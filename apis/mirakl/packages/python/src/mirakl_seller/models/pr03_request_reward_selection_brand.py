# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pr03_request_reward_selection import PR03RequestRewardSelection
from mirakl_seller._runtime import ApiModel


class PR03RequestRewardSelectionBrand(PR03RequestRewardSelection):
    """PR03RequestRewardSelectionBrand model."""

    values: List[StrictStr]
