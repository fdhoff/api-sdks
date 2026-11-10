# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import date, datetime
from typing import Any, AsyncIterator, Dict, Iterator, List, Mapping, Optional, Union

from pydantic import StrictBool, StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import (
    AsyncDownload,
    AsyncResource,
    Download,
    LinkHeader,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from gitea_rest.models.activity import Activity
from gitea_rest.models.add_collaborator_option import AddCollaboratorOption
from gitea_rest.models.create_deploy_key_token_option import CreateDeployKeyTokenOption
from gitea_rest.models.create_fork_option import CreateForkOption
from gitea_rest.models.create_key_option import CreateKeyOption
from gitea_rest.models.create_push_mirror_option import CreatePushMirrorOption
from gitea_rest.models.deploy_key import DeployKey
from gitea_rest.models.edit_repo_option import EditRepoOption
from gitea_rest.models.generate_repo_option import GenerateRepoOption
from gitea_rest.models.issue_config import IssueConfig
from gitea_rest.models.issue_config_validation import IssueConfigValidation
from gitea_rest.models.issue_template import IssueTemplate
from gitea_rest.models.merge_upstream_request import MergeUpstreamRequest
from gitea_rest.models.merge_upstream_response import MergeUpstreamResponse
from gitea_rest.models.migrate_repo_options import MigrateRepoOptions
from gitea_rest.models.new_issue_pins_allowed import NewIssuePinsAllowed
from gitea_rest.models.push_mirror import PushMirror
from gitea_rest.models.repo_collaborator_permission import RepoCollaboratorPermission
from gitea_rest.models.repo_topic_options import RepoTopicOptions
from gitea_rest.models.repository import Repository
from gitea_rest.models.search_results import SearchResults
from gitea_rest.models.team import Team
from gitea_rest.models.topic_list_response import TopicListResponse
from gitea_rest.models.topic_name import TopicName
from gitea_rest.models.tracked_time import TrackedTime
from gitea_rest.models.transfer_repo_option import TransferRepoOption
from gitea_rest.models.update_repo_avatar_option import UpdateRepoAvatarOption
from gitea_rest.models.user import User

_accept_repo_transfer: Operation[Repository] = Operation(
    id="acceptRepoTransfer",
    method="POST",
    path="/repos/{owner}/{repo}/transfer/accept",
    resource="repos",
    name="accept_transfer",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Repository,
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
_create_fork: Operation[Repository] = Operation(
    id="createFork",
    method="POST",
    path="/repos/{owner}/{repo}/forks",
    resource="repos",
    name="fork",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Repository,
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
_generate_repo: Operation[Repository] = Operation(
    id="generateRepo",
    method="POST",
    path="/repos/{template_owner}/{template_repo}/generate",
    resource="repos",
    name="generate",
    params=(
        Param("template_owner", "template_owner", "path"),
        Param("template_repo", "template_repo", "path"),
    ),
    response=Repository,
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
_list_forks: Operation[List[Repository]] = Operation(
    id="listForks",
    method="GET",
    path="/repos/{owner}/{repo}/forks",
    resource="repos",
    name="list_forks",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Repository],
    returns_json=True,
    iterator="iter_forks",
    item=_models.Repository,
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
_reject_repo_transfer: Operation[Repository] = Operation(
    id="rejectRepoTransfer",
    method="POST",
    path="/repos/{owner}/{repo}/transfer/reject",
    resource="repos",
    name="reject_transfer",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Repository,
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
_repo_add_collaborator: Operation[None] = Operation(
    id="repoAddCollaborator",
    method="PUT",
    path="/repos/{owner}/{repo}/collaborators/{collaborator}",
    resource="repos",
    name="add_collaborator",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("collaborator", "collaborator", "path"),
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
_repo_add_push_mirror: Operation[PushMirror] = Operation(
    id="repoAddPushMirror",
    method="POST",
    path="/repos/{owner}/{repo}/push_mirrors",
    resource="repos",
    name="add_push_mirror",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=PushMirror,
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
_repo_add_team: Operation[None] = Operation(
    id="repoAddTeam",
    method="PUT",
    path="/repos/{owner}/{repo}/teams/{team}",
    resource="repos",
    name="add_team",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("team", "team", "path"),
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
_repo_add_topic: Operation[None] = Operation(
    id="repoAddTopic",
    method="PUT",
    path="/repos/{owner}/{repo}/topics/{topic}",
    resource="repos",
    name="add_topic",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("topic", "topic", "path"),
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
_repo_check_assignee: Operation[None] = Operation(
    id="repoCheckAssignee",
    method="GET",
    path="/repos/{owner}/{repo}/assignees/{assignee}",
    resource="repos",
    name="check_assignee",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("assignee", "assignee", "path"),
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
_repo_check_collaborator: Operation[None] = Operation(
    id="repoCheckCollaborator",
    method="GET",
    path="/repos/{owner}/{repo}/collaborators/{collaborator}",
    resource="repos",
    name="check_collaborator",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("collaborator", "collaborator", "path"),
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
_repo_check_team: Operation[Team] = Operation(
    id="repoCheckTeam",
    method="GET",
    path="/repos/{owner}/{repo}/teams/{team}",
    resource="repos",
    name="check_team",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("team", "team", "path"),
    ),
    response=Team,
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
_repo_create_deploy_token: Operation[DeployKey] = Operation(
    id="repoCreateDeployToken",
    method="POST",
    path="/repos/{owner}/{repo}/keys/tokens",
    resource="repos",
    name="create_deploy_token",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=DeployKey,
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
_repo_create_key: Operation[DeployKey] = Operation(
    id="repoCreateKey",
    method="POST",
    path="/repos/{owner}/{repo}/keys",
    resource="repos",
    name="add_deploy_key",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=DeployKey,
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
_repo_delete: Operation[None] = Operation(
    id="repoDelete",
    method="DELETE",
    path="/repos/{owner}/{repo}",
    resource="repos",
    name="delete",
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
_repo_delete_avatar: Operation[None] = Operation(
    id="repoDeleteAvatar",
    method="DELETE",
    path="/repos/{owner}/{repo}/avatar",
    resource="repos",
    name="delete_avatar",
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
_repo_delete_collaborator: Operation[None] = Operation(
    id="repoDeleteCollaborator",
    method="DELETE",
    path="/repos/{owner}/{repo}/collaborators/{collaborator}",
    resource="repos",
    name="remove_collaborator",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("collaborator", "collaborator", "path"),
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
_repo_delete_key: Operation[None] = Operation(
    id="repoDeleteKey",
    method="DELETE",
    path="/repos/{owner}/{repo}/keys/{id}",
    resource="repos",
    name="delete_deploy_key",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
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
_repo_delete_push_mirror: Operation[None] = Operation(
    id="repoDeletePushMirror",
    method="DELETE",
    path="/repos/{owner}/{repo}/push_mirrors/{name}",
    resource="repos",
    name="delete_push_mirror",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("name", "name", "path"),
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
_repo_delete_team: Operation[None] = Operation(
    id="repoDeleteTeam",
    method="DELETE",
    path="/repos/{owner}/{repo}/teams/{team}",
    resource="repos",
    name="remove_team",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("team", "team", "path"),
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
_repo_delete_topic: Operation[None] = Operation(
    id="repoDeleteTopic",
    method="DELETE",
    path="/repos/{owner}/{repo}/topics/{topic}",
    resource="repos",
    name="remove_topic",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("topic", "topic", "path"),
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
_repo_edit: Operation[Repository] = Operation(
    id="repoEdit",
    method="PATCH",
    path="/repos/{owner}/{repo}",
    resource="repos",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Repository,
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
_repo_get: Operation[Repository] = Operation(
    id="repoGet",
    method="GET",
    path="/repos/{owner}/{repo}",
    resource="repos",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Repository,
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
_repo_get_archive: Operation[None] = Operation(
    id="repoGetArchive",
    method="GET",
    path="/repos/{owner}/{repo}/archive/{archive}",
    resource="repos",
    name="download_archive",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("archive", "archive", "path"),
        Param("path", "path", "query"),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
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
_repo_get_assignees: Operation[List[User]] = Operation(
    id="repoGetAssignees",
    method="GET",
    path="/repos/{owner}/{repo}/assignees",
    resource="repos",
    name="list_assignees",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[User],
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
_repo_get_by_id: Operation[Repository] = Operation(
    id="repoGetByID",
    method="GET",
    path="/repositories/{id}",
    resource="repos",
    name="get_by_id",
    params=(Param("id", "id", "path"),),
    response=Repository,
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
_repo_get_issue_config: Operation[IssueConfig] = Operation(
    id="repoGetIssueConfig",
    method="GET",
    path="/repos/{owner}/{repo}/issue_config",
    resource="repos",
    name="get_issue_config",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=IssueConfig,
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
_repo_get_issue_templates: Operation[List[IssueTemplate]] = Operation(
    id="repoGetIssueTemplates",
    method="GET",
    path="/repos/{owner}/{repo}/issue_templates",
    resource="repos",
    name="list_issue_templates",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[IssueTemplate],
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
_repo_get_key: Operation[DeployKey] = Operation(
    id="repoGetKey",
    method="GET",
    path="/repos/{owner}/{repo}/keys/{id}",
    resource="repos",
    name="get_deploy_key",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=DeployKey,
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
_repo_get_languages: Operation[Dict[str, int]] = Operation(
    id="repoGetLanguages",
    method="GET",
    path="/repos/{owner}/{repo}/languages",
    resource="repos",
    name="get_languages",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Dict[str, int],
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
_repo_get_licenses: Operation[List[str]] = Operation(
    id="repoGetLicenses",
    method="GET",
    path="/repos/{owner}/{repo}/licenses",
    resource="repos",
    name="list_licenses",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[str],
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
_repo_get_push_mirror_by_remote_name: Operation[PushMirror] = Operation(
    id="repoGetPushMirrorByRemoteName",
    method="GET",
    path="/repos/{owner}/{repo}/push_mirrors/{name}",
    resource="repos",
    name="get_push_mirror",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("name", "name", "path"),
    ),
    response=PushMirror,
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
_repo_get_repo_permissions: Operation[RepoCollaboratorPermission] = Operation(
    id="repoGetRepoPermissions",
    method="GET",
    path="/repos/{owner}/{repo}/collaborators/{collaborator}/permission",
    resource="repos",
    name="get_permissions",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("collaborator", "collaborator", "path"),
    ),
    response=RepoCollaboratorPermission,
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
_repo_get_reviewers: Operation[List[User]] = Operation(
    id="repoGetReviewers",
    method="GET",
    path="/repos/{owner}/{repo}/reviewers",
    resource="repos",
    name="list_reviewers",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[User],
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
_repo_list_activity_feeds: Operation[List[Activity]] = Operation(
    id="repoListActivityFeeds",
    method="GET",
    path="/repos/{owner}/{repo}/activities/feeds",
    resource="repos",
    name="list_activity_feeds",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("date", "var_date", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Activity],
    returns_json=True,
    iterator="iter_activity_feeds",
    item=_models.Activity,
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
_repo_list_collaborators: Operation[List[User]] = Operation(
    id="repoListCollaborators",
    method="GET",
    path="/repos/{owner}/{repo}/collaborators",
    resource="repos",
    name="list_collaborators",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_collaborators",
    item=_models.User,
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
_repo_list_keys: Operation[List[DeployKey]] = Operation(
    id="repoListKeys",
    method="GET",
    path="/repos/{owner}/{repo}/keys",
    resource="repos",
    name="list_deploy_keys",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("key_id", "key_id", "query"),
        Param("fingerprint", "fingerprint", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[DeployKey],
    returns_json=True,
    iterator="iter_deploy_keys",
    item=_models.DeployKey,
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
_repo_list_push_mirrors: Operation[List[PushMirror]] = Operation(
    id="repoListPushMirrors",
    method="GET",
    path="/repos/{owner}/{repo}/push_mirrors",
    resource="repos",
    name="list_push_mirrors",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[PushMirror],
    returns_json=True,
    iterator="iter_push_mirrors",
    item=_models.PushMirror,
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
_repo_list_stargazers: Operation[List[User]] = Operation(
    id="repoListStargazers",
    method="GET",
    path="/repos/{owner}/{repo}/stargazers",
    resource="repos",
    name="list_stargazers",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_stargazers",
    item=_models.User,
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
_repo_list_subscribers: Operation[List[User]] = Operation(
    id="repoListSubscribers",
    method="GET",
    path="/repos/{owner}/{repo}/subscribers",
    resource="repos",
    name="list_watchers",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_watchers",
    item=_models.User,
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
_repo_list_teams: Operation[List[Team]] = Operation(
    id="repoListTeams",
    method="GET",
    path="/repos/{owner}/{repo}/teams",
    resource="repos",
    name="list_teams",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[Team],
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
_repo_list_topics: Operation[TopicName] = Operation(
    id="repoListTopics",
    method="GET",
    path="/repos/{owner}/{repo}/topics",
    resource="repos",
    name="list_topics",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=TopicName,
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
_repo_merge_upstream: Operation[MergeUpstreamResponse] = Operation(
    id="repoMergeUpstream",
    method="POST",
    path="/repos/{owner}/{repo}/merge-upstream",
    resource="repos",
    name="merge_upstream",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=MergeUpstreamResponse,
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
_repo_migrate: Operation[Repository] = Operation(
    id="repoMigrate",
    method="POST",
    path="/repos/migrate",
    resource="repos",
    name="migrate",
    params=(),
    response=Repository,
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
_repo_mirror_sync: Operation[None] = Operation(
    id="repoMirrorSync",
    method="POST",
    path="/repos/{owner}/{repo}/mirror-sync",
    resource="repos",
    name="sync_mirror",
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
_repo_new_pin_allowed: Operation[NewIssuePinsAllowed] = Operation(
    id="repoNewPinAllowed",
    method="GET",
    path="/repos/{owner}/{repo}/new_pin_allowed",
    resource="repos",
    name="check_pin_allowed",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=NewIssuePinsAllowed,
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
_repo_push_mirror_sync: Operation[None] = Operation(
    id="repoPushMirrorSync",
    method="POST",
    path="/repos/{owner}/{repo}/push_mirrors-sync",
    resource="repos",
    name="sync_push_mirrors",
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
_repo_search: Operation[SearchResults] = Operation(
    id="repoSearch",
    method="GET",
    path="/repos/search",
    resource="repos",
    name="search",
    params=(
        Param("q", "q", "query"),
        Param("topic", "topic", "query"),
        Param("includeDesc", "include_desc", "query"),
        Param("uid", "uid", "query"),
        Param("priority_owner_id", "priority_owner_id", "query"),
        Param("team_id", "team_id", "query"),
        Param("starredBy", "starred_by", "query"),
        Param("private", "private", "query"),
        Param("is_private", "is_private", "query"),
        Param("template", "template", "query"),
        Param("archived", "archived", "query"),
        Param("mode", "mode", "query"),
        Param("exclusive", "exclusive", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=SearchResults,
    returns_json=True,
    iterator="iter_search",
    item=_models.Repository,
    paging=LinkHeader(
        items="data",
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
_repo_signing_key: Operation[str] = Operation(
    id="repoSigningKey",
    method="GET",
    path="/repos/{owner}/{repo}/signing-key.gpg",
    resource="repos",
    name="get_signing_key",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=str,
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
_repo_signing_key_ssh: Operation[str] = Operation(
    id="repoSigningKeySSH",
    method="GET",
    path="/repos/{owner}/{repo}/signing-key.pub",
    resource="repos",
    name="get_ssh_signing_key",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=str,
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
_repo_tracked_times: Operation[List[TrackedTime]] = Operation(
    id="repoTrackedTimes",
    method="GET",
    path="/repos/{owner}/{repo}/times",
    resource="repos",
    name="list_tracked_times",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("user", "user", "query"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[TrackedTime],
    returns_json=True,
    iterator="iter_tracked_times",
    item=_models.TrackedTime,
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
_repo_transfer: Operation[Repository] = Operation(
    id="repoTransfer",
    method="POST",
    path="/repos/{owner}/{repo}/transfer",
    resource="repos",
    name="transfer",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Repository,
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
_repo_update_avatar: Operation[None] = Operation(
    id="repoUpdateAvatar",
    method="POST",
    path="/repos/{owner}/{repo}/avatar",
    resource="repos",
    name="update_avatar",
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
_repo_update_topics: Operation[None] = Operation(
    id="repoUpdateTopics",
    method="PUT",
    path="/repos/{owner}/{repo}/topics",
    resource="repos",
    name="replace_topics",
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
_repo_validate_issue_config: Operation[IssueConfigValidation] = Operation(
    id="repoValidateIssueConfig",
    method="GET",
    path="/repos/{owner}/{repo}/issue_config/validate",
    resource="repos",
    name="validate_issue_config",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=IssueConfigValidation,
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
_topic_search: Operation[TopicListResponse] = Operation(
    id="topicSearch",
    method="GET",
    path="/topics/search",
    resource="repos",
    name="search_topics",
    params=(
        Param("q", "q", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=TopicListResponse,
    returns_json=True,
    iterator="iter_search_topics",
    item=_models.TopicResponse,
    paging=LinkHeader(
        items="topics",
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

OPERATIONS = (
    _accept_repo_transfer,
    _create_fork,
    _generate_repo,
    _list_forks,
    _reject_repo_transfer,
    _repo_add_collaborator,
    _repo_add_push_mirror,
    _repo_add_team,
    _repo_add_topic,
    _repo_check_assignee,
    _repo_check_collaborator,
    _repo_check_team,
    _repo_create_deploy_token,
    _repo_create_key,
    _repo_delete,
    _repo_delete_avatar,
    _repo_delete_collaborator,
    _repo_delete_key,
    _repo_delete_push_mirror,
    _repo_delete_team,
    _repo_delete_topic,
    _repo_edit,
    _repo_get,
    _repo_get_archive,
    _repo_get_assignees,
    _repo_get_by_id,
    _repo_get_issue_config,
    _repo_get_issue_templates,
    _repo_get_key,
    _repo_get_languages,
    _repo_get_licenses,
    _repo_get_push_mirror_by_remote_name,
    _repo_get_repo_permissions,
    _repo_get_reviewers,
    _repo_list_activity_feeds,
    _repo_list_collaborators,
    _repo_list_keys,
    _repo_list_push_mirrors,
    _repo_list_stargazers,
    _repo_list_subscribers,
    _repo_list_teams,
    _repo_list_topics,
    _repo_merge_upstream,
    _repo_migrate,
    _repo_mirror_sync,
    _repo_new_pin_allowed,
    _repo_push_mirror_sync,
    _repo_search,
    _repo_signing_key,
    _repo_signing_key_ssh,
    _repo_tracked_times,
    _repo_transfer,
    _repo_update_avatar,
    _repo_update_topics,
    _repo_validate_issue_config,
    _topic_search,
)


class ReposApi(Resource):
    @checked
    def accept_transfer(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Accept a repository transfer (acceptRepoTransfer)."""
        return self._call(
            _accept_repo_transfer,
            owner=owner,
            repo=repo,
        )

    @checked
    def fork(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateForkOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Fork a repository (createFork)."""
        return self._call(
            _create_fork,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def generate(
        self,
        template_owner: StrictStr,
        template_repo: StrictStr,
        body: Optional[Union[GenerateRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Create a repository from a template repository (generateRepo)."""
        return self._call(
            _generate_repo,
            template_owner=template_owner,
            template_repo=template_repo,
            _body=body,
        )

    @checked
    def list_forks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of a repository's forks (listForks)."""
        return self._call(
            _list_forks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_forks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_forks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def reject_transfer(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Reject a repository transfer (rejectRepoTransfer)."""
        return self._call(
            _reject_repo_transfer,
            owner=owner,
            repo=repo,
        )

    @checked
    def add_collaborator(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
        body: Optional[Union[AddCollaboratorOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Add a collaborator, or change a collaborator's permission (repoAddCollaborator)."""
        return self._call(
            _repo_add_collaborator,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
            _body=body,
        )

    @checked
    def add_push_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreatePushMirrorOption, Mapping[str, Any]]] = None,
    ) -> PushMirror:
        """Add a push mirror (repoAddPushMirror)."""
        return self._call(
            _repo_add_push_mirror,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def add_team(
        self,
        owner: StrictStr,
        repo: StrictStr,
        team: StrictStr,
    ) -> None:
        """Give a team access to a repository (repoAddTeam)."""
        return self._call(
            _repo_add_team,
            owner=owner,
            repo=repo,
            team=team,
        )

    @checked
    def add_topic(
        self,
        owner: StrictStr,
        repo: StrictStr,
        topic: StrictStr,
    ) -> None:
        """Add a topic to a repository (repoAddTopic)."""
        return self._call(
            _repo_add_topic,
            owner=owner,
            repo=repo,
            topic=topic,
        )

    @checked
    def check_assignee(
        self,
        owner: StrictStr,
        repo: StrictStr,
        assignee: StrictStr,
    ) -> None:
        """Check whether a user can be assigned issues and pull requests (repoCheckAssignee)."""
        return self._call(
            _repo_check_assignee,
            owner=owner,
            repo=repo,
            assignee=assignee,
        )

    @checked
    def check_collaborator(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
    ) -> None:
        """Check whether a user is a collaborator (repoCheckCollaborator)."""
        return self._call(
            _repo_check_collaborator,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
        )

    @checked
    def check_team(
        self,
        owner: StrictStr,
        repo: StrictStr,
        team: StrictStr,
    ) -> Team:
        """Check whether a team has access to a repository (repoCheckTeam)."""
        return self._call(
            _repo_check_team,
            owner=owner,
            repo=repo,
            team=team,
        )

    @checked
    def create_deploy_token(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateDeployKeyTokenOption, Mapping[str, Any]]] = None,
    ) -> DeployKey:
        """Create a deploy token, for Git over HTTPS (repoCreateDeployToken)."""
        return self._call(
            _repo_create_deploy_token,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def add_deploy_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateKeyOption, Mapping[str, Any]]] = None,
    ) -> DeployKey:
        """Add a deploy key (repoCreateKey)."""
        return self._call(
            _repo_create_key,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Delete a repository (repoDelete)."""
        return self._call(
            _repo_delete,
            owner=owner,
            repo=repo,
        )

    @checked
    def delete_avatar(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Remove a repository's avatar (repoDeleteAvatar)."""
        return self._call(
            _repo_delete_avatar,
            owner=owner,
            repo=repo,
        )

    @checked
    def remove_collaborator(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
    ) -> None:
        """Remove a collaborator (repoDeleteCollaborator)."""
        return self._call(
            _repo_delete_collaborator,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
        )

    @checked
    def delete_deploy_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a deploy key (repoDeleteKey)."""
        return self._call(
            _repo_delete_key,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def delete_push_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> None:
        """Delete a push mirror (repoDeletePushMirror)."""
        return self._call(
            _repo_delete_push_mirror,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    def remove_team(
        self,
        owner: StrictStr,
        repo: StrictStr,
        team: StrictStr,
    ) -> None:
        """Remove a team's access to a repository (repoDeleteTeam)."""
        return self._call(
            _repo_delete_team,
            owner=owner,
            repo=repo,
            team=team,
        )

    @checked
    def remove_topic(
        self,
        owner: StrictStr,
        repo: StrictStr,
        topic: StrictStr,
    ) -> None:
        """Remove a topic from a repository (repoDeleteTopic)."""
        return self._call(
            _repo_delete_topic,
            owner=owner,
            repo=repo,
            topic=topic,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[EditRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Change a repository's settings (repoEdit)."""
        return self._call(
            _repo_edit,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Get a repository (repoGet)."""
        return self._call(
            _repo_get,
            owner=owner,
            repo=repo,
        )

    @checked
    def download_archive(
        self,
        owner: StrictStr,
        repo: StrictStr,
        archive: StrictStr,
        *,
        path: Optional[List[StrictStr]] = None,
    ) -> Download:
        """Download an archive of a repository at a ref (repoGetArchive). Close the download, or read it in a `with` block."""
        return self._download(
            _repo_get_archive,
            owner=owner,
            repo=repo,
            archive=archive,
            path=path,
        )

    @checked
    def list_assignees(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[User]:
        """List the users that issues and pull requests can be assigned to (repoGetAssignees)."""
        return self._call(
            _repo_get_assignees,
            owner=owner,
            repo=repo,
        )

    @checked
    def get_by_id(
        self,
        id: StrictInt,
    ) -> Repository:
        """Get a repository by its ID (repoGetByID)."""
        return self._call(
            _repo_get_by_id,
            id=id,
        )

    @checked
    def get_issue_config(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> IssueConfig:
        """Get a repository's issue template configuration (repoGetIssueConfig)."""
        return self._call(
            _repo_get_issue_config,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_issue_templates(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[IssueTemplate]:
        """List a repository's issue templates (repoGetIssueTemplates)."""
        return self._call(
            _repo_get_issue_templates,
            owner=owner,
            repo=repo,
        )

    @checked
    def get_deploy_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> DeployKey:
        """Get a deploy key (repoGetKey)."""
        return self._call(
            _repo_get_key,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def get_languages(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Dict[str, int]:
        """Get how many bytes of each language a repository holds (repoGetLanguages)."""
        return self._call(
            _repo_get_languages,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_licenses(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[str]:
        """List the licenses found in a repository (repoGetLicenses)."""
        return self._call(
            _repo_get_licenses,
            owner=owner,
            repo=repo,
        )

    @checked
    def get_push_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> PushMirror:
        """Get a push mirror by its remote name (repoGetPushMirrorByRemoteName)."""
        return self._call(
            _repo_get_push_mirror_by_remote_name,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    def get_permissions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
    ) -> RepoCollaboratorPermission:
        """Get a user's permissions on a repository (repoGetRepoPermissions)."""
        return self._call(
            _repo_get_repo_permissions,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
        )

    @checked
    def list_reviewers(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[User]:
        """List the users that can be asked to review pull requests (repoGetReviewers)."""
        return self._call(
            _repo_get_reviewers,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_activity_feeds(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of a repository's activity (repoListActivityFeeds)."""
        return self._call(
            _repo_list_activity_feeds,
            owner=owner,
            repo=repo,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_activity_feeds,
            owner=owner,
            repo=repo,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def list_collaborators(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of a repository's collaborators (repoListCollaborators)."""
        return self._call(
            _repo_list_collaborators,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_collaborators(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_collaborators,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def list_deploy_keys(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        key_id: Optional[StrictInt] = None,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[DeployKey]:
        """List one page of a repository's deploy keys (repoListKeys)."""
        return self._call(
            _repo_list_keys,
            owner=owner,
            repo=repo,
            key_id=key_id,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def iter_deploy_keys(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        key_id: Optional[StrictInt] = None,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.DeployKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_keys,
            owner=owner,
            repo=repo,
            key_id=key_id,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def list_push_mirrors(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PushMirror]:
        """List one page of a repository's push mirrors (repoListPushMirrors)."""
        return self._call(
            _repo_list_push_mirrors,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_push_mirrors(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.PushMirror]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_push_mirrors,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def list_stargazers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users who starred a repository (repoListStargazers)."""
        return self._call(
            _repo_list_stargazers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_stargazers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_stargazers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def list_watchers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users who watch a repository (repoListSubscribers)."""
        return self._call(
            _repo_list_subscribers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_watchers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_subscribers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def list_teams(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[Team]:
        """List the teams that have access to a repository (repoListTeams)."""
        return self._call(
            _repo_list_teams,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_topics(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> TopicName:
        """List a page of a repository's topics (repoListTopics)."""
        return self._call(
            _repo_list_topics,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def merge_upstream(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[MergeUpstreamRequest, Mapping[str, Any]]] = None,
    ) -> MergeUpstreamResponse:
        """Merge a branch from a fork's upstream repository (repoMergeUpstream)."""
        return self._call(
            _repo_merge_upstream,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def migrate(
        self,
        body: Optional[Union[MigrateRepoOptions, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Migrate a repository from another service (repoMigrate)."""
        return self._call(
            _repo_migrate,
            _body=body,
        )

    @checked
    def sync_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Sync a mirror repository from its remote (repoMirrorSync)."""
        return self._call(
            _repo_mirror_sync,
            owner=owner,
            repo=repo,
        )

    @checked
    def check_pin_allowed(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> NewIssuePinsAllowed:
        """Check whether more issues and pull requests can be pinned (repoNewPinAllowed)."""
        return self._call(
            _repo_new_pin_allowed,
            owner=owner,
            repo=repo,
        )

    @checked
    def sync_push_mirrors(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Push a repository to all of its push mirrors (repoPushMirrorSync)."""
        return self._call(
            _repo_push_mirror_sync,
            owner=owner,
            repo=repo,
        )

    @checked
    def search(
        self,
        *,
        q: Optional[StrictStr] = None,
        topic: Optional[StrictBool] = None,
        include_desc: Optional[StrictBool] = None,
        uid: Optional[StrictInt] = None,
        priority_owner_id: Optional[StrictInt] = None,
        team_id: Optional[StrictInt] = None,
        starred_by: Optional[StrictInt] = None,
        private: Optional[StrictBool] = None,
        is_private: Optional[StrictBool] = None,
        template: Optional[StrictBool] = None,
        archived: Optional[StrictBool] = None,
        mode: Optional[StrictStr] = None,
        exclusive: Optional[StrictBool] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> SearchResults:
        """Get one page of the repositories that match a search (repoSearch)."""
        return self._call(
            _repo_search,
            q=q,
            topic=topic,
            include_desc=include_desc,
            uid=uid,
            priority_owner_id=priority_owner_id,
            team_id=team_id,
            starred_by=starred_by,
            private=private,
            is_private=is_private,
            template=template,
            archived=archived,
            mode=mode,
            exclusive=exclusive,
            sort=sort,
            order=order,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        *,
        q: Optional[StrictStr] = None,
        topic: Optional[StrictBool] = None,
        include_desc: Optional[StrictBool] = None,
        uid: Optional[StrictInt] = None,
        priority_owner_id: Optional[StrictInt] = None,
        team_id: Optional[StrictInt] = None,
        starred_by: Optional[StrictInt] = None,
        private: Optional[StrictBool] = None,
        is_private: Optional[StrictBool] = None,
        template: Optional[StrictBool] = None,
        archived: Optional[StrictBool] = None,
        mode: Optional[StrictStr] = None,
        exclusive: Optional[StrictBool] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_search,
            q=q,
            topic=topic,
            include_desc=include_desc,
            uid=uid,
            priority_owner_id=priority_owner_id,
            team_id=team_id,
            starred_by=starred_by,
            private=private,
            is_private=is_private,
            template=template,
            archived=archived,
            mode=mode,
            exclusive=exclusive,
            sort=sort,
            order=order,
            page=page,
            limit=limit,
        )

    @checked
    def get_signing_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> str:
        """Get the GPG key a repository signs commits with (repoSigningKey)."""
        return self._call(
            _repo_signing_key,
            owner=owner,
            repo=repo,
        )

    @checked
    def get_ssh_signing_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> str:
        """Get the SSH key a repository signs commits with (repoSigningKeySSH)."""
        return self._call(
            _repo_signing_key_ssh,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[TrackedTime]:
        """List one page of the time tracked on a repository (repoTrackedTimes)."""
        return self._call(
            _repo_tracked_times,
            owner=owner,
            repo=repo,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.TrackedTime]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_tracked_times,
            owner=owner,
            repo=repo,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def transfer(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[TransferRepoOption, Mapping[str, Any]],
    ) -> Repository:
        """Start transferring a repository to a new owner (repoTransfer)."""
        return self._call(
            _repo_transfer,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def update_avatar(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[UpdateRepoAvatarOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Set a repository's avatar (repoUpdateAvatar)."""
        return self._call(
            _repo_update_avatar,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def replace_topics(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[RepoTopicOptions, Mapping[str, Any]]] = None,
    ) -> None:
        """Replace a repository's topics (repoUpdateTopics)."""
        return self._call(
            _repo_update_topics,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def validate_issue_config(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> IssueConfigValidation:
        """Check a repository's issue template configuration (repoValidateIssueConfig)."""
        return self._call(
            _repo_validate_issue_config,
            owner=owner,
            repo=repo,
        )

    @checked
    def search_topics(
        self,
        *,
        q: StrictStr,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> TopicListResponse:
        """Get one page of the topics that match a keyword (topicSearch)."""
        return self._call(
            _topic_search,
            q=q,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search_topics(
        self,
        *,
        q: StrictStr,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.TopicResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _topic_search,
            q=q,
            page=page,
            limit=limit,
        )


class AsyncReposApi(AsyncResource):
    @checked
    async def accept_transfer(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Accept a repository transfer (acceptRepoTransfer)."""
        return await self._call(
            _accept_repo_transfer,
            owner=owner,
            repo=repo,
        )

    @checked
    async def fork(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateForkOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Fork a repository (createFork)."""
        return await self._call(
            _create_fork,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def generate(
        self,
        template_owner: StrictStr,
        template_repo: StrictStr,
        body: Optional[Union[GenerateRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Create a repository from a template repository (generateRepo)."""
        return await self._call(
            _generate_repo,
            template_owner=template_owner,
            template_repo=template_repo,
            _body=body,
        )

    @checked
    async def list_forks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of a repository's forks (listForks)."""
        return await self._call(
            _list_forks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_forks(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_forks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def reject_transfer(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Reject a repository transfer (rejectRepoTransfer)."""
        return await self._call(
            _reject_repo_transfer,
            owner=owner,
            repo=repo,
        )

    @checked
    async def add_collaborator(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
        body: Optional[Union[AddCollaboratorOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Add a collaborator, or change a collaborator's permission (repoAddCollaborator)."""
        return await self._call(
            _repo_add_collaborator,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
            _body=body,
        )

    @checked
    async def add_push_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreatePushMirrorOption, Mapping[str, Any]]] = None,
    ) -> PushMirror:
        """Add a push mirror (repoAddPushMirror)."""
        return await self._call(
            _repo_add_push_mirror,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def add_team(
        self,
        owner: StrictStr,
        repo: StrictStr,
        team: StrictStr,
    ) -> None:
        """Give a team access to a repository (repoAddTeam)."""
        return await self._call(
            _repo_add_team,
            owner=owner,
            repo=repo,
            team=team,
        )

    @checked
    async def add_topic(
        self,
        owner: StrictStr,
        repo: StrictStr,
        topic: StrictStr,
    ) -> None:
        """Add a topic to a repository (repoAddTopic)."""
        return await self._call(
            _repo_add_topic,
            owner=owner,
            repo=repo,
            topic=topic,
        )

    @checked
    async def check_assignee(
        self,
        owner: StrictStr,
        repo: StrictStr,
        assignee: StrictStr,
    ) -> None:
        """Check whether a user can be assigned issues and pull requests (repoCheckAssignee)."""
        return await self._call(
            _repo_check_assignee,
            owner=owner,
            repo=repo,
            assignee=assignee,
        )

    @checked
    async def check_collaborator(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
    ) -> None:
        """Check whether a user is a collaborator (repoCheckCollaborator)."""
        return await self._call(
            _repo_check_collaborator,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
        )

    @checked
    async def check_team(
        self,
        owner: StrictStr,
        repo: StrictStr,
        team: StrictStr,
    ) -> Team:
        """Check whether a team has access to a repository (repoCheckTeam)."""
        return await self._call(
            _repo_check_team,
            owner=owner,
            repo=repo,
            team=team,
        )

    @checked
    async def create_deploy_token(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateDeployKeyTokenOption, Mapping[str, Any]]] = None,
    ) -> DeployKey:
        """Create a deploy token, for Git over HTTPS (repoCreateDeployToken)."""
        return await self._call(
            _repo_create_deploy_token,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def add_deploy_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateKeyOption, Mapping[str, Any]]] = None,
    ) -> DeployKey:
        """Add a deploy key (repoCreateKey)."""
        return await self._call(
            _repo_create_key,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Delete a repository (repoDelete)."""
        return await self._call(
            _repo_delete,
            owner=owner,
            repo=repo,
        )

    @checked
    async def delete_avatar(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Remove a repository's avatar (repoDeleteAvatar)."""
        return await self._call(
            _repo_delete_avatar,
            owner=owner,
            repo=repo,
        )

    @checked
    async def remove_collaborator(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
    ) -> None:
        """Remove a collaborator (repoDeleteCollaborator)."""
        return await self._call(
            _repo_delete_collaborator,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
        )

    @checked
    async def delete_deploy_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a deploy key (repoDeleteKey)."""
        return await self._call(
            _repo_delete_key,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def delete_push_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> None:
        """Delete a push mirror (repoDeletePushMirror)."""
        return await self._call(
            _repo_delete_push_mirror,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    async def remove_team(
        self,
        owner: StrictStr,
        repo: StrictStr,
        team: StrictStr,
    ) -> None:
        """Remove a team's access to a repository (repoDeleteTeam)."""
        return await self._call(
            _repo_delete_team,
            owner=owner,
            repo=repo,
            team=team,
        )

    @checked
    async def remove_topic(
        self,
        owner: StrictStr,
        repo: StrictStr,
        topic: StrictStr,
    ) -> None:
        """Remove a topic from a repository (repoDeleteTopic)."""
        return await self._call(
            _repo_delete_topic,
            owner=owner,
            repo=repo,
            topic=topic,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[EditRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Change a repository's settings (repoEdit)."""
        return await self._call(
            _repo_edit,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Get a repository (repoGet)."""
        return await self._call(
            _repo_get,
            owner=owner,
            repo=repo,
        )

    @checked
    async def download_archive(
        self,
        owner: StrictStr,
        repo: StrictStr,
        archive: StrictStr,
        *,
        path: Optional[List[StrictStr]] = None,
    ) -> AsyncDownload:
        """Download an archive of a repository at a ref (repoGetArchive). Close the download, or read it in an `async with` block."""
        return await self._download(
            _repo_get_archive,
            owner=owner,
            repo=repo,
            archive=archive,
            path=path,
        )

    @checked
    async def list_assignees(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[User]:
        """List the users that issues and pull requests can be assigned to (repoGetAssignees)."""
        return await self._call(
            _repo_get_assignees,
            owner=owner,
            repo=repo,
        )

    @checked
    async def get_by_id(
        self,
        id: StrictInt,
    ) -> Repository:
        """Get a repository by its ID (repoGetByID)."""
        return await self._call(
            _repo_get_by_id,
            id=id,
        )

    @checked
    async def get_issue_config(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> IssueConfig:
        """Get a repository's issue template configuration (repoGetIssueConfig)."""
        return await self._call(
            _repo_get_issue_config,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_issue_templates(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[IssueTemplate]:
        """List a repository's issue templates (repoGetIssueTemplates)."""
        return await self._call(
            _repo_get_issue_templates,
            owner=owner,
            repo=repo,
        )

    @checked
    async def get_deploy_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> DeployKey:
        """Get a deploy key (repoGetKey)."""
        return await self._call(
            _repo_get_key,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def get_languages(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Dict[str, int]:
        """Get how many bytes of each language a repository holds (repoGetLanguages)."""
        return await self._call(
            _repo_get_languages,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_licenses(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[str]:
        """List the licenses found in a repository (repoGetLicenses)."""
        return await self._call(
            _repo_get_licenses,
            owner=owner,
            repo=repo,
        )

    @checked
    async def get_push_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> PushMirror:
        """Get a push mirror by its remote name (repoGetPushMirrorByRemoteName)."""
        return await self._call(
            _repo_get_push_mirror_by_remote_name,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    async def get_permissions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        collaborator: StrictStr,
    ) -> RepoCollaboratorPermission:
        """Get a user's permissions on a repository (repoGetRepoPermissions)."""
        return await self._call(
            _repo_get_repo_permissions,
            owner=owner,
            repo=repo,
            collaborator=collaborator,
        )

    @checked
    async def list_reviewers(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[User]:
        """List the users that can be asked to review pull requests (repoGetReviewers)."""
        return await self._call(
            _repo_get_reviewers,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_activity_feeds(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of a repository's activity (repoListActivityFeeds)."""
        return await self._call(
            _repo_list_activity_feeds,
            owner=owner,
            repo=repo,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_activity_feeds,
            owner=owner,
            repo=repo,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    async def list_collaborators(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of a repository's collaborators (repoListCollaborators)."""
        return await self._call(
            _repo_list_collaborators,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_collaborators(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_collaborators,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def list_deploy_keys(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        key_id: Optional[StrictInt] = None,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[DeployKey]:
        """List one page of a repository's deploy keys (repoListKeys)."""
        return await self._call(
            _repo_list_keys,
            owner=owner,
            repo=repo,
            key_id=key_id,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def iter_deploy_keys(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        key_id: Optional[StrictInt] = None,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.DeployKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_keys,
            owner=owner,
            repo=repo,
            key_id=key_id,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    async def list_push_mirrors(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PushMirror]:
        """List one page of a repository's push mirrors (repoListPushMirrors)."""
        return await self._call(
            _repo_list_push_mirrors,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_push_mirrors(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.PushMirror]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_push_mirrors,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def list_stargazers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users who starred a repository (repoListStargazers)."""
        return await self._call(
            _repo_list_stargazers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_stargazers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_stargazers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def list_watchers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users who watch a repository (repoListSubscribers)."""
        return await self._call(
            _repo_list_subscribers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_watchers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_subscribers,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def list_teams(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[Team]:
        """List the teams that have access to a repository (repoListTeams)."""
        return await self._call(
            _repo_list_teams,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_topics(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> TopicName:
        """List a page of a repository's topics (repoListTopics)."""
        return await self._call(
            _repo_list_topics,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def merge_upstream(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[MergeUpstreamRequest, Mapping[str, Any]]] = None,
    ) -> MergeUpstreamResponse:
        """Merge a branch from a fork's upstream repository (repoMergeUpstream)."""
        return await self._call(
            _repo_merge_upstream,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def migrate(
        self,
        body: Optional[Union[MigrateRepoOptions, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Migrate a repository from another service (repoMigrate)."""
        return await self._call(
            _repo_migrate,
            _body=body,
        )

    @checked
    async def sync_mirror(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Sync a mirror repository from its remote (repoMirrorSync)."""
        return await self._call(
            _repo_mirror_sync,
            owner=owner,
            repo=repo,
        )

    @checked
    async def check_pin_allowed(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> NewIssuePinsAllowed:
        """Check whether more issues and pull requests can be pinned (repoNewPinAllowed)."""
        return await self._call(
            _repo_new_pin_allowed,
            owner=owner,
            repo=repo,
        )

    @checked
    async def sync_push_mirrors(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Push a repository to all of its push mirrors (repoPushMirrorSync)."""
        return await self._call(
            _repo_push_mirror_sync,
            owner=owner,
            repo=repo,
        )

    @checked
    async def search(
        self,
        *,
        q: Optional[StrictStr] = None,
        topic: Optional[StrictBool] = None,
        include_desc: Optional[StrictBool] = None,
        uid: Optional[StrictInt] = None,
        priority_owner_id: Optional[StrictInt] = None,
        team_id: Optional[StrictInt] = None,
        starred_by: Optional[StrictInt] = None,
        private: Optional[StrictBool] = None,
        is_private: Optional[StrictBool] = None,
        template: Optional[StrictBool] = None,
        archived: Optional[StrictBool] = None,
        mode: Optional[StrictStr] = None,
        exclusive: Optional[StrictBool] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> SearchResults:
        """Get one page of the repositories that match a search (repoSearch)."""
        return await self._call(
            _repo_search,
            q=q,
            topic=topic,
            include_desc=include_desc,
            uid=uid,
            priority_owner_id=priority_owner_id,
            team_id=team_id,
            starred_by=starred_by,
            private=private,
            is_private=is_private,
            template=template,
            archived=archived,
            mode=mode,
            exclusive=exclusive,
            sort=sort,
            order=order,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        *,
        q: Optional[StrictStr] = None,
        topic: Optional[StrictBool] = None,
        include_desc: Optional[StrictBool] = None,
        uid: Optional[StrictInt] = None,
        priority_owner_id: Optional[StrictInt] = None,
        team_id: Optional[StrictInt] = None,
        starred_by: Optional[StrictInt] = None,
        private: Optional[StrictBool] = None,
        is_private: Optional[StrictBool] = None,
        template: Optional[StrictBool] = None,
        archived: Optional[StrictBool] = None,
        mode: Optional[StrictStr] = None,
        exclusive: Optional[StrictBool] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_search,
            q=q,
            topic=topic,
            include_desc=include_desc,
            uid=uid,
            priority_owner_id=priority_owner_id,
            team_id=team_id,
            starred_by=starred_by,
            private=private,
            is_private=is_private,
            template=template,
            archived=archived,
            mode=mode,
            exclusive=exclusive,
            sort=sort,
            order=order,
            page=page,
            limit=limit,
        )

    @checked
    async def get_signing_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> str:
        """Get the GPG key a repository signs commits with (repoSigningKey)."""
        return await self._call(
            _repo_signing_key,
            owner=owner,
            repo=repo,
        )

    @checked
    async def get_ssh_signing_key(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> str:
        """Get the SSH key a repository signs commits with (repoSigningKeySSH)."""
        return await self._call(
            _repo_signing_key_ssh,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[TrackedTime]:
        """List one page of the time tracked on a repository (repoTrackedTimes)."""
        return await self._call(
            _repo_tracked_times,
            owner=owner,
            repo=repo,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.TrackedTime]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_tracked_times,
            owner=owner,
            repo=repo,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    async def transfer(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[TransferRepoOption, Mapping[str, Any]],
    ) -> Repository:
        """Start transferring a repository to a new owner (repoTransfer)."""
        return await self._call(
            _repo_transfer,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def update_avatar(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[UpdateRepoAvatarOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Set a repository's avatar (repoUpdateAvatar)."""
        return await self._call(
            _repo_update_avatar,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def replace_topics(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[RepoTopicOptions, Mapping[str, Any]]] = None,
    ) -> None:
        """Replace a repository's topics (repoUpdateTopics)."""
        return await self._call(
            _repo_update_topics,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def validate_issue_config(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> IssueConfigValidation:
        """Check a repository's issue template configuration (repoValidateIssueConfig)."""
        return await self._call(
            _repo_validate_issue_config,
            owner=owner,
            repo=repo,
        )

    @checked
    async def search_topics(
        self,
        *,
        q: StrictStr,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> TopicListResponse:
        """Get one page of the topics that match a keyword (topicSearch)."""
        return await self._call(
            _topic_search,
            q=q,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search_topics(
        self,
        *,
        q: StrictStr,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.TopicResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _topic_search,
            q=q,
            page=page,
            limit=limit,
        )
