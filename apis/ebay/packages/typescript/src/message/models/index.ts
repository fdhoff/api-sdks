// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface BulkConversation {
  conversationId?: string;
  conversationStatus?: string;
  conversationType?: string;
}

export interface BulkUpdateConversation429Response {
  errors?: Array<Error>;
}

export interface BulkUpdateConversationsRequest {
  conversations?: Array<BulkConversation>;
}

export interface BulkUpdateConversationsResponse {
  conversationsMetadata?: ConversationsMetadata;
  conversationsResponse?: Array<ConversationsResponse>;
}

export interface ConversationDetail {
  conversationId?: string;
  conversationStatus?: string;
  conversationTitle?: string;
  conversationType?: string;
  createdDate?: string;
  latestMessage?: MessageDetail;
  referenceId?: string;
  referenceType?: string;
  unreadCount?: number;
}

export interface ConversationsMetadata {
  totalConversationsCount?: number;
  updateFailureCount?: number;
  updateSuccessCount?: number;
}

export interface ConversationsResponse {
  conversationId?: string;
  updateStatus?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface GetAllMyConversationsResponse {
  conversations?: Array<ConversationDetail>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface GetMessagesByConversationIdResponse {
  conversationStatus?: string;
  conversationTitle?: string;
  conversationType?: string;
  href?: string;
  limit?: number;
  messages?: Array<MessageDetail>;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface MessageDetail {
  createdDate?: string;
  messageBody?: string;
  messageId?: string;
  messageMedia?: Array<MessageMedia>;
  readStatus?: boolean;
  recipientUsername?: string;
  senderUsername?: string;
  subject?: string;
}

export interface MessageMedia {
  mediaName?: string;
  mediaType?: string;
  mediaUrl?: string;
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

export interface Reference {
  referenceId?: string;
  referenceType?: string;
}

export interface SendMessageRequest {
  conversationId?: string;
  emailCopyToSender?: boolean;
  messageMedia?: Array<MessageMedia>;
  messageText?: string;
  otherPartyUsername?: string;
  reference?: Reference;
}

export interface SendMessageResponse {
  createdDate?: string;
  messageBody?: string;
  messageId?: string;
  messageMedia?: Array<MessageMedia>;
  readStatus?: boolean;
  recipientUserName?: string;
  senderUserName?: string;
  subject?: string;
}

export interface UpdateConversationRequest {
  conversationId?: string;
  conversationStatus?: string;
  conversationType?: string;
  read?: boolean;
}
