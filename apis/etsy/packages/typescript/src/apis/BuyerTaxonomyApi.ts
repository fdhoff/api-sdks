// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { BuyerTaxonomyNodeProperties, BuyerTaxonomyNodes, ErrorSchema } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getBuyerTaxonomyNodes: Operation = {
  id: 'getBuyerTaxonomyNodes',
  method: 'GET',
  path: '/v3/application/buyer-taxonomy/nodes',
  resource: 'buyerTaxonomy',
  name: 'listNodes',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getPropertiesByBuyerTaxonomyId: Operation = {
  id: 'getPropertiesByBuyerTaxonomyId',
  method: 'GET',
  path: '/v3/application/buyer-taxonomy/nodes/{taxonomy_id}/properties',
  resource: 'buyerTaxonomy',
  name: 'listProperties',
  params: [{ wire: 'taxonomy_id', name: 'taxonomyId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getBuyerTaxonomyNodes, getPropertiesByBuyerTaxonomyId];

export class BuyerTaxonomyApi extends Resource {
  /** List the buyer taxonomy tree. */
  listNodes(options?: RequestOptions): Promise<BuyerTaxonomyNodes> {
    return this.call(getBuyerTaxonomyNodes, undefined, {}, options);
  }

  /** List the properties of one buyer taxonomy node. */
  listProperties(taxonomyId: number, options?: RequestOptions): Promise<BuyerTaxonomyNodeProperties> {
    return this.call(getPropertiesByBuyerTaxonomyId, undefined, { taxonomyId }, options);
  }
}
