# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, FileInput, Operation, Param, Resource, Scheme, checked
from ebay_sell.media.models.create_image_from_url_request import CreateImageFromUrlRequest
from ebay_sell.media.models.image_response import ImageResponse

_create_image_from_file: Operation[ImageResponse] = Operation(
    id="createImageFromFile",
    method="POST",
    path="/commerce/media/v1_beta/image/create_image_from_file",
    resource="images",
    name="upload",
    params=(Param("image", "image", "form"),),
    response=ImageResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="apim",
)
_create_image_from_url: Operation[ImageResponse] = Operation(
    id="createImageFromUrl",
    method="POST",
    path="/commerce/media/v1_beta/image/create_image_from_url",
    resource="images",
    name="create_from_url",
    params=(),
    response=ImageResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="apim",
)
_get_image: Operation[ImageResponse] = Operation(
    id="getImage",
    method="GET",
    path="/commerce/media/v1_beta/image/{image_id}",
    resource="images",
    name="get",
    params=(Param("image_id", "image_id", "path"),),
    response=ImageResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="apim",
)

OPERATIONS = (
    _create_image_from_file,
    _create_image_from_url,
    _get_image,
)


class ImagesApi(Resource):
    @checked
    def upload(
        self,
        *,
        image: FileInput,
    ) -> ImageResponse:
        """Upload an image file to eBay's picture service."""
        return self._call(
            _create_image_from_file,
            image=image,
        )

    @checked
    def create_from_url(
        self,
        body: Union[CreateImageFromUrlRequest, Mapping[str, Any]],
    ) -> ImageResponse:
        """Create an image on eBay's picture service from a public URL."""
        return self._call(
            _create_image_from_url,
            _body=body,
        )

    @checked
    def get(
        self,
        image_id: StrictStr,
    ) -> ImageResponse:
        """Get one image."""
        return self._call(
            _get_image,
            image_id=image_id,
        )


class AsyncImagesApi(AsyncResource):
    @checked
    async def upload(
        self,
        *,
        image: FileInput,
    ) -> ImageResponse:
        """Upload an image file to eBay's picture service."""
        return await self._call(
            _create_image_from_file,
            image=image,
        )

    @checked
    async def create_from_url(
        self,
        body: Union[CreateImageFromUrlRequest, Mapping[str, Any]],
    ) -> ImageResponse:
        """Create an image on eBay's picture service from a public URL."""
        return await self._call(
            _create_image_from_url,
            _body=body,
        )

    @checked
    async def get(
        self,
        image_id: StrictStr,
    ) -> ImageResponse:
        """Get one image."""
        return await self._call(
            _get_image,
            image_id=image_id,
        )
