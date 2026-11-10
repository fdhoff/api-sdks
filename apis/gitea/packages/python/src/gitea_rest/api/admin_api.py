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
from gitea_rest.models.action_runner import ActionRunner
from gitea_rest.models.action_runners_response import ActionRunnersResponse
from gitea_rest.models.action_workflow_jobs_response import ActionWorkflowJobsResponse
from gitea_rest.models.action_workflow_runs_response import ActionWorkflowRunsResponse
from gitea_rest.models.badge import Badge
from gitea_rest.models.create_hook_option import CreateHookOption
from gitea_rest.models.create_key_option import CreateKeyOption
from gitea_rest.models.create_org_option import CreateOrgOption
from gitea_rest.models.create_repo_option import CreateRepoOption
from gitea_rest.models.create_user_option import CreateUserOption
from gitea_rest.models.cron import Cron
from gitea_rest.models.edit_action_runner_option import EditActionRunnerOption
from gitea_rest.models.edit_hook_option import EditHookOption
from gitea_rest.models.edit_user_option import EditUserOption
from gitea_rest.models.email import Email
from gitea_rest.models.hook import Hook
from gitea_rest.models.organization import Organization
from gitea_rest.models.package import Package
from gitea_rest.models.public_key import PublicKey
from gitea_rest.models.rename_user_option import RenameUserOption
from gitea_rest.models.repository import Repository
from gitea_rest.models.user import User
from gitea_rest.models.user_badge_option import UserBadgeOption

_admin_add_user_badges: Operation[None] = Operation(
    id="adminAddUserBadges",
    method="POST",
    path="/admin/users/{username}/badges",
    resource="admin",
    name="add_user_badges",
    params=(Param("username", "username", "path"),),
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
_admin_adopt_repository: Operation[None] = Operation(
    id="adminAdoptRepository",
    method="POST",
    path="/admin/unadopted/{owner}/{repo}",
    resource="admin",
    name="adopt_repo",
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
_admin_create_hook: Operation[Hook] = Operation(
    id="adminCreateHook",
    method="POST",
    path="/admin/hooks",
    resource="admin",
    name="create_hook",
    params=(),
    response=Hook,
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
_admin_create_org: Operation[Organization] = Operation(
    id="adminCreateOrg",
    method="POST",
    path="/admin/users/{username}/orgs",
    resource="admin",
    name="create_org",
    params=(Param("username", "username", "path"),),
    response=Organization,
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
_admin_create_public_key: Operation[PublicKey] = Operation(
    id="adminCreatePublicKey",
    method="POST",
    path="/admin/users/{username}/keys",
    resource="admin",
    name="add_user_key",
    params=(Param("username", "username", "path"),),
    response=PublicKey,
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
_admin_create_repo: Operation[Repository] = Operation(
    id="adminCreateRepo",
    method="POST",
    path="/admin/users/{username}/repos",
    resource="admin",
    name="create_repo",
    params=(Param("username", "username", "path"),),
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
_admin_create_runner_registration_token: Operation[None] = Operation(
    id="adminCreateRunnerRegistrationToken",
    method="POST",
    path="/admin/actions/runners/registration-token",
    resource="admin",
    name="create_runner_registration_token",
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
_admin_create_user: Operation[User] = Operation(
    id="adminCreateUser",
    method="POST",
    path="/admin/users",
    resource="admin",
    name="create_user",
    params=(),
    response=User,
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
_admin_cron_list: Operation[List[Cron]] = Operation(
    id="adminCronList",
    method="GET",
    path="/admin/cron",
    resource="admin",
    name="list_cron_tasks",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Cron],
    returns_json=True,
    iterator="iter_cron_tasks",
    item=_models.Cron,
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
_admin_cron_run: Operation[None] = Operation(
    id="adminCronRun",
    method="POST",
    path="/admin/cron/{task}",
    resource="admin",
    name="run_cron_task",
    params=(Param("task", "task", "path"),),
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
_admin_delete_hook: Operation[None] = Operation(
    id="adminDeleteHook",
    method="DELETE",
    path="/admin/hooks/{id}",
    resource="admin",
    name="delete_hook",
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
_admin_delete_unadopted_repository: Operation[None] = Operation(
    id="adminDeleteUnadoptedRepository",
    method="DELETE",
    path="/admin/unadopted/{owner}/{repo}",
    resource="admin",
    name="delete_unadopted_repo",
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
_admin_delete_user: Operation[None] = Operation(
    id="adminDeleteUser",
    method="DELETE",
    path="/admin/users/{username}",
    resource="admin",
    name="delete_user",
    params=(
        Param("username", "username", "path"),
        Param("purge", "purge", "query"),
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
_admin_delete_user_badges: Operation[None] = Operation(
    id="adminDeleteUserBadges",
    method="DELETE",
    path="/admin/users/{username}/badges",
    resource="admin",
    name="delete_user_badges",
    params=(Param("username", "username", "path"),),
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
_admin_delete_user_public_key: Operation[None] = Operation(
    id="adminDeleteUserPublicKey",
    method="DELETE",
    path="/admin/users/{username}/keys/{id}",
    resource="admin",
    name="delete_user_key",
    params=(
        Param("username", "username", "path"),
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
_admin_edit_hook: Operation[Hook] = Operation(
    id="adminEditHook",
    method="PATCH",
    path="/admin/hooks/{id}",
    resource="admin",
    name="update_hook",
    params=(Param("id", "id", "path"),),
    response=Hook,
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
_admin_edit_user: Operation[User] = Operation(
    id="adminEditUser",
    method="PATCH",
    path="/admin/users/{username}",
    resource="admin",
    name="update_user",
    params=(Param("username", "username", "path"),),
    response=User,
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
_admin_get_all_emails: Operation[List[Email]] = Operation(
    id="adminGetAllEmails",
    method="GET",
    path="/admin/emails",
    resource="admin",
    name="list_emails",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Email],
    returns_json=True,
    iterator="iter_emails",
    item=_models.Email,
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
_admin_get_all_orgs: Operation[List[Organization]] = Operation(
    id="adminGetAllOrgs",
    method="GET",
    path="/admin/orgs",
    resource="admin",
    name="list_orgs",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Organization],
    returns_json=True,
    iterator="iter_orgs",
    item=_models.Organization,
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
_admin_get_hook: Operation[Hook] = Operation(
    id="adminGetHook",
    method="GET",
    path="/admin/hooks/{id}",
    resource="admin",
    name="get_hook",
    params=(Param("id", "id", "path"),),
    response=Hook,
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
_admin_list_hooks: Operation[List[Hook]] = Operation(
    id="adminListHooks",
    method="GET",
    path="/admin/hooks",
    resource="admin",
    name="list_hooks",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("type", "type", "query"),
    ),
    response=List[Hook],
    returns_json=True,
    iterator="iter_hooks",
    item=_models.Hook,
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
_admin_list_packages: Operation[List[Package]] = Operation(
    id="adminListPackages",
    method="GET",
    path="/admin/packages",
    resource="admin",
    name="list_packages",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("type", "type", "query"),
        Param("q", "q", "query"),
    ),
    response=List[Package],
    returns_json=True,
    iterator="iter_packages",
    item=_models.Package,
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
_admin_list_user_badges: Operation[List[Badge]] = Operation(
    id="adminListUserBadges",
    method="GET",
    path="/admin/users/{username}/badges",
    resource="admin",
    name="list_user_badges",
    params=(Param("username", "username", "path"),),
    response=List[Badge],
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
_admin_rename_user: Operation[None] = Operation(
    id="adminRenameUser",
    method="POST",
    path="/admin/users/{username}/rename",
    resource="admin",
    name="rename_user",
    params=(Param("username", "username", "path"),),
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
_admin_search_emails: Operation[List[Email]] = Operation(
    id="adminSearchEmails",
    method="GET",
    path="/admin/emails/search",
    resource="admin",
    name="search_emails",
    params=(
        Param("q", "q", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Email],
    returns_json=True,
    iterator="iter_search_emails",
    item=_models.Email,
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
_admin_search_users: Operation[List[User]] = Operation(
    id="adminSearchUsers",
    method="GET",
    path="/admin/users",
    resource="admin",
    name="search_users",
    params=(
        Param("source_id", "source_id", "query"),
        Param("login_name", "login_name", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
        Param("q", "q", "query"),
        Param("visibility", "visibility", "query"),
        Param("is_active", "is_active", "query"),
        Param("is_admin", "is_admin", "query"),
        Param("is_restricted", "is_restricted", "query"),
        Param("is_2fa_enabled", "is_2fa_enabled", "query"),
        Param("is_prohibit_login", "is_prohibit_login", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_search_users",
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
_admin_unadopted_list: Operation[List[str]] = Operation(
    id="adminUnadoptedList",
    method="GET",
    path="/admin/unadopted",
    resource="admin",
    name="list_unadopted_repos",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("query", "query", "query"),
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
_delete_admin_runner: Operation[None] = Operation(
    id="deleteAdminRunner",
    method="DELETE",
    path="/admin/actions/runners/{runner_id}",
    resource="admin",
    name="delete_runner",
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
_get_admin_runner: Operation[ActionRunner] = Operation(
    id="getAdminRunner",
    method="GET",
    path="/admin/actions/runners/{runner_id}",
    resource="admin",
    name="get_runner",
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
_get_admin_runners: Operation[ActionRunnersResponse] = Operation(
    id="getAdminRunners",
    method="GET",
    path="/admin/actions/runners",
    resource="admin",
    name="list_runners",
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
_list_admin_workflow_jobs: Operation[ActionWorkflowJobsResponse] = Operation(
    id="listAdminWorkflowJobs",
    method="GET",
    path="/admin/actions/jobs",
    resource="admin",
    name="list_jobs",
    params=(
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
_list_admin_workflow_runs: Operation[ActionWorkflowRunsResponse] = Operation(
    id="listAdminWorkflowRuns",
    method="GET",
    path="/admin/actions/runs",
    resource="admin",
    name="list_runs",
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
_update_admin_runner: Operation[ActionRunner] = Operation(
    id="updateAdminRunner",
    method="PATCH",
    path="/admin/actions/runners/{runner_id}",
    resource="admin",
    name="update_runner",
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

OPERATIONS = (
    _admin_add_user_badges,
    _admin_adopt_repository,
    _admin_create_hook,
    _admin_create_org,
    _admin_create_public_key,
    _admin_create_repo,
    _admin_create_runner_registration_token,
    _admin_create_user,
    _admin_cron_list,
    _admin_cron_run,
    _admin_delete_hook,
    _admin_delete_unadopted_repository,
    _admin_delete_user,
    _admin_delete_user_badges,
    _admin_delete_user_public_key,
    _admin_edit_hook,
    _admin_edit_user,
    _admin_get_all_emails,
    _admin_get_all_orgs,
    _admin_get_hook,
    _admin_list_hooks,
    _admin_list_packages,
    _admin_list_user_badges,
    _admin_rename_user,
    _admin_search_emails,
    _admin_search_users,
    _admin_unadopted_list,
    _delete_admin_runner,
    _get_admin_runner,
    _get_admin_runners,
    _list_admin_workflow_jobs,
    _list_admin_workflow_runs,
    _update_admin_runner,
)


class AdminApi(Resource):
    @checked
    def add_user_badges(
        self,
        username: StrictStr,
        body: Optional[Union[UserBadgeOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Add badges to a user (adminAddUserBadges)."""
        return self._call(
            _admin_add_user_badges,
            username=username,
            _body=body,
        )

    @checked
    def adopt_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Adopt an unadopted repository (adminAdoptRepository)."""
        return self._call(
            _admin_adopt_repository,
            owner=owner,
            repo=repo,
        )

    @checked
    def create_hook(
        self,
        body: Union[CreateHookOption, Mapping[str, Any]],
    ) -> Hook:
        """Create a system or default webhook (adminCreateHook)."""
        return self._call(
            _admin_create_hook,
            _body=body,
        )

    @checked
    def create_org(
        self,
        username: StrictStr,
        body: Union[CreateOrgOption, Mapping[str, Any]],
    ) -> Organization:
        """Create an organization owned by a user (adminCreateOrg)."""
        return self._call(
            _admin_create_org,
            username=username,
            _body=body,
        )

    @checked
    def add_user_key(
        self,
        username: StrictStr,
        body: Optional[Union[CreateKeyOption, Mapping[str, Any]]] = None,
    ) -> PublicKey:
        """Add an SSH key to a user (adminCreatePublicKey)."""
        return self._call(
            _admin_create_public_key,
            username=username,
            _body=body,
        )

    @checked
    def create_repo(
        self,
        username: StrictStr,
        body: Union[CreateRepoOption, Mapping[str, Any]],
    ) -> Repository:
        """Create a repository owned by a user (adminCreateRepo)."""
        return self._call(
            _admin_create_repo,
            username=username,
            _body=body,
        )

    @checked
    def create_runner_registration_token(
        self,
    ) -> None:
        """Create a token that registers a global runner (adminCreateRunnerRegistrationToken)."""
        return self._call(
            _admin_create_runner_registration_token,
        )

    @checked
    def create_user(
        self,
        body: Optional[Union[CreateUserOption, Mapping[str, Any]]] = None,
    ) -> User:
        """Create a user (adminCreateUser)."""
        return self._call(
            _admin_create_user,
            _body=body,
        )

    @checked
    def list_cron_tasks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Cron]:
        """List one page of the instance's cron tasks (adminCronList)."""
        return self._call(
            _admin_cron_list,
            page=page,
            limit=limit,
        )

    @checked
    def iter_cron_tasks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Cron]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_cron_list,
            page=page,
            limit=limit,
        )

    @checked
    def run_cron_task(
        self,
        task: StrictStr,
    ) -> None:
        """Run a cron task now (adminCronRun)."""
        return self._call(
            _admin_cron_run,
            task=task,
        )

    @checked
    def delete_hook(
        self,
        id: StrictInt,
    ) -> None:
        """Delete a system or default webhook (adminDeleteHook)."""
        return self._call(
            _admin_delete_hook,
            id=id,
        )

    @checked
    def delete_unadopted_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Delete an unadopted repository's files (adminDeleteUnadoptedRepository)."""
        return self._call(
            _admin_delete_unadopted_repository,
            owner=owner,
            repo=repo,
        )

    @checked
    def delete_user(
        self,
        username: StrictStr,
        *,
        purge: Optional[StrictBool] = None,
    ) -> None:
        """Delete a user (adminDeleteUser)."""
        return self._call(
            _admin_delete_user,
            username=username,
            purge=purge,
        )

    @checked
    def delete_user_badges(
        self,
        username: StrictStr,
        body: Optional[Union[UserBadgeOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove badges from a user (adminDeleteUserBadges)."""
        return self._call(
            _admin_delete_user_badges,
            username=username,
            _body=body,
        )

    @checked
    def delete_user_key(
        self,
        username: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a user's SSH key (adminDeleteUserPublicKey)."""
        return self._call(
            _admin_delete_user_public_key,
            username=username,
            id=id,
        )

    @checked
    def update_hook(
        self,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change a system or default webhook (adminEditHook)."""
        return self._call(
            _admin_edit_hook,
            id=id,
            _body=body,
        )

    @checked
    def update_user(
        self,
        username: StrictStr,
        body: Optional[Union[EditUserOption, Mapping[str, Any]]] = None,
    ) -> User:
        """Change a user (adminEditUser)."""
        return self._call(
            _admin_edit_user,
            username=username,
            _body=body,
        )

    @checked
    def list_emails(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Email]:
        """List one page of every user's email addresses (adminGetAllEmails)."""
        return self._call(
            _admin_get_all_emails,
            page=page,
            limit=limit,
        )

    @checked
    def iter_emails(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Email]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_get_all_emails,
            page=page,
            limit=limit,
        )

    @checked
    def list_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of every organization (adminGetAllOrgs)."""
        return self._call(
            _admin_get_all_orgs,
            page=page,
            limit=limit,
        )

    @checked
    def iter_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_get_all_orgs,
            page=page,
            limit=limit,
        )

    @checked
    def get_hook(
        self,
        id: StrictInt,
    ) -> Hook:
        """Get a system or default webhook (adminGetHook)."""
        return self._call(
            _admin_get_hook,
            id=id,
        )

    @checked
    def list_hooks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
    ) -> List[Hook]:
        """List one page of the instance's system and default webhooks (adminListHooks)."""
        return self._call(
            _admin_list_hooks,
            page=page,
            limit=limit,
            type=type,
        )

    @checked
    def iter_hooks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
    ) -> Iterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_list_hooks,
            page=page,
            limit=limit,
            type=type,
        )

    @checked
    def list_packages(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> List[Package]:
        """List one page of every package (adminListPackages)."""
        return self._call(
            _admin_list_packages,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    def iter_packages(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> Iterator[_models.Package]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_list_packages,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    def list_user_badges(
        self,
        username: StrictStr,
    ) -> List[Badge]:
        """List a user's badges (adminListUserBadges)."""
        return self._call(
            _admin_list_user_badges,
            username=username,
        )

    @checked
    def rename_user(
        self,
        username: StrictStr,
        body: Union[RenameUserOption, Mapping[str, Any]],
    ) -> None:
        """Rename a user (adminRenameUser)."""
        return self._call(
            _admin_rename_user,
            username=username,
            _body=body,
        )

    @checked
    def search_emails(
        self,
        *,
        q: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Email]:
        """Get one page of the email addresses that match a search (adminSearchEmails)."""
        return self._call(
            _admin_search_emails,
            q=q,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search_emails(
        self,
        *,
        q: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Email]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_search_emails,
            q=q,
            page=page,
            limit=limit,
        )

    @checked
    def search_users(
        self,
        *,
        source_id: Optional[StrictInt] = None,
        login_name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        visibility: Optional[StrictStr] = None,
        is_active: Optional[StrictBool] = None,
        is_admin: Optional[StrictBool] = None,
        is_restricted: Optional[StrictBool] = None,
        is_2fa_enabled: Optional[StrictBool] = None,
        is_prohibit_login: Optional[StrictBool] = None,
    ) -> List[User]:
        """Get one page of the users on the instance that match a search (adminSearchUsers)."""
        return self._call(
            _admin_search_users,
            source_id=source_id,
            login_name=login_name,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            q=q,
            visibility=visibility,
            is_active=is_active,
            is_admin=is_admin,
            is_restricted=is_restricted,
            is_2fa_enabled=is_2fa_enabled,
            is_prohibit_login=is_prohibit_login,
        )

    @checked
    def iter_search_users(
        self,
        *,
        source_id: Optional[StrictInt] = None,
        login_name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        visibility: Optional[StrictStr] = None,
        is_active: Optional[StrictBool] = None,
        is_admin: Optional[StrictBool] = None,
        is_restricted: Optional[StrictBool] = None,
        is_2fa_enabled: Optional[StrictBool] = None,
        is_prohibit_login: Optional[StrictBool] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_search_users,
            source_id=source_id,
            login_name=login_name,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            q=q,
            visibility=visibility,
            is_active=is_active,
            is_admin=is_admin,
            is_restricted=is_restricted,
            is_2fa_enabled=is_2fa_enabled,
            is_prohibit_login=is_prohibit_login,
        )

    @checked
    def list_unadopted_repos(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        query: Optional[StrictStr] = None,
    ) -> List[str]:
        """List a page of the repositories on disk that no user or organization owns (adminUnadoptedList)."""
        return self._call(
            _admin_unadopted_list,
            page=page,
            limit=limit,
            query=query,
        )

    @checked
    def delete_runner(
        self,
        runner_id: StrictStr,
    ) -> None:
        """Delete a global runner (deleteAdminRunner)."""
        return self._call(
            _delete_admin_runner,
            runner_id=runner_id,
        )

    @checked
    def get_runner(
        self,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get a global runner (getAdminRunner)."""
        return self._call(
            _get_admin_runner,
            runner_id=runner_id,
        )

    @checked
    def list_runners(
        self,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List the instance's global runners (getAdminRunners)."""
        return self._call(
            _get_admin_runners,
            disabled=disabled,
        )

    @checked
    def list_jobs(
        self,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of every workflow job on the instance (listAdminWorkflowJobs)."""
        return self._call(
            _list_admin_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_jobs(
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
            _list_admin_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def list_runs(
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
        """List one page of every workflow run on the instance (listAdminWorkflowRuns)."""
        return self._call(
            _list_admin_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs(
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
            _list_admin_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def update_runner(
        self,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change a global runner (updateAdminRunner)."""
        return self._call(
            _update_admin_runner,
            runner_id=runner_id,
            _body=body,
        )


class AsyncAdminApi(AsyncResource):
    @checked
    async def add_user_badges(
        self,
        username: StrictStr,
        body: Optional[Union[UserBadgeOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Add badges to a user (adminAddUserBadges)."""
        return await self._call(
            _admin_add_user_badges,
            username=username,
            _body=body,
        )

    @checked
    async def adopt_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Adopt an unadopted repository (adminAdoptRepository)."""
        return await self._call(
            _admin_adopt_repository,
            owner=owner,
            repo=repo,
        )

    @checked
    async def create_hook(
        self,
        body: Union[CreateHookOption, Mapping[str, Any]],
    ) -> Hook:
        """Create a system or default webhook (adminCreateHook)."""
        return await self._call(
            _admin_create_hook,
            _body=body,
        )

    @checked
    async def create_org(
        self,
        username: StrictStr,
        body: Union[CreateOrgOption, Mapping[str, Any]],
    ) -> Organization:
        """Create an organization owned by a user (adminCreateOrg)."""
        return await self._call(
            _admin_create_org,
            username=username,
            _body=body,
        )

    @checked
    async def add_user_key(
        self,
        username: StrictStr,
        body: Optional[Union[CreateKeyOption, Mapping[str, Any]]] = None,
    ) -> PublicKey:
        """Add an SSH key to a user (adminCreatePublicKey)."""
        return await self._call(
            _admin_create_public_key,
            username=username,
            _body=body,
        )

    @checked
    async def create_repo(
        self,
        username: StrictStr,
        body: Union[CreateRepoOption, Mapping[str, Any]],
    ) -> Repository:
        """Create a repository owned by a user (adminCreateRepo)."""
        return await self._call(
            _admin_create_repo,
            username=username,
            _body=body,
        )

    @checked
    async def create_runner_registration_token(
        self,
    ) -> None:
        """Create a token that registers a global runner (adminCreateRunnerRegistrationToken)."""
        return await self._call(
            _admin_create_runner_registration_token,
        )

    @checked
    async def create_user(
        self,
        body: Optional[Union[CreateUserOption, Mapping[str, Any]]] = None,
    ) -> User:
        """Create a user (adminCreateUser)."""
        return await self._call(
            _admin_create_user,
            _body=body,
        )

    @checked
    async def list_cron_tasks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Cron]:
        """List one page of the instance's cron tasks (adminCronList)."""
        return await self._call(
            _admin_cron_list,
            page=page,
            limit=limit,
        )

    @checked
    def iter_cron_tasks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Cron]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_cron_list,
            page=page,
            limit=limit,
        )

    @checked
    async def run_cron_task(
        self,
        task: StrictStr,
    ) -> None:
        """Run a cron task now (adminCronRun)."""
        return await self._call(
            _admin_cron_run,
            task=task,
        )

    @checked
    async def delete_hook(
        self,
        id: StrictInt,
    ) -> None:
        """Delete a system or default webhook (adminDeleteHook)."""
        return await self._call(
            _admin_delete_hook,
            id=id,
        )

    @checked
    async def delete_unadopted_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Delete an unadopted repository's files (adminDeleteUnadoptedRepository)."""
        return await self._call(
            _admin_delete_unadopted_repository,
            owner=owner,
            repo=repo,
        )

    @checked
    async def delete_user(
        self,
        username: StrictStr,
        *,
        purge: Optional[StrictBool] = None,
    ) -> None:
        """Delete a user (adminDeleteUser)."""
        return await self._call(
            _admin_delete_user,
            username=username,
            purge=purge,
        )

    @checked
    async def delete_user_badges(
        self,
        username: StrictStr,
        body: Optional[Union[UserBadgeOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove badges from a user (adminDeleteUserBadges)."""
        return await self._call(
            _admin_delete_user_badges,
            username=username,
            _body=body,
        )

    @checked
    async def delete_user_key(
        self,
        username: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a user's SSH key (adminDeleteUserPublicKey)."""
        return await self._call(
            _admin_delete_user_public_key,
            username=username,
            id=id,
        )

    @checked
    async def update_hook(
        self,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change a system or default webhook (adminEditHook)."""
        return await self._call(
            _admin_edit_hook,
            id=id,
            _body=body,
        )

    @checked
    async def update_user(
        self,
        username: StrictStr,
        body: Optional[Union[EditUserOption, Mapping[str, Any]]] = None,
    ) -> User:
        """Change a user (adminEditUser)."""
        return await self._call(
            _admin_edit_user,
            username=username,
            _body=body,
        )

    @checked
    async def list_emails(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Email]:
        """List one page of every user's email addresses (adminGetAllEmails)."""
        return await self._call(
            _admin_get_all_emails,
            page=page,
            limit=limit,
        )

    @checked
    def iter_emails(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Email]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_get_all_emails,
            page=page,
            limit=limit,
        )

    @checked
    async def list_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of every organization (adminGetAllOrgs)."""
        return await self._call(
            _admin_get_all_orgs,
            page=page,
            limit=limit,
        )

    @checked
    def iter_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_get_all_orgs,
            page=page,
            limit=limit,
        )

    @checked
    async def get_hook(
        self,
        id: StrictInt,
    ) -> Hook:
        """Get a system or default webhook (adminGetHook)."""
        return await self._call(
            _admin_get_hook,
            id=id,
        )

    @checked
    async def list_hooks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
    ) -> List[Hook]:
        """List one page of the instance's system and default webhooks (adminListHooks)."""
        return await self._call(
            _admin_list_hooks,
            page=page,
            limit=limit,
            type=type,
        )

    @checked
    def iter_hooks(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_list_hooks,
            page=page,
            limit=limit,
            type=type,
        )

    @checked
    async def list_packages(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> List[Package]:
        """List one page of every package (adminListPackages)."""
        return await self._call(
            _admin_list_packages,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    def iter_packages(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Package]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_list_packages,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    async def list_user_badges(
        self,
        username: StrictStr,
    ) -> List[Badge]:
        """List a user's badges (adminListUserBadges)."""
        return await self._call(
            _admin_list_user_badges,
            username=username,
        )

    @checked
    async def rename_user(
        self,
        username: StrictStr,
        body: Union[RenameUserOption, Mapping[str, Any]],
    ) -> None:
        """Rename a user (adminRenameUser)."""
        return await self._call(
            _admin_rename_user,
            username=username,
            _body=body,
        )

    @checked
    async def search_emails(
        self,
        *,
        q: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Email]:
        """Get one page of the email addresses that match a search (adminSearchEmails)."""
        return await self._call(
            _admin_search_emails,
            q=q,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search_emails(
        self,
        *,
        q: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Email]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_search_emails,
            q=q,
            page=page,
            limit=limit,
        )

    @checked
    async def search_users(
        self,
        *,
        source_id: Optional[StrictInt] = None,
        login_name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        visibility: Optional[StrictStr] = None,
        is_active: Optional[StrictBool] = None,
        is_admin: Optional[StrictBool] = None,
        is_restricted: Optional[StrictBool] = None,
        is_2fa_enabled: Optional[StrictBool] = None,
        is_prohibit_login: Optional[StrictBool] = None,
    ) -> List[User]:
        """Get one page of the users on the instance that match a search (adminSearchUsers)."""
        return await self._call(
            _admin_search_users,
            source_id=source_id,
            login_name=login_name,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            q=q,
            visibility=visibility,
            is_active=is_active,
            is_admin=is_admin,
            is_restricted=is_restricted,
            is_2fa_enabled=is_2fa_enabled,
            is_prohibit_login=is_prohibit_login,
        )

    @checked
    def iter_search_users(
        self,
        *,
        source_id: Optional[StrictInt] = None,
        login_name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        visibility: Optional[StrictStr] = None,
        is_active: Optional[StrictBool] = None,
        is_admin: Optional[StrictBool] = None,
        is_restricted: Optional[StrictBool] = None,
        is_2fa_enabled: Optional[StrictBool] = None,
        is_prohibit_login: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _admin_search_users,
            source_id=source_id,
            login_name=login_name,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            q=q,
            visibility=visibility,
            is_active=is_active,
            is_admin=is_admin,
            is_restricted=is_restricted,
            is_2fa_enabled=is_2fa_enabled,
            is_prohibit_login=is_prohibit_login,
        )

    @checked
    async def list_unadopted_repos(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        query: Optional[StrictStr] = None,
    ) -> List[str]:
        """List a page of the repositories on disk that no user or organization owns (adminUnadoptedList)."""
        return await self._call(
            _admin_unadopted_list,
            page=page,
            limit=limit,
            query=query,
        )

    @checked
    async def delete_runner(
        self,
        runner_id: StrictStr,
    ) -> None:
        """Delete a global runner (deleteAdminRunner)."""
        return await self._call(
            _delete_admin_runner,
            runner_id=runner_id,
        )

    @checked
    async def get_runner(
        self,
        runner_id: StrictStr,
    ) -> ActionRunner:
        """Get a global runner (getAdminRunner)."""
        return await self._call(
            _get_admin_runner,
            runner_id=runner_id,
        )

    @checked
    async def list_runners(
        self,
        *,
        disabled: Optional[StrictBool] = None,
    ) -> ActionRunnersResponse:
        """List the instance's global runners (getAdminRunners)."""
        return await self._call(
            _get_admin_runners,
            disabled=disabled,
        )

    @checked
    async def list_jobs(
        self,
        *,
        status: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> ActionWorkflowJobsResponse:
        """List one page of every workflow job on the instance (listAdminWorkflowJobs)."""
        return await self._call(
            _list_admin_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    def iter_jobs(
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
            _list_admin_workflow_jobs,
            status=status,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
        )

    @checked
    async def list_runs(
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
        """List one page of every workflow run on the instance (listAdminWorkflowRuns)."""
        return await self._call(
            _list_admin_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    def iter_runs(
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
            _list_admin_workflow_runs,
            event=event,
            branch=branch,
            status=status,
            actor=actor,
            head_sha=head_sha,
            page=page,
            limit=limit,
        )

    @checked
    async def update_runner(
        self,
        runner_id: StrictStr,
        body: Optional[Union[EditActionRunnerOption, Mapping[str, Any]]] = None,
    ) -> ActionRunner:
        """Change a global runner (updateAdminRunner)."""
        return await self._call(
            _update_admin_runner,
            runner_id=runner_id,
            _body=body,
        )
