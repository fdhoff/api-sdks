# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictBool, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.card import Card
from mercury_banking.models.card_list_response import CardListResponse
from mercury_banking.models.card_reveal_response import CardRevealResponse
from mercury_banking.models.create_card_request import CreateCardRequest
from mercury_banking.models.update_card_request import UpdateCardRequest

_cancel_card: Operation[Card] = Operation(
    id="cancelCard",
    method="POST",
    path="/cards/{cardId}/cancel",
    resource="cards",
    name="cancel",
    params=(Param("cardId", "card_id", "path"),),
    response=Card,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_create_card: Operation[Card] = Operation(
    id="createCard",
    method="POST",
    path="/cards",
    resource="cards",
    name="create",
    params=(),
    response=Card,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_freeze_card: Operation[Card] = Operation(
    id="freezeCard",
    method="POST",
    path="/cards/{cardId}/freeze",
    resource="cards",
    name="freeze",
    params=(Param("cardId", "card_id", "path"),),
    response=Card,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_card: Operation[Card] = Operation(
    id="getCard",
    method="GET",
    path="/cards/{cardId}",
    resource="cards",
    name="get",
    params=(Param("cardId", "card_id", "path"),),
    response=Card,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_cards: Operation[CardListResponse] = Operation(
    id="listCards",
    method="GET",
    path="/cards",
    resource="cards",
    name="list",
    params=(
        Param("accountId", "account_id", "query"),
        Param("status", "status", "query"),
        Param("type", "type", "query"),
        Param("kind", "kind", "query"),
        Param("userId", "user_id", "query"),
        Param("isAgentCard", "is_agent_card", "query"),
        Param("isSingleUse", "is_single_use", "query"),
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
    ),
    response=CardListResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Card,
    paging=Cursor(items="cards", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_reveal_card_pan: Operation[CardRevealResponse] = Operation(
    id="revealCardPan",
    method="GET",
    path="/cards/{cardId}/reveal",
    resource="cards",
    name="reveal",
    params=(Param("cardId", "card_id", "path"),),
    response=CardRevealResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="vault",
)
_unfreeze_card: Operation[Card] = Operation(
    id="unfreezeCard",
    method="POST",
    path="/cards/{cardId}/unfreeze",
    resource="cards",
    name="unfreeze",
    params=(Param("cardId", "card_id", "path"),),
    response=Card,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_update_card: Operation[Card] = Operation(
    id="updateCard",
    method="POST",
    path="/cards/{cardId}",
    resource="cards",
    name="update",
    params=(Param("cardId", "card_id", "path"),),
    response=Card,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _cancel_card,
    _create_card,
    _freeze_card,
    _get_card,
    _list_cards,
    _reveal_card_pan,
    _unfreeze_card,
    _update_card,
)


class CardsApi(Resource):
    @checked
    def cancel(
        self,
        card_id: UUID,
    ) -> Card:
        """Cancel a card for good."""
        return self._call(
            _cancel_card,
            card_id=card_id,
        )

    @checked
    def create(
        self,
        body: Optional[Union[CreateCardRequest, Mapping[str, Any]]] = None,
    ) -> Card:
        """Issue a card."""
        return self._call(
            _create_card,
            _body=body,
        )

    @checked
    def freeze(
        self,
        card_id: UUID,
    ) -> Card:
        """Freeze a card."""
        return self._call(
            _freeze_card,
            card_id=card_id,
        )

    @checked
    def get(
        self,
        card_id: UUID,
    ) -> Card:
        """Get one card."""
        return self._call(
            _get_card,
            card_id=card_id,
        )

    @checked
    def list(
        self,
        *,
        account_id: Optional[List[StrictStr]] = None,
        status: Optional[List[StrictStr]] = None,
        type: Optional[List[StrictStr]] = None,
        kind: Optional[List[StrictStr]] = None,
        user_id: Optional[StrictStr] = None,
        is_agent_card: Optional[StrictBool] = None,
        is_single_use: Optional[StrictBool] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> CardListResponse:
        """List one page of cards."""
        return self._call(
            _list_cards,
            account_id=account_id,
            status=status,
            type=type,
            kind=kind,
            user_id=user_id,
            is_agent_card=is_agent_card,
            is_single_use=is_single_use,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    def iter(
        self,
        *,
        account_id: Optional[List[StrictStr]] = None,
        status: Optional[List[StrictStr]] = None,
        type: Optional[List[StrictStr]] = None,
        kind: Optional[List[StrictStr]] = None,
        user_id: Optional[StrictStr] = None,
        is_agent_card: Optional[StrictBool] = None,
        is_single_use: Optional[StrictBool] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> Iterator[_models.Card]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_cards,
            account_id=account_id,
            status=status,
            type=type,
            kind=kind,
            user_id=user_id,
            is_agent_card=is_agent_card,
            is_single_use=is_single_use,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    def reveal(
        self,
        card_id: UUID,
    ) -> CardRevealResponse:
        """Get a card's full number and security code. Never log the result."""
        return self._call(
            _reveal_card_pan,
            card_id=card_id,
        )

    @checked
    def unfreeze(
        self,
        card_id: UUID,
    ) -> Card:
        """Unfreeze a card."""
        return self._call(
            _unfreeze_card,
            card_id=card_id,
        )

    @checked
    def update(
        self,
        card_id: UUID,
        body: Optional[Union[UpdateCardRequest, Mapping[str, Any]]] = None,
    ) -> Card:
        """Update a card."""
        return self._call(
            _update_card,
            card_id=card_id,
            _body=body,
        )


class AsyncCardsApi(AsyncResource):
    @checked
    async def cancel(
        self,
        card_id: UUID,
    ) -> Card:
        """Cancel a card for good."""
        return await self._call(
            _cancel_card,
            card_id=card_id,
        )

    @checked
    async def create(
        self,
        body: Optional[Union[CreateCardRequest, Mapping[str, Any]]] = None,
    ) -> Card:
        """Issue a card."""
        return await self._call(
            _create_card,
            _body=body,
        )

    @checked
    async def freeze(
        self,
        card_id: UUID,
    ) -> Card:
        """Freeze a card."""
        return await self._call(
            _freeze_card,
            card_id=card_id,
        )

    @checked
    async def get(
        self,
        card_id: UUID,
    ) -> Card:
        """Get one card."""
        return await self._call(
            _get_card,
            card_id=card_id,
        )

    @checked
    async def list(
        self,
        *,
        account_id: Optional[List[StrictStr]] = None,
        status: Optional[List[StrictStr]] = None,
        type: Optional[List[StrictStr]] = None,
        kind: Optional[List[StrictStr]] = None,
        user_id: Optional[StrictStr] = None,
        is_agent_card: Optional[StrictBool] = None,
        is_single_use: Optional[StrictBool] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> CardListResponse:
        """List one page of cards."""
        return await self._call(
            _list_cards,
            account_id=account_id,
            status=status,
            type=type,
            kind=kind,
            user_id=user_id,
            is_agent_card=is_agent_card,
            is_single_use=is_single_use,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    def iter(
        self,
        *,
        account_id: Optional[List[StrictStr]] = None,
        status: Optional[List[StrictStr]] = None,
        type: Optional[List[StrictStr]] = None,
        kind: Optional[List[StrictStr]] = None,
        user_id: Optional[StrictStr] = None,
        is_agent_card: Optional[StrictBool] = None,
        is_single_use: Optional[StrictBool] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> AsyncIterator[_models.Card]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_cards,
            account_id=account_id,
            status=status,
            type=type,
            kind=kind,
            user_id=user_id,
            is_agent_card=is_agent_card,
            is_single_use=is_single_use,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    async def reveal(
        self,
        card_id: UUID,
    ) -> CardRevealResponse:
        """Get a card's full number and security code. Never log the result."""
        return await self._call(
            _reveal_card_pan,
            card_id=card_id,
        )

    @checked
    async def unfreeze(
        self,
        card_id: UUID,
    ) -> Card:
        """Unfreeze a card."""
        return await self._call(
            _unfreeze_card,
            card_id=card_id,
        )

    @checked
    async def update(
        self,
        card_id: UUID,
        body: Optional[Union[UpdateCardRequest, Mapping[str, Any]]] = None,
    ) -> Card:
        """Update a card."""
        return await self._call(
            _update_card,
            card_id=card_id,
            _body=body,
        )
