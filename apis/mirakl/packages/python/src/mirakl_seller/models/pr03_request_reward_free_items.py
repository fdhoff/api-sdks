# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pr03_request_reward import PR03RequestReward
from mirakl_seller.models.pr03_request_reward_selection import PR03RequestRewardSelection
from mirakl_seller._runtime import ApiModel


class PR03RequestRewardFreeItems(PR03RequestReward):
    """PR03RequestRewardFreeItems model."""

    free_items_quantity: StrictInt
