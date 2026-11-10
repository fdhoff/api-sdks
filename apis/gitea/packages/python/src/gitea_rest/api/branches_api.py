# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import AsyncResource, LinkHeader, Operation, Param, Resource, Scheme, checked
from gitea_rest.models.branch import Branch
from gitea_rest.models.branch_protection import BranchProtection
from gitea_rest.models.create_branch_protection_option import CreateBranchProtectionOption
from gitea_rest.models.create_branch_repo_option import CreateBranchRepoOption
from gitea_rest.models.edit_branch_protection_option import EditBranchProtectionOption
from gitea_rest.models.rename_branch_repo_option import RenameBranchRepoOption
from gitea_rest.models.update_branch_protection_priories import UpdateBranchProtectionPriories
from gitea_rest.models.update_branch_repo_option import UpdateBranchRepoOption

_repo_create_branch: Operation[Branch] = Operation(
    id="repoCreateBranch",
    method="POST",
    path="/repos/{owner}/{repo}/branches",
    resource="branches",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Branch,
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
_repo_create_branch_protection: Operation[BranchProtection] = Operation(
    id="repoCreateBranchProtection",
    method="POST",
    path="/repos/{owner}/{repo}/branch_protections",
    resource="branches",
    name="create_protection",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=BranchProtection,
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
_repo_delete_branch: Operation[None] = Operation(
    id="repoDeleteBranch",
    method="DELETE",
    path="/repos/{owner}/{repo}/branches/{branch}",
    resource="branches",
    name="delete",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("branch", "branch", "path"),
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
_repo_delete_branch_protection: Operation[None] = Operation(
    id="repoDeleteBranchProtection",
    method="DELETE",
    path="/repos/{owner}/{repo}/branch_protections/{name}",
    resource="branches",
    name="delete_protection",
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
_repo_edit_branch_protection: Operation[BranchProtection] = Operation(
    id="repoEditBranchProtection",
    method="PATCH",
    path="/repos/{owner}/{repo}/branch_protections/{name}",
    resource="branches",
    name="update_protection",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("name", "name", "path"),
    ),
    response=BranchProtection,
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
_repo_get_branch: Operation[Branch] = Operation(
    id="repoGetBranch",
    method="GET",
    path="/repos/{owner}/{repo}/branches/{branch}",
    resource="branches",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("branch", "branch", "path"),
    ),
    response=Branch,
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
_repo_get_branch_protection: Operation[BranchProtection] = Operation(
    id="repoGetBranchProtection",
    method="GET",
    path="/repos/{owner}/{repo}/branch_protections/{name}",
    resource="branches",
    name="get_protection",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("name", "name", "path"),
    ),
    response=BranchProtection,
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
_repo_list_branch_protection: Operation[List[BranchProtection]] = Operation(
    id="repoListBranchProtection",
    method="GET",
    path="/repos/{owner}/{repo}/branch_protections",
    resource="branches",
    name="list_protections",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[BranchProtection],
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
_repo_list_branches: Operation[List[Branch]] = Operation(
    id="repoListBranches",
    method="GET",
    path="/repos/{owner}/{repo}/branches",
    resource="branches",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("q", "q", "query"),
    ),
    response=List[Branch],
    returns_json=True,
    iterator="iter",
    item=_models.Branch,
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
_repo_rename_branch: Operation[None] = Operation(
    id="repoRenameBranch",
    method="PATCH",
    path="/repos/{owner}/{repo}/branches/{branch}",
    resource="branches",
    name="rename",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("branch", "branch", "path"),
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
_repo_update_branch: Operation[None] = Operation(
    id="repoUpdateBranch",
    method="PUT",
    path="/repos/{owner}/{repo}/branches/{branch}",
    resource="branches",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("branch", "branch", "path"),
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
_repo_update_branch_protection_priories: Operation[None] = Operation(
    id="repoUpdateBranchProtectionPriories",
    method="POST",
    path="/repos/{owner}/{repo}/branch_protections/priority",
    resource="branches",
    name="reorder_protections",
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

OPERATIONS = (
    _repo_create_branch,
    _repo_create_branch_protection,
    _repo_delete_branch,
    _repo_delete_branch_protection,
    _repo_edit_branch_protection,
    _repo_get_branch,
    _repo_get_branch_protection,
    _repo_list_branch_protection,
    _repo_list_branches,
    _repo_rename_branch,
    _repo_update_branch,
    _repo_update_branch_protection_priories,
)


class BranchesApi(Resource):
    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateBranchRepoOption, Mapping[str, Any]]] = None,
    ) -> Branch:
        """Create a branch (repoCreateBranch)."""
        return self._call(
            _repo_create_branch,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def create_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateBranchProtectionOption, Mapping[str, Any]]] = None,
    ) -> BranchProtection:
        """Create a branch protection rule (repoCreateBranchProtection)."""
        return self._call(
            _repo_create_branch_protection,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
    ) -> None:
        """Delete a branch (repoDeleteBranch)."""
        return self._call(
            _repo_delete_branch,
            owner=owner,
            repo=repo,
            branch=branch,
        )

    @checked
    def delete_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> None:
        """Delete a branch protection rule (repoDeleteBranchProtection)."""
        return self._call(
            _repo_delete_branch_protection,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    def update_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
        body: Optional[Union[EditBranchProtectionOption, Mapping[str, Any]]] = None,
    ) -> BranchProtection:
        """Change a branch protection rule (repoEditBranchProtection)."""
        return self._call(
            _repo_edit_branch_protection,
            owner=owner,
            repo=repo,
            name=name,
            _body=body,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
    ) -> Branch:
        """Get a branch (repoGetBranch)."""
        return self._call(
            _repo_get_branch,
            owner=owner,
            repo=repo,
            branch=branch,
        )

    @checked
    def get_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> BranchProtection:
        """Get a branch protection rule (repoGetBranchProtection)."""
        return self._call(
            _repo_get_branch_protection,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    def list_protections(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[BranchProtection]:
        """List a repository's branch protection rules (repoListBranchProtection)."""
        return self._call(
            _repo_list_branch_protection,
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
        q: Optional[StrictStr] = None,
    ) -> List[Branch]:
        """List one page of a repository's branches (repoListBranches)."""
        return self._call(
            _repo_list_branches,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
            q=q,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        q: Optional[StrictStr] = None,
    ) -> Iterator[_models.Branch]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_branches,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
            q=q,
        )

    @checked
    def rename(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
        body: Optional[Union[RenameBranchRepoOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Rename a branch (repoRenameBranch)."""
        return self._call(
            _repo_rename_branch,
            owner=owner,
            repo=repo,
            branch=branch,
            _body=body,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
        body: Optional[Union[UpdateBranchRepoOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Point a branch at another commit (repoUpdateBranch)."""
        return self._call(
            _repo_update_branch,
            owner=owner,
            repo=repo,
            branch=branch,
            _body=body,
        )

    @checked
    def reorder_protections(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[UpdateBranchProtectionPriories, Mapping[str, Any]]] = None,
    ) -> None:
        """Set the order in which branch protection rules apply (repoUpdateBranchProtectionPriories)."""
        return self._call(
            _repo_update_branch_protection_priories,
            owner=owner,
            repo=repo,
            _body=body,
        )


class AsyncBranchesApi(AsyncResource):
    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateBranchRepoOption, Mapping[str, Any]]] = None,
    ) -> Branch:
        """Create a branch (repoCreateBranch)."""
        return await self._call(
            _repo_create_branch,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def create_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateBranchProtectionOption, Mapping[str, Any]]] = None,
    ) -> BranchProtection:
        """Create a branch protection rule (repoCreateBranchProtection)."""
        return await self._call(
            _repo_create_branch_protection,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
    ) -> None:
        """Delete a branch (repoDeleteBranch)."""
        return await self._call(
            _repo_delete_branch,
            owner=owner,
            repo=repo,
            branch=branch,
        )

    @checked
    async def delete_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> None:
        """Delete a branch protection rule (repoDeleteBranchProtection)."""
        return await self._call(
            _repo_delete_branch_protection,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    async def update_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
        body: Optional[Union[EditBranchProtectionOption, Mapping[str, Any]]] = None,
    ) -> BranchProtection:
        """Change a branch protection rule (repoEditBranchProtection)."""
        return await self._call(
            _repo_edit_branch_protection,
            owner=owner,
            repo=repo,
            name=name,
            _body=body,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
    ) -> Branch:
        """Get a branch (repoGetBranch)."""
        return await self._call(
            _repo_get_branch,
            owner=owner,
            repo=repo,
            branch=branch,
        )

    @checked
    async def get_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        name: StrictStr,
    ) -> BranchProtection:
        """Get a branch protection rule (repoGetBranchProtection)."""
        return await self._call(
            _repo_get_branch_protection,
            owner=owner,
            repo=repo,
            name=name,
        )

    @checked
    async def list_protections(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[BranchProtection]:
        """List a repository's branch protection rules (repoListBranchProtection)."""
        return await self._call(
            _repo_list_branch_protection,
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
        q: Optional[StrictStr] = None,
    ) -> List[Branch]:
        """List one page of a repository's branches (repoListBranches)."""
        return await self._call(
            _repo_list_branches,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
            q=q,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        q: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Branch]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_branches,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
            q=q,
        )

    @checked
    async def rename(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
        body: Optional[Union[RenameBranchRepoOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Rename a branch (repoRenameBranch)."""
        return await self._call(
            _repo_rename_branch,
            owner=owner,
            repo=repo,
            branch=branch,
            _body=body,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        branch: StrictStr,
        body: Optional[Union[UpdateBranchRepoOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Point a branch at another commit (repoUpdateBranch)."""
        return await self._call(
            _repo_update_branch,
            owner=owner,
            repo=repo,
            branch=branch,
            _body=body,
        )

    @checked
    async def reorder_protections(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[UpdateBranchProtectionPriories, Mapping[str, Any]]] = None,
    ) -> None:
        """Set the order in which branch protection rules apply (repoUpdateBranchProtectionPriories)."""
        return await self._call(
            _repo_update_branch_protection_priories,
            owner=owner,
            repo=repo,
            _body=body,
        )
