// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface BenchmarkMetadata {
  average?: string;
}

export interface Cycle {
  cycleType?: string;
  evaluationDate?: string;
  evaluationMonth?: string;
}

export interface Definition {
  dataType?: string;
  key?: string;
  localizedName?: string;
}

export interface Dimension {
  dimensionKey?: string;
  name?: string;
  value?: string;
}

export interface DimensionMetric {
  dimension?: Dimension;
  metrics?: Array<Metric>;
}

export interface Distribution {
  name?: string;
  value?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface EvaluationCycle {
  endDate?: string;
  evaluationDate?: string;
  evaluationType?: string;
  startDate?: string;
}

export interface FindSellerStandardsProfilesResponse {
  standardsProfiles?: Array<StandardsProfile>;
}

export interface GetCustomerServiceMetric429Response {
  errors?: Array<Error>;
}

export interface GetCustomerServiceMetricResponse {
  dimensionMetrics?: Array<DimensionMetric>;
  evaluationCycle?: EvaluationCycle;
  marketplaceId?: string;
}

export interface Header {
  dimensionKeys?: Array<Definition>;
  metrics?: Array<Definition>;
}

export interface Metadata {
  metadataHeader?: MetadataHeader;
  metadataRecords?: Array<MetadataRecord>;
}

export interface MetadataHeader {
  key?: string;
  metadataKeys?: Array<Definition>;
}

export interface MetadataRecord {
  metadataValues?: Array<Value>;
  value?: Value;
}

export interface Metric {
  benchmark?: MetricBenchmark;
  distributions?: Array<MetricDistribution>;
  metricKey?: string;
  value?: string;
}

export interface MetricBenchmark {
  adjustment?: string;
  basis?: string;
  metadata?: BenchmarkMetadata;
  rating?: string;
}

export interface MetricDistribution {
  basis?: string;
  data?: Array<Distribution>;
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

export interface ModelRecord {
  dimensionValues?: Array<Value>;
  metricValues?: Array<Value>;
}

export interface Report {
  dimensionMetadata?: Array<Metadata>;
  endDate?: string;
  header?: Header;
  lastUpdatedDate?: string;
  records?: Array<ModelRecord>;
  startDate?: string;
  warnings?: Array<Error>;
}

export interface StandardsProfile {
  cycle?: Cycle;
  defaultProgram?: boolean;
  evaluationReason?: string;
  metrics?: Array<Metric>;
  program?: string;
  standardsLevel?: string;
}

export interface Value {
  applicable?: boolean;
  value?: object;
}
