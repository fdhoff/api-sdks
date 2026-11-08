# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, FileInput, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.fulfillment import models as _models
from ebay_sell.fulfillment.models.accept_payment_dispute_request import AcceptPaymentDisputeRequest
from ebay_sell.fulfillment.models.add_evidence_payment_dispute_request import AddEvidencePaymentDisputeRequest
from ebay_sell.fulfillment.models.add_evidence_payment_dispute_response import AddEvidencePaymentDisputeResponse
from ebay_sell.fulfillment.models.contest_payment_dispute_request import ContestPaymentDisputeRequest
from ebay_sell.fulfillment.models.dispute_summary_response import DisputeSummaryResponse
from ebay_sell.fulfillment.models.file_evidence import FileEvidence
from ebay_sell.fulfillment.models.payment_dispute import PaymentDispute
from ebay_sell.fulfillment.models.payment_dispute_activity_history import PaymentDisputeActivityHistory
from ebay_sell.fulfillment.models.update_evidence_payment_dispute_request import UpdateEvidencePaymentDisputeRequest

_accept_payment_dispute: Operation[None] = Operation(
    id="acceptPaymentDispute",
    method="POST",
    path="/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/accept",
    resource="payment_disputes",
    name="accept",
    params=(Param("payment_dispute_id", "payment_dispute_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)
_add_evidence: Operation[AddEvidencePaymentDisputeResponse] = Operation(
    id="addEvidence",
    method="POST",
    path="/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/add_evidence",
    resource="payment_disputes",
    name="add_evidence",
    params=(Param("payment_dispute_id", "payment_dispute_id", "path"),),
    response=AddEvidencePaymentDisputeResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)
_contest_payment_dispute: Operation[None] = Operation(
    id="contestPaymentDispute",
    method="POST",
    path="/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/contest",
    resource="payment_disputes",
    name="contest",
    params=(Param("payment_dispute_id", "payment_dispute_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)
_get_activities: Operation[PaymentDisputeActivityHistory] = Operation(
    id="getActivities",
    method="GET",
    path="/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/activity",
    resource="payment_disputes",
    name="list_activities",
    params=(Param("payment_dispute_id", "payment_dispute_id", "path"),),
    response=PaymentDisputeActivityHistory,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)
_get_payment_dispute: Operation[PaymentDispute] = Operation(
    id="getPaymentDispute",
    method="GET",
    path="/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}",
    resource="payment_disputes",
    name="get",
    params=(Param("payment_dispute_id", "payment_dispute_id", "path"),),
    response=PaymentDispute,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)
_get_payment_dispute_summaries: Operation[DisputeSummaryResponse] = Operation(
    id="getPaymentDisputeSummaries",
    method="GET",
    path="/sell/fulfillment/v1/payment_dispute_summary",
    resource="payment_disputes",
    name="list_summaries",
    params=(
        Param("order_id", "order_id", "query"),
        Param("buyer_username", "buyer_username", "query"),
        Param("open_date_from", "open_date_from", "query"),
        Param("open_date_to", "open_date_to", "query"),
        Param("payment_dispute_status", "payment_dispute_status", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=DisputeSummaryResponse,
    returns_json=True,
    iterator="iter_summaries",
    item=_models.PaymentDisputeSummary,
    paging=NextLink(
        items="paymentDisputeSummaries",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)
_update_evidence: Operation[None] = Operation(
    id="updateEvidence",
    method="POST",
    path="/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/update_evidence",
    resource="payment_disputes",
    name="update_evidence",
    params=(Param("payment_dispute_id", "payment_dispute_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)
_upload_evidence_file: Operation[FileEvidence] = Operation(
    id="uploadEvidenceFile",
    method="POST",
    path="/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/upload_evidence_file",
    resource="payment_disputes",
    name="upload_evidence_file",
    params=(
        Param("payment_dispute_id", "payment_dispute_id", "path"),
        Param("file", "file", "form"),
    ),
    response=FileEvidence,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.payment.dispute",)),),),
    host="apiz",
)

OPERATIONS = (
    _accept_payment_dispute,
    _add_evidence,
    _contest_payment_dispute,
    _get_activities,
    _get_payment_dispute,
    _get_payment_dispute_summaries,
    _update_evidence,
    _upload_evidence_file,
)


class PaymentDisputesApi(Resource):
    @checked
    def accept(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[AcceptPaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Accept a payment dispute."""
        return self._call(
            _accept_payment_dispute,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    def add_evidence(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[AddEvidencePaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> AddEvidencePaymentDisputeResponse:
        """Add a set of uploaded evidence files to a payment dispute."""
        return self._call(
            _add_evidence,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    def contest(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[ContestPaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Contest a payment dispute."""
        return self._call(
            _contest_payment_dispute,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    def list_activities(
        self,
        payment_dispute_id: StrictStr,
    ) -> PaymentDisputeActivityHistory:
        """List the activity on a payment dispute."""
        return self._call(
            _get_activities,
            payment_dispute_id=payment_dispute_id,
        )

    @checked
    def get(
        self,
        payment_dispute_id: StrictStr,
    ) -> PaymentDispute:
        """Get one payment dispute."""
        return self._call(
            _get_payment_dispute,
            payment_dispute_id=payment_dispute_id,
        )

    @checked
    def list_summaries(
        self,
        *,
        order_id: Optional[StrictStr] = None,
        buyer_username: Optional[StrictStr] = None,
        open_date_from: Optional[StrictStr] = None,
        open_date_to: Optional[StrictStr] = None,
        payment_dispute_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> DisputeSummaryResponse:
        """List one page of the seller's payment disputes."""
        return self._call(
            _get_payment_dispute_summaries,
            order_id=order_id,
            buyer_username=buyer_username,
            open_date_from=open_date_from,
            open_date_to=open_date_to,
            payment_dispute_status=payment_dispute_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_summaries(
        self,
        *,
        order_id: Optional[StrictStr] = None,
        buyer_username: Optional[StrictStr] = None,
        open_date_from: Optional[StrictStr] = None,
        open_date_to: Optional[StrictStr] = None,
        payment_dispute_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.PaymentDisputeSummary]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_payment_dispute_summaries,
            order_id=order_id,
            buyer_username=buyer_username,
            open_date_from=open_date_from,
            open_date_to=open_date_to,
            payment_dispute_status=payment_dispute_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def update_evidence(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[UpdateEvidencePaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Add uploaded files to an existing set of evidence."""
        return self._call(
            _update_evidence,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    def upload_evidence_file(
        self,
        payment_dispute_id: StrictStr,
        *,
        file: FileInput,
    ) -> FileEvidence:
        """Upload a file to use as evidence in a payment dispute."""
        return self._call(
            _upload_evidence_file,
            payment_dispute_id=payment_dispute_id,
            file=file,
        )


class AsyncPaymentDisputesApi(AsyncResource):
    @checked
    async def accept(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[AcceptPaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Accept a payment dispute."""
        return await self._call(
            _accept_payment_dispute,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    async def add_evidence(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[AddEvidencePaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> AddEvidencePaymentDisputeResponse:
        """Add a set of uploaded evidence files to a payment dispute."""
        return await self._call(
            _add_evidence,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    async def contest(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[ContestPaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Contest a payment dispute."""
        return await self._call(
            _contest_payment_dispute,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    async def list_activities(
        self,
        payment_dispute_id: StrictStr,
    ) -> PaymentDisputeActivityHistory:
        """List the activity on a payment dispute."""
        return await self._call(
            _get_activities,
            payment_dispute_id=payment_dispute_id,
        )

    @checked
    async def get(
        self,
        payment_dispute_id: StrictStr,
    ) -> PaymentDispute:
        """Get one payment dispute."""
        return await self._call(
            _get_payment_dispute,
            payment_dispute_id=payment_dispute_id,
        )

    @checked
    async def list_summaries(
        self,
        *,
        order_id: Optional[StrictStr] = None,
        buyer_username: Optional[StrictStr] = None,
        open_date_from: Optional[StrictStr] = None,
        open_date_to: Optional[StrictStr] = None,
        payment_dispute_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> DisputeSummaryResponse:
        """List one page of the seller's payment disputes."""
        return await self._call(
            _get_payment_dispute_summaries,
            order_id=order_id,
            buyer_username=buyer_username,
            open_date_from=open_date_from,
            open_date_to=open_date_to,
            payment_dispute_status=payment_dispute_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_summaries(
        self,
        *,
        order_id: Optional[StrictStr] = None,
        buyer_username: Optional[StrictStr] = None,
        open_date_from: Optional[StrictStr] = None,
        open_date_to: Optional[StrictStr] = None,
        payment_dispute_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.PaymentDisputeSummary]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_payment_dispute_summaries,
            order_id=order_id,
            buyer_username=buyer_username,
            open_date_from=open_date_from,
            open_date_to=open_date_to,
            payment_dispute_status=payment_dispute_status,
            limit=limit,
            offset=offset,
        )

    @checked
    async def update_evidence(
        self,
        payment_dispute_id: StrictStr,
        body: Optional[Union[UpdateEvidencePaymentDisputeRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Add uploaded files to an existing set of evidence."""
        return await self._call(
            _update_evidence,
            payment_dispute_id=payment_dispute_id,
            _body=body,
        )

    @checked
    async def upload_evidence_file(
        self,
        payment_dispute_id: StrictStr,
        *,
        file: FileInput,
    ) -> FileEvidence:
        """Upload a file to use as evidence in a payment dispute."""
        return await self._call(
            _upload_evidence_file,
            payment_dispute_id=payment_dispute_id,
            file=file,
        )
