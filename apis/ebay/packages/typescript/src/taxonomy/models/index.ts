// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface AncestorReference {
  categoryId?: string;
  categoryName?: string;
  categorySubtreeNodeHref?: string;
  categoryTreeNodeLevel?: number;
}

export interface Aspect {
  aspectConstraint?: AspectConstraint;
  aspectValues?: Array<AspectValue>;
  localizedAspectName?: string;
  relevanceIndicator?: RelevanceIndicator;
}

export interface AspectConstraint {
  aspectApplicableTo?: Array<string>;
  aspectDataType?: string;
  aspectEnabledForVariations?: boolean;
  aspectFormat?: string;
  aspectMaxLength?: number;
  aspectMode?: string;
  aspectRequired?: boolean;
  aspectUsage?: string;
  expectedRequiredByDate?: string;
  itemToAspectCardinality?: string;
  aspectAdvancedDataType?: string;
}

export interface AspectMetadata {
  aspects?: Array<Aspect>;
}

export interface AspectValue {
  localizedValue?: string;
  valueConstraints?: Array<ValueConstraint>;
}

export interface BaseCategoryTree {
  categoryTreeId?: string;
  categoryTreeVersion?: string;
}

export interface Category {
  categoryId?: string;
  categoryName?: string;
}

export interface CategoryAspect {
  category?: Category;
  aspects?: Array<Aspect>;
}

export interface CategorySubtree {
  categorySubtreeNode?: CategoryTreeNode;
  categoryTreeId?: string;
  categoryTreeVersion?: string;
}

export interface CategorySuggestion {
  category?: Category;
  categoryTreeNodeAncestors?: Array<AncestorReference>;
  categoryTreeNodeLevel?: number;
  relevancy?: string;
}

export interface CategorySuggestionResponse {
  categorySuggestions?: Array<CategorySuggestion>;
  categoryTreeId?: string;
  categoryTreeVersion?: string;
}

export interface CategoryTree {
  applicableMarketplaceIds?: Array<string>;
  categoryTreeId?: string;
  categoryTreeVersion?: string;
  rootCategoryNode?: CategoryTreeNode;
}

export interface CategoryTreeNode {
  category?: Category;
  categoryTreeNodeLevel?: number;
  childCategoryTreeNodes?: Array<CategoryTreeNode>;
  leafCategoryTreeNode?: boolean;
  parentCategoryTreeNodeHref?: string;
}

export interface CompatibilityProperty {
  name?: string;
  localizedName?: string;
}

export interface CompatibilityPropertyValue {
  value?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface ExpiredCategories {
  expiredCategories?: Array<ExpiredCategory>;
}

export interface ExpiredCategory {
  fromCategoryId?: string;
  toCategoryId?: string;
}

export interface FetchItemAspects429Response {
  errors?: Array<Error>;
}

export interface GetCategoriesAspectResponse {
  categoryTreeId?: string;
  categoryTreeVersion?: string;
  categoryAspects?: Array<CategoryAspect>;
}

export interface GetCompatibilityMetadataResponse {
  compatibilityProperties?: Array<CompatibilityProperty>;
}

export interface GetCompatibilityPropertyValuesResponse {
  compatibilityPropertyValues?: Array<CompatibilityPropertyValue>;
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

export interface RelevanceIndicator {
  searchCount?: number;
}

export interface ValueConstraint {
  applicableForLocalizedAspectName?: string;
  applicableForLocalizedAspectValues?: Array<string>;
}
