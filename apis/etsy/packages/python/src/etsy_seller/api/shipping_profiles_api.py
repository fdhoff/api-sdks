# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shipping_carriers import ShippingCarriers
from etsy_seller.models.shop_shipping_profile import ShopShippingProfile
from etsy_seller.models.shop_shipping_profile_destination import ShopShippingProfileDestination
from etsy_seller.models.shop_shipping_profile_destinations import ShopShippingProfileDestinations
from etsy_seller.models.shop_shipping_profile_upgrade import ShopShippingProfileUpgrade
from etsy_seller.models.shop_shipping_profile_upgrades import ShopShippingProfileUpgrades
from etsy_seller.models.shop_shipping_profiles import ShopShippingProfiles

_create_shop_shipping_profile: Operation[ShopShippingProfile] = Operation(
    id="createShopShippingProfile",
    method="POST",
    path="/v3/application/shops/{shop_id}/shipping-profiles",
    resource="shipping_profiles",
    name="create",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("title", "title", "urlencoded"),
        Param("origin_country_iso", "origin_country_iso", "urlencoded"),
        Param("primary_cost", "primary_cost", "urlencoded"),
        Param("secondary_cost", "secondary_cost", "urlencoded"),
        Param("min_processing_time", "min_processing_time", "urlencoded"),
        Param("max_processing_time", "max_processing_time", "urlencoded"),
        Param("processing_time_unit", "processing_time_unit", "urlencoded"),
        Param("destination_country_iso", "destination_country_iso", "urlencoded"),
        Param("destination_region", "destination_region", "urlencoded"),
        Param("origin_postal_code", "origin_postal_code", "urlencoded"),
        Param("shipping_carrier_id", "shipping_carrier_id", "urlencoded"),
        Param("mail_class", "mail_class", "urlencoded"),
        Param("min_delivery_days", "min_delivery_days", "urlencoded"),
        Param("max_delivery_days", "max_delivery_days", "urlencoded"),
    ),
    response=ShopShippingProfile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_create_shop_shipping_profile_destination: Operation[ShopShippingProfileDestination] = Operation(
    id="createShopShippingProfileDestination",
    method="POST",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations",
    resource="shipping_profiles",
    name="create_destination",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("primary_cost", "primary_cost", "urlencoded"),
        Param("secondary_cost", "secondary_cost", "urlencoded"),
        Param("destination_country_iso", "destination_country_iso", "urlencoded"),
        Param("destination_region", "destination_region", "urlencoded"),
        Param("shipping_carrier_id", "shipping_carrier_id", "urlencoded"),
        Param("mail_class", "mail_class", "urlencoded"),
        Param("min_delivery_days", "min_delivery_days", "urlencoded"),
        Param("max_delivery_days", "max_delivery_days", "urlencoded"),
    ),
    response=ShopShippingProfileDestination,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_create_shop_shipping_profile_upgrade: Operation[ShopShippingProfileUpgrade] = Operation(
    id="createShopShippingProfileUpgrade",
    method="POST",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades",
    resource="shipping_profiles",
    name="create_upgrade",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("type", "type", "urlencoded"),
        Param("upgrade_name", "upgrade_name", "urlencoded"),
        Param("price", "price", "urlencoded"),
        Param("secondary_price", "secondary_price", "urlencoded"),
        Param("shipping_carrier_id", "shipping_carrier_id", "urlencoded"),
        Param("mail_class", "mail_class", "urlencoded"),
        Param("min_delivery_days", "min_delivery_days", "urlencoded"),
        Param("max_delivery_days", "max_delivery_days", "urlencoded"),
    ),
    response=ShopShippingProfileUpgrade,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_delete_shop_shipping_profile: Operation[None] = Operation(
    id="deleteShopShippingProfile",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}",
    resource="shipping_profiles",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_delete_shop_shipping_profile_destination: Operation[None] = Operation(
    id="deleteShopShippingProfileDestination",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}",
    resource="shipping_profiles",
    name="delete_destination",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("shipping_profile_destination_id", "shipping_profile_destination_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_delete_shop_shipping_profile_upgrade: Operation[None] = Operation(
    id="deleteShopShippingProfileUpgrade",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}",
    resource="shipping_profiles",
    name="delete_upgrade",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("upgrade_id", "upgrade_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_get_shipping_carriers: Operation[ShippingCarriers] = Operation(
    id="getShippingCarriers",
    method="GET",
    path="/v3/application/shipping-carriers",
    resource="shipping_profiles",
    name="list_carriers",
    params=(Param("origin_country_iso", "origin_country_iso", "query"),),
    response=ShippingCarriers,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_shop_shipping_profile: Operation[ShopShippingProfile] = Operation(
    id="getShopShippingProfile",
    method="GET",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}",
    resource="shipping_profiles",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
    ),
    response=ShopShippingProfile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_get_shop_shipping_profile_destinations_by_shipping_profile: Operation[ShopShippingProfileDestinations] = Operation(
    id="getShopShippingProfileDestinationsByShippingProfile",
    method="GET",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations",
    resource="shipping_profiles",
    name="list_destinations",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=ShopShippingProfileDestinations,
    returns_json=True,
    iterator="iter_destinations",
    item=_models.ShopShippingProfileDestination,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_get_shop_shipping_profile_upgrades: Operation[ShopShippingProfileUpgrades] = Operation(
    id="getShopShippingProfileUpgrades",
    method="GET",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades",
    resource="shipping_profiles",
    name="list_upgrades",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
    ),
    response=ShopShippingProfileUpgrades,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_get_shop_shipping_profiles: Operation[ShopShippingProfiles] = Operation(
    id="getShopShippingProfiles",
    method="GET",
    path="/v3/application/shops/{shop_id}/shipping-profiles",
    resource="shipping_profiles",
    name="list",
    params=(Param("shop_id", "shop_id", "path"),),
    response=ShopShippingProfiles,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_update_shop_shipping_profile: Operation[ShopShippingProfile] = Operation(
    id="updateShopShippingProfile",
    method="PUT",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}",
    resource="shipping_profiles",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("title", "title", "urlencoded"),
        Param("origin_country_iso", "origin_country_iso", "urlencoded"),
        Param("min_processing_time", "min_processing_time", "urlencoded"),
        Param("max_processing_time", "max_processing_time", "urlencoded"),
        Param("processing_time_unit", "processing_time_unit", "urlencoded"),
        Param("origin_postal_code", "origin_postal_code", "urlencoded"),
    ),
    response=ShopShippingProfile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_update_shop_shipping_profile_destination: Operation[ShopShippingProfileDestination] = Operation(
    id="updateShopShippingProfileDestination",
    method="PUT",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}",
    resource="shipping_profiles",
    name="update_destination",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("shipping_profile_destination_id", "shipping_profile_destination_id", "path"),
        Param("primary_cost", "primary_cost", "urlencoded"),
        Param("secondary_cost", "secondary_cost", "urlencoded"),
        Param("destination_country_iso", "destination_country_iso", "urlencoded"),
        Param("destination_region", "destination_region", "urlencoded"),
        Param("shipping_carrier_id", "shipping_carrier_id", "urlencoded"),
        Param("mail_class", "mail_class", "urlencoded"),
        Param("min_delivery_days", "min_delivery_days", "urlencoded"),
        Param("max_delivery_days", "max_delivery_days", "urlencoded"),
    ),
    response=ShopShippingProfileDestination,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_update_shop_shipping_profile_upgrade: Operation[ShopShippingProfileUpgrade] = Operation(
    id="updateShopShippingProfileUpgrade",
    method="PUT",
    path="/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}",
    resource="shipping_profiles",
    name="update_upgrade",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shipping_profile_id", "shipping_profile_id", "path"),
        Param("upgrade_id", "upgrade_id", "path"),
        Param("upgrade_name", "upgrade_name", "urlencoded"),
        Param("type", "type", "urlencoded"),
        Param("price", "price", "urlencoded"),
        Param("secondary_price", "secondary_price", "urlencoded"),
        Param("shipping_carrier_id", "shipping_carrier_id", "urlencoded"),
        Param("mail_class", "mail_class", "urlencoded"),
        Param("min_delivery_days", "min_delivery_days", "urlencoded"),
        Param("max_delivery_days", "max_delivery_days", "urlencoded"),
    ),
    response=ShopShippingProfileUpgrade,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)

OPERATIONS = (
    _create_shop_shipping_profile,
    _create_shop_shipping_profile_destination,
    _create_shop_shipping_profile_upgrade,
    _delete_shop_shipping_profile,
    _delete_shop_shipping_profile_destination,
    _delete_shop_shipping_profile_upgrade,
    _get_shipping_carriers,
    _get_shop_shipping_profile,
    _get_shop_shipping_profile_destinations_by_shipping_profile,
    _get_shop_shipping_profile_upgrades,
    _get_shop_shipping_profiles,
    _update_shop_shipping_profile,
    _update_shop_shipping_profile_destination,
    _update_shop_shipping_profile_upgrade,
)


class ShippingProfilesApi(Resource):
    @checked
    def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: StrictStr,
        origin_country_iso: StrictStr,
        primary_cost: Annotated[float, Field(ge=0)],
        secondary_cost: Annotated[float, Field(ge=0)],
        min_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        max_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        processing_time_unit: Optional[StrictStr] = None,
        destination_country_iso: Optional[StrictStr] = None,
        destination_region: Optional[StrictStr] = None,
        origin_postal_code: Optional[StrictStr] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfile:
        """Create a shipping profile."""
        return self._call(
            _create_shop_shipping_profile,
            shop_id=shop_id,
            title=title,
            origin_country_iso=origin_country_iso,
            primary_cost=primary_cost,
            secondary_cost=secondary_cost,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
            destination_country_iso=destination_country_iso,
            destination_region=destination_region,
            origin_postal_code=origin_postal_code,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    def create_destination(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        primary_cost: Annotated[float, Field(ge=0)],
        secondary_cost: Annotated[float, Field(ge=0)],
        destination_country_iso: Optional[StrictStr] = None,
        destination_region: Optional[StrictStr] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileDestination:
        """Add a destination to a shipping profile."""
        return self._call(
            _create_shop_shipping_profile_destination,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            primary_cost=primary_cost,
            secondary_cost=secondary_cost,
            destination_country_iso=destination_country_iso,
            destination_region=destination_region,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    def create_upgrade(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        type: StrictInt,
        upgrade_name: StrictStr,
        price: Annotated[float, Field(ge=0)],
        secondary_price: Annotated[float, Field(ge=0)],
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileUpgrade:
        """Add an upgrade to a shipping profile."""
        return self._call(
            _create_shop_shipping_profile_upgrade,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            type=type,
            upgrade_name=upgrade_name,
            price=price,
            secondary_price=secondary_price,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shipping profile."""
        return self._call(
            _delete_shop_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
        )

    @checked
    def delete_destination(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_destination_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shipping profile destination."""
        return self._call(
            _delete_shop_shipping_profile_destination,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_destination_id=shipping_profile_destination_id,
        )

    @checked
    def delete_upgrade(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        upgrade_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shipping profile upgrade."""
        return self._call(
            _delete_shop_shipping_profile_upgrade,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            upgrade_id=upgrade_id,
        )

    @checked
    def list_carriers(
        self,
        *,
        origin_country_iso: StrictStr,
    ) -> ShippingCarriers:
        """List the shipping carriers and mail classes for an origin country."""
        return self._call(
            _get_shipping_carriers,
            origin_country_iso=origin_country_iso,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopShippingProfile:
        """Get one shipping profile."""
        return self._call(
            _get_shop_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
        )

    @checked
    def list_destinations(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> ShopShippingProfileDestinations:
        """List one page of a shipping profile&#39;s destinations."""
        return self._call(
            _get_shop_shipping_profile_destinations_by_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_destinations(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.ShopShippingProfileDestination]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_shipping_profile_destinations_by_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            limit=limit,
            offset=offset,
        )

    @checked
    def list_upgrades(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopShippingProfileUpgrades:
        """List a shipping profile&#39;s upgrades."""
        return self._call(
            _get_shop_shipping_profile_upgrades,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopShippingProfiles:
        """List a shop&#39;s shipping profiles."""
        return self._call(
            _get_shop_shipping_profiles,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: Optional[StrictStr] = None,
        origin_country_iso: Optional[StrictStr] = None,
        min_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        max_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        processing_time_unit: Optional[StrictStr] = None,
        origin_postal_code: Optional[StrictStr] = None,
    ) -> ShopShippingProfile:
        """Update a shipping profile."""
        return self._call(
            _update_shop_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            title=title,
            origin_country_iso=origin_country_iso,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
            origin_postal_code=origin_postal_code,
        )

    @checked
    def update_destination(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_destination_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        primary_cost: Optional[Annotated[float, Field(ge=0)]] = None,
        secondary_cost: Optional[Annotated[float, Field(ge=0)]] = None,
        destination_country_iso: Optional[StrictStr] = None,
        destination_region: Optional[StrictStr] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileDestination:
        """Update a shipping profile destination."""
        return self._call(
            _update_shop_shipping_profile_destination,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_destination_id=shipping_profile_destination_id,
            primary_cost=primary_cost,
            secondary_cost=secondary_cost,
            destination_country_iso=destination_country_iso,
            destination_region=destination_region,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    def update_upgrade(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        upgrade_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        upgrade_name: Optional[StrictStr] = None,
        type: Optional[StrictInt] = None,
        price: Optional[Annotated[float, Field(ge=0)]] = None,
        secondary_price: Optional[Annotated[float, Field(ge=0)]] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileUpgrade:
        """Update a shipping profile upgrade."""
        return self._call(
            _update_shop_shipping_profile_upgrade,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            upgrade_id=upgrade_id,
            upgrade_name=upgrade_name,
            type=type,
            price=price,
            secondary_price=secondary_price,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )


class AsyncShippingProfilesApi(AsyncResource):
    @checked
    async def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: StrictStr,
        origin_country_iso: StrictStr,
        primary_cost: Annotated[float, Field(ge=0)],
        secondary_cost: Annotated[float, Field(ge=0)],
        min_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        max_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        processing_time_unit: Optional[StrictStr] = None,
        destination_country_iso: Optional[StrictStr] = None,
        destination_region: Optional[StrictStr] = None,
        origin_postal_code: Optional[StrictStr] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfile:
        """Create a shipping profile."""
        return await self._call(
            _create_shop_shipping_profile,
            shop_id=shop_id,
            title=title,
            origin_country_iso=origin_country_iso,
            primary_cost=primary_cost,
            secondary_cost=secondary_cost,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
            destination_country_iso=destination_country_iso,
            destination_region=destination_region,
            origin_postal_code=origin_postal_code,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    async def create_destination(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        primary_cost: Annotated[float, Field(ge=0)],
        secondary_cost: Annotated[float, Field(ge=0)],
        destination_country_iso: Optional[StrictStr] = None,
        destination_region: Optional[StrictStr] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileDestination:
        """Add a destination to a shipping profile."""
        return await self._call(
            _create_shop_shipping_profile_destination,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            primary_cost=primary_cost,
            secondary_cost=secondary_cost,
            destination_country_iso=destination_country_iso,
            destination_region=destination_region,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    async def create_upgrade(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        type: StrictInt,
        upgrade_name: StrictStr,
        price: Annotated[float, Field(ge=0)],
        secondary_price: Annotated[float, Field(ge=0)],
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileUpgrade:
        """Add an upgrade to a shipping profile."""
        return await self._call(
            _create_shop_shipping_profile_upgrade,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            type=type,
            upgrade_name=upgrade_name,
            price=price,
            secondary_price=secondary_price,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shipping profile."""
        return await self._call(
            _delete_shop_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
        )

    @checked
    async def delete_destination(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_destination_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shipping profile destination."""
        return await self._call(
            _delete_shop_shipping_profile_destination,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_destination_id=shipping_profile_destination_id,
        )

    @checked
    async def delete_upgrade(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        upgrade_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shipping profile upgrade."""
        return await self._call(
            _delete_shop_shipping_profile_upgrade,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            upgrade_id=upgrade_id,
        )

    @checked
    async def list_carriers(
        self,
        *,
        origin_country_iso: StrictStr,
    ) -> ShippingCarriers:
        """List the shipping carriers and mail classes for an origin country."""
        return await self._call(
            _get_shipping_carriers,
            origin_country_iso=origin_country_iso,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopShippingProfile:
        """Get one shipping profile."""
        return await self._call(
            _get_shop_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
        )

    @checked
    async def list_destinations(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> ShopShippingProfileDestinations:
        """List one page of a shipping profile&#39;s destinations."""
        return await self._call(
            _get_shop_shipping_profile_destinations_by_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_destinations(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.ShopShippingProfileDestination]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_shipping_profile_destinations_by_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            limit=limit,
            offset=offset,
        )

    @checked
    async def list_upgrades(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopShippingProfileUpgrades:
        """List a shipping profile&#39;s upgrades."""
        return await self._call(
            _get_shop_shipping_profile_upgrades,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopShippingProfiles:
        """List a shop&#39;s shipping profiles."""
        return await self._call(
            _get_shop_shipping_profiles,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: Optional[StrictStr] = None,
        origin_country_iso: Optional[StrictStr] = None,
        min_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        max_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        processing_time_unit: Optional[StrictStr] = None,
        origin_postal_code: Optional[StrictStr] = None,
    ) -> ShopShippingProfile:
        """Update a shipping profile."""
        return await self._call(
            _update_shop_shipping_profile,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            title=title,
            origin_country_iso=origin_country_iso,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
            origin_postal_code=origin_postal_code,
        )

    @checked
    async def update_destination(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_destination_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        primary_cost: Optional[Annotated[float, Field(ge=0)]] = None,
        secondary_cost: Optional[Annotated[float, Field(ge=0)]] = None,
        destination_country_iso: Optional[StrictStr] = None,
        destination_region: Optional[StrictStr] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileDestination:
        """Update a shipping profile destination."""
        return await self._call(
            _update_shop_shipping_profile_destination,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_destination_id=shipping_profile_destination_id,
            primary_cost=primary_cost,
            secondary_cost=secondary_cost,
            destination_country_iso=destination_country_iso,
            destination_region=destination_region,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )

    @checked
    async def update_upgrade(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Annotated[int, Field(strict=True, ge=1)],
        upgrade_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        upgrade_name: Optional[StrictStr] = None,
        type: Optional[StrictInt] = None,
        price: Optional[Annotated[float, Field(ge=0)]] = None,
        secondary_price: Optional[Annotated[float, Field(ge=0)]] = None,
        shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        mail_class: Optional[StrictStr] = None,
        min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
        max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None,
    ) -> ShopShippingProfileUpgrade:
        """Update a shipping profile upgrade."""
        return await self._call(
            _update_shop_shipping_profile_upgrade,
            shop_id=shop_id,
            shipping_profile_id=shipping_profile_id,
            upgrade_id=upgrade_id,
            upgrade_name=upgrade_name,
            type=type,
            price=price,
            secondary_price=secondary_price,
            shipping_carrier_id=shipping_carrier_id,
            mail_class=mail_class,
            min_delivery_days=min_delivery_days,
            max_delivery_days=max_delivery_days,
        )
