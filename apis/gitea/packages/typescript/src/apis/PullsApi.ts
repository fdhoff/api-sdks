// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  ChangedFile,
  Commit,
  CreatePullRequestOption,
  CreatePullReviewCommentReplyOptions,
  CreatePullReviewOptions,
  DismissPullReviewOptions,
  EditPullRequestOption,
  MergePullRequestOption,
  PullRequest,
  PullReview,
  PullReviewComment,
  PullReviewRequestOptions,
  SubmitPullReviewOptions,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const repoCancelScheduledAutoMerge: Operation = {
  id: 'repoCancelScheduledAutoMerge',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/pulls/{index}/merge',
  resource: 'pulls',
  name: 'cancelAutoMerge',
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

const repoCreatePullRequest: Operation = {
  id: 'repoCreatePullRequest',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls',
  resource: 'pulls',
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

const repoCreatePullReview: Operation = {
  id: 'repoCreatePullReview',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews',
  resource: 'pulls',
  name: 'createReview',
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

const repoCreatePullReviewCommentReply: Operation = {
  id: 'repoCreatePullReviewCommentReply',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/comments/{id}/replies',
  resource: 'pulls',
  name: 'replyToReviewComment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
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

const repoCreatePullReviewRequests: Operation = {
  id: 'repoCreatePullReviewRequests',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/requested_reviewers',
  resource: 'pulls',
  name: 'requestReviews',
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

const repoDeletePullReview: Operation = {
  id: 'repoDeletePullReview',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews/{id}',
  resource: 'pulls',
  name: 'deleteReview',
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

const repoDeletePullReviewRequests: Operation = {
  id: 'repoDeletePullReviewRequests',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/pulls/{index}/requested_reviewers',
  resource: 'pulls',
  name: 'cancelReviewRequests',
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

const repoDismissPullReview: Operation = {
  id: 'repoDismissPullReview',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals',
  resource: 'pulls',
  name: 'dismissReview',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
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

const repoDownloadPullDiffOrPatch: Operation = {
  id: 'repoDownloadPullDiffOrPatch',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}.{diffType}',
  resource: 'pulls',
  name: 'getDiff',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'diffType', name: 'diffType', location: 'path' },
    { wire: 'binary', name: 'binary', location: 'query' },
  ],
  returnsText: true,
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

const repoEditPullRequest: Operation = {
  id: 'repoEditPullRequest',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/pulls/{index}',
  resource: 'pulls',
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

const repoGetPullRequest: Operation = {
  id: 'repoGetPullRequest',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}',
  resource: 'pulls',
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

const repoGetPullRequestByBaseHead: Operation = {
  id: 'repoGetPullRequestByBaseHead',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{base}/{head}',
  resource: 'pulls',
  name: 'getByBranches',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'base', name: 'base', location: 'path' },
    { wire: 'head', name: 'head', location: 'path' },
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

const repoGetPullRequestCommits: Operation = {
  id: 'repoGetPullRequestCommits',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}/commits',
  resource: 'pulls',
  name: 'listCommits',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'verification', name: 'verification', location: 'query' },
    { wire: 'files', name: 'files', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterCommits',
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

const repoGetPullRequestFiles: Operation = {
  id: 'repoGetPullRequestFiles',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}/files',
  resource: 'pulls',
  name: 'listFiles',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'skip-to', name: 'skipTo', location: 'query' },
    { wire: 'whitespace', name: 'whitespace', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFiles',
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

const repoGetPullReview: Operation = {
  id: 'repoGetPullReview',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews/{id}',
  resource: 'pulls',
  name: 'getReview',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
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

const repoGetPullReviewComments: Operation = {
  id: 'repoGetPullReviewComments',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments',
  resource: 'pulls',
  name: 'listReviewComments',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
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

const repoListPinnedPullRequests: Operation = {
  id: 'repoListPinnedPullRequests',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/pinned',
  resource: 'pulls',
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

const repoListPullRequests: Operation = {
  id: 'repoListPullRequests',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls',
  resource: 'pulls',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'base_branch', name: 'baseBranch', location: 'query' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'milestone', name: 'milestone', location: 'query' },
    { wire: 'labels', name: 'labels', location: 'query' },
    { wire: 'poster', name: 'poster', location: 'query' },
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

const repoListPullReviews: Operation = {
  id: 'repoListPullReviews',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews',
  resource: 'pulls',
  name: 'listReviews',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterReviews',
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

const repoMergePullRequest: Operation = {
  id: 'repoMergePullRequest',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/merge',
  resource: 'pulls',
  name: 'merge',
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

const repoPullRequestIsMerged: Operation = {
  id: 'repoPullRequestIsMerged',
  method: 'GET',
  path: '/repos/{owner}/{repo}/pulls/{index}/merge',
  resource: 'pulls',
  name: 'checkMerged',
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

const repoResolvePullReviewComment: Operation = {
  id: 'repoResolvePullReviewComment',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/comments/{id}/resolve',
  resource: 'pulls',
  name: 'resolveReviewComment',
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

const repoSubmitPullReview: Operation = {
  id: 'repoSubmitPullReview',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews/{id}',
  resource: 'pulls',
  name: 'submitReview',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
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

const repoUnDismissPullReview: Operation = {
  id: 'repoUnDismissPullReview',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals',
  resource: 'pulls',
  name: 'undismissReview',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
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

const repoUnresolvePullReviewComment: Operation = {
  id: 'repoUnresolvePullReviewComment',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/comments/{id}/unresolve',
  resource: 'pulls',
  name: 'unresolveReviewComment',
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

const repoUpdatePullRequest: Operation = {
  id: 'repoUpdatePullRequest',
  method: 'POST',
  path: '/repos/{owner}/{repo}/pulls/{index}/update',
  resource: 'pulls',
  name: 'updateBranch',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'index', name: 'index', location: 'path' },
    { wire: 'style', name: 'style', location: 'query' },
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
  repoCancelScheduledAutoMerge,
  repoCreatePullRequest,
  repoCreatePullReview,
  repoCreatePullReviewCommentReply,
  repoCreatePullReviewRequests,
  repoDeletePullReview,
  repoDeletePullReviewRequests,
  repoDismissPullReview,
  repoDownloadPullDiffOrPatch,
  repoEditPullRequest,
  repoGetPullRequest,
  repoGetPullRequestByBaseHead,
  repoGetPullRequestCommits,
  repoGetPullRequestFiles,
  repoGetPullReview,
  repoGetPullReviewComments,
  repoListPinnedPullRequests,
  repoListPullRequests,
  repoListPullReviews,
  repoMergePullRequest,
  repoPullRequestIsMerged,
  repoResolvePullReviewComment,
  repoSubmitPullReview,
  repoUnDismissPullReview,
  repoUnresolvePullReviewComment,
  repoUpdatePullRequest,
];

export class PullsApi extends Resource {
  /** Cancel a pull request's scheduled merge (repoCancelScheduledAutoMerge). */
  cancelAutoMerge(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(repoCancelScheduledAutoMerge, undefined, { owner, repo, index }, options);
  }

  /** Open a pull request (repoCreatePullRequest). */
  create(owner: string, repo: string, body?: CreatePullRequestOption, options?: RequestOptions): Promise<PullRequest> {
    return this.call(repoCreatePullRequest, body, { owner, repo }, options);
  }

  /** Start a review of a pull request (repoCreatePullReview). */
  createReview(
    owner: string,
    repo: string,
    index: number,
    body: CreatePullReviewOptions,
    options?: RequestOptions,
  ): Promise<PullReview> {
    return this.call(repoCreatePullReview, body, { owner, repo, index }, options);
  }

  /** Reply to a review comment (repoCreatePullReviewCommentReply). */
  replyToReviewComment(
    owner: string,
    repo: string,
    index: number,
    id: number,
    body: CreatePullReviewCommentReplyOptions,
    options?: RequestOptions,
  ): Promise<PullReviewComment> {
    return this.call(repoCreatePullReviewCommentReply, body, { owner, repo, index, id }, options);
  }

  /** Ask users or teams to review a pull request (repoCreatePullReviewRequests). */
  requestReviews(
    owner: string,
    repo: string,
    index: number,
    body: PullReviewRequestOptions,
    options?: RequestOptions,
  ): Promise<Array<PullReview>> {
    return this.call(repoCreatePullReviewRequests, body, { owner, repo, index }, options);
  }

  /** Delete a pull request review (repoDeletePullReview). */
  deleteReview(owner: string, repo: string, index: number, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoDeletePullReview, undefined, { owner, repo, index, id }, options);
  }

  /** Withdraw review requests from a pull request (repoDeletePullReviewRequests). */
  cancelReviewRequests(
    owner: string,
    repo: string,
    index: number,
    body: PullReviewRequestOptions,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoDeletePullReviewRequests, body, { owner, repo, index }, options);
  }

  /** Dismiss a pull request review (repoDismissPullReview). */
  dismissReview(
    owner: string,
    repo: string,
    index: number,
    id: number,
    body: DismissPullReviewOptions,
    options?: RequestOptions,
  ): Promise<PullReview> {
    return this.call(repoDismissPullReview, body, { owner, repo, index, id }, options);
  }

  /** Get a pull request's diff or patch as text (repoDownloadPullDiffOrPatch). */
  getDiff(
    owner: string,
    repo: string,
    index: number,
    diffType: 'diff' | 'patch',
    params: { binary?: boolean } = {},
    options?: RequestOptions,
  ): Promise<string> {
    return this.call(repoDownloadPullDiffOrPatch, undefined, { owner, repo, index, diffType, ...params }, options);
  }

  /** Change a pull request (repoEditPullRequest). */
  update(
    owner: string,
    repo: string,
    index: number,
    body?: EditPullRequestOption,
    options?: RequestOptions,
  ): Promise<PullRequest> {
    return this.call(repoEditPullRequest, body, { owner, repo, index }, options);
  }

  /** Get a pull request (repoGetPullRequest). */
  get(owner: string, repo: string, index: number, options?: RequestOptions): Promise<PullRequest> {
    return this.call(repoGetPullRequest, undefined, { owner, repo, index }, options);
  }

  /** Get the pull request from a head branch into a base branch (repoGetPullRequestByBaseHead). */
  getByBranches(
    owner: string,
    repo: string,
    base: string,
    head: string,
    options?: RequestOptions,
  ): Promise<PullRequest> {
    return this.call(repoGetPullRequestByBaseHead, undefined, { owner, repo, base, head }, options);
  }

  /** List one page of a pull request's commits (repoGetPullRequestCommits). */
  listCommits(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number; verification?: boolean; files?: boolean } = {},
    options?: RequestOptions,
  ): Promise<Array<Commit>> {
    return this.call(repoGetPullRequestCommits, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterCommits(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number; verification?: boolean; files?: boolean } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Commit, void, undefined> {
    return this.paginate(repoGetPullRequestCommits, undefined, { owner, repo, index, ...params }, options);
  }

  /** List one page of the files a pull request changes (repoGetPullRequestFiles). */
  listFiles(
    owner: string,
    repo: string,
    index: number,
    params: {
      skipTo?: string;
      whitespace?: 'ignore-all' | 'ignore-change' | 'ignore-eol' | 'show-all';
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<ChangedFile>> {
    return this.call(repoGetPullRequestFiles, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFiles(
    owner: string,
    repo: string,
    index: number,
    params: {
      skipTo?: string;
      whitespace?: 'ignore-all' | 'ignore-change' | 'ignore-eol' | 'show-all';
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ChangedFile, void, undefined> {
    return this.paginate(repoGetPullRequestFiles, undefined, { owner, repo, index, ...params }, options);
  }

  /** Get a pull request review (repoGetPullReview). */
  getReview(owner: string, repo: string, index: number, id: number, options?: RequestOptions): Promise<PullReview> {
    return this.call(repoGetPullReview, undefined, { owner, repo, index, id }, options);
  }

  /** List a review's comments (repoGetPullReviewComments). */
  listReviewComments(
    owner: string,
    repo: string,
    index: number,
    id: number,
    options?: RequestOptions,
  ): Promise<Array<PullReviewComment>> {
    return this.call(repoGetPullReviewComments, undefined, { owner, repo, index, id }, options);
  }

  /** List a repository's pinned pull requests (repoListPinnedPullRequests). */
  listPinned(owner: string, repo: string, options?: RequestOptions): Promise<Array<PullRequest>> {
    return this.call(repoListPinnedPullRequests, undefined, { owner, repo }, options);
  }

  /** List one page of a repository's pull requests (repoListPullRequests). */
  list(
    owner: string,
    repo: string,
    params: {
      baseBranch?: string;
      state?: 'open' | 'closed' | 'all';
      sort?: 'oldest' | 'recentupdate' | 'recentclose' | 'leastupdate' | 'mostcomment' | 'leastcomment' | 'priority';
      milestone?: number;
      labels?: Array<number>;
      poster?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<PullRequest>> {
    return this.call(repoListPullRequests, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: {
      baseBranch?: string;
      state?: 'open' | 'closed' | 'all';
      sort?: 'oldest' | 'recentupdate' | 'recentclose' | 'leastupdate' | 'mostcomment' | 'leastcomment' | 'priority';
      milestone?: number;
      labels?: Array<number>;
      poster?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PullRequest, void, undefined> {
    return this.paginate(repoListPullRequests, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of a pull request's reviews (repoListPullReviews). */
  listReviews(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<PullReview>> {
    return this.call(repoListPullReviews, undefined, { owner, repo, index, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterReviews(
    owner: string,
    repo: string,
    index: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PullReview, void, undefined> {
    return this.paginate(repoListPullReviews, undefined, { owner, repo, index, ...params }, options);
  }

  /** Merge a pull request (repoMergePullRequest). */
  merge(
    owner: string,
    repo: string,
    index: number,
    body?: MergePullRequestOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoMergePullRequest, body, { owner, repo, index }, options);
  }

  /** Check whether a pull request is merged (repoPullRequestIsMerged). */
  checkMerged(owner: string, repo: string, index: number, options?: RequestOptions): Promise<void> {
    return this.call(repoPullRequestIsMerged, undefined, { owner, repo, index }, options);
  }

  /** Mark a review comment's conversation resolved (repoResolvePullReviewComment). */
  resolveReviewComment(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoResolvePullReviewComment, undefined, { owner, repo, id }, options);
  }

  /** Submit a pending pull request review (repoSubmitPullReview). */
  submitReview(
    owner: string,
    repo: string,
    index: number,
    id: number,
    body: SubmitPullReviewOptions,
    options?: RequestOptions,
  ): Promise<PullReview> {
    return this.call(repoSubmitPullReview, body, { owner, repo, index, id }, options);
  }

  /** Restore a dismissed pull request review (repoUnDismissPullReview). */
  undismissReview(
    owner: string,
    repo: string,
    index: number,
    id: number,
    options?: RequestOptions,
  ): Promise<PullReview> {
    return this.call(repoUnDismissPullReview, undefined, { owner, repo, index, id }, options);
  }

  /** Mark a review comment's conversation unresolved (repoUnresolvePullReviewComment). */
  unresolveReviewComment(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoUnresolvePullReviewComment, undefined, { owner, repo, id }, options);
  }

  /** Merge or rebase a pull request's base branch into its head branch (repoUpdatePullRequest). */
  updateBranch(
    owner: string,
    repo: string,
    index: number,
    params: { style?: 'merge' | 'rebase' } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoUpdatePullRequest, undefined, { owner, repo, index, ...params }, options);
  }
}
