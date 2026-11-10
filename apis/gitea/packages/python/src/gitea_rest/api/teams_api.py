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
from gitea_rest.models.activity import Activity
from gitea_rest.models.create_team_option import CreateTeamOption
from gitea_rest.models.edit_team_option import EditTeamOption
from gitea_rest.models.repository import Repository
from gitea_rest.models.team import Team
from gitea_rest.models.team_search_results import TeamSearchResults
from gitea_rest.models.user import User

_org_add_team_member: Operation[None] = Operation(
    id="orgAddTeamMember",
    method="PUT",
    path="/teams/{id}/members/{username}",
    resource="teams",
    name="add_member",
    params=(
        Param("id", "id", "path"),
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
_org_add_team_repository: Operation[None] = Operation(
    id="orgAddTeamRepository",
    method="PUT",
    path="/teams/{id}/repos/{org}/{repo}",
    resource="teams",
    name="add_repo",
    params=(
        Param("id", "id", "path"),
        Param("org", "org", "path"),
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
_org_create_team: Operation[Team] = Operation(
    id="orgCreateTeam",
    method="POST",
    path="/orgs/{org}/teams",
    resource="teams",
    name="create",
    params=(Param("org", "org", "path"),),
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
_org_delete_team: Operation[None] = Operation(
    id="orgDeleteTeam",
    method="DELETE",
    path="/teams/{id}",
    resource="teams",
    name="delete",
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
_org_edit_team: Operation[Team] = Operation(
    id="orgEditTeam",
    method="PATCH",
    path="/teams/{id}",
    resource="teams",
    name="update",
    params=(Param("id", "id", "path"),),
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
_org_get_team: Operation[Team] = Operation(
    id="orgGetTeam",
    method="GET",
    path="/teams/{id}",
    resource="teams",
    name="get",
    params=(Param("id", "id", "path"),),
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
_org_list_team_activity_feeds: Operation[List[Activity]] = Operation(
    id="orgListTeamActivityFeeds",
    method="GET",
    path="/teams/{id}/activities/feeds",
    resource="teams",
    name="list_activity_feeds",
    params=(
        Param("id", "id", "path"),
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
_org_list_team_member: Operation[User] = Operation(
    id="orgListTeamMember",
    method="GET",
    path="/teams/{id}/members/{username}",
    resource="teams",
    name="get_member",
    params=(
        Param("id", "id", "path"),
        Param("username", "username", "path"),
    ),
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
_org_list_team_members: Operation[List[User]] = Operation(
    id="orgListTeamMembers",
    method="GET",
    path="/teams/{id}/members",
    resource="teams",
    name="list_members",
    params=(
        Param("id", "id", "path"),
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
_org_list_team_repo: Operation[Repository] = Operation(
    id="orgListTeamRepo",
    method="GET",
    path="/teams/{id}/repos/{org}/{repo}",
    resource="teams",
    name="get_repo",
    params=(
        Param("id", "id", "path"),
        Param("org", "org", "path"),
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
_org_list_team_repos: Operation[List[Repository]] = Operation(
    id="orgListTeamRepos",
    method="GET",
    path="/teams/{id}/repos",
    resource="teams",
    name="list_repos",
    params=(
        Param("id", "id", "path"),
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
_org_list_teams: Operation[List[Team]] = Operation(
    id="orgListTeams",
    method="GET",
    path="/orgs/{org}/teams",
    resource="teams",
    name="list",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Team],
    returns_json=True,
    iterator="iter",
    item=_models.Team,
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
_org_remove_team_member: Operation[None] = Operation(
    id="orgRemoveTeamMember",
    method="DELETE",
    path="/teams/{id}/members/{username}",
    resource="teams",
    name="remove_member",
    params=(
        Param("id", "id", "path"),
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
_org_remove_team_repository: Operation[None] = Operation(
    id="orgRemoveTeamRepository",
    method="DELETE",
    path="/teams/{id}/repos/{org}/{repo}",
    resource="teams",
    name="remove_repo",
    params=(
        Param("id", "id", "path"),
        Param("org", "org", "path"),
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
_team_search: Operation[TeamSearchResults] = Operation(
    id="teamSearch",
    method="GET",
    path="/orgs/{org}/teams/search",
    resource="teams",
    name="search",
    params=(
        Param("org", "org", "path"),
        Param("q", "q", "query"),
        Param("include_desc", "include_desc", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=TeamSearchResults,
    returns_json=True,
    iterator="iter_search",
    item=_models.Team,
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
    _org_add_team_member,
    _org_add_team_repository,
    _org_create_team,
    _org_delete_team,
    _org_edit_team,
    _org_get_team,
    _org_list_team_activity_feeds,
    _org_list_team_member,
    _org_list_team_members,
    _org_list_team_repo,
    _org_list_team_repos,
    _org_list_teams,
    _org_remove_team_member,
    _org_remove_team_repository,
    _team_search,
)


class TeamsApi(Resource):
    @checked
    def add_member(
        self,
        id: StrictInt,
        username: StrictStr,
    ) -> None:
        """Add a member to a team (orgAddTeamMember)."""
        return self._call(
            _org_add_team_member,
            id=id,
            username=username,
        )

    @checked
    def add_repo(
        self,
        id: StrictInt,
        org: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Give a team access to a repository (orgAddTeamRepository)."""
        return self._call(
            _org_add_team_repository,
            id=id,
            org=org,
            repo=repo,
        )

    @checked
    def create(
        self,
        org: StrictStr,
        body: Optional[Union[CreateTeamOption, Mapping[str, Any]]] = None,
    ) -> Team:
        """Create a team (orgCreateTeam)."""
        return self._call(
            _org_create_team,
            org=org,
            _body=body,
        )

    @checked
    def delete(
        self,
        id: StrictInt,
    ) -> None:
        """Delete a team (orgDeleteTeam)."""
        return self._call(
            _org_delete_team,
            id=id,
        )

    @checked
    def update(
        self,
        id: StrictInt,
        body: Optional[Union[EditTeamOption, Mapping[str, Any]]] = None,
    ) -> Team:
        """Change a team (orgEditTeam)."""
        return self._call(
            _org_edit_team,
            id=id,
            _body=body,
        )

    @checked
    def get(
        self,
        id: StrictInt,
    ) -> Team:
        """Get a team (orgGetTeam)."""
        return self._call(
            _org_get_team,
            id=id,
        )

    @checked
    def list_activity_feeds(
        self,
        id: StrictInt,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of a team's activity (orgListTeamActivityFeeds)."""
        return self._call(
            _org_list_team_activity_feeds,
            id=id,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        id: StrictInt,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_team_activity_feeds,
            id=id,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def get_member(
        self,
        id: StrictInt,
        username: StrictStr,
    ) -> User:
        """Get a member of a team (orgListTeamMember)."""
        return self._call(
            _org_list_team_member,
            id=id,
            username=username,
        )

    @checked
    def list_members(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of a team's members (orgListTeamMembers)."""
        return self._call(
            _org_list_team_members,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_members(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_team_members,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def get_repo(
        self,
        id: StrictInt,
        org: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Get a repository that a team has access to (orgListTeamRepo)."""
        return self._call(
            _org_list_team_repo,
            id=id,
            org=org,
            repo=repo,
        )

    @checked
    def list_repos(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of a team's repositories (orgListTeamRepos)."""
        return self._call(
            _org_list_team_repos,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_team_repos,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def list(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Team]:
        """List one page of an organization's teams (orgListTeams)."""
        return self._call(
            _org_list_teams,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Team]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_teams,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def remove_member(
        self,
        id: StrictInt,
        username: StrictStr,
    ) -> None:
        """Remove a member from a team (orgRemoveTeamMember)."""
        return self._call(
            _org_remove_team_member,
            id=id,
            username=username,
        )

    @checked
    def remove_repo(
        self,
        id: StrictInt,
        org: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Remove a team's access to a repository (orgRemoveTeamRepository)."""
        return self._call(
            _org_remove_team_repository,
            id=id,
            org=org,
            repo=repo,
        )

    @checked
    def search(
        self,
        org: StrictStr,
        *,
        q: Optional[StrictStr] = None,
        include_desc: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> TeamSearchResults:
        """Get one page of an organization's teams that match a search (teamSearch)."""
        return self._call(
            _team_search,
            org=org,
            q=q,
            include_desc=include_desc,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        org: StrictStr,
        *,
        q: Optional[StrictStr] = None,
        include_desc: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Team]:
        """Iterate every item across all pages."""
        return self._paginate(
            _team_search,
            org=org,
            q=q,
            include_desc=include_desc,
            page=page,
            limit=limit,
        )


class AsyncTeamsApi(AsyncResource):
    @checked
    async def add_member(
        self,
        id: StrictInt,
        username: StrictStr,
    ) -> None:
        """Add a member to a team (orgAddTeamMember)."""
        return await self._call(
            _org_add_team_member,
            id=id,
            username=username,
        )

    @checked
    async def add_repo(
        self,
        id: StrictInt,
        org: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Give a team access to a repository (orgAddTeamRepository)."""
        return await self._call(
            _org_add_team_repository,
            id=id,
            org=org,
            repo=repo,
        )

    @checked
    async def create(
        self,
        org: StrictStr,
        body: Optional[Union[CreateTeamOption, Mapping[str, Any]]] = None,
    ) -> Team:
        """Create a team (orgCreateTeam)."""
        return await self._call(
            _org_create_team,
            org=org,
            _body=body,
        )

    @checked
    async def delete(
        self,
        id: StrictInt,
    ) -> None:
        """Delete a team (orgDeleteTeam)."""
        return await self._call(
            _org_delete_team,
            id=id,
        )

    @checked
    async def update(
        self,
        id: StrictInt,
        body: Optional[Union[EditTeamOption, Mapping[str, Any]]] = None,
    ) -> Team:
        """Change a team (orgEditTeam)."""
        return await self._call(
            _org_edit_team,
            id=id,
            _body=body,
        )

    @checked
    async def get(
        self,
        id: StrictInt,
    ) -> Team:
        """Get a team (orgGetTeam)."""
        return await self._call(
            _org_get_team,
            id=id,
        )

    @checked
    async def list_activity_feeds(
        self,
        id: StrictInt,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Activity]:
        """List one page of a team's activity (orgListTeamActivityFeeds)."""
        return await self._call(
            _org_list_team_activity_feeds,
            id=id,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    def iter_activity_feeds(
        self,
        id: StrictInt,
        *,
        var_date: Optional[date] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Activity]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_team_activity_feeds,
            id=id,
            var_date=var_date,
            page=page,
            limit=limit,
        )

    @checked
    async def get_member(
        self,
        id: StrictInt,
        username: StrictStr,
    ) -> User:
        """Get a member of a team (orgListTeamMember)."""
        return await self._call(
            _org_list_team_member,
            id=id,
            username=username,
        )

    @checked
    async def list_members(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of a team's members (orgListTeamMembers)."""
        return await self._call(
            _org_list_team_members,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_members(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_team_members,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    async def get_repo(
        self,
        id: StrictInt,
        org: StrictStr,
        repo: StrictStr,
    ) -> Repository:
        """Get a repository that a team has access to (orgListTeamRepo)."""
        return await self._call(
            _org_list_team_repo,
            id=id,
            org=org,
            repo=repo,
        )

    @checked
    async def list_repos(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of a team's repositories (orgListTeamRepos)."""
        return await self._call(
            _org_list_team_repos,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        id: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_team_repos,
            id=id,
            page=page,
            limit=limit,
        )

    @checked
    async def list(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Team]:
        """List one page of an organization's teams (orgListTeams)."""
        return await self._call(
            _org_list_teams,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        org: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Team]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_teams,
            org=org,
            page=page,
            limit=limit,
        )

    @checked
    async def remove_member(
        self,
        id: StrictInt,
        username: StrictStr,
    ) -> None:
        """Remove a member from a team (orgRemoveTeamMember)."""
        return await self._call(
            _org_remove_team_member,
            id=id,
            username=username,
        )

    @checked
    async def remove_repo(
        self,
        id: StrictInt,
        org: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Remove a team's access to a repository (orgRemoveTeamRepository)."""
        return await self._call(
            _org_remove_team_repository,
            id=id,
            org=org,
            repo=repo,
        )

    @checked
    async def search(
        self,
        org: StrictStr,
        *,
        q: Optional[StrictStr] = None,
        include_desc: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> TeamSearchResults:
        """Get one page of an organization's teams that match a search (teamSearch)."""
        return await self._call(
            _team_search,
            org=org,
            q=q,
            include_desc=include_desc,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        org: StrictStr,
        *,
        q: Optional[StrictStr] = None,
        include_desc: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Team]:
        """Iterate every item across all pages."""
        return self._paginate(
            _team_search,
            org=org,
            q=q,
            include_desc=include_desc,
            page=page,
            limit=limit,
        )
