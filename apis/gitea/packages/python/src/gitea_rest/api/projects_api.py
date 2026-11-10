# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictInt, StrictStr

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
from gitea_rest.models.create_project_column_option import CreateProjectColumnOption
from gitea_rest.models.create_project_option import CreateProjectOption
from gitea_rest.models.edit_project_column_option import EditProjectColumnOption
from gitea_rest.models.edit_project_option import EditProjectOption
from gitea_rest.models.issue import Issue
from gitea_rest.models.move_project_columns_option import MoveProjectColumnsOption
from gitea_rest.models.move_project_issue_option import MoveProjectIssueOption
from gitea_rest.models.project import Project
from gitea_rest.models.project_column import ProjectColumn

_org_add_issue_to_project_column: Operation[None] = Operation(
    id="orgAddIssueToProjectColumn",
    method="POST",
    path="/orgs/{org}/projects/{id}/columns/{column_id}/issues/{issue_id}",
    resource="projects",
    name="add_issue_to_column_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_org_create_project: Operation[Project] = Operation(
    id="orgCreateProject",
    method="POST",
    path="/orgs/{org}/projects",
    resource="projects",
    name="create_for_org",
    params=(Param("org", "org", "path"),),
    response=Project,
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
_org_create_project_column: Operation[ProjectColumn] = Operation(
    id="orgCreateProjectColumn",
    method="POST",
    path="/orgs/{org}/projects/{id}/columns",
    resource="projects",
    name="create_column_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
    ),
    response=ProjectColumn,
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
_org_delete_project: Operation[None] = Operation(
    id="orgDeleteProject",
    method="DELETE",
    path="/orgs/{org}/projects/{id}",
    resource="projects",
    name="delete_for_org",
    params=(
        Param("org", "org", "path"),
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
_org_delete_project_column: Operation[None] = Operation(
    id="orgDeleteProjectColumn",
    method="DELETE",
    path="/orgs/{org}/projects/{id}/columns/{column_id}",
    resource="projects",
    name="delete_column_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
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
_org_edit_project: Operation[Project] = Operation(
    id="orgEditProject",
    method="PATCH",
    path="/orgs/{org}/projects/{id}",
    resource="projects",
    name="update_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
    ),
    response=Project,
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
_org_edit_project_column: Operation[ProjectColumn] = Operation(
    id="orgEditProjectColumn",
    method="PATCH",
    path="/orgs/{org}/projects/{id}/columns/{column_id}",
    resource="projects",
    name="update_column_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
    ),
    response=ProjectColumn,
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
_org_get_project: Operation[Project] = Operation(
    id="orgGetProject",
    method="GET",
    path="/orgs/{org}/projects/{id}",
    resource="projects",
    name="get_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
    ),
    response=Project,
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
_org_get_project_column: Operation[ProjectColumn] = Operation(
    id="orgGetProjectColumn",
    method="GET",
    path="/orgs/{org}/projects/{id}/columns/{column_id}",
    resource="projects",
    name="get_column_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
    ),
    response=ProjectColumn,
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
_org_list_project_column_issues: Operation[List[Issue]] = Operation(
    id="orgListProjectColumnIssues",
    method="GET",
    path="/orgs/{org}/projects/{id}/columns/{column_id}/issues",
    resource="projects",
    name="list_column_issues_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Issue],
    returns_json=True,
    iterator="iter_column_issues_for_org",
    item=_models.Issue,
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
_org_list_project_columns: Operation[List[ProjectColumn]] = Operation(
    id="orgListProjectColumns",
    method="GET",
    path="/orgs/{org}/projects/{id}/columns",
    resource="projects",
    name="list_columns_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[ProjectColumn],
    returns_json=True,
    iterator="iter_columns_for_org",
    item=_models.ProjectColumn,
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
_org_list_projects: Operation[List[Project]] = Operation(
    id="orgListProjects",
    method="GET",
    path="/orgs/{org}/projects",
    resource="projects",
    name="list_for_org",
    params=(
        Param("org", "org", "path"),
        Param("state", "state", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Project],
    returns_json=True,
    iterator="iter_for_org",
    item=_models.Project,
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
_org_move_project_columns: Operation[None] = Operation(
    id="orgMoveProjectColumns",
    method="POST",
    path="/orgs/{org}/projects/{id}/columns/move",
    resource="projects",
    name="reorder_columns_for_org",
    params=(
        Param("org", "org", "path"),
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
_org_move_project_issue: Operation[None] = Operation(
    id="orgMoveProjectIssue",
    method="POST",
    path="/orgs/{org}/projects/{id}/issues/{issue_id}/move",
    resource="projects",
    name="move_issue_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_org_remove_issue_from_project_column: Operation[None] = Operation(
    id="orgRemoveIssueFromProjectColumn",
    method="DELETE",
    path="/orgs/{org}/projects/{id}/columns/{column_id}/issues/{issue_id}",
    resource="projects",
    name="remove_issue_from_column_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_org_set_default_project_column: Operation[None] = Operation(
    id="orgSetDefaultProjectColumn",
    method="POST",
    path="/orgs/{org}/projects/{id}/columns/{column_id}/default",
    resource="projects",
    name="set_default_column_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
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
_repo_add_issue_to_project_column: Operation[None] = Operation(
    id="repoAddIssueToProjectColumn",
    method="POST",
    path="/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues/{issue_id}",
    resource="projects",
    name="add_issue_to_column",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_repo_create_project: Operation[Project] = Operation(
    id="repoCreateProject",
    method="POST",
    path="/repos/{owner}/{repo}/projects",
    resource="projects",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Project,
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
_repo_create_project_column: Operation[ProjectColumn] = Operation(
    id="repoCreateProjectColumn",
    method="POST",
    path="/repos/{owner}/{repo}/projects/{id}/columns",
    resource="projects",
    name="create_column",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=ProjectColumn,
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
_repo_delete_project: Operation[None] = Operation(
    id="repoDeleteProject",
    method="DELETE",
    path="/repos/{owner}/{repo}/projects/{id}",
    resource="projects",
    name="delete",
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
_repo_delete_project_column: Operation[None] = Operation(
    id="repoDeleteProjectColumn",
    method="DELETE",
    path="/repos/{owner}/{repo}/projects/{id}/columns/{column_id}",
    resource="projects",
    name="delete_column",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
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
_repo_edit_project: Operation[Project] = Operation(
    id="repoEditProject",
    method="PATCH",
    path="/repos/{owner}/{repo}/projects/{id}",
    resource="projects",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Project,
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
_repo_edit_project_column: Operation[ProjectColumn] = Operation(
    id="repoEditProjectColumn",
    method="PATCH",
    path="/repos/{owner}/{repo}/projects/{id}/columns/{column_id}",
    resource="projects",
    name="update_column",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
    ),
    response=ProjectColumn,
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
_repo_get_project: Operation[Project] = Operation(
    id="repoGetProject",
    method="GET",
    path="/repos/{owner}/{repo}/projects/{id}",
    resource="projects",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Project,
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
_repo_get_project_column: Operation[ProjectColumn] = Operation(
    id="repoGetProjectColumn",
    method="GET",
    path="/repos/{owner}/{repo}/projects/{id}/columns/{column_id}",
    resource="projects",
    name="get_column",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
    ),
    response=ProjectColumn,
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
_repo_list_project_column_issues: Operation[List[Issue]] = Operation(
    id="repoListProjectColumnIssues",
    method="GET",
    path="/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues",
    resource="projects",
    name="list_column_issues",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Issue],
    returns_json=True,
    iterator="iter_column_issues",
    item=_models.Issue,
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
_repo_list_project_columns: Operation[List[ProjectColumn]] = Operation(
    id="repoListProjectColumns",
    method="GET",
    path="/repos/{owner}/{repo}/projects/{id}/columns",
    resource="projects",
    name="list_columns",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[ProjectColumn],
    returns_json=True,
    iterator="iter_columns",
    item=_models.ProjectColumn,
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
_repo_list_projects: Operation[List[Project]] = Operation(
    id="repoListProjects",
    method="GET",
    path="/repos/{owner}/{repo}/projects",
    resource="projects",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("state", "state", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Project],
    returns_json=True,
    iterator="iter",
    item=_models.Project,
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
_repo_move_project_columns: Operation[None] = Operation(
    id="repoMoveProjectColumns",
    method="POST",
    path="/repos/{owner}/{repo}/projects/{id}/columns/move",
    resource="projects",
    name="reorder_columns",
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
_repo_move_project_issue: Operation[None] = Operation(
    id="repoMoveProjectIssue",
    method="POST",
    path="/repos/{owner}/{repo}/projects/{id}/issues/{issue_id}/move",
    resource="projects",
    name="move_issue",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_repo_remove_issue_from_project_column: Operation[None] = Operation(
    id="repoRemoveIssueFromProjectColumn",
    method="DELETE",
    path="/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues/{issue_id}",
    resource="projects",
    name="remove_issue_from_column",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_repo_set_default_project_column: Operation[None] = Operation(
    id="repoSetDefaultProjectColumn",
    method="POST",
    path="/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/default",
    resource="projects",
    name="set_default_column",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
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
_user_current_add_issue_to_project_column: Operation[None] = Operation(
    id="userCurrentAddIssueToProjectColumn",
    method="POST",
    path="/user/projects/{id}/columns/{column_id}/issues/{issue_id}",
    resource="projects",
    name="add_issue_to_column_for_user",
    params=(
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_user_current_create_project: Operation[Project] = Operation(
    id="userCurrentCreateProject",
    method="POST",
    path="/user/projects",
    resource="projects",
    name="create_for_user",
    params=(),
    response=Project,
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
_user_current_create_project_column: Operation[ProjectColumn] = Operation(
    id="userCurrentCreateProjectColumn",
    method="POST",
    path="/user/projects/{id}/columns",
    resource="projects",
    name="create_column_for_user",
    params=(Param("id", "id", "path"),),
    response=ProjectColumn,
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
_user_current_delete_project: Operation[None] = Operation(
    id="userCurrentDeleteProject",
    method="DELETE",
    path="/user/projects/{id}",
    resource="projects",
    name="delete_for_user",
    params=(Param("id", "id", "path"),),
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
_user_current_delete_project_column: Operation[None] = Operation(
    id="userCurrentDeleteProjectColumn",
    method="DELETE",
    path="/user/projects/{id}/columns/{column_id}",
    resource="projects",
    name="delete_column_for_user",
    params=(
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
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
_user_current_edit_project: Operation[Project] = Operation(
    id="userCurrentEditProject",
    method="PATCH",
    path="/user/projects/{id}",
    resource="projects",
    name="update_for_user",
    params=(Param("id", "id", "path"),),
    response=Project,
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
_user_current_edit_project_column: Operation[ProjectColumn] = Operation(
    id="userCurrentEditProjectColumn",
    method="PATCH",
    path="/user/projects/{id}/columns/{column_id}",
    resource="projects",
    name="update_column_for_user",
    params=(
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
    ),
    response=ProjectColumn,
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
_user_current_get_project: Operation[Project] = Operation(
    id="userCurrentGetProject",
    method="GET",
    path="/user/projects/{id}",
    resource="projects",
    name="get_for_user",
    params=(Param("id", "id", "path"),),
    response=Project,
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
_user_current_get_project_column: Operation[ProjectColumn] = Operation(
    id="userCurrentGetProjectColumn",
    method="GET",
    path="/user/projects/{id}/columns/{column_id}",
    resource="projects",
    name="get_column_for_user",
    params=(
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
    ),
    response=ProjectColumn,
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
_user_current_list_project_column_issues: Operation[List[Issue]] = Operation(
    id="userCurrentListProjectColumnIssues",
    method="GET",
    path="/user/projects/{id}/columns/{column_id}/issues",
    resource="projects",
    name="list_column_issues_for_user",
    params=(
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Issue],
    returns_json=True,
    iterator="iter_column_issues_for_user",
    item=_models.Issue,
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
_user_current_list_project_columns: Operation[List[ProjectColumn]] = Operation(
    id="userCurrentListProjectColumns",
    method="GET",
    path="/user/projects/{id}/columns",
    resource="projects",
    name="list_columns_for_user",
    params=(
        Param("id", "id", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[ProjectColumn],
    returns_json=True,
    iterator="iter_columns_for_user",
    item=_models.ProjectColumn,
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
_user_current_list_projects: Operation[List[Project]] = Operation(
    id="userCurrentListProjects",
    method="GET",
    path="/user/projects",
    resource="projects",
    name="list_for_user",
    params=(
        Param("state", "state", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Project],
    returns_json=True,
    iterator="iter_for_user",
    item=_models.Project,
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
_user_current_move_project_columns: Operation[None] = Operation(
    id="userCurrentMoveProjectColumns",
    method="POST",
    path="/user/projects/{id}/columns/move",
    resource="projects",
    name="reorder_columns_for_user",
    params=(Param("id", "id", "path"),),
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
_user_current_move_project_issue: Operation[None] = Operation(
    id="userCurrentMoveProjectIssue",
    method="POST",
    path="/user/projects/{id}/issues/{issue_id}/move",
    resource="projects",
    name="move_issue_for_user",
    params=(
        Param("id", "id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_user_current_remove_issue_from_project_column: Operation[None] = Operation(
    id="userCurrentRemoveIssueFromProjectColumn",
    method="DELETE",
    path="/user/projects/{id}/columns/{column_id}/issues/{issue_id}",
    resource="projects",
    name="remove_issue_from_column_for_user",
    params=(
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
        Param("issue_id", "issue_id", "path"),
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
_user_current_set_default_project_column: Operation[None] = Operation(
    id="userCurrentSetDefaultProjectColumn",
    method="POST",
    path="/user/projects/{id}/columns/{column_id}/default",
    resource="projects",
    name="set_default_column_for_user",
    params=(
        Param("id", "id", "path"),
        Param("column_id", "column_id", "path"),
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

OPERATIONS = (
    _org_add_issue_to_project_column,
    _org_create_project,
    _org_create_project_column,
    _org_delete_project,
    _org_delete_project_column,
    _org_edit_project,
    _org_edit_project_column,
    _org_get_project,
    _org_get_project_column,
    _org_list_project_column_issues,
    _org_list_project_columns,
    _org_list_projects,
    _org_move_project_columns,
    _org_move_project_issue,
    _org_remove_issue_from_project_column,
    _org_set_default_project_column,
    _repo_add_issue_to_project_column,
    _repo_create_project,
    _repo_create_project_column,
    _repo_delete_project,
    _repo_delete_project_column,
    _repo_edit_project,
    _repo_edit_project_column,
    _repo_get_project,
    _repo_get_project_column,
    _repo_list_project_column_issues,
    _repo_list_project_columns,
    _repo_list_projects,
    _repo_move_project_columns,
    _repo_move_project_issue,
    _repo_remove_issue_from_project_column,
    _repo_set_default_project_column,
    _user_current_add_issue_to_project_column,
    _user_current_create_project,
    _user_current_create_project_column,
    _user_current_delete_project,
    _user_current_delete_project_column,
    _user_current_edit_project,
    _user_current_edit_project_column,
    _user_current_get_project,
    _user_current_get_project_column,
    _user_current_list_project_column_issues,
    _user_current_list_project_columns,
    _user_current_list_projects,
    _user_current_move_project_columns,
    _user_current_move_project_issue,
    _user_current_remove_issue_from_project_column,
    _user_current_set_default_project_column,
)


class ProjectsApi(Resource):
    @checked
    def add_issue_to_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Add an issue to an organization project column (orgAddIssueToProjectColumn)."""
        return self._call(
            _org_add_issue_to_project_column,
            org=org,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    def create_for_org(
        self,
        org: StrictStr,
        body: Optional[Union[CreateProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Create an organization project (orgCreateProject)."""
        return self._call(
            _org_create_project,
            org=org,
            _body=body,
        )

    @checked
    def create_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[CreateProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Add a column to an organization project (orgCreateProjectColumn)."""
        return self._call(
            _org_create_project_column,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    def delete_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an organization project (orgDeleteProject)."""
        return self._call(
            _org_delete_project,
            org=org,
            id=id,
        )

    @checked
    def delete_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Delete an organization project column (orgDeleteProjectColumn)."""
        return self._call(
            _org_delete_project_column,
            org=org,
            id=id,
            column_id=column_id,
        )

    @checked
    def update_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Change an organization project (orgEditProject)."""
        return self._call(
            _org_edit_project,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    def update_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        body: Optional[Union[EditProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Change an organization project column (orgEditProjectColumn)."""
        return self._call(
            _org_edit_project_column,
            org=org,
            id=id,
            column_id=column_id,
            _body=body,
        )

    @checked
    def get_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> Project:
        """Get an organization project (orgGetProject)."""
        return self._call(
            _org_get_project,
            org=org,
            id=id,
        )

    @checked
    def get_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> ProjectColumn:
        """Get an organization project column (orgGetProjectColumn)."""
        return self._call(
            _org_get_project_column,
            org=org,
            id=id,
            column_id=column_id,
        )

    @checked
    def list_column_issues_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues in an organization project column (orgListProjectColumnIssues)."""
        return self._call(
            _org_list_project_column_issues,
            org=org,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_column_issues_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_project_column_issues,
            org=org,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def list_columns_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ProjectColumn]:
        """List one page of an organization project's columns (orgListProjectColumns)."""
        return self._call(
            _org_list_project_columns,
            org=org,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_columns_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ProjectColumn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_project_columns,
            org=org,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def list_for_org(
        self,
        org: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of an organization's projects (orgListProjects)."""
        return self._call(
            _org_list_projects,
            org=org,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_org(
        self,
        org: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_projects,
            org=org,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def reorder_columns_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[MoveProjectColumnsOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Reorder an organization project's columns (orgMoveProjectColumns)."""
        return self._call(
            _org_move_project_columns,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    def move_issue_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        issue_id: StrictInt,
        body: Optional[Union[MoveProjectIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Move an issue within an organization project (orgMoveProjectIssue)."""
        return self._call(
            _org_move_project_issue,
            org=org,
            id=id,
            issue_id=issue_id,
            _body=body,
        )

    @checked
    def remove_issue_from_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Remove an issue from an organization project column (orgRemoveIssueFromProjectColumn)."""
        return self._call(
            _org_remove_issue_from_project_column,
            org=org,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    def set_default_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Make a column the default of an organization project (orgSetDefaultProjectColumn)."""
        return self._call(
            _org_set_default_project_column,
            org=org,
            id=id,
            column_id=column_id,
        )

    @checked
    def add_issue_to_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Add an issue to a repository project column (repoAddIssueToProjectColumn)."""
        return self._call(
            _repo_add_issue_to_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Create a repository project (repoCreateProject)."""
        return self._call(
            _repo_create_project,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def create_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[CreateProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Add a column to a repository project (repoCreateProjectColumn)."""
        return self._call(
            _repo_create_project_column,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a repository project (repoDeleteProject)."""
        return self._call(
            _repo_delete_project,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def delete_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Delete a repository project column (repoDeleteProjectColumn)."""
        return self._call(
            _repo_delete_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Change a repository project (repoEditProject)."""
        return self._call(
            _repo_edit_project,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def update_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        body: Optional[Union[EditProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Change a repository project column (repoEditProjectColumn)."""
        return self._call(
            _repo_edit_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            _body=body,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Project:
        """Get a repository project (repoGetProject)."""
        return self._call(
            _repo_get_project,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def get_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> ProjectColumn:
        """Get a repository project column (repoGetProjectColumn)."""
        return self._call(
            _repo_get_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
        )

    @checked
    def list_column_issues(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues in a repository project column (repoListProjectColumnIssues)."""
        return self._call(
            _repo_list_project_column_issues,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_column_issues(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_project_column_issues,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def list_columns(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ProjectColumn]:
        """List one page of a repository project's columns (repoListProjectColumns)."""
        return self._call(
            _repo_list_project_columns,
            owner=owner,
            repo=repo,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_columns(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ProjectColumn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_project_columns,
            owner=owner,
            repo=repo,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of a repository's projects (repoListProjects)."""
        return self._call(
            _repo_list_projects,
            owner=owner,
            repo=repo,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_projects,
            owner=owner,
            repo=repo,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def reorder_columns(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[MoveProjectColumnsOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Reorder a repository project's columns (repoMoveProjectColumns)."""
        return self._call(
            _repo_move_project_columns,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def move_issue(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        issue_id: StrictInt,
        body: Optional[Union[MoveProjectIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Move an issue within a repository project (repoMoveProjectIssue)."""
        return self._call(
            _repo_move_project_issue,
            owner=owner,
            repo=repo,
            id=id,
            issue_id=issue_id,
            _body=body,
        )

    @checked
    def remove_issue_from_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Remove an issue from a repository project column (repoRemoveIssueFromProjectColumn)."""
        return self._call(
            _repo_remove_issue_from_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    def set_default_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Make a column the default of a repository project (repoSetDefaultProjectColumn)."""
        return self._call(
            _repo_set_default_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
        )

    @checked
    def add_issue_to_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Add an issue to a column of one of your projects (userCurrentAddIssueToProjectColumn)."""
        return self._call(
            _user_current_add_issue_to_project_column,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    def create_for_user(
        self,
        body: Optional[Union[CreateProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Create a project of your own (userCurrentCreateProject)."""
        return self._call(
            _user_current_create_project,
            _body=body,
        )

    @checked
    def create_column_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[CreateProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Add a column to one of your projects (userCurrentCreateProjectColumn)."""
        return self._call(
            _user_current_create_project_column,
            id=id,
            _body=body,
        )

    @checked
    def delete_for_user(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your projects (userCurrentDeleteProject)."""
        return self._call(
            _user_current_delete_project,
            id=id,
        )

    @checked
    def delete_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Delete a column of one of your projects (userCurrentDeleteProjectColumn)."""
        return self._call(
            _user_current_delete_project_column,
            id=id,
            column_id=column_id,
        )

    @checked
    def update_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[EditProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Change one of your projects (userCurrentEditProject)."""
        return self._call(
            _user_current_edit_project,
            id=id,
            _body=body,
        )

    @checked
    def update_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        body: Optional[Union[EditProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Change a column of one of your projects (userCurrentEditProjectColumn)."""
        return self._call(
            _user_current_edit_project_column,
            id=id,
            column_id=column_id,
            _body=body,
        )

    @checked
    def get_for_user(
        self,
        id: StrictInt,
    ) -> Project:
        """Get one of your projects (userCurrentGetProject)."""
        return self._call(
            _user_current_get_project,
            id=id,
        )

    @checked
    def get_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
    ) -> ProjectColumn:
        """Get a column of one of your projects (userCurrentGetProjectColumn)."""
        return self._call(
            _user_current_get_project_column,
            id=id,
            column_id=column_id,
        )

    @checked
    def list_column_issues_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues in a column of one of your projects (userCurrentListProjectColumnIssues)."""
        return self._call(
            _user_current_list_project_column_issues,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_column_issues_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_project_column_issues,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def list_columns_for_user(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ProjectColumn]:
        """List one page of the columns of one of your projects (userCurrentListProjectColumns)."""
        return self._call(
            _user_current_list_project_columns,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_columns_for_user(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ProjectColumn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_project_columns,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def list_for_user(
        self,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of your own projects (userCurrentListProjects)."""
        return self._call(
            _user_current_list_projects,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_user(
        self,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_projects,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def reorder_columns_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[MoveProjectColumnsOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Reorder the columns of one of your projects (userCurrentMoveProjectColumns)."""
        return self._call(
            _user_current_move_project_columns,
            id=id,
            _body=body,
        )

    @checked
    def move_issue_for_user(
        self,
        id: StrictInt,
        issue_id: StrictInt,
        body: Optional[Union[MoveProjectIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Move an issue within one of your projects (userCurrentMoveProjectIssue)."""
        return self._call(
            _user_current_move_project_issue,
            id=id,
            issue_id=issue_id,
            _body=body,
        )

    @checked
    def remove_issue_from_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Remove an issue from a column of one of your projects (userCurrentRemoveIssueFromProjectColumn)."""
        return self._call(
            _user_current_remove_issue_from_project_column,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    def set_default_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Make a column the default of one of your projects (userCurrentSetDefaultProjectColumn)."""
        return self._call(
            _user_current_set_default_project_column,
            id=id,
            column_id=column_id,
        )


class AsyncProjectsApi(AsyncResource):
    @checked
    async def add_issue_to_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Add an issue to an organization project column (orgAddIssueToProjectColumn)."""
        return await self._call(
            _org_add_issue_to_project_column,
            org=org,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    async def create_for_org(
        self,
        org: StrictStr,
        body: Optional[Union[CreateProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Create an organization project (orgCreateProject)."""
        return await self._call(
            _org_create_project,
            org=org,
            _body=body,
        )

    @checked
    async def create_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[CreateProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Add a column to an organization project (orgCreateProjectColumn)."""
        return await self._call(
            _org_create_project_column,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    async def delete_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an organization project (orgDeleteProject)."""
        return await self._call(
            _org_delete_project,
            org=org,
            id=id,
        )

    @checked
    async def delete_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Delete an organization project column (orgDeleteProjectColumn)."""
        return await self._call(
            _org_delete_project_column,
            org=org,
            id=id,
            column_id=column_id,
        )

    @checked
    async def update_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Change an organization project (orgEditProject)."""
        return await self._call(
            _org_edit_project,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    async def update_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        body: Optional[Union[EditProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Change an organization project column (orgEditProjectColumn)."""
        return await self._call(
            _org_edit_project_column,
            org=org,
            id=id,
            column_id=column_id,
            _body=body,
        )

    @checked
    async def get_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> Project:
        """Get an organization project (orgGetProject)."""
        return await self._call(
            _org_get_project,
            org=org,
            id=id,
        )

    @checked
    async def get_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> ProjectColumn:
        """Get an organization project column (orgGetProjectColumn)."""
        return await self._call(
            _org_get_project_column,
            org=org,
            id=id,
            column_id=column_id,
        )

    @checked
    async def list_column_issues_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues in an organization project column (orgListProjectColumnIssues)."""
        return await self._call(
            _org_list_project_column_issues,
            org=org,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_column_issues_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_project_column_issues,
            org=org,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    async def list_columns_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ProjectColumn]:
        """List one page of an organization project's columns (orgListProjectColumns)."""
        return await self._call(
            _org_list_project_columns,
            org=org,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_columns_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ProjectColumn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_project_columns,
            org=org,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    async def list_for_org(
        self,
        org: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of an organization's projects (orgListProjects)."""
        return await self._call(
            _org_list_projects,
            org=org,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_org(
        self,
        org: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_projects,
            org=org,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    async def reorder_columns_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[MoveProjectColumnsOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Reorder an organization project's columns (orgMoveProjectColumns)."""
        return await self._call(
            _org_move_project_columns,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    async def move_issue_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        issue_id: StrictInt,
        body: Optional[Union[MoveProjectIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Move an issue within an organization project (orgMoveProjectIssue)."""
        return await self._call(
            _org_move_project_issue,
            org=org,
            id=id,
            issue_id=issue_id,
            _body=body,
        )

    @checked
    async def remove_issue_from_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Remove an issue from an organization project column (orgRemoveIssueFromProjectColumn)."""
        return await self._call(
            _org_remove_issue_from_project_column,
            org=org,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    async def set_default_column_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Make a column the default of an organization project (orgSetDefaultProjectColumn)."""
        return await self._call(
            _org_set_default_project_column,
            org=org,
            id=id,
            column_id=column_id,
        )

    @checked
    async def add_issue_to_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Add an issue to a repository project column (repoAddIssueToProjectColumn)."""
        return await self._call(
            _repo_add_issue_to_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Create a repository project (repoCreateProject)."""
        return await self._call(
            _repo_create_project,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def create_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[CreateProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Add a column to a repository project (repoCreateProjectColumn)."""
        return await self._call(
            _repo_create_project_column,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a repository project (repoDeleteProject)."""
        return await self._call(
            _repo_delete_project,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def delete_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Delete a repository project column (repoDeleteProjectColumn)."""
        return await self._call(
            _repo_delete_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Change a repository project (repoEditProject)."""
        return await self._call(
            _repo_edit_project,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def update_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        body: Optional[Union[EditProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Change a repository project column (repoEditProjectColumn)."""
        return await self._call(
            _repo_edit_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            _body=body,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Project:
        """Get a repository project (repoGetProject)."""
        return await self._call(
            _repo_get_project,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def get_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> ProjectColumn:
        """Get a repository project column (repoGetProjectColumn)."""
        return await self._call(
            _repo_get_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
        )

    @checked
    async def list_column_issues(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues in a repository project column (repoListProjectColumnIssues)."""
        return await self._call(
            _repo_list_project_column_issues,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_column_issues(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_project_column_issues,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    async def list_columns(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ProjectColumn]:
        """List one page of a repository project's columns (repoListProjectColumns)."""
        return await self._call(
            _repo_list_project_columns,
            owner=owner,
            repo=repo,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_columns(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ProjectColumn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_project_columns,
            owner=owner,
            repo=repo,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    async def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of a repository's projects (repoListProjects)."""
        return await self._call(
            _repo_list_projects,
            owner=owner,
            repo=repo,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_projects,
            owner=owner,
            repo=repo,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    async def reorder_columns(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[MoveProjectColumnsOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Reorder a repository project's columns (repoMoveProjectColumns)."""
        return await self._call(
            _repo_move_project_columns,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def move_issue(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        issue_id: StrictInt,
        body: Optional[Union[MoveProjectIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Move an issue within a repository project (repoMoveProjectIssue)."""
        return await self._call(
            _repo_move_project_issue,
            owner=owner,
            repo=repo,
            id=id,
            issue_id=issue_id,
            _body=body,
        )

    @checked
    async def remove_issue_from_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Remove an issue from a repository project column (repoRemoveIssueFromProjectColumn)."""
        return await self._call(
            _repo_remove_issue_from_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    async def set_default_column(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Make a column the default of a repository project (repoSetDefaultProjectColumn)."""
        return await self._call(
            _repo_set_default_project_column,
            owner=owner,
            repo=repo,
            id=id,
            column_id=column_id,
        )

    @checked
    async def add_issue_to_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Add an issue to a column of one of your projects (userCurrentAddIssueToProjectColumn)."""
        return await self._call(
            _user_current_add_issue_to_project_column,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    async def create_for_user(
        self,
        body: Optional[Union[CreateProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Create a project of your own (userCurrentCreateProject)."""
        return await self._call(
            _user_current_create_project,
            _body=body,
        )

    @checked
    async def create_column_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[CreateProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Add a column to one of your projects (userCurrentCreateProjectColumn)."""
        return await self._call(
            _user_current_create_project_column,
            id=id,
            _body=body,
        )

    @checked
    async def delete_for_user(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your projects (userCurrentDeleteProject)."""
        return await self._call(
            _user_current_delete_project,
            id=id,
        )

    @checked
    async def delete_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Delete a column of one of your projects (userCurrentDeleteProjectColumn)."""
        return await self._call(
            _user_current_delete_project_column,
            id=id,
            column_id=column_id,
        )

    @checked
    async def update_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[EditProjectOption, Mapping[str, Any]]] = None,
    ) -> Project:
        """Change one of your projects (userCurrentEditProject)."""
        return await self._call(
            _user_current_edit_project,
            id=id,
            _body=body,
        )

    @checked
    async def update_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        body: Optional[Union[EditProjectColumnOption, Mapping[str, Any]]] = None,
    ) -> ProjectColumn:
        """Change a column of one of your projects (userCurrentEditProjectColumn)."""
        return await self._call(
            _user_current_edit_project_column,
            id=id,
            column_id=column_id,
            _body=body,
        )

    @checked
    async def get_for_user(
        self,
        id: StrictInt,
    ) -> Project:
        """Get one of your projects (userCurrentGetProject)."""
        return await self._call(
            _user_current_get_project,
            id=id,
        )

    @checked
    async def get_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
    ) -> ProjectColumn:
        """Get a column of one of your projects (userCurrentGetProjectColumn)."""
        return await self._call(
            _user_current_get_project_column,
            id=id,
            column_id=column_id,
        )

    @checked
    async def list_column_issues_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues in a column of one of your projects (userCurrentListProjectColumnIssues)."""
        return await self._call(
            _user_current_list_project_column_issues,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_column_issues_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_project_column_issues,
            id=id,
            column_id=column_id,
            page=page,
            limit=limit,
        )

    @checked
    async def list_columns_for_user(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ProjectColumn]:
        """List one page of the columns of one of your projects (userCurrentListProjectColumns)."""
        return await self._call(
            _user_current_list_project_columns,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_columns_for_user(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ProjectColumn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_project_columns,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    async def list_for_user(
        self,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of your own projects (userCurrentListProjects)."""
        return await self._call(
            _user_current_list_projects,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_user(
        self,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_projects,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    async def reorder_columns_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[MoveProjectColumnsOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Reorder the columns of one of your projects (userCurrentMoveProjectColumns)."""
        return await self._call(
            _user_current_move_project_columns,
            id=id,
            _body=body,
        )

    @checked
    async def move_issue_for_user(
        self,
        id: StrictInt,
        issue_id: StrictInt,
        body: Optional[Union[MoveProjectIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Move an issue within one of your projects (userCurrentMoveProjectIssue)."""
        return await self._call(
            _user_current_move_project_issue,
            id=id,
            issue_id=issue_id,
            _body=body,
        )

    @checked
    async def remove_issue_from_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
        issue_id: StrictInt,
    ) -> None:
        """Remove an issue from a column of one of your projects (userCurrentRemoveIssueFromProjectColumn)."""
        return await self._call(
            _user_current_remove_issue_from_project_column,
            id=id,
            column_id=column_id,
            issue_id=issue_id,
        )

    @checked
    async def set_default_column_for_user(
        self,
        id: StrictInt,
        column_id: StrictInt,
    ) -> None:
        """Make a column the default of one of your projects (userCurrentSetDefaultProjectColumn)."""
        return await self._call(
            _user_current_set_default_project_column,
            id=id,
            column_id=column_id,
        )
