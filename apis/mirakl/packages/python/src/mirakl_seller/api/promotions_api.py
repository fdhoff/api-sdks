# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from mirakl_seller import models as _models
from mirakl_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from mirakl_seller.models.pr01_response200 import PR01Response200
from mirakl_seller.models.pr03_request import PR03Request
from mirakl_seller.models.pr04_request import PR04Request

_p_r01: Operation[PR01Response200] = Operation(
    id="PR01",
    method="GET",
    path="/api/promotions",
    resource="promotions",
    name="list",
    params=(
        Param("ids", "ids", "query"),
        Param("types", "types", "query"),
        Param("states", "states", "query"),
        Param("ending_after", "ending_after", "query"),
        Param("starting_before", "starting_before", "query"),
        Param("date_created_from", "date_created_from", "query"),
        Param("date_created_to", "date_created_to", "query"),
        Param("last_request_date", "last_request_date", "query"),
        Param("locale", "locale", "query"),
        Param("trigger_offer_ids", "trigger_offer_ids", "query"),
        Param("reward_offer_ids", "reward_offer_ids", "query"),
        Param("channel_codes", "channel_codes", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("max", "max", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=PR01Response200,
    returns_json=True,
    iterator="iter",
    item=_models.PR01Response200Promotions,
    paging=Offset(items="promotions", total="total_count", offset="offset"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PROMOTION_READ",
                ),
            ),
        ),
    ),
)
_p_r03: Operation[None] = Operation(
    id="PR03",
    method="POST",
    path="/api/promotions",
    resource="promotions",
    name="create",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=None,
    security=((Scheme("Shop-API-Key", ("ROLE_SHOP_ADMIN",)),),),
)
_p_r04: Operation[None] = Operation(
    id="PR04",
    method="PUT",
    path="/api/promotions/{promotion_internal_id}",
    resource="promotions",
    name="update",
    params=(
        Param("promotion_internal_id", "promotion_internal_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=((Scheme("Shop-API-Key", ("ROLE_SHOP_ADMIN",)),),),
)

OPERATIONS = (
    _p_r01,
    _p_r03,
    _p_r04,
)


class PromotionsApi(Resource):
    @checked
    def list(
        self,
        *,
        ids: Optional[StrictStr] = None,
        types: Optional[StrictStr] = None,
        states: Optional[StrictStr] = None,
        ending_after: Optional[datetime] = None,
        starting_before: Optional[datetime] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_request_date: Optional[datetime] = None,
        locale: Optional[StrictStr] = None,
        trigger_offer_ids: Optional[StrictStr] = None,
        reward_offer_ids: Optional[StrictStr] = None,
        channel_codes: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> PR01Response200:
        """List one page of promotions (PR01)."""
        return self._call(
            _p_r01,
            ids=ids,
            types=types,
            states=states,
            ending_after=ending_after,
            starting_before=starting_before,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_request_date=last_request_date,
            locale=locale,
            trigger_offer_ids=trigger_offer_ids,
            reward_offer_ids=reward_offer_ids,
            channel_codes=channel_codes,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        ids: Optional[StrictStr] = None,
        types: Optional[StrictStr] = None,
        states: Optional[StrictStr] = None,
        ending_after: Optional[datetime] = None,
        starting_before: Optional[datetime] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_request_date: Optional[datetime] = None,
        locale: Optional[StrictStr] = None,
        trigger_offer_ids: Optional[StrictStr] = None,
        reward_offer_ids: Optional[StrictStr] = None,
        channel_codes: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.PR01Response200Promotions]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p_r01,
            ids=ids,
            types=types,
            states=states,
            ending_after=ending_after,
            starting_before=starting_before,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_request_date=last_request_date,
            locale=locale,
            trigger_offer_ids=trigger_offer_ids,
            reward_offer_ids=reward_offer_ids,
            channel_codes=channel_codes,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def create(
        self,
        body: Optional[Union[PR03Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Create a promotion (PR03)."""
        return self._call(
            _p_r03,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        promotion_internal_id: StrictStr,
        body: Optional[Union[PR04Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Update a promotion (PR04)."""
        return self._call(
            _p_r04,
            promotion_internal_id=promotion_internal_id,
            _body=body,
            shop_id=shop_id,
        )


class AsyncPromotionsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        ids: Optional[StrictStr] = None,
        types: Optional[StrictStr] = None,
        states: Optional[StrictStr] = None,
        ending_after: Optional[datetime] = None,
        starting_before: Optional[datetime] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_request_date: Optional[datetime] = None,
        locale: Optional[StrictStr] = None,
        trigger_offer_ids: Optional[StrictStr] = None,
        reward_offer_ids: Optional[StrictStr] = None,
        channel_codes: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> PR01Response200:
        """List one page of promotions (PR01)."""
        return await self._call(
            _p_r01,
            ids=ids,
            types=types,
            states=states,
            ending_after=ending_after,
            starting_before=starting_before,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_request_date=last_request_date,
            locale=locale,
            trigger_offer_ids=trigger_offer_ids,
            reward_offer_ids=reward_offer_ids,
            channel_codes=channel_codes,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        ids: Optional[StrictStr] = None,
        types: Optional[StrictStr] = None,
        states: Optional[StrictStr] = None,
        ending_after: Optional[datetime] = None,
        starting_before: Optional[datetime] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_request_date: Optional[datetime] = None,
        locale: Optional[StrictStr] = None,
        trigger_offer_ids: Optional[StrictStr] = None,
        reward_offer_ids: Optional[StrictStr] = None,
        channel_codes: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.PR01Response200Promotions]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p_r01,
            ids=ids,
            types=types,
            states=states,
            ending_after=ending_after,
            starting_before=starting_before,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_request_date=last_request_date,
            locale=locale,
            trigger_offer_ids=trigger_offer_ids,
            reward_offer_ids=reward_offer_ids,
            channel_codes=channel_codes,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    async def create(
        self,
        body: Optional[Union[PR03Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Create a promotion (PR03)."""
        return await self._call(
            _p_r03,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        promotion_internal_id: StrictStr,
        body: Optional[Union[PR04Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Update a promotion (PR04)."""
        return await self._call(
            _p_r04,
            promotion_internal_id=promotion_internal_id,
            _body=body,
            shop_id=shop_id,
        )
