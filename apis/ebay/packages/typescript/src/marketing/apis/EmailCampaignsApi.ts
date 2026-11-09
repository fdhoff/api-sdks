// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateAdsByInventoryReference429Response,
  CreateEmailCampaignRequest,
  CreateEmailCampaignResponse,
  DeleteEmailCampaignResponse,
  GetEmailCampaignAudiencesResponse,
  GetEmailCampaignResponse,
  GetEmailCampaignsResponse,
  GetEmailPreviewResponse,
  GetEmailReportResponse,
  UpdateCampaignRequest,
  UpdateEmailCampaignResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createEmailCampaign: Operation = {
  id: 'createEmailCampaign',
  method: 'POST',
  path: '/sell/marketing/v1/email_campaign',
  resource: 'emailCampaigns',
  name: 'create',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const deleteEmailCampaign: Operation = {
  id: 'deleteEmailCampaign',
  method: 'DELETE',
  path: '/sell/marketing/v1/email_campaign/{email_campaign_id}',
  resource: 'emailCampaigns',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'email_campaign_id', name: 'emailCampaignId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getAudiences: Operation = {
  id: 'getAudiences',
  method: 'GET',
  path: '/sell/marketing/v1/email_campaign/audience',
  resource: 'emailCampaigns',
  name: 'listAudiences',
  host: 'api',
  params: [
    { wire: 'emailCampaignType', name: 'emailCampaignType', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterAudiences',
  paging: { style: 'next_link', items: 'audiences', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getEmailCampaign: Operation = {
  id: 'getEmailCampaign',
  method: 'GET',
  path: '/sell/marketing/v1/email_campaign/{email_campaign_id}',
  resource: 'emailCampaigns',
  name: 'get',
  host: 'api',
  params: [{ wire: 'email_campaign_id', name: 'emailCampaignId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getEmailCampaigns: Operation = {
  id: 'getEmailCampaigns',
  method: 'GET',
  path: '/sell/marketing/v1/email_campaign',
  resource: 'emailCampaigns',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'campaigns', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getEmailPreview: Operation = {
  id: 'getEmailPreview',
  method: 'GET',
  path: '/sell/marketing/v1/email_campaign/{email_campaign_id}/email_preview',
  resource: 'emailCampaigns',
  name: 'getPreview',
  host: 'api',
  params: [{ wire: 'email_campaign_id', name: 'emailCampaignId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getEmailReport: Operation = {
  id: 'getEmailReport',
  method: 'GET',
  path: '/sell/marketing/v1/email_campaign/report',
  resource: 'emailCampaigns',
  name: 'getReport',
  host: 'api',
  params: [
    { wire: 'endDate', name: 'endDate', location: 'query' },
    { wire: 'startDate', name: 'startDate', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const updateEmailCampaign: Operation = {
  id: 'updateEmailCampaign',
  method: 'PUT',
  path: '/sell/marketing/v1/email_campaign/{email_campaign_id}',
  resource: 'emailCampaigns',
  name: 'update',
  host: 'api',
  params: [{ wire: 'email_campaign_id', name: 'emailCampaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createEmailCampaign,
  deleteEmailCampaign,
  getAudiences,
  getEmailCampaign,
  getEmailCampaigns,
  getEmailPreview,
  getEmailReport,
  updateEmailCampaign,
];

export class EmailCampaignsApi extends Resource {
  /** Create a store email campaign. */
  create(
    body: CreateEmailCampaignRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<CreateEmailCampaignResponse> {
    return this.call(createEmailCampaign, body, { ...params }, options);
  }

  /** Delete an email campaign. */
  delete(emailCampaignId: string, options?: RequestOptions): Promise<DeleteEmailCampaignResponse> {
    return this.call(deleteEmailCampaign, undefined, { emailCampaignId }, options);
  }

  /** List one page of the audiences an email campaign can target. */
  listAudiences(
    params: { emailCampaignType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): Promise<GetEmailCampaignAudiencesResponse> {
    return this.call(getAudiences, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterAudiences(
    params: { emailCampaignType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): AsyncGenerator<models.CampaignAudience, void, undefined> {
    return this.paginate(getAudiences, undefined, { ...params }, options);
  }

  /** Get one email campaign. */
  get(emailCampaignId: string, options?: RequestOptions): Promise<GetEmailCampaignResponse> {
    return this.call(getEmailCampaign, undefined, { emailCampaignId }, options);
  }

  /** List one page of the seller's store email campaigns. */
  list(
    params: { limit?: string; offset?: string; q?: string; sort?: string } = {},
    options?: RequestOptions,
  ): Promise<GetEmailCampaignsResponse> {
    return this.call(getEmailCampaigns, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: string; offset?: string; q?: string; sort?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.CampaignDTO, void, undefined> {
    return this.paginate(getEmailCampaigns, undefined, { ...params }, options);
  }

  /** Preview the email of a campaign. */
  getPreview(emailCampaignId: string, options?: RequestOptions): Promise<GetEmailPreviewResponse> {
    return this.call(getEmailPreview, undefined, { emailCampaignId }, options);
  }

  /** Get the performance of the seller's email campaigns. */
  getReport(params: { endDate: string; startDate: string }, options?: RequestOptions): Promise<GetEmailReportResponse> {
    return this.call(getEmailReport, undefined, { ...params }, options);
  }

  /** Update an email campaign. */
  update(
    emailCampaignId: string,
    body: UpdateCampaignRequest,
    options?: RequestOptions,
  ): Promise<UpdateEmailCampaignResponse> {
    return this.call(updateEmailCampaign, body, { emailCampaignId }, options);
  }
}
