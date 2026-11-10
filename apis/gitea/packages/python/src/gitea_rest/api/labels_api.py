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
from gitea_rest.models.create_label_option import CreateLabelOption
from gitea_rest.models.edit_label_option import EditLabelOption
from gitea_rest.models.label import Label

_issue_create_label: Operation[Label] = Operation(
    id="issueCreateLabel",
    method="POST",
    path="/repos/{owner}/{repo}/labels",
    resource="labels",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Label,
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
_issue_delete_label: Operation[None] = Operation(
    id="issueDeleteLabel",
    method="DELETE",
    path="/repos/{owner}/{repo}/labels/{id}",
    resource="labels",
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
_issue_edit_label: Operation[Label] = Operation(
    id="issueEditLabel",
    method="PATCH",
    path="/repos/{owner}/{repo}/labels/{id}",
    resource="labels",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Label,
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
_issue_get_label: Operation[Label] = Operation(
    id="issueGetLabel",
    method="GET",
    path="/repos/{owner}/{repo}/labels/{id}",
    resource="labels",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Label,
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
_issue_list_labels: Operation[List[Label]] = Operation(
    id="issueListLabels",
    method="GET",
    path="/repos/{owner}/{repo}/labels",
    resource="labels",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Label],
    returns_json=True,
    iterator="iter",
    item=_models.Label,
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
_org_create_label: Operation[Label] = Operation(
    id="orgCreateLabel",
    method="POST",
    path="/orgs/{org}/labels",
    resource="labels",
    name="create_for_org",
    params=(Param("org", "org", "path"),),
    response=Label,
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
_org_delete_label: Operation[None] = Operation(
    id="orgDeleteLabel",
    method="DELETE",
    path="/orgs/{org}/labels/{id}",
    resource="labels",
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
_org_edit_label: Operation[Label] = Operation(
    id="orgEditLabel",
    method="PATCH",
    path="/orgs/{org}/labels/{id}",
    resource="labels",
    name="update_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
    ),
    response=Label,
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
_org_get_label: Operation[Label] = Operation(
    id="orgGetLabel",
    method="GET",
    path="/orgs/{org}/labels/{id}",
    resource="labels",
    name="get_for_org",
    params=(
        Param("org", "org", "path"),
        Param("id", "id", "path"),
    ),
    response=Label,
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
_org_list_labels: Operation[List[Label]] = Operation(
    id="orgListLabels",
    method="GET",
    path="/orgs/{org}/labels",
    resource="labels",
    name="list_for_org",
    params=(
        Param("org", "org", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Label],
    returns_json=True,
    iterator="iter_for_org",
    item=_models.Label,
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
    _issue_create_label,
    _issue_delete_label,
    _issue_edit_label,
    _issue_get_label,
    _issue_list_labels,
    _org_create_label,
    _org_delete_label,
    _org_edit_label,
    _org_get_label,
    _org_list_labels,
)


class LabelsApi(Resource):
    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Create a repository label (issueCreateLabel)."""
        return self._call(
            _issue_create_label,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a repository label (issueDeleteLabel)."""
        return self._call(
            _issue_delete_label,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Change a repository label (issueEditLabel)."""
        return self._call(
            _issue_edit_label,
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
        id: StrictInt,
    ) -> Label:
        """Get a repository label (issueGetLabel)."""
        return self._call(
            _issue_get_label,
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
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Label]:
        """List one page of a repository's labels (issueListLabels)."""
        return self._call(
            _issue_list_labels,
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
    ) -> Iterator[_models.Label]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_labels,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def create_for_org(
        self,
        org: StrictStr,
        body: Optional[Union[CreateLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Create an organization label (orgCreateLabel)."""
        return self._call(
            _org_create_label,
            org=org,
            _body=body,
        )

    @checked
    def delete_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an organization label (orgDeleteLabel)."""
        return self._call(
            _org_delete_label,
            org=org,
            id=id,
        )

    @checked
    def update_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Change an organization label (orgEditLabel)."""
        return self._call(
            _org_edit_label,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    def get_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> Label:
        """Get an organization label (orgGetLabel)."""
        return self._call(
            _org_get_label,
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
    ) -> List[Label]:
        """List one page of an organization's labels (orgListLabels)."""
        return self._call(
            _org_list_labels,
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
    ) -> Iterator[_models.Label]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_labels,
            org=org,
            page=page,
            limit=limit,
        )


class AsyncLabelsApi(AsyncResource):
    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Create a repository label (issueCreateLabel)."""
        return await self._call(
            _issue_create_label,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a repository label (issueDeleteLabel)."""
        return await self._call(
            _issue_delete_label,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Change a repository label (issueEditLabel)."""
        return await self._call(
            _issue_edit_label,
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
        id: StrictInt,
    ) -> Label:
        """Get a repository label (issueGetLabel)."""
        return await self._call(
            _issue_get_label,
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
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Label]:
        """List one page of a repository's labels (issueListLabels)."""
        return await self._call(
            _issue_list_labels,
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
    ) -> AsyncIterator[_models.Label]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_labels,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    async def create_for_org(
        self,
        org: StrictStr,
        body: Optional[Union[CreateLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Create an organization label (orgCreateLabel)."""
        return await self._call(
            _org_create_label,
            org=org,
            _body=body,
        )

    @checked
    async def delete_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an organization label (orgDeleteLabel)."""
        return await self._call(
            _org_delete_label,
            org=org,
            id=id,
        )

    @checked
    async def update_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditLabelOption, Mapping[str, Any]]] = None,
    ) -> Label:
        """Change an organization label (orgEditLabel)."""
        return await self._call(
            _org_edit_label,
            org=org,
            id=id,
            _body=body,
        )

    @checked
    async def get_for_org(
        self,
        org: StrictStr,
        id: StrictInt,
    ) -> Label:
        """Get an organization label (orgGetLabel)."""
        return await self._call(
            _org_get_label,
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
    ) -> List[Label]:
        """List one page of an organization's labels (orgListLabels)."""
        return await self._call(
            _org_list_labels,
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
    ) -> AsyncIterator[_models.Label]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_labels,
            org=org,
            page=page,
            limit=limit,
        )
