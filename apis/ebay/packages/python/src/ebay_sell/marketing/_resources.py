# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.marketing.api import (
    ad_groups_api,
    ads_api,
    campaigns_api,
    email_campaigns_api,
    item_price_markdowns_api,
    item_promotions_api,
    keywords_api,
    negative_keywords_api,
    promotion_reports_api,
    promotions_api,
    report_metadata_api,
    report_tasks_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        ad_groups_api.OPERATIONS,
        ads_api.OPERATIONS,
        campaigns_api.OPERATIONS,
        email_campaigns_api.OPERATIONS,
        item_price_markdowns_api.OPERATIONS,
        item_promotions_api.OPERATIONS,
        keywords_api.OPERATIONS,
        negative_keywords_api.OPERATIONS,
        promotion_reports_api.OPERATIONS,
        promotions_api.OPERATIONS,
        report_metadata_api.OPERATIONS,
        report_tasks_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.ad_groups = ad_groups_api.AdGroupsApi(transport)
        self.ads = ads_api.AdsApi(transport)
        self.campaigns = campaigns_api.CampaignsApi(transport)
        self.email_campaigns = email_campaigns_api.EmailCampaignsApi(transport)
        self.item_price_markdowns = item_price_markdowns_api.ItemPriceMarkdownsApi(transport)
        self.item_promotions = item_promotions_api.ItemPromotionsApi(transport)
        self.keywords = keywords_api.KeywordsApi(transport)
        self.negative_keywords = negative_keywords_api.NegativeKeywordsApi(transport)
        self.promotion_reports = promotion_reports_api.PromotionReportsApi(transport)
        self.promotions = promotions_api.PromotionsApi(transport)
        self.report_metadata = report_metadata_api.ReportMetadataApi(transport)
        self.report_tasks = report_tasks_api.ReportTasksApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.ad_groups = ad_groups_api.AsyncAdGroupsApi(transport)
        self.ads = ads_api.AsyncAdsApi(transport)
        self.campaigns = campaigns_api.AsyncCampaignsApi(transport)
        self.email_campaigns = email_campaigns_api.AsyncEmailCampaignsApi(transport)
        self.item_price_markdowns = item_price_markdowns_api.AsyncItemPriceMarkdownsApi(transport)
        self.item_promotions = item_promotions_api.AsyncItemPromotionsApi(transport)
        self.keywords = keywords_api.AsyncKeywordsApi(transport)
        self.negative_keywords = negative_keywords_api.AsyncNegativeKeywordsApi(transport)
        self.promotion_reports = promotion_reports_api.AsyncPromotionReportsApi(transport)
        self.promotions = promotions_api.AsyncPromotionsApi(transport)
        self.report_metadata = report_metadata_api.AsyncReportMetadataApi(transport)
        self.report_tasks = report_tasks_api.AsyncReportTasksApi(transport)
