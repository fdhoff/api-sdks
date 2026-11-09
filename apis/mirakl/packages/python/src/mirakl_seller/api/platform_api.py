# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictBool, StrictInt, StrictStr

from mirakl_seller._runtime import (
    AsyncResource,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mirakl_seller.models.af01_response200 import AF01Response200
from mirakl_seller.models.ch11_response200 import CH11Response200
from mirakl_seller.models.cur01_response200 import CUR01Response200
from mirakl_seller.models.do01_response200 import DO01Response200
from mirakl_seller.models.l01_response200 import L01Response200
from mirakl_seller.models.of61_response200 import OF61Response200
from mirakl_seller.models.pc01_response200 import PC01Response200
from mirakl_seller.models.re01_response200 import RE01Response200
from mirakl_seller.models.sh11_response200 import SH11Response200
from mirakl_seller.models.sh12_response200 import SH12Response200
from mirakl_seller.models.sh21_response200 import SH21Response200
from mirakl_seller.models.sh31_response200 import SH31Response200
from mirakl_seller.models.sh42_response200 import SH42Response200
from mirakl_seller.models.sh52_response200 import SH52Response200

_a_f01: Operation[AF01Response200] = Operation(
    id="AF01",
    method="GET",
    path="/api/additional_fields",
    resource="platform",
    name="list_custom_fields",
    params=(
        Param("entities", "entities", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=AF01Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SETTINGS_READ",
                    "ROLE_PARTNER_OFFER_SETTINGS_READ",
                    "ROLE_PARTNER_SHOP_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_c_h11: Operation[CH11Response200] = Operation(
    id="CH11",
    method="GET",
    path="/api/channels",
    resource="platform",
    name="list_channels",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=CH11Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CHANNEL_READ",
                ),
            ),
        ),
    ),
)
_c_ur01: Operation[CUR01Response200] = Operation(
    id="CUR01",
    method="GET",
    path="/api/currencies",
    resource="platform",
    name="list_currencies",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=CUR01Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_CURRENCY_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_d_o01: Operation[DO01Response200] = Operation(
    id="DO01",
    method="GET",
    path="/api/documents",
    resource="platform",
    name="list_document_types",
    params=(
        Param("entities", "entities", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=DO01Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_l01: Operation[L01Response200] = Operation(
    id="L01",
    method="GET",
    path="/api/locales",
    resource="platform",
    name="list_locales",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=L01Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_I18N_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_o_f61: Operation[OF61Response200] = Operation(
    id="OF61",
    method="GET",
    path="/api/offers/states",
    resource="platform",
    name="list_offer_conditions",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OF61Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_p_c01: Operation[PC01Response200] = Operation(
    id="PC01",
    method="GET",
    path="/api/platform/configuration",
    resource="platform",
    name="get_configuration",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=PC01Response200,
    returns_json=True,
    security=((Scheme("Shop-API-Key", ("ROLE_SHOP_ADMIN",)),),),
)
_r_e01: Operation[RE01Response200] = Operation(
    id="RE01",
    method="GET",
    path="/api/reasons",
    resource="platform",
    name="list_reasons",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RE01Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_s_h11: Operation[SH11Response200] = Operation(
    id="SH11",
    method="GET",
    path="/api/shipping/zones",
    resource="platform",
    name="list_shipping_zones",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=SH11Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHIPPING_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_s_h12: Operation[SH12Response200] = Operation(
    id="SH12",
    method="GET",
    path="/api/shipping/types",
    resource="platform",
    name="list_shipping_methods",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=SH12Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHIPPING_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_s_h21: Operation[SH21Response200] = Operation(
    id="SH21",
    method="GET",
    path="/api/shipping/carriers",
    resource="platform",
    name="list_carriers",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=SH21Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHIPPING_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_s_h31: Operation[SH31Response200] = Operation(
    id="SH31",
    method="GET",
    path="/api/shipping/logistic_classes",
    resource="platform",
    name="list_logistic_classes",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=SH31Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHIPPING_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_s_h42: Operation[SH42Response200] = Operation(
    id="SH42",
    method="GET",
    path="/api/shipping/configuration/shop",
    resource="platform",
    name="get_shipping_configuration",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=SH42Response200,
    returns_json=True,
    security=((Scheme("Shop-API-Key", ("ROLE_SHOP_ADMIN",)),),),
)
_s_h52: Operation[SH52Response200] = Operation(
    id="SH52",
    method="GET",
    path="/api/shipping/charges/shop",
    resource="platform",
    name="get_shipping_charges",
    params=(
        Param("overridden_by_shop", "overridden_by_shop", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=SH52Response200,
    returns_json=True,
    security=((Scheme("Shop-API-Key", ("ROLE_SHOP_ADMIN",)),),),
)
_v01: Operation[None] = Operation(
    id="V01",
    method="GET",
    path="/api/version",
    resource="platform",
    name="health_check",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=None,
    security=(),
)

OPERATIONS = (
    _a_f01,
    _c_h11,
    _c_ur01,
    _d_o01,
    _l01,
    _o_f61,
    _p_c01,
    _r_e01,
    _s_h11,
    _s_h12,
    _s_h21,
    _s_h31,
    _s_h42,
    _s_h52,
    _v01,
)


class PlatformApi(Resource):
    @checked
    def list_custom_fields(
        self,
        *,
        entities: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> AF01Response200:
        """List the operator's custom fields (AF01)."""
        return self._call(
            _a_f01,
            entities=entities,
            shop_id=shop_id,
        )

    @checked
    def list_channels(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> CH11Response200:
        """List the enabled sales channels (CH11)."""
        return self._call(
            _c_h11,
            shop_id=shop_id,
        )

    @checked
    def list_currencies(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> CUR01Response200:
        """List currency codes and labels (CUR01)."""
        return self._call(
            _c_ur01,
            shop_id=shop_id,
        )

    @checked
    def list_document_types(
        self,
        *,
        entities: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> DO01Response200:
        """List the document types (DO01)."""
        return self._call(
            _d_o01,
            entities=entities,
            shop_id=shop_id,
        )

    @checked
    def list_locales(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> L01Response200:
        """List locale codes and labels (L01)."""
        return self._call(
            _l01,
            shop_id=shop_id,
        )

    @checked
    def list_offer_conditions(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF61Response200:
        """List the offer conditions (OF61)."""
        return self._call(
            _o_f61,
            shop_id=shop_id,
        )

    @checked
    def get_configuration(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> PC01Response200:
        """Get the platform configuration (PC01)."""
        return self._call(
            _p_c01,
            shop_id=shop_id,
        )

    @checked
    def list_reasons(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RE01Response200:
        """List the reasons for incidents, refunds and other actions (RE01)."""
        return self._call(
            _r_e01,
            shop_id=shop_id,
        )

    @checked
    def list_shipping_zones(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH11Response200:
        """List the active shipping zones (SH11)."""
        return self._call(
            _s_h11,
            shop_id=shop_id,
        )

    @checked
    def list_shipping_methods(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH12Response200:
        """List the active shipping methods (SH12)."""
        return self._call(
            _s_h12,
            shop_id=shop_id,
        )

    @checked
    def list_carriers(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH21Response200:
        """List the carriers (SH21)."""
        return self._call(
            _s_h21,
            shop_id=shop_id,
        )

    @checked
    def list_logistic_classes(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH31Response200:
        """List the logistic classes (SH31)."""
        return self._call(
            _s_h31,
            shop_id=shop_id,
        )

    @checked
    def get_shipping_configuration(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH42Response200:
        """Get your shop's shipping configuration (SH42)."""
        return self._call(
            _s_h42,
            shop_id=shop_id,
        )

    @checked
    def get_shipping_charges(
        self,
        *,
        overridden_by_shop: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> SH52Response200:
        """Get the shipping charges set for your shop (SH52)."""
        return self._call(
            _s_h52,
            overridden_by_shop=overridden_by_shop,
            shop_id=shop_id,
        )

    @checked
    def health_check(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Check that the instance is up. Needs no key (V01)."""
        return self._call(
            _v01,
            shop_id=shop_id,
        )


class AsyncPlatformApi(AsyncResource):
    @checked
    async def list_custom_fields(
        self,
        *,
        entities: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> AF01Response200:
        """List the operator's custom fields (AF01)."""
        return await self._call(
            _a_f01,
            entities=entities,
            shop_id=shop_id,
        )

    @checked
    async def list_channels(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> CH11Response200:
        """List the enabled sales channels (CH11)."""
        return await self._call(
            _c_h11,
            shop_id=shop_id,
        )

    @checked
    async def list_currencies(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> CUR01Response200:
        """List currency codes and labels (CUR01)."""
        return await self._call(
            _c_ur01,
            shop_id=shop_id,
        )

    @checked
    async def list_document_types(
        self,
        *,
        entities: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> DO01Response200:
        """List the document types (DO01)."""
        return await self._call(
            _d_o01,
            entities=entities,
            shop_id=shop_id,
        )

    @checked
    async def list_locales(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> L01Response200:
        """List locale codes and labels (L01)."""
        return await self._call(
            _l01,
            shop_id=shop_id,
        )

    @checked
    async def list_offer_conditions(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OF61Response200:
        """List the offer conditions (OF61)."""
        return await self._call(
            _o_f61,
            shop_id=shop_id,
        )

    @checked
    async def get_configuration(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> PC01Response200:
        """Get the platform configuration (PC01)."""
        return await self._call(
            _p_c01,
            shop_id=shop_id,
        )

    @checked
    async def list_reasons(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RE01Response200:
        """List the reasons for incidents, refunds and other actions (RE01)."""
        return await self._call(
            _r_e01,
            shop_id=shop_id,
        )

    @checked
    async def list_shipping_zones(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH11Response200:
        """List the active shipping zones (SH11)."""
        return await self._call(
            _s_h11,
            shop_id=shop_id,
        )

    @checked
    async def list_shipping_methods(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH12Response200:
        """List the active shipping methods (SH12)."""
        return await self._call(
            _s_h12,
            shop_id=shop_id,
        )

    @checked
    async def list_carriers(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH21Response200:
        """List the carriers (SH21)."""
        return await self._call(
            _s_h21,
            shop_id=shop_id,
        )

    @checked
    async def list_logistic_classes(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH31Response200:
        """List the logistic classes (SH31)."""
        return await self._call(
            _s_h31,
            shop_id=shop_id,
        )

    @checked
    async def get_shipping_configuration(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> SH42Response200:
        """Get your shop's shipping configuration (SH42)."""
        return await self._call(
            _s_h42,
            shop_id=shop_id,
        )

    @checked
    async def get_shipping_charges(
        self,
        *,
        overridden_by_shop: Optional[StrictBool] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> SH52Response200:
        """Get the shipping charges set for your shop (SH52)."""
        return await self._call(
            _s_h52,
            overridden_by_shop=overridden_by_shop,
            shop_id=shop_id,
        )

    @checked
    async def health_check(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Check that the instance is up. Needs no key (V01)."""
        return await self._call(
            _v01,
            shop_id=shop_id,
        )
