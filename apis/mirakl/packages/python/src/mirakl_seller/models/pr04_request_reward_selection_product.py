# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pr04_request_reward_selection import PR04RequestRewardSelection
from mirakl_seller.models.pr04_request_reward_selection_product_values import PR04RequestRewardSelectionProductValues
from mirakl_seller._runtime import ApiModel


class PR04RequestRewardSelectionProduct(PR04RequestRewardSelection):
    """PR04RequestRewardSelectionProduct model."""

    values: List[PR04RequestRewardSelectionProductValues]
