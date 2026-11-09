// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { AdGroupsApi, OPERATIONS as AdGroupsApiOperations } from './apis/AdGroupsApi.js';
import { AdsApi, OPERATIONS as AdsApiOperations } from './apis/AdsApi.js';
import { CampaignsApi, OPERATIONS as CampaignsApiOperations } from './apis/CampaignsApi.js';
import { EmailCampaignsApi, OPERATIONS as EmailCampaignsApiOperations } from './apis/EmailCampaignsApi.js';
import { ItemPriceMarkdownsApi, OPERATIONS as ItemPriceMarkdownsApiOperations } from './apis/ItemPriceMarkdownsApi.js';
import { ItemPromotionsApi, OPERATIONS as ItemPromotionsApiOperations } from './apis/ItemPromotionsApi.js';
import { KeywordsApi, OPERATIONS as KeywordsApiOperations } from './apis/KeywordsApi.js';
import { NegativeKeywordsApi, OPERATIONS as NegativeKeywordsApiOperations } from './apis/NegativeKeywordsApi.js';
import { PromotionReportsApi, OPERATIONS as PromotionReportsApiOperations } from './apis/PromotionReportsApi.js';
import { PromotionsApi, OPERATIONS as PromotionsApiOperations } from './apis/PromotionsApi.js';
import { ReportMetadataApi, OPERATIONS as ReportMetadataApiOperations } from './apis/ReportMetadataApi.js';
import { ReportTasksApi, OPERATIONS as ReportTasksApiOperations } from './apis/ReportTasksApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...AdGroupsApiOperations,
    ...AdsApiOperations,
    ...CampaignsApiOperations,
    ...EmailCampaignsApiOperations,
    ...ItemPriceMarkdownsApiOperations,
    ...ItemPromotionsApiOperations,
    ...KeywordsApiOperations,
    ...NegativeKeywordsApiOperations,
    ...PromotionReportsApiOperations,
    ...PromotionsApiOperations,
    ...ReportMetadataApiOperations,
    ...ReportTasksApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly adGroups: AdGroupsApi;
  readonly ads: AdsApi;
  readonly campaigns: CampaignsApi;
  readonly emailCampaigns: EmailCampaignsApi;
  readonly itemPriceMarkdowns: ItemPriceMarkdownsApi;
  readonly itemPromotions: ItemPromotionsApi;
  readonly keywords: KeywordsApi;
  readonly negativeKeywords: NegativeKeywordsApi;
  readonly promotionReports: PromotionReportsApi;
  readonly promotions: PromotionsApi;
  readonly reportMetadata: ReportMetadataApi;
  readonly reportTasks: ReportTasksApi;

  constructor(transport: Transport) {
    this.adGroups = new AdGroupsApi(transport);
    this.ads = new AdsApi(transport);
    this.campaigns = new CampaignsApi(transport);
    this.emailCampaigns = new EmailCampaignsApi(transport);
    this.itemPriceMarkdowns = new ItemPriceMarkdownsApi(transport);
    this.itemPromotions = new ItemPromotionsApi(transport);
    this.keywords = new KeywordsApi(transport);
    this.negativeKeywords = new NegativeKeywordsApi(transport);
    this.promotionReports = new PromotionReportsApi(transport);
    this.promotions = new PromotionsApi(transport);
    this.reportMetadata = new ReportMetadataApi(transport);
    this.reportTasks = new ReportTasksApi(transport);
  }
}
