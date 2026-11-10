# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import date
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
from gitea_rest.models.activity import Activity
from gitea_rest.models.create_org_option import CreateOrgOption
from gitea_rest.models.create_repo_option import CreateRepoOption
from gitea_rest.models.edit_org_option import EditOrgOption
from gitea_rest.models.organization import Organization
from gitea_rest.models.rename_org_option import RenameOrgOption
from gitea_rest.models.repository import Repository
from gitea_rest.models.update_user_avatar_option import UpdateUserAvatarOption
from gitea_rest.models.user import User

_create_org_repo: Operation[Repository] = Operation(
    id="createOrgRepo",
    method="POST",
    path="/orgs/{org}/repos",
    resource="orgs",
    name="create_repo",
    params=(Param("org", "org", "path"),),
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
_org_conceal_member: Operation[None] = Operation(
    id="orgConcealMember",
    method="DELETE",
    path="/orgs/{org}/public_members/{username}",
    resource="orgs",
    name="conceal_member",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
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
_org_create: Operation[Organization] = Operation(
    id="orgCreate",
    method="POST",
    path="/orgs",
    resource="orgs",
    name="create",
    params=(),
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
_org_delete: Operation[None] = Operation(
    id="orgDelete",
    method="DELETE",
    path="/orgs/{org}",
    resource="orgs",
    name="delete",
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
_org_delete_avatar: Operation[None] = Operation(
    id="orgDeleteAvatar",
    method="DELETE",
    path="/orgs/{org}/avatar",
    resource="orgs",
    name="delete_avatar",
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
_org_delete_member: Operation[None] = Operation(
    id="orgDeleteMember",
    method="DELETE",
    path="/orgs/{org}/members/{username}",
    resource="orgs",
    name="remove_member",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
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
_org_delete_repos: Operation[None] = Operation(
    id="orgDeleteRepos",
    method="DELETE",
    path="/orgs/{org}/repos",
    resource="orgs",
    name="delete_repos",
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
_org_edit: Operation[Organization] = Operation(
    id="orgEdit",
    method="PATCH",
    path="/orgs/{org}",
    resource="orgs",
    name="update",
    params=(Param("org", "org", "path"),),
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
_org_get: Operation[Organization] = Operation(
    id="orgGet",
    method="GET",
    path="/orgs/{org}",
    resource="orgs",
    name="get",
    params=(Param("org", "org", "path"),),
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
_org_get_all: Operation[List[Organization]] = Operation(
    id="orgGetAll",
    method="GET",
    path="/orgs",
    resource="orgs",
    name="list",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Organization],
    returns_json=True,
    iterator="iter",
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
_org_is_member: Operation[None] = Operation(
    id="orgIsMember",
    method="GET",
    path="/orgs/{org}/members/{username}",
    resource="orgs",
    name="check_member",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
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
_org_is_public_member: Operation[None] = Operation(
    id="orgIsPublicMember",
    method="GET",
    path="/orgs/{org}/public_members/{username}",
    resource="orgs",
    name="check_public_member",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
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
_org_list_activity_feeds: Operation[List[Activity]] = Operation(
    id="orgListActivityFeeds",
    method="GET",
    path="/orgs/{org}/activities/feeds",
    resource="orgs",
    name="list_activity_feeds",
    params=(
        Param("org", "org", "path"),
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
_org_list_members: Operation[List[User]] = Operation(
    id="orgListMembers",
    method="GET",
    path="/orgs/{org}/members",
    resource="orgs",
    name="list_members",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_members",
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
_org_list_public_members: Operation[List[User]] = Operation(
    id="orgListPublicMembers",
    method="GET",
    path="/orgs/{org}/public_members",
    resource="orgs",
    name="list_public_members",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_public_members",
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
_org_list_repos: Operation[List[Repository]] = Operation(
    id="orgListRepos",
    method="GET",
    path="/orgs/{org}/repos",
    resource="orgs",
    name="list_repos",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Repository],
    returns_json=True,
    iterator="iter_repos",
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
_org_publicize_member: Operation[None] = Operation(
    id="orgPublicizeMember",
    method="PUT",
    path="/orgs/{org}/public_members/{username}",
    resource="orgs",
    name="publicize_member",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
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
_org_update_avatar: Operation[None] = Operation(
    id="orgUpdateAvatar",
    method="POST",
    path="/orgs/{org}/avatar",
    resource="orgs",
    name="update_avatar",
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
_organization_block_user: Operation[None] = Operation(
    id="organizationBlockUser",
    method="PUT",
    path="/orgs/{org}/blocks/{username}",
    resource="orgs",
    name="block_user",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
        Param("note", "note", "query"),
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
_organization_check_user_block: Operation[None] = Operation(
    id="organizationCheckUserBlock",
    method="GET",
    path="/orgs/{org}/blocks/{username}",
    resource="orgs",
    name="check_blocked_user",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
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
_organization_list_blocks: Operation[List[User]] = Operation(
    id="organizationListBlocks",
    method="GET",
    path="/orgs/{org}/blocks",
    resource="orgs",
    name="list_blocked_users",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_blocked_users",
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
_organization_unblock_user: Operation[None] = Operation(
    id="organizationUnblockUser",
    method="DELETE",
    path="/orgs/{org}/blocks/{username}",
    resource="orgs",
    name="unblock_user",
    params=(
        Param("org", "org", "path"),
        Param("username", "username", "path"),
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
_rename_org: Operation[None] = Operation(
    id="renameOrg",
    method="POST",
    path="/orgs/{org}/rename",
    resource="orgs",
    name="rename",
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

OPERATIONS = (
    _create_org_repo,
    _org_conceal_member,
    _org_create,
    _org_delete,
    _org_delete_avatar,
    _org_delete_member,
    _org_delete_repos,
    _org_edit,
    _org_get,
    _org_get_all,
    _org_is_member,
    _org_is_public_member,
    _org_list_activity_feeds,
    _org_list_members,
    _org_list_public_members,
    _org_list_repos,
    _org_publicize_member,
    _org_update_avatar,
    _organization_block_user,
    _organization_check_user_block,
    _organization_list_blocks,
    _organization_unblock_user,
    _rename_org,
)


class OrgsApi(Resource):
    @checked
    def create_repo(
        self,
        org: StrictStr,
        body: Optional[Union[CreateRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Create a repository in an organization (createOrgRepo)."""
        return self._call(
            _create_org_repo,
            org=org,
            _body=body,
        )

    @checked
    def conceal_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Make a user's membership of an organization private (orgConcealMember)."""
        return self._call(
            _org_conceal_member,
            org=org,
            username=username,
        )

    @checked
    def create(
        self,
        body: Union[CreateOrgOption, Mapping[str, Any]],
    ) -> Organization:
        """Create an organization (orgCreate)."""
        return self._call(
            _org_create,
            _body=body,
        )

    @checked
    def delete(
        self,
        org: StrictStr,
    ) -> None:
        """Delete an organization (orgDelete)."""
        return self._call(
            _org_delete,
            org=org,
        )

    @checked
    def delete_avatar(
        self,
        org: StrictStr,
    ) -> None:
        """Remove an organization's avatar (orgDeleteAvatar)."""
        return self._call(
            _org_delete_avatar,
            org=org,
        )

    @checked
    def remove_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Remove a member from an organization (orgDeleteMember)."""
        return self._call(
            _org_delete_member,
            org=org,
            username=username,
        )

    @checked
    def delete_repos(
        self,
        org: StrictStr,
    ) -> None:
        """Delete every repository in an organization (orgDeleteRepos)."""
        return self._call(
            _org_delete_repos,
            org=org,
        )

    @checked
    def update(
        self,
        org: StrictStr,
        body: Union[EditOrgOption, Mapping[str, Any]],
    ) -> Organization:
        """Change an organization (orgEdit)."""
        return self._call(
            _org_edit,
            org=org,
            _body=body,
        )

    @checked
    def get(
        self,
        org: StrictStr,
    ) -> Organization:
        """Get an organization (orgGet)."""
        return self._call(
            _org_get,
            org=org,
        )

    @checked
    def list(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of the organizations you can see (orgGetAll)."""
        return self._call(
            _org_get_all,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_get_all,
            page=page,
            limit=limit,
        )

    @checked
    def check_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Check whether a user is a member of an organization (orgIsMember)."""
        return self._call(
            _org_is_member,
            org=org,
            username=username,
        )

    @checked
    def check_public_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Check whether a user's membership of an organization is public (orgIsPublicMember)."""
        return self._call(
            _org_is_public_member,
            org=org,
            username=username,
        )

    @checked
    def list_activity_feeds(
        self,
        org: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of an organization's activity (orgListActivityFeeds)."""
        return self._call(
            _org_list_activity_feeds,
            org=org,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        org: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_activity_feeds,
            org=org,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def list_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of an organization's members (orgListMembers)."""
        return self._call(
            _org_list_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def list_public_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of an organization's public members (orgListPublicMembers)."""
        return self._call(
            _org_list_public_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_public_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_public_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def list_repos(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of an organization's repositories (orgListRepos)."""
        return self._call(
            _org_list_repos,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_repos,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def publicize_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Make a user's membership of an organization public (orgPublicizeMember)."""
        return self._call(
            _org_publicize_member,
            org=org,
            username=username,
        )

    @checked
    def update_avatar(
        self,
        org: StrictStr,
        body: Optional[Union[UpdateUserAvatarOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Set an organization's avatar (orgUpdateAvatar)."""
        return self._call(
            _org_update_avatar,
            org=org,
            _body=body,
        )

    @checked
    def block_user(
        self,
        org: StrictStr,
        username: StrictStr,
        *,
        note: Optional[StrictStr] = None,
    ) -> None:
        """Block a user from an organization (organizationBlockUser)."""
        return self._call(
            _organization_block_user,
            org=org,
            username=username,
            note=note,
        )

    @checked
    def check_blocked_user(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Check whether an organization blocks a user (organizationCheckUserBlock)."""
        return self._call(
            _organization_check_user_block,
            org=org,
            username=username,
        )

    @checked
    def list_blocked_users(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users an organization blocks (organizationListBlocks)."""
        return self._call(
            _organization_list_blocks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_blocked_users(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _organization_list_blocks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def unblock_user(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Unblock a user from an organization (organizationUnblockUser)."""
        return self._call(
            _organization_unblock_user,
            org=org,
            username=username,
        )

    @checked
    def rename(
        self,
        org: StrictStr,
        body: Union[RenameOrgOption, Mapping[str, Any]],
    ) -> None:
        """Rename an organization (renameOrg)."""
        return self._call(
            _rename_org,
            org=org,
            _body=body,
        )


class AsyncOrgsApi(AsyncResource):
    @checked
    async def create_repo(
        self,
        org: StrictStr,
        body: Optional[Union[CreateRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Create a repository in an organization (createOrgRepo)."""
        return await self._call(
            _create_org_repo,
            org=org,
            _body=body,
        )

    @checked
    async def conceal_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Make a user's membership of an organization private (orgConcealMember)."""
        return await self._call(
            _org_conceal_member,
            org=org,
            username=username,
        )

    @checked
    async def create(
        self,
        body: Union[CreateOrgOption, Mapping[str, Any]],
    ) -> Organization:
        """Create an organization (orgCreate)."""
        return await self._call(
            _org_create,
            _body=body,
        )

    @checked
    async def delete(
        self,
        org: StrictStr,
    ) -> None:
        """Delete an organization (orgDelete)."""
        return await self._call(
            _org_delete,
            org=org,
        )

    @checked
    async def delete_avatar(
        self,
        org: StrictStr,
    ) -> None:
        """Remove an organization's avatar (orgDeleteAvatar)."""
        return await self._call(
            _org_delete_avatar,
            org=org,
        )

    @checked
    async def remove_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Remove a member from an organization (orgDeleteMember)."""
        return await self._call(
            _org_delete_member,
            org=org,
            username=username,
        )

    @checked
    async def delete_repos(
        self,
        org: StrictStr,
    ) -> None:
        """Delete every repository in an organization (orgDeleteRepos)."""
        return await self._call(
            _org_delete_repos,
            org=org,
        )

    @checked
    async def update(
        self,
        org: StrictStr,
        body: Union[EditOrgOption, Mapping[str, Any]],
    ) -> Organization:
        """Change an organization (orgEdit)."""
        return await self._call(
            _org_edit,
            org=org,
            _body=body,
        )

    @checked
    async def get(
        self,
        org: StrictStr,
    ) -> Organization:
        """Get an organization (orgGet)."""
        return await self._call(
            _org_get,
            org=org,
        )

    @checked
    async def list(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of the organizations you can see (orgGetAll)."""
        return await self._call(
            _org_get_all,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_get_all,
            page=page,
            limit=limit,
        )

    @checked
    async def check_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Check whether a user is a member of an organization (orgIsMember)."""
        return await self._call(
            _org_is_member,
            org=org,
            username=username,
        )

    @checked
    async def check_public_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Check whether a user's membership of an organization is public (orgIsPublicMember)."""
        return await self._call(
            _org_is_public_member,
            org=org,
            username=username,
        )

    @checked
    async def list_activity_feeds(
        self,
        org: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of an organization's activity (orgListActivityFeeds)."""
        return await self._call(
            _org_list_activity_feeds,
            org=org,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        org: StrictStr,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_activity_feeds,
            org=org,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    async def list_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of an organization's members (orgListMembers)."""
        return await self._call(
            _org_list_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def list_public_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of an organization's public members (orgListPublicMembers)."""
        return await self._call(
            _org_list_public_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_public_members(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_public_members,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def list_repos(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of an organization's repositories (orgListRepos)."""
        return await self._call(
            _org_list_repos,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_repos,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def publicize_member(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Make a user's membership of an organization public (orgPublicizeMember)."""
        return await self._call(
            _org_publicize_member,
            org=org,
            username=username,
        )

    @checked
    async def update_avatar(
        self,
        org: StrictStr,
        body: Optional[Union[UpdateUserAvatarOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Set an organization's avatar (orgUpdateAvatar)."""
        return await self._call(
            _org_update_avatar,
            org=org,
            _body=body,
        )

    @checked
    async def block_user(
        self,
        org: StrictStr,
        username: StrictStr,
        *,
        note: Optional[StrictStr] = None,
    ) -> None:
        """Block a user from an organization (organizationBlockUser)."""
        return await self._call(
            _organization_block_user,
            org=org,
            username=username,
            note=note,
        )

    @checked
    async def check_blocked_user(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Check whether an organization blocks a user (organizationCheckUserBlock)."""
        return await self._call(
            _organization_check_user_block,
            org=org,
            username=username,
        )

    @checked
    async def list_blocked_users(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users an organization blocks (organizationListBlocks)."""
        return await self._call(
            _organization_list_blocks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter_blocked_users(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _organization_list_blocks,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def unblock_user(
        self,
        org: StrictStr,
        username: StrictStr,
    ) -> None:
        """Unblock a user from an organization (organizationUnblockUser)."""
        return await self._call(
            _organization_unblock_user,
            org=org,
            username=username,
        )

    @checked
    async def rename(
        self,
        org: StrictStr,
        body: Union[RenameOrgOption, Mapping[str, Any]],
    ) -> None:
        """Rename an organization (renameOrg)."""
        return await self._call(
            _rename_org,
            org=org,
            _body=body,
        )
