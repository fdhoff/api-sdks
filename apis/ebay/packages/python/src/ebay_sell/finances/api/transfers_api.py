# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.finances.models.transfer import Transfer

_get_transfer: Operation[Transfer] = Operation(
    id="getTransfer",
    method="GET",
    path="/sell/finances/v1/transfer/{transfer_Id}",
    resource="transfers",
    name="get",
    params=(
        Param("transfer_Id", "transfer_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=Transfer,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="apiz",
)

OPERATIONS = (_get_transfer,)


class TransfersApi(Resource):
    @checked
    def get(
        self,
        transfer_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> Transfer:
        """Get one transfer of funds the seller owes eBay."""
        return self._call(
            _get_transfer,
            transfer_id=transfer_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncTransfersApi(AsyncResource):
    @checked
    async def get(
        self,
        transfer_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> Transfer:
        """Get one transfer of funds the seller owes eBay."""
        return await self._call(
            _get_transfer,
            transfer_id=transfer_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
