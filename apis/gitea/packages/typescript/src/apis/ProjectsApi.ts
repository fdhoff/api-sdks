// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  CreateProjectColumnOption,
  CreateProjectOption,
  EditProjectColumnOption,
  EditProjectOption,
  Issue,
  MoveProjectColumnsOption,
  MoveProjectIssueOption,
  Project,
  ProjectColumn,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const orgAddIssueToProjectColumn: Operation = {
  id: 'orgAddIssueToProjectColumn',
  method: 'POST',
  path: '/orgs/{org}/projects/{id}/columns/{column_id}/issues/{issue_id}',
  resource: 'projects',
  name: 'addIssueToColumnForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const orgCreateProject: Operation = {
  id: 'orgCreateProject',
  method: 'POST',
  path: '/orgs/{org}/projects',
  resource: 'projects',
  name: 'createForOrg',
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

const orgCreateProjectColumn: Operation = {
  id: 'orgCreateProjectColumn',
  method: 'POST',
  path: '/orgs/{org}/projects/{id}/columns',
  resource: 'projects',
  name: 'createColumnForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
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

const orgDeleteProject: Operation = {
  id: 'orgDeleteProject',
  method: 'DELETE',
  path: '/orgs/{org}/projects/{id}',
  resource: 'projects',
  name: 'deleteForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
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

const orgDeleteProjectColumn: Operation = {
  id: 'orgDeleteProjectColumn',
  method: 'DELETE',
  path: '/orgs/{org}/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'deleteColumnForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const orgEditProject: Operation = {
  id: 'orgEditProject',
  method: 'PATCH',
  path: '/orgs/{org}/projects/{id}',
  resource: 'projects',
  name: 'updateForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
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

const orgEditProjectColumn: Operation = {
  id: 'orgEditProjectColumn',
  method: 'PATCH',
  path: '/orgs/{org}/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'updateColumnForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const orgGetProject: Operation = {
  id: 'orgGetProject',
  method: 'GET',
  path: '/orgs/{org}/projects/{id}',
  resource: 'projects',
  name: 'getForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
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

const orgGetProjectColumn: Operation = {
  id: 'orgGetProjectColumn',
  method: 'GET',
  path: '/orgs/{org}/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'getColumnForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const orgListProjectColumnIssues: Operation = {
  id: 'orgListProjectColumnIssues',
  method: 'GET',
  path: '/orgs/{org}/projects/{id}/columns/{column_id}/issues',
  resource: 'projects',
  name: 'listColumnIssuesForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterColumnIssuesForOrg',
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

const orgListProjectColumns: Operation = {
  id: 'orgListProjectColumns',
  method: 'GET',
  path: '/orgs/{org}/projects/{id}/columns',
  resource: 'projects',
  name: 'listColumnsForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterColumnsForOrg',
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

const orgListProjects: Operation = {
  id: 'orgListProjects',
  method: 'GET',
  path: '/orgs/{org}/projects',
  resource: 'projects',
  name: 'listForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterForOrg',
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

const orgMoveProjectColumns: Operation = {
  id: 'orgMoveProjectColumns',
  method: 'POST',
  path: '/orgs/{org}/projects/{id}/columns/move',
  resource: 'projects',
  name: 'reorderColumnsForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
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

const orgMoveProjectIssue: Operation = {
  id: 'orgMoveProjectIssue',
  method: 'POST',
  path: '/orgs/{org}/projects/{id}/issues/{issue_id}/move',
  resource: 'projects',
  name: 'moveIssueForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const orgRemoveIssueFromProjectColumn: Operation = {
  id: 'orgRemoveIssueFromProjectColumn',
  method: 'DELETE',
  path: '/orgs/{org}/projects/{id}/columns/{column_id}/issues/{issue_id}',
  resource: 'projects',
  name: 'removeIssueFromColumnForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const orgSetDefaultProjectColumn: Operation = {
  id: 'orgSetDefaultProjectColumn',
  method: 'POST',
  path: '/orgs/{org}/projects/{id}/columns/{column_id}/default',
  resource: 'projects',
  name: 'setDefaultColumnForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const repoAddIssueToProjectColumn: Operation = {
  id: 'repoAddIssueToProjectColumn',
  method: 'POST',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues/{issue_id}',
  resource: 'projects',
  name: 'addIssueToColumn',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const repoCreateProject: Operation = {
  id: 'repoCreateProject',
  method: 'POST',
  path: '/repos/{owner}/{repo}/projects',
  resource: 'projects',
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

const repoCreateProjectColumn: Operation = {
  id: 'repoCreateProjectColumn',
  method: 'POST',
  path: '/repos/{owner}/{repo}/projects/{id}/columns',
  resource: 'projects',
  name: 'createColumn',
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

const repoDeleteProject: Operation = {
  id: 'repoDeleteProject',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/projects/{id}',
  resource: 'projects',
  name: 'delete',
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

const repoDeleteProjectColumn: Operation = {
  id: 'repoDeleteProjectColumn',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'deleteColumn',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const repoEditProject: Operation = {
  id: 'repoEditProject',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/projects/{id}',
  resource: 'projects',
  name: 'update',
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

const repoEditProjectColumn: Operation = {
  id: 'repoEditProjectColumn',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'updateColumn',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const repoGetProject: Operation = {
  id: 'repoGetProject',
  method: 'GET',
  path: '/repos/{owner}/{repo}/projects/{id}',
  resource: 'projects',
  name: 'get',
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

const repoGetProjectColumn: Operation = {
  id: 'repoGetProjectColumn',
  method: 'GET',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'getColumn',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const repoListProjectColumnIssues: Operation = {
  id: 'repoListProjectColumnIssues',
  method: 'GET',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues',
  resource: 'projects',
  name: 'listColumnIssues',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterColumnIssues',
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

const repoListProjectColumns: Operation = {
  id: 'repoListProjectColumns',
  method: 'GET',
  path: '/repos/{owner}/{repo}/projects/{id}/columns',
  resource: 'projects',
  name: 'listColumns',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterColumns',
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

const repoListProjects: Operation = {
  id: 'repoListProjects',
  method: 'GET',
  path: '/repos/{owner}/{repo}/projects',
  resource: 'projects',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'state', name: 'state', location: 'query' },
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

const repoMoveProjectColumns: Operation = {
  id: 'repoMoveProjectColumns',
  method: 'POST',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/move',
  resource: 'projects',
  name: 'reorderColumns',
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

const repoMoveProjectIssue: Operation = {
  id: 'repoMoveProjectIssue',
  method: 'POST',
  path: '/repos/{owner}/{repo}/projects/{id}/issues/{issue_id}/move',
  resource: 'projects',
  name: 'moveIssue',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const repoRemoveIssueFromProjectColumn: Operation = {
  id: 'repoRemoveIssueFromProjectColumn',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues/{issue_id}',
  resource: 'projects',
  name: 'removeIssueFromColumn',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const repoSetDefaultProjectColumn: Operation = {
  id: 'repoSetDefaultProjectColumn',
  method: 'POST',
  path: '/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/default',
  resource: 'projects',
  name: 'setDefaultColumn',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const userCurrentAddIssueToProjectColumn: Operation = {
  id: 'userCurrentAddIssueToProjectColumn',
  method: 'POST',
  path: '/user/projects/{id}/columns/{column_id}/issues/{issue_id}',
  resource: 'projects',
  name: 'addIssueToColumnForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const userCurrentCreateProject: Operation = {
  id: 'userCurrentCreateProject',
  method: 'POST',
  path: '/user/projects',
  resource: 'projects',
  name: 'createForUser',
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

const userCurrentCreateProjectColumn: Operation = {
  id: 'userCurrentCreateProjectColumn',
  method: 'POST',
  path: '/user/projects/{id}/columns',
  resource: 'projects',
  name: 'createColumnForUser',
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

const userCurrentDeleteProject: Operation = {
  id: 'userCurrentDeleteProject',
  method: 'DELETE',
  path: '/user/projects/{id}',
  resource: 'projects',
  name: 'deleteForUser',
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

const userCurrentDeleteProjectColumn: Operation = {
  id: 'userCurrentDeleteProjectColumn',
  method: 'DELETE',
  path: '/user/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'deleteColumnForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const userCurrentEditProject: Operation = {
  id: 'userCurrentEditProject',
  method: 'PATCH',
  path: '/user/projects/{id}',
  resource: 'projects',
  name: 'updateForUser',
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

const userCurrentEditProjectColumn: Operation = {
  id: 'userCurrentEditProjectColumn',
  method: 'PATCH',
  path: '/user/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'updateColumnForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const userCurrentGetProject: Operation = {
  id: 'userCurrentGetProject',
  method: 'GET',
  path: '/user/projects/{id}',
  resource: 'projects',
  name: 'getForUser',
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

const userCurrentGetProjectColumn: Operation = {
  id: 'userCurrentGetProjectColumn',
  method: 'GET',
  path: '/user/projects/{id}/columns/{column_id}',
  resource: 'projects',
  name: 'getColumnForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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

const userCurrentListProjectColumnIssues: Operation = {
  id: 'userCurrentListProjectColumnIssues',
  method: 'GET',
  path: '/user/projects/{id}/columns/{column_id}/issues',
  resource: 'projects',
  name: 'listColumnIssuesForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterColumnIssuesForUser',
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

const userCurrentListProjectColumns: Operation = {
  id: 'userCurrentListProjectColumns',
  method: 'GET',
  path: '/user/projects/{id}/columns',
  resource: 'projects',
  name: 'listColumnsForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterColumnsForUser',
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

const userCurrentListProjects: Operation = {
  id: 'userCurrentListProjects',
  method: 'GET',
  path: '/user/projects',
  resource: 'projects',
  name: 'listForUser',
  params: [
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterForUser',
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

const userCurrentMoveProjectColumns: Operation = {
  id: 'userCurrentMoveProjectColumns',
  method: 'POST',
  path: '/user/projects/{id}/columns/move',
  resource: 'projects',
  name: 'reorderColumnsForUser',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
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

const userCurrentMoveProjectIssue: Operation = {
  id: 'userCurrentMoveProjectIssue',
  method: 'POST',
  path: '/user/projects/{id}/issues/{issue_id}/move',
  resource: 'projects',
  name: 'moveIssueForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const userCurrentRemoveIssueFromProjectColumn: Operation = {
  id: 'userCurrentRemoveIssueFromProjectColumn',
  method: 'DELETE',
  path: '/user/projects/{id}/columns/{column_id}/issues/{issue_id}',
  resource: 'projects',
  name: 'removeIssueFromColumnForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
    { wire: 'issue_id', name: 'issueId', location: 'path' },
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

const userCurrentSetDefaultProjectColumn: Operation = {
  id: 'userCurrentSetDefaultProjectColumn',
  method: 'POST',
  path: '/user/projects/{id}/columns/{column_id}/default',
  resource: 'projects',
  name: 'setDefaultColumnForUser',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'column_id', name: 'columnId', location: 'path' },
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
  orgAddIssueToProjectColumn,
  orgCreateProject,
  orgCreateProjectColumn,
  orgDeleteProject,
  orgDeleteProjectColumn,
  orgEditProject,
  orgEditProjectColumn,
  orgGetProject,
  orgGetProjectColumn,
  orgListProjectColumnIssues,
  orgListProjectColumns,
  orgListProjects,
  orgMoveProjectColumns,
  orgMoveProjectIssue,
  orgRemoveIssueFromProjectColumn,
  orgSetDefaultProjectColumn,
  repoAddIssueToProjectColumn,
  repoCreateProject,
  repoCreateProjectColumn,
  repoDeleteProject,
  repoDeleteProjectColumn,
  repoEditProject,
  repoEditProjectColumn,
  repoGetProject,
  repoGetProjectColumn,
  repoListProjectColumnIssues,
  repoListProjectColumns,
  repoListProjects,
  repoMoveProjectColumns,
  repoMoveProjectIssue,
  repoRemoveIssueFromProjectColumn,
  repoSetDefaultProjectColumn,
  userCurrentAddIssueToProjectColumn,
  userCurrentCreateProject,
  userCurrentCreateProjectColumn,
  userCurrentDeleteProject,
  userCurrentDeleteProjectColumn,
  userCurrentEditProject,
  userCurrentEditProjectColumn,
  userCurrentGetProject,
  userCurrentGetProjectColumn,
  userCurrentListProjectColumnIssues,
  userCurrentListProjectColumns,
  userCurrentListProjects,
  userCurrentMoveProjectColumns,
  userCurrentMoveProjectIssue,
  userCurrentRemoveIssueFromProjectColumn,
  userCurrentSetDefaultProjectColumn,
];

export class ProjectsApi extends Resource {
  /** Add an issue to an organization project column (orgAddIssueToProjectColumn). */
  addIssueToColumnForOrg(
    org: string,
    id: number,
    columnId: number,
    issueId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(orgAddIssueToProjectColumn, undefined, { org, id, columnId, issueId }, options);
  }

  /** Create an organization project (orgCreateProject). */
  createForOrg(org: string, body?: CreateProjectOption, options?: RequestOptions): Promise<Project> {
    return this.call(orgCreateProject, body, { org }, options);
  }

  /** Add a column to an organization project (orgCreateProjectColumn). */
  createColumnForOrg(
    org: string,
    id: number,
    body?: CreateProjectColumnOption,
    options?: RequestOptions,
  ): Promise<ProjectColumn> {
    return this.call(orgCreateProjectColumn, body, { org, id }, options);
  }

  /** Delete an organization project (orgDeleteProject). */
  deleteForOrg(org: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteProject, undefined, { org, id }, options);
  }

  /** Delete an organization project column (orgDeleteProjectColumn). */
  deleteColumnForOrg(org: string, id: number, columnId: number, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteProjectColumn, undefined, { org, id, columnId }, options);
  }

  /** Change an organization project (orgEditProject). */
  updateForOrg(org: string, id: number, body?: EditProjectOption, options?: RequestOptions): Promise<Project> {
    return this.call(orgEditProject, body, { org, id }, options);
  }

  /** Change an organization project column (orgEditProjectColumn). */
  updateColumnForOrg(
    org: string,
    id: number,
    columnId: number,
    body?: EditProjectColumnOption,
    options?: RequestOptions,
  ): Promise<ProjectColumn> {
    return this.call(orgEditProjectColumn, body, { org, id, columnId }, options);
  }

  /** Get an organization project (orgGetProject). */
  getForOrg(org: string, id: number, options?: RequestOptions): Promise<Project> {
    return this.call(orgGetProject, undefined, { org, id }, options);
  }

  /** Get an organization project column (orgGetProjectColumn). */
  getColumnForOrg(org: string, id: number, columnId: number, options?: RequestOptions): Promise<ProjectColumn> {
    return this.call(orgGetProjectColumn, undefined, { org, id, columnId }, options);
  }

  /** List one page of the issues in an organization project column (orgListProjectColumnIssues). */
  listColumnIssuesForOrg(
    org: string,
    id: number,
    columnId: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Issue>> {
    return this.call(orgListProjectColumnIssues, undefined, { org, id, columnId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterColumnIssuesForOrg(
    org: string,
    id: number,
    columnId: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Issue, void, undefined> {
    return this.paginate(orgListProjectColumnIssues, undefined, { org, id, columnId, ...params }, options);
  }

  /** List one page of an organization project's columns (orgListProjectColumns). */
  listColumnsForOrg(
    org: string,
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<ProjectColumn>> {
    return this.call(orgListProjectColumns, undefined, { org, id, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterColumnsForOrg(
    org: string,
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ProjectColumn, void, undefined> {
    return this.paginate(orgListProjectColumns, undefined, { org, id, ...params }, options);
  }

  /** List one page of an organization's projects (orgListProjects). */
  listForOrg(
    org: string,
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Project>> {
    return this.call(orgListProjects, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForOrg(
    org: string,
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Project, void, undefined> {
    return this.paginate(orgListProjects, undefined, { org, ...params }, options);
  }

  /** Reorder an organization project's columns (orgMoveProjectColumns). */
  reorderColumnsForOrg(
    org: string,
    id: number,
    body?: MoveProjectColumnsOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(orgMoveProjectColumns, body, { org, id }, options);
  }

  /** Move an issue within an organization project (orgMoveProjectIssue). */
  moveIssueForOrg(
    org: string,
    id: number,
    issueId: number,
    body?: MoveProjectIssueOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(orgMoveProjectIssue, body, { org, id, issueId }, options);
  }

  /** Remove an issue from an organization project column (orgRemoveIssueFromProjectColumn). */
  removeIssueFromColumnForOrg(
    org: string,
    id: number,
    columnId: number,
    issueId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(orgRemoveIssueFromProjectColumn, undefined, { org, id, columnId, issueId }, options);
  }

  /** Make a column the default of an organization project (orgSetDefaultProjectColumn). */
  setDefaultColumnForOrg(org: string, id: number, columnId: number, options?: RequestOptions): Promise<void> {
    return this.call(orgSetDefaultProjectColumn, undefined, { org, id, columnId }, options);
  }

  /** Add an issue to a repository project column (repoAddIssueToProjectColumn). */
  addIssueToColumn(
    owner: string,
    repo: string,
    id: number,
    columnId: number,
    issueId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoAddIssueToProjectColumn, undefined, { owner, repo, id, columnId, issueId }, options);
  }

  /** Create a repository project (repoCreateProject). */
  create(owner: string, repo: string, body?: CreateProjectOption, options?: RequestOptions): Promise<Project> {
    return this.call(repoCreateProject, body, { owner, repo }, options);
  }

  /** Add a column to a repository project (repoCreateProjectColumn). */
  createColumn(
    owner: string,
    repo: string,
    id: number,
    body?: CreateProjectColumnOption,
    options?: RequestOptions,
  ): Promise<ProjectColumn> {
    return this.call(repoCreateProjectColumn, body, { owner, repo, id }, options);
  }

  /** Delete a repository project (repoDeleteProject). */
  delete(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteProject, undefined, { owner, repo, id }, options);
  }

  /** Delete a repository project column (repoDeleteProjectColumn). */
  deleteColumn(owner: string, repo: string, id: number, columnId: number, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteProjectColumn, undefined, { owner, repo, id, columnId }, options);
  }

  /** Change a repository project (repoEditProject). */
  update(
    owner: string,
    repo: string,
    id: number,
    body?: EditProjectOption,
    options?: RequestOptions,
  ): Promise<Project> {
    return this.call(repoEditProject, body, { owner, repo, id }, options);
  }

  /** Change a repository project column (repoEditProjectColumn). */
  updateColumn(
    owner: string,
    repo: string,
    id: number,
    columnId: number,
    body?: EditProjectColumnOption,
    options?: RequestOptions,
  ): Promise<ProjectColumn> {
    return this.call(repoEditProjectColumn, body, { owner, repo, id, columnId }, options);
  }

  /** Get a repository project (repoGetProject). */
  get(owner: string, repo: string, id: number, options?: RequestOptions): Promise<Project> {
    return this.call(repoGetProject, undefined, { owner, repo, id }, options);
  }

  /** Get a repository project column (repoGetProjectColumn). */
  getColumn(
    owner: string,
    repo: string,
    id: number,
    columnId: number,
    options?: RequestOptions,
  ): Promise<ProjectColumn> {
    return this.call(repoGetProjectColumn, undefined, { owner, repo, id, columnId }, options);
  }

  /** List one page of the issues in a repository project column (repoListProjectColumnIssues). */
  listColumnIssues(
    owner: string,
    repo: string,
    id: number,
    columnId: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Issue>> {
    return this.call(repoListProjectColumnIssues, undefined, { owner, repo, id, columnId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterColumnIssues(
    owner: string,
    repo: string,
    id: number,
    columnId: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Issue, void, undefined> {
    return this.paginate(repoListProjectColumnIssues, undefined, { owner, repo, id, columnId, ...params }, options);
  }

  /** List one page of a repository project's columns (repoListProjectColumns). */
  listColumns(
    owner: string,
    repo: string,
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<ProjectColumn>> {
    return this.call(repoListProjectColumns, undefined, { owner, repo, id, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterColumns(
    owner: string,
    repo: string,
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ProjectColumn, void, undefined> {
    return this.paginate(repoListProjectColumns, undefined, { owner, repo, id, ...params }, options);
  }

  /** List one page of a repository's projects (repoListProjects). */
  list(
    owner: string,
    repo: string,
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Project>> {
    return this.call(repoListProjects, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Project, void, undefined> {
    return this.paginate(repoListProjects, undefined, { owner, repo, ...params }, options);
  }

  /** Reorder a repository project's columns (repoMoveProjectColumns). */
  reorderColumns(
    owner: string,
    repo: string,
    id: number,
    body?: MoveProjectColumnsOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoMoveProjectColumns, body, { owner, repo, id }, options);
  }

  /** Move an issue within a repository project (repoMoveProjectIssue). */
  moveIssue(
    owner: string,
    repo: string,
    id: number,
    issueId: number,
    body?: MoveProjectIssueOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoMoveProjectIssue, body, { owner, repo, id, issueId }, options);
  }

  /** Remove an issue from a repository project column (repoRemoveIssueFromProjectColumn). */
  removeIssueFromColumn(
    owner: string,
    repo: string,
    id: number,
    columnId: number,
    issueId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoRemoveIssueFromProjectColumn, undefined, { owner, repo, id, columnId, issueId }, options);
  }

  /** Make a column the default of a repository project (repoSetDefaultProjectColumn). */
  setDefaultColumn(owner: string, repo: string, id: number, columnId: number, options?: RequestOptions): Promise<void> {
    return this.call(repoSetDefaultProjectColumn, undefined, { owner, repo, id, columnId }, options);
  }

  /** Add an issue to a column of one of your projects (userCurrentAddIssueToProjectColumn). */
  addIssueToColumnForUser(id: number, columnId: number, issueId: number, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentAddIssueToProjectColumn, undefined, { id, columnId, issueId }, options);
  }

  /** Create a project of your own (userCurrentCreateProject). */
  createForUser(body?: CreateProjectOption, options?: RequestOptions): Promise<Project> {
    return this.call(userCurrentCreateProject, body, {}, options);
  }

  /** Add a column to one of your projects (userCurrentCreateProjectColumn). */
  createColumnForUser(id: number, body?: CreateProjectColumnOption, options?: RequestOptions): Promise<ProjectColumn> {
    return this.call(userCurrentCreateProjectColumn, body, { id }, options);
  }

  /** Delete one of your projects (userCurrentDeleteProject). */
  deleteForUser(id: number, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentDeleteProject, undefined, { id }, options);
  }

  /** Delete a column of one of your projects (userCurrentDeleteProjectColumn). */
  deleteColumnForUser(id: number, columnId: number, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentDeleteProjectColumn, undefined, { id, columnId }, options);
  }

  /** Change one of your projects (userCurrentEditProject). */
  updateForUser(id: number, body?: EditProjectOption, options?: RequestOptions): Promise<Project> {
    return this.call(userCurrentEditProject, body, { id }, options);
  }

  /** Change a column of one of your projects (userCurrentEditProjectColumn). */
  updateColumnForUser(
    id: number,
    columnId: number,
    body?: EditProjectColumnOption,
    options?: RequestOptions,
  ): Promise<ProjectColumn> {
    return this.call(userCurrentEditProjectColumn, body, { id, columnId }, options);
  }

  /** Get one of your projects (userCurrentGetProject). */
  getForUser(id: number, options?: RequestOptions): Promise<Project> {
    return this.call(userCurrentGetProject, undefined, { id }, options);
  }

  /** Get a column of one of your projects (userCurrentGetProjectColumn). */
  getColumnForUser(id: number, columnId: number, options?: RequestOptions): Promise<ProjectColumn> {
    return this.call(userCurrentGetProjectColumn, undefined, { id, columnId }, options);
  }

  /** List one page of the issues in a column of one of your projects (userCurrentListProjectColumnIssues). */
  listColumnIssuesForUser(
    id: number,
    columnId: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Issue>> {
    return this.call(userCurrentListProjectColumnIssues, undefined, { id, columnId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterColumnIssuesForUser(
    id: number,
    columnId: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Issue, void, undefined> {
    return this.paginate(userCurrentListProjectColumnIssues, undefined, { id, columnId, ...params }, options);
  }

  /** List one page of the columns of one of your projects (userCurrentListProjectColumns). */
  listColumnsForUser(
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<ProjectColumn>> {
    return this.call(userCurrentListProjectColumns, undefined, { id, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterColumnsForUser(
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ProjectColumn, void, undefined> {
    return this.paginate(userCurrentListProjectColumns, undefined, { id, ...params }, options);
  }

  /** List one page of your own projects (userCurrentListProjects). */
  listForUser(
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Project>> {
    return this.call(userCurrentListProjects, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForUser(
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Project, void, undefined> {
    return this.paginate(userCurrentListProjects, undefined, { ...params }, options);
  }

  /** Reorder the columns of one of your projects (userCurrentMoveProjectColumns). */
  reorderColumnsForUser(id: number, body?: MoveProjectColumnsOption, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentMoveProjectColumns, body, { id }, options);
  }

  /** Move an issue within one of your projects (userCurrentMoveProjectIssue). */
  moveIssueForUser(
    id: number,
    issueId: number,
    body?: MoveProjectIssueOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(userCurrentMoveProjectIssue, body, { id, issueId }, options);
  }

  /** Remove an issue from a column of one of your projects (userCurrentRemoveIssueFromProjectColumn). */
  removeIssueFromColumnForUser(id: number, columnId: number, issueId: number, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentRemoveIssueFromProjectColumn, undefined, { id, columnId, issueId }, options);
  }

  /** Make a column the default of one of your projects (userCurrentSetDefaultProjectColumn). */
  setDefaultColumnForUser(id: number, columnId: number, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentSetDefaultProjectColumn, undefined, { id, columnId }, options);
  }
}
