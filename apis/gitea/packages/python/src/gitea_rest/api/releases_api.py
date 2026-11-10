# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictBool, StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import AsyncResource, FileInput, LinkHeader, Operation, Param, Resource, Scheme, checked
from gitea_rest.models.attachment import Attachment
from gitea_rest.models.create_release_option import CreateReleaseOption
from gitea_rest.models.edit_attachment_options import EditAttachmentOptions
from gitea_rest.models.edit_release_option import EditReleaseOption
from gitea_rest.models.release import Release

_repo_create_release: Operation[Release] = Operation(
    id="repoCreateRelease",
    method="POST",
    path="/repos/{owner}/{repo}/releases",
    resource="releases",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Release,
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
_repo_create_release_attachment: Operation[Attachment] = Operation(
    id="repoCreateReleaseAttachment",
    method="POST",
    path="/repos/{owner}/{repo}/releases/{id}/assets",
    resource="releases",
    name="upload_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("name", "name", "query"),
        Param("attachment", "attachment", "form"),
    ),
    response=Attachment,
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
_repo_delete_release: Operation[None] = Operation(
    id="repoDeleteRelease",
    method="DELETE",
    path="/repos/{owner}/{repo}/releases/{id}",
    resource="releases",
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
_repo_delete_release_attachment: Operation[None] = Operation(
    id="repoDeleteReleaseAttachment",
    method="DELETE",
    path="/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}",
    resource="releases",
    name="delete_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("attachment_id", "attachment_id", "path"),
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
_repo_delete_release_by_tag: Operation[None] = Operation(
    id="repoDeleteReleaseByTag",
    method="DELETE",
    path="/repos/{owner}/{repo}/releases/tags/{tag}",
    resource="releases",
    name="delete_by_tag",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("tag", "tag", "path"),
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
_repo_edit_release: Operation[Release] = Operation(
    id="repoEditRelease",
    method="PATCH",
    path="/repos/{owner}/{repo}/releases/{id}",
    resource="releases",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Release,
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
_repo_edit_release_attachment: Operation[Attachment] = Operation(
    id="repoEditReleaseAttachment",
    method="PATCH",
    path="/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}",
    resource="releases",
    name="update_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("attachment_id", "attachment_id", "path"),
    ),
    response=Attachment,
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
_repo_get_latest_release: Operation[Release] = Operation(
    id="repoGetLatestRelease",
    method="GET",
    path="/repos/{owner}/{repo}/releases/latest",
    resource="releases",
    name="get_latest",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Release,
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
_repo_get_release: Operation[Release] = Operation(
    id="repoGetRelease",
    method="GET",
    path="/repos/{owner}/{repo}/releases/{id}",
    resource="releases",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Release,
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
_repo_get_release_attachment: Operation[Attachment] = Operation(
    id="repoGetReleaseAttachment",
    method="GET",
    path="/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}",
    resource="releases",
    name="get_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
        Param("attachment_id", "attachment_id", "path"),
    ),
    response=Attachment,
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
_repo_get_release_by_tag: Operation[Release] = Operation(
    id="repoGetReleaseByTag",
    method="GET",
    path="/repos/{owner}/{repo}/releases/tags/{tag}",
    resource="releases",
    name="get_by_tag",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("tag", "tag", "path"),
    ),
    response=Release,
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
_repo_list_release_attachments: Operation[List[Attachment]] = Operation(
    id="repoListReleaseAttachments",
    method="GET",
    path="/repos/{owner}/{repo}/releases/{id}/assets",
    resource="releases",
    name="list_attachments",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=List[Attachment],
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
_repo_list_releases: Operation[List[Release]] = Operation(
    id="repoListReleases",
    method="GET",
    path="/repos/{owner}/{repo}/releases",
    resource="releases",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("draft", "draft", "query"),
        Param("pre-release", "pre_release", "query"),
        Param("tag_filter", "tag_filter", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Release],
    returns_json=True,
    iterator="iter",
    item=_models.Release,
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
    _repo_create_release,
    _repo_create_release_attachment,
    _repo_delete_release,
    _repo_delete_release_attachment,
    _repo_delete_release_by_tag,
    _repo_edit_release,
    _repo_edit_release_attachment,
    _repo_get_latest_release,
    _repo_get_release,
    _repo_get_release_attachment,
    _repo_get_release_by_tag,
    _repo_list_release_attachments,
    _repo_list_releases,
)


class ReleasesApi(Resource):
    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateReleaseOption, Mapping[str, Any]]] = None,
    ) -> Release:
        """Create a release (repoCreateRelease)."""
        return self._call(
            _repo_create_release,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def upload_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        name: Optional[StrictStr] = None,
        attachment: Optional[FileInput] = None,
    ) -> Attachment:
        """Upload an attachment to a release (repoCreateReleaseAttachment)."""
        return self._call(
            _repo_create_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            name=name,
            attachment=attachment,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a release (repoDeleteRelease)."""
        return self._call(
            _repo_delete_release,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def delete_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> None:
        """Delete a release attachment (repoDeleteReleaseAttachment)."""
        return self._call(
            _repo_delete_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    def delete_by_tag(
        self,
        owner: StrictStr,
        repo: StrictStr,
        tag: StrictStr,
    ) -> None:
        """Delete a release by its tag name (repoDeleteReleaseByTag)."""
        return self._call(
            _repo_delete_release_by_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditReleaseOption, Mapping[str, Any]]] = None,
    ) -> Release:
        """Change a release (repoEditRelease)."""
        return self._call(
            _repo_edit_release,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def update_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
        body: Optional[Union[EditAttachmentOptions, Mapping[str, Any]]] = None,
    ) -> Attachment:
        """Rename a release attachment (repoEditReleaseAttachment)."""
        return self._call(
            _repo_edit_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
            _body=body,
        )

    @checked
    def get_latest(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Release:
        """Get the latest release that is not a draft or prerelease (repoGetLatestRelease)."""
        return self._call(
            _repo_get_latest_release,
            owner=owner,
            repo=repo,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Release:
        """Get a release (repoGetRelease)."""
        return self._call(
            _repo_get_release,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def get_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> Attachment:
        """Get a release attachment (repoGetReleaseAttachment)."""
        return self._call(
            _repo_get_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    def get_by_tag(
        self,
        owner: StrictStr,
        repo: StrictStr,
        tag: StrictStr,
    ) -> Release:
        """Get a release by its tag name (repoGetReleaseByTag)."""
        return self._call(
            _repo_get_release_by_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    def list_attachments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> List[Attachment]:
        """List a release's attachments (repoListReleaseAttachments)."""
        return self._call(
            _repo_list_release_attachments,
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
        draft: Optional[StrictBool] = None,
        pre_release: Optional[StrictBool] = None,
        tag_filter: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Release]:
        """List one page of a repository's releases (repoListReleases)."""
        return self._call(
            _repo_list_releases,
            owner=owner,
            repo=repo,
            draft=draft,
            pre_release=pre_release,
            tag_filter=tag_filter,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        draft: Optional[StrictBool] = None,
        pre_release: Optional[StrictBool] = None,
        tag_filter: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Release]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_releases,
            owner=owner,
            repo=repo,
            draft=draft,
            pre_release=pre_release,
            tag_filter=tag_filter,
            page=page,
            limit=limit,
        )


class AsyncReleasesApi(AsyncResource):
    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateReleaseOption, Mapping[str, Any]]] = None,
    ) -> Release:
        """Create a release (repoCreateRelease)."""
        return await self._call(
            _repo_create_release,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def upload_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        name: Optional[StrictStr] = None,
        attachment: Optional[FileInput] = None,
    ) -> Attachment:
        """Upload an attachment to a release (repoCreateReleaseAttachment)."""
        return await self._call(
            _repo_create_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            name=name,
            attachment=attachment,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a release (repoDeleteRelease)."""
        return await self._call(
            _repo_delete_release,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def delete_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> None:
        """Delete a release attachment (repoDeleteReleaseAttachment)."""
        return await self._call(
            _repo_delete_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    async def delete_by_tag(
        self,
        owner: StrictStr,
        repo: StrictStr,
        tag: StrictStr,
    ) -> None:
        """Delete a release by its tag name (repoDeleteReleaseByTag)."""
        return await self._call(
            _repo_delete_release_by_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditReleaseOption, Mapping[str, Any]]] = None,
    ) -> Release:
        """Change a release (repoEditRelease)."""
        return await self._call(
            _repo_edit_release,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def update_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
        body: Optional[Union[EditAttachmentOptions, Mapping[str, Any]]] = None,
    ) -> Attachment:
        """Rename a release attachment (repoEditReleaseAttachment)."""
        return await self._call(
            _repo_edit_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
            _body=body,
        )

    @checked
    async def get_latest(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> Release:
        """Get the latest release that is not a draft or prerelease (repoGetLatestRelease)."""
        return await self._call(
            _repo_get_latest_release,
            owner=owner,
            repo=repo,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Release:
        """Get a release (repoGetRelease)."""
        return await self._call(
            _repo_get_release,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def get_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> Attachment:
        """Get a release attachment (repoGetReleaseAttachment)."""
        return await self._call(
            _repo_get_release_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    async def get_by_tag(
        self,
        owner: StrictStr,
        repo: StrictStr,
        tag: StrictStr,
    ) -> Release:
        """Get a release by its tag name (repoGetReleaseByTag)."""
        return await self._call(
            _repo_get_release_by_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    async def list_attachments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> List[Attachment]:
        """List a release's attachments (repoListReleaseAttachments)."""
        return await self._call(
            _repo_list_release_attachments,
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
        draft: Optional[StrictBool] = None,
        pre_release: Optional[StrictBool] = None,
        tag_filter: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Release]:
        """List one page of a repository's releases (repoListReleases)."""
        return await self._call(
            _repo_list_releases,
            owner=owner,
            repo=repo,
            draft=draft,
            pre_release=pre_release,
            tag_filter=tag_filter,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        draft: Optional[StrictBool] = None,
        pre_release: Optional[StrictBool] = None,
        tag_filter: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Release]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_releases,
            owner=owner,
            repo=repo,
            draft=draft,
            pre_release=pre_release,
            tag_filter=tag_filter,
            page=page,
            limit=limit,
        )
