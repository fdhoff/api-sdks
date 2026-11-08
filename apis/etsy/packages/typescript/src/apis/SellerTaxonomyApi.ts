// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, SellerTaxonomyNodes, TaxonomyNodeProperties } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getPropertiesByTaxonomyId: Operation = {
  id: 'getPropertiesByTaxonomyId',
  method: 'GET',
  path: '/v3/application/seller-taxonomy/nodes/{taxonomy_id}/properties',
  resource: 'sellerTaxonomy',
  name: 'listProperties',
  params: [
    { wire: 'taxonomy_id', name: 'taxonomyId', location: 'path' },
    { wire: 'supports_variations', name: 'supportsVariations', location: 'query' },
    { wire: 'supports_attributes', name: 'supportsAttributes', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getSellerTaxonomyNodes: Operation = {
  id: 'getSellerTaxonomyNodes',
  method: 'GET',
  path: '/v3/application/seller-taxonomy/nodes',
  resource: 'sellerTaxonomy',
  name: 'listNodes',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getPropertiesByTaxonomyId, getSellerTaxonomyNodes];

export class SellerTaxonomyApi extends Resource {
  /** List the properties of one seller taxonomy node. */
  listProperties(
    taxonomyId: number,
    params: { supportsVariations?: boolean; supportsAttributes?: boolean } = {},
    options?: RequestOptions,
  ): Promise<TaxonomyNodeProperties> {
    return this.call(getPropertiesByTaxonomyId, undefined, { taxonomyId, ...params }, options);
  }

  /** List the seller taxonomy tree. */
  listNodes(options?: RequestOptions): Promise<SellerTaxonomyNodes> {
    return this.call(getSellerTaxonomyNodes, undefined, {}, options);
  }
}
