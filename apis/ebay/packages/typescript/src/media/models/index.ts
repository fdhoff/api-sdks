// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface CreateDocumentFromUrlRequest {
  documentType?: string;
  documentUrl?: string;
  languages?: Array<string>;
}

export interface CreateDocumentRequest {
  documentType?: string;
  languages?: Array<string>;
}

export interface CreateDocumentResponse {
  documentId?: string;
  documentStatus?: string;
  documentType?: string;
  languages?: Array<string>;
}

export interface CreateImageFromFile429Response {
  errors?: Array<Error>;
}

export interface CreateImageFromUrlRequest {
  imageUrl?: string;
}

export interface CreateVideoRequest {
  classification?: Array<string>;
  description?: string;
  size?: number;
  title?: string;
}

export interface DocumentMetadata {
  fileName?: string;
  fileSize?: string;
  fileType?: string;
}

export interface DocumentResponse {
  documentId?: string;
  documentMetadata?: DocumentMetadata;
  documentStatus?: string;
  documentType?: string;
  languages?: Array<string>;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface Image {
  imageUrl?: string;
}

export interface ImageResponse {
  expirationDate?: string;
  imageUrl?: string;
  maxDimensionImageUrl?: string;
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

export interface Moderation {
  rejectReasons?: Array<string>;
}

export interface Play {
  playUrl?: string;
  protocol?: string;
}

export interface Video {
  classification?: Array<string>;
  description?: string;
  expirationDate?: string;
  moderation?: Moderation;
  playLists?: Array<Play>;
  size?: number;
  status?: string;
  statusMessage?: string;
  thumbnail?: Image;
  title?: string;
  videoId?: string;
}
