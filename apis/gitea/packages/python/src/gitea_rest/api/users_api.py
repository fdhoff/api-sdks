# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import date
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
from gitea_rest.models.access_token import AccessToken
from gitea_rest.models.activity import Activity
from gitea_rest.models.create_access_token_option import CreateAccessTokenOption
from gitea_rest.models.gpg_key import GPGKey
from gitea_rest.models.organization import Organization
from gitea_rest.models.organization_permissions import OrganizationPermissions
from gitea_rest.models.project import Project
from gitea_rest.models.public_key import PublicKey
from gitea_rest.models.repository import Repository
from gitea_rest.models.user import User
from gitea_rest.models.user_heatmap_data import UserHeatmapData
from gitea_rest.models.user_search_results import UserSearchResults

_org_get_user_permissions: Operation[OrganizationPermissions] = Operation(
    id="orgGetUserPermissions",
    method="GET",
    path="/users/{username}/orgs/{org}/permissions",
    resource="users",
    name="get_org_permissions",
    params=(
        Param("username", "username", "path"),
        Param("org", "org", "path"),
    ),
    response=OrganizationPermissions,
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
_org_list_user_orgs: Operation[List[Organization]] = Operation(
    id="orgListUserOrgs",
    method="GET",
    path="/users/{username}/orgs",
    resource="users",
    name="list_orgs",
    params=(
        Param("username", "username", "path"),
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
_user_check_following: Operation[None] = Operation(
    id="userCheckFollowing",
    method="GET",
    path="/users/{username}/following/{target}",
    resource="users",
    name="check_following",
    params=(
        Param("username", "username", "path"),
        Param("target", "target", "path"),
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
_user_create_token: Operation[AccessToken] = Operation(
    id="userCreateToken",
    method="POST",
    path="/users/{username}/tokens",
    resource="users",
    name="create_token",
    params=(Param("username", "username", "path"),),
    response=AccessToken,
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
_user_delete_access_token: Operation[None] = Operation(
    id="userDeleteAccessToken",
    method="DELETE",
    path="/users/{username}/tokens/{token}",
    resource="users",
    name="delete_token",
    params=(
        Param("username", "username", "path"),
        Param("token", "token", "path"),
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
_user_get: Operation[User] = Operation(
    id="userGet",
    method="GET",
    path="/users/{username}",
    resource="users",
    name="get",
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
_user_get_heatmap_data: Operation[List[UserHeatmapData]] = Operation(
    id="userGetHeatmapData",
    method="GET",
    path="/users/{username}/heatmap",
    resource="users",
    name="get_heatmap",
    params=(Param("username", "username", "path"),),
    response=List[UserHeatmapData],
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
_user_get_tokens: Operation[List[AccessToken]] = Operation(
    id="userGetTokens",
    method="GET",
    path="/users/{username}/tokens",
    resource="users",
    name="list_tokens",
    params=(
        Param("username", "username", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[AccessToken],
    returns_json=True,
    iterator="iter_tokens",
    item=_models.AccessToken,
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
_user_list_activity_feeds: Operation[List[Activity]] = Operation(
    id="userListActivityFeeds",
    method="GET",
    path="/users/{username}/activities/feeds",
    resource="users",
    name="list_activity_feeds",
    params=(
        Param("username", "username", "path"),
        Param("only-performed-by", "only_performed_by", "query"),
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
_user_list_followers: Operation[List[User]] = Operation(
    id="userListFollowers",
    method="GET",
    path="/users/{username}/followers",
    resource="users",
    name="list_followers",
    params=(
        Param("username", "username", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_followers",
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
_user_list_following: Operation[List[User]] = Operation(
    id="userListFollowing",
    method="GET",
    path="/users/{username}/following",
    resource="users",
    name="list_following",
    params=(
        Param("username", "username", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_following",
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
_user_list_gpg_keys: Operation[List[GPGKey]] = Operation(
    id="userListGPGKeys",
    method="GET",
    path="/users/{username}/gpg_keys",
    resource="users",
    name="list_gpg_keys",
    params=(
        Param("username", "username", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[GPGKey],
    returns_json=True,
    iterator="iter_gpg_keys",
    item=_models.GPGKey,
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
_user_list_keys: Operation[List[PublicKey]] = Operation(
    id="userListKeys",
    method="GET",
    path="/users/{username}/keys",
    resource="users",
    name="list_keys",
    params=(
        Param("username", "username", "path"),
        Param("fingerprint", "fingerprint", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[PublicKey],
    returns_json=True,
    iterator="iter_keys",
    item=_models.PublicKey,
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
_user_list_projects: Operation[List[Project]] = Operation(
    id="userListProjects",
    method="GET",
    path="/users/{username}/projects",
    resource="users",
    name="list_projects",
    params=(
        Param("username", "username", "path"),
        Param("state", "state", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Project],
    returns_json=True,
    iterator="iter_projects",
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
_user_list_repos: Operation[List[Repository]] = Operation(
    id="userListRepos",
    method="GET",
    path="/users/{username}/repos",
    resource="users",
    name="list_repos",
    params=(
        Param("username", "username", "path"),
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
_user_list_starred: Operation[List[Repository]] = Operation(
    id="userListStarred",
    method="GET",
    path="/users/{username}/starred",
    resource="users",
    name="list_starred",
    params=(
        Param("username", "username", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Repository],
    returns_json=True,
    iterator="iter_starred",
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
_user_list_subscriptions: Operation[List[Repository]] = Operation(
    id="userListSubscriptions",
    method="GET",
    path="/users/{username}/subscriptions",
    resource="users",
    name="list_watched",
    params=(
        Param("username", "username", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Repository],
    returns_json=True,
    iterator="iter_watched",
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
_user_search: Operation[UserSearchResults] = Operation(
    id="userSearch",
    method="GET",
    path="/users/search",
    resource="users",
    name="search",
    params=(
        Param("q", "q", "query"),
        Param("uid", "uid", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=UserSearchResults,
    returns_json=True,
    iterator="iter_search",
    item=_models.User,
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

OPERATIONS = (
    _org_get_user_permissions,
    _org_list_user_orgs,
    _user_check_following,
    _user_create_token,
    _user_delete_access_token,
    _user_get,
    _user_get_heatmap_data,
    _user_get_tokens,
    _user_list_activity_feeds,
    _user_list_followers,
    _user_list_following,
    _user_list_gpg_keys,
    _user_list_keys,
    _user_list_projects,
    _user_list_repos,
    _user_list_starred,
    _user_list_subscriptions,
    _user_search,
)


class UsersApi(Resource):
    @checked
    def get_org_permissions(
        self,
        username: StrictStr,
        org: StrictStr,
    ) -> OrganizationPermissions:
        """Get a user's permissions in an organization (orgGetUserPermissions)."""
        return self._call(
            _org_get_user_permissions,
            username=username,
            org=org,
        )

    @checked
    def list_orgs(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of a user's organizations (orgListUserOrgs)."""
        return self._call(
            _org_list_user_orgs,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_orgs(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_user_orgs,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def check_following(
        self,
        username: StrictStr,
        target: StrictStr,
    ) -> None:
        """Check whether a user follows another (userCheckFollowing)."""
        return self._call(
            _user_check_following,
            username=username,
            target=target,
        )

    @checked
    def create_token(
        self,
        username: StrictStr,
        body: Optional[Union[CreateAccessTokenOption, Mapping[str, Any]]] = None,
    ) -> AccessToken:
        """Create an access token for a user (userCreateToken)."""
        return self._call(
            _user_create_token,
            username=username,
            _body=body,
        )

    @checked
    def delete_token(
        self,
        username: StrictStr,
        token: StrictStr,
    ) -> None:
        """Delete one of a user's access tokens (userDeleteAccessToken)."""
        return self._call(
            _user_delete_access_token,
            username=username,
            token=token,
        )

    @checked
    def get(
        self,
        username: StrictStr,
    ) -> User:
        """Get a user (userGet)."""
        return self._call(
            _user_get,
            username=username,
        )

    @checked
    def get_heatmap(
        self,
        username: StrictStr,
    ) -> List[UserHeatmapData]:
        """Get a user's contribution heatmap (userGetHeatmapData)."""
        return self._call(
            _user_get_heatmap_data,
            username=username,
        )

    @checked
    def list_tokens(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[AccessToken]:
        """List one page of a user's access tokens (userGetTokens)."""
        return self._call(
            _user_get_tokens,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tokens(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.AccessToken]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_get_tokens,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def list_activity_feeds(
        self,
        username: StrictStr,
        *,
        only_performed_by: Optional[StrictBool] = None,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of a user's activity (userListActivityFeeds)."""
        return self._call(
            _user_list_activity_feeds,
            username=username,
            only_performed_by=only_performed_by,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        username: StrictStr,
        *,
        only_performed_by: Optional[StrictBool] = None,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_activity_feeds,
            username=username,
            only_performed_by=only_performed_by,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def list_followers(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of a user's followers (userListFollowers)."""
        return self._call(
            _user_list_followers,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_followers(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_followers,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def list_following(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users a user follows (userListFollowing)."""
        return self._call(
            _user_list_following,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_following(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_following,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def list_gpg_keys(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[GPGKey]:
        """List one page of a user's GPG keys (userListGPGKeys)."""
        return self._call(
            _user_list_gpg_keys,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_gpg_keys(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.GPGKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_gpg_keys,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def list_keys(
        self,
        username: StrictStr,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PublicKey]:
        """List one page of a user's SSH keys (userListKeys)."""
        return self._call(
            _user_list_keys,
            username=username,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def iter_keys(
        self,
        username: StrictStr,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.PublicKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_keys,
            username=username,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def list_projects(
        self,
        username: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of a user's projects (userListProjects)."""
        return self._call(
            _user_list_projects,
            username=username,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_projects(
        self,
        username: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_projects,
            username=username,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def list_repos(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of a user's repositories (userListRepos)."""
        return self._call(
            _user_list_repos,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_repos,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def list_starred(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories a user starred (userListStarred)."""
        return self._call(
            _user_list_starred,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_starred(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_starred,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def list_watched(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories a user watches (userListSubscriptions)."""
        return self._call(
            _user_list_subscriptions,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_watched(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_subscriptions,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def search(
        self,
        *,
        q: Optional[StrictStr] = None,
        uid: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> UserSearchResults:
        """Get one page of the users that match a search (userSearch)."""
        return self._call(
            _user_search,
            q=q,
            uid=uid,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        *,
        q: Optional[StrictStr] = None,
        uid: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_search,
            q=q,
            uid=uid,
            page=page,
            limit=limit,
        )


class AsyncUsersApi(AsyncResource):
    @checked
    async def get_org_permissions(
        self,
        username: StrictStr,
        org: StrictStr,
    ) -> OrganizationPermissions:
        """Get a user's permissions in an organization (orgGetUserPermissions)."""
        return await self._call(
            _org_get_user_permissions,
            username=username,
            org=org,
        )

    @checked
    async def list_orgs(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of a user's organizations (orgListUserOrgs)."""
        return await self._call(
            _org_list_user_orgs,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_orgs(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_user_orgs,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def check_following(
        self,
        username: StrictStr,
        target: StrictStr,
    ) -> None:
        """Check whether a user follows another (userCheckFollowing)."""
        return await self._call(
            _user_check_following,
            username=username,
            target=target,
        )

    @checked
    async def create_token(
        self,
        username: StrictStr,
        body: Optional[Union[CreateAccessTokenOption, Mapping[str, Any]]] = None,
    ) -> AccessToken:
        """Create an access token for a user (userCreateToken)."""
        return await self._call(
            _user_create_token,
            username=username,
            _body=body,
        )

    @checked
    async def delete_token(
        self,
        username: StrictStr,
        token: StrictStr,
    ) -> None:
        """Delete one of a user's access tokens (userDeleteAccessToken)."""
        return await self._call(
            _user_delete_access_token,
            username=username,
            token=token,
        )

    @checked
    async def get(
        self,
        username: StrictStr,
    ) -> User:
        """Get a user (userGet)."""
        return await self._call(
            _user_get,
            username=username,
        )

    @checked
    async def get_heatmap(
        self,
        username: StrictStr,
    ) -> List[UserHeatmapData]:
        """Get a user's contribution heatmap (userGetHeatmapData)."""
        return await self._call(
            _user_get_heatmap_data,
            username=username,
        )

    @checked
    async def list_tokens(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[AccessToken]:
        """List one page of a user's access tokens (userGetTokens)."""
        return await self._call(
            _user_get_tokens,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tokens(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.AccessToken]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_get_tokens,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def list_activity_feeds(
        self,
        username: StrictStr,
        *,
        only_performed_by: Optional[StrictBool] = None,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of a user's activity (userListActivityFeeds)."""
        return await self._call(
            _user_list_activity_feeds,
            username=username,
            only_performed_by=only_performed_by,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        username: StrictStr,
        *,
        only_performed_by: Optional[StrictBool] = None,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_activity_feeds,
            username=username,
            only_performed_by=only_performed_by,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    async def list_followers(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of a user's followers (userListFollowers)."""
        return await self._call(
            _user_list_followers,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_followers(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_followers,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def list_following(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users a user follows (userListFollowing)."""
        return await self._call(
            _user_list_following,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_following(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_following,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def list_gpg_keys(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[GPGKey]:
        """List one page of a user's GPG keys (userListGPGKeys)."""
        return await self._call(
            _user_list_gpg_keys,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_gpg_keys(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.GPGKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_gpg_keys,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def list_keys(
        self,
        username: StrictStr,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PublicKey]:
        """List one page of a user's SSH keys (userListKeys)."""
        return await self._call(
            _user_list_keys,
            username=username,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def iter_keys(
        self,
        username: StrictStr,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.PublicKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_keys,
            username=username,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    async def list_projects(
        self,
        username: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Project]:
        """List one page of a user's projects (userListProjects)."""
        return await self._call(
            _user_list_projects,
            username=username,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_projects(
        self,
        username: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Project]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_projects,
            username=username,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    async def list_repos(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of a user's repositories (userListRepos)."""
        return await self._call(
            _user_list_repos,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_repos,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def list_starred(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories a user starred (userListStarred)."""
        return await self._call(
            _user_list_starred,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_starred(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_starred,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def list_watched(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories a user watches (userListSubscriptions)."""
        return await self._call(
            _user_list_subscriptions,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    def iter_watched(
        self,
        username: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_subscriptions,
            username=username,
            page=page,
            limit=limit,
        )

    @checked
    async def search(
        self,
        *,
        q: Optional[StrictStr] = None,
        uid: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> UserSearchResults:
        """Get one page of the users that match a search (userSearch)."""
        return await self._call(
            _user_search,
            q=q,
            uid=uid,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        *,
        q: Optional[StrictStr] = None,
        uid: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_search,
            q=q,
            uid=uid,
            page=page,
            limit=limit,
        )
