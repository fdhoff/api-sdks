// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { ApplicationApi, OPERATIONS as ApplicationApiOperations } from './apis/ApplicationApi.js';
import { BuyerTaxonomyApi, OPERATIONS as BuyerTaxonomyApiOperations } from './apis/BuyerTaxonomyApi.js';
import { EconomicOperatorsApi, OPERATIONS as EconomicOperatorsApiOperations } from './apis/EconomicOperatorsApi.js';
import { HolidayPreferencesApi, OPERATIONS as HolidayPreferencesApiOperations } from './apis/HolidayPreferencesApi.js';
import { LedgerEntriesApi, OPERATIONS as LedgerEntriesApiOperations } from './apis/LedgerEntriesApi.js';
import { ListingFilesApi, OPERATIONS as ListingFilesApiOperations } from './apis/ListingFilesApi.js';
import { ListingImagesApi, OPERATIONS as ListingImagesApiOperations } from './apis/ListingImagesApi.js';
import { ListingInventoryApi, OPERATIONS as ListingInventoryApiOperations } from './apis/ListingInventoryApi.js';
import {
  ListingPersonalizationApi,
  OPERATIONS as ListingPersonalizationApiOperations,
} from './apis/ListingPersonalizationApi.js';
import { ListingPropertiesApi, OPERATIONS as ListingPropertiesApiOperations } from './apis/ListingPropertiesApi.js';
import {
  ListingTranslationsApi,
  OPERATIONS as ListingTranslationsApiOperations,
} from './apis/ListingTranslationsApi.js';
import {
  ListingVariationImagesApi,
  OPERATIONS as ListingVariationImagesApiOperations,
} from './apis/ListingVariationImagesApi.js';
import { ListingVideosApi, OPERATIONS as ListingVideosApiOperations } from './apis/ListingVideosApi.js';
import { ListingsApi, OPERATIONS as ListingsApiOperations } from './apis/ListingsApi.js';
import { PaymentsApi, OPERATIONS as PaymentsApiOperations } from './apis/PaymentsApi.js';
import { ProcessingProfilesApi, OPERATIONS as ProcessingProfilesApiOperations } from './apis/ProcessingProfilesApi.js';
import { ProductionPartnersApi, OPERATIONS as ProductionPartnersApiOperations } from './apis/ProductionPartnersApi.js';
import { ReceiptsApi, OPERATIONS as ReceiptsApiOperations } from './apis/ReceiptsApi.js';
import { ReturnPoliciesApi, OPERATIONS as ReturnPoliciesApiOperations } from './apis/ReturnPoliciesApi.js';
import { ReviewsApi, OPERATIONS as ReviewsApiOperations } from './apis/ReviewsApi.js';
import { SellerTaxonomyApi, OPERATIONS as SellerTaxonomyApiOperations } from './apis/SellerTaxonomyApi.js';
import { ShippingProfilesApi, OPERATIONS as ShippingProfilesApiOperations } from './apis/ShippingProfilesApi.js';
import { ShopSectionsApi, OPERATIONS as ShopSectionsApiOperations } from './apis/ShopSectionsApi.js';
import { ShopsApi, OPERATIONS as ShopsApiOperations } from './apis/ShopsApi.js';
import { TransactionsApi, OPERATIONS as TransactionsApiOperations } from './apis/TransactionsApi.js';
import { UserAddressesApi, OPERATIONS as UserAddressesApiOperations } from './apis/UserAddressesApi.js';
import { UsersApi, OPERATIONS as UsersApiOperations } from './apis/UsersApi.js';
import type { Operation, Transport } from './runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...ApplicationApiOperations,
    ...BuyerTaxonomyApiOperations,
    ...EconomicOperatorsApiOperations,
    ...HolidayPreferencesApiOperations,
    ...LedgerEntriesApiOperations,
    ...ListingFilesApiOperations,
    ...ListingImagesApiOperations,
    ...ListingInventoryApiOperations,
    ...ListingPersonalizationApiOperations,
    ...ListingPropertiesApiOperations,
    ...ListingTranslationsApiOperations,
    ...ListingVariationImagesApiOperations,
    ...ListingVideosApiOperations,
    ...ListingsApiOperations,
    ...PaymentsApiOperations,
    ...ProcessingProfilesApiOperations,
    ...ProductionPartnersApiOperations,
    ...ReceiptsApiOperations,
    ...ReturnPoliciesApiOperations,
    ...ReviewsApiOperations,
    ...SellerTaxonomyApiOperations,
    ...ShippingProfilesApiOperations,
    ...ShopSectionsApiOperations,
    ...ShopsApiOperations,
    ...TransactionsApiOperations,
    ...UserAddressesApiOperations,
    ...UsersApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly application: ApplicationApi;
  readonly buyerTaxonomy: BuyerTaxonomyApi;
  readonly economicOperators: EconomicOperatorsApi;
  readonly holidayPreferences: HolidayPreferencesApi;
  readonly ledgerEntries: LedgerEntriesApi;
  readonly listingFiles: ListingFilesApi;
  readonly listingImages: ListingImagesApi;
  readonly listingInventory: ListingInventoryApi;
  readonly listingPersonalization: ListingPersonalizationApi;
  readonly listingProperties: ListingPropertiesApi;
  readonly listingTranslations: ListingTranslationsApi;
  readonly listingVariationImages: ListingVariationImagesApi;
  readonly listingVideos: ListingVideosApi;
  readonly listings: ListingsApi;
  readonly payments: PaymentsApi;
  readonly processingProfiles: ProcessingProfilesApi;
  readonly productionPartners: ProductionPartnersApi;
  readonly receipts: ReceiptsApi;
  readonly returnPolicies: ReturnPoliciesApi;
  readonly reviews: ReviewsApi;
  readonly sellerTaxonomy: SellerTaxonomyApi;
  readonly shippingProfiles: ShippingProfilesApi;
  readonly shopSections: ShopSectionsApi;
  readonly shops: ShopsApi;
  readonly transactions: TransactionsApi;
  readonly userAddresses: UserAddressesApi;
  readonly users: UsersApi;

  constructor(transport: Transport) {
    this.application = new ApplicationApi(transport);
    this.buyerTaxonomy = new BuyerTaxonomyApi(transport);
    this.economicOperators = new EconomicOperatorsApi(transport);
    this.holidayPreferences = new HolidayPreferencesApi(transport);
    this.ledgerEntries = new LedgerEntriesApi(transport);
    this.listingFiles = new ListingFilesApi(transport);
    this.listingImages = new ListingImagesApi(transport);
    this.listingInventory = new ListingInventoryApi(transport);
    this.listingPersonalization = new ListingPersonalizationApi(transport);
    this.listingProperties = new ListingPropertiesApi(transport);
    this.listingTranslations = new ListingTranslationsApi(transport);
    this.listingVariationImages = new ListingVariationImagesApi(transport);
    this.listingVideos = new ListingVideosApi(transport);
    this.listings = new ListingsApi(transport);
    this.payments = new PaymentsApi(transport);
    this.processingProfiles = new ProcessingProfilesApi(transport);
    this.productionPartners = new ProductionPartnersApi(transport);
    this.receipts = new ReceiptsApi(transport);
    this.returnPolicies = new ReturnPoliciesApi(transport);
    this.reviews = new ReviewsApi(transport);
    this.sellerTaxonomy = new SellerTaxonomyApi(transport);
    this.shippingProfiles = new ShippingProfilesApi(transport);
    this.shopSections = new ShopSectionsApi(transport);
    this.shops = new ShopsApi(transport);
    this.transactions = new TransactionsApi(transport);
    this.userAddresses = new UserAddressesApi(transport);
    this.users = new UsersApi(transport);
  }
}
