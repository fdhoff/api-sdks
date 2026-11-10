// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  ActionArtifact,
  ActionArtifactsResponse,
  ActionRunner,
  ActionRunnersResponse,
  ActionTaskResponse,
  ActionVariable,
  ActionWorkflow,
  ActionWorkflowJob,
  ActionWorkflowJobsResponse,
  ActionWorkflowResponse,
  ActionWorkflowRun,
  ActionWorkflowRunsResponse,
  CreateActionWorkflowDispatch,
  CreateOrUpdateSecretOption,
  CreateVariableOption,
  EditActionRunnerOption,
  RunDetails,
  Secret,
  UpdateVariableOption,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const actionsDisableWorkflow: Operation = {
  id: 'ActionsDisableWorkflow',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable',
  resource: 'actions',
  name: 'disableWorkflow',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'workflow_id', name: 'workflowId', location: 'path' },
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

const actionsDispatchWorkflow: Operation = {
  id: 'ActionsDispatchWorkflow',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches',
  resource: 'actions',
  name: 'dispatchWorkflow',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'workflow_id', name: 'workflowId', location: 'path' },
    { wire: 'return_run_details', name: 'returnRunDetails', location: 'query' },
    { wire: 'scoped_workflow_source_repo_id', name: 'scopedWorkflowSourceRepoId', location: 'query' },
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

const actionsEnableWorkflow: Operation = {
  id: 'ActionsEnableWorkflow',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable',
  resource: 'actions',
  name: 'enableWorkflow',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'workflow_id', name: 'workflowId', location: 'path' },
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

const actionsGetWorkflow: Operation = {
  id: 'ActionsGetWorkflow',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/workflows/{workflow_id}',
  resource: 'actions',
  name: 'getWorkflow',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'workflow_id', name: 'workflowId', location: 'path' },
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

const actionsListRepositoryWorkflows: Operation = {
  id: 'ActionsListRepositoryWorkflows',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/workflows',
  resource: 'actions',
  name: 'listWorkflows',
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

const actionsListWorkflowRuns: Operation = {
  id: 'ActionsListWorkflowRuns',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs',
  resource: 'actions',
  name: 'listWorkflowRuns',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'workflow_id', name: 'workflowId', location: 'path' },
    { wire: 'event', name: 'event', location: 'query' },
    { wire: 'branch', name: 'branch', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'actor', name: 'actor', location: 'query' },
    { wire: 'head_sha', name: 'headSha', location: 'query' },
    { wire: 'exclude_pull_requests', name: 'excludePullRequests', location: 'query' },
    { wire: 'scoped_workflow_source_repo_id', name: 'scopedWorkflowSourceRepoId', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterWorkflowRuns',
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

const approveWorkflowRun: Operation = {
  id: 'approveWorkflowRun',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/approve',
  resource: 'actions',
  name: 'approveRun',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const cancelWorkflowRun: Operation = {
  id: 'cancelWorkflowRun',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/cancel',
  resource: 'actions',
  name: 'cancelRun',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const createOrgVariable: Operation = {
  id: 'createOrgVariable',
  method: 'POST',
  path: '/orgs/{org}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'createVariableForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const createRepoVariable: Operation = {
  id: 'createRepoVariable',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'createVariable',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const createUserVariable: Operation = {
  id: 'createUserVariable',
  method: 'POST',
  path: '/user/actions/variables/{variablename}',
  resource: 'actions',
  name: 'createVariableForUser',
  params: [{ wire: 'variablename', name: 'variablename', location: 'path' }],
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

const deleteActionRun: Operation = {
  id: 'deleteActionRun',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/actions/runs/{run}',
  resource: 'actions',
  name: 'deleteRun',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const deleteArtifact: Operation = {
  id: 'deleteArtifact',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/actions/artifacts/{artifact_id}',
  resource: 'actions',
  name: 'deleteArtifact',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'artifact_id', name: 'artifactId', location: 'path' },
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

const deleteOrgRunner: Operation = {
  id: 'deleteOrgRunner',
  method: 'DELETE',
  path: '/orgs/{org}/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'deleteRunnerForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'runner_id', name: 'runnerId', location: 'path' },
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

const deleteOrgSecret: Operation = {
  id: 'deleteOrgSecret',
  method: 'DELETE',
  path: '/orgs/{org}/actions/secrets/{secretname}',
  resource: 'actions',
  name: 'deleteSecretForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'secretname', name: 'secretname', location: 'path' },
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

const deleteOrgVariable: Operation = {
  id: 'deleteOrgVariable',
  method: 'DELETE',
  path: '/orgs/{org}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'deleteVariableForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const deleteRepoRunner: Operation = {
  id: 'deleteRepoRunner',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'deleteRunner',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'runner_id', name: 'runnerId', location: 'path' },
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

const deleteRepoSecret: Operation = {
  id: 'deleteRepoSecret',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/actions/secrets/{secretname}',
  resource: 'actions',
  name: 'deleteSecret',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'secretname', name: 'secretname', location: 'path' },
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

const deleteRepoVariable: Operation = {
  id: 'deleteRepoVariable',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'deleteVariable',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const deleteUserRunner: Operation = {
  id: 'deleteUserRunner',
  method: 'DELETE',
  path: '/user/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'deleteRunnerForUser',
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

const deleteUserSecret: Operation = {
  id: 'deleteUserSecret',
  method: 'DELETE',
  path: '/user/actions/secrets/{secretname}',
  resource: 'actions',
  name: 'deleteSecretForUser',
  params: [{ wire: 'secretname', name: 'secretname', location: 'path' }],
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

const deleteUserVariable: Operation = {
  id: 'deleteUserVariable',
  method: 'DELETE',
  path: '/user/actions/variables/{variablename}',
  resource: 'actions',
  name: 'deleteVariableForUser',
  params: [{ wire: 'variablename', name: 'variablename', location: 'path' }],
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

const downloadActionsRunJobLogs: Operation = {
  id: 'downloadActionsRunJobLogs',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/jobs/{job_id}/logs',
  resource: 'actions',
  name: 'downloadJobLogs',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'job_id', name: 'jobId', location: 'path' },
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

const downloadArtifact: Operation = {
  id: 'downloadArtifact',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip',
  resource: 'actions',
  name: 'downloadArtifact',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'artifact_id', name: 'artifactId', location: 'path' },
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

const forceCancelWorkflowRun: Operation = {
  id: 'forceCancelWorkflowRun',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/force-cancel',
  resource: 'actions',
  name: 'forceCancelRun',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const getArtifact: Operation = {
  id: 'getArtifact',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/artifacts/{artifact_id}',
  resource: 'actions',
  name: 'getArtifact',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'artifact_id', name: 'artifactId', location: 'path' },
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

const getArtifacts: Operation = {
  id: 'getArtifacts',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/artifacts',
  resource: 'actions',
  name: 'listArtifacts',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'name', name: 'name', location: 'query' },
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

const getArtifactsOfRun: Operation = {
  id: 'getArtifactsOfRun',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/artifacts',
  resource: 'actions',
  name: 'listRunArtifacts',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
    { wire: 'name', name: 'name', location: 'query' },
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

const getOrgRunner: Operation = {
  id: 'getOrgRunner',
  method: 'GET',
  path: '/orgs/{org}/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'getRunnerForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'runner_id', name: 'runnerId', location: 'path' },
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

const getOrgRunners: Operation = {
  id: 'getOrgRunners',
  method: 'GET',
  path: '/orgs/{org}/actions/runners',
  resource: 'actions',
  name: 'listRunnersForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'disabled', name: 'disabled', location: 'query' },
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

const getOrgVariable: Operation = {
  id: 'getOrgVariable',
  method: 'GET',
  path: '/orgs/{org}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'getVariableForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const getOrgVariablesList: Operation = {
  id: 'getOrgVariablesList',
  method: 'GET',
  path: '/orgs/{org}/actions/variables',
  resource: 'actions',
  name: 'listVariablesForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterVariablesForOrg',
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

const getOrgWorkflowJobs: Operation = {
  id: 'getOrgWorkflowJobs',
  method: 'GET',
  path: '/orgs/{org}/actions/jobs',
  resource: 'actions',
  name: 'listJobsForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterJobsForOrg',
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

const getOrgWorkflowRuns: Operation = {
  id: 'getOrgWorkflowRuns',
  method: 'GET',
  path: '/orgs/{org}/actions/runs',
  resource: 'actions',
  name: 'listRunsForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'event', name: 'event', location: 'query' },
    { wire: 'branch', name: 'branch', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'actor', name: 'actor', location: 'query' },
    { wire: 'head_sha', name: 'headSha', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRunsForOrg',
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

const getRepoRunner: Operation = {
  id: 'getRepoRunner',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'getRunner',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'runner_id', name: 'runnerId', location: 'path' },
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

const getRepoRunners: Operation = {
  id: 'getRepoRunners',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runners',
  resource: 'actions',
  name: 'listRunners',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'disabled', name: 'disabled', location: 'query' },
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

const getRepoVariable: Operation = {
  id: 'getRepoVariable',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'getVariable',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const getRepoVariablesList: Operation = {
  id: 'getRepoVariablesList',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/variables',
  resource: 'actions',
  name: 'listVariables',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterVariables',
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

const getUserRunner: Operation = {
  id: 'getUserRunner',
  method: 'GET',
  path: '/user/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'getRunnerForUser',
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

const getUserRunners: Operation = {
  id: 'getUserRunners',
  method: 'GET',
  path: '/user/actions/runners',
  resource: 'actions',
  name: 'listRunnersForUser',
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

const getUserVariable: Operation = {
  id: 'getUserVariable',
  method: 'GET',
  path: '/user/actions/variables/{variablename}',
  resource: 'actions',
  name: 'getVariableForUser',
  params: [{ wire: 'variablename', name: 'variablename', location: 'path' }],
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

const getUserVariablesList: Operation = {
  id: 'getUserVariablesList',
  method: 'GET',
  path: '/user/actions/variables',
  resource: 'actions',
  name: 'listVariablesForUser',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterVariablesForUser',
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

const getUserWorkflowJobs: Operation = {
  id: 'getUserWorkflowJobs',
  method: 'GET',
  path: '/user/actions/jobs',
  resource: 'actions',
  name: 'listJobsForUser',
  params: [
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterJobsForUser',
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

const getUserWorkflowRuns: Operation = {
  id: 'getUserWorkflowRuns',
  method: 'GET',
  path: '/user/actions/runs',
  resource: 'actions',
  name: 'listRunsForUser',
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
  iterator: 'iterRunsForUser',
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

const getWorkflowJob: Operation = {
  id: 'getWorkflowJob',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/jobs/{job_id}',
  resource: 'actions',
  name: 'getJob',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'job_id', name: 'jobId', location: 'path' },
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

const getWorkflowRun: Operation = {
  id: 'GetWorkflowRun',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runs/{run}',
  resource: 'actions',
  name: 'getRun',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const getWorkflowRunAttempt: Operation = {
  id: 'getWorkflowRunAttempt',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}',
  resource: 'actions',
  name: 'getRunAttempt',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
    { wire: 'attempt', name: 'attempt', location: 'path' },
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

const getWorkflowRunLogs: Operation = {
  id: 'getWorkflowRunLogs',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/logs',
  resource: 'actions',
  name: 'downloadRunLogs',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const getWorkflowRuns: Operation = {
  id: 'getWorkflowRuns',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runs',
  resource: 'actions',
  name: 'listRuns',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'event', name: 'event', location: 'query' },
    { wire: 'branch', name: 'branch', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'actor', name: 'actor', location: 'query' },
    { wire: 'head_sha', name: 'headSha', location: 'query' },
    { wire: 'exclude_pull_requests', name: 'excludePullRequests', location: 'query' },
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

const listActionTasks: Operation = {
  id: 'ListActionTasks',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/tasks',
  resource: 'actions',
  name: 'listTasks',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTasks',
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

const listWorkflowJobs: Operation = {
  id: 'listWorkflowJobs',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/jobs',
  resource: 'actions',
  name: 'listJobs',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const listWorkflowRunAttemptJobs: Operation = {
  id: 'listWorkflowRunAttemptJobs',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs',
  resource: 'actions',
  name: 'listRunAttemptJobs',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
    { wire: 'attempt', name: 'attempt', location: 'path' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRunAttemptJobs',
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

const listWorkflowRunJobs: Operation = {
  id: 'listWorkflowRunJobs',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/jobs',
  resource: 'actions',
  name: 'listRunJobs',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRunJobs',
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

const orgCreateRunnerRegistrationToken: Operation = {
  id: 'orgCreateRunnerRegistrationToken',
  method: 'POST',
  path: '/orgs/{org}/actions/runners/registration-token',
  resource: 'actions',
  name: 'createRunnerRegistrationTokenForOrg',
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

const orgListActionsSecrets: Operation = {
  id: 'orgListActionsSecrets',
  method: 'GET',
  path: '/orgs/{org}/actions/secrets',
  resource: 'actions',
  name: 'listSecretsForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSecretsForOrg',
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

const repoCreateRunnerRegistrationToken: Operation = {
  id: 'repoCreateRunnerRegistrationToken',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/runners/registration-token',
  resource: 'actions',
  name: 'createRunnerRegistrationToken',
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

const repoListActionsSecrets: Operation = {
  id: 'repoListActionsSecrets',
  method: 'GET',
  path: '/repos/{owner}/{repo}/actions/secrets',
  resource: 'actions',
  name: 'listSecrets',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSecrets',
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

const rerunFailedWorkflowRun: Operation = {
  id: 'rerunFailedWorkflowRun',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs',
  resource: 'actions',
  name: 'rerunFailedJobs',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const rerunWorkflowJob: Operation = {
  id: 'rerunWorkflowJob',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun',
  resource: 'actions',
  name: 'rerunJob',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
    { wire: 'job_id', name: 'jobId', location: 'path' },
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

const rerunWorkflowRun: Operation = {
  id: 'rerunWorkflowRun',
  method: 'POST',
  path: '/repos/{owner}/{repo}/actions/runs/{run}/rerun',
  resource: 'actions',
  name: 'rerunRun',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'run', name: 'run', location: 'path' },
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

const updateOrgRunner: Operation = {
  id: 'updateOrgRunner',
  method: 'PATCH',
  path: '/orgs/{org}/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'updateRunnerForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'runner_id', name: 'runnerId', location: 'path' },
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

const updateOrgSecret: Operation = {
  id: 'updateOrgSecret',
  method: 'PUT',
  path: '/orgs/{org}/actions/secrets/{secretname}',
  resource: 'actions',
  name: 'setSecretForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'secretname', name: 'secretname', location: 'path' },
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

const updateOrgVariable: Operation = {
  id: 'updateOrgVariable',
  method: 'PUT',
  path: '/orgs/{org}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'updateVariableForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const updateRepoRunner: Operation = {
  id: 'updateRepoRunner',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'updateRunner',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'runner_id', name: 'runnerId', location: 'path' },
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

const updateRepoSecret: Operation = {
  id: 'updateRepoSecret',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/actions/secrets/{secretname}',
  resource: 'actions',
  name: 'setSecret',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'secretname', name: 'secretname', location: 'path' },
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

const updateRepoVariable: Operation = {
  id: 'updateRepoVariable',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/actions/variables/{variablename}',
  resource: 'actions',
  name: 'updateVariable',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'variablename', name: 'variablename', location: 'path' },
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

const updateUserRunner: Operation = {
  id: 'updateUserRunner',
  method: 'PATCH',
  path: '/user/actions/runners/{runner_id}',
  resource: 'actions',
  name: 'updateRunnerForUser',
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

const updateUserSecret: Operation = {
  id: 'updateUserSecret',
  method: 'PUT',
  path: '/user/actions/secrets/{secretname}',
  resource: 'actions',
  name: 'setSecretForUser',
  params: [{ wire: 'secretname', name: 'secretname', location: 'path' }],
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

const updateUserVariable: Operation = {
  id: 'updateUserVariable',
  method: 'PUT',
  path: '/user/actions/variables/{variablename}',
  resource: 'actions',
  name: 'updateVariableForUser',
  params: [{ wire: 'variablename', name: 'variablename', location: 'path' }],
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

const userCreateRunnerRegistrationToken: Operation = {
  id: 'userCreateRunnerRegistrationToken',
  method: 'POST',
  path: '/user/actions/runners/registration-token',
  resource: 'actions',
  name: 'createRunnerRegistrationTokenForUser',
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

export const OPERATIONS: readonly Operation[] = [
  actionsDisableWorkflow,
  actionsDispatchWorkflow,
  actionsEnableWorkflow,
  actionsGetWorkflow,
  actionsListRepositoryWorkflows,
  actionsListWorkflowRuns,
  approveWorkflowRun,
  cancelWorkflowRun,
  createOrgVariable,
  createRepoVariable,
  createUserVariable,
  deleteActionRun,
  deleteArtifact,
  deleteOrgRunner,
  deleteOrgSecret,
  deleteOrgVariable,
  deleteRepoRunner,
  deleteRepoSecret,
  deleteRepoVariable,
  deleteUserRunner,
  deleteUserSecret,
  deleteUserVariable,
  downloadActionsRunJobLogs,
  downloadArtifact,
  forceCancelWorkflowRun,
  getArtifact,
  getArtifacts,
  getArtifactsOfRun,
  getOrgRunner,
  getOrgRunners,
  getOrgVariable,
  getOrgVariablesList,
  getOrgWorkflowJobs,
  getOrgWorkflowRuns,
  getRepoRunner,
  getRepoRunners,
  getRepoVariable,
  getRepoVariablesList,
  getUserRunner,
  getUserRunners,
  getUserVariable,
  getUserVariablesList,
  getUserWorkflowJobs,
  getUserWorkflowRuns,
  getWorkflowJob,
  getWorkflowRun,
  getWorkflowRunAttempt,
  getWorkflowRunLogs,
  getWorkflowRuns,
  listActionTasks,
  listWorkflowJobs,
  listWorkflowRunAttemptJobs,
  listWorkflowRunJobs,
  orgCreateRunnerRegistrationToken,
  orgListActionsSecrets,
  repoCreateRunnerRegistrationToken,
  repoListActionsSecrets,
  rerunFailedWorkflowRun,
  rerunWorkflowJob,
  rerunWorkflowRun,
  updateOrgRunner,
  updateOrgSecret,
  updateOrgVariable,
  updateRepoRunner,
  updateRepoSecret,
  updateRepoVariable,
  updateUserRunner,
  updateUserSecret,
  updateUserVariable,
  userCreateRunnerRegistrationToken,
];

export class ActionsApi extends Resource {
  /** Disable a workflow (ActionsDisableWorkflow). */
  disableWorkflow(owner: string, repo: string, workflowId: string, options?: RequestOptions): Promise<void> {
    return this.call(actionsDisableWorkflow, undefined, { owner, repo, workflowId }, options);
  }

  /** Start a workflow run by hand (ActionsDispatchWorkflow). */
  dispatchWorkflow(
    owner: string,
    repo: string,
    workflowId: string,
    body?: CreateActionWorkflowDispatch,
    params: { returnRunDetails?: boolean; scopedWorkflowSourceRepoId?: number } = {},
    options?: RequestOptions,
  ): Promise<RunDetails | undefined> {
    return this.call(actionsDispatchWorkflow, body, { owner, repo, workflowId, ...params }, options);
  }

  /** Enable a workflow (ActionsEnableWorkflow). */
  enableWorkflow(owner: string, repo: string, workflowId: string, options?: RequestOptions): Promise<void> {
    return this.call(actionsEnableWorkflow, undefined, { owner, repo, workflowId }, options);
  }

  /** Get a workflow (ActionsGetWorkflow). */
  getWorkflow(owner: string, repo: string, workflowId: string, options?: RequestOptions): Promise<ActionWorkflow> {
    return this.call(actionsGetWorkflow, undefined, { owner, repo, workflowId }, options);
  }

  /** List a repository's workflows (ActionsListRepositoryWorkflows). */
  listWorkflows(owner: string, repo: string, options?: RequestOptions): Promise<ActionWorkflowResponse> {
    return this.call(actionsListRepositoryWorkflows, undefined, { owner, repo }, options);
  }

  /** List one page of a workflow's runs (ActionsListWorkflowRuns). */
  listWorkflowRuns(
    owner: string,
    repo: string,
    workflowId: string,
    params: {
      event?: string;
      branch?: string;
      status?: string;
      actor?: string;
      headSha?: string;
      excludePullRequests?: boolean;
      scopedWorkflowSourceRepoId?: number;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowRunsResponse> {
    return this.call(actionsListWorkflowRuns, undefined, { owner, repo, workflowId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterWorkflowRuns(
    owner: string,
    repo: string,
    workflowId: string,
    params: {
      event?: string;
      branch?: string;
      status?: string;
      actor?: string;
      headSha?: string;
      excludePullRequests?: boolean;
      scopedWorkflowSourceRepoId?: number;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowRun, void, undefined> {
    return this.paginate(actionsListWorkflowRuns, undefined, { owner, repo, workflowId, ...params }, options);
  }

  /** Approve a workflow run that waits for approval (approveWorkflowRun). */
  approveRun(owner: string, repo: string, run: number, options?: RequestOptions): Promise<ActionWorkflowRun> {
    return this.call(approveWorkflowRun, undefined, { owner, repo, run }, options);
  }

  /** Cancel a workflow run (cancelWorkflowRun). */
  cancelRun(owner: string, repo: string, run: number, options?: RequestOptions): Promise<ActionWorkflowRun> {
    return this.call(cancelWorkflowRun, undefined, { owner, repo, run }, options);
  }

  /** Create an organization variable (createOrgVariable). */
  createVariableForOrg(
    org: string,
    variablename: string,
    body?: CreateVariableOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(createOrgVariable, body, { org, variablename }, options);
  }

  /** Create a repository variable (createRepoVariable). */
  createVariable(
    owner: string,
    repo: string,
    variablename: string,
    body?: CreateVariableOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(createRepoVariable, body, { owner, repo, variablename }, options);
  }

  /** Create a variable of your own (createUserVariable). */
  createVariableForUser(variablename: string, body?: CreateVariableOption, options?: RequestOptions): Promise<void> {
    return this.call(createUserVariable, body, { variablename }, options);
  }

  /** Delete a workflow run (deleteActionRun). */
  deleteRun(owner: string, repo: string, run: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteActionRun, undefined, { owner, repo, run }, options);
  }

  /** Delete an artifact (deleteArtifact). */
  deleteArtifact(owner: string, repo: string, artifactId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteArtifact, undefined, { owner, repo, artifactId }, options);
  }

  /** Delete an organization runner (deleteOrgRunner). */
  deleteRunnerForOrg(org: string, runnerId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteOrgRunner, undefined, { org, runnerId }, options);
  }

  /** Delete an organization secret (deleteOrgSecret). */
  deleteSecretForOrg(org: string, secretname: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteOrgSecret, undefined, { org, secretname }, options);
  }

  /** Delete an organization variable (deleteOrgVariable). */
  deleteVariableForOrg(
    org: string,
    variablename: string,
    options?: RequestOptions,
  ): Promise<ActionVariable | undefined> {
    return this.call(deleteOrgVariable, undefined, { org, variablename }, options);
  }

  /** Delete a repository runner (deleteRepoRunner). */
  deleteRunner(owner: string, repo: string, runnerId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteRepoRunner, undefined, { owner, repo, runnerId }, options);
  }

  /** Delete a repository secret (deleteRepoSecret). */
  deleteSecret(owner: string, repo: string, secretname: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteRepoSecret, undefined, { owner, repo, secretname }, options);
  }

  /** Delete a repository variable (deleteRepoVariable). */
  deleteVariable(
    owner: string,
    repo: string,
    variablename: string,
    options?: RequestOptions,
  ): Promise<ActionVariable | undefined> {
    return this.call(deleteRepoVariable, undefined, { owner, repo, variablename }, options);
  }

  /** Delete one of your runners (deleteUserRunner). */
  deleteRunnerForUser(runnerId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteUserRunner, undefined, { runnerId }, options);
  }

  /** Delete one of your secrets (deleteUserSecret). */
  deleteSecretForUser(secretname: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteUserSecret, undefined, { secretname }, options);
  }

  /** Delete one of your variables (deleteUserVariable). */
  deleteVariableForUser(variablename: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteUserVariable, undefined, { variablename }, options);
  }

  /** Download a workflow job's logs (downloadActionsRunJobLogs). */
  downloadJobLogs(owner: string, repo: string, jobId: number, options?: RequestOptions): Promise<void> {
    return this.call(downloadActionsRunJobLogs, undefined, { owner, repo, jobId }, options);
  }

  /** Download an artifact, through a redirect to its file (downloadArtifact). */
  downloadArtifact(owner: string, repo: string, artifactId: string, options?: RequestOptions): Promise<void> {
    return this.call(downloadArtifact, undefined, { owner, repo, artifactId }, options);
  }

  /** Cancel a workflow run at once (forceCancelWorkflowRun). */
  forceCancelRun(owner: string, repo: string, run: number, options?: RequestOptions): Promise<ActionWorkflowRun> {
    return this.call(forceCancelWorkflowRun, undefined, { owner, repo, run }, options);
  }

  /** Get an artifact (getArtifact). */
  getArtifact(owner: string, repo: string, artifactId: string, options?: RequestOptions): Promise<ActionArtifact> {
    return this.call(getArtifact, undefined, { owner, repo, artifactId }, options);
  }

  /** List a repository's artifacts (getArtifacts). */
  listArtifacts(
    owner: string,
    repo: string,
    params: { name?: string } = {},
    options?: RequestOptions,
  ): Promise<ActionArtifactsResponse> {
    return this.call(getArtifacts, undefined, { owner, repo, ...params }, options);
  }

  /** List a workflow run's artifacts (getArtifactsOfRun). */
  listRunArtifacts(
    owner: string,
    repo: string,
    run: number,
    params: { name?: string } = {},
    options?: RequestOptions,
  ): Promise<ActionArtifactsResponse> {
    return this.call(getArtifactsOfRun, undefined, { owner, repo, run, ...params }, options);
  }

  /** Get an organization runner (getOrgRunner). */
  getRunnerForOrg(org: string, runnerId: string, options?: RequestOptions): Promise<ActionRunner> {
    return this.call(getOrgRunner, undefined, { org, runnerId }, options);
  }

  /** List an organization's runners (getOrgRunners). */
  listRunnersForOrg(
    org: string,
    params: { disabled?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ActionRunnersResponse> {
    return this.call(getOrgRunners, undefined, { org, ...params }, options);
  }

  /** Get an organization variable (getOrgVariable). */
  getVariableForOrg(org: string, variablename: string, options?: RequestOptions): Promise<ActionVariable> {
    return this.call(getOrgVariable, undefined, { org, variablename }, options);
  }

  /** List one page of an organization's variables (getOrgVariablesList). */
  listVariablesForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<ActionVariable>> {
    return this.call(getOrgVariablesList, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterVariablesForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionVariable, void, undefined> {
    return this.paginate(getOrgVariablesList, undefined, { org, ...params }, options);
  }

  /** List one page of an organization's workflow jobs (getOrgWorkflowJobs). */
  listJobsForOrg(
    org: string,
    params: { status?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowJobsResponse> {
    return this.call(getOrgWorkflowJobs, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterJobsForOrg(
    org: string,
    params: { status?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowJob, void, undefined> {
    return this.paginate(getOrgWorkflowJobs, undefined, { org, ...params }, options);
  }

  /** List one page of an organization's workflow runs (getOrgWorkflowRuns). */
  listRunsForOrg(
    org: string,
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
    return this.call(getOrgWorkflowRuns, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRunsForOrg(
    org: string,
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
    return this.paginate(getOrgWorkflowRuns, undefined, { org, ...params }, options);
  }

  /** Get a repository runner (getRepoRunner). */
  getRunner(owner: string, repo: string, runnerId: string, options?: RequestOptions): Promise<ActionRunner> {
    return this.call(getRepoRunner, undefined, { owner, repo, runnerId }, options);
  }

  /** List a repository's runners (getRepoRunners). */
  listRunners(
    owner: string,
    repo: string,
    params: { disabled?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ActionRunnersResponse> {
    return this.call(getRepoRunners, undefined, { owner, repo, ...params }, options);
  }

  /** Get a repository variable (getRepoVariable). */
  getVariable(owner: string, repo: string, variablename: string, options?: RequestOptions): Promise<ActionVariable> {
    return this.call(getRepoVariable, undefined, { owner, repo, variablename }, options);
  }

  /** List one page of a repository's variables (getRepoVariablesList). */
  listVariables(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<ActionVariable>> {
    return this.call(getRepoVariablesList, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterVariables(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionVariable, void, undefined> {
    return this.paginate(getRepoVariablesList, undefined, { owner, repo, ...params }, options);
  }

  /** Get one of your runners (getUserRunner). */
  getRunnerForUser(runnerId: string, options?: RequestOptions): Promise<ActionRunner> {
    return this.call(getUserRunner, undefined, { runnerId }, options);
  }

  /** List your own runners (getUserRunners). */
  listRunnersForUser(params: { disabled?: boolean } = {}, options?: RequestOptions): Promise<ActionRunnersResponse> {
    return this.call(getUserRunners, undefined, { ...params }, options);
  }

  /** Get one of your variables (getUserVariable). */
  getVariableForUser(variablename: string, options?: RequestOptions): Promise<ActionVariable> {
    return this.call(getUserVariable, undefined, { variablename }, options);
  }

  /** List one page of your own variables (getUserVariablesList). */
  listVariablesForUser(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<ActionVariable>> {
    return this.call(getUserVariablesList, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterVariablesForUser(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionVariable, void, undefined> {
    return this.paginate(getUserVariablesList, undefined, { ...params }, options);
  }

  /** List one page of your own workflow jobs (getUserWorkflowJobs). */
  listJobsForUser(
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowJobsResponse> {
    return this.call(getUserWorkflowJobs, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterJobsForUser(
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowJob, void, undefined> {
    return this.paginate(getUserWorkflowJobs, undefined, { ...params }, options);
  }

  /** List one page of your own workflow runs (getUserWorkflowRuns). */
  listRunsForUser(
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
    return this.call(getUserWorkflowRuns, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRunsForUser(
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
    return this.paginate(getUserWorkflowRuns, undefined, { ...params }, options);
  }

  /** Get a workflow job (getWorkflowJob). */
  getJob(owner: string, repo: string, jobId: string, options?: RequestOptions): Promise<ActionWorkflowJob> {
    return this.call(getWorkflowJob, undefined, { owner, repo, jobId }, options);
  }

  /** Get a workflow run (GetWorkflowRun). */
  getRun(owner: string, repo: string, run: number, options?: RequestOptions): Promise<ActionWorkflowRun> {
    return this.call(getWorkflowRun, undefined, { owner, repo, run }, options);
  }

  /** Get one attempt of a workflow run (getWorkflowRunAttempt). */
  getRunAttempt(
    owner: string,
    repo: string,
    run: number,
    attempt: number,
    options?: RequestOptions,
  ): Promise<ActionWorkflowRun> {
    return this.call(getWorkflowRunAttempt, undefined, { owner, repo, run, attempt }, options);
  }

  /** Download a workflow run's logs (getWorkflowRunLogs). */
  downloadRunLogs(owner: string, repo: string, run: number, options?: RequestOptions): Promise<void> {
    return this.call(getWorkflowRunLogs, undefined, { owner, repo, run }, options);
  }

  /** List one page of a repository's workflow runs (getWorkflowRuns). */
  listRuns(
    owner: string,
    repo: string,
    params: {
      event?: string;
      branch?: string;
      status?: string;
      actor?: string;
      headSha?: string;
      excludePullRequests?: boolean;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowRunsResponse> {
    return this.call(getWorkflowRuns, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRuns(
    owner: string,
    repo: string,
    params: {
      event?: string;
      branch?: string;
      status?: string;
      actor?: string;
      headSha?: string;
      excludePullRequests?: boolean;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowRun, void, undefined> {
    return this.paginate(getWorkflowRuns, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of a repository's action tasks (ListActionTasks). */
  listTasks(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<ActionTaskResponse> {
    return this.call(listActionTasks, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTasks(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionTask, void, undefined> {
    return this.paginate(listActionTasks, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of a repository's workflow jobs (listWorkflowJobs). */
  listJobs(
    owner: string,
    repo: string,
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowJobsResponse> {
    return this.call(listWorkflowJobs, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterJobs(
    owner: string,
    repo: string,
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowJob, void, undefined> {
    return this.paginate(listWorkflowJobs, undefined, { owner, repo, ...params }, options);
  }

  /** List one page of the jobs in one attempt of a workflow run (listWorkflowRunAttemptJobs). */
  listRunAttemptJobs(
    owner: string,
    repo: string,
    run: number,
    attempt: number,
    params: { status?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowJobsResponse> {
    return this.call(listWorkflowRunAttemptJobs, undefined, { owner, repo, run, attempt, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRunAttemptJobs(
    owner: string,
    repo: string,
    run: number,
    attempt: number,
    params: { status?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowJob, void, undefined> {
    return this.paginate(listWorkflowRunAttemptJobs, undefined, { owner, repo, run, attempt, ...params }, options);
  }

  /** List one page of a workflow run's jobs (listWorkflowRunJobs). */
  listRunJobs(
    owner: string,
    repo: string,
    run: number,
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): Promise<ActionWorkflowJobsResponse> {
    return this.call(listWorkflowRunJobs, undefined, { owner, repo, run, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRunJobs(
    owner: string,
    repo: string,
    run: number,
    params: { status?: string; page?: number; limit?: number; sort?: string; order?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ActionWorkflowJob, void, undefined> {
    return this.paginate(listWorkflowRunJobs, undefined, { owner, repo, run, ...params }, options);
  }

  /** Create a token that registers an organization runner (orgCreateRunnerRegistrationToken). */
  createRunnerRegistrationTokenForOrg(org: string, options?: RequestOptions): Promise<void> {
    return this.call(orgCreateRunnerRegistrationToken, undefined, { org }, options);
  }

  /** List one page of an organization's secrets (orgListActionsSecrets). */
  listSecretsForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Secret>> {
    return this.call(orgListActionsSecrets, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSecretsForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Secret, void, undefined> {
    return this.paginate(orgListActionsSecrets, undefined, { org, ...params }, options);
  }

  /** Create a token that registers a repository runner (repoCreateRunnerRegistrationToken). */
  createRunnerRegistrationToken(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(repoCreateRunnerRegistrationToken, undefined, { owner, repo }, options);
  }

  /** List one page of a repository's secrets (repoListActionsSecrets). */
  listSecrets(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Secret>> {
    return this.call(repoListActionsSecrets, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSecrets(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Secret, void, undefined> {
    return this.paginate(repoListActionsSecrets, undefined, { owner, repo, ...params }, options);
  }

  /** Run a workflow run's failed jobs again (rerunFailedWorkflowRun). */
  rerunFailedJobs(owner: string, repo: string, run: number, options?: RequestOptions): Promise<void> {
    return this.call(rerunFailedWorkflowRun, undefined, { owner, repo, run }, options);
  }

  /** Run a workflow job again (rerunWorkflowJob). */
  rerunJob(
    owner: string,
    repo: string,
    run: number,
    jobId: number,
    options?: RequestOptions,
  ): Promise<ActionWorkflowJob> {
    return this.call(rerunWorkflowJob, undefined, { owner, repo, run, jobId }, options);
  }

  /** Run a workflow run again (rerunWorkflowRun). */
  rerunRun(owner: string, repo: string, run: number, options?: RequestOptions): Promise<ActionWorkflowRun> {
    return this.call(rerunWorkflowRun, undefined, { owner, repo, run }, options);
  }

  /** Change an organization runner (updateOrgRunner). */
  updateRunnerForOrg(
    org: string,
    runnerId: string,
    body?: EditActionRunnerOption,
    options?: RequestOptions,
  ): Promise<ActionRunner> {
    return this.call(updateOrgRunner, body, { org, runnerId }, options);
  }

  /** Create or change an organization secret (updateOrgSecret). */
  setSecretForOrg(
    org: string,
    secretname: string,
    body?: CreateOrUpdateSecretOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateOrgSecret, body, { org, secretname }, options);
  }

  /** Change an organization variable (updateOrgVariable). */
  updateVariableForOrg(
    org: string,
    variablename: string,
    body?: UpdateVariableOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateOrgVariable, body, { org, variablename }, options);
  }

  /** Change a repository runner (updateRepoRunner). */
  updateRunner(
    owner: string,
    repo: string,
    runnerId: string,
    body?: EditActionRunnerOption,
    options?: RequestOptions,
  ): Promise<ActionRunner> {
    return this.call(updateRepoRunner, body, { owner, repo, runnerId }, options);
  }

  /** Create or change a repository secret (updateRepoSecret). */
  setSecret(
    owner: string,
    repo: string,
    secretname: string,
    body?: CreateOrUpdateSecretOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateRepoSecret, body, { owner, repo, secretname }, options);
  }

  /** Change a repository variable (updateRepoVariable). */
  updateVariable(
    owner: string,
    repo: string,
    variablename: string,
    body?: UpdateVariableOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateRepoVariable, body, { owner, repo, variablename }, options);
  }

  /** Change one of your runners (updateUserRunner). */
  updateRunnerForUser(
    runnerId: string,
    body?: EditActionRunnerOption,
    options?: RequestOptions,
  ): Promise<ActionRunner> {
    return this.call(updateUserRunner, body, { runnerId }, options);
  }

  /** Create or change one of your secrets (updateUserSecret). */
  setSecretForUser(secretname: string, body?: CreateOrUpdateSecretOption, options?: RequestOptions): Promise<void> {
    return this.call(updateUserSecret, body, { secretname }, options);
  }

  /** Change one of your variables (updateUserVariable). */
  updateVariableForUser(variablename: string, body?: UpdateVariableOption, options?: RequestOptions): Promise<void> {
    return this.call(updateUserVariable, body, { variablename }, options);
  }

  /** Create a token that registers a runner of your own (userCreateRunnerRegistrationToken). */
  createRunnerRegistrationTokenForUser(options?: RequestOptions): Promise<void> {
    return this.call(userCreateRunnerRegistrationToken, undefined, {}, options);
  }
}
