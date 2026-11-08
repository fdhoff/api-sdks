# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.media.api import documents_api, images_api, post_order_documents_api, videos_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        documents_api.OPERATIONS,
        images_api.OPERATIONS,
        post_order_documents_api.OPERATIONS,
        videos_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.documents = documents_api.DocumentsApi(transport)
        self.images = images_api.ImagesApi(transport)
        self.post_order_documents = post_order_documents_api.PostOrderDocumentsApi(transport)
        self.videos = videos_api.VideosApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.documents = documents_api.AsyncDocumentsApi(transport)
        self.images = images_api.AsyncImagesApi(transport)
        self.post_order_documents = post_order_documents_api.AsyncPostOrderDocumentsApi(transport)
        self.videos = videos_api.AsyncVideosApi(transport)
