// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Address {
  addressLine1?: string;
  addressLine2?: string;
  city?: string;
  country?: string;
  county?: string;
  postalCode?: string;
  stateOrProvince?: string;
}

export interface BusinessAccount {
  address?: Address;
  doingBusinessAs?: string;
  email?: string;
  name?: string;
  primaryContact?: Contact;
  primaryPhone?: Phone;
  secondaryPhone?: Phone;
  website?: string;
}

export interface Contact {
  firstName?: string;
  lastName?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface GetUser429Response {
  errors?: Array<Error>;
}

export interface IndividualAccount {
  email?: string;
  firstName?: string;
  lastName?: string;
  primaryPhone?: Phone;
  registrationAddress?: Address;
  secondaryPhone?: Phone;
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

export interface Phone {
  countryCode?: string;
  number?: string;
  phoneType?: string;
}

export interface UserResponse {
  accountType?: string;
  businessAccount?: BusinessAccount;
  individualAccount?: IndividualAccount;
  registrationMarketplaceId?: string;
  status?: string;
  userId?: string;
  username?: string;
}
