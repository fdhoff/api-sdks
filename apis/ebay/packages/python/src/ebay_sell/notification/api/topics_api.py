# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.notification import models as _models
from ebay_sell.notification.models.topic import Topic
from ebay_sell.notification.models.topic_search_response import TopicSearchResponse

_get_topic: Operation[Topic] = Operation(
    id="getTopic",
    method="GET",
    path="/commerce/notification/v1/topic/{topic_id}",
    resource="topics",
    name="get",
    params=(Param("topic_id", "topic_id", "path"),),
    response=Topic,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_topics: Operation[TopicSearchResponse] = Operation(
    id="getTopics",
    method="GET",
    path="/commerce/notification/v1/topic",
    resource="topics",
    name="list",
    params=(
        Param("continuation_token", "continuation_token", "query"),
        Param("limit", "limit", "query"),
    ),
    response=TopicSearchResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Topic,
    paging=NextLink(
        items="topics",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (
    _get_topic,
    _get_topics,
)


class TopicsApi(Resource):
    @checked
    def get(
        self,
        topic_id: StrictStr,
    ) -> Topic:
        """Get one notification topic."""
        return self._call(
            _get_topic,
            topic_id=topic_id,
        )

    @checked
    def list(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> TopicSearchResponse:
        """List one page of notification topics."""
        return self._call(
            _get_topics,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> Iterator[_models.Topic]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_topics,
            continuation_token=continuation_token,
            limit=limit,
        )


class AsyncTopicsApi(AsyncResource):
    @checked
    async def get(
        self,
        topic_id: StrictStr,
    ) -> Topic:
        """Get one notification topic."""
        return await self._call(
            _get_topic,
            topic_id=topic_id,
        )

    @checked
    async def list(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> TopicSearchResponse:
        """List one page of notification topics."""
        return await self._call(
            _get_topics,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Topic]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_topics,
            continuation_token=continuation_token,
            limit=limit,
        )
