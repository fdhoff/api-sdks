// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  ActionRunner,
  ActionRunnersResponse,
  ActionWorkflowJobsResponse,
  ActionWorkflowRunsResponse,
  Badge,
  CreateHookOption,
  CreateKeyOption,
  CreateOrgOption,
  CreateRepoOption,
  CreateUserOption,
  Cron,
  EditActionRunnerOption,
  EditHookOption,
  EditUserOption,
  Email,
  Hook,
  Organization,
  Package,
  PublicKey,
  RenameUserOption,
  Repository,
  User,
  UserBadgeOption,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const adminAddUserBadges: Operation = {
  id: 'adminAddUserBadges',
  method: 'POST',
  path: '/admin/users/{username}/badges',
  resource: 'admin',
  name: 'addUserBadges',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminAdoptRepository: Operation = {
  id: 'adminAdoptRepository',
  method: 'POST',
  path: '/admin/unadopted/{owner}/{repo}',
  resource: 'admin',
  name: 'adoptRepo',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const adminCreateHook: Operation = {
  id: 'adminCreateHook',
  method: 'POST',
  path: '/admin/hooks',
  resource: 'admin',
  name: 'createHook',
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

const adminCreateOrg: Operation = {
  id: 'adminCreateOrg',
  method: 'POST',
  path: '/admin/users/{username}/orgs',
  resource: 'admin',
  name: 'createOrg',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminCreatePublicKey: Operation = {
  id: 'adminCreatePublicKey',
  method: 'POST',
  path: '/admin/users/{username}/keys',
  resource: 'admin',
  name: 'addUserKey',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminCreateRepo: Operation = {
  id: 'adminCreateRepo',
  method: 'POST',
  path: '/admin/users/{username}/repos',
  resource: 'admin',
  name: 'createRepo',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminCreateRunnerRegistrationToken: Operation = {
  id: 'adminCreateRunnerRegistrationToken',
  method: 'POST',
  path: '/admin/actions/runners/registration-token',
  resource: 'admin',
  name: 'createRunnerRegistrationToken',
  params: [],
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

const adminCreateUser: Operation = {
  id: 'adminCreateUser',
  method: 'POST',
  path: '/admin/users',
  resource: 'admin',
  name: 'createUser',
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

const adminCronList: Operation = {
  id: 'adminCronList',
  method: 'GET',
  path: '/admin/cron',
  resource: 'admin',
  name: 'listCronTasks',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterCronTasks',
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

const adminCronRun: Operation = {
  id: 'adminCronRun',
  method: 'POST',
  path: '/admin/cron/{task}',
  resource: 'admin',
  name: 'runCronTask',
  params: [{ wire: 'task', name: 'task', location: 'path' }],
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

const adminDeleteHook: Operation = {
  id: 'adminDeleteHook',
  method: 'DELETE',
  path: '/admin/hooks/{id}',
  resource: 'admin',
  name: 'deleteHook',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
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

const adminDeleteUnadoptedRepository: Operation = {
  id: 'adminDeleteUnadoptedRepository',
  method: 'DELETE',
  path: '/admin/unadopted/{owner}/{repo}',
  resource: 'admin',
  name: 'deleteUnadoptedRepo',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const adminDeleteUser: Operation = {
  id: 'adminDeleteUser',
  method: 'DELETE',
  path: '/admin/users/{username}',
  resource: 'admin',
  name: 'deleteUser',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'purge', name: 'purge', location: 'query' },
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

const adminDeleteUserBadges: Operation = {
  id: 'adminDeleteUserBadges',
  method: 'DELETE',
  path: '/admin/users/{username}/badges',
  resource: 'admin',
  name: 'deleteUserBadges',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminDeleteUserPublicKey: Operation = {
  id: 'adminDeleteUserPublicKey',
  method: 'DELETE',
  path: '/admin/users/{username}/keys/{id}',
  resource: 'admin',
  name: 'deleteUserKey',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
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

const adminEditHook: Operation = {
  id: 'adminEditHook',
  method: 'PATCH',
  path: '/admin/hooks/{id}',
  resource: 'admin',
  name: 'updateHook',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
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

const adminEditUser: Operation = {
  id: 'adminEditUser',
  method: 'PATCH',
  path: '/admin/users/{username}',
  resource: 'admin',
  name: 'updateUser',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminGetAllEmails: Operation = {
  id: 'adminGetAllEmails',
  method: 'GET',
  path: '/admin/emails',
  resource: 'admin',
  name: 'listEmails',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterEmails',
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

const adminGetAllOrgs: Operation = {
  id: 'adminGetAllOrgs',
  method: 'GET',
  path: '/admin/orgs',
  resource: 'admin',
  name: 'listOrgs',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterOrgs',
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

const adminGetHook: Operation = {
  id: 'adminGetHook',
  method: 'GET',
  path: '/admin/hooks/{id}',
  resource: 'admin',
  name: 'getHook',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
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

const adminListHooks: Operation = {
  id: 'adminListHooks',
  method: 'GET',
  path: '/admin/hooks',
  resource: 'admin',
  name: 'listHooks',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterHooks',
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

const adminListPackages: Operation = {
  id: 'adminListPackages',
  method: 'GET',
  path: '/admin/packages',
  resource: 'admin',
  name: 'listPackages',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterPackages',
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

const adminListUserBadges: Operation = {
  id: 'adminListUserBadges',
  method: 'GET',
  path: '/admin/users/{username}/badges',
  resource: 'admin',
  name: 'listUserBadges',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminRenameUser: Operation = {
  id: 'adminRenameUser',
  method: 'POST',
  path: '/admin/users/{username}/rename',
  resource: 'admin',
  name: 'renameUser',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const adminSearchEmails: Operation = {
  id: 'adminSearchEmails',
  method: 'GET',
  path: '/admin/emails/search',
  resource: 'admin',
  name: 'searchEmails',
  params: [
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSearchEmails',
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

const adminSearchUsers: Operation = {
  id: 'adminSearchUsers',
  method: 'GET',
  path: '/admin/users',
  resource: 'admin',
  name: 'searchUsers',
  params: [
    { wire: 'source_id', name: 'sourceId', location: 'query' },
    { wire: 'login_name', name: 'loginName', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'visibility', name: 'visibility', location: 'query' },
    { wire: 'is_active', name: 'isActive', location: 'query' },
    { wire: 'is_admin', name: 'isAdmin', location: 'query' },
    { wire: 'is_restricted', name: 'isRestricted', location: 'query' },
    { wire: 'is_2fa_enabled', name: 'is2faEnabled', location: 'query' },
    { wire: 'is_prohibit_login', name: 'isProhibitLogin', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSearchUsers',
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

const adminUnadoptedList: Operation = {
  id: 'adminUnadoptedList',
  method: 'GET',
  path: '/admin/unadopted',
  resource: 'admin',
  name: 'listUnadoptedRepos',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'query', name: 'query', location: 'query' },
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

const deleteAdminRunner: Operation = {
  id: 'deleteAdminRunner',
  method: 'DELETE',
  path: '/admin/actions/runners/{runner_id}',
  resource: 'admin',
  name: 'deleteRunner',
  params: [{ wire: 'runner_id', name: 'runnerId', location: 'path' }],
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

const getAdminRunner: Operation = {
  id: 'getAdminRunner',
  method: 'GET',
  path: '/admin/actions/runners/{runner_id}',
  resource: 'admin',
  name: 'getRunner',
  params: [{ wire: 'runner_id', name: 'runnerId', location: 'path' }],
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

const getAdminRunners: Operation = {
  id: 'getAdminRunners',
  method: 'GET',
  path: '/admin/actions/runners',
  resource: 'admin',
  name: 'listRunners',
  params: [{ wire: 'disabled', name: 'disabled', location: 'query' }],
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

const listAdminWorkflowJobs: Operation = {
  id: 'listAdminWorkflowJobs',
  method: 'GET',
  path: '/admin/actions/jobs',
  resource: 'admin',
  name: 'listJobs',
  params: [
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterJobs',
  paging: { style: 'link_header', items: 'jobs', rel: 'next', params: ['page', 'limit'] },
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

const listAdminWorkflowRuns: Operation = {
  id: 'listAdminWorkflowRuns',
  method: 'GET',
  path: '/admin/actions/runs',
  resource: 'admin',
  name: 'listRuns',
  params: [
    { wire: 'event', name: 'event', location: 'query' },
    { wire: 'branch', name: 'branch', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'actor', name: 'actor', location: 'query' },
    { wire: 'head_sha', name: 'headSha', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRuns',
  paging: { style: 'link_header', items: 'workflow_runs', rel: 'next', params: ['page', 'limit'] },
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

const updateAdminRunner: Operation = {
  id: 'updateAdminRunner',
  method: 'PATCH',
  path: '/admin/actions/runners/{runner_id}',
  resource: 'admin',
  name: 'updateRunner',
  params: [{ wire: 'runner_id', name: 'runnerId', location: 'path' }],
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

export const OPERATIONS: readonly Operation[] = [
  adminAddUserBadges,
  adminAdoptRepository,
  adminCreateHook,
  adminCreateOrg,
  adminCreatePublicKey,
  adminCreateRepo,
  adminCreateRunnerRegistrationToken,
  adminCreateUser,
  adminCronList,
  adminCronRun,
  adminDeleteHook,
  adminDeleteUnadoptedRepository,
  adminDeleteUser,
  adminDeleteUserBadges,
  adminDeleteUserPublicKey,
  adminEditHook,
  adminEditUser,
  adminGetAllEmails,
  adminGetAllOrgs,
  adminGetHook,
  adminListHooks,
  adminListPackages,
  adminListUserBadges,
  adminRenameUser,
  adminSearchEmails,
  adminSearchUsers,
  adminUnadoptedList,
  deleteAdminRunner,
  getAdminRunner,
  getAdminRunners,
  listAdminWorkflowJobs,
  listAdminWorkflowRuns,
  updateAdminRunner,
];

export class AdminApi extends Resource {
  /** Add badges to a user (adminAddUserBadges). */
  addUserBadges(username: string, body?: UserBadgeOption, options?: RequestOptions): Promise<void> {
    return this.call(adminAddUserBadges, body, { username }, options);
  }

  /** Adopt an unadopted repository (adminAdoptRepository). */
  adoptRepo(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(adminAdoptRepository, undefined, { owner, repo }, options);
  }

  /** Create a system or default webhook (adminCreateHook). */
  createHook(body: CreateHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(adminCreateHook, body, {}, options);
  }

  /** Create an organization owned by a user (adminCreateOrg). */
  createOrg(username: string, body: CreateOrgOption, options?: RequestOptions): Promise<Organization> {
    return this.call(adminCreateOrg, body, { username }, options);
  }

  /** Add an SSH key to a user (adminCreatePublicKey). */
  addUserKey(username: string, body?: CreateKeyOption, options?: RequestOptions): Promise<PublicKey> {
    return this.call(adminCreatePublicKey, body, { username }, options);
  }

  /** Create a repository owned by a user (adminCreateRepo). */
  createRepo(username: string, body: CreateRepoOption, options?: RequestOptions): Promise<Repository> {
    return this.call(adminCreateRepo, body, { username }, options);
  }

  /** Create a token that registers a global runner (adminCreateRunnerRegistrationToken). */
  createRunnerRegistrationToken(options?: RequestOptions): Promise<void> {
    return this.call(adminCreateRunnerRegistrationToken, undefined, {}, options);
  }

  /** Create a user (adminCreateUser). */
  createUser(body?: CreateUserOption, options?: RequestOptions): Promise<User> {
    return this.call(adminCreateUser, body, {}, options);
  }

  /** List one page of the instance's cron tasks (adminCronList). */
  listCronTasks(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Cron>> {
    return this.call(adminCronList, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterCronTasks(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Cron, void, undefined> {
    return this.paginate(adminCronList, undefined, { ...params }, options);
  }

  /** Run a cron task now (adminCronRun). */
  runCronTask(task: string, options?: RequestOptions): Promise<void> {
    return this.call(adminCronRun, undefined, { task }, options);
  }

  /** Delete a system or default webhook (adminDeleteHook). */
  deleteHook(id: number, options?: RequestOptions): Promise<void> {
    return this.call(adminDeleteHook, undefined, { id }, options);
  }

  /** Delete an unadopted repository's files (adminDeleteUnadoptedRepository). */
  deleteUnadoptedRepo(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(adminDeleteUnadoptedRepository, undefined, { owner, repo }, options);
  }

  /** Delete a user (adminDeleteUser). */
  deleteUser(username: string, params: { purge?: boolean } = {}, options?: RequestOptions): Promise<void> {
    return this.call(adminDeleteUser, undefined, { username, ...params }, options);
  }

  /** Remove badges from a user (adminDeleteUserBadges). */
  deleteUserBadges(username: string, body?: UserBadgeOption, options?: RequestOptions): Promise<void> {
    return this.call(adminDeleteUserBadges, body, { username }, options);
  }

  /** Delete a user's SSH key (adminDeleteUserPublicKey). */
  deleteUserKey(username: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(adminDeleteUserPublicKey, undefined, { username, id }, options);
  }

  /** Change a system or default webhook (adminEditHook). */
  updateHook(id: number, body?: EditHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(adminEditHook, body, { id }, options);
  }

  /** Change a user (adminEditUser). */
  updateUser(username: string, body?: EditUserOption, options?: RequestOptions): Promise<User> {
    return this.call(adminEditUser, body, { username }, options);
  }

  /** List one page of every user's email addresses (adminGetAllEmails). */
  listEmails(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Email>> {
    return this.call(adminGetAllEmails, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterEmails(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Email, void, undefined> {
    return this.paginate(adminGetAllEmails, undefined, { ...params }, options);
  }

  /** List one page of every organization (adminGetAllOrgs). */
  listOrgs(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Organization>> {
    return this.call(adminGetAllOrgs, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterOrgs(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Organization, void, undefined> {
    return this.paginate(adminGetAllOrgs, undefined, { ...params }, options);
  }

  /** Get a system or default webhook (adminGetHook). */
  getHook(id: number, options?: RequestOptions): Promise<Hook> {
    return this.call(adminGetHook, undefined, { id }, options);
  }

  /** List one page of the instance's system and default webhooks (adminListHooks). */
  listHooks(
    params: { page?: number; limit?: number; type?: 'system' | 'default' | 'all' } = {},
    options?: RequestOptions,
  ): Promise<Array<Hook>> {
    return this.call(adminListHooks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterHooks(
    params: { page?: number; limit?: number; type?: 'system' | 'default' | 'all' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Hook, void, undefined> {
    return this.paginate(adminListHooks, undefined, { ...params }, options);
  }

  /** List one page of every package (adminListPackages). */
  listPackages(
    params: {
      page?: number;
      limit?: number;
      type?:
        | 'alpine'
        | 'cargo'
        | 'chef'
        | 'composer'
        | 'conan'
        | 'conda'
        | 'container'
        | 'cran'
        | 'debian'
        | 'generic'
        | 'go'
        | 'helm'
        | 'maven'
        | 'npm'
        | 'nuget'
        | 'pub'
        | 'pypi'
        | 'rpm'
        | 'rubygems'
        | 'swift'
        | 'terraform'
        | 'vagrant';
      q?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<Package>> {
    return this.call(adminListPackages, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterPackages(
    params: {
      page?: number;
      limit?: number;
      type?:
        | 'alpine'
        | 'cargo'
        | 'chef'
        | 'composer'
        | 'conan'
        | 'conda'
        | 'container'
        | 'cran'
        | 'debian'
        | 'generic'
        | 'go'
        | 'helm'
        | 'maven'
        | 'npm'
        | 'nuget'
        | 'pub'
        | 'pypi'
        | 'rpm'
        | 'rubygems'
        | 'swift'
        | 'terraform'
        | 'vagrant';
      q?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Package, void, undefined> {
    return this.paginate(adminListPackages, undefined, { ...params }, options);
  }

  /** List a user's badges (adminListUserBadges). */
  listUserBadges(username: string, options?: RequestOptions): Promise<Array<Badge>> {
    return this.call(adminListUserBadges, undefined, { username }, options);
  }

  /** Rename a user (adminRenameUser). */
  renameUser(username: string, body: RenameUserOption, options?: RequestOptions): Promise<void> {
    return this.call(adminRenameUser, body, { username }, options);
  }

  /** Get one page of the email addresses that match a search (adminSearchEmails). */
  searchEmails(
    params: { q?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Email>> {
    return this.call(adminSearchEmails, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSearchEmails(
    params: { q?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Email, void, undefined> {
    return this.paginate(adminSearchEmails, undefined, { ...params }, options);
  }

  /** Get one page of the users on the instance that match a search (adminSearchUsers). */
  searchUsers(
    params: {
      sourceId?: number;
      loginName?: string;
      page?: number;
      limit?: number;
      sort?: string;
      order?: string;
      q?: string;
      visibility?: string;
      isActive?: boolean;
      isAdmin?: boolean;
      isRestricted?: boolean;
      is2faEnabled?: boolean;
      isProhibitLogin?: boolean;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(adminSearchUsers, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSearchUsers(
    params: {
      sourceId?: number;
      loginName?: string;
      page?: number;
      limit?: number;
      sort?: string;
      order?: string;
      q?: string;
      visibility?: string;
      isActive?: boolean;
      isAdmin?: boolean;
      isRestricted?: boolean;
      is2faEnabled?: boolean;
      isProhibitLogin?: boolean;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(adminSearchUsers, undefined, { ...params }, options);
  }

  /** List a page of the repositories on disk that no user or organization owns (adminUnadoptedList). */
  listUnadoptedRepos(
    params: { page?: number; limit?: number; query?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<string>> {
    return this.call(adminUnadoptedList, undefined, { ...params }, options);
  }

  /** Delete a global runner (deleteAdminRunner). */
  deleteRunner(runnerId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteAdminRunner, undefined, { runnerId }, options);
  }

  /** Get a global runner (getAdminRunner). */
  getRunner(runnerId: string, options?: RequestOptions): Promise<ActionRunner> {
    return this.call(getAdminRunner, undefined, { runnerId }, options);
  }

  /** List the instance's global runners (getAdminRunners). */
  listRunners(params: { disabled?: boolean } = {}, options?: RequestOptions): Promise<ActionRunnersResponse> {
    return this.call(getAdminRunners, undefined, { ...params }, options);
  }

  /** List one page of every workflow job on the instance (listAdminWorkflowJobs). */
  listJobs(
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowJobsResponse> {
    return this.call(listAdminWorkflowJobs, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterJobs(
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowJob, void, undefined> {
    return this.paginate(listAdminWorkflowJobs, undefined, { ...params }, options);
  }

  /** List one page of every workflow run on the instance (listAdminWorkflowRuns). */
  listRuns(
    params: {
      event?: string;
      branch?: string;
      status?: string;
      actor?: string;
      headSha?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowRunsResponse> {
    return this.call(listAdminWorkflowRuns, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRuns(
    params: {
      event?: string;
      branch?: string;
      status?: string;
      actor?: string;
      headSha?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowRun, void, undefined> {
    return this.paginate(listAdminWorkflowRuns, undefined, { ...params }, options);
  }

  /** Change a global runner (updateAdminRunner). */
  updateRunner(runnerId: string, body?: EditActionRunnerOption, options?: RequestOptions): Promise<ActionRunner> {
    return this.call(updateAdminRunner, body, { runnerId }, options);
  }
}
