# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import AsyncIterator, Iterator, Optional

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated

from mirakl_seller import models as _models
from mirakl_seller._runtime import (
    AsyncDownload,
    AsyncResource,
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
from mirakl_seller.models.h11_response200 import H11Response200
from mirakl_seller.models.p31_response200 import P31Response200
from mirakl_seller.models.p41_request_multipart_form_data_conversion_options import (
    P41RequestMultipartFormDataConversionOptions,
)
from mirakl_seller.models.p41_response201 import P41Response201
from mirakl_seller.models.p42_response200 import P42Response200
from mirakl_seller.models.p51_response200 import P51Response200
from mirakl_seller.models.pm11_response200 import PM11Response200
from mirakl_seller.models.vl11_response200 import VL11Response200

_h11: Operation[H11Response200] = Operation(
    id="H11",
    method="GET",
    path="/api/hierarchies",
    resource="products",
    name="list_categories",
    params=(
        Param("hierarchy", "hierarchy", "query"),
        Param("max_level", "max_level", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=H11Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PRODUCT_CONFIGURATION_READ",
                ),
            ),
        ),
    ),
)
_p31: Operation[P31Response200] = Operation(
    id="P31",
    method="GET",
    path="/api/products",
    resource="products",
    name="list",
    params=(
        Param("product_references", "product_references", "query"),
        Param("products", "products", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=P31Response200,
    returns_json=True,
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
_p41: Operation[P41Response201] = Operation(
    id="P41",
    method="POST",
    path="/api/products/imports",
    resource="products",
    name="import_",
    params=(
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("conversion_options", "conversion_options", "form"),
        Param("conversion_type", "conversion_type", "form"),
        Param("file", "file", "form"),
        Param("operator_format", "operator_format", "form"),
    ),
    response=P41Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PRODUCT_WRITE",
                ),
            ),
        ),
    ),
)
_p42: Operation[P42Response200] = Operation(
    id="P42",
    method="GET",
    path="/api/products/imports/{import}",
    resource="products",
    name="get_import",
    params=(
        Param("import", "import_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=P42Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PRODUCT_WRITE",
                ),
            ),
        ),
    ),
    job=Job(
        state="import_status",
        done=("COMPLETE",),
        failed=(
            "TRANSFORMATION_FAILED",
            "CANCELLED",
            "FAILED",
        ),
    ),
)
_p44: Operation[None] = Operation(
    id="P44",
    method="GET",
    path="/api/products/imports/{import}/error_report",
    resource="products",
    name="download_error_report",
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
                    "ROLE_PARTNER_PRODUCT_WRITE",
                ),
            ),
        ),
    ),
)
_p45: Operation[None] = Operation(
    id="P45",
    method="GET",
    path="/api/products/imports/{import}/new_product_report",
    resource="products",
    name="download_new_product_report",
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
                    "ROLE_PARTNER_PRODUCT_WRITE",
                ),
            ),
        ),
    ),
)
_p46: Operation[None] = Operation(
    id="P46",
    method="GET",
    path="/api/products/imports/{import}/transformed_file",
    resource="products",
    name="download_transformed_file",
    params=(
        Param("import", "import_id", "path"),
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
                    "ROLE_PARTNER_PRODUCT_WRITE",
                ),
            ),
        ),
    ),
)
_p47: Operation[None] = Operation(
    id="P47",
    method="GET",
    path="/api/products/imports/{import}/transformation_error_report",
    resource="products",
    name="download_transformation_error_report",
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
                    "ROLE_PARTNER_PRODUCT_WRITE",
                ),
            ),
        ),
    ),
)
_p51: Operation[P51Response200] = Operation(
    id="P51",
    method="GET",
    path="/api/products/imports",
    resource="products",
    name="list_imports",
    params=(
        Param("last_request_date", "last_request_date", "query"),
        Param("status", "status", "query"),
        Param("has_transformed_file", "has_transformed_file", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("max", "max", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=P51Response200,
    returns_json=True,
    iterator="iter_imports",
    item=_models.P51Response200ProductImportTrackings,
    paging=Offset(items="product_import_trackings", total="total_count", offset="offset"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PRODUCT_WRITE",
                ),
            ),
        ),
    ),
)
_p_m11: Operation[PM11Response200] = Operation(
    id="PM11",
    method="GET",
    path="/api/products/attributes",
    resource="products",
    name="list_attributes",
    params=(
        Param("hierarchy", "hierarchy", "query"),
        Param("max_level", "max_level", "query"),
        Param("all_operator_attributes", "all_operator_attributes", "query"),
        Param("with_roles", "with_roles", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=PM11Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PRODUCT_CONFIGURATION_READ",
                ),
            ),
        ),
    ),
)
_v_l11: Operation[VL11Response200] = Operation(
    id="VL11",
    method="GET",
    path="/api/values_lists",
    resource="products",
    name="list_value_lists",
    params=(
        Param("code", "code", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=VL11Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PRODUCT_CONFIGURATION_READ",
                ),
            ),
        ),
    ),
)

OPERATIONS = (
    _h11,
    _p31,
    _p41,
    _p42,
    _p44,
    _p45,
    _p46,
    _p47,
    _p51,
    _p_m11,
    _v_l11,
)


class ProductsApi(Resource):
    @checked
    def list_categories(
        self,
        *,
        hierarchy: Optional[StrictStr] = None,
        max_level: Optional[StrictInt] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> H11Response200:
        """List catalog categories and their parents and children (H11)."""
        return self._call(
            _h11,
            hierarchy=hierarchy,
            max_level=max_level,
            shop_id=shop_id,
        )

    @checked
    def list(
        self,
        *,
        product_references: StrictStr,
        products: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> P31Response200:
        """Get products by their references (P31)."""
        return self._call(
            _p31,
            product_references=product_references,
            products=products,
            shop_id=shop_id,
        )

    @checked
    def import_(
        self,
        *,
        file: FileInput,
        shop_id: Optional[StrictInt] = None,
        conversion_options: Optional[P41RequestMultipartFormDataConversionOptions] = None,
        conversion_type: Optional[StrictStr] = None,
        operator_format: Optional[StrictBool] = None,
    ) -> P41Response201:
        """Import a product file into the operator's catalog (P41)."""
        return self._call(
            _p41,
            shop_id=shop_id,
            conversion_options=conversion_options,
            conversion_type=conversion_type,
            file=file,
            operator_format=operator_format,
        )

    @checked
    def get_import(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> P42Response200:
        """Get the status of a product import (P42)."""
        return self._call(
            _p42,
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
    ) -> P42Response200:
        """Poll every `interval` seconds until the job that `import_` started ends, and return its last status,
        done or failed. Pass the `import_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass."""
        return self._wait(
            _p42,
            interval=interval,
            timeout=timeout,
            import_id=import_id,
        )

    @checked
    def download_error_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download the report of a product import's rejected products (P44). Close the download, or read it in a `with` block."""
        return self._download(
            _p44,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def download_new_product_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download the report of a product import's added products (P45). Close the download, or read it in a `with` block."""
        return self._download(
            _p45,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def download_transformed_file(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download a product import's file in the operator's format (P46). Close the download, or read it in a `with` block."""
        return self._download(
            _p46,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def download_transformation_error_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download a product import's transformation error report (P47). Close the download, or read it in a `with` block."""
        return self._download(
            _p47,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    def list_imports(
        self,
        *,
        last_request_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        has_transformed_file: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> P51Response200:
        """List one page of product imports (P51)."""
        return self._call(
            _p51,
            last_request_date=last_request_date,
            status=status,
            has_transformed_file=has_transformed_file,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter_imports(
        self,
        *,
        last_request_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        has_transformed_file: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.P51Response200ProductImportTrackings]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p51,
            last_request_date=last_request_date,
            status=status,
            has_transformed_file=has_transformed_file,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def list_attributes(
        self,
        *,
        hierarchy: Optional[StrictStr] = None,
        max_level: Optional[StrictInt] = None,
        all_operator_attributes: Optional[StrictBool] = None,
        with_roles: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> PM11Response200:
        """Get the product attribute configuration (PM11)."""
        return self._call(
            _p_m11,
            hierarchy=hierarchy,
            max_level=max_level,
            all_operator_attributes=all_operator_attributes,
            with_roles=with_roles,
            shop_id=shop_id,
        )

    @checked
    def list_value_lists(
        self,
        *,
        code: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> VL11Response200:
        """Get the operator's value lists (VL11)."""
        return self._call(
            _v_l11,
            code=code,
            shop_id=shop_id,
        )


class AsyncProductsApi(AsyncResource):
    @checked
    async def list_categories(
        self,
        *,
        hierarchy: Optional[StrictStr] = None,
        max_level: Optional[StrictInt] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> H11Response200:
        """List catalog categories and their parents and children (H11)."""
        return await self._call(
            _h11,
            hierarchy=hierarchy,
            max_level=max_level,
            shop_id=shop_id,
        )

    @checked
    async def list(
        self,
        *,
        product_references: StrictStr,
        products: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> P31Response200:
        """Get products by their references (P31)."""
        return await self._call(
            _p31,
            product_references=product_references,
            products=products,
            shop_id=shop_id,
        )

    @checked
    async def import_(
        self,
        *,
        file: FileInput,
        shop_id: Optional[StrictInt] = None,
        conversion_options: Optional[P41RequestMultipartFormDataConversionOptions] = None,
        conversion_type: Optional[StrictStr] = None,
        operator_format: Optional[StrictBool] = None,
    ) -> P41Response201:
        """Import a product file into the operator's catalog (P41)."""
        return await self._call(
            _p41,
            shop_id=shop_id,
            conversion_options=conversion_options,
            conversion_type=conversion_type,
            file=file,
            operator_format=operator_format,
        )

    @checked
    async def get_import(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> P42Response200:
        """Get the status of a product import (P42)."""
        return await self._call(
            _p42,
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
    ) -> P42Response200:
        """Poll every `interval` seconds until the job that `import_` started ends, and return its last status,
        done or failed. Pass the `import_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass, and
        stops when the task is cancelled."""
        return await self._wait(
            _p42,
            interval=interval,
            timeout=timeout,
            import_id=import_id,
        )

    @checked
    async def download_error_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download the report of a product import's rejected products (P44). Close the download, or read it in an `async with` block."""
        return await self._download(
            _p44,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def download_new_product_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download the report of a product import's added products (P45). Close the download, or read it in an `async with` block."""
        return await self._download(
            _p45,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def download_transformed_file(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download a product import's file in the operator's format (P46). Close the download, or read it in an `async with` block."""
        return await self._download(
            _p46,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def download_transformation_error_report(
        self,
        import_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download a product import's transformation error report (P47). Close the download, or read it in an `async with` block."""
        return await self._download(
            _p47,
            import_id=import_id,
            shop_id=shop_id,
        )

    @checked
    async def list_imports(
        self,
        *,
        last_request_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        has_transformed_file: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> P51Response200:
        """List one page of product imports (P51)."""
        return await self._call(
            _p51,
            last_request_date=last_request_date,
            status=status,
            has_transformed_file=has_transformed_file,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter_imports(
        self,
        *,
        last_request_date: Optional[datetime] = None,
        status: Optional[StrictStr] = None,
        has_transformed_file: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.P51Response200ProductImportTrackings]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p51,
            last_request_date=last_request_date,
            status=status,
            has_transformed_file=has_transformed_file,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    async def list_attributes(
        self,
        *,
        hierarchy: Optional[StrictStr] = None,
        max_level: Optional[StrictInt] = None,
        all_operator_attributes: Optional[StrictBool] = None,
        with_roles: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> PM11Response200:
        """Get the product attribute configuration (PM11)."""
        return await self._call(
            _p_m11,
            hierarchy=hierarchy,
            max_level=max_level,
            all_operator_attributes=all_operator_attributes,
            with_roles=with_roles,
            shop_id=shop_id,
        )

    @checked
    async def list_value_lists(
        self,
        *,
        code: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> VL11Response200:
        """Get the operator's value lists (VL11)."""
        return await self._call(
            _v_l11,
            code=code,
            shop_id=shop_id,
        )
