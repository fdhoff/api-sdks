// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  Activity,
  AddCollaboratorOption,
  CreateDeployKeyTokenOption,
  CreateForkOption,
  CreateKeyOption,
  CreatePushMirrorOption,
  DeployKey,
  EditRepoOption,
  GenerateRepoOption,
  IssueConfig,
  IssueConfigValidation,
  IssueTemplate,
  MergeUpstreamRequest,
  MergeUpstreamResponse,
  MigrateRepoOptions,
  NewIssuePinsAllowed,
  PushMirror,
  RepoCollaboratorPermission,
  RepoTopicOptions,
  Repository,
  SearchResults,
  Team,
  TopicListResponse,
  TopicName,
  TrackedTime,
  TransferRepoOption,
  UpdateRepoAvatarOption,
  User,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const acceptRepoTransfer: Operation = {
  id: 'acceptRepoTransfer',
  method: 'POST',
  path: '/repos/{owner}/{repo}/transfer/accept',
  resource: 'repos',
  name: 'acceptTransfer',
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

const createFork: Operation = {
  id: 'createFork',
  method: 'POST',
  path: '/repos/{owner}/{repo}/forks',
  resource: 'repos',
  name: 'fork',
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

const generateRepo: Operation = {
  id: 'generateRepo',
  method: 'POST',
  path: '/repos/{template_owner}/{template_repo}/generate',
  resource: 'repos',
  name: 'generate',
  params: [
    { wire: 'template_owner', name: 'templateOwner', location: 'path' },
    { wire: 'template_repo', name: 'templateRepo', location: 'path' },
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

const listForks: Operation = {
  id: 'listForks',
  method: 'GET',
  path: '/repos/{owner}/{repo}/forks',
  resource: 'repos',
  name: 'listForks',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterForks',
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

const rejectRepoTransfer: Operation = {
  id: 'rejectRepoTransfer',
  method: 'POST',
  path: '/repos/{owner}/{repo}/transfer/reject',
  resource: 'repos',
  name: 'rejectTransfer',
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

const repoAddCollaborator: Operation = {
  id: 'repoAddCollaborator',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/collaborators/{collaborator}',
  resource: 'repos',
  name: 'addCollaborator',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'collaborator', name: 'collaborator', location: 'path' },
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

const repoAddPushMirror: Operation = {
  id: 'repoAddPushMirror',
  method: 'POST',
  path: '/repos/{owner}/{repo}/push_mirrors',
  resource: 'repos',
  name: 'addPushMirror',
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

const repoAddTeam: Operation = {
  id: 'repoAddTeam',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/teams/{team}',
  resource: 'repos',
  name: 'addTeam',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'team', name: 'team', location: 'path' },
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

const repoAddTopic: Operation = {
  id: 'repoAddTopic',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/topics/{topic}',
  resource: 'repos',
  name: 'addTopic',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'topic', name: 'topic', location: 'path' },
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

const repoCheckAssignee: Operation = {
  id: 'repoCheckAssignee',
  method: 'GET',
  path: '/repos/{owner}/{repo}/assignees/{assignee}',
  resource: 'repos',
  name: 'checkAssignee',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoCheckCollaborator: Operation = {
  id: 'repoCheckCollaborator',
  method: 'GET',
  path: '/repos/{owner}/{repo}/collaborators/{collaborator}',
  resource: 'repos',
  name: 'checkCollaborator',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'collaborator', name: 'collaborator', location: 'path' },
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

const repoCheckTeam: Operation = {
  id: 'repoCheckTeam',
  method: 'GET',
  path: '/repos/{owner}/{repo}/teams/{team}',
  resource: 'repos',
  name: 'checkTeam',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'team', name: 'team', location: 'path' },
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

const repoCreateDeployToken: Operation = {
  id: 'repoCreateDeployToken',
  method: 'POST',
  path: '/repos/{owner}/{repo}/keys/tokens',
  resource: 'repos',
  name: 'createDeployToken',
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

const repoCreateKey: Operation = {
  id: 'repoCreateKey',
  method: 'POST',
  path: '/repos/{owner}/{repo}/keys',
  resource: 'repos',
  name: 'addDeployKey',
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

const repoDelete: Operation = {
  id: 'repoDelete',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}',
  resource: 'repos',
  name: 'delete',
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

const repoDeleteAvatar: Operation = {
  id: 'repoDeleteAvatar',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/avatar',
  resource: 'repos',
  name: 'deleteAvatar',
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

const repoDeleteCollaborator: Operation = {
  id: 'repoDeleteCollaborator',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/collaborators/{collaborator}',
  resource: 'repos',
  name: 'removeCollaborator',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'collaborator', name: 'collaborator', location: 'path' },
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

const repoDeleteKey: Operation = {
  id: 'repoDeleteKey',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/keys/{id}',
  resource: 'repos',
  name: 'deleteDeployKey',
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

const repoDeletePushMirror: Operation = {
  id: 'repoDeletePushMirror',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/push_mirrors/{name}',
  resource: 'repos',
  name: 'deletePushMirror',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

const repoDeleteTeam: Operation = {
  id: 'repoDeleteTeam',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/teams/{team}',
  resource: 'repos',
  name: 'removeTeam',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'team', name: 'team', location: 'path' },
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

const repoDeleteTopic: Operation = {
  id: 'repoDeleteTopic',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/topics/{topic}',
  resource: 'repos',
  name: 'removeTopic',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'topic', name: 'topic', location: 'path' },
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

const repoEdit: Operation = {
  id: 'repoEdit',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}',
  resource: 'repos',
  name: 'update',
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

const repoGet: Operation = {
  id: 'repoGet',
  method: 'GET',
  path: '/repos/{owner}/{repo}',
  resource: 'repos',
  name: 'get',
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

const repoGetArchive: Operation = {
  id: 'repoGetArchive',
  method: 'GET',
  path: '/repos/{owner}/{repo}/archive/{archive}',
  resource: 'repos',
  name: 'downloadArchive',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'archive', name: 'archive', location: 'path' },
    { wire: 'path', name: 'path', location: 'query' },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
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

const repoGetAssignees: Operation = {
  id: 'repoGetAssignees',
  method: 'GET',
  path: '/repos/{owner}/{repo}/assignees',
  resource: 'repos',
  name: 'listAssignees',
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

const repoGetByID: Operation = {
  id: 'repoGetByID',
  method: 'GET',
  path: '/repositories/{id}',
  resource: 'repos',
  name: 'getById',
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

const repoGetIssueConfig: Operation = {
  id: 'repoGetIssueConfig',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issue_config',
  resource: 'repos',
  name: 'getIssueConfig',
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

const repoGetIssueTemplates: Operation = {
  id: 'repoGetIssueTemplates',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issue_templates',
  resource: 'repos',
  name: 'listIssueTemplates',
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

const repoGetKey: Operation = {
  id: 'repoGetKey',
  method: 'GET',
  path: '/repos/{owner}/{repo}/keys/{id}',
  resource: 'repos',
  name: 'getDeployKey',
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

const repoGetLanguages: Operation = {
  id: 'repoGetLanguages',
  method: 'GET',
  path: '/repos/{owner}/{repo}/languages',
  resource: 'repos',
  name: 'getLanguages',
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

const repoGetLicenses: Operation = {
  id: 'repoGetLicenses',
  method: 'GET',
  path: '/repos/{owner}/{repo}/licenses',
  resource: 'repos',
  name: 'listLicenses',
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

const repoGetPushMirrorByRemoteName: Operation = {
  id: 'repoGetPushMirrorByRemoteName',
  method: 'GET',
  path: '/repos/{owner}/{repo}/push_mirrors/{name}',
  resource: 'repos',
  name: 'getPushMirror',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

const repoGetRepoPermissions: Operation = {
  id: 'repoGetRepoPermissions',
  method: 'GET',
  path: '/repos/{owner}/{repo}/collaborators/{collaborator}/permission',
  resource: 'repos',
  name: 'getPermissions',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'collaborator', name: 'collaborator', location: 'path' },
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

const repoGetReviewers: Operation = {
  id: 'repoGetReviewers',
  method: 'GET',
  path: '/repos/{owner}/{repo}/reviewers',
  resource: 'repos',
  name: 'listReviewers',
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

const repoListActivityFeeds: Operation = {
  id: 'repoListActivityFeeds',
  method: 'GET',
  path: '/repos/{owner}/{repo}/activities/feeds',
  resource: 'repos',
  name: 'listActivityFeeds',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoListCollaborators: Operation = {
  id: 'repoListCollaborators',
  method: 'GET',
  path: '/repos/{owner}/{repo}/collaborators',
  resource: 'repos',
  name: 'listCollaborators',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterCollaborators',
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

const repoListKeys: Operation = {
  id: 'repoListKeys',
  method: 'GET',
  path: '/repos/{owner}/{repo}/keys',
  resource: 'repos',
  name: 'listDeployKeys',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'key_id', name: 'keyId', location: 'query' },
    { wire: 'fingerprint', name: 'fingerprint', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterDeployKeys',
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

const repoListPushMirrors: Operation = {
  id: 'repoListPushMirrors',
  method: 'GET',
  path: '/repos/{owner}/{repo}/push_mirrors',
  resource: 'repos',
  name: 'listPushMirrors',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterPushMirrors',
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

const repoListStargazers: Operation = {
  id: 'repoListStargazers',
  method: 'GET',
  path: '/repos/{owner}/{repo}/stargazers',
  resource: 'repos',
  name: 'listStargazers',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStargazers',
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

const repoListSubscribers: Operation = {
  id: 'repoListSubscribers',
  method: 'GET',
  path: '/repos/{owner}/{repo}/subscribers',
  resource: 'repos',
  name: 'listWatchers',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterWatchers',
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

const repoListTeams: Operation = {
  id: 'repoListTeams',
  method: 'GET',
  path: '/repos/{owner}/{repo}/teams',
  resource: 'repos',
  name: 'listTeams',
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

const repoListTopics: Operation = {
  id: 'repoListTopics',
  method: 'GET',
  path: '/repos/{owner}/{repo}/topics',
  resource: 'repos',
  name: 'listTopics',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
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

const repoMergeUpstream: Operation = {
  id: 'repoMergeUpstream',
  method: 'POST',
  path: '/repos/{owner}/{repo}/merge-upstream',
  resource: 'repos',
  name: 'mergeUpstream',
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

const repoMigrate: Operation = {
  id: 'repoMigrate',
  method: 'POST',
  path: '/repos/migrate',
  resource: 'repos',
  name: 'migrate',
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

const repoMirrorSync: Operation = {
  id: 'repoMirrorSync',
  method: 'POST',
  path: '/repos/{owner}/{repo}/mirror-sync',
  resource: 'repos',
  name: 'syncMirror',
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

const repoNewPinAllowed: Operation = {
  id: 'repoNewPinAllowed',
  method: 'GET',
  path: '/repos/{owner}/{repo}/new_pin_allowed',
  resource: 'repos',
  name: 'checkPinAllowed',
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

const repoPushMirrorSync: Operation = {
  id: 'repoPushMirrorSync',
  method: 'POST',
  path: '/repos/{owner}/{repo}/push_mirrors-sync',
  resource: 'repos',
  name: 'syncPushMirrors',
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

const repoSearch: Operation = {
  id: 'repoSearch',
  method: 'GET',
  path: '/repos/search',
  resource: 'repos',
  name: 'search',
  params: [
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'topic', name: 'topic', location: 'query' },
    { wire: 'includeDesc', name: 'includeDesc', location: 'query' },
    { wire: 'uid', name: 'uid', location: 'query' },
    { wire: 'priority_owner_id', name: 'priorityOwnerId', location: 'query' },
    { wire: 'team_id', name: 'teamId', location: 'query' },
    { wire: 'starredBy', name: 'starredBy', location: 'query' },
    { wire: 'private', name: '_private', location: 'query' },
    { wire: 'is_private', name: 'isPrivate', location: 'query' },
    { wire: 'template', name: 'template', location: 'query' },
    { wire: 'archived', name: 'archived', location: 'query' },
    { wire: 'mode', name: 'mode', location: 'query' },
    { wire: 'exclusive', name: 'exclusive', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSearch',
  paging: { style: 'link_header', items: 'data', rel: 'next', params: ['page', 'limit'] },
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

const repoSigningKey: Operation = {
  id: 'repoSigningKey',
  method: 'GET',
  path: '/repos/{owner}/{repo}/signing-key.gpg',
  resource: 'repos',
  name: 'getSigningKey',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoSigningKeySSH: Operation = {
  id: 'repoSigningKeySSH',
  method: 'GET',
  path: '/repos/{owner}/{repo}/signing-key.pub',
  resource: 'repos',
  name: 'getSshSigningKey',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoTrackedTimes: Operation = {
  id: 'repoTrackedTimes',
  method: 'GET',
  path: '/repos/{owner}/{repo}/times',
  resource: 'repos',
  name: 'listTrackedTimes',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoTransfer: Operation = {
  id: 'repoTransfer',
  method: 'POST',
  path: '/repos/{owner}/{repo}/transfer',
  resource: 'repos',
  name: 'transfer',
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

const repoUpdateAvatar: Operation = {
  id: 'repoUpdateAvatar',
  method: 'POST',
  path: '/repos/{owner}/{repo}/avatar',
  resource: 'repos',
  name: 'updateAvatar',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoUpdateTopics: Operation = {
  id: 'repoUpdateTopics',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/topics',
  resource: 'repos',
  name: 'replaceTopics',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoValidateIssueConfig: Operation = {
  id: 'repoValidateIssueConfig',
  method: 'GET',
  path: '/repos/{owner}/{repo}/issue_config/validate',
  resource: 'repos',
  name: 'validateIssueConfig',
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

const topicSearch: Operation = {
  id: 'topicSearch',
  method: 'GET',
  path: '/topics/search',
  resource: 'repos',
  name: 'searchTopics',
  params: [
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSearchTopics',
  paging: { style: 'link_header', items: 'topics', rel: 'next', params: ['page', 'limit'] },
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
  acceptRepoTransfer,
  createFork,
  generateRepo,
  listForks,
  rejectRepoTransfer,
  repoAddCollaborator,
  repoAddPushMirror,
  repoAddTeam,
  repoAddTopic,
  repoCheckAssignee,
  repoCheckCollaborator,
  repoCheckTeam,
  repoCreateDeployToken,
  repoCreateKey,
  repoDelete,
  repoDeleteAvatar,
  repoDeleteCollaborator,
  repoDeleteKey,
  repoDeletePushMirror,
  repoDeleteTeam,
  repoDeleteTopic,
  repoEdit,
  repoGet,
  repoGetArchive,
  repoGetAssignees,
  repoGetByID,
  repoGetIssueConfig,
  repoGetIssueTemplates,
  repoGetKey,
  repoGetLanguages,
  repoGetLicenses,
  repoGetPushMirrorByRemoteName,
  repoGetRepoPermissions,
  repoGetReviewers,
  repoListActivityFeeds,
  repoListCollaborators,
  repoListKeys,
  repoListPushMirrors,
  repoListStargazers,
  repoListSubscribers,
  repoListTeams,
  repoListTopics,
  repoMergeUpstream,
  repoMigrate,
  repoMirrorSync,
  repoNewPinAllowed,
  repoPushMirrorSync,
  repoSearch,
  repoSigningKey,
  repoSigningKeySSH,
  repoTrackedTimes,
  repoTransfer,
  repoUpdateAvatar,
  repoUpdateTopics,
  repoValidateIssueConfig,
  topicSearch,
];

export class ReposApi extends Resource {
  /** Accept a repository transfer (acceptRepoTransfer). */
  acceptTransfer(owner: string, repo: string, options?: RequestOptions): Promise<Repository> {
    return this.call(acceptRepoTransfer, undefined, { owner, repo }, options);
  }

  /** Fork a repository (createFork). */
  fork(owner: string, repo: string, body?: CreateForkOption, options?: RequestOptions): Promise<Repository> {
    return this.call(createFork, body, { owner, repo }, options);
  }

  /** Create a repository from a template repository (generateRepo). */
  generate(
    templateOwner: string,
    templateRepo: string,
    body?: GenerateRepoOption,
    options?: RequestOptions,
  ): Promise<Repository> {
    return this.call(generateRepo, body, { templateOwner, templateRepo }, options);
  }

  /** List one page of a repository's forks (listForks). */
  listForks(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Repository>> {
    return this.call(listForks, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForks(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(listForks, undefined, { owner, repo, ...params }, options);
  }

  /** Reject a repository transfer (rejectRepoTransfer). */
  rejectTransfer(owner: string, repo: string, options?: RequestOptions): Promise<Repository> {
    return this.call(rejectRepoTransfer, undefined, { owner, repo }, options);
  }

  /** Add a collaborator, or change a collaborator's permission (repoAddCollaborator). */
  addCollaborator(
    owner: string,
    repo: string,
    collaborator: string,
    body?: AddCollaboratorOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoAddCollaborator, body, { owner, repo, collaborator }, options);
  }

  /** Add a push mirror (repoAddPushMirror). */
  addPushMirror(
    owner: string,
    repo: string,
    body?: CreatePushMirrorOption,
    options?: RequestOptions,
  ): Promise<PushMirror> {
    return this.call(repoAddPushMirror, body, { owner, repo }, options);
  }

  /** Give a team access to a repository (repoAddTeam). */
  addTeam(owner: string, repo: string, team: string, options?: RequestOptions): Promise<void> {
    return this.call(repoAddTeam, undefined, { owner, repo, team }, options);
  }

  /** Add a topic to a repository (repoAddTopic). */
  addTopic(owner: string, repo: string, topic: string, options?: RequestOptions): Promise<void> {
    return this.call(repoAddTopic, undefined, { owner, repo, topic }, options);
  }

  /** Check whether a user can be assigned issues and pull requests (repoCheckAssignee). */
  checkAssignee(owner: string, repo: string, assignee: string, options?: RequestOptions): Promise<void> {
    return this.call(repoCheckAssignee, undefined, { owner, repo, assignee }, options);
  }

  /** Check whether a user is a collaborator (repoCheckCollaborator). */
  checkCollaborator(owner: string, repo: string, collaborator: string, options?: RequestOptions): Promise<void> {
    return this.call(repoCheckCollaborator, undefined, { owner, repo, collaborator }, options);
  }

  /** Check whether a team has access to a repository (repoCheckTeam). */
  checkTeam(owner: string, repo: string, team: string, options?: RequestOptions): Promise<Team> {
    return this.call(repoCheckTeam, undefined, { owner, repo, team }, options);
  }

  /** Create a deploy token, for Git over HTTPS (repoCreateDeployToken). */
  createDeployToken(
    owner: string,
    repo: string,
    body?: CreateDeployKeyTokenOption,
    options?: RequestOptions,
  ): Promise<DeployKey> {
    return this.call(repoCreateDeployToken, body, { owner, repo }, options);
  }

  /** Add a deploy key (repoCreateKey). */
  addDeployKey(owner: string, repo: string, body?: CreateKeyOption, options?: RequestOptions): Promise<DeployKey> {
    return this.call(repoCreateKey, body, { owner, repo }, options);
  }

  /** Delete a repository (repoDelete). */
  delete(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDelete, undefined, { owner, repo }, options);
  }

  /** Remove a repository's avatar (repoDeleteAvatar). */
  deleteAvatar(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteAvatar, undefined, { owner, repo }, options);
  }

  /** Remove a collaborator (repoDeleteCollaborator). */
  removeCollaborator(owner: string, repo: string, collaborator: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteCollaborator, undefined, { owner, repo, collaborator }, options);
  }

  /** Delete a deploy key (repoDeleteKey). */
  deleteDeployKey(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteKey, undefined, { owner, repo, id }, options);
  }

  /** Delete a push mirror (repoDeletePushMirror). */
  deletePushMirror(owner: string, repo: string, name: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeletePushMirror, undefined, { owner, repo, name }, options);
  }

  /** Remove a team's access to a repository (repoDeleteTeam). */
  removeTeam(owner: string, repo: string, team: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteTeam, undefined, { owner, repo, team }, options);
  }

  /** Remove a topic from a repository (repoDeleteTopic). */
  removeTopic(owner: string, repo: string, topic: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteTopic, undefined, { owner, repo, topic }, options);
  }

  /** Change a repository's settings (repoEdit). */
  update(owner: string, repo: string, body?: EditRepoOption, options?: RequestOptions): Promise<Repository> {
    return this.call(repoEdit, body, { owner, repo }, options);
  }

  /** Get a repository (repoGet). */
  get(owner: string, repo: string, options?: RequestOptions): Promise<Repository> {
    return this.call(repoGet, undefined, { owner, repo }, options);
  }

  /** Download an archive of a repository at a ref (repoGetArchive). */
  downloadArchive(
    owner: string,
    repo: string,
    archive: string,
    params: { path?: Array<string> } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(repoGetArchive, undefined, { owner, repo, archive, ...params }, options);
  }

  /** List the users that issues and pull requests can be assigned to (repoGetAssignees). */
  listAssignees(owner: string, repo: string, options?: RequestOptions): Promise<Array<User>> {
    return this.call(repoGetAssignees, undefined, { owner, repo }, options);
  }

  /** Get a repository by its ID (repoGetByID). */
  getById(id: number, options?: RequestOptions): Promise<Repository> {
    return this.call(repoGetByID, undefined, { id }, options);
  }

  /** Get a repository's issue template configuration (repoGetIssueConfig). */
  getIssueConfig(owner: string, repo: string, options?: RequestOptions): Promise<IssueConfig> {
    return this.call(repoGetIssueConfig, undefined, { owner, repo }, options);
  }

  /** List a repository's issue templates (repoGetIssueTemplates). */
  listIssueTemplates(owner: string, repo: string, options?: RequestOptions): Promise<Array<IssueTemplate>> {
    return this.call(repoGetIssueTemplates, undefined, { owner, repo }, options);
  }

  /** Get a deploy key (repoGetKey). */
  getDeployKey(owner: string, repo: string, id: number, options?: RequestOptions): Promise<DeployKey> {
    return this.call(repoGetKey, undefined, { owner, repo, id }, options);
  }

  /** Get how many bytes of each language a repository holds (repoGetLanguages). */
  getLanguages(owner: string, repo: string, options?: RequestOptions): Promise<{ [key: string]: number }> {
    return this.call(repoGetLanguages, undefined, { owner, repo }, options);
  }

  /** List the licenses found in a repository (repoGetLicenses). */
  listLicenses(owner: string, repo: string, options?: RequestOptions): Promise<Array<string>> {
    return this.call(repoGetLicenses, undefined, { owner, repo }, options);
  }

  /** Get a push mirror by its remote name (repoGetPushMirrorByRemoteName). */
  getPushMirror(owner: string, repo: string, name: string, options?: RequestOptions): Promise<PushMirror> {
    return this.call(repoGetPushMirrorByRemoteName, undefined, { owner, repo, name }, options);
  }

  /** Get a user's permissions on a repository (repoGetRepoPermissions). */
  getPermissions(
    owner: string,
    repo: string,
    collaborator: string,
    options?: RequestOptions,
  ): Promise<RepoCollaboratorPermission> {
    return this.call(repoGetRepoPermissions, undefined, { owner, repo, collaborator }, options);
  }

  /** List the users that can be asked to review pull requests (repoGetReviewers). */
  listReviewers(owner: string, repo: string, options?: RequestOptions): Promise<Array<User>> {
    return this.call(repoGetReviewers, undefined, { owner, repo }, options);
  }

  /** List one page of a repository's activity (repoListActivityFeeds). */
  listActivityFeeds(
    owner: string,
    repo: string,
    params: { date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Activity>> {
    return this.call(repoListActivityFeeds, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterActivityFeeds(
    owner: string,
    repo: string,
    params: { date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Activity, void, undefined> {
    return this.paginate(repoListActivityFeeds, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of a repository's collaborators (repoListCollaborators). */
  listCollaborators(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(repoListCollaborators, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterCollaborators(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(repoListCollaborators, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of a repository's deploy keys (repoListKeys). */
  listDeployKeys(
    owner: string,
    repo: string,
    params: { keyId?: number; fingerprint?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<DeployKey>> {
    return this.call(repoListKeys, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterDeployKeys(
    owner: string,
    repo: string,
    params: { keyId?: number; fingerprint?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.DeployKey, void, undefined> {
    return this.paginate(repoListKeys, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of a repository's push mirrors (repoListPushMirrors). */
  listPushMirrors(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<PushMirror>> {
    return this.call(repoListPushMirrors, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterPushMirrors(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PushMirror, void, undefined> {
    return this.paginate(repoListPushMirrors, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of the users who starred a repository (repoListStargazers). */
  listStargazers(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(repoListStargazers, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStargazers(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(repoListStargazers, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of the users who watch a repository (repoListSubscribers). */
  listWatchers(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(repoListSubscribers, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterWatchers(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(repoListSubscribers, undefined, { owner, repo, ...params }, options);
  }

  /** List the teams that have access to a repository (repoListTeams). */
  listTeams(owner: string, repo: string, options?: RequestOptions): Promise<Array<Team>> {
    return this.call(repoListTeams, undefined, { owner, repo }, options);
  }

  /** List a page of a repository's topics (repoListTopics). */
  listTopics(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<TopicName> {
    return this.call(repoListTopics, undefined, { owner, repo, ...params }, options);
  }

  /** Merge a branch from a fork's upstream repository (repoMergeUpstream). */
  mergeUpstream(
    owner: string,
    repo: string,
    body?: MergeUpstreamRequest,
    options?: RequestOptions,
  ): Promise<MergeUpstreamResponse> {
    return this.call(repoMergeUpstream, body, { owner, repo }, options);
  }

  /** Migrate a repository from another service (repoMigrate). */
  migrate(body?: MigrateRepoOptions, options?: RequestOptions): Promise<Repository> {
    return this.call(repoMigrate, body, {}, options);
  }

  /** Sync a mirror repository from its remote (repoMirrorSync). */
  syncMirror(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(repoMirrorSync, undefined, { owner, repo }, options);
  }

  /** Check whether more issues and pull requests can be pinned (repoNewPinAllowed). */
  checkPinAllowed(owner: string, repo: string, options?: RequestOptions): Promise<NewIssuePinsAllowed> {
    return this.call(repoNewPinAllowed, undefined, { owner, repo }, options);
  }

  /** Push a repository to all of its push mirrors (repoPushMirrorSync). */
  syncPushMirrors(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(repoPushMirrorSync, undefined, { owner, repo }, options);
  }

  /** Get one page of the repositories that match a search (repoSearch). */
  search(
    params: {
      q?: string;
      topic?: boolean;
      includeDesc?: boolean;
      uid?: number;
      priorityOwnerId?: number;
      teamId?: number;
      starredBy?: number;
      _private?: boolean;
      isPrivate?: boolean;
      template?: boolean;
      archived?: boolean;
      mode?: string;
      exclusive?: boolean;
      sort?: string;
      order?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<SearchResults> {
    return this.call(repoSearch, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSearch(
    params: {
      q?: string;
      topic?: boolean;
      includeDesc?: boolean;
      uid?: number;
      priorityOwnerId?: number;
      teamId?: number;
      starredBy?: number;
      _private?: boolean;
      isPrivate?: boolean;
      template?: boolean;
      archived?: boolean;
      mode?: string;
      exclusive?: boolean;
      sort?: string;
      order?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(repoSearch, undefined, { ...params }, options);
  }

  /** Get the GPG key a repository signs commits with (repoSigningKey). */
  getSigningKey(owner: string, repo: string, options?: RequestOptions): Promise<string> {
    return this.call(repoSigningKey, undefined, { owner, repo }, options);
  }

  /** Get the SSH key a repository signs commits with (repoSigningKeySSH). */
  getSshSigningKey(owner: string, repo: string, options?: RequestOptions): Promise<string> {
    return this.call(repoSigningKeySSH, undefined, { owner, repo }, options);
  }

  /** List one page of the time tracked on a repository (repoTrackedTimes). */
  listTrackedTimes(
    owner: string,
    repo: string,
    params: { user?: string; since?: string; before?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<TrackedTime>> {
    return this.call(repoTrackedTimes, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTrackedTimes(
    owner: string,
    repo: string,
    params: { user?: string; since?: string; before?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TrackedTime, void, undefined> {
    return this.paginate(repoTrackedTimes, undefined, { owner, repo, ...params }, options);
  }

  /** Start transferring a repository to a new owner (repoTransfer). */
  transfer(owner: string, repo: string, body: TransferRepoOption, options?: RequestOptions): Promise<Repository> {
    return this.call(repoTransfer, body, { owner, repo }, options);
  }

  /** Set a repository's avatar (repoUpdateAvatar). */
  updateAvatar(owner: string, repo: string, body?: UpdateRepoAvatarOption, options?: RequestOptions): Promise<void> {
    return this.call(repoUpdateAvatar, body, { owner, repo }, options);
  }

  /** Replace a repository's topics (repoUpdateTopics). */
  replaceTopics(owner: string, repo: string, body?: RepoTopicOptions, options?: RequestOptions): Promise<void> {
    return this.call(repoUpdateTopics, body, { owner, repo }, options);
  }

  /** Check a repository's issue template configuration (repoValidateIssueConfig). */
  validateIssueConfig(owner: string, repo: string, options?: RequestOptions): Promise<IssueConfigValidation> {
    return this.call(repoValidateIssueConfig, undefined, { owner, repo }, options);
  }

  /** Get one page of the topics that match a keyword (topicSearch). */
  searchTopics(
    params: { q: string; page?: number; limit?: number },
    options?: RequestOptions,
  ): Promise<TopicListResponse> {
    return this.call(topicSearch, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSearchTopics(
    params: { q: string; page?: number; limit?: number },
    options?: RequestOptions,
  ): AsyncGenerator<models.TopicResponse, void, undefined> {
    return this.paginate(topicSearch, undefined, { ...params }, options);
  }
}
