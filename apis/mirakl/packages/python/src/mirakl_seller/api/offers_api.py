# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import Field, StrictBool, StrictInt, StrictStr
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
from mirakl_seller.models.of01_response201 import OF01Response201
from mirakl_seller.models.of02_response200 import OF02Response200
from mirakl_seller.models.of04_response200 import OF04Response200
from mirakl_seller.models.of21_response200 import OF21Response200
from mirakl_seller.models.of22_response200 import OF22Response200
from mirakl_seller.models.of24_request import OF24Request
from mirakl_seller.models.of24_response201 import OF24Response201
from mirakl_seller.models.of52_request import OF52Request
from mirakl_seller.models.of52_response200 import OF52Response200
from mirakl_seller.models.of53_response200 import OF53Response200
from mirakl_seller.models.p11_response200 import P11Response200
from mirakl_seller.models.pri01_response201 import PRI01Response201
from mirakl_seller.models.pri02_response200 import PRI02Response200
from mirakl_seller.models.sto01_response201 import STO01Response201
from mirakl_seller.models.sto02_response200 import STO02Response200

_o_f01: Operation[OF01Response201] = Operation(
    id="OF01",
    method="POST",
    path="/api/offers/imports",
    resource="offers",
    name="import_",
    params=(
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("file", "file", "form"),
        Param("import_mode", "import_mode", "form"),
        Param("operator_format", "operator_format", "form"),
        Param("with_products", "with_products", "form"),
    ),
    response=OF01Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_WRITE",
                ),
            ),
        ),
    ),
)
_o_f02: Operation[OF02Response200] = Operation(
    id="OF02",
    method="GET",
    path="/api/offers/imports/{import}",
    resource="offers",
    name="get_import",
    params=(
        Param("import", "import_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=OF02Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_WRITE",
                    "ROLE_PARTNER_OFFER_TRACKING_READ",
                ),
            ),
        ),
    ),
    job=Job(state="status", done=("COMPLETE",), failed=("FAILED",)),
)
_o_f03: Operation[None] = Operation(
    id="OF03",
    method="GET",
    path="/api/offers/imports/{import}/error_report",
    resource="offers",
    name="download_import_error_report",
    params=(
        Param("import", "import_id", "path"),
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
                    "ROLE_PARTNER_OFFER_WRITE",
                    "ROLE_PARTNER_OFFER_TRACKING_READ",
                ),
            ),
        ),
    ),
)
_o_f04: Operation[OF04Response200] = Operation(
    id="OF04",
    method="GET",
    path="/api/offers/imports",
    resource="offers",
    name="list_imports",
    params=(
        Param("start_date", "start_date", "query"),
        Param("end_date", "end_date", "query"),
        Param("status", "status", "query"),
        Param("mode", "mode", "query"),
        Param("origins", "origins", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=OF04Response200,
    returns_json=True,
    iterator="iter_imports",
    item=_models.OF04Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_WRITE",
                    "ROLE_PARTNER_OFFER_TRACKING_READ",
                ),
            ),
        ),
    ),
)
_o_f21: Operation[OF21Response200] = Operation(
    id="OF21",
    method="GET",
    path="/api/offers",
    resource="offers",
    name="list",
    params=(
        Param("offer_state_codes", "offer_state_codes", "query"),
        Param("sku", "sku", "query"),
        Param("product_id", "product_id", "query"),
        Param("favorite", "favorite", "query"),
        Param("pricing_channel_code", "pricing_channel_code", "query"),
        Param("pricing_customer_organization_id", "pricing_customer_organization_id", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("max", "max", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=OF21Response200,
    returns_json=True,
    iterator="iter",
    item=_models.OF21Response200Offers,
    paging=Offset(items="offers", total="total_count", offset="offset"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_READ",
                ),
            ),
        ),
    ),
)
_o_f22: Operation[OF22Response200] = Operation(
    id="OF22",
    method="GET",
    path="/api/offers/{offer}",
    resource="offers",
    name="get",
    params=(
        Param("offer", "offer", "path"),
        Param("pricing_channel_code", "pricing_channel_code", "query"),
        Param("pricing_customer_organization_id", "pricing_customer_organization_id", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=OF22Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_READ",
                ),
            ),
        ),
    ),
)
_o_f24: Operation[OF24Response201] = Operation(
    id="OF24",
    method="POST",
    path="/api/offers",
    resource="offers",
    name="update",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OF24Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_WRITE",
                ),
            ),
        ),
    ),
)
_o_f52: Operation[OF52Response200] = Operation(
    id="OF52",
    method="POST",
    path="/api/offers/export/async",
    resource="offers",
    name="export",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OF52Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_OFFER_READ",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
)
_o_f53: Operation[OF53Response200] = Operation(
    id="OF53",
    method="GET",
    path="/api/offers/export/async/status/{tracking_id}",
    resource="offers",
    name="get_export",
    params=(
        Param("tracking_id", "tracking_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=OF53Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_OFFER_READ",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
    job=Job(state="status", done=("COMPLETED",), failed=("FAILED",)),
)
_p11: Operation[P11Response200] = Operation(
    id="P11",
    method="GET",
    path="/api/products/offers",
    resource="offers",
    name="list_for_products",
    params=(
        Param("product_ids", "product_ids", "query"),
        Param("product_references", "product_references", "query"),
        Param("offer_state_codes", "offer_state_codes", "query"),
        Param("all_offers", "all_offers", "query"),
        Param("channel_codes", "channel_codes", "query"),
        Param("all_channels", "all_channels", "query"),
        Param("pricing_channel_code", "pricing_channel_code", "query"),
        Param("pricing_customer_organization_id", "pricing_customer_organization_id", "query"),
        Param("shipping_zones", "shipping_zones", "query"),
        Param("all_shipping_zones", "all_shipping_zones", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("max", "max", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=P11Response200,
    returns_json=True,
    iterator="iter_for_products",
    item=_models.P11Response200Products,
    paging=Offset(items="products", total="total_count", offset="offset"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PRODUCT_READ",
                ),
            ),
        ),
    ),
)
_p_ri01: Operation[PRI01Response201] = Operation(
    id="PRI01",
    method="POST",
    path="/api/offers/pricing/imports",
    resource="offers",
    name="import_prices",
    params=(
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("file", "file", "form"),
    ),
    response=PRI01Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_PRICING_WRITE",
                ),
            ),
        ),
    ),
)
_p_ri02: Operation[PRI02Response200] = Operation(
    id="PRI02",
    method="GET",
    path="/api/offers/pricing/imports",
    resource="offers",
    name="list_price_imports",
    params=(
        Param("import_id", "import_id", "query"),
        Param("start_date", "start_date", "query"),
        Param("end_date", "end_date", "query"),
        Param("status", "status", "query"),
        Param("origins", "origins", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=PRI02Response200,
    returns_json=True,
    iterator="iter_price_imports",
    item=_models.PRI02Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_PRICING_READ",
                ),
            ),
        ),
    ),
)
_p_ri03: Operation[None] = Operation(
    id="PRI03",
    method="GET",
    path="/api/offers/pricing/imports/{import_id}/error_report",
    resource="offers",
    name="download_price_import_error_report",
    params=(
        Param("import_id", "import_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    binary_response=True,
    accept="text/csv",
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_PRICING_READ",
                ),
            ),
        ),
    ),
)
_s_to01: Operation[STO01Response201] = Operation(
    id="STO01",
    method="POST",
    path="/api/offers/stock/imports",
    resource="offers",
    name="import_stock",
    params=(
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("file", "file", "form"),
    ),
    response=STO01Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_STOCK_WRITE",
                ),
            ),
        ),
    ),
)
_s_to02: Operation[STO02Response200] = Operation(
    id="STO02",
    method="GET",
    path="/api/offers/stock/imports/{import_id}/status",
    resource="offers",
    name="get_stock_import",
    params=(
        Param("import_id", "import_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=STO02Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_STOCK_WRITE",
                ),
            ),
        ),
    ),
    job=Job(state="status", done=("COMPLETE",), failed=("FAILED",)),
)
_s_to03: Operation[None] = Operation(
    id="STO03",
    method="GET",
    path="/api/offers/stock/imports/{import_id}/error_report",
    resource="offers",
    name="download_stock_import_error_report",
    params=(
        Param("import_id", "import_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    binary_response=True,
    accept="text/csv",
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_STOCK_WRITE",
                ),
            ),
        ),
    ),
)

OPERATIONS = (
    _o_f01,
    _o_f02,
    _o_f03,
    _o_f04,
    _o_f21,
    _o_f22,
    _o_f24,
    _o_f52,
    _o_f53,
    _p11,
    _p_ri01,
    _p_ri02,
    _p_ri03,
    _s_to01,
    _s_to02,
    _s_to03,
)


class OffersApi(Resource):
    @checked
    def import_(
        self,
        *,
        file: FileInput,
        import_mode: StrictStr,
        shop_id: Optional[StrictInt] = None,
        operator_format: Optional[StrictBool] = None,
        with_products: Optional[StrictBool] = None,
    ) -> OF01Response201:
        """Import a file that creates, updates or deletes offers (OF01)."""
        return self._call(
            _o_f01,
            shop_id=shop_id,
            file=file,
            import_mode=import_mode,
            operator_format=operator_format,
            with_products=with_products,
        )

    @checked
    def get_import(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF02Response200:
        """Get the status and statistics of an offer import (OF02)."""
        return self._call(
            _o_f02,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def wait_for_import(
        self,
        import_id: StrictInt,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> OF02Response200:
        """Poll every `interval` seconds until the job that `import_` started ends, and return its last status,
        done or failed. Pass the `import_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass."""
        return self._wait(
            _o_f02,
            interval=interval,
            timeout=timeout,
            import_id=import_id,
        )

    @checked
    def download_import_error_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download an offer import's error report (OF03). Close the download, or read it in a `with` block."""
        return self._download(
            _o_f03,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def list_imports(
        self,
        *,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        mode: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> OF04Response200:
        """List one page of offer imports (OF04)."""
        return self._call(
            _o_f04,
            start_date=start_date,
            end_date=end_date,
            status=status,
            mode=mode,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_imports(
        self,
        *,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        mode: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.OF04Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _o_f04,
            start_date=start_date,
            end_date=end_date,
            status=status,
            mode=mode,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def list(
        self,
        *,
        offer_state_codes: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
        product_id: Optional[StrictStr] = None,
        favorite: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> OF21Response200:
        """List one page of your shop's offers (OF21)."""
        return self._call(
            _o_f21,
            offer_state_codes=offer_state_codes,
            sku=sku,
            product_id=product_id,
            favorite=favorite,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
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
        offer_state_codes: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
        product_id: Optional[StrictStr] = None,
        favorite: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.OF21Response200Offers]:
        """Iterate every item across all pages."""
        return self._paginate(
            _o_f21,
            offer_state_codes=offer_state_codes,
            sku=sku,
            product_id=product_id,
            favorite=favorite,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def get(
        self,
        offer: StrictInt,
        *,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> OF22Response200:
        """Get one offer (OF22)."""
        return self._call(
            _o_f22,
            offer=offer,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        body: Optional[Union[OF24Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF24Response201:
        """Create, update or delete offers (OF24)."""
        return self._call(
            _o_f24,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def export(
        self,
        body: Optional[Union[OF52Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF52Response200:
        """Start an export of offers as CSV or JSON files (OF52)."""
        return self._call(
            _o_f52,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def get_export(
        self,
        tracking_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF53Response200:
        """Get the status of an offer export (OF53)."""
        return self._call(
            _o_f53,
            tracking_id=tracking_id,
            shop_id=shop_id,
        )

    @checked
    def wait_for_export(
        self,
        tracking_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> OF53Response200:
        """Poll every `interval` seconds until the job that `export` started ends, and return its last status,
        done or failed. Pass the `tracking_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass."""
        return self._wait(
            _o_f53,
            interval=interval,
            timeout=timeout,
            tracking_id=tracking_id,
        )

    @checked
    def list_for_products(
        self,
        *,
        product_ids: Optional[StrictStr] = None,
        product_references: Optional[StrictStr] = None,
        offer_state_codes: Optional[StrictStr] = None,
        all_offers: Optional[StrictBool] = None,
        channel_codes: Optional[StrictStr] = None,
        all_channels: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shipping_zones: Optional[StrictStr] = None,
        all_shipping_zones: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> P11Response200:
        """List one page of the offers on each given product (P11)."""
        return self._call(
            _p11,
            product_ids=product_ids,
            product_references=product_references,
            offer_state_codes=offer_state_codes,
            all_offers=all_offers,
            channel_codes=channel_codes,
            all_channels=all_channels,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shipping_zones=shipping_zones,
            all_shipping_zones=all_shipping_zones,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter_for_products(
        self,
        *,
        product_ids: Optional[StrictStr] = None,
        product_references: Optional[StrictStr] = None,
        offer_state_codes: Optional[StrictStr] = None,
        all_offers: Optional[StrictBool] = None,
        channel_codes: Optional[StrictStr] = None,
        all_channels: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shipping_zones: Optional[StrictStr] = None,
        all_shipping_zones: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.P11Response200Products]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p11,
            product_ids=product_ids,
            product_references=product_references,
            offer_state_codes=offer_state_codes,
            all_offers=all_offers,
            channel_codes=channel_codes,
            all_channels=all_channels,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shipping_zones=shipping_zones,
            all_shipping_zones=all_shipping_zones,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def import_prices(
        self,
        *,
        file: FileInput,
        shop_id: Optional[StrictInt] = None,
    ) -> PRI01Response201:
        """Import a price file (PRI01)."""
        return self._call(
            _p_ri01,
            shop_id=shop_id,
            file=file,
        )

    @checked
    def list_price_imports(
        self,
        *,
        import_id: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> PRI02Response200:
        """List one page of price imports (PRI02)."""
        return self._call(
            _p_ri02,
            import_id=import_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_price_imports(
        self,
        *,
        import_id: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.PRI02Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p_ri02,
            import_id=import_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def download_price_import_error_report(
        self,
        import_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download a price import's error report as CSV (PRI03). Close the download, or read it in a `with` block."""
        return self._download(
            _p_ri03,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def import_stock(
        self,
        *,
        file: FileInput,
        shop_id: Optional[StrictInt] = None,
    ) -> STO01Response201:
        """Import a stock file (STO01)."""
        return self._call(
            _s_to01,
            shop_id=shop_id,
            file=file,
        )

    @checked
    def get_stock_import(
        self,
        import_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> STO02Response200:
        """Get the status and statistics of a stock import (STO02)."""
        return self._call(
            _s_to02,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def wait_for_stock_import(
        self,
        import_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> STO02Response200:
        """Poll every `interval` seconds until the job that `import_stock` started ends, and return its last status,
        done or failed. Pass the `import_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass."""
        return self._wait(
            _s_to02,
            interval=interval,
            timeout=timeout,
            import_id=import_id,
        )

    @checked
    def download_stock_import_error_report(
        self,
        import_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download a stock import's error report as CSV (STO03). Close the download, or read it in a `with` block."""
        return self._download(
            _s_to03,
            import_id=import_id,
            shop_id=shop_id,
        )


class AsyncOffersApi(AsyncResource):
    @checked
    async def import_(
        self,
        *,
        file: FileInput,
        import_mode: StrictStr,
        shop_id: Optional[StrictInt] = None,
        operator_format: Optional[StrictBool] = None,
        with_products: Optional[StrictBool] = None,
    ) -> OF01Response201:
        """Import a file that creates, updates or deletes offers (OF01)."""
        return await self._call(
            _o_f01,
            shop_id=shop_id,
            file=file,
            import_mode=import_mode,
            operator_format=operator_format,
            with_products=with_products,
        )

    @checked
    async def get_import(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF02Response200:
        """Get the status and statistics of an offer import (OF02)."""
        return await self._call(
            _o_f02,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def wait_for_import(
        self,
        import_id: StrictInt,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> OF02Response200:
        """Poll every `interval` seconds until the job that `import_` started ends, and return its last status,
        done or failed. Pass the `import_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass, and
        stops when the task is cancelled."""
        return await self._wait(
            _o_f02,
            interval=interval,
            timeout=timeout,
            import_id=import_id,
        )

    @checked
    async def download_import_error_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download an offer import's error report (OF03). Close the download, or read it in an `async with` block."""
        return await self._download(
            _o_f03,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def list_imports(
        self,
        *,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        mode: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> OF04Response200:
        """List one page of offer imports (OF04)."""
        return await self._call(
            _o_f04,
            start_date=start_date,
            end_date=end_date,
            status=status,
            mode=mode,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_imports(
        self,
        *,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        mode: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.OF04Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _o_f04,
            start_date=start_date,
            end_date=end_date,
            status=status,
            mode=mode,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def list(
        self,
        *,
        offer_state_codes: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
        product_id: Optional[StrictStr] = None,
        favorite: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> OF21Response200:
        """List one page of your shop's offers (OF21)."""
        return await self._call(
            _o_f21,
            offer_state_codes=offer_state_codes,
            sku=sku,
            product_id=product_id,
            favorite=favorite,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
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
        offer_state_codes: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
        product_id: Optional[StrictStr] = None,
        favorite: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.OF21Response200Offers]:
        """Iterate every item across all pages."""
        return self._paginate(
            _o_f21,
            offer_state_codes=offer_state_codes,
            sku=sku,
            product_id=product_id,
            favorite=favorite,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    async def get(
        self,
        offer: StrictInt,
        *,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> OF22Response200:
        """Get one offer (OF22)."""
        return await self._call(
            _o_f22,
            offer=offer,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        body: Optional[Union[OF24Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF24Response201:
        """Create, update or delete offers (OF24)."""
        return await self._call(
            _o_f24,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def export(
        self,
        body: Optional[Union[OF52Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF52Response200:
        """Start an export of offers as CSV or JSON files (OF52)."""
        return await self._call(
            _o_f52,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def get_export(
        self,
        tracking_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF53Response200:
        """Get the status of an offer export (OF53)."""
        return await self._call(
            _o_f53,
            tracking_id=tracking_id,
            shop_id=shop_id,
        )

    @checked
    async def wait_for_export(
        self,
        tracking_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> OF53Response200:
        """Poll every `interval` seconds until the job that `export` started ends, and return its last status,
        done or failed. Pass the `tracking_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass, and
        stops when the task is cancelled."""
        return await self._wait(
            _o_f53,
            interval=interval,
            timeout=timeout,
            tracking_id=tracking_id,
        )

    @checked
    async def list_for_products(
        self,
        *,
        product_ids: Optional[StrictStr] = None,
        product_references: Optional[StrictStr] = None,
        offer_state_codes: Optional[StrictStr] = None,
        all_offers: Optional[StrictBool] = None,
        channel_codes: Optional[StrictStr] = None,
        all_channels: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shipping_zones: Optional[StrictStr] = None,
        all_shipping_zones: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> P11Response200:
        """List one page of the offers on each given product (P11)."""
        return await self._call(
            _p11,
            product_ids=product_ids,
            product_references=product_references,
            offer_state_codes=offer_state_codes,
            all_offers=all_offers,
            channel_codes=channel_codes,
            all_channels=all_channels,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shipping_zones=shipping_zones,
            all_shipping_zones=all_shipping_zones,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter_for_products(
        self,
        *,
        product_ids: Optional[StrictStr] = None,
        product_references: Optional[StrictStr] = None,
        offer_state_codes: Optional[StrictStr] = None,
        all_offers: Optional[StrictBool] = None,
        channel_codes: Optional[StrictStr] = None,
        all_channels: Optional[StrictBool] = None,
        pricing_channel_code: Optional[StrictStr] = None,
        pricing_customer_organization_id: Optional[StrictStr] = None,
        shipping_zones: Optional[StrictStr] = None,
        all_shipping_zones: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.P11Response200Products]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p11,
            product_ids=product_ids,
            product_references=product_references,
            offer_state_codes=offer_state_codes,
            all_offers=all_offers,
            channel_codes=channel_codes,
            all_channels=all_channels,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shipping_zones=shipping_zones,
            all_shipping_zones=all_shipping_zones,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    async def import_prices(
        self,
        *,
        file: FileInput,
        shop_id: Optional[StrictInt] = None,
    ) -> PRI01Response201:
        """Import a price file (PRI01)."""
        return await self._call(
            _p_ri01,
            shop_id=shop_id,
            file=file,
        )

    @checked
    async def list_price_imports(
        self,
        *,
        import_id: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> PRI02Response200:
        """List one page of price imports (PRI02)."""
        return await self._call(
            _p_ri02,
            import_id=import_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_price_imports(
        self,
        *,
        import_id: Optional[List[StrictStr]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        origins: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.PRI02Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p_ri02,
            import_id=import_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            origins=origins,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def download_price_import_error_report(
        self,
        import_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download a price import's error report as CSV (PRI03). Close the download, or read it in an `async with` block."""
        return await self._download(
            _p_ri03,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def import_stock(
        self,
        *,
        file: FileInput,
        shop_id: Optional[StrictInt] = None,
    ) -> STO01Response201:
        """Import a stock file (STO01)."""
        return await self._call(
            _s_to01,
            shop_id=shop_id,
            file=file,
        )

    @checked
    async def get_stock_import(
        self,
        import_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> STO02Response200:
        """Get the status and statistics of a stock import (STO02)."""
        return await self._call(
            _s_to02,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def wait_for_stock_import(
        self,
        import_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> STO02Response200:
        """Poll every `interval` seconds until the job that `import_stock` started ends, and return its last status,
        done or failed. Pass the `import_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass, and
        stops when the task is cancelled."""
        return await self._wait(
            _s_to02,
            interval=interval,
            timeout=timeout,
            import_id=import_id,
        )

    @checked
    async def download_stock_import_error_report(
        self,
        import_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download a stock import's error report as CSV (STO03). Close the download, or read it in an `async with` block."""
        return await self._download(
            _s_to03,
            import_id=import_id,
            shop_id=shop_id,
        )
