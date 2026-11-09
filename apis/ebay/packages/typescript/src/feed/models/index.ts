// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface CreateInventoryTaskRequest {
  feedType?: string;
  filterCriteria?: InventoryFilterCriteria;
  schemaVersion?: string;
}

export interface CreateOrderTaskRequest {
  feedType?: string;
  filterCriteria?: OrderFilterCriteria;
  schemaVersion?: string;
}

export interface CreateServiceMetricsTaskRequest {
  feedType?: string;
  filterCriteria?: CustomerServiceMetricsFilterCriteria;
  schemaVersion?: string;
}

export interface CreateTaskRequest {
  feedType?: string;
  schemaVersion?: string;
}

export interface CreateUserScheduleRequest {
  feedType?: string;
  preferredTriggerDayOfMonth?: number;
  preferredTriggerDayOfWeek?: string;
  preferredTriggerHour?: string;
  scheduleEndDate?: string;
  scheduleName?: string;
  scheduleStartDate?: string;
  scheduleTemplateId?: string;
  schemaVersion?: string;
}

export interface CustomerServiceMetricTaskCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  tasks?: Array<ServiceMetricsTask>;
  total?: number;
}

export interface CustomerServiceMetricsFilterCriteria {
  customerServiceMetricType?: string;
  evaluationMarketplaceId?: string;
  listingCategories?: Array<string>;
  shippingRegions?: Array<string>;
}

export interface DateRange {
  from?: string;
  to?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface GetOrderTasks429Response {
  errors?: Array<Error>;
}

export interface InventoryFilterCriteria {
  listingFormat?: string;
}

export interface InventoryTask {
  taskId?: string;
  status?: string;
  feedType?: string;
  creationDate?: string;
  completionDate?: string;
  schemaVersion?: string;
  detailHref?: string;
  uploadSummary?: UploadSummary;
  filterCriteria?: InventoryFilterCriteria;
}

export interface InventoryTaskCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  tasks?: Array<InventoryTask>;
  total?: number;
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

export interface OrderFilterCriteria {
  creationDateRange?: DateRange;
  modifiedDateRange?: DateRange;
  orderStatus?: string;
}

export interface OrderTask {
  completionDate?: string;
  creationDate?: string;
  detailHref?: string;
  feedType?: string;
  filterCriteria?: OrderFilterCriteria;
  schemaVersion?: string;
  status?: string;
  taskId?: string;
  uploadSummary?: UploadSummary;
}

export interface OrderTaskCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  tasks?: Array<OrderTask>;
  total?: number;
}

export interface ScheduleTemplateCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  scheduleTemplates?: Array<ScheduleTemplateResponse>;
  total?: number;
}

export interface ScheduleTemplateResponse {
  feedType?: string;
  frequency?: string;
  name?: string;
  scheduleTemplateId?: string;
  status?: string;
  supportedConfigurations?: Array<SupportedConfiguration>;
}

export interface ServiceMetricsTask {
  completionDate?: string;
  creationDate?: string;
  detailHref?: string;
  feedType?: string;
  filterCriteria?: CustomerServiceMetricsFilterCriteria;
  schemaVersion?: string;
  status?: string;
  taskId?: string;
}

export interface SupportedConfiguration {
  defaultValue?: string;
  property?: string;
  usage?: string;
}

export interface Task {
  completionDate?: string;
  creationDate?: string;
  detailHref?: string;
  feedType?: string;
  schemaVersion?: string;
  status?: string;
  taskId?: string;
  uploadSummary?: UploadSummary;
}

export interface TaskCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  tasks?: Array<Task>;
  total?: number;
}

export interface UpdateUserScheduleRequest {
  preferredTriggerDayOfMonth?: number;
  preferredTriggerDayOfWeek?: string;
  preferredTriggerHour?: string;
  scheduleEndDate?: string;
  scheduleName?: string;
  scheduleStartDate?: string;
  schemaVersion?: string;
}

export interface UploadSummary {
  failureCount?: number;
  successCount?: number;
}

export interface UserScheduleCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  schedules?: Array<UserScheduleResponse>;
  total?: number;
}

export interface UserScheduleResponse {
  scheduleId?: string;
  creationDate?: string;
  feedType?: string;
  lastModifiedDate?: string;
  preferredTriggerDayOfMonth?: number;
  preferredTriggerDayOfWeek?: string;
  preferredTriggerHour?: string;
  scheduleEndDate?: string;
  scheduleName?: string;
  scheduleStartDate?: string;
  scheduleTemplateId?: string;
  schemaVersion?: string;
  status?: string;
  statusReason?: string;
}
