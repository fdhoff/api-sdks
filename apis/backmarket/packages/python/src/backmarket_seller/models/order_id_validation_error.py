# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from backmarket_seller.models.order_id_validation_error_data import OrderIdValidationErrorData
from backmarket_seller.models.order_id_validation_error_error import OrderIdValidationErrorError
from backmarket_seller._runtime import ApiModel


class OrderIdValidationError(ApiModel):
    """OrderIdValidationError model."""

    error: OrderIdValidationErrorError
    data: OrderIdValidationErrorData
