# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.media.models.create_video_request import CreateVideoRequest
from ebay_sell.media.models.video import Video

_create_video: Operation[None] = Operation(
    id="createVideo",
    method="POST",
    path="/commerce/media/v1_beta/video",
    resource="videos",
    name="create",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="apim",
)
_get_video: Operation[Video] = Operation(
    id="getVideo",
    method="GET",
    path="/commerce/media/v1_beta/video/{video_id}",
    resource="videos",
    name="get",
    params=(Param("video_id", "video_id", "path"),),
    response=Video,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="apim",
)

OPERATIONS = (
    _create_video,
    _get_video,
)


class VideosApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[CreateVideoRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Create a video resource to upload content to."""
        return self._call(
            _create_video,
            _body=body,
        )

    @checked
    def get(
        self,
        video_id: StrictStr,
    ) -> Video:
        """Get one video and its status."""
        return self._call(
            _get_video,
            video_id=video_id,
        )


class AsyncVideosApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[CreateVideoRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Create a video resource to upload content to."""
        return await self._call(
            _create_video,
            _body=body,
        )

    @checked
    async def get(
        self,
        video_id: StrictStr,
    ) -> Video:
        """Get one video and its status."""
        return await self._call(
            _get_video,
            video_id=video_id,
        )
