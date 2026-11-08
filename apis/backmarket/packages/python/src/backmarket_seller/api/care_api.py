# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictInt, StrictStr

from backmarket_seller import models as _models
from backmarket_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource, checked
from backmarket_seller.models.get_care_folder_details_response import GetCareFolderDetailsResponse
from backmarket_seller.models.get_care_folder_list_response import GetCareFolderListResponse
from backmarket_seller.models.post_item_transfer_create_request import PostItemTransferCreateRequest
from backmarket_seller.models.post_message_response import PostMessageResponse
from backmarket_seller.models.post_note_request import PostNoteRequest
from backmarket_seller.models.post_note_response import PostNoteResponse
from backmarket_seller.models.post_refund_create_request import PostRefundCreateRequest

_get_care_folder_details: Operation[GetCareFolderDetailsResponse] = Operation(
    id="getCareFolderDetails",
    method="GET",
    path="/ws/sav/{careFolderId}",
    resource="care",
    name="get_folder",
    params=(Param("careFolderId", "care_folder_id", "path"),),
    response=GetCareFolderDetailsResponse,
    returns_json=True,
)
_get_care_folder_list: Operation[GetCareFolderListResponse] = Operation(
    id="getCareFolderList",
    method="GET",
    path="/ws/sav",
    resource="care",
    name="list_folders",
    params=(
        Param("last_id", "last_id", "query"),
        Param("state", "state", "query"),
        Param("orderline", "orderline", "query"),
        Param("last_modification_date", "last_modification_date", "query"),
        Param("last_message_date", "last_message_date", "query"),
        Param("page", "page", "query"),
    ),
    response=GetCareFolderListResponse,
    returns_json=True,
    iterator="iter_folders",
    item=_models.CareFolder,
)
_post_item_transfer: Operation[None] = Operation(
    id="postItemTransfer",
    method="POST",
    path="/ws/sav/{careFolderId}/item-transfer",
    resource="care",
    name="transfer_item",
    params=(Param("careFolderId", "care_folder_id", "path"),),
    response=None,
)
_post_message: Operation[PostMessageResponse] = Operation(
    id="postMessage",
    method="POST",
    path="/ws/sav/{careFolderId}/msg",
    resource="care",
    name="send_message",
    params=(
        Param("careFolderId", "care_folder_id", "path"),
        Param("attachment", "attachment", "form"),
        Param("message", "message", "form"),
    ),
    response=PostMessageResponse,
    returns_json=True,
)
_post_note: Operation[PostNoteResponse] = Operation(
    id="postNote",
    method="POST",
    path="/ws/sav/{careFolderId}/note",
    resource="care",
    name="add_note",
    params=(Param("careFolderId", "care_folder_id", "path"),),
    response=PostNoteResponse,
    returns_json=True,
)
_post_problem: Operation[None] = Operation(
    id="postProblem",
    method="POST",
    path="/ws/sav/{careFolderId}/problem",
    resource="care",
    name="report_problem",
    params=(
        Param("careFolderId", "care_folder_id", "path"),
        Param("problem_type", "problem_type", "form"),
        Param("message", "message", "form"),
        Param("attachment", "attachment", "form"),
    ),
    response=None,
)
_post_refund_create: Operation[str] = Operation(
    id="postRefundCreate",
    method="POST",
    path="/ws/sav/refund",
    resource="care",
    name="create_refund",
    params=(),
    response=str,
)

OPERATIONS = (
    _get_care_folder_details,
    _get_care_folder_list,
    _post_item_transfer,
    _post_message,
    _post_note,
    _post_problem,
    _post_refund_create,
)


class CareApi(Resource):
    @checked
    def get_folder(
        self,
        care_folder_id: StrictInt,
    ) -> GetCareFolderDetailsResponse:
        """Get one care folder."""
        return self._call(
            _get_care_folder_details,
            care_folder_id=care_folder_id,
        )

    @checked
    def list_folders(
        self,
        *,
        last_id: Optional[StrictInt] = None,
        state: Optional[StrictInt] = None,
        orderline: Optional[StrictInt] = None,
        last_modification_date: Optional[StrictStr] = None,
        last_message_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> GetCareFolderListResponse:
        """List one page of care folders."""
        return self._call(
            _get_care_folder_list,
            last_id=last_id,
            state=state,
            orderline=orderline,
            last_modification_date=last_modification_date,
            last_message_date=last_message_date,
            page=page,
        )

    @checked
    def iter_folders(
        self,
        *,
        last_id: Optional[StrictInt] = None,
        state: Optional[StrictInt] = None,
        orderline: Optional[StrictInt] = None,
        last_modification_date: Optional[StrictStr] = None,
        last_message_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> Iterator[_models.CareFolder]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_care_folder_list,
            last_id=last_id,
            state=state,
            orderline=orderline,
            last_modification_date=last_modification_date,
            last_message_date=last_message_date,
            page=page,
        )

    @checked
    def transfer_item(
        self,
        care_folder_id: StrictInt,
        body: Union[PostItemTransferCreateRequest, Mapping[str, Any]],
    ) -> None:
        """Transfer an item on a care folder."""
        return self._call(
            _post_item_transfer,
            care_folder_id=care_folder_id,
            _body=body,
        )

    @checked
    def send_message(
        self,
        care_folder_id: StrictInt,
        *,
        message: StrictStr,
        attachment: Optional[List[FileInput]] = None,
    ) -> PostMessageResponse:
        """Send a message on a care folder."""
        return self._call(
            _post_message,
            care_folder_id=care_folder_id,
            attachment=attachment,
            message=message,
        )

    @checked
    def add_note(
        self,
        care_folder_id: StrictInt,
        body: Union[PostNoteRequest, Mapping[str, Any]],
    ) -> PostNoteResponse:
        """Add a note to a care folder."""
        return self._call(
            _post_note,
            care_folder_id=care_folder_id,
            _body=body,
        )

    @checked
    def report_problem(
        self,
        care_folder_id: StrictInt,
        *,
        problem_type: Optional[StrictStr] = None,
        message: Optional[StrictStr] = None,
        attachment: Optional[List[FileInput]] = None,
    ) -> None:
        """Report a problem on a care folder."""
        return self._call(
            _post_problem,
            care_folder_id=care_folder_id,
            problem_type=problem_type,
            message=message,
            attachment=attachment,
        )

    @checked
    def create_refund(
        self,
        body: Optional[Union[PostRefundCreateRequest, Mapping[str, Any]]] = None,
    ) -> str:
        """Create a refund. Never retried on failure."""
        return self._call(
            _post_refund_create,
            _body=body,
        )


class AsyncCareApi(AsyncResource):
    @checked
    async def get_folder(
        self,
        care_folder_id: StrictInt,
    ) -> GetCareFolderDetailsResponse:
        """Get one care folder."""
        return await self._call(
            _get_care_folder_details,
            care_folder_id=care_folder_id,
        )

    @checked
    async def list_folders(
        self,
        *,
        last_id: Optional[StrictInt] = None,
        state: Optional[StrictInt] = None,
        orderline: Optional[StrictInt] = None,
        last_modification_date: Optional[StrictStr] = None,
        last_message_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> GetCareFolderListResponse:
        """List one page of care folders."""
        return await self._call(
            _get_care_folder_list,
            last_id=last_id,
            state=state,
            orderline=orderline,
            last_modification_date=last_modification_date,
            last_message_date=last_message_date,
            page=page,
        )

    @checked
    def iter_folders(
        self,
        *,
        last_id: Optional[StrictInt] = None,
        state: Optional[StrictInt] = None,
        orderline: Optional[StrictInt] = None,
        last_modification_date: Optional[StrictStr] = None,
        last_message_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.CareFolder]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_care_folder_list,
            last_id=last_id,
            state=state,
            orderline=orderline,
            last_modification_date=last_modification_date,
            last_message_date=last_message_date,
            page=page,
        )

    @checked
    async def transfer_item(
        self,
        care_folder_id: StrictInt,
        body: Union[PostItemTransferCreateRequest, Mapping[str, Any]],
    ) -> None:
        """Transfer an item on a care folder."""
        return await self._call(
            _post_item_transfer,
            care_folder_id=care_folder_id,
            _body=body,
        )

    @checked
    async def send_message(
        self,
        care_folder_id: StrictInt,
        *,
        message: StrictStr,
        attachment: Optional[List[FileInput]] = None,
    ) -> PostMessageResponse:
        """Send a message on a care folder."""
        return await self._call(
            _post_message,
            care_folder_id=care_folder_id,
            attachment=attachment,
            message=message,
        )

    @checked
    async def add_note(
        self,
        care_folder_id: StrictInt,
        body: Union[PostNoteRequest, Mapping[str, Any]],
    ) -> PostNoteResponse:
        """Add a note to a care folder."""
        return await self._call(
            _post_note,
            care_folder_id=care_folder_id,
            _body=body,
        )

    @checked
    async def report_problem(
        self,
        care_folder_id: StrictInt,
        *,
        problem_type: Optional[StrictStr] = None,
        message: Optional[StrictStr] = None,
        attachment: Optional[List[FileInput]] = None,
    ) -> None:
        """Report a problem on a care folder."""
        return await self._call(
            _post_problem,
            care_folder_id=care_folder_id,
            problem_type=problem_type,
            message=message,
            attachment=attachment,
        )

    @checked
    async def create_refund(
        self,
        body: Optional[Union[PostRefundCreateRequest, Mapping[str, Any]]] = None,
    ) -> str:
        """Create a refund. Never retried on failure."""
        return await self._call(
            _post_refund_create,
            _body=body,
        )
