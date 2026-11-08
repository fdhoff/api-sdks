# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account_v2.models.create_calculated_shipping_rules_request import CreateCalculatedShippingRulesRequest
from ebay_sell.account_v2.models.create_flat_shipping_rules_request import CreateFlatShippingRulesRequest
from ebay_sell.account_v2.models.create_promotional_shipping_rule_request import CreatePromotionalShippingRuleRequest
from ebay_sell.account_v2.models.get_combined_shipping_rules_public_api_response import (
    GetCombinedShippingRulesPublicApiResponse,
)
from ebay_sell.account_v2.models.update_calculated_shipping_rules_request import UpdateCalculatedShippingRulesRequest
from ebay_sell.account_v2.models.update_combined_payments_request import UpdateCombinedPaymentsRequest
from ebay_sell.account_v2.models.update_flat_shipping_rules_request import UpdateFlatShippingRulesRequest
from ebay_sell.account_v2.models.update_promotional_shipping_rule_request import UpdatePromotionalShippingRuleRequest

_create_calculated_shipping_rules: Operation[None] = Operation(
    id="createCalculatedShippingRules",
    method="POST",
    path="/sell/account/v2/combined_shipping_rules/create_calculated_shipping_rules",
    resource="combined_shipping_rules",
    name="create_calculated",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_create_flat_shipping_rules: Operation[None] = Operation(
    id="createFlatShippingRules",
    method="POST",
    path="/sell/account/v2/combined_shipping_rules/create_flat_shipping_rules",
    resource="combined_shipping_rules",
    name="create_flat",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_create_promotional_shipping_rule: Operation[None] = Operation(
    id="createPromotionalShippingRule",
    method="POST",
    path="/sell/account/v2/combined_shipping_rules/create_promotional_shipping_rule",
    resource="combined_shipping_rules",
    name="create_promotional",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_get_combined_shipping_rules: Operation[GetCombinedShippingRulesPublicApiResponse] = Operation(
    id="getCombinedShippingRules",
    method="GET",
    path="/sell/account/v2/combined_shipping_rules",
    resource="combined_shipping_rules",
    name="get",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=GetCombinedShippingRulesPublicApiResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account.readonly",)),),),
    host="api",
)
_update_calculated_shipping_rules: Operation[None] = Operation(
    id="updateCalculatedShippingRules",
    method="POST",
    path="/sell/account/v2/combined_shipping_rules/update_calculated_shipping_rules",
    resource="combined_shipping_rules",
    name="update_calculated",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_update_combined_payments: Operation[None] = Operation(
    id="updateCombinedPayments",
    method="POST",
    path="/sell/account/v2/combined_shipping_rules/update_combined_payments",
    resource="combined_shipping_rules",
    name="update_combined_payments",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_update_flat_shipping_rules: Operation[None] = Operation(
    id="updateFlatShippingRules",
    method="POST",
    path="/sell/account/v2/combined_shipping_rules/update_flat_shipping_rules",
    resource="combined_shipping_rules",
    name="update_flat",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_update_promotional_shipping_rule: Operation[None] = Operation(
    id="updatePromotionalShippingRule",
    method="POST",
    path="/sell/account/v2/combined_shipping_rules/update_promotional_shipping_rule",
    resource="combined_shipping_rules",
    name="update_promotional",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _create_calculated_shipping_rules,
    _create_flat_shipping_rules,
    _create_promotional_shipping_rule,
    _get_combined_shipping_rules,
    _update_calculated_shipping_rules,
    _update_combined_payments,
    _update_flat_shipping_rules,
    _update_promotional_shipping_rule,
)


class CombinedShippingRulesApi(Resource):
    @checked
    def create_calculated(
        self,
        body: Optional[Union[CreateCalculatedShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create calculated combined shipping rules."""
        return self._call(
            _create_calculated_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def create_flat(
        self,
        body: Optional[Union[CreateFlatShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create flat-rate combined shipping rules."""
        return self._call(
            _create_flat_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def create_promotional(
        self,
        body: Optional[Union[CreatePromotionalShippingRuleRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create a promotional shipping rule."""
        return self._call(
            _create_promotional_shipping_rule,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetCombinedShippingRulesPublicApiResponse:
        """Get the seller's combined shipping rules."""
        return self._call(
            _get_combined_shipping_rules,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def update_calculated(
        self,
        body: Optional[Union[UpdateCalculatedShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update calculated combined shipping rules."""
        return self._call(
            _update_calculated_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def update_combined_payments(
        self,
        body: Optional[Union[UpdateCombinedPaymentsRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Set whether buyers can pay for several items at once."""
        return self._call(
            _update_combined_payments,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def update_flat(
        self,
        body: Optional[Union[UpdateFlatShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update flat-rate combined shipping rules."""
        return self._call(
            _update_flat_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def update_promotional(
        self,
        body: Optional[Union[UpdatePromotionalShippingRuleRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update a promotional shipping rule."""
        return self._call(
            _update_promotional_shipping_rule,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncCombinedShippingRulesApi(AsyncResource):
    @checked
    async def create_calculated(
        self,
        body: Optional[Union[CreateCalculatedShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create calculated combined shipping rules."""
        return await self._call(
            _create_calculated_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def create_flat(
        self,
        body: Optional[Union[CreateFlatShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create flat-rate combined shipping rules."""
        return await self._call(
            _create_flat_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def create_promotional(
        self,
        body: Optional[Union[CreatePromotionalShippingRuleRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create a promotional shipping rule."""
        return await self._call(
            _create_promotional_shipping_rule,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetCombinedShippingRulesPublicApiResponse:
        """Get the seller's combined shipping rules."""
        return await self._call(
            _get_combined_shipping_rules,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def update_calculated(
        self,
        body: Optional[Union[UpdateCalculatedShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update calculated combined shipping rules."""
        return await self._call(
            _update_calculated_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def update_combined_payments(
        self,
        body: Optional[Union[UpdateCombinedPaymentsRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Set whether buyers can pay for several items at once."""
        return await self._call(
            _update_combined_payments,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def update_flat(
        self,
        body: Optional[Union[UpdateFlatShippingRulesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update flat-rate combined shipping rules."""
        return await self._call(
            _update_flat_shipping_rules,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def update_promotional(
        self,
        body: Optional[Union[UpdatePromotionalShippingRuleRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update a promotional shipping rule."""
        return await self._call(
            _update_promotional_shipping_rule,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
