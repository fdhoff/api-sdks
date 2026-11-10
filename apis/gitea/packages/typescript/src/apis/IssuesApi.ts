// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  AddTimeOption,
  Attachment,
  Comment,
  CreateIssueCommentOption,
  CreateIssueOption,
  EditAttachmentOptions,
  EditDeadlineOption,
  EditIssueCommentOption,
  EditIssueOption,
  EditReactionOption,
  Issue,
  IssueAssigneesOption,
  IssueDeadline,
  IssueLabelsOption,
  IssueMeta,
  Label,
  LockIssueOption,
  Reaction,
  TimelineComment,
  TrackedTime,
  User,
  WatchInfo,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const issueAddAssignees: Operation = {
  id: 'issueAddAssignees',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/assignees',
  resource: 'issues',
  name: 'addAssignees',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueAddLabel: Operation = {
  id: 'issueAddLabel',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/labels',
  resource: 'issues',
  name: 'addLabels',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueAddSubscription: Operation = {
  id: 'issueAddSubscription',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}',
  resource: 'issues',
  name: 'subscribe',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'user', name: 'user', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueAddTime: Operation = {
  id: 'issueAddTime',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/times',
  resource: 'issues',
  name: 'addTrackedTime',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCheckAssignee: Operation = {
  id: 'issueCheckAssignee',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/assignees/{assignee}',
  resource: 'issues',
  name: 'checkAssignee',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'assignee', name: 'assignee', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCheckSubscription: Operation = {
  id: 'issueCheckSubscription',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/subscriptions/check',
  resource: 'issues',
  name: 'checkSubscription',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueClearLabels: Operation = {
  id: 'issueClearLabels',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/labels',
  resource: 'issues',
  name: 'clearLabels',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCreateComment: Operation = {
  id: 'issueCreateComment',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/comments',
  resource: 'issues',
  name: 'createComment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCreateIssue: Operation = {
  id: 'issueCreateIssue',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues',
  resource: 'issues',
  name: 'create',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCreateIssueAttachment: Operation = {
  id: 'issueCreateIssueAttachment',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/assets',
  resource: 'issues',
  name: 'uploadAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'name', name: 'name', location: 'query' },
    { wire: 'attachment', name: 'attachment', location: 'form' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCreateIssueBlocking: Operation = {
  id: 'issueCreateIssueBlocking',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/blocks',
  resource: 'issues',
  name: 'addBlocked',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCreateIssueCommentAttachment: Operation = {
  id: 'issueCreateIssueCommentAttachment',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/assets',
  resource: 'issues',
  name: 'uploadCommentAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'name', name: 'name', location: 'query' },
    { wire: 'attachment', name: 'attachment', location: 'form' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueCreateIssueDependencies: Operation = {
  id: 'issueCreateIssueDependencies',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/dependencies',
  resource: 'issues',
  name: 'addDependency',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDelete: Operation = {
  id: 'issueDelete',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}',
  resource: 'issues',
  name: 'delete',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteComment: Operation = {
  id: 'issueDeleteComment',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/comments/{id}',
  resource: 'issues',
  name: 'deleteComment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteCommentReaction: Operation = {
  id: 'issueDeleteCommentReaction',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/reactions',
  resource: 'issues',
  name: 'removeCommentReaction',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  hasBody: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteIssueAttachment: Operation = {
  id: 'issueDeleteIssueAttachment',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}',
  resource: 'issues',
  name: 'deleteAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteIssueCommentAttachment: Operation = {
  id: 'issueDeleteIssueCommentAttachment',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}',
  resource: 'issues',
  name: 'deleteCommentAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteIssueReaction: Operation = {
  id: 'issueDeleteIssueReaction',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/reactions',
  resource: 'issues',
  name: 'removeReaction',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteStopWatch: Operation = {
  id: 'issueDeleteStopWatch',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/stopwatch/delete',
  resource: 'issues',
  name: 'deleteStopwatch',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteSubscription: Operation = {
  id: 'issueDeleteSubscription',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}',
  resource: 'issues',
  name: 'unsubscribe',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'user', name: 'user', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueDeleteTime: Operation = {
  id: 'issueDeleteTime',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/times/{id}',
  resource: 'issues',
  name: 'deleteTrackedTime',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueEditComment: Operation = {
  id: 'issueEditComment',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/issues/comments/{id}',
  resource: 'issues',
  name: 'updateComment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueEditIssue: Operation = {
  id: 'issueEditIssue',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/issues/{index}',
  resource: 'issues',
  name: 'update',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueEditIssueAttachment: Operation = {
  id: 'issueEditIssueAttachment',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}',
  resource: 'issues',
  name: 'updateAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueEditIssueCommentAttachment: Operation = {
  id: 'issueEditIssueCommentAttachment',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}',
  resource: 'issues',
  name: 'updateCommentAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueEditIssueDeadline: Operation = {
  id: 'issueEditIssueDeadline',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/deadline',
  resource: 'issues',
  name: 'setDeadline',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetComment: Operation = {
  id: 'issueGetComment',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/comments/{id}',
  resource: 'issues',
  name: 'getComment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetCommentReactions: Operation = {
  id: 'issueGetCommentReactions',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/reactions',
  resource: 'issues',
  name: 'listCommentReactions',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetComments: Operation = {
  id: 'issueGetComments',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/comments',
  resource: 'issues',
  name: 'listComments',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetCommentsAndTimeline: Operation = {
  id: 'issueGetCommentsAndTimeline',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/timeline',
  resource: 'issues',
  name: 'listTimeline',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTimeline',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetIssue: Operation = {
  id: 'issueGetIssue',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}',
  resource: 'issues',
  name: 'get',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetIssueAttachment: Operation = {
  id: 'issueGetIssueAttachment',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}',
  resource: 'issues',
  name: 'getAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetIssueCommentAttachment: Operation = {
  id: 'issueGetIssueCommentAttachment',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}',
  resource: 'issues',
  name: 'getCommentAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetIssueReactions: Operation = {
  id: 'issueGetIssueReactions',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/reactions',
  resource: 'issues',
  name: 'listReactions',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterReactions',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetLabels: Operation = {
  id: 'issueGetLabels',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/labels',
  resource: 'issues',
  name: 'listLabels',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueGetRepoComments: Operation = {
  id: 'issueGetRepoComments',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/comments',
  resource: 'issues',
  name: 'listRepoComments',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRepoComments',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueListBlocks: Operation = {
  id: 'issueListBlocks',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/blocks',
  resource: 'issues',
  name: 'listBlocked',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterBlocked',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueListIssueAttachments: Operation = {
  id: 'issueListIssueAttachments',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/assets',
  resource: 'issues',
  name: 'listAttachments',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueListIssueCommentAttachments: Operation = {
  id: 'issueListIssueCommentAttachments',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/assets',
  resource: 'issues',
  name: 'listCommentAttachments',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueListIssueDependencies: Operation = {
  id: 'issueListIssueDependencies',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/dependencies',
  resource: 'issues',
  name: 'listDependencies',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterDependencies',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueListIssues: Operation = {
  id: 'issueListIssues',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues',
  resource: 'issues',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'labels', name: 'labels', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
    { wire: 'milestones', name: 'milestones', location: 'query' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
    { wire: 'created_by', name: 'createdBy', location: 'query' },
    { wire: 'assigned_by', name: 'assignedBy', location: 'query' },
    { wire: 'mentioned_by', name: 'mentionedBy', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueLockIssue: Operation = {
  id: 'issueLockIssue',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/issues/{index}/lock',
  resource: 'issues',
  name: 'lock',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issuePostCommentReaction: Operation = {
  id: 'issuePostCommentReaction',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/comments/{id}/reactions',
  resource: 'issues',
  name: 'addCommentReaction',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issuePostIssueReaction: Operation = {
  id: 'issuePostIssueReaction',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/reactions',
  resource: 'issues',
  name: 'addReaction',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueRemoveAssignees: Operation = {
  id: 'issueRemoveAssignees',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/assignees',
  resource: 'issues',
  name: 'removeAssignees',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueRemoveIssueBlocking: Operation = {
  id: 'issueRemoveIssueBlocking',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/blocks',
  resource: 'issues',
  name: 'removeBlocked',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueRemoveIssueDependencies: Operation = {
  id: 'issueRemoveIssueDependencies',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/dependencies',
  resource: 'issues',
  name: 'removeDependency',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueRemoveLabel: Operation = {
  id: 'issueRemoveLabel',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/labels/{id}',
  resource: 'issues',
  name: 'removeLabel',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueReplaceLabels: Operation = {
  id: 'issueReplaceLabels',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/issues/{index}/labels',
  resource: 'issues',
  name: 'replaceLabels',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueResetTime: Operation = {
  id: 'issueResetTime',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/times',
  resource: 'issues',
  name: 'resetTrackedTime',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueSearchIssues: Operation = {
  id: 'issueSearchIssues',
  method: 'GET',
  path: '/repos/issues/search',
  resource: 'issues',
  name: 'search',
  params: [
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'labels', name: 'labels', location: 'query' },
    { wire: 'milestones', name: 'milestones', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
    { wire: 'assigned', name: 'assigned', location: 'query' },
    { wire: 'created', name: 'created', location: 'query' },
    { wire: 'mentioned', name: 'mentioned', location: 'query' },
    { wire: 'review_requested', name: 'reviewRequested', location: 'query' },
    { wire: 'reviewed', name: 'reviewed', location: 'query' },
    { wire: 'owner', name: 'owner', location: 'query' },
    { wire: 'created_by', name: 'createdBy', location: 'query' },
    { wire: 'team', name: 'team', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSearch',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueStartStopWatch: Operation = {
  id: 'issueStartStopWatch',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/stopwatch/start',
  resource: 'issues',
  name: 'startStopwatch',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueStopStopWatch: Operation = {
  id: 'issueStopStopWatch',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/stopwatch/stop',
  resource: 'issues',
  name: 'stopStopwatch',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueSubscriptions: Operation = {
  id: 'issueSubscriptions',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/subscriptions',
  resource: 'issues',
  name: 'listSubscribers',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSubscribers',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueTrackedTimes: Operation = {
  id: 'issueTrackedTimes',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/{index}/times',
  resource: 'issues',
  name: 'listTrackedTimes',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'user', name: 'user', location: 'query' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTrackedTimes',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const issueUnlockIssue: Operation = {
  id: 'issueUnlockIssue',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/lock',
  resource: 'issues',
  name: 'unlock',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const moveIssuePin: Operation = {
  id: 'moveIssuePin',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/issues/{index}/pin/{position}',
  resource: 'issues',
  name: 'movePin',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'position', name: 'position', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const pinIssue: Operation = {
  id: 'pinIssue',
  method: 'POST',
  path: '/repos/{owner}/{repo}/issues/{index}/pin',
  resource: 'issues',
  name: 'pin',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const repoListPinnedIssues: Operation = {
  id: 'repoListPinnedIssues',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issues/pinned',
  resource: 'issues',
  name: 'listPinned',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const unpinIssue: Operation = {
  id: 'unpinIssue',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/issues/{index}/pin',
  resource: 'issues',
  name: 'unpin',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  issueAddAssignees,
  issueAddLabel,
  issueAddSubscription,
  issueAddTime,
  issueCheckAssignee,
  issueCheckSubscription,
  issueClearLabels,
  issueCreateComment,
  issueCreateIssue,
  issueCreateIssueAttachment,
  issueCreateIssueBlocking,
  issueCreateIssueCommentAttachment,
  issueCreateIssueDependencies,
  issueDelete,
  issueDeleteComment,
  issueDeleteCommentReaction,
  issueDeleteIssueAttachment,
  issueDeleteIssueCommentAttachment,
  issueDeleteIssueReaction,
  issueDeleteStopWatch,
  issueDeleteSubscription,
  issueDeleteTime,
  issueEditComment,
  issueEditIssue,
  issueEditIssueAttachment,
  issueEditIssueCommentAttachment,
  issueEditIssueDeadline,
  issueGetComment,
  issueGetCommentReactions,
  issueGetComments,
  issueGetCommentsAndTimeline,
  issueGetIssue,
  issueGetIssueAttachment,
  issueGetIssueCommentAttachment,
  issueGetIssueReactions,
  issueGetLabels,
  issueGetRepoComments,
  issueListBlocks,
  issueListIssueAttachments,
  issueListIssueCommentAttachments,
  issueListIssueDependencies,
  issueListIssues,
  issueLockIssue,
  issuePostCommentReaction,
  issuePostIssueReaction,
  issueRemoveAssignees,
  issueRemoveIssueBlocking,
  issueRemoveIssueDependencies,
  issueRemoveLabel,
  issueReplaceLabels,
  issueResetTime,
  issueSearchIssues,
  issueStartStopWatch,
  issueStopStopWatch,
  issueSubscriptions,
  issueTrackedTimes,
  issueUnlockIssue,
  moveIssuePin,
  pinIssue,
  repoListPinnedIssues,
  unpinIssue,
];

export class IssuesApi extends Resource {
  /** Assign users to an issue (issueAddAssignees). */
  addAssignees(
    owner: string,
    repo: string,
    index: number,
    body: IssueAssigneesOption,
    options?: RequestOptions,
  ): Promise<Issue> {
    return this.call(issueAddAssignees, body, { owner, repo, index }, options);
  }

  /** Add labels to an issue (issueAddLabel). */
  addLabels(
    owner: string,
    repo: string,
    index: number,
    body?: IssueLabelsOption,
    options?: RequestOptions,
  ): Promise<Array<Label>> {
    return this.call(issueAddLabel, body, { owner, repo, index }, options);
  }

  /** Subscribe a user to an issue (issueAddSubscription). */
  subscribe(owner: string, repo: string, index: number, user: string, options?: RequestOptions): Promise<void> {
    return this.call(issueAddSubscription, undefined, { owner, repo, index, user }, options);
  }

  /** Track time spent on an issue (issueAddTime). */
  addTrackedTime(
    owner: string,
    repo: string,
    index: number,
    body?: AddTimeOption,
    options?: RequestOptions,
  ): Promise<TrackedTime> {
    return this.call(issueAddTime, body, { owner, repo, index }, options);
  }

  /** Check whether a user is assigned to an issue (issueCheckAssignee). */
  checkAssignee(owner: string, repo: string, index: number, assignee: string, options?: RequestOptions): Promise<void> {
    return this.call(issueCheckAssignee, undefined, { owner, repo, index, assignee }, options);
  }

  /** Check whether you are subscribed to an issue (issueCheckSubscription). */
  checkSubscription(owner: string, repo: string, index: number, options?: RequestOptions): Promise<WatchInfo> {
    return this.call(issueCheckSubscription, undefined, { owner, repo, index }, options);
  }

  /** Remove every label from an issue (issueClearLabels). */
  clearLabels(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(issueClearLabels, undefined, { owner, repo, index }, options);
  }

  /** Comment on an issue (issueCreateComment). */
  createComment(
    owner: string,
    repo: string,
    index: number,
    body?: CreateIssueCommentOption,
    options?: RequestOptions,
  ): Promise<Comment> {
    return this.call(issueCreateComment, body, { owner, repo, index }, options);
  }

  /** Open an issue (issueCreateIssue). */
  create(owner: string, repo: string, body?: CreateIssueOption, options?: RequestOptions): Promise<Issue> {
    return this.call(issueCreateIssue, body, { owner, repo }, options);
  }

  /** Upload an attachment to an issue (issueCreateIssueAttachment). */
  uploadAttachment(
    owner: string,
    repo: string,
    index: number,
    params: { name?: string; attachment: FileInput },
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(issueCreateIssueAttachment, undefined, { owner, repo, index, ...params }, options);
  }

  /** Make an issue block another (issueCreateIssueBlocking). */
  addBlocked(owner: string, repo: string, index: string, body?: IssueMeta, options?: RequestOptions): Promise<Issue> {
    return this.call(issueCreateIssueBlocking, body, { owner, repo, index }, options);
  }

  /** Upload an attachment to an issue comment (issueCreateIssueCommentAttachment). */
  uploadCommentAttachment(
    owner: string,
    repo: string,
    id: number,
    params: { name?: string; attachment: FileInput },
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(issueCreateIssueCommentAttachment, undefined, { owner, repo, id, ...params }, options);
  }

  /** Make an issue depend on another (issueCreateIssueDependencies). */
  addDependency(
    owner: string,
    repo: string,
    index: string,
    body?: IssueMeta,
    options?: RequestOptions,
  ): Promise<Issue> {
    return this.call(issueCreateIssueDependencies, body, { owner, repo, index }, options);
  }

  /** Delete an issue (issueDelete). */
  delete(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(issueDelete, undefined, { owner, repo, index }, options);
  }

  /** Delete an issue comment (issueDeleteComment). */
  deleteComment(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(issueDeleteComment, undefined, { owner, repo, id }, options);
  }

  /** Remove a reaction from an issue comment (issueDeleteCommentReaction). */
  removeCommentReaction(
    owner: string,
    repo: string,
    id: number,
    body?: EditReactionOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(issueDeleteCommentReaction, body, { owner, repo, id }, options);
  }

  /** Delete an issue attachment (issueDeleteIssueAttachment). */
  deleteAttachment(
    owner: string,
    repo: string,
    index: number,
    attachmentId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(issueDeleteIssueAttachment, undefined, { owner, repo, index, attachmentId }, options);
  }

  /** Delete an issue comment attachment (issueDeleteIssueCommentAttachment). */
  deleteCommentAttachment(
    owner: string,
    repo: string,
    id: number,
    attachmentId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(issueDeleteIssueCommentAttachment, undefined, { owner, repo, id, attachmentId }, options);
  }

  /** Remove a reaction from an issue (issueDeleteIssueReaction). */
  removeReaction(
    owner: string,
    repo: string,
    index: number,
    body?: EditReactionOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(issueDeleteIssueReaction, body, { owner, repo, index }, options);
  }

  /** Cancel an issue's stopwatch without tracking its time (issueDeleteStopWatch). */
  deleteStopwatch(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(issueDeleteStopWatch, undefined, { owner, repo, index }, options);
  }

  /** Unsubscribe a user from an issue (issueDeleteSubscription). */
  unsubscribe(owner: string, repo: string, index: number, user: string, options?: RequestOptions): Promise<void> {
    return this.call(issueDeleteSubscription, undefined, { owner, repo, index, user }, options);
  }

  /** Delete one tracked time entry from an issue (issueDeleteTime). */
  deleteTrackedTime(owner: string, repo: string, index: number, id: number, options?: RequestOptions): Promise<void> {
    return this.call(issueDeleteTime, undefined, { owner, repo, index, id }, options);
  }

  /** Change an issue comment (issueEditComment). */
  updateComment(
    owner: string,
    repo: string,
    id: number,
    body?: EditIssueCommentOption,
    options?: RequestOptions,
  ): Promise<Comment | undefined> {
    return this.call(issueEditComment, body, { owner, repo, id }, options);
  }

  /** Change an issue or pull request (issueEditIssue). */
  update(owner: string, repo: string, index: number, body?: EditIssueOption, options?: RequestOptions): Promise<Issue> {
    return this.call(issueEditIssue, body, { owner, repo, index }, options);
  }

  /** Rename an issue attachment (issueEditIssueAttachment). */
  updateAttachment(
    owner: string,
    repo: string,
    index: number,
    attachmentId: number,
    body?: EditAttachmentOptions,
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(issueEditIssueAttachment, body, { owner, repo, index, attachmentId }, options);
  }

  /** Rename an issue comment attachment (issueEditIssueCommentAttachment). */
  updateCommentAttachment(
    owner: string,
    repo: string,
    id: number,
    attachmentId: number,
    body?: EditAttachmentOptions,
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(issueEditIssueCommentAttachment, body, { owner, repo, id, attachmentId }, options);
  }

  /** Set or clear an issue's due date (issueEditIssueDeadline). */
  setDeadline(
    owner: string,
    repo: string,
    index: number,
    body?: EditDeadlineOption,
    options?: RequestOptions,
  ): Promise<IssueDeadline> {
    return this.call(issueEditIssueDeadline, body, { owner, repo, index }, options);
  }

  /** Get an issue comment (issueGetComment). */
  getComment(owner: string, repo: string, id: number, options?: RequestOptions): Promise<Comment | undefined> {
    return this.call(issueGetComment, undefined, { owner, repo, id }, options);
  }

  /** List an issue comment's reactions (issueGetCommentReactions). */
  listCommentReactions(owner: string, repo: string, id: number, options?: RequestOptions): Promise<Array<Reaction>> {
    return this.call(issueGetCommentReactions, undefined, { owner, repo, id }, options);
  }

  /** List an issue's comments (issueGetComments). */
  listComments(
    owner: string,
    repo: string,
    index: number,
    params: { since?: string; before?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<Comment>> {
    return this.call(issueGetComments, undefined, { owner, repo, index, ...params }, options);
  }

  /** List one page of an issue's comments and events (issueGetCommentsAndTimeline). */
  listTimeline(
    owner: string,
    repo: string,
    index: number,
    params: { since?: string; page?: number; limit?: number; before?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<TimelineComment>> {
    return this.call(issueGetCommentsAndTimeline, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTimeline(
    owner: string,
    repo: string,
    index: number,
    params: { since?: string; page?: number; limit?: number; before?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TimelineComment, void, undefined> {
    return this.paginate(issueGetCommentsAndTimeline, undefined, { owner, repo, index, ...params }, options);
  }

  /** Get an issue or pull request (issueGetIssue). */
  get(owner: string, repo: string, index: number, options?: RequestOptions): Promise<Issue> {
    return this.call(issueGetIssue, undefined, { owner, repo, index }, options);
  }

  /** Get an issue attachment (issueGetIssueAttachment). */
  getAttachment(
    owner: string,
    repo: string,
    index: number,
    attachmentId: number,
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(issueGetIssueAttachment, undefined, { owner, repo, index, attachmentId }, options);
  }

  /** Get an issue comment attachment (issueGetIssueCommentAttachment). */
  getCommentAttachment(
    owner: string,
    repo: string,
    id: number,
    attachmentId: number,
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(issueGetIssueCommentAttachment, undefined, { owner, repo, id, attachmentId }, options);
  }

  /** List one page of an issue's reactions (issueGetIssueReactions). */
  listReactions(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Reaction>> {
    return this.call(issueGetIssueReactions, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterReactions(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Reaction, void, undefined> {
    return this.paginate(issueGetIssueReactions, undefined, { owner, repo, index, ...params }, options);
  }

  /** List an issue's labels (issueGetLabels). */
  listLabels(owner: string, repo: string, index: number, options?: RequestOptions): Promise<Array<Label>> {
    return this.call(issueGetLabels, undefined, { owner, repo, index }, options);
  }

  /** List one page of the comments on a repository's issues (issueGetRepoComments). */
  listRepoComments(
    owner: string,
    repo: string,
    params: { since?: string; before?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Comment>> {
    return this.call(issueGetRepoComments, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRepoComments(
    owner: string,
    repo: string,
    params: { since?: string; before?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Comment, void, undefined> {
    return this.paginate(issueGetRepoComments, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of the issues that an issue blocks (issueListBlocks). */
  listBlocked(
    owner: string,
    repo: string,
    index: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Issue>> {
    return this.call(issueListBlocks, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterBlocked(
    owner: string,
    repo: string,
    index: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Issue, void, undefined> {
    return this.paginate(issueListBlocks, undefined, { owner, repo, index, ...params }, options);
  }

  /** List an issue's attachments (issueListIssueAttachments). */
  listAttachments(owner: string, repo: string, index: number, options?: RequestOptions): Promise<Array<Attachment>> {
    return this.call(issueListIssueAttachments, undefined, { owner, repo, index }, options);
  }

  /** List an issue comment's attachments (issueListIssueCommentAttachments). */
  listCommentAttachments(
    owner: string,
    repo: string,
    id: number,
    options?: RequestOptions,
  ): Promise<Array<Attachment>> {
    return this.call(issueListIssueCommentAttachments, undefined, { owner, repo, id }, options);
  }

  /** List one page of the issues that block an issue (issueListIssueDependencies). */
  listDependencies(
    owner: string,
    repo: string,
    index: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Issue>> {
    return this.call(issueListIssueDependencies, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterDependencies(
    owner: string,
    repo: string,
    index: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Issue, void, undefined> {
    return this.paginate(issueListIssueDependencies, undefined, { owner, repo, index, ...params }, options);
  }

  /** List one page of a repository's issues and pull requests (issueListIssues). */
  list(
    owner: string,
    repo: string,
    params: {
      state?: 'closed' | 'open' | 'all';
      labels?: string;
      q?: string;
      type?: 'issues' | 'pulls';
      milestones?: string;
      since?: string;
      before?: string;
      createdBy?: string;
      assignedBy?: string;
      mentionedBy?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<Issue>> {
    return this.call(issueListIssues, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: {
      state?: 'closed' | 'open' | 'all';
      labels?: string;
      q?: string;
      type?: 'issues' | 'pulls';
      milestones?: string;
      since?: string;
      before?: string;
      createdBy?: string;
      assignedBy?: string;
      mentionedBy?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Issue, void, undefined> {
    return this.paginate(issueListIssues, undefined, { owner, repo, ...params }, options);
  }

  /** Lock an issue's conversation (issueLockIssue). */
  lock(owner: string, repo: string, index: number, body?: LockIssueOption, options?: RequestOptions): Promise<void> {
    return this.call(issueLockIssue, body, { owner, repo, index }, options);
  }

  /** React to an issue comment (issuePostCommentReaction). */
  addCommentReaction(
    owner: string,
    repo: string,
    id: number,
    body?: EditReactionOption,
    options?: RequestOptions,
  ): Promise<Reaction> {
    return this.call(issuePostCommentReaction, body, { owner, repo, id }, options);
  }

  /** React to an issue (issuePostIssueReaction). */
  addReaction(
    owner: string,
    repo: string,
    index: number,
    body?: EditReactionOption,
    options?: RequestOptions,
  ): Promise<Reaction> {
    return this.call(issuePostIssueReaction, body, { owner, repo, index }, options);
  }

  /** Unassign users from an issue (issueRemoveAssignees). */
  removeAssignees(
    owner: string,
    repo: string,
    index: number,
    body: IssueAssigneesOption,
    options?: RequestOptions,
  ): Promise<Issue> {
    return this.call(issueRemoveAssignees, body, { owner, repo, index }, options);
  }

  /** Stop an issue blocking another (issueRemoveIssueBlocking). */
  removeBlocked(
    owner: string,
    repo: string,
    index: string,
    body?: IssueMeta,
    options?: RequestOptions,
  ): Promise<Issue> {
    return this.call(issueRemoveIssueBlocking, body, { owner, repo, index }, options);
  }

  /** Stop an issue depending on another (issueRemoveIssueDependencies). */
  removeDependency(
    owner: string,
    repo: string,
    index: string,
    body?: IssueMeta,
    options?: RequestOptions,
  ): Promise<Issue> {
    return this.call(issueRemoveIssueDependencies, body, { owner, repo, index }, options);
  }

  /** Remove a label from an issue (issueRemoveLabel). */
  removeLabel(owner: string, repo: string, index: number, id: number, options?: RequestOptions): Promise<void> {
    return this.call(issueRemoveLabel, undefined, { owner, repo, index, id }, options);
  }

  /** Replace an issue's labels (issueReplaceLabels). */
  replaceLabels(
    owner: string,
    repo: string,
    index: number,
    body?: IssueLabelsOption,
    options?: RequestOptions,
  ): Promise<Array<Label>> {
    return this.call(issueReplaceLabels, body, { owner, repo, index }, options);
  }

  /** Delete all of your tracked time on an issue (issueResetTime). */
  resetTrackedTime(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(issueResetTime, undefined, { owner, repo, index }, options);
  }

  /** Get one page of the issues and pull requests that match a search, across repositories (issueSearchIssues). */
  search(
    params: {
      state?: 'open' | 'closed' | 'all';
      labels?: string;
      milestones?: string;
      q?: string;
      type?: 'issues' | 'pulls';
      since?: string;
      before?: string;
      assigned?: boolean;
      created?: boolean;
      mentioned?: boolean;
      reviewRequested?: boolean;
      reviewed?: boolean;
      owner?: string;
      createdBy?: string;
      team?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<Issue>> {
    return this.call(issueSearchIssues, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSearch(
    params: {
      state?: 'open' | 'closed' | 'all';
      labels?: string;
      milestones?: string;
      q?: string;
      type?: 'issues' | 'pulls';
      since?: string;
      before?: string;
      assigned?: boolean;
      created?: boolean;
      mentioned?: boolean;
      reviewRequested?: boolean;
      reviewed?: boolean;
      owner?: string;
      createdBy?: string;
      team?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Issue, void, undefined> {
    return this.paginate(issueSearchIssues, undefined, { ...params }, options);
  }

  /** Start a stopwatch on an issue (issueStartStopWatch). */
  startStopwatch(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(issueStartStopWatch, undefined, { owner, repo, index }, options);
  }

  /** Stop an issue's stopwatch and track its time (issueStopStopWatch). */
  stopStopwatch(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(issueStopStopWatch, undefined, { owner, repo, index }, options);
  }

  /** List one page of an issue's subscribers (issueSubscriptions). */
  listSubscribers(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(issueSubscriptions, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSubscribers(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(issueSubscriptions, undefined, { owner, repo, index, ...params }, options);
  }

  /** List one page of the time tracked on an issue (issueTrackedTimes). */
  listTrackedTimes(
    owner: string,
    repo: string,
    index: number,
    params: { user?: string; since?: string; before?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<TrackedTime>> {
    return this.call(issueTrackedTimes, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTrackedTimes(
    owner: string,
    repo: string,
    index: number,
    params: { user?: string; since?: string; before?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TrackedTime, void, undefined> {
    return this.paginate(issueTrackedTimes, undefined, { owner, repo, index, ...params }, options);
  }

  /** Unlock an issue's conversation (issueUnlockIssue). */
  unlock(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(issueUnlockIssue, undefined, { owner, repo, index }, options);
  }

  /** Move a pinned issue to another position (moveIssuePin). */
  movePin(owner: string, repo: string, index: number, position: number, options?: RequestOptions): Promise<void> {
    return this.call(moveIssuePin, undefined, { owner, repo, index, position }, options);
  }

  /** Pin an issue (pinIssue). */
  pin(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(pinIssue, undefined, { owner, repo, index }, options);
  }

  /** List a repository's pinned issues (repoListPinnedIssues). */
  listPinned(owner: string, repo: string, options?: RequestOptions): Promise<Array<Issue>> {
    return this.call(repoListPinnedIssues, undefined, { owner, repo }, options);
  }

  /** Unpin an issue (unpinIssue). */
  unpin(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(unpinIssue, undefined, { owner, repo, index }, options);
  }
}
