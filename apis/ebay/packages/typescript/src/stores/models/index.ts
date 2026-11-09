// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface AddStoreCategoryRequestType {
  categoryName?: string;
  destinationParentCategoryId?: string;
  listingDestinationCategoryId?: string;
}

export interface DeleteStoreCategoryRequestType {
  listingDestinationCategoryId?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface GetStoreCategories429Response {
  errors?: Array<Error>;
}

export interface GetStoreCategoriesResponseType {
  storeCategories?: Array<StoreCategoryType>;
}

export interface GetStoreResponseType {
  description?: string;
  lastOpenedTime?: string;
  logo?: StoreLogoType;
  name?: string;
  url?: string;
  urlPath?: string;
}

export interface GetStoreTaskResponseType {
  task?: StoreTaskType;
}

export interface GetStoreTasksResponseType {
  task?: Array<StoreTaskType>;
}

export interface ModelError {
  category?: string;
  domain?: string;
  errorId?: number;
  inputRefIds?: Array<string>;
  longMessage?: string;
  message?: string;
  outputRefIds?: Array<string>;
  parameters?: Array<ErrorParameter>;
  subdomain?: string;
}

export interface MoveStoreCategoryRequestType {
  categoryId?: string;
  destinationParentCategoryId?: string;
  listingDestinationCategoryId?: string;
}

export interface RenameStoreCategoryRequestType {
  categoryName?: string;
}

export interface StoreCategoryType {
  categoryId?: string;
  categoryName?: string;
  childrenCategories?: Array<StoreCategoryType>;
  level?: number;
  order?: number;
}

export interface StoreLogoType {
  url?: string;
}

export interface StoreTaskType {
  id?: string;
  message?: string;
  status?: string;
  type?: string;
}
