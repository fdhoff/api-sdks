# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import AsyncResource, LinkHeader, Operation, Param, Resource, Scheme, checked
from gitea_rest.models.create_milestone_option import CreateMilestoneOption
from gitea_rest.models.edit_milestone_option import EditMilestoneOption
from gitea_rest.models.milestone import Milestone

_issue_create_milestone: Operation[Milestone] = Operation(
    id="issueCreateMilestone",
    method="POST",
    path="/repos/{owner}/{repo}/milestones",
    resource="milestones",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Milestone,
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
_issue_delete_milestone: Operation[None] = Operation(
    id="issueDeleteMilestone",
    method="DELETE",
    path="/repos/{owner}/{repo}/milestones/{id}",
    resource="milestones",
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
_issue_edit_milestone: Operation[Milestone] = Operation(
    id="issueEditMilestone",
    method="PATCH",
    path="/repos/{owner}/{repo}/milestones/{id}",
    resource="milestones",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Milestone,
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
_issue_get_milestone: Operation[Milestone] = Operation(
    id="issueGetMilestone",
    method="GET",
    path="/repos/{owner}/{repo}/milestones/{id}",
    resource="milestones",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Milestone,
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
_issue_get_milestones_list: Operation[List[Milestone]] = Operation(
    id="issueGetMilestonesList",
    method="GET",
    path="/repos/{owner}/{repo}/milestones",
    resource="milestones",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("state", "state", "query"),
        Param("name", "name", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Milestone],
    returns_json=True,
    iterator="iter",
    item=_models.Milestone,
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
    _issue_create_milestone,
    _issue_delete_milestone,
    _issue_edit_milestone,
    _issue_get_milestone,
    _issue_get_milestones_list,
)


class MilestonesApi(Resource):
    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateMilestoneOption, Mapping[str, Any]]] = None,
    ) -> Milestone:
        """Create a milestone (issueCreateMilestone)."""
        return self._call(
            _issue_create_milestone,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> None:
        """Delete a milestone (issueDeleteMilestone)."""
        return self._call(
            _issue_delete_milestone,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
        body: Optional[Union[EditMilestoneOption, Mapping[str, Any]]] = None,
    ) -> Milestone:
        """Change a milestone (issueEditMilestone)."""
        return self._call(
            _issue_edit_milestone,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> Milestone:
        """Get a milestone (issueGetMilestone)."""
        return self._call(
            _issue_get_milestone,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Milestone]:
        """List one page of a repository's milestones (issueGetMilestonesList)."""
        return self._call(
            _issue_get_milestones_list,
            owner=owner,
            repo=repo,
            state=state,
            name=name,
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
        name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Milestone]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_milestones_list,
            owner=owner,
            repo=repo,
            state=state,
            name=name,
            page=page,
            limit=limit,
        )


class AsyncMilestonesApi(AsyncResource):
    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateMilestoneOption, Mapping[str, Any]]] = None,
    ) -> Milestone:
        """Create a milestone (issueCreateMilestone)."""
        return await self._call(
            _issue_create_milestone,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> None:
        """Delete a milestone (issueDeleteMilestone)."""
        return await self._call(
            _issue_delete_milestone,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
        body: Optional[Union[EditMilestoneOption, Mapping[str, Any]]] = None,
    ) -> Milestone:
        """Change a milestone (issueEditMilestone)."""
        return await self._call(
            _issue_edit_milestone,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictStr,
    ) -> Milestone:
        """Get a milestone (issueGetMilestone)."""
        return await self._call(
            _issue_get_milestone,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Milestone]:
        """List one page of a repository's milestones (issueGetMilestonesList)."""
        return await self._call(
            _issue_get_milestones_list,
            owner=owner,
            repo=repo,
            state=state,
            name=name,
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
        name: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Milestone]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_milestones_list,
            owner=owner,
            repo=repo,
            state=state,
            name=name,
            page=page,
            limit=limit,
        )
