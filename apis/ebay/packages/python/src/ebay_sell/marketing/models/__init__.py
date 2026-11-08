# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

# import models into model package
from ebay_sell.marketing.models.ad import Ad
from ebay_sell.marketing.models.ad_group import AdGroup
from ebay_sell.marketing.models.ad_group_paged_collection_response import AdGroupPagedCollectionResponse
from ebay_sell.marketing.models.ad_ids import AdIds
from ebay_sell.marketing.models.ad_paged_collection_response import AdPagedCollectionResponse
from ebay_sell.marketing.models.ad_reference import AdReference
from ebay_sell.marketing.models.ad_references import AdReferences
from ebay_sell.marketing.models.ad_response import AdResponse
from ebay_sell.marketing.models.ad_update_response import AdUpdateResponse
from ebay_sell.marketing.models.ad_update_status_by_listing_id_response import AdUpdateStatusByListingIdResponse
from ebay_sell.marketing.models.ad_update_status_response import AdUpdateStatusResponse
from ebay_sell.marketing.models.additional_info import AdditionalInfo
from ebay_sell.marketing.models.additional_info_data import AdditionalInfoData
from ebay_sell.marketing.models.ads import Ads
from ebay_sell.marketing.models.alert import Alert
from ebay_sell.marketing.models.alert_details import AlertDetails
from ebay_sell.marketing.models.alert_dimension import AlertDimension
from ebay_sell.marketing.models.amount import Amount
from ebay_sell.marketing.models.aspect import Aspect
from ebay_sell.marketing.models.base_response import BaseResponse
from ebay_sell.marketing.models.bid_preference import BidPreference
from ebay_sell.marketing.models.budget import Budget
from ebay_sell.marketing.models.budget_recommendation_response import BudgetRecommendationResponse
from ebay_sell.marketing.models.budget_request import BudgetRequest
from ebay_sell.marketing.models.bulk_ad_response import BulkAdResponse
from ebay_sell.marketing.models.bulk_ad_update_response import BulkAdUpdateResponse
from ebay_sell.marketing.models.bulk_ad_update_status_by_listing_id_response import (
    BulkAdUpdateStatusByListingIdResponse,
)
from ebay_sell.marketing.models.bulk_ad_update_status_response import BulkAdUpdateStatusResponse
from ebay_sell.marketing.models.bulk_create_ad_request import BulkCreateAdRequest
from ebay_sell.marketing.models.bulk_create_ads_by_inventory_reference429_response import (
    BulkCreateAdsByInventoryReference429Response,
)
from ebay_sell.marketing.models.bulk_create_ads_by_inventory_reference_request import (
    BulkCreateAdsByInventoryReferenceRequest,
)
from ebay_sell.marketing.models.bulk_create_ads_by_inventory_reference_response import (
    BulkCreateAdsByInventoryReferenceResponse,
)
from ebay_sell.marketing.models.bulk_create_keyword_request import BulkCreateKeywordRequest
from ebay_sell.marketing.models.bulk_create_keyword_response import BulkCreateKeywordResponse
from ebay_sell.marketing.models.bulk_create_negative_keyword_request import BulkCreateNegativeKeywordRequest
from ebay_sell.marketing.models.bulk_create_negative_keyword_response import BulkCreateNegativeKeywordResponse
from ebay_sell.marketing.models.bulk_delete_ad_request import BulkDeleteAdRequest
from ebay_sell.marketing.models.bulk_delete_ad_response import BulkDeleteAdResponse
from ebay_sell.marketing.models.bulk_delete_ads_by_inventory_reference_request import (
    BulkDeleteAdsByInventoryReferenceRequest,
)
from ebay_sell.marketing.models.bulk_delete_ads_by_inventory_reference_response import (
    BulkDeleteAdsByInventoryReferenceResponse,
)
from ebay_sell.marketing.models.bulk_update_ad_status_by_listing_id_request import BulkUpdateAdStatusByListingIdRequest
from ebay_sell.marketing.models.bulk_update_ad_status_request import BulkUpdateAdStatusRequest
from ebay_sell.marketing.models.bulk_update_ads_by_inventory_reference_response import (
    BulkUpdateAdsByInventoryReferenceResponse,
)
from ebay_sell.marketing.models.bulk_update_keyword_request import BulkUpdateKeywordRequest
from ebay_sell.marketing.models.bulk_update_keyword_response import BulkUpdateKeywordResponse
from ebay_sell.marketing.models.bulk_update_negative_keyword_request import BulkUpdateNegativeKeywordRequest
from ebay_sell.marketing.models.bulk_update_negative_keyword_response import BulkUpdateNegativeKeywordResponse
from ebay_sell.marketing.models.campaign import Campaign
from ebay_sell.marketing.models.campaign_audience import CampaignAudience
from ebay_sell.marketing.models.campaign_budget import CampaignBudget
from ebay_sell.marketing.models.campaign_budget_request import CampaignBudgetRequest
from ebay_sell.marketing.models.campaign_criterion import CampaignCriterion
from ebay_sell.marketing.models.campaign_dto import CampaignDTO
from ebay_sell.marketing.models.campaign_paged_collection_response import CampaignPagedCollectionResponse
from ebay_sell.marketing.models.campaigns import Campaigns
from ebay_sell.marketing.models.clone_campaign_request import CloneCampaignRequest
from ebay_sell.marketing.models.coupon_configuration import CouponConfiguration
from ebay_sell.marketing.models.create_ad_group_request import CreateAdGroupRequest
from ebay_sell.marketing.models.create_ad_request import CreateAdRequest
from ebay_sell.marketing.models.create_ads_by_inventory_reference_request import CreateAdsByInventoryReferenceRequest
from ebay_sell.marketing.models.create_ads_by_inventory_reference_response import CreateAdsByInventoryReferenceResponse
from ebay_sell.marketing.models.create_campaign_request import CreateCampaignRequest
from ebay_sell.marketing.models.create_email_campaign_request import CreateEmailCampaignRequest
from ebay_sell.marketing.models.create_email_campaign_response import CreateEmailCampaignResponse
from ebay_sell.marketing.models.create_keyword_request import CreateKeywordRequest
from ebay_sell.marketing.models.create_negative_keyword_request import CreateNegativeKeywordRequest
from ebay_sell.marketing.models.create_report_task import CreateReportTask
from ebay_sell.marketing.models.delete_ad_request import DeleteAdRequest
from ebay_sell.marketing.models.delete_ad_response import DeleteAdResponse
from ebay_sell.marketing.models.delete_ads_by_inventory_reference_request import DeleteAdsByInventoryReferenceRequest
from ebay_sell.marketing.models.delete_ads_by_inventory_reference_response import DeleteAdsByInventoryReferenceResponse
from ebay_sell.marketing.models.delete_email_campaign_response import DeleteEmailCampaignResponse
from ebay_sell.marketing.models.dimension import Dimension
from ebay_sell.marketing.models.dimension_key_annotation import DimensionKeyAnnotation
from ebay_sell.marketing.models.dimension_metadata import DimensionMetadata
from ebay_sell.marketing.models.discount_benefit import DiscountBenefit
from ebay_sell.marketing.models.discount_rule import DiscountRule
from ebay_sell.marketing.models.discount_specification import DiscountSpecification
from ebay_sell.marketing.models.dynamic_ad_rate_preference import DynamicAdRatePreference
from ebay_sell.marketing.models.error import Error
from ebay_sell.marketing.models.error_parameter import ErrorParameter
from ebay_sell.marketing.models.funding_strategy import FundingStrategy
from ebay_sell.marketing.models.get_email_campaign_audiences_response import GetEmailCampaignAudiencesResponse
from ebay_sell.marketing.models.get_email_campaign_response import GetEmailCampaignResponse
from ebay_sell.marketing.models.get_email_campaigns_response import GetEmailCampaignsResponse
from ebay_sell.marketing.models.get_email_preview_response import GetEmailPreviewResponse
from ebay_sell.marketing.models.get_email_report_response import GetEmailReportResponse
from ebay_sell.marketing.models.inventory_criterion import InventoryCriterion
from ebay_sell.marketing.models.inventory_item import InventoryItem
from ebay_sell.marketing.models.inventory_reference import InventoryReference
from ebay_sell.marketing.models.item_basis import ItemBasis
from ebay_sell.marketing.models.item_markdown_status import ItemMarkdownStatus
from ebay_sell.marketing.models.item_price_markdown import ItemPriceMarkdown
from ebay_sell.marketing.models.item_promotion import ItemPromotion
from ebay_sell.marketing.models.item_promotion_response import ItemPromotionResponse
from ebay_sell.marketing.models.items_paged_collection import ItemsPagedCollection
from ebay_sell.marketing.models.keyword import Keyword
from ebay_sell.marketing.models.keyword_paged_collection_response import KeywordPagedCollectionResponse
from ebay_sell.marketing.models.keyword_request import KeywordRequest
from ebay_sell.marketing.models.keyword_response import KeywordResponse
from ebay_sell.marketing.models.listing_detail import ListingDetail
from ebay_sell.marketing.models.max_cpc import MaxCpc
from ebay_sell.marketing.models.metric_metadata import MetricMetadata
from ebay_sell.marketing.models.negative_keyword import NegativeKeyword
from ebay_sell.marketing.models.negative_keyword_paged_collection_response import NegativeKeywordPagedCollectionResponse
from ebay_sell.marketing.models.negative_keyword_response import NegativeKeywordResponse
from ebay_sell.marketing.models.price_range import PriceRange
from ebay_sell.marketing.models.promotion_detail import PromotionDetail
from ebay_sell.marketing.models.promotion_report_detail import PromotionReportDetail
from ebay_sell.marketing.models.promotions_paged_collection import PromotionsPagedCollection
from ebay_sell.marketing.models.promotions_report_paged_collection import PromotionsReportPagedCollection
from ebay_sell.marketing.models.proposed_bid import ProposedBid
from ebay_sell.marketing.models.report_metadata import ReportMetadata
from ebay_sell.marketing.models.report_metadatas import ReportMetadatas
from ebay_sell.marketing.models.report_task import ReportTask
from ebay_sell.marketing.models.report_task_paged_collection import ReportTaskPagedCollection
from ebay_sell.marketing.models.rule_criteria import RuleCriteria
from ebay_sell.marketing.models.selected_inventory_discount import SelectedInventoryDiscount
from ebay_sell.marketing.models.selection_rule import SelectionRule
from ebay_sell.marketing.models.suggest_budget_response import SuggestBudgetResponse
from ebay_sell.marketing.models.suggest_max_cpc_request import SuggestMaxCpcRequest
from ebay_sell.marketing.models.suggest_max_cpc_response import SuggestMaxCpcResponse
from ebay_sell.marketing.models.suggested_bids import SuggestedBids
from ebay_sell.marketing.models.suggested_keywords import SuggestedKeywords
from ebay_sell.marketing.models.summary_report_response import SummaryReportResponse
from ebay_sell.marketing.models.targeted_ads_paged_collection import TargetedAdsPagedCollection
from ebay_sell.marketing.models.targeted_bid_request import TargetedBidRequest
from ebay_sell.marketing.models.targeted_bids_paged_collection import TargetedBidsPagedCollection
from ebay_sell.marketing.models.targeted_keyword_request import TargetedKeywordRequest
from ebay_sell.marketing.models.targeted_keywords_paged_collection import TargetedKeywordsPagedCollection
from ebay_sell.marketing.models.targeting_items import TargetingItems
from ebay_sell.marketing.models.update_ad_group_request import UpdateAdGroupRequest
from ebay_sell.marketing.models.update_ad_status_by_listing_id_request import UpdateAdStatusByListingIdRequest
from ebay_sell.marketing.models.update_ad_status_request import UpdateAdStatusRequest
from ebay_sell.marketing.models.update_adrate_strategy_request import UpdateAdrateStrategyRequest
from ebay_sell.marketing.models.update_ads_by_inventory_reference_response import UpdateAdsByInventoryReferenceResponse
from ebay_sell.marketing.models.update_bid_percentage_request import UpdateBidPercentageRequest
from ebay_sell.marketing.models.update_bidding_strategy_request import UpdateBiddingStrategyRequest
from ebay_sell.marketing.models.update_campaign_budget_request import UpdateCampaignBudgetRequest
from ebay_sell.marketing.models.update_campaign_identification_request import UpdateCampaignIdentificationRequest
from ebay_sell.marketing.models.update_campaign_request import UpdateCampaignRequest
from ebay_sell.marketing.models.update_email_campaign_response import UpdateEmailCampaignResponse
from ebay_sell.marketing.models.update_keyword_by_keyword_id_request import UpdateKeywordByKeywordIdRequest
from ebay_sell.marketing.models.update_keyword_request import UpdateKeywordRequest
from ebay_sell.marketing.models.update_keyword_response import UpdateKeywordResponse
from ebay_sell.marketing.models.update_negative_keyword_id_request import UpdateNegativeKeywordIdRequest
from ebay_sell.marketing.models.update_negative_keyword_request import UpdateNegativeKeywordRequest
from ebay_sell.marketing.models.update_negative_keyword_response import UpdateNegativeKeywordResponse


__all__ = [
    "Ad",
    "AdGroup",
    "AdGroupPagedCollectionResponse",
    "AdIds",
    "AdPagedCollectionResponse",
    "AdReference",
    "AdReferences",
    "AdResponse",
    "AdUpdateResponse",
    "AdUpdateStatusByListingIdResponse",
    "AdUpdateStatusResponse",
    "AdditionalInfo",
    "AdditionalInfoData",
    "Ads",
    "Alert",
    "AlertDetails",
    "AlertDimension",
    "Amount",
    "Aspect",
    "BaseResponse",
    "BidPreference",
    "Budget",
    "BudgetRecommendationResponse",
    "BudgetRequest",
    "BulkAdResponse",
    "BulkAdUpdateResponse",
    "BulkAdUpdateStatusByListingIdResponse",
    "BulkAdUpdateStatusResponse",
    "BulkCreateAdRequest",
    "BulkCreateAdsByInventoryReference429Response",
    "BulkCreateAdsByInventoryReferenceRequest",
    "BulkCreateAdsByInventoryReferenceResponse",
    "BulkCreateKeywordRequest",
    "BulkCreateKeywordResponse",
    "BulkCreateNegativeKeywordRequest",
    "BulkCreateNegativeKeywordResponse",
    "BulkDeleteAdRequest",
    "BulkDeleteAdResponse",
    "BulkDeleteAdsByInventoryReferenceRequest",
    "BulkDeleteAdsByInventoryReferenceResponse",
    "BulkUpdateAdStatusByListingIdRequest",
    "BulkUpdateAdStatusRequest",
    "BulkUpdateAdsByInventoryReferenceResponse",
    "BulkUpdateKeywordRequest",
    "BulkUpdateKeywordResponse",
    "BulkUpdateNegativeKeywordRequest",
    "BulkUpdateNegativeKeywordResponse",
    "Campaign",
    "CampaignAudience",
    "CampaignBudget",
    "CampaignBudgetRequest",
    "CampaignCriterion",
    "CampaignDTO",
    "CampaignPagedCollectionResponse",
    "Campaigns",
    "CloneCampaignRequest",
    "CouponConfiguration",
    "CreateAdGroupRequest",
    "CreateAdRequest",
    "CreateAdsByInventoryReferenceRequest",
    "CreateAdsByInventoryReferenceResponse",
    "CreateCampaignRequest",
    "CreateEmailCampaignRequest",
    "CreateEmailCampaignResponse",
    "CreateKeywordRequest",
    "CreateNegativeKeywordRequest",
    "CreateReportTask",
    "DeleteAdRequest",
    "DeleteAdResponse",
    "DeleteAdsByInventoryReferenceRequest",
    "DeleteAdsByInventoryReferenceResponse",
    "DeleteEmailCampaignResponse",
    "Dimension",
    "DimensionKeyAnnotation",
    "DimensionMetadata",
    "DiscountBenefit",
    "DiscountRule",
    "DiscountSpecification",
    "DynamicAdRatePreference",
    "Error",
    "ErrorParameter",
    "FundingStrategy",
    "GetEmailCampaignAudiencesResponse",
    "GetEmailCampaignResponse",
    "GetEmailCampaignsResponse",
    "GetEmailPreviewResponse",
    "GetEmailReportResponse",
    "InventoryCriterion",
    "InventoryItem",
    "InventoryReference",
    "ItemBasis",
    "ItemMarkdownStatus",
    "ItemPriceMarkdown",
    "ItemPromotion",
    "ItemPromotionResponse",
    "ItemsPagedCollection",
    "Keyword",
    "KeywordPagedCollectionResponse",
    "KeywordRequest",
    "KeywordResponse",
    "ListingDetail",
    "MaxCpc",
    "MetricMetadata",
    "NegativeKeyword",
    "NegativeKeywordPagedCollectionResponse",
    "NegativeKeywordResponse",
    "PriceRange",
    "PromotionDetail",
    "PromotionReportDetail",
    "PromotionsPagedCollection",
    "PromotionsReportPagedCollection",
    "ProposedBid",
    "ReportMetadata",
    "ReportMetadatas",
    "ReportTask",
    "ReportTaskPagedCollection",
    "RuleCriteria",
    "SelectedInventoryDiscount",
    "SelectionRule",
    "SuggestBudgetResponse",
    "SuggestMaxCpcRequest",
    "SuggestMaxCpcResponse",
    "SuggestedBids",
    "SuggestedKeywords",
    "SummaryReportResponse",
    "TargetedAdsPagedCollection",
    "TargetedBidRequest",
    "TargetedBidsPagedCollection",
    "TargetedKeywordRequest",
    "TargetedKeywordsPagedCollection",
    "TargetingItems",
    "UpdateAdGroupRequest",
    "UpdateAdStatusByListingIdRequest",
    "UpdateAdStatusRequest",
    "UpdateAdrateStrategyRequest",
    "UpdateAdsByInventoryReferenceResponse",
    "UpdateBidPercentageRequest",
    "UpdateBiddingStrategyRequest",
    "UpdateCampaignBudgetRequest",
    "UpdateCampaignIdentificationRequest",
    "UpdateCampaignRequest",
    "UpdateEmailCampaignResponse",
    "UpdateKeywordByKeywordIdRequest",
    "UpdateKeywordRequest",
    "UpdateKeywordResponse",
    "UpdateNegativeKeywordIdRequest",
    "UpdateNegativeKeywordRequest",
    "UpdateNegativeKeywordResponse",
]
