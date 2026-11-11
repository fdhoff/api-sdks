# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from mirakl_seller import models as _models
from mirakl_seller._runtime import (
    AsyncDownload,
    AsyncResource,
    Cursor,
    Download,
    FileInput,
    Job,
    Offset,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mirakl_seller.models.dr11_response200 import DR11Response200
from mirakl_seller.models.dr12_response200 import DR12Response200
from mirakl_seller.models.dr74_request_multipart_form_data_documents_input import (
    DR74RequestMultipartFormDataDocumentsInput,
)
from mirakl_seller.models.dr74_response200 import DR74Response200
from mirakl_seller.models.dr75_request import DR75Request
from mirakl_seller.models.dr75_response200 import DR75Response200
from mirakl_seller.models.dr76_request import DR76Request
from mirakl_seller.models.dr76_response200 import DR76Response200
from mirakl_seller.models.iv01_response200 import IV01Response200
from mirakl_seller.models.sbc11_response200 import SBC11Response200
from mirakl_seller.models.tl02_response200 import TL02Response200
from mirakl_seller.models.tl03_request import TL03Request
from mirakl_seller.models.tl03_response200 import TL03Response200
from mirakl_seller.models.tl04_response200 import TL04Response200

_d_r11: Operation[DR11Response200] = Operation(
    id="DR11",
    method="GET",
    path="/api/document-request/requests",
    resource="accounting",
    name="list_document_requests",
    params=(
        Param("id", "id", "query"),
        Param("document_number", "document_number", "query"),
        Param("date_created_from", "date_created_from", "query"),
        Param("date_created_to", "date_created_to", "query"),
        Param("last_updated_from", "last_updated_from", "query"),
        Param("last_updated_to", "last_updated_to", "query"),
        Param("issue_date_from", "issue_date_from", "query"),
        Param("issue_date_to", "issue_date_to", "query"),
        Param("state", "state", "query"),
        Param("type", "type", "query"),
        Param("issuer_type", "issuer_type", "query"),
        Param("entity_id", "entity_id", "query"),
        Param("entity_type", "entity_type", "query"),
        Param("shop_billing_cycle_id", "shop_billing_cycle_id", "query"),
        Param("shop_billing_cycle_from", "shop_billing_cycle_from", "query"),
        Param("shop_billing_cycle_to", "shop_billing_cycle_to", "query"),
        Param("payment_state", "payment_state", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=DR11Response200,
    returns_json=True,
    iterator="iter_document_requests",
    item=_models.DR11Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_REQUEST_READ",
                    "ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_d_r12: Operation[DR12Response200] = Operation(
    id="DR12",
    method="GET",
    path="/api/document-request/{document_request_id}/lines",
    resource="accounting",
    name="list_document_request_lines",
    params=(
        Param("document_request_id", "document_request_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=DR12Response200,
    returns_json=True,
    iterator="iter_document_request_lines",
    item=_models.DR12Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_REQUEST_READ",
                    "ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_d_r73: Operation[None] = Operation(
    id="DR73",
    method="GET",
    path="/api/document-request/documents/download",
    resource="accounting",
    name="download_documents",
    params=(
        Param("document_request_id", "document_request_id", "query"),
        Param("document_id", "document_id", "query"),
        Param("document_format", "document_format", "query"),
        Param("entity_id", "entity_id", "query"),
        Param("entity_type", "entity_type", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_READ",
                    "ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_d_r74: Operation[DR74Response200] = Operation(
    id="DR74",
    method="POST",
    path="/api/document-request/documents/upload",
    resource="accounting",
    name="upload_documents",
    params=(
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("documents_input", "documents_input", "form"),
        Param("files", "files", "form"),
    ),
    response=DR74Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_WRITE",
                ),
            ),
        ),
    ),
)
_d_r75: Operation[DR75Response200] = Operation(
    id="DR75",
    method="POST",
    path="/api/document-request/documents/confirm-issuance",
    resource="accounting",
    name="confirm_issuance",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=DR75Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_WRITE",
                ),
            ),
        ),
    ),
)
_d_r76: Operation[DR76Response200] = Operation(
    id="DR76",
    method="POST",
    path="/api/document-request/documents/generate",
    resource="accounting",
    name="generate_documents",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=DR76Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_WRITE",
                ),
            ),
        ),
    ),
)
_i_v01: Operation[IV01Response200] = Operation(
    id="IV01",
    method="GET",
    path="/api/invoices",
    resource="accounting",
    name="list_invoices",
    params=(
        Param("currency", "currency", "query"),
        Param("end_date", "end_date", "query"),
        Param("invoice_id", "invoice_id", "query"),
        Param("issuing_user_types", "issuing_user_types", "query"),
        Param("pay_out_psp_codes", "pay_out_psp_codes", "query"),
        Param("payment_status", "payment_status", "query"),
        Param("seller_billing_cycle_id", "seller_billing_cycle_id", "query"),
        Param("start_date", "start_date", "query"),
        Param("type", "type", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("max", "max", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=IV01Response200,
    returns_json=True,
    iterator="iter_invoices",
    item=_models.IV01Response200Invoices,
    paging=Offset(items="invoices", total="total_count", offset="offset"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ",
                    "ROLE_PARTNER_OWN_ACCOUNTING_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_i_v02: Operation[None] = Operation(
    id="IV02",
    method="GET",
    path="/api/invoices/{accounting_document_id}",
    resource="accounting",
    name="download_invoice",
    params=(
        Param("accounting_document_id", "accounting_document_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ",
                    "ROLE_PARTNER_OWN_ACCOUNTING_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_s_bc11: Operation[SBC11Response200] = Operation(
    id="SBC11",
    method="GET",
    path="/api/seller-billing-cycles",
    resource="accounting",
    name="list_billing_cycles",
    params=(
        Param("currency", "currency", "query"),
        Param("end_date", "end_date", "query"),
        Param("id", "id", "query"),
        Param("pay_out_psp_code", "pay_out_psp_code", "query"),
        Param("pay_out_state", "pay_out_state", "query"),
        Param("start_date", "start_date", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=SBC11Response200,
    returns_json=True,
    iterator="iter_billing_cycles",
    item=_models.SBC11Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SELLER_BILLING_CYCLE_READ",
                    "ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_t_l02: Operation[TL02Response200] = Operation(
    id="TL02",
    method="GET",
    path="/api/sellerpayment/transactions_logs",
    resource="accounting",
    name="list_transactions",
    params=(
        Param("seller_billing_cycle_id", "seller_billing_cycle_id", "query"),
        Param("date_created_from", "date_created_from", "query"),
        Param("date_created_to", "date_created_to", "query"),
        Param("transaction_date_from", "transaction_date_from", "query"),
        Param("transaction_date_to", "transaction_date_to", "query"),
        Param("last_updated_from", "last_updated_from", "query"),
        Param("payment_state", "payment_state", "query"),
        Param("transaction_type", "transaction_type", "query"),
        Param("accounting_document_number", "accounting_document_number", "query"),
        Param("order_id", "order_id", "query"),
        Param("order_line_id", "order_line_id", "query"),
        Param("order_reference_for_customer", "order_reference_for_customer", "query"),
        Param("order_reference_for_seller", "order_reference_for_seller", "query"),
        Param("accounting_document_id", "accounting_document_id", "query"),
        Param("shop_model", "shop_model", "query"),
        Param("pay_out_psp_codes", "pay_out_psp_codes", "query"),
        Param("other_reference", "other_reference", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=TL02Response200,
    returns_json=True,
    iterator="iter_transactions",
    item=_models.TL02Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ACCOUNTANCY",
                    "ROLE_PARTNER_TRANSACTION_LOG_READ",
                ),
            ),
        ),
    ),
)
_t_l03: Operation[TL03Response200] = Operation(
    id="TL03",
    method="POST",
    path="/api/sellerpayment/transactions_logs/async",
    resource="accounting",
    name="export_transactions",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=TL03Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ACCOUNTANCY",
                    "ROLE_PARTNER_TRANSACTION_LOG_READ",
                ),
            ),
        ),
    ),
)
_t_l04: Operation[TL04Response200] = Operation(
    id="TL04",
    method="GET",
    path="/api/sellerpayment/transactions_logs/async/status/{tracking_id}",
    resource="accounting",
    name="get_transaction_export",
    params=(
        Param("tracking_id", "tracking_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=TL04Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ACCOUNTANCY",
                    "ROLE_PARTNER_TRANSACTION_LOG_READ",
                ),
            ),
        ),
    ),
    job=Job(
        state="status",
        done=("COMPLETED",),
        failed=(
            "FAILED",
            "CANCELED",
        ),
    ),
)

OPERATIONS = (
    _d_r11,
    _d_r12,
    _d_r73,
    _d_r74,
    _d_r75,
    _d_r76,
    _i_v01,
    _i_v02,
    _s_bc11,
    _t_l02,
    _t_l03,
    _t_l04,
)


class AccountingApi(Resource):
    @checked
    def list_document_requests(
        self,
        *,
        id: Optional[StrictStr] = None,
        document_number: Optional[StrictStr] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        issue_date_from: Optional[datetime] = None,
        issue_date_to: Optional[datetime] = None,
        state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        issuer_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_billing_cycle_id: Optional[StrictStr] = None,
        shop_billing_cycle_from: Optional[datetime] = None,
        shop_billing_cycle_to: Optional[datetime] = None,
        payment_state: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> DR11Response200:
        """List one page of accounting document requests (DR11)."""
        return self._call(
            _d_r11,
            id=id,
            document_number=document_number,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            issue_date_from=issue_date_from,
            issue_date_to=issue_date_to,
            state=state,
            type=type,
            issuer_type=issuer_type,
            entity_id=entity_id,
            entity_type=entity_type,
            shop_billing_cycle_id=shop_billing_cycle_id,
            shop_billing_cycle_from=shop_billing_cycle_from,
            shop_billing_cycle_to=shop_billing_cycle_to,
            payment_state=payment_state,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_document_requests(
        self,
        *,
        id: Optional[StrictStr] = None,
        document_number: Optional[StrictStr] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        issue_date_from: Optional[datetime] = None,
        issue_date_to: Optional[datetime] = None,
        state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        issuer_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_billing_cycle_id: Optional[StrictStr] = None,
        shop_billing_cycle_from: Optional[datetime] = None,
        shop_billing_cycle_to: Optional[datetime] = None,
        payment_state: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.DR11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _d_r11,
            id=id,
            document_number=document_number,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            issue_date_from=issue_date_from,
            issue_date_to=issue_date_to,
            state=state,
            type=type,
            issuer_type=issuer_type,
            entity_id=entity_id,
            entity_type=entity_type,
            shop_billing_cycle_id=shop_billing_cycle_id,
            shop_billing_cycle_from=shop_billing_cycle_from,
            shop_billing_cycle_to=shop_billing_cycle_to,
            payment_state=payment_state,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def list_document_request_lines(
        self,
        document_request_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> DR12Response200:
        """List one page of a document request's lines (DR12)."""
        return self._call(
            _d_r12,
            document_request_id=document_request_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_document_request_lines(
        self,
        document_request_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.DR12Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _d_r12,
            document_request_id=document_request_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def download_documents(
        self,
        *,
        document_request_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        document_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        document_format: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download accounting documents (DR73). Close the download, or read it in a `with` block."""
        return self._download(
            _d_r73,
            document_request_id=document_request_id,
            document_id=document_id,
            document_format=document_format,
            entity_id=entity_id,
            entity_type=entity_type,
            shop_id=shop_id,
        )

    @checked
    def upload_documents(
        self,
        *,
        documents_input: DR74RequestMultipartFormDataDocumentsInput,
        files: List[FileInput],
        shop_id: Optional[StrictInt] = None,
    ) -> DR74Response200:
        """Upload accounting documents (DR74)."""
        return self._call(
            _d_r74,
            shop_id=shop_id,
            documents_input=documents_input,
            files=files,
        )

    @checked
    def confirm_issuance(
        self,
        body: Optional[Union[DR75Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> DR75Response200:
        """Confirm that accounting documents were issued (DR75)."""
        return self._call(
            _d_r75,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def generate_documents(
        self,
        body: Optional[Union[DR76Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> DR76Response200:
        """Issue accounting documents and generate their files (DR76)."""
        return self._call(
            _d_r76,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list_invoices(
        self,
        *,
        currency: Optional[StrictStr] = None,
        end_date: Optional[datetime] = None,
        invoice_id: Optional[Annotated[List[StrictInt], Field(max_length=100)]] = None,
        issuing_user_types: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        payment_status: Optional[StrictStr] = None,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        start_date: Optional[datetime] = None,
        type: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> IV01Response200:
        """List one page of accounting documents (IV01)."""
        return self._call(
            _i_v01,
            currency=currency,
            end_date=end_date,
            invoice_id=invoice_id,
            issuing_user_types=issuing_user_types,
            pay_out_psp_codes=pay_out_psp_codes,
            payment_status=payment_status,
            seller_billing_cycle_id=seller_billing_cycle_id,
            start_date=start_date,
            type=type,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter_invoices(
        self,
        *,
        currency: Optional[StrictStr] = None,
        end_date: Optional[datetime] = None,
        invoice_id: Optional[Annotated[List[StrictInt], Field(max_length=100)]] = None,
        issuing_user_types: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        payment_status: Optional[StrictStr] = None,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        start_date: Optional[datetime] = None,
        type: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.IV01Response200Invoices]:
        """Iterate every item across all pages."""
        return self._paginate(
            _i_v01,
            currency=currency,
            end_date=end_date,
            invoice_id=invoice_id,
            issuing_user_types=issuing_user_types,
            pay_out_psp_codes=pay_out_psp_codes,
            payment_status=payment_status,
            seller_billing_cycle_id=seller_billing_cycle_id,
            start_date=start_date,
            type=type,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def download_invoice(
        self,
        accounting_document_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download an accounting document (IV02). Close the download, or read it in a `with` block."""
        return self._download(
            _i_v02,
            accounting_document_id=accounting_document_id,
            shop_id=shop_id,
        )

    @checked
    def list_billing_cycles(
        self,
        *,
        currency: Optional[List[StrictStr]] = None,
        end_date: Optional[datetime] = None,
        id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        pay_out_psp_code: Optional[List[StrictStr]] = None,
        pay_out_state: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> SBC11Response200:
        """List one page of seller billing cycles (SBC11)."""
        return self._call(
            _s_bc11,
            currency=currency,
            end_date=end_date,
            id=id,
            pay_out_psp_code=pay_out_psp_code,
            pay_out_state=pay_out_state,
            start_date=start_date,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_billing_cycles(
        self,
        *,
        currency: Optional[List[StrictStr]] = None,
        end_date: Optional[datetime] = None,
        id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        pay_out_psp_code: Optional[List[StrictStr]] = None,
        pay_out_state: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.SBC11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_bc11,
            currency=currency,
            end_date=end_date,
            id=id,
            pay_out_psp_code=pay_out_psp_code,
            pay_out_state=pay_out_state,
            start_date=start_date,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def list_transactions(
        self,
        *,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        transaction_date_from: Optional[datetime] = None,
        transaction_date_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        payment_state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        transaction_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_number: Optional[StrictStr] = None,
        order_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_line_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_customer: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_seller: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_id: Optional[StrictStr] = None,
        shop_model: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        other_reference: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=2000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> TL02Response200:
        """List one page of transaction lines (TL02)."""
        return self._call(
            _t_l02,
            seller_billing_cycle_id=seller_billing_cycle_id,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            transaction_date_from=transaction_date_from,
            transaction_date_to=transaction_date_to,
            last_updated_from=last_updated_from,
            payment_state=payment_state,
            transaction_type=transaction_type,
            accounting_document_number=accounting_document_number,
            order_id=order_id,
            order_line_id=order_line_id,
            order_reference_for_customer=order_reference_for_customer,
            order_reference_for_seller=order_reference_for_seller,
            accounting_document_id=accounting_document_id,
            shop_model=shop_model,
            pay_out_psp_codes=pay_out_psp_codes,
            other_reference=other_reference,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_transactions(
        self,
        *,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        transaction_date_from: Optional[datetime] = None,
        transaction_date_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        payment_state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        transaction_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_number: Optional[StrictStr] = None,
        order_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_line_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_customer: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_seller: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_id: Optional[StrictStr] = None,
        shop_model: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        other_reference: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=2000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.TL02Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _t_l02,
            seller_billing_cycle_id=seller_billing_cycle_id,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            transaction_date_from=transaction_date_from,
            transaction_date_to=transaction_date_to,
            last_updated_from=last_updated_from,
            payment_state=payment_state,
            transaction_type=transaction_type,
            accounting_document_number=accounting_document_number,
            order_id=order_id,
            order_line_id=order_line_id,
            order_reference_for_customer=order_reference_for_customer,
            order_reference_for_seller=order_reference_for_seller,
            accounting_document_id=accounting_document_id,
            shop_model=shop_model,
            pay_out_psp_codes=pay_out_psp_codes,
            other_reference=other_reference,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def export_transactions(
        self,
        body: Optional[Union[TL03Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> TL03Response200:
        """Start an export of transaction lines as JSON files (TL03)."""
        return self._call(
            _t_l03,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def get_transaction_export(
        self,
        tracking_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> TL04Response200:
        """Get the status of a transaction line export (TL04)."""
        return self._call(
            _t_l04,
            tracking_id=tracking_id,
            shop_id=shop_id,
        )

    @checked
    def wait_for_transaction_export(
        self,
        tracking_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> TL04Response200:
        """Poll every `interval` seconds until the job that `export_transactions` started ends, and return its last status,
        done or failed. Pass the `tracking_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass."""
        return self._wait(
            _t_l04,
            interval=interval,
            timeout=timeout,
            tracking_id=tracking_id,
        )


class AsyncAccountingApi(AsyncResource):
    @checked
    async def list_document_requests(
        self,
        *,
        id: Optional[StrictStr] = None,
        document_number: Optional[StrictStr] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        issue_date_from: Optional[datetime] = None,
        issue_date_to: Optional[datetime] = None,
        state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        issuer_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_billing_cycle_id: Optional[StrictStr] = None,
        shop_billing_cycle_from: Optional[datetime] = None,
        shop_billing_cycle_to: Optional[datetime] = None,
        payment_state: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> DR11Response200:
        """List one page of accounting document requests (DR11)."""
        return await self._call(
            _d_r11,
            id=id,
            document_number=document_number,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            issue_date_from=issue_date_from,
            issue_date_to=issue_date_to,
            state=state,
            type=type,
            issuer_type=issuer_type,
            entity_id=entity_id,
            entity_type=entity_type,
            shop_billing_cycle_id=shop_billing_cycle_id,
            shop_billing_cycle_from=shop_billing_cycle_from,
            shop_billing_cycle_to=shop_billing_cycle_to,
            payment_state=payment_state,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_document_requests(
        self,
        *,
        id: Optional[StrictStr] = None,
        document_number: Optional[StrictStr] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        issue_date_from: Optional[datetime] = None,
        issue_date_to: Optional[datetime] = None,
        state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        issuer_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_billing_cycle_id: Optional[StrictStr] = None,
        shop_billing_cycle_from: Optional[datetime] = None,
        shop_billing_cycle_to: Optional[datetime] = None,
        payment_state: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.DR11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _d_r11,
            id=id,
            document_number=document_number,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            issue_date_from=issue_date_from,
            issue_date_to=issue_date_to,
            state=state,
            type=type,
            issuer_type=issuer_type,
            entity_id=entity_id,
            entity_type=entity_type,
            shop_billing_cycle_id=shop_billing_cycle_id,
            shop_billing_cycle_from=shop_billing_cycle_from,
            shop_billing_cycle_to=shop_billing_cycle_to,
            payment_state=payment_state,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def list_document_request_lines(
        self,
        document_request_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> DR12Response200:
        """List one page of a document request's lines (DR12)."""
        return await self._call(
            _d_r12,
            document_request_id=document_request_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_document_request_lines(
        self,
        document_request_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.DR12Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _d_r12,
            document_request_id=document_request_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def download_documents(
        self,
        *,
        document_request_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        document_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        document_format: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        entity_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download accounting documents (DR73). Close the download, or read it in an `async with` block."""
        return await self._download(
            _d_r73,
            document_request_id=document_request_id,
            document_id=document_id,
            document_format=document_format,
            entity_id=entity_id,
            entity_type=entity_type,
            shop_id=shop_id,
        )

    @checked
    async def upload_documents(
        self,
        *,
        documents_input: DR74RequestMultipartFormDataDocumentsInput,
        files: List[FileInput],
        shop_id: Optional[StrictInt] = None,
    ) -> DR74Response200:
        """Upload accounting documents (DR74)."""
        return await self._call(
            _d_r74,
            shop_id=shop_id,
            documents_input=documents_input,
            files=files,
        )

    @checked
    async def confirm_issuance(
        self,
        body: Optional[Union[DR75Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> DR75Response200:
        """Confirm that accounting documents were issued (DR75)."""
        return await self._call(
            _d_r75,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def generate_documents(
        self,
        body: Optional[Union[DR76Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> DR76Response200:
        """Issue accounting documents and generate their files (DR76)."""
        return await self._call(
            _d_r76,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list_invoices(
        self,
        *,
        currency: Optional[StrictStr] = None,
        end_date: Optional[datetime] = None,
        invoice_id: Optional[Annotated[List[StrictInt], Field(max_length=100)]] = None,
        issuing_user_types: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        payment_status: Optional[StrictStr] = None,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        start_date: Optional[datetime] = None,
        type: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> IV01Response200:
        """List one page of accounting documents (IV01)."""
        return await self._call(
            _i_v01,
            currency=currency,
            end_date=end_date,
            invoice_id=invoice_id,
            issuing_user_types=issuing_user_types,
            pay_out_psp_codes=pay_out_psp_codes,
            payment_status=payment_status,
            seller_billing_cycle_id=seller_billing_cycle_id,
            start_date=start_date,
            type=type,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter_invoices(
        self,
        *,
        currency: Optional[StrictStr] = None,
        end_date: Optional[datetime] = None,
        invoice_id: Optional[Annotated[List[StrictInt], Field(max_length=100)]] = None,
        issuing_user_types: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        payment_status: Optional[StrictStr] = None,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        start_date: Optional[datetime] = None,
        type: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.IV01Response200Invoices]:
        """Iterate every item across all pages."""
        return self._paginate(
            _i_v01,
            currency=currency,
            end_date=end_date,
            invoice_id=invoice_id,
            issuing_user_types=issuing_user_types,
            pay_out_psp_codes=pay_out_psp_codes,
            payment_status=payment_status,
            seller_billing_cycle_id=seller_billing_cycle_id,
            start_date=start_date,
            type=type,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    async def download_invoice(
        self,
        accounting_document_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download an accounting document (IV02). Close the download, or read it in an `async with` block."""
        return await self._download(
            _i_v02,
            accounting_document_id=accounting_document_id,
            shop_id=shop_id,
        )

    @checked
    async def list_billing_cycles(
        self,
        *,
        currency: Optional[List[StrictStr]] = None,
        end_date: Optional[datetime] = None,
        id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        pay_out_psp_code: Optional[List[StrictStr]] = None,
        pay_out_state: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> SBC11Response200:
        """List one page of seller billing cycles (SBC11)."""
        return await self._call(
            _s_bc11,
            currency=currency,
            end_date=end_date,
            id=id,
            pay_out_psp_code=pay_out_psp_code,
            pay_out_state=pay_out_state,
            start_date=start_date,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_billing_cycles(
        self,
        *,
        currency: Optional[List[StrictStr]] = None,
        end_date: Optional[datetime] = None,
        id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        pay_out_psp_code: Optional[List[StrictStr]] = None,
        pay_out_state: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.SBC11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_bc11,
            currency=currency,
            end_date=end_date,
            id=id,
            pay_out_psp_code=pay_out_psp_code,
            pay_out_state=pay_out_state,
            start_date=start_date,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def list_transactions(
        self,
        *,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        transaction_date_from: Optional[datetime] = None,
        transaction_date_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        payment_state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        transaction_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_number: Optional[StrictStr] = None,
        order_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_line_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_customer: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_seller: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_id: Optional[StrictStr] = None,
        shop_model: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        other_reference: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=2000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> TL02Response200:
        """List one page of transaction lines (TL02)."""
        return await self._call(
            _t_l02,
            seller_billing_cycle_id=seller_billing_cycle_id,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            transaction_date_from=transaction_date_from,
            transaction_date_to=transaction_date_to,
            last_updated_from=last_updated_from,
            payment_state=payment_state,
            transaction_type=transaction_type,
            accounting_document_number=accounting_document_number,
            order_id=order_id,
            order_line_id=order_line_id,
            order_reference_for_customer=order_reference_for_customer,
            order_reference_for_seller=order_reference_for_seller,
            accounting_document_id=accounting_document_id,
            shop_model=shop_model,
            pay_out_psp_codes=pay_out_psp_codes,
            other_reference=other_reference,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_transactions(
        self,
        *,
        seller_billing_cycle_id: Optional[
            Annotated[List[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(max_length=100)]
        ] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        transaction_date_from: Optional[datetime] = None,
        transaction_date_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        payment_state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        transaction_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_number: Optional[StrictStr] = None,
        order_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_line_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_customer: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        order_reference_for_seller: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        accounting_document_id: Optional[StrictStr] = None,
        shop_model: Optional[List[StrictStr]] = None,
        pay_out_psp_codes: Optional[List[StrictStr]] = None,
        other_reference: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=2000, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.TL02Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _t_l02,
            seller_billing_cycle_id=seller_billing_cycle_id,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            transaction_date_from=transaction_date_from,
            transaction_date_to=transaction_date_to,
            last_updated_from=last_updated_from,
            payment_state=payment_state,
            transaction_type=transaction_type,
            accounting_document_number=accounting_document_number,
            order_id=order_id,
            order_line_id=order_line_id,
            order_reference_for_customer=order_reference_for_customer,
            order_reference_for_seller=order_reference_for_seller,
            accounting_document_id=accounting_document_id,
            shop_model=shop_model,
            pay_out_psp_codes=pay_out_psp_codes,
            other_reference=other_reference,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def export_transactions(
        self,
        body: Optional[Union[TL03Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> TL03Response200:
        """Start an export of transaction lines as JSON files (TL03)."""
        return await self._call(
            _t_l03,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def get_transaction_export(
        self,
        tracking_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> TL04Response200:
        """Get the status of a transaction line export (TL04)."""
        return await self._call(
            _t_l04,
            tracking_id=tracking_id,
            shop_id=shop_id,
        )

    @checked
    async def wait_for_transaction_export(
        self,
        tracking_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> TL04Response200:
        """Poll every `interval` seconds until the job that `export_transactions` started ends, and return its last status,
        done or failed. Pass the `tracking_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass, and
        stops when the task is cancelled."""
        return await self._wait(
            _t_l04,
            interval=interval,
            timeout=timeout,
            tracking_id=tracking_id,
        )
