# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.bulk_create_keyword_request import BulkCreateKeywordRequest
from ebay_sell.marketing.models.bulk_create_keyword_response import BulkCreateKeywordResponse
from ebay_sell.marketing.models.bulk_update_keyword_request import BulkUpdateKeywordRequest
from ebay_sell.marketing.models.bulk_update_keyword_response import BulkUpdateKeywordResponse
from ebay_sell.marketing.models.create_keyword_request import CreateKeywordRequest
from ebay_sell.marketing.models.keyword import Keyword
from ebay_sell.marketing.models.keyword_paged_collection_response import KeywordPagedCollectionResponse
from ebay_sell.marketing.models.update_keyword_request import UpdateKeywordRequest
from ebay_sell.marketing.models.update_keyword_response import UpdateKeywordResponse

_bulk_create_keyword: Operation[BulkCreateKeywordResponse] = Operation(
    id="bulkCreateKeyword",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_keyword",
    resource="keywords",
    name="bulk_create",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkCreateKeywordResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_update_keyword: Operation[BulkUpdateKeywordResponse] = Operation(
    id="bulkUpdateKeyword",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_keyword",
    resource="keywords",
    name="bulk_update",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkUpdateKeywordResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_create_keyword: Operation[object] = Operation(
    id="createKeyword",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/keyword",
    resource="keywords",
    name="create",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_keyword: Operation[Keyword] = Operation(
    id="getKeyword",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}",
    resource="keywords",
    name="get",
    params=(
        Param("campaign_id", "campaign_id", "path"),
        Param("keyword_id", "keyword_id", "path"),
    ),
    response=Keyword,
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
_get_keywords: Operation[KeywordPagedCollectionResponse] = Operation(
    id="getKeywords",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/keyword",
    resource="keywords",
    name="list",
    params=(
        Param("campaign_id", "campaign_id", "path"),
        Param("ad_group_ids", "ad_group_ids", "query"),
        Param("keyword_status", "keyword_status", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=KeywordPagedCollectionResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Keyword,
    paging=NextLink(
        items="keywords",
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
_update_keyword: Operation[UpdateKeywordResponse] = Operation(
    id="updateKeyword",
    method="PUT",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}",
    resource="keywords",
    name="update",
    params=(
        Param("campaign_id", "campaign_id", "path"),
        Param("keyword_id", "keyword_id", "path"),
    ),
    response=UpdateKeywordResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _bulk_create_keyword,
    _bulk_update_keyword,
    _create_keyword,
    _get_keyword,
    _get_keywords,
    _update_keyword,
)


class KeywordsApi(Resource):
    @checked
    def bulk_create(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateKeywordRequest, Mapping[str, Any]],
    ) -> BulkCreateKeywordResponse:
        """Create several keywords."""
        return self._call(
            _bulk_create_keyword,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_update(
        self,
        campaign_id: StrictStr,
        body: Union[BulkUpdateKeywordRequest, Mapping[str, Any]],
    ) -> BulkUpdateKeywordResponse:
        """Change the bids or status of several keywords."""
        return self._call(
            _bulk_update_keyword,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def create(
        self,
        campaign_id: StrictStr,
        body: Union[CreateKeywordRequest, Mapping[str, Any]],
    ) -> object:
        """Create a keyword in an ad group."""
        return self._call(
            _create_keyword,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def get(
        self,
        campaign_id: StrictStr,
        keyword_id: StrictStr,
    ) -> Keyword:
        """Get one keyword."""
        return self._call(
            _get_keyword,
            campaign_id=campaign_id,
            keyword_id=keyword_id,
        )

    @checked
    def list(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        keyword_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> KeywordPagedCollectionResponse:
        """List one page of a campaign's keywords."""
        return self._call(
            _get_keywords,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            keyword_status=keyword_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        keyword_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.Keyword]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_keywords,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            keyword_status=keyword_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def update(
        self,
        campaign_id: StrictStr,
        keyword_id: StrictStr,
        body: Union[UpdateKeywordRequest, Mapping[str, Any]],
    ) -> UpdateKeywordResponse:
        """Change the bid or status of a keyword."""
        return self._call(
            _update_keyword,
            campaign_id=campaign_id,
            keyword_id=keyword_id,
            _body=body,
        )


class AsyncKeywordsApi(AsyncResource):
    @checked
    async def bulk_create(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateKeywordRequest, Mapping[str, Any]],
    ) -> BulkCreateKeywordResponse:
        """Create several keywords."""
        return await self._call(
            _bulk_create_keyword,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_update(
        self,
        campaign_id: StrictStr,
        body: Union[BulkUpdateKeywordRequest, Mapping[str, Any]],
    ) -> BulkUpdateKeywordResponse:
        """Change the bids or status of several keywords."""
        return await self._call(
            _bulk_update_keyword,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def create(
        self,
        campaign_id: StrictStr,
        body: Union[CreateKeywordRequest, Mapping[str, Any]],
    ) -> object:
        """Create a keyword in an ad group."""
        return await self._call(
            _create_keyword,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def get(
        self,
        campaign_id: StrictStr,
        keyword_id: StrictStr,
    ) -> Keyword:
        """Get one keyword."""
        return await self._call(
            _get_keyword,
            campaign_id=campaign_id,
            keyword_id=keyword_id,
        )

    @checked
    async def list(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        keyword_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> KeywordPagedCollectionResponse:
        """List one page of a campaign's keywords."""
        return await self._call(
            _get_keywords,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            keyword_status=keyword_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        keyword_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Keyword]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_keywords,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            keyword_status=keyword_status,
            limit=limit,
            offset=offset,
        )

    @checked
    async def update(
        self,
        campaign_id: StrictStr,
        keyword_id: StrictStr,
        body: Union[UpdateKeywordRequest, Mapping[str, Any]],
    ) -> UpdateKeywordResponse:
        """Change the bid or status of a keyword."""
        return await self._call(
            _update_keyword,
            campaign_id=campaign_id,
            keyword_id=keyword_id,
            _body=body,
        )
