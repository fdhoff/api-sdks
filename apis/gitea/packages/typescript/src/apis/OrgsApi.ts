// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  Activity,
  CreateOrgOption,
  CreateRepoOption,
  EditOrgOption,
  Organization,
  RenameOrgOption,
  Repository,
  UpdateUserAvatarOption,
  User,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createOrgRepo: Operation = {
  id: 'createOrgRepo',
  method: 'POST',
  path: '/orgs/{org}/repos',
  resource: 'orgs',
  name: 'createRepo',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const orgConcealMember: Operation = {
  id: 'orgConcealMember',
  method: 'DELETE',
  path: '/orgs/{org}/public_members/{username}',
  resource: 'orgs',
  name: 'concealMember',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
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

const orgCreate: Operation = {
  id: 'orgCreate',
  method: 'POST',
  path: '/orgs',
  resource: 'orgs',
  name: 'create',
  params: [],
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

const orgDelete: Operation = {
  id: 'orgDelete',
  method: 'DELETE',
  path: '/orgs/{org}',
  resource: 'orgs',
  name: 'delete',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const orgDeleteAvatar: Operation = {
  id: 'orgDeleteAvatar',
  method: 'DELETE',
  path: '/orgs/{org}/avatar',
  resource: 'orgs',
  name: 'deleteAvatar',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const orgDeleteMember: Operation = {
  id: 'orgDeleteMember',
  method: 'DELETE',
  path: '/orgs/{org}/members/{username}',
  resource: 'orgs',
  name: 'removeMember',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
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

const orgDeleteRepos: Operation = {
  id: 'orgDeleteRepos',
  method: 'DELETE',
  path: '/orgs/{org}/repos',
  resource: 'orgs',
  name: 'deleteRepos',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const orgEdit: Operation = {
  id: 'orgEdit',
  method: 'PATCH',
  path: '/orgs/{org}',
  resource: 'orgs',
  name: 'update',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const orgGet: Operation = {
  id: 'orgGet',
  method: 'GET',
  path: '/orgs/{org}',
  resource: 'orgs',
  name: 'get',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const orgGetAll: Operation = {
  id: 'orgGetAll',
  method: 'GET',
  path: '/orgs',
  resource: 'orgs',
  name: 'list',
  params: [
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

const orgIsMember: Operation = {
  id: 'orgIsMember',
  method: 'GET',
  path: '/orgs/{org}/members/{username}',
  resource: 'orgs',
  name: 'checkMember',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
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

const orgIsPublicMember: Operation = {
  id: 'orgIsPublicMember',
  method: 'GET',
  path: '/orgs/{org}/public_members/{username}',
  resource: 'orgs',
  name: 'checkPublicMember',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
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

const orgListActivityFeeds: Operation = {
  id: 'orgListActivityFeeds',
  method: 'GET',
  path: '/orgs/{org}/activities/feeds',
  resource: 'orgs',
  name: 'listActivityFeeds',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'date', name: 'date', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterActivityFeeds',
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

const orgListMembers: Operation = {
  id: 'orgListMembers',
  method: 'GET',
  path: '/orgs/{org}/members',
  resource: 'orgs',
  name: 'listMembers',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterMembers',
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

const orgListPublicMembers: Operation = {
  id: 'orgListPublicMembers',
  method: 'GET',
  path: '/orgs/{org}/public_members',
  resource: 'orgs',
  name: 'listPublicMembers',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterPublicMembers',
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

const orgListRepos: Operation = {
  id: 'orgListRepos',
  method: 'GET',
  path: '/orgs/{org}/repos',
  resource: 'orgs',
  name: 'listRepos',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRepos',
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

const orgPublicizeMember: Operation = {
  id: 'orgPublicizeMember',
  method: 'PUT',
  path: '/orgs/{org}/public_members/{username}',
  resource: 'orgs',
  name: 'publicizeMember',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
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

const orgUpdateAvatar: Operation = {
  id: 'orgUpdateAvatar',
  method: 'POST',
  path: '/orgs/{org}/avatar',
  resource: 'orgs',
  name: 'updateAvatar',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const organizationBlockUser: Operation = {
  id: 'organizationBlockUser',
  method: 'PUT',
  path: '/orgs/{org}/blocks/{username}',
  resource: 'orgs',
  name: 'blockUser',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'note', name: 'note', location: 'query' },
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

const organizationCheckUserBlock: Operation = {
  id: 'organizationCheckUserBlock',
  method: 'GET',
  path: '/orgs/{org}/blocks/{username}',
  resource: 'orgs',
  name: 'checkBlockedUser',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
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

const organizationListBlocks: Operation = {
  id: 'organizationListBlocks',
  method: 'GET',
  path: '/orgs/{org}/blocks',
  resource: 'orgs',
  name: 'listBlockedUsers',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterBlockedUsers',
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

const organizationUnblockUser: Operation = {
  id: 'organizationUnblockUser',
  method: 'DELETE',
  path: '/orgs/{org}/blocks/{username}',
  resource: 'orgs',
  name: 'unblockUser',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
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

const renameOrg: Operation = {
  id: 'renameOrg',
  method: 'POST',
  path: '/orgs/{org}/rename',
  resource: 'orgs',
  name: 'rename',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

export const OPERATIONS: readonly Operation[] = [
  createOrgRepo,
  orgConcealMember,
  orgCreate,
  orgDelete,
  orgDeleteAvatar,
  orgDeleteMember,
  orgDeleteRepos,
  orgEdit,
  orgGet,
  orgGetAll,
  orgIsMember,
  orgIsPublicMember,
  orgListActivityFeeds,
  orgListMembers,
  orgListPublicMembers,
  orgListRepos,
  orgPublicizeMember,
  orgUpdateAvatar,
  organizationBlockUser,
  organizationCheckUserBlock,
  organizationListBlocks,
  organizationUnblockUser,
  renameOrg,
];

export class OrgsApi extends Resource {
  /** Create a repository in an organization (createOrgRepo). */
  createRepo(org: string, body?: CreateRepoOption, options?: RequestOptions): Promise<Repository> {
    return this.call(createOrgRepo, body, { org }, options);
  }

  /** Make a user's membership of an organization private (orgConcealMember). */
  concealMember(org: string, username: string, options?: RequestOptions): Promise<void> {
    return this.call(orgConcealMember, undefined, { org, username }, options);
  }

  /** Create an organization (orgCreate). */
  create(body: CreateOrgOption, options?: RequestOptions): Promise<Organization> {
    return this.call(orgCreate, body, {}, options);
  }

  /** Delete an organization (orgDelete). */
  delete(org: string, options?: RequestOptions): Promise<void> {
    return this.call(orgDelete, undefined, { org }, options);
  }

  /** Remove an organization's avatar (orgDeleteAvatar). */
  deleteAvatar(org: string, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteAvatar, undefined, { org }, options);
  }

  /** Remove a member from an organization (orgDeleteMember). */
  removeMember(org: string, username: string, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteMember, undefined, { org, username }, options);
  }

  /** Delete every repository in an organization (orgDeleteRepos). */
  deleteRepos(org: string, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteRepos, undefined, { org }, options);
  }

  /** Change an organization (orgEdit). */
  update(org: string, body: EditOrgOption, options?: RequestOptions): Promise<Organization> {
    return this.call(orgEdit, body, { org }, options);
  }

  /** Get an organization (orgGet). */
  get(org: string, options?: RequestOptions): Promise<Organization> {
    return this.call(orgGet, undefined, { org }, options);
  }

  /** List one page of the organizations you can see (orgGetAll). */
  list(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Organization>> {
    return this.call(orgGetAll, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Organization, void, undefined> {
    return this.paginate(orgGetAll, undefined, { ...params }, options);
  }

  /** Check whether a user is a member of an organization (orgIsMember). */
  checkMember(org: string, username: string, options?: RequestOptions): Promise<void> {
    return this.call(orgIsMember, undefined, { org, username }, options);
  }

  /** Check whether a user's membership of an organization is public (orgIsPublicMember). */
  checkPublicMember(org: string, username: string, options?: RequestOptions): Promise<void> {
    return this.call(orgIsPublicMember, undefined, { org, username }, options);
  }

  /** List one page of an organization's activity (orgListActivityFeeds). */
  listActivityFeeds(
    org: string,
    params: { date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Activity>> {
    return this.call(orgListActivityFeeds, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterActivityFeeds(
    org: string,
    params: { date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Activity, void, undefined> {
    return this.paginate(orgListActivityFeeds, undefined, { org, ...params }, options);
  }

  /** List one page of an organization's members (orgListMembers). */
  listMembers(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(orgListMembers, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterMembers(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(orgListMembers, undefined, { org, ...params }, options);
  }

  /** List one page of an organization's public members (orgListPublicMembers). */
  listPublicMembers(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(orgListPublicMembers, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterPublicMembers(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(orgListPublicMembers, undefined, { org, ...params }, options);
  }

  /** List one page of an organization's repositories (orgListRepos). */
  listRepos(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Repository>> {
    return this.call(orgListRepos, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRepos(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(orgListRepos, undefined, { org, ...params }, options);
  }

  /** Make a user's membership of an organization public (orgPublicizeMember). */
  publicizeMember(org: string, username: string, options?: RequestOptions): Promise<void> {
    return this.call(orgPublicizeMember, undefined, { org, username }, options);
  }

  /** Set an organization's avatar (orgUpdateAvatar). */
  updateAvatar(org: string, body?: UpdateUserAvatarOption, options?: RequestOptions): Promise<void> {
    return this.call(orgUpdateAvatar, body, { org }, options);
  }

  /** Block a user from an organization (organizationBlockUser). */
  blockUser(org: string, username: string, params: { note?: string } = {}, options?: RequestOptions): Promise<void> {
    return this.call(organizationBlockUser, undefined, { org, username, ...params }, options);
  }

  /** Check whether an organization blocks a user (organizationCheckUserBlock). */
  checkBlockedUser(org: string, username: string, options?: RequestOptions): Promise<void> {
    return this.call(organizationCheckUserBlock, undefined, { org, username }, options);
  }

  /** List one page of the users an organization blocks (organizationListBlocks). */
  listBlockedUsers(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(organizationListBlocks, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterBlockedUsers(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(organizationListBlocks, undefined, { org, ...params }, options);
  }

  /** Unblock a user from an organization (organizationUnblockUser). */
  unblockUser(org: string, username: string, options?: RequestOptions): Promise<void> {
    return this.call(organizationUnblockUser, undefined, { org, username }, options);
  }

  /** Rename an organization (renameOrg). */
  rename(org: string, body: RenameOrgOption, options?: RequestOptions): Promise<void> {
    return this.call(renameOrg, body, { org }, options);
  }
}
