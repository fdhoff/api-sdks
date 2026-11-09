// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface CreateSigningKeyRequest {
  signingKeyCipher?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface GetSigningKeys429Response {
  errors?: Array<Error>;
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

export interface QuerySigningKeysResponse {
  signingKeys?: Array<SigningKey>;
}

export interface SigningKey {
  creationTime?: number;
  expirationTime?: number;
  jwe?: string;
  privateKey?: string;
  publicKey?: string;
  signingKeyCipher?: string;
  signingKeyId?: string;
}
