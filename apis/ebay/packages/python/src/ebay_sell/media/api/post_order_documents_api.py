# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, FileInput, Operation, Param, Resource, Scheme, checked

_remove_post_order_document: Operation[None] = Operation(
    id="removePostOrderDocument",
    method="DELETE",
    path="/commerce/media/v1_beta/post_order/document/{document_id}",
    resource="post_order_documents",
    name="delete",
    params=(Param("document_id", "document_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.post_order.document",)),),),
    host="apiz",
)
_upload_post_order_document: Operation[None] = Operation(
    id="uploadPostOrderDocument",
    method="POST",
    path="/commerce/media/v1_beta/post_order/document",
    resource="post_order_documents",
    name="upload",
    params=(
        Param("file", "file", "form"),
        Param("documentUsageType", "document_usage_type", "form"),
        Param("entityType", "entity_type", "form"),
        Param("entityId", "entity_id", "form"),
    ),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.post_order.document",)),),),
    host="apiz",
)

OPERATIONS = (
    _remove_post_order_document,
    _upload_post_order_document,
)


class PostOrderDocumentsApi(Resource):
    @checked
    def delete(
        self,
        document_id: StrictStr,
    ) -> None:
        """Delete a post-order document."""
        return self._call(
            _remove_post_order_document,
            document_id=document_id,
        )

    @checked
    def upload(
        self,
        *,
        file: FileInput,
        document_usage_type: StrictStr,
        entity_type: StrictStr,
        entity_id: StrictStr,
    ) -> None:
        """Upload a document for a return"""
        return self._call(
            _upload_post_order_document,
            file=file,
            document_usage_type=document_usage_type,
            entity_type=entity_type,
            entity_id=entity_id,
        )


class AsyncPostOrderDocumentsApi(AsyncResource):
    @checked
    async def delete(
        self,
        document_id: StrictStr,
    ) -> None:
        """Delete a post-order document."""
        return await self._call(
            _remove_post_order_document,
            document_id=document_id,
        )

    @checked
    async def upload(
        self,
        *,
        file: FileInput,
        document_usage_type: StrictStr,
        entity_type: StrictStr,
        entity_id: StrictStr,
    ) -> None:
        """Upload a document for a return"""
        return await self._call(
            _upload_post_order_document,
            file=file,
            document_usage_type=document_usage_type,
            entity_type=entity_type,
            entity_id=entity_id,
        )
