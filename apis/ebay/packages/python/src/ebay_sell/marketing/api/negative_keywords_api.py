# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.bulk_create_negative_keyword_request import BulkCreateNegativeKeywordRequest
from ebay_sell.marketing.models.bulk_create_negative_keyword_response import BulkCreateNegativeKeywordResponse
from ebay_sell.marketing.models.bulk_update_negative_keyword_request import BulkUpdateNegativeKeywordRequest
from ebay_sell.marketing.models.bulk_update_negative_keyword_response import BulkUpdateNegativeKeywordResponse
from ebay_sell.marketing.models.create_negative_keyword_request import CreateNegativeKeywordRequest
from ebay_sell.marketing.models.negative_keyword import NegativeKeyword
from ebay_sell.marketing.models.negative_keyword_paged_collection_response import NegativeKeywordPagedCollectionResponse
from ebay_sell.marketing.models.update_negative_keyword_request import UpdateNegativeKeywordRequest

_bulk_create_negative_keyword: Operation[BulkCreateNegativeKeywordResponse] = Operation(
    id="bulkCreateNegativeKeyword",
    method="POST",
    path="/sell/marketing/v1/bulk_create_negative_keyword",
    resource="negative_keywords",
    name="bulk_create",
    params=(),
    response=BulkCreateNegativeKeywordResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_update_negative_keyword: Operation[BulkUpdateNegativeKeywordResponse] = Operation(
    id="bulkUpdateNegativeKeyword",
    method="POST",
    path="/sell/marketing/v1/bulk_update_negative_keyword",
    resource="negative_keywords",
    name="bulk_update",
    params=(),
    response=BulkUpdateNegativeKeywordResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_create_negative_keyword: Operation[object] = Operation(
    id="createNegativeKeyword",
    method="POST",
    path="/sell/marketing/v1/negative_keyword",
    resource="negative_keywords",
    name="create",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_negative_keyword: Operation[NegativeKeyword] = Operation(
    id="getNegativeKeyword",
    method="GET",
    path="/sell/marketing/v1/negative_keyword/{negative_keyword_id}",
    resource="negative_keywords",
    name="get",
    params=(Param("negative_keyword_id", "negative_keyword_id", "path"),),
    response=NegativeKeyword,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                ),
            ),
        ),
    ),
    host="api",
)
_get_negative_keywords: Operation[NegativeKeywordPagedCollectionResponse] = Operation(
    id="getNegativeKeywords",
    method="GET",
    path="/sell/marketing/v1/negative_keyword",
    resource="negative_keywords",
    name="list",
    params=(
        Param("ad_group_ids", "ad_group_ids", "query"),
        Param("campaign_ids", "campaign_ids", "query"),
        Param("limit", "limit", "query"),
        Param("negative_keyword_status", "negative_keyword_status", "query"),
        Param("offset", "offset", "query"),
    ),
    response=NegativeKeywordPagedCollectionResponse,
    returns_json=True,
    iterator="iter",
    item=_models.NegativeKeyword,
    paging=NextLink(
        items="negativeKeywords",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                ),
            ),
        ),
    ),
    host="api",
)
_update_negative_keyword: Operation[None] = Operation(
    id="updateNegativeKeyword",
    method="PUT",
    path="/sell/marketing/v1/negative_keyword/{negative_keyword_id}",
    resource="negative_keywords",
    name="update",
    params=(Param("negative_keyword_id", "negative_keyword_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _bulk_create_negative_keyword,
    _bulk_update_negative_keyword,
    _create_negative_keyword,
    _get_negative_keyword,
    _get_negative_keywords,
    _update_negative_keyword,
)


class NegativeKeywordsApi(Resource):
    @checked
    def bulk_create(
        self,
        body: Union[BulkCreateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> BulkCreateNegativeKeywordResponse:
        """Create several negative keywords."""
        return self._call(
            _bulk_create_negative_keyword,
            _body=body,
        )

    @checked
    def bulk_update(
        self,
        body: Union[BulkUpdateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> BulkUpdateNegativeKeywordResponse:
        """Change the status of several negative keywords."""
        return self._call(
            _bulk_update_negative_keyword,
            _body=body,
        )

    @checked
    def create(
        self,
        body: Union[CreateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> object:
        """Create a negative keyword."""
        return self._call(
            _create_negative_keyword,
            _body=body,
        )

    @checked
    def get(
        self,
        negative_keyword_id: StrictStr,
    ) -> NegativeKeyword:
        """Get one negative keyword."""
        return self._call(
            _get_negative_keyword,
            negative_keyword_id=negative_keyword_id,
        )

    @checked
    def list(
        self,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        campaign_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        negative_keyword_status: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> NegativeKeywordPagedCollectionResponse:
        """List one page of negative keywords."""
        return self._call(
            _get_negative_keywords,
            ad_group_ids=ad_group_ids,
            campaign_ids=campaign_ids,
            limit=limit,
            negative_keyword_status=negative_keyword_status,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        campaign_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        negative_keyword_status: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.NegativeKeyword]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_negative_keywords,
            ad_group_ids=ad_group_ids,
            campaign_ids=campaign_ids,
            limit=limit,
            negative_keyword_status=negative_keyword_status,
            offset=offset,
        )

    @checked
    def update(
        self,
        negative_keyword_id: StrictStr,
        body: Union[UpdateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> None:
        """Change the status of a negative keyword."""
        return self._call(
            _update_negative_keyword,
            negative_keyword_id=negative_keyword_id,
            _body=body,
        )


class AsyncNegativeKeywordsApi(AsyncResource):
    @checked
    async def bulk_create(
        self,
        body: Union[BulkCreateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> BulkCreateNegativeKeywordResponse:
        """Create several negative keywords."""
        return await self._call(
            _bulk_create_negative_keyword,
            _body=body,
        )

    @checked
    async def bulk_update(
        self,
        body: Union[BulkUpdateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> BulkUpdateNegativeKeywordResponse:
        """Change the status of several negative keywords."""
        return await self._call(
            _bulk_update_negative_keyword,
            _body=body,
        )

    @checked
    async def create(
        self,
        body: Union[CreateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> object:
        """Create a negative keyword."""
        return await self._call(
            _create_negative_keyword,
            _body=body,
        )

    @checked
    async def get(
        self,
        negative_keyword_id: StrictStr,
    ) -> NegativeKeyword:
        """Get one negative keyword."""
        return await self._call(
            _get_negative_keyword,
            negative_keyword_id=negative_keyword_id,
        )

    @checked
    async def list(
        self,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        campaign_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        negative_keyword_status: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> NegativeKeywordPagedCollectionResponse:
        """List one page of negative keywords."""
        return await self._call(
            _get_negative_keywords,
            ad_group_ids=ad_group_ids,
            campaign_ids=campaign_ids,
            limit=limit,
            negative_keyword_status=negative_keyword_status,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        campaign_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        negative_keyword_status: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.NegativeKeyword]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_negative_keywords,
            ad_group_ids=ad_group_ids,
            campaign_ids=campaign_ids,
            limit=limit,
            negative_keyword_status=negative_keyword_status,
            offset=offset,
        )

    @checked
    async def update(
        self,
        negative_keyword_id: StrictStr,
        body: Union[UpdateNegativeKeywordRequest, Mapping[str, Any]],
    ) -> None:
        """Change the status of a negative keyword."""
        return await self._call(
            _update_negative_keyword,
            negative_keyword_id=negative_keyword_id,
            _body=body,
        )
