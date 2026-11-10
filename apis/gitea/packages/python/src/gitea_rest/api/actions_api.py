# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictBool, StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import (
    AsyncResource,
    LinkHeader,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from gitea_rest.models.action_artifact import ActionArtifact
from gitea_rest.models.action_artifacts_response import ActionArtifactsResponse
from gitea_rest.models.action_runner import ActionRunner
from gitea_rest.models.action_runners_response import ActionRunnersResponse
from gitea_rest.models.action_task_response import ActionTaskResponse
from gitea_rest.models.action_variable import ActionVariable
from gitea_rest.models.action_workflow import ActionWorkflow
from gitea_rest.models.action_workflow_job import ActionWorkflowJob
from gitea_rest.models.action_workflow_jobs_response import ActionWorkflowJobsResponse
from gitea_rest.models.action_workflow_response import ActionWorkflowResponse
from gitea_rest.models.action_workflow_run import ActionWorkflowRun
from gitea_rest.models.action_workflow_runs_response import ActionWorkflowRunsResponse
from gitea_rest.models.create_action_workflow_dispatch import CreateActionWorkflowDispatch
from gitea_rest.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from gitea_rest.models.create_variable_option import CreateVariableOption
from gitea_rest.models.edit_action_runner_option import EditActionRunnerOption
from gitea_rest.models.run_details import RunDetails
from gitea_rest.models.secret import Secret
from gitea_rest.models.update_variable_option import UpdateVariableOption

_actions_disable_workflow: Operation[None] = Operation(
    id="ActionsDisableWorkflow",
    method="PUT",
    path="/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable",
    resource="actions",
    name="disable_workflow",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("workflow_id", "workflow_id", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_actions_dispatch_workflow: Operation[RunDetails] = Operation(
    id="ActionsDispatchWorkflow",
    method="POST",
    path="/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
    resource="actions",
    name="dispatch_workflow",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("workflow_id", "workflow_id", "path"),
        Param("return_run_details", "return_run_details", "query"),
        Param("scoped_workflow_source_repo_id", "scoped_workflow_source_repo_id", "query"),
    ),
    response=RunDetails,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_actions_enable_workflow: Operation[None] = Operation(
    id="ActionsEnableWorkflow",
    method="PUT",
    path="/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable",
    resource="actions",
    name="enable_workflow",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("workflow_id", "workflow_id", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_actions_get_workflow: Operation[ActionWorkflow] = Operation(
    id="ActionsGetWorkflow",
    method="GET",
    path="/repos/{owner}/{repo}/actions/workflows/{workflow_id}",
    resource="actions",
    name="get_workflow",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("workflow_id", "workflow_id", "path"),
    ),
    response=ActionWorkflow,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_actions_list_repository_workflows: Operation[ActionWorkflowResponse] = Operation(
    id="ActionsListRepositoryWorkflows",
    method="GET",
    path="/repos/{owner}/{repo}/actions/workflows",
    resource="actions",
    name="list_workflows",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=ActionWorkflowResponse,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_actions_list_workflow_runs: Operation[ActionWorkflowRunsResponse] = Operation(
    id="ActionsListWorkflowRuns",
    method="GET",
    path="/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs",
    resource="actions",
    name="list_workflow_runs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("workflow_id", "workflow_id", "path"),
        Param("event", "event", "query"),
        Param("branch", "branch", "query"),
        Param("status", "status", "query"),
        Param("actor", "actor", "query"),
        Param("head_sha", "head_sha", "query"),
        Param("exclude_pull_requests", "exclude_pull_requests", "query"),
        Param("scoped_workflow_source_repo_id", "scoped_workflow_source_repo_id", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=ActionWorkflowRunsResponse,
    returns_json=True,
    iterator="iter_workflow_runs",
    item=_models.ActionWorkflowRun,
    paging=LinkHeader(
        items="workflow_runs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_approve_workflow_run: Operation[ActionWorkflowRun] = Operation(
    id="approveWorkflowRun",
    method="POST",
    path="/repos/{owner}/{repo}/actions/runs/{run}/approve",
    resource="actions",
    name="approve_run",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=ActionWorkflowRun,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_cancel_workflow_run: Operation[ActionWorkflowRun] = Operation(
    id="cancelWorkflowRun",
    method="POST",
    path="/repos/{owner}/{repo}/actions/runs/{run}/cancel",
    resource="actions",
    name="cancel_run",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=ActionWorkflowRun,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_create_org_variable: Operation[None] = Operation(
    id="createOrgVariable",
    method="POST",
    path="/orgs/{org}/actions/variables/{variablename}",
    resource="actions",
    name="create_variable_for_org",
    params=(
        Param("org", "org", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_create_repo_variable: Operation[None] = Operation(
    id="createRepoVariable",
    method="POST",
    path="/repos/{owner}/{repo}/actions/variables/{variablename}",
    resource="actions",
    name="create_variable",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_create_user_variable: Operation[None] = Operation(
    id="createUserVariable",
    method="POST",
    path="/user/actions/variables/{variablename}",
    resource="actions",
    name="create_variable_for_user",
    params=(Param("variablename", "variablename", "path"),),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_action_run: Operation[None] = Operation(
    id="deleteActionRun",
    method="DELETE",
    path="/repos/{owner}/{repo}/actions/runs/{run}",
    resource="actions",
    name="delete_run",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_artifact: Operation[None] = Operation(
    id="deleteArtifact",
    method="DELETE",
    path="/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
    resource="actions",
    name="delete_artifact",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("artifact_id", "artifact_id", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_org_runner: Operation[None] = Operation(
    id="deleteOrgRunner",
    method="DELETE",
    path="/orgs/{org}/actions/runners/{runner_id}",
    resource="actions",
    name="delete_runner_for_org",
    params=(
        Param("org", "org", "path"),
        Param("runner_id", "runner_id", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_org_secret: Operation[None] = Operation(
    id="deleteOrgSecret",
    method="DELETE",
    path="/orgs/{org}/actions/secrets/{secretname}",
    resource="actions",
    name="delete_secret_for_org",
    params=(
        Param("org", "org", "path"),
        Param("secretname", "secretname", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_org_variable: Operation[ActionVariable] = Operation(
    id="deleteOrgVariable",
    method="DELETE",
    path="/orgs/{org}/actions/variables/{variablename}",
    resource="actions",
    name="delete_variable_for_org",
    params=(
        Param("org", "org", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=ActionVariable,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_repo_runner: Operation[None] = Operation(
    id="deleteRepoRunner",
    method="DELETE",
    path="/repos/{owner}/{repo}/actions/runners/{runner_id}",
    resource="actions",
    name="delete_runner",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("runner_id", "runner_id", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_repo_secret: Operation[None] = Operation(
    id="deleteRepoSecret",
    method="DELETE",
    path="/repos/{owner}/{repo}/actions/secrets/{secretname}",
    resource="actions",
    name="delete_secret",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("secretname", "secretname", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_repo_variable: Operation[ActionVariable] = Operation(
    id="deleteRepoVariable",
    method="DELETE",
    path="/repos/{owner}/{repo}/actions/variables/{variablename}",
    resource="actions",
    name="delete_variable",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=ActionVariable,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_user_runner: Operation[None] = Operation(
    id="deleteUserRunner",
    method="DELETE",
    path="/user/actions/runners/{runner_id}",
    resource="actions",
    name="delete_runner_for_user",
    params=(Param("runner_id", "runner_id", "path"),),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_user_secret: Operation[None] = Operation(
    id="deleteUserSecret",
    method="DELETE",
    path="/user/actions/secrets/{secretname}",
    resource="actions",
    name="delete_secret_for_user",
    params=(Param("secretname", "secretname", "path"),),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_delete_user_variable: Operation[None] = Operation(
    id="deleteUserVariable",
    method="DELETE",
    path="/user/actions/variables/{variablename}",
    resource="actions",
    name="delete_variable_for_user",
    params=(Param("variablename", "variablename", "path"),),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_download_actions_run_job_logs: Operation[None] = Operation(
    id="downloadActionsRunJobLogs",
    method="GET",
    path="/repos/{owner}/{repo}/actions/jobs/{job_id}/logs",
    resource="actions",
    name="download_job_logs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("job_id", "job_id", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_download_artifact: Operation[None] = Operation(
    id="downloadArtifact",
    method="GET",
    path="/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip",
    resource="actions",
    name="download_artifact",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("artifact_id", "artifact_id", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_force_cancel_workflow_run: Operation[ActionWorkflowRun] = Operation(
    id="forceCancelWorkflowRun",
    method="POST",
    path="/repos/{owner}/{repo}/actions/runs/{run}/force-cancel",
    resource="actions",
    name="force_cancel_run",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=ActionWorkflowRun,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_artifact: Operation[ActionArtifact] = Operation(
    id="getArtifact",
    method="GET",
    path="/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
    resource="actions",
    name="get_artifact",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("artifact_id", "artifact_id", "path"),
    ),
    response=ActionArtifact,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_artifacts: Operation[ActionArtifactsResponse] = Operation(
    id="getArtifacts",
    method="GET",
    path="/repos/{owner}/{repo}/actions/artifacts",
    resource="actions",
    name="list_artifacts",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("name", "name", "query"),
    ),
    response=ActionArtifactsResponse,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_artifacts_of_run: Operation[ActionArtifactsResponse] = Operation(
    id="getArtifactsOfRun",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runs/{run}/artifacts",
    resource="actions",
    name="list_run_artifacts",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
        Param("name", "name", "query"),
    ),
    response=ActionArtifactsResponse,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_org_runner: Operation[ActionRunner] = Operation(
    id="getOrgRunner",
    method="GET",
    path="/orgs/{org}/actions/runners/{runner_id}",
    resource="actions",
    name="get_runner_for_org",
    params=(
        Param("org", "org", "path"),
        Param("runner_id", "runner_id", "path"),
    ),
    response=ActionRunner,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_org_runners: Operation[ActionRunnersResponse] = Operation(
    id="getOrgRunners",
    method="GET",
    path="/orgs/{org}/actions/runners",
    resource="actions",
    name="list_runners_for_org",
    params=(
        Param("org", "org", "path"),
        Param("disabled", "disabled", "query"),
    ),
    response=ActionRunnersResponse,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_org_variable: Operation[ActionVariable] = Operation(
    id="getOrgVariable",
    method="GET",
    path="/orgs/{org}/actions/variables/{variablename}",
    resource="actions",
    name="get_variable_for_org",
    params=(
        Param("org", "org", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=ActionVariable,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_org_variables_list: Operation[List[ActionVariable]] = Operation(
    id="getOrgVariablesList",
    method="GET",
    path="/orgs/{org}/actions/variables",
    resource="actions",
    name="list_variables_for_org",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[ActionVariable],
    returns_json=True,
    iterator="iter_variables_for_org",
    item=_models.ActionVariable,
    paging=LinkHeader(
        items="$",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_org_workflow_jobs: Operation[ActionWorkflowJobsResponse] = Operation(
    id="getOrgWorkflowJobs",
    method="GET",
    path="/orgs/{org}/actions/jobs",
    resource="actions",
    name="list_jobs_for_org",
    params=(
        Param("org", "org", "path"),
        Param("status", "status", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=ActionWorkflowJobsResponse,
    returns_json=True,
    iterator="iter_jobs_for_org",
    item=_models.ActionWorkflowJob,
    paging=LinkHeader(
        items="jobs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_org_workflow_runs: Operation[ActionWorkflowRunsResponse] = Operation(
    id="getOrgWorkflowRuns",
    method="GET",
    path="/orgs/{org}/actions/runs",
    resource="actions",
    name="list_runs_for_org",
    params=(
        Param("org", "org", "path"),
        Param("event", "event", "query"),
        Param("branch", "branch", "query"),
        Param("status", "status", "query"),
        Param("actor", "actor", "query"),
        Param("head_sha", "head_sha", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=ActionWorkflowRunsResponse,
    returns_json=True,
    iterator="iter_runs_for_org",
    item=_models.ActionWorkflowRun,
    paging=LinkHeader(
        items="workflow_runs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_repo_runner: Operation[ActionRunner] = Operation(
    id="getRepoRunner",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runners/{runner_id}",
    resource="actions",
    name="get_runner",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("runner_id", "runner_id", "path"),
    ),
    response=ActionRunner,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_repo_runners: Operation[ActionRunnersResponse] = Operation(
    id="getRepoRunners",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runners",
    resource="actions",
    name="list_runners",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("disabled", "disabled", "query"),
    ),
    response=ActionRunnersResponse,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_repo_variable: Operation[ActionVariable] = Operation(
    id="getRepoVariable",
    method="GET",
    path="/repos/{owner}/{repo}/actions/variables/{variablename}",
    resource="actions",
    name="get_variable",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=ActionVariable,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_repo_variables_list: Operation[List[ActionVariable]] = Operation(
    id="getRepoVariablesList",
    method="GET",
    path="/repos/{owner}/{repo}/actions/variables",
    resource="actions",
    name="list_variables",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[ActionVariable],
    returns_json=True,
    iterator="iter_variables",
    item=_models.ActionVariable,
    paging=LinkHeader(
        items="$",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_user_runner: Operation[ActionRunner] = Operation(
    id="getUserRunner",
    method="GET",
    path="/user/actions/runners/{runner_id}",
    resource="actions",
    name="get_runner_for_user",
    params=(Param("runner_id", "runner_id", "path"),),
    response=ActionRunner,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_user_runners: Operation[ActionRunnersResponse] = Operation(
    id="getUserRunners",
    method="GET",
    path="/user/actions/runners",
    resource="actions",
    name="list_runners_for_user",
    params=(Param("disabled", "disabled", "query"),),
    response=ActionRunnersResponse,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_user_variable: Operation[ActionVariable] = Operation(
    id="getUserVariable",
    method="GET",
    path="/user/actions/variables/{variablename}",
    resource="actions",
    name="get_variable_for_user",
    params=(Param("variablename", "variablename", "path"),),
    response=ActionVariable,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_user_variables_list: Operation[List[ActionVariable]] = Operation(
    id="getUserVariablesList",
    method="GET",
    path="/user/actions/variables",
    resource="actions",
    name="list_variables_for_user",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[ActionVariable],
    returns_json=True,
    iterator="iter_variables_for_user",
    item=_models.ActionVariable,
    paging=LinkHeader(
        items="$",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_user_workflow_jobs: Operation[ActionWorkflowJobsResponse] = Operation(
    id="getUserWorkflowJobs",
    method="GET",
    path="/user/actions/jobs",
    resource="actions",
    name="list_jobs_for_user",
    params=(
        Param("status", "status", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=ActionWorkflowJobsResponse,
    returns_json=True,
    iterator="iter_jobs_for_user",
    item=_models.ActionWorkflowJob,
    paging=LinkHeader(
        items="jobs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_user_workflow_runs: Operation[ActionWorkflowRunsResponse] = Operation(
    id="getUserWorkflowRuns",
    method="GET",
    path="/user/actions/runs",
    resource="actions",
    name="list_runs_for_user",
    params=(
        Param("event", "event", "query"),
        Param("branch", "branch", "query"),
        Param("status", "status", "query"),
        Param("actor", "actor", "query"),
        Param("head_sha", "head_sha", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=ActionWorkflowRunsResponse,
    returns_json=True,
    iterator="iter_runs_for_user",
    item=_models.ActionWorkflowRun,
    paging=LinkHeader(
        items="workflow_runs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_workflow_job: Operation[ActionWorkflowJob] = Operation(
    id="getWorkflowJob",
    method="GET",
    path="/repos/{owner}/{repo}/actions/jobs/{job_id}",
    resource="actions",
    name="get_job",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("job_id", "job_id", "path"),
    ),
    response=ActionWorkflowJob,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_workflow_run: Operation[ActionWorkflowRun] = Operation(
    id="GetWorkflowRun",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runs/{run}",
    resource="actions",
    name="get_run",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=ActionWorkflowRun,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_workflow_run_attempt: Operation[ActionWorkflowRun] = Operation(
    id="getWorkflowRunAttempt",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}",
    resource="actions",
    name="get_run_attempt",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
        Param("attempt", "attempt", "path"),
    ),
    response=ActionWorkflowRun,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_workflow_run_logs: Operation[None] = Operation(
    id="getWorkflowRunLogs",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runs/{run}/logs",
    resource="actions",
    name="download_run_logs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_get_workflow_runs: Operation[ActionWorkflowRunsResponse] = Operation(
    id="getWorkflowRuns",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runs",
    resource="actions",
    name="list_runs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("event", "event", "query"),
        Param("branch", "branch", "query"),
        Param("status", "status", "query"),
        Param("actor", "actor", "query"),
        Param("head_sha", "head_sha", "query"),
        Param("exclude_pull_requests", "exclude_pull_requests", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=ActionWorkflowRunsResponse,
    returns_json=True,
    iterator="iter_runs",
    item=_models.ActionWorkflowRun,
    paging=LinkHeader(
        items="workflow_runs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_list_action_tasks: Operation[ActionTaskResponse] = Operation(
    id="ListActionTasks",
    method="GET",
    path="/repos/{owner}/{repo}/actions/tasks",
    resource="actions",
    name="list_tasks",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=ActionTaskResponse,
    returns_json=True,
    iterator="iter_tasks",
    item=_models.ActionTask,
    paging=LinkHeader(
        items="workflow_runs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_list_workflow_jobs: Operation[ActionWorkflowJobsResponse] = Operation(
    id="listWorkflowJobs",
    method="GET",
    path="/repos/{owner}/{repo}/actions/jobs",
    resource="actions",
    name="list_jobs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("status", "status", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=ActionWorkflowJobsResponse,
    returns_json=True,
    iterator="iter_jobs",
    item=_models.ActionWorkflowJob,
    paging=LinkHeader(
        items="jobs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_list_workflow_run_attempt_jobs: Operation[ActionWorkflowJobsResponse] = Operation(
    id="listWorkflowRunAttemptJobs",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs",
    resource="actions",
    name="list_run_attempt_jobs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
        Param("attempt", "attempt", "path"),
        Param("status", "status", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=ActionWorkflowJobsResponse,
    returns_json=True,
    iterator="iter_run_attempt_jobs",
    item=_models.ActionWorkflowJob,
    paging=LinkHeader(
        items="jobs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_list_workflow_run_jobs: Operation[ActionWorkflowJobsResponse] = Operation(
    id="listWorkflowRunJobs",
    method="GET",
    path="/repos/{owner}/{repo}/actions/runs/{run}/jobs",
    resource="actions",
    name="list_run_jobs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
        Param("status", "status", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=ActionWorkflowJobsResponse,
    returns_json=True,
    iterator="iter_run_jobs",
    item=_models.ActionWorkflowJob,
    paging=LinkHeader(
        items="jobs",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_org_create_runner_registration_token: Operation[None] = Operation(
    id="orgCreateRunnerRegistrationToken",
    method="POST",
    path="/orgs/{org}/actions/runners/registration-token",
    resource="actions",
    name="create_runner_registration_token_for_org",
    params=(Param("org", "org", "path"),),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_org_list_actions_secrets: Operation[List[Secret]] = Operation(
    id="orgListActionsSecrets",
    method="GET",
    path="/orgs/{org}/actions/secrets",
    resource="actions",
    name="list_secrets_for_org",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Secret],
    returns_json=True,
    iterator="iter_secrets_for_org",
    item=_models.Secret,
    paging=LinkHeader(
        items="$",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_repo_create_runner_registration_token: Operation[None] = Operation(
    id="repoCreateRunnerRegistrationToken",
    method="POST",
    path="/repos/{owner}/{repo}/actions/runners/registration-token",
    resource="actions",
    name="create_runner_registration_token",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_repo_list_actions_secrets: Operation[List[Secret]] = Operation(
    id="repoListActionsSecrets",
    method="GET",
    path="/repos/{owner}/{repo}/actions/secrets",
    resource="actions",
    name="list_secrets",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Secret],
    returns_json=True,
    iterator="iter_secrets",
    item=_models.Secret,
    paging=LinkHeader(
        items="$",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_rerun_failed_workflow_run: Operation[None] = Operation(
    id="rerunFailedWorkflowRun",
    method="POST",
    path="/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs",
    resource="actions",
    name="rerun_failed_jobs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_rerun_workflow_job: Operation[ActionWorkflowJob] = Operation(
    id="rerunWorkflowJob",
    method="POST",
    path="/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun",
    resource="actions",
    name="rerun_job",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
        Param("job_id", "job_id", "path"),
    ),
    response=ActionWorkflowJob,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_rerun_workflow_run: Operation[ActionWorkflowRun] = Operation(
    id="rerunWorkflowRun",
    method="POST",
    path="/repos/{owner}/{repo}/actions/runs/{run}/rerun",
    resource="actions",
    name="rerun_run",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("run", "run", "path"),
    ),
    response=ActionWorkflowRun,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_org_runner: Operation[ActionRunner] = Operation(
    id="updateOrgRunner",
    method="PATCH",
    path="/orgs/{org}/actions/runners/{runner_id}",
    resource="actions",
    name="update_runner_for_org",
    params=(
        Param("org", "org", "path"),
        Param("runner_id", "runner_id", "path"),
    ),
    response=ActionRunner,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_org_secret: Operation[None] = Operation(
    id="updateOrgSecret",
    method="PUT",
    path="/orgs/{org}/actions/secrets/{secretname}",
    resource="actions",
    name="set_secret_for_org",
    params=(
        Param("org", "org", "path"),
        Param("secretname", "secretname", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_org_variable: Operation[None] = Operation(
    id="updateOrgVariable",
    method="PUT",
    path="/orgs/{org}/actions/variables/{variablename}",
    resource="actions",
    name="update_variable_for_org",
    params=(
        Param("org", "org", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_repo_runner: Operation[ActionRunner] = Operation(
    id="updateRepoRunner",
    method="PATCH",
    path="/repos/{owner}/{repo}/actions/runners/{runner_id}",
    resource="actions",
    name="update_runner",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("runner_id", "runner_id", "path"),
    ),
    response=ActionRunner,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_repo_secret: Operation[None] = Operation(
    id="updateRepoSecret",
    method="PUT",
    path="/repos/{owner}/{repo}/actions/secrets/{secretname}",
    resource="actions",
    name="set_secret",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("secretname", "secretname", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_repo_variable: Operation[None] = Operation(
    id="updateRepoVariable",
    method="PUT",
    path="/repos/{owner}/{repo}/actions/variables/{variablename}",
    resource="actions",
    name="update_variable",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("variablename", "variablename", "path"),
    ),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_user_runner: Operation[ActionRunner] = Operation(
    id="updateUserRunner",
    method="PATCH",
    path="/user/actions/runners/{runner_id}",
    resource="actions",
    name="update_runner_for_user",
    params=(Param("runner_id", "runner_id", "path"),),
    response=ActionRunner,
    returns_json=True,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_user_secret: Operation[None] = Operation(
    id="updateUserSecret",
    method="PUT",
    path="/user/actions/secrets/{secretname}",
    resource="actions",
    name="set_secret_for_user",
    params=(Param("secretname", "secretname", "path"),),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_update_user_variable: Operation[None] = Operation(
    id="updateUserVariable",
    method="PUT",
    path="/user/actions/variables/{variablename}",
    resource="actions",
    name="update_variable_for_user",
    params=(Param("variablename", "variablename", "path"),),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)
_user_create_runner_registration_token: Operation[None] = Operation(
    id="userCreateRunnerRegistrationToken",
    method="POST",
    path="/user/actions/runners/registration-token",
    resource="actions",
    name="create_runner_registration_token_for_user",
    params=(),
    response=None,
    security=(
        (Scheme("AuthorizationHeaderToken", ()),),
        (
            Scheme("AuthorizationHeaderToken", ()),
            Scheme("SudoHeader", ()),
        ),
        (Scheme("BasicAuth", ()),),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("SudoHeader", ()),
        ),
        (
            Scheme("BasicAuth", ()),
            Scheme("TOTPHeader", ()),
            Scheme("SudoHeader", ()),
        ),
    ),
)

OPERATIONS = (
    _actions_disable_workflow,
    _actions_dispatch_workflow,
    _actions_enable_workflow,
    _actions_get_workflow,
    _actions_list_repository_workflows,
    _actions_list_workflow_runs,
    _approve_workflow_run,
    _cancel_workflow_run,
    _create_org_variable,
    _create_repo_variable,
    _create_user_variable,
    _delete_action_run,
    _delete_artifact,
    _delete_org_runner,
    _delete_org_secret,
    _delete_org_variable,
    _delete_repo_runner,
    _delete_repo_secret,
    _delete_repo_variable,
    _delete_user_runner,
    _delete_user_secret,
    _delete_user_variable,
    _download_actions_run_job_logs,
    _download_artifact,
    _force_cancel_workflow_run,
    _get_artifact,
    _get_artifacts,
    _get_artifacts_of_run,
    _get_org_runner,
    _get_org_runners,
    _get_org_variable,
    _get_org_variables_list,
    _get_org_workflow_jobs,
    _get_org_workflow_runs,
    _get_repo_runner,
    _get_repo_runners,
    _get_repo_variable,
    _get_repo_variables_list,
    _get_user_runner,
    _get_user_runners,
    _get_user_variable,
    _get_user_variables_list,
    _get_user_workflow_jobs,
    _get_user_workflow_runs,
    _get_workflow_job,
    _get_workflow_run,
    _get_workflow_run_attempt,
    _get_workflow_run_logs,
    _get_workflow_runs,
    _list_action_tasks,
    _list_workflow_jobs,
    _list_workflow_run_attempt_jobs,
    _list_workflow_run_jobs,
    _org_create_runner_registration_token,
    _org_list_actions_secrets,
    _repo_create_runner_registration_token,
    _repo_list_actions_secrets,
    _rerun_failed_workflow_run,
    _rerun_workflow_job,
    _rerun_workflow_run,
    _update_org_runner,
    _update_org_secret,
    _update_org_variable,
    _update_repo_runner,
    _update_repo_secret,
    _update_repo_variable,
    _update_user_runner,
    _update_user_secret,
    _update_user_variable,
    _user_create_runner_registration_token,
)


class ActionsApi(Resource):
    @checked
    def disable_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
    ) -> None:
        """Disable a workflow (ActionsDisableWorkflow)."""
        return self._call(
            _actions_disable_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
        )

    @checked
    def dispatch_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
        body: Optional[Union[CreateActionWorkflowDispatch, Mapping[str, Any]]] = None,
        *,
        return_run_details: Optional[StrictBool] = None,
        scoped_workflow_source_repo_id: Optional[StrictInt] = None,
    ) -> RunDetails:
        """Start a workflow run by hand (ActionsDispatchWorkflow)."""
        return self._call(
            _actions_dispatch_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            _body=body,
            return_run_details=return_run_details,
            scoped_workflow_source_repo_id=scoped_workflow_source_repo_id,
        )

    @checked
    def enable_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
    ) -> None:
        """Enable a workflow (ActionsEnableWorkflow)."""
        return self._call(
            _actions_enable_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
        )

    @checked
    def get_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
    ) -> ActionWorkflow:
        """Get a workflow (ActionsGetWorkflow)."""
        return self._call(
            _actions_get_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
        )

    @checked
    def list_workflows(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> ActionWorkflowResponse:
        """List a repository's workflows (ActionsListRepositoryWorkflows)."""
        return self._call(
            _actions_list_repository_workflows,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_workflow_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        scoped_workflow_source_repo_id: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of a workflow's runs (ActionsListWorkflowRuns)."""
        return self._call(
            _actions_list_workflow_runs,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            scoped_workflow_source_repo_id=scoped_workflow_source_repo_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_workflow_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        scoped_workflow_source_repo_id: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _actions_list_workflow_runs,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            scoped_workflow_source_repo_id=scoped_workflow_source_repo_id,
            page=page,
            limit=limit,
        )

    @checked
    def approve_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Approve a workflow run that waits for approval (approveWorkflowRun)."""
        return self._call(
            _approve_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def cancel_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Cancel a workflow run (cancelWorkflowRun)."""
        return self._call(
            _cancel_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def create_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[CreateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create an organization variable (createOrgVariable)."""
        return self._call(
            _create_org_variable,
            org=org,
            variablename=variablename,
            _body=body,
        )

    @checked
    def create_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[CreateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create a repository variable (createRepoVariable)."""
        return self._call(
            _create_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
            _body=body,
        )

    @checked
    def create_variable_for_user(
        self,
        variablename: StrictStr,
        body: Optional[Union[CreateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create a variable of your own (createUserVariable)."""
        return self._call(
            _create_user_variable,
            variablename=variablename,
            _body=body,
        )

    @checked
    def delete_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> None:
        """Delete a workflow run (deleteActionRun)."""
        return self._call(
            _delete_action_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def delete_artifact(
        self,
        owner: StrictStr,
        repo: StrictStr,
        artifact_id: StrictStr,
    ) -> None:
        """Delete an artifact (deleteArtifact)."""
        return self._call(
            _delete_artifact,
            owner=owner,
            repo=repo,
            artifact_id=artifact_id,
        )

    @checked
    def delete_runner_for_org(
        self,
        org: StrictStr,
        runner_id: StrictStr,
    ) -> None:
        """Delete an organization runner (deleteOrgRunner)."""
        return self._call(
            _delete_org_runner,
            org=org,
            runner_id=runner_id,
        )

    @checked
    def delete_secret_for_org(
        self,
        org: StrictStr,
        secretname: StrictStr,
    ) -> None:
        """Delete an organization secret (deleteOrgSecret)."""
        return self._call(
            _delete_org_secret,
            org=org,
            secretname=secretname,
        )

    @checked
    def delete_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Delete an organization variable (deleteOrgVariable)."""
        return self._call(
            _delete_org_variable,
            org=org,
            variablename=variablename,
        )

    @checked
    def delete_runner(
        self,
        owner: StrictStr,
        repo: StrictStr,
        runner_id: StrictStr,
    ) -> None:
        """Delete a repository runner (deleteRepoRunner)."""
        return self._call(
            _delete_repo_runner,
            owner=owner,
            repo=repo,
            runner_id=runner_id,
        )

    @checked
    def delete_secret(
        self,
        owner: StrictStr,
        repo: StrictStr,
        secretname: StrictStr,
    ) -> None:
        """Delete a repository secret (deleteRepoSecret)."""
        return self._call(
            _delete_repo_secret,
            owner=owner,
            repo=repo,
            secretname=secretname,
        )

    @checked
    def delete_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Delete a repository variable (deleteRepoVariable)."""
        return self._call(
            _delete_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
        )

    @checked
    def delete_runner_for_user(
        self,
        runner_id: StrictStr,
    ) -> None:
        """Delete one of your runners (deleteUserRunner)."""
        return self._call(
            _delete_user_runner,
            runner_id=runner_id,
        )

    @checked
    def delete_secret_for_user(
        self,
        secretname: StrictStr,
    ) -> None:
        """Delete one of your secrets (deleteUserSecret)."""
        return self._call(
            _delete_user_secret,
            secretname=secretname,
        )

    @checked
    def delete_variable_for_user(
        self,
        variablename: StrictStr,
    ) -> None:
        """Delete one of your variables (deleteUserVariable)."""
        return self._call(
            _delete_user_variable,
            variablename=variablename,
        )

    @checked
    def download_job_logs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        job_id: StrictInt,
    ) -> None:
        """Download a workflow job's logs (downloadActionsRunJobLogs)."""
        return self._call(
            _download_actions_run_job_logs,
            owner=owner,
            repo=repo,
            job_id=job_id,
        )

    @checked
    def download_artifact(
        self,
        owner: StrictStr,
        repo: StrictStr,
        artifact_id: StrictStr,
    ) -> None:
        """Download an artifact, through a redirect to its file (downloadArtifact)."""
        return self._call(
            _download_artifact,
            owner=owner,
            repo=repo,
            artifact_id=artifact_id,
        )

    @checked
    def force_cancel_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Cancel a workflow run at once (forceCancelWorkflowRun)."""
        return self._call(
            _force_cancel_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def get_artifact(
        self,
        owner: StrictStr,
        repo: StrictStr,
        artifact_id: StrictStr,
    ) -> ActionArtifact:
        """Get an artifact (getArtifact)."""
        return self._call(
            _get_artifact,
            owner=owner,
            repo=repo,
            artifact_id=artifact_id,
        )

    @checked
    def list_artifacts(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        name: Optional[StrictStr] = None,
    ) -> ActionArtifactsResponse:
        """List a repository's artifacts (getArtifacts)."""
        return self._call(
            _get_artifacts,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    def list_run_artifacts(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        *,
        name: Optional[StrictStr] = None,
    ) -> ActionArtifactsResponse:
        """List a workflow run's artifacts (getArtifactsOfRun)."""
        return self._call(
            _get_artifacts_of_run,
            owner=owner,
            repo=repo,
            run=run,
            name=name,
        )

    @checked
    def get_runner_for_org(
        self,
        org: StrictStr,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get an organization runner (getOrgRunner)."""
        return self._call(
            _get_org_runner,
            org=org,
            runner_id=runner_id,
        )

    @checked
    def list_runners_for_org(
        self,
        org: StrictStr,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List an organization's runners (getOrgRunners)."""
        return self._call(
            _get_org_runners,
            org=org,
            disabled=disabled,
        )

    @checked
    def get_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Get an organization variable (getOrgVariable)."""
        return self._call(
            _get_org_variable,
            org=org,
            variablename=variablename,
        )

    @checked
    def list_variables_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ActionVariable]:
        """List one page of an organization's variables (getOrgVariablesList)."""
        return self._call(
            _get_org_variables_list,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_variables_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionVariable]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_org_variables_list,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def list_jobs_for_org(
        self,
        org: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of an organization's workflow jobs (getOrgWorkflowJobs)."""
        return self._call(
            _get_org_workflow_jobs,
            org=org,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    def iter_jobs_for_org(
        self,
        org: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_org_workflow_jobs,
            org=org,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    def list_runs_for_org(
        self,
        org: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of an organization's workflow runs (getOrgWorkflowRuns)."""
        return self._call(
            _get_org_workflow_runs,
            org=org,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs_for_org(
        self,
        org: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_org_workflow_runs,
            org=org,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def get_runner(
        self,
        owner: StrictStr,
        repo: StrictStr,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get a repository runner (getRepoRunner)."""
        return self._call(
            _get_repo_runner,
            owner=owner,
            repo=repo,
            runner_id=runner_id,
        )

    @checked
    def list_runners(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List a repository's runners (getRepoRunners)."""
        return self._call(
            _get_repo_runners,
            owner=owner,
            repo=repo,
            disabled=disabled,
        )

    @checked
    def get_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Get a repository variable (getRepoVariable)."""
        return self._call(
            _get_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
        )

    @checked
    def list_variables(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ActionVariable]:
        """List one page of a repository's variables (getRepoVariablesList)."""
        return self._call(
            _get_repo_variables_list,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_variables(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionVariable]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_repo_variables_list,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def get_runner_for_user(
        self,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get one of your runners (getUserRunner)."""
        return self._call(
            _get_user_runner,
            runner_id=runner_id,
        )

    @checked
    def list_runners_for_user(
        self,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List your own runners (getUserRunners)."""
        return self._call(
            _get_user_runners,
            disabled=disabled,
        )

    @checked
    def get_variable_for_user(
        self,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Get one of your variables (getUserVariable)."""
        return self._call(
            _get_user_variable,
            variablename=variablename,
        )

    @checked
    def list_variables_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ActionVariable]:
        """List one page of your own variables (getUserVariablesList)."""
        return self._call(
            _get_user_variables_list,
            page=page,
            limit=limit,
        )

    @checked
    def iter_variables_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionVariable]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_variables_list,
            page=page,
            limit=limit,
        )

    @checked
    def list_jobs_for_user(
        self,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of your own workflow jobs (getUserWorkflowJobs)."""
        return self._call(
            _get_user_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_jobs_for_user(
        self,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def list_runs_for_user(
        self,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of your own workflow runs (getUserWorkflowRuns)."""
        return self._call(
            _get_user_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs_for_user(
        self,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def get_job(
        self,
        owner: StrictStr,
        repo: StrictStr,
        job_id: StrictStr,
    ) -> ActionWorkflowJob:
        """Get a workflow job (getWorkflowJob)."""
        return self._call(
            _get_workflow_job,
            owner=owner,
            repo=repo,
            job_id=job_id,
        )

    @checked
    def get_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Get a workflow run (GetWorkflowRun)."""
        return self._call(
            _get_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def get_run_attempt(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        attempt: StrictInt,
    ) -> ActionWorkflowRun:
        """Get one attempt of a workflow run (getWorkflowRunAttempt)."""
        return self._call(
            _get_workflow_run_attempt,
            owner=owner,
            repo=repo,
            run=run,
            attempt=attempt,
        )

    @checked
    def download_run_logs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> None:
        """Download a workflow run's logs (getWorkflowRunLogs)."""
        return self._call(
            _get_workflow_run_logs,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def list_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of a repository's workflow runs (getWorkflowRuns)."""
        return self._call(
            _get_workflow_runs,
            owner=owner,
            repo=repo,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_workflow_runs,
            owner=owner,
            repo=repo,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            page=page,
            limit=limit,
        )

    @checked
    def list_tasks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionTaskResponse:
        """List one page of a repository's action tasks (ListActionTasks)."""
        return self._call(
            _list_action_tasks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tasks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_action_tasks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def list_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of a repository's workflow jobs (listWorkflowJobs)."""
        return self._call(
            _list_workflow_jobs,
            owner=owner,
            repo=repo,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_workflow_jobs,
            owner=owner,
            repo=repo,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def list_run_attempt_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        attempt: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of the jobs in one attempt of a workflow run (listWorkflowRunAttemptJobs)."""
        return self._call(
            _list_workflow_run_attempt_jobs,
            owner=owner,
            repo=repo,
            run=run,
            attempt=attempt,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    def iter_run_attempt_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        attempt: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_workflow_run_attempt_jobs,
            owner=owner,
            repo=repo,
            run=run,
            attempt=attempt,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    def list_run_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of a workflow run's jobs (listWorkflowRunJobs)."""
        return self._call(
            _list_workflow_run_jobs,
            owner=owner,
            repo=repo,
            run=run,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_run_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_workflow_run_jobs,
            owner=owner,
            repo=repo,
            run=run,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def create_runner_registration_token_for_org(
        self,
        org: StrictStr,
    ) -> None:
        """Create a token that registers an organization runner (orgCreateRunnerRegistrationToken)."""
        return self._call(
            _org_create_runner_registration_token,
            org=org,
        )

    @checked
    def list_secrets_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Secret]:
        """List one page of an organization's secrets (orgListActionsSecrets)."""
        return self._call(
            _org_list_actions_secrets,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_secrets_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Secret]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_actions_secrets,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def create_runner_registration_token(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Create a token that registers a repository runner (repoCreateRunnerRegistrationToken)."""
        return self._call(
            _repo_create_runner_registration_token,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_secrets(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Secret]:
        """List one page of a repository's secrets (repoListActionsSecrets)."""
        return self._call(
            _repo_list_actions_secrets,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_secrets(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Secret]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_actions_secrets,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def rerun_failed_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> None:
        """Run a workflow run's failed jobs again (rerunFailedWorkflowRun)."""
        return self._call(
            _rerun_failed_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def rerun_job(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        job_id: StrictInt,
    ) -> ActionWorkflowJob:
        """Run a workflow job again (rerunWorkflowJob)."""
        return self._call(
            _rerun_workflow_job,
            owner=owner,
            repo=repo,
            run=run,
            job_id=job_id,
        )

    @checked
    def rerun_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Run a workflow run again (rerunWorkflowRun)."""
        return self._call(
            _rerun_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    def update_runner_for_org(
        self,
        org: StrictStr,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change an organization runner (updateOrgRunner)."""
        return self._call(
            _update_org_runner,
            org=org,
            runner_id=runner_id,
            _body=body,
        )

    @checked
    def set_secret_for_org(
        self,
        org: StrictStr,
        secretname: StrictStr,
        body: Optional[Union[CreateOrUpdateSecretOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create or change an organization secret (updateOrgSecret)."""
        return self._call(
            _update_org_secret,
            org=org,
            secretname=secretname,
            _body=body,
        )

    @checked
    def update_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[UpdateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Change an organization variable (updateOrgVariable)."""
        return self._call(
            _update_org_variable,
            org=org,
            variablename=variablename,
            _body=body,
        )

    @checked
    def update_runner(
        self,
        owner: StrictStr,
        repo: StrictStr,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change a repository runner (updateRepoRunner)."""
        return self._call(
            _update_repo_runner,
            owner=owner,
            repo=repo,
            runner_id=runner_id,
            _body=body,
        )

    @checked
    def set_secret(
        self,
        owner: StrictStr,
        repo: StrictStr,
        secretname: StrictStr,
        body: Optional[Union[CreateOrUpdateSecretOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create or change a repository secret (updateRepoSecret)."""
        return self._call(
            _update_repo_secret,
            owner=owner,
            repo=repo,
            secretname=secretname,
            _body=body,
        )

    @checked
    def update_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[UpdateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Change a repository variable (updateRepoVariable)."""
        return self._call(
            _update_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
            _body=body,
        )

    @checked
    def update_runner_for_user(
        self,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change one of your runners (updateUserRunner)."""
        return self._call(
            _update_user_runner,
            runner_id=runner_id,
            _body=body,
        )

    @checked
    def set_secret_for_user(
        self,
        secretname: StrictStr,
        body: Optional[Union[CreateOrUpdateSecretOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create or change one of your secrets (updateUserSecret)."""
        return self._call(
            _update_user_secret,
            secretname=secretname,
            _body=body,
        )

    @checked
    def update_variable_for_user(
        self,
        variablename: StrictStr,
        body: Optional[Union[UpdateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Change one of your variables (updateUserVariable)."""
        return self._call(
            _update_user_variable,
            variablename=variablename,
            _body=body,
        )

    @checked
    def create_runner_registration_token_for_user(
        self,
    ) -> None:
        """Create a token that registers a runner of your own (userCreateRunnerRegistrationToken)."""
        return self._call(
            _user_create_runner_registration_token,
        )


class AsyncActionsApi(AsyncResource):
    @checked
    async def disable_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
    ) -> None:
        """Disable a workflow (ActionsDisableWorkflow)."""
        return await self._call(
            _actions_disable_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
        )

    @checked
    async def dispatch_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
        body: Optional[Union[CreateActionWorkflowDispatch, Mapping[str, Any]]] = None,
        *,
        return_run_details: Optional[StrictBool] = None,
        scoped_workflow_source_repo_id: Optional[StrictInt] = None,
    ) -> RunDetails:
        """Start a workflow run by hand (ActionsDispatchWorkflow)."""
        return await self._call(
            _actions_dispatch_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            _body=body,
            return_run_details=return_run_details,
            scoped_workflow_source_repo_id=scoped_workflow_source_repo_id,
        )

    @checked
    async def enable_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
    ) -> None:
        """Enable a workflow (ActionsEnableWorkflow)."""
        return await self._call(
            _actions_enable_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
        )

    @checked
    async def get_workflow(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
    ) -> ActionWorkflow:
        """Get a workflow (ActionsGetWorkflow)."""
        return await self._call(
            _actions_get_workflow,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
        )

    @checked
    async def list_workflows(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> ActionWorkflowResponse:
        """List a repository's workflows (ActionsListRepositoryWorkflows)."""
        return await self._call(
            _actions_list_repository_workflows,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_workflow_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        scoped_workflow_source_repo_id: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of a workflow's runs (ActionsListWorkflowRuns)."""
        return await self._call(
            _actions_list_workflow_runs,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            scoped_workflow_source_repo_id=scoped_workflow_source_repo_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_workflow_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        workflow_id: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        scoped_workflow_source_repo_id: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _actions_list_workflow_runs,
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            scoped_workflow_source_repo_id=scoped_workflow_source_repo_id,
            page=page,
            limit=limit,
        )

    @checked
    async def approve_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Approve a workflow run that waits for approval (approveWorkflowRun)."""
        return await self._call(
            _approve_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def cancel_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Cancel a workflow run (cancelWorkflowRun)."""
        return await self._call(
            _cancel_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def create_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[CreateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create an organization variable (createOrgVariable)."""
        return await self._call(
            _create_org_variable,
            org=org,
            variablename=variablename,
            _body=body,
        )

    @checked
    async def create_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[CreateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create a repository variable (createRepoVariable)."""
        return await self._call(
            _create_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
            _body=body,
        )

    @checked
    async def create_variable_for_user(
        self,
        variablename: StrictStr,
        body: Optional[Union[CreateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create a variable of your own (createUserVariable)."""
        return await self._call(
            _create_user_variable,
            variablename=variablename,
            _body=body,
        )

    @checked
    async def delete_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> None:
        """Delete a workflow run (deleteActionRun)."""
        return await self._call(
            _delete_action_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def delete_artifact(
        self,
        owner: StrictStr,
        repo: StrictStr,
        artifact_id: StrictStr,
    ) -> None:
        """Delete an artifact (deleteArtifact)."""
        return await self._call(
            _delete_artifact,
            owner=owner,
            repo=repo,
            artifact_id=artifact_id,
        )

    @checked
    async def delete_runner_for_org(
        self,
        org: StrictStr,
        runner_id: StrictStr,
    ) -> None:
        """Delete an organization runner (deleteOrgRunner)."""
        return await self._call(
            _delete_org_runner,
            org=org,
            runner_id=runner_id,
        )

    @checked
    async def delete_secret_for_org(
        self,
        org: StrictStr,
        secretname: StrictStr,
    ) -> None:
        """Delete an organization secret (deleteOrgSecret)."""
        return await self._call(
            _delete_org_secret,
            org=org,
            secretname=secretname,
        )

    @checked
    async def delete_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Delete an organization variable (deleteOrgVariable)."""
        return await self._call(
            _delete_org_variable,
            org=org,
            variablename=variablename,
        )

    @checked
    async def delete_runner(
        self,
        owner: StrictStr,
        repo: StrictStr,
        runner_id: StrictStr,
    ) -> None:
        """Delete a repository runner (deleteRepoRunner)."""
        return await self._call(
            _delete_repo_runner,
            owner=owner,
            repo=repo,
            runner_id=runner_id,
        )

    @checked
    async def delete_secret(
        self,
        owner: StrictStr,
        repo: StrictStr,
        secretname: StrictStr,
    ) -> None:
        """Delete a repository secret (deleteRepoSecret)."""
        return await self._call(
            _delete_repo_secret,
            owner=owner,
            repo=repo,
            secretname=secretname,
        )

    @checked
    async def delete_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Delete a repository variable (deleteRepoVariable)."""
        return await self._call(
            _delete_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
        )

    @checked
    async def delete_runner_for_user(
        self,
        runner_id: StrictStr,
    ) -> None:
        """Delete one of your runners (deleteUserRunner)."""
        return await self._call(
            _delete_user_runner,
            runner_id=runner_id,
        )

    @checked
    async def delete_secret_for_user(
        self,
        secretname: StrictStr,
    ) -> None:
        """Delete one of your secrets (deleteUserSecret)."""
        return await self._call(
            _delete_user_secret,
            secretname=secretname,
        )

    @checked
    async def delete_variable_for_user(
        self,
        variablename: StrictStr,
    ) -> None:
        """Delete one of your variables (deleteUserVariable)."""
        return await self._call(
            _delete_user_variable,
            variablename=variablename,
        )

    @checked
    async def download_job_logs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        job_id: StrictInt,
    ) -> None:
        """Download a workflow job's logs (downloadActionsRunJobLogs)."""
        return await self._call(
            _download_actions_run_job_logs,
            owner=owner,
            repo=repo,
            job_id=job_id,
        )

    @checked
    async def download_artifact(
        self,
        owner: StrictStr,
        repo: StrictStr,
        artifact_id: StrictStr,
    ) -> None:
        """Download an artifact, through a redirect to its file (downloadArtifact)."""
        return await self._call(
            _download_artifact,
            owner=owner,
            repo=repo,
            artifact_id=artifact_id,
        )

    @checked
    async def force_cancel_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Cancel a workflow run at once (forceCancelWorkflowRun)."""
        return await self._call(
            _force_cancel_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def get_artifact(
        self,
        owner: StrictStr,
        repo: StrictStr,
        artifact_id: StrictStr,
    ) -> ActionArtifact:
        """Get an artifact (getArtifact)."""
        return await self._call(
            _get_artifact,
            owner=owner,
            repo=repo,
            artifact_id=artifact_id,
        )

    @checked
    async def list_artifacts(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        name: Optional[StrictStr] = None,
    ) -> ActionArtifactsResponse:
        """List a repository's artifacts (getArtifacts)."""
        return await self._call(
            _get_artifacts,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    async def list_run_artifacts(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        *,
        name: Optional[StrictStr] = None,
    ) -> ActionArtifactsResponse:
        """List a workflow run's artifacts (getArtifactsOfRun)."""
        return await self._call(
            _get_artifacts_of_run,
            owner=owner,
            repo=repo,
            run=run,
            name=name,
        )

    @checked
    async def get_runner_for_org(
        self,
        org: StrictStr,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get an organization runner (getOrgRunner)."""
        return await self._call(
            _get_org_runner,
            org=org,
            runner_id=runner_id,
        )

    @checked
    async def list_runners_for_org(
        self,
        org: StrictStr,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List an organization's runners (getOrgRunners)."""
        return await self._call(
            _get_org_runners,
            org=org,
            disabled=disabled,
        )

    @checked
    async def get_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Get an organization variable (getOrgVariable)."""
        return await self._call(
            _get_org_variable,
            org=org,
            variablename=variablename,
        )

    @checked
    async def list_variables_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ActionVariable]:
        """List one page of an organization's variables (getOrgVariablesList)."""
        return await self._call(
            _get_org_variables_list,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_variables_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionVariable]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_org_variables_list,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def list_jobs_for_org(
        self,
        org: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of an organization's workflow jobs (getOrgWorkflowJobs)."""
        return await self._call(
            _get_org_workflow_jobs,
            org=org,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    def iter_jobs_for_org(
        self,
        org: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_org_workflow_jobs,
            org=org,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    async def list_runs_for_org(
        self,
        org: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of an organization's workflow runs (getOrgWorkflowRuns)."""
        return await self._call(
            _get_org_workflow_runs,
            org=org,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs_for_org(
        self,
        org: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_org_workflow_runs,
            org=org,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    async def get_runner(
        self,
        owner: StrictStr,
        repo: StrictStr,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get a repository runner (getRepoRunner)."""
        return await self._call(
            _get_repo_runner,
            owner=owner,
            repo=repo,
            runner_id=runner_id,
        )

    @checked
    async def list_runners(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List a repository's runners (getRepoRunners)."""
        return await self._call(
            _get_repo_runners,
            owner=owner,
            repo=repo,
            disabled=disabled,
        )

    @checked
    async def get_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Get a repository variable (getRepoVariable)."""
        return await self._call(
            _get_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
        )

    @checked
    async def list_variables(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ActionVariable]:
        """List one page of a repository's variables (getRepoVariablesList)."""
        return await self._call(
            _get_repo_variables_list,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_variables(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionVariable]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_repo_variables_list,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def get_runner_for_user(
        self,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get one of your runners (getUserRunner)."""
        return await self._call(
            _get_user_runner,
            runner_id=runner_id,
        )

    @checked
    async def list_runners_for_user(
        self,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List your own runners (getUserRunners)."""
        return await self._call(
            _get_user_runners,
            disabled=disabled,
        )

    @checked
    async def get_variable_for_user(
        self,
        variablename: StrictStr,
    ) -> ActionVariable:
        """Get one of your variables (getUserVariable)."""
        return await self._call(
            _get_user_variable,
            variablename=variablename,
        )

    @checked
    async def list_variables_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ActionVariable]:
        """List one page of your own variables (getUserVariablesList)."""
        return await self._call(
            _get_user_variables_list,
            page=page,
            limit=limit,
        )

    @checked
    def iter_variables_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionVariable]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_variables_list,
            page=page,
            limit=limit,
        )

    @checked
    async def list_jobs_for_user(
        self,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of your own workflow jobs (getUserWorkflowJobs)."""
        return await self._call(
            _get_user_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_jobs_for_user(
        self,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    async def list_runs_for_user(
        self,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of your own workflow runs (getUserWorkflowRuns)."""
        return await self._call(
            _get_user_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs_for_user(
        self,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    async def get_job(
        self,
        owner: StrictStr,
        repo: StrictStr,
        job_id: StrictStr,
    ) -> ActionWorkflowJob:
        """Get a workflow job (getWorkflowJob)."""
        return await self._call(
            _get_workflow_job,
            owner=owner,
            repo=repo,
            job_id=job_id,
        )

    @checked
    async def get_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Get a workflow run (GetWorkflowRun)."""
        return await self._call(
            _get_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def get_run_attempt(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        attempt: StrictInt,
    ) -> ActionWorkflowRun:
        """Get one attempt of a workflow run (getWorkflowRunAttempt)."""
        return await self._call(
            _get_workflow_run_attempt,
            owner=owner,
            repo=repo,
            run=run,
            attempt=attempt,
        )

    @checked
    async def download_run_logs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> None:
        """Download a workflow run's logs (getWorkflowRunLogs)."""
        return await self._call(
            _get_workflow_run_logs,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def list_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowRunsResponse:
        """List one page of a repository's workflow runs (getWorkflowRuns)."""
        return await self._call(
            _get_workflow_runs,
            owner=owner,
            repo=repo,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        event: Optional[StrictStr] = None,
        branch: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        actor: Optional[StrictStr] = None,
        head_sha: Optional[StrictStr] = None,
        exclude_pull_requests: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionWorkflowRun]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_workflow_runs,
            owner=owner,
            repo=repo,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            exclude_pull_requests=exclude_pull_requests,
            page=page,
            limit=limit,
        )

    @checked
    async def list_tasks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionTaskResponse:
        """List one page of a repository's action tasks (ListActionTasks)."""
        return await self._call(
            _list_action_tasks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tasks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_action_tasks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def list_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of a repository's workflow jobs (listWorkflowJobs)."""
        return await self._call(
            _list_workflow_jobs,
            owner=owner,
            repo=repo,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_workflow_jobs,
            owner=owner,
            repo=repo,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    async def list_run_attempt_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        attempt: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of the jobs in one attempt of a workflow run (listWorkflowRunAttemptJobs)."""
        return await self._call(
            _list_workflow_run_attempt_jobs,
            owner=owner,
            repo=repo,
            run=run,
            attempt=attempt,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    def iter_run_attempt_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        attempt: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_workflow_run_attempt_jobs,
            owner=owner,
            repo=repo,
            run=run,
            attempt=attempt,
            status=status,
            page=page,
            limit=limit,
        )

    @checked
    async def list_run_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of a workflow run's jobs (listWorkflowRunJobs)."""
        return await self._call(
            _list_workflow_run_jobs,
            owner=owner,
            repo=repo,
            run=run,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_run_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ActionWorkflowJob]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_workflow_run_jobs,
            owner=owner,
            repo=repo,
            run=run,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    async def create_runner_registration_token_for_org(
        self,
        org: StrictStr,
    ) -> None:
        """Create a token that registers an organization runner (orgCreateRunnerRegistrationToken)."""
        return await self._call(
            _org_create_runner_registration_token,
            org=org,
        )

    @checked
    async def list_secrets_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Secret]:
        """List one page of an organization's secrets (orgListActionsSecrets)."""
        return await self._call(
            _org_list_actions_secrets,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_secrets_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Secret]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_actions_secrets,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def create_runner_registration_token(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Create a token that registers a repository runner (repoCreateRunnerRegistrationToken)."""
        return await self._call(
            _repo_create_runner_registration_token,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_secrets(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Secret]:
        """List one page of a repository's secrets (repoListActionsSecrets)."""
        return await self._call(
            _repo_list_actions_secrets,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_secrets(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Secret]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_actions_secrets,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def rerun_failed_jobs(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> None:
        """Run a workflow run's failed jobs again (rerunFailedWorkflowRun)."""
        return await self._call(
            _rerun_failed_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def rerun_job(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
        job_id: StrictInt,
    ) -> ActionWorkflowJob:
        """Run a workflow job again (rerunWorkflowJob)."""
        return await self._call(
            _rerun_workflow_job,
            owner=owner,
            repo=repo,
            run=run,
            job_id=job_id,
        )

    @checked
    async def rerun_run(
        self,
        owner: StrictStr,
        repo: StrictStr,
        run: StrictInt,
    ) -> ActionWorkflowRun:
        """Run a workflow run again (rerunWorkflowRun)."""
        return await self._call(
            _rerun_workflow_run,
            owner=owner,
            repo=repo,
            run=run,
        )

    @checked
    async def update_runner_for_org(
        self,
        org: StrictStr,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change an organization runner (updateOrgRunner)."""
        return await self._call(
            _update_org_runner,
            org=org,
            runner_id=runner_id,
            _body=body,
        )

    @checked
    async def set_secret_for_org(
        self,
        org: StrictStr,
        secretname: StrictStr,
        body: Optional[Union[CreateOrUpdateSecretOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create or change an organization secret (updateOrgSecret)."""
        return await self._call(
            _update_org_secret,
            org=org,
            secretname=secretname,
            _body=body,
        )

    @checked
    async def update_variable_for_org(
        self,
        org: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[UpdateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Change an organization variable (updateOrgVariable)."""
        return await self._call(
            _update_org_variable,
            org=org,
            variablename=variablename,
            _body=body,
        )

    @checked
    async def update_runner(
        self,
        owner: StrictStr,
        repo: StrictStr,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change a repository runner (updateRepoRunner)."""
        return await self._call(
            _update_repo_runner,
            owner=owner,
            repo=repo,
            runner_id=runner_id,
            _body=body,
        )

    @checked
    async def set_secret(
        self,
        owner: StrictStr,
        repo: StrictStr,
        secretname: StrictStr,
        body: Optional[Union[CreateOrUpdateSecretOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create or change a repository secret (updateRepoSecret)."""
        return await self._call(
            _update_repo_secret,
            owner=owner,
            repo=repo,
            secretname=secretname,
            _body=body,
        )

    @checked
    async def update_variable(
        self,
        owner: StrictStr,
        repo: StrictStr,
        variablename: StrictStr,
        body: Optional[Union[UpdateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Change a repository variable (updateRepoVariable)."""
        return await self._call(
            _update_repo_variable,
            owner=owner,
            repo=repo,
            variablename=variablename,
            _body=body,
        )

    @checked
    async def update_runner_for_user(
        self,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change one of your runners (updateUserRunner)."""
        return await self._call(
            _update_user_runner,
            runner_id=runner_id,
            _body=body,
        )

    @checked
    async def set_secret_for_user(
        self,
        secretname: StrictStr,
        body: Optional[Union[CreateOrUpdateSecretOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Create or change one of your secrets (updateUserSecret)."""
        return await self._call(
            _update_user_secret,
            secretname=secretname,
            _body=body,
        )

    @checked
    async def update_variable_for_user(
        self,
        variablename: StrictStr,
        body: Optional[Union[UpdateVariableOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Change one of your variables (updateUserVariable)."""
        return await self._call(
            _update_user_variable,
            variablename=variablename,
            _body=body,
        )

    @checked
    async def create_runner_registration_token_for_user(
        self,
    ) -> None:
        """Create a token that registers a runner of your own (userCreateRunnerRegistrationToken)."""
        return await self._call(
            _user_create_runner_registration_token,
        )
