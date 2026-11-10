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
from gitea_rest.models.create_hook_option import CreateHookOption
from gitea_rest.models.edit_git_hook_option import EditGitHookOption
from gitea_rest.models.edit_hook_option import EditHookOption
from gitea_rest.models.git_hook import GitHook
from gitea_rest.models.hook import Hook

_org_create_hook: Operation[Hook] = Operation(
    id="orgCreateHook",
    method="POST",
    path="/orgs/{org}/hooks",
    resource="hooks",
    name="create_for_org",
    params=(Param("org", "org", "path"),),
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
_org_delete_hook: Operation[None] = Operation(
    id="orgDeleteHook",
    method="DELETE",
    path="/orgs/{org}/hooks/{id}",
    resource="hooks",
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
_org_edit_hook: Operation[Hook] = Operation(
    id="orgEditHook",
    method="PATCH",
    path="/orgs/{org}/hooks/{id}",
    resource="hooks",
    name="update_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
    ),
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
_org_get_hook: Operation[Hook] = Operation(
    id="orgGetHook",
    method="GET",
    path="/orgs/{org}/hooks/{id}",
    resource="hooks",
    name="get_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
    ),
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
_org_list_hooks: Operation[List[Hook]] = Operation(
    id="orgListHooks",
    method="GET",
    path="/orgs/{org}/hooks",
    resource="hooks",
    name="list_for_org",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Hook],
    returns_json=True,
    iterator="iter_for_org",
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
_repo_create_hook: Operation[Hook] = Operation(
    id="repoCreateHook",
    method="POST",
    path="/repos/{owner}/{repo}/hooks",
    resource="hooks",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
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
_repo_delete_git_hook: Operation[None] = Operation(
    id="repoDeleteGitHook",
    method="DELETE",
    path="/repos/{owner}/{repo}/hooks/git/{id}",
    resource="hooks",
    name="delete_git_hook",
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
_repo_delete_hook: Operation[None] = Operation(
    id="repoDeleteHook",
    method="DELETE",
    path="/repos/{owner}/{repo}/hooks/{id}",
    resource="hooks",
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
_repo_edit_git_hook: Operation[GitHook] = Operation(
    id="repoEditGitHook",
    method="PATCH",
    path="/repos/{owner}/{repo}/hooks/git/{id}",
    resource="hooks",
    name="update_git_hook",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=GitHook,
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
_repo_edit_hook: Operation[Hook] = Operation(
    id="repoEditHook",
    method="PATCH",
    path="/repos/{owner}/{repo}/hooks/{id}",
    resource="hooks",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
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
_repo_get_git_hook: Operation[GitHook] = Operation(
    id="repoGetGitHook",
    method="GET",
    path="/repos/{owner}/{repo}/hooks/git/{id}",
    resource="hooks",
    name="get_git_hook",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=GitHook,
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
_repo_get_hook: Operation[Hook] = Operation(
    id="repoGetHook",
    method="GET",
    path="/repos/{owner}/{repo}/hooks/{id}",
    resource="hooks",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
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
_repo_list_git_hooks: Operation[List[GitHook]] = Operation(
    id="repoListGitHooks",
    method="GET",
    path="/repos/{owner}/{repo}/hooks/git",
    resource="hooks",
    name="list_git_hooks",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[GitHook],
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
_repo_list_hooks: Operation[List[Hook]] = Operation(
    id="repoListHooks",
    method="GET",
    path="/repos/{owner}/{repo}/hooks",
    resource="hooks",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Hook],
    returns_json=True,
    iterator="iter",
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
_repo_test_hook: Operation[None] = Operation(
    id="repoTestHook",
    method="POST",
    path="/repos/{owner}/{repo}/hooks/{id}/tests",
    resource="hooks",
    name="test",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("ref", "ref", "query"),
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
_user_create_hook: Operation[Hook] = Operation(
    id="userCreateHook",
    method="POST",
    path="/user/hooks",
    resource="hooks",
    name="create_for_user",
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
_user_delete_hook: Operation[None] = Operation(
    id="userDeleteHook",
    method="DELETE",
    path="/user/hooks/{id}",
    resource="hooks",
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
_user_edit_hook: Operation[Hook] = Operation(
    id="userEditHook",
    method="PATCH",
    path="/user/hooks/{id}",
    resource="hooks",
    name="update_for_user",
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
_user_get_hook: Operation[Hook] = Operation(
    id="userGetHook",
    method="GET",
    path="/user/hooks/{id}",
    resource="hooks",
    name="get_for_user",
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
_user_list_hooks: Operation[List[Hook]] = Operation(
    id="userListHooks",
    method="GET",
    path="/user/hooks",
    resource="hooks",
    name="list_for_user",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Hook],
    returns_json=True,
    iterator="iter_for_user",
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

OPERATIONS = (
    _org_create_hook,
    _org_delete_hook,
    _org_edit_hook,
    _org_get_hook,
    _org_list_hooks,
    _repo_create_hook,
    _repo_delete_git_hook,
    _repo_delete_hook,
    _repo_edit_git_hook,
    _repo_edit_hook,
    _repo_get_git_hook,
    _repo_get_hook,
    _repo_list_git_hooks,
    _repo_list_hooks,
    _repo_test_hook,
    _user_create_hook,
    _user_delete_hook,
    _user_edit_hook,
    _user_get_hook,
    _user_list_hooks,
)


class HooksApi(Resource):
    @checked
    def create_for_org(
        self,
        org: StrictStr,
        body: Union[CreateHookOption, Mapping[str, Any]],
    ) -> Hook:
        """Create an organization webhook (orgCreateHook)."""
        return self._call(
            _org_create_hook,
            org=org,
            _body=body,
        )

    @checked
    def delete_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an organization webhook (orgDeleteHook)."""
        return self._call(
            _org_delete_hook,
            org=org,
            id=id,
        )

    @checked
    def update_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change an organization webhook (orgEditHook)."""
        return self._call(
            _org_edit_hook,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    def get_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> Hook:
        """Get an organization webhook (orgGetHook)."""
        return self._call(
            _org_get_hook,
            org=org,
            id=id,
        )

    @checked
    def list_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Hook]:
        """List one page of an organization's webhooks (orgListHooks)."""
        return self._call(
            _org_list_hooks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_hooks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Create a repository webhook (repoCreateHook)."""
        return self._call(
            _repo_create_hook,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def delete_git_hook(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> None:
        """Clear a Git hook's content (repoDeleteGitHook)."""
        return self._call(
            _repo_delete_git_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a repository webhook (repoDeleteHook)."""
        return self._call(
            _repo_delete_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def update_git_hook(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
        body: Optional[Union[EditGitHookOption, Mapping[str, Any]]] = None,
    ) -> GitHook:
        """Change a Git hook's content (repoEditGitHook)."""
        return self._call(
            _repo_edit_git_hook,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change a repository webhook (repoEditHook)."""
        return self._call(
            _repo_edit_hook,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def get_git_hook(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> GitHook:
        """Get a Git hook (repoGetGitHook)."""
        return self._call(
            _repo_get_git_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Hook:
        """Get a repository webhook (repoGetHook)."""
        return self._call(
            _repo_get_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def list_git_hooks(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[GitHook]:
        """List a repository's Git hooks (repoListGitHooks)."""
        return self._call(
            _repo_list_git_hooks,
            owner=owner,
            repo=repo,
        )

    @checked
    def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Hook]:
        """List one page of a repository's webhooks (repoListHooks)."""
        return self._call(
            _repo_list_hooks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_hooks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def test(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        ref: Optional[StrictStr] = None,
    ) -> None:
        """Send a test push event to a repository webhook (repoTestHook)."""
        return self._call(
            _repo_test_hook,
            owner=owner,
            repo=repo,
            id=id,
            ref=ref,
        )

    @checked
    def create_for_user(
        self,
        body: Union[CreateHookOption, Mapping[str, Any]],
    ) -> Hook:
        """Create a webhook of your own (userCreateHook)."""
        return self._call(
            _user_create_hook,
            _body=body,
        )

    @checked
    def delete_for_user(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your webhooks (userDeleteHook)."""
        return self._call(
            _user_delete_hook,
            id=id,
        )

    @checked
    def update_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change one of your webhooks (userEditHook)."""
        return self._call(
            _user_edit_hook,
            id=id,
            _body=body,
        )

    @checked
    def get_for_user(
        self,
        id: StrictInt,
    ) -> Hook:
        """Get one of your webhooks (userGetHook)."""
        return self._call(
            _user_get_hook,
            id=id,
        )

    @checked
    def list_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Hook]:
        """List one page of your own webhooks (userListHooks)."""
        return self._call(
            _user_list_hooks,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_hooks,
            page=page,
            limit=limit,
        )


class AsyncHooksApi(AsyncResource):
    @checked
    async def create_for_org(
        self,
        org: StrictStr,
        body: Union[CreateHookOption, Mapping[str, Any]],
    ) -> Hook:
        """Create an organization webhook (orgCreateHook)."""
        return await self._call(
            _org_create_hook,
            org=org,
            _body=body,
        )

    @checked
    async def delete_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an organization webhook (orgDeleteHook)."""
        return await self._call(
            _org_delete_hook,
            org=org,
            id=id,
        )

    @checked
    async def update_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change an organization webhook (orgEditHook)."""
        return await self._call(
            _org_edit_hook,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    async def get_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> Hook:
        """Get an organization webhook (orgGetHook)."""
        return await self._call(
            _org_get_hook,
            org=org,
            id=id,
        )

    @checked
    async def list_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Hook]:
        """List one page of an organization's webhooks (orgListHooks)."""
        return await self._call(
            _org_list_hooks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_org(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_hooks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Create a repository webhook (repoCreateHook)."""
        return await self._call(
            _repo_create_hook,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def delete_git_hook(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> None:
        """Clear a Git hook's content (repoDeleteGitHook)."""
        return await self._call(
            _repo_delete_git_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a repository webhook (repoDeleteHook)."""
        return await self._call(
            _repo_delete_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def update_git_hook(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
        body: Optional[Union[EditGitHookOption, Mapping[str, Any]]] = None,
    ) -> GitHook:
        """Change a Git hook's content (repoEditGitHook)."""
        return await self._call(
            _repo_edit_git_hook,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change a repository webhook (repoEditHook)."""
        return await self._call(
            _repo_edit_hook,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def get_git_hook(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> GitHook:
        """Get a Git hook (repoGetGitHook)."""
        return await self._call(
            _repo_get_git_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Hook:
        """Get a repository webhook (repoGetHook)."""
        return await self._call(
            _repo_get_hook,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def list_git_hooks(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[GitHook]:
        """List a repository's Git hooks (repoListGitHooks)."""
        return await self._call(
            _repo_list_git_hooks,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Hook]:
        """List one page of a repository's webhooks (repoListHooks)."""
        return await self._call(
            _repo_list_hooks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_hooks,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def test(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        ref: Optional[StrictStr] = None,
    ) -> None:
        """Send a test push event to a repository webhook (repoTestHook)."""
        return await self._call(
            _repo_test_hook,
            owner=owner,
            repo=repo,
            id=id,
            ref=ref,
        )

    @checked
    async def create_for_user(
        self,
        body: Union[CreateHookOption, Mapping[str, Any]],
    ) -> Hook:
        """Create a webhook of your own (userCreateHook)."""
        return await self._call(
            _user_create_hook,
            _body=body,
        )

    @checked
    async def delete_for_user(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your webhooks (userDeleteHook)."""
        return await self._call(
            _user_delete_hook,
            id=id,
        )

    @checked
    async def update_for_user(
        self,
        id: StrictInt,
        body: Optional[Union[EditHookOption, Mapping[str, Any]]] = None,
    ) -> Hook:
        """Change one of your webhooks (userEditHook)."""
        return await self._call(
            _user_edit_hook,
            id=id,
            _body=body,
        )

    @checked
    async def get_for_user(
        self,
        id: StrictInt,
    ) -> Hook:
        """Get one of your webhooks (userGetHook)."""
        return await self._call(
            _user_get_hook,
            id=id,
        )

    @checked
    async def list_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Hook]:
        """List one page of your own webhooks (userListHooks)."""
        return await self._call(
            _user_list_hooks,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_user(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Hook]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_hooks,
            page=page,
            limit=limit,
        )
