# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import AsyncResource, LinkHeader, Operation, Param, Resource, Scheme, checked
from gitea_rest.models.create_tag_option import CreateTagOption
from gitea_rest.models.create_tag_protection_option import CreateTagProtectionOption
from gitea_rest.models.edit_tag_protection_option import EditTagProtectionOption
from gitea_rest.models.tag import Tag
from gitea_rest.models.tag_protection import TagProtection

_repo_create_tag: Operation[Tag] = Operation(
    id="repoCreateTag",
    method="POST",
    path="/repos/{owner}/{repo}/tags",
    resource="tags",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Tag,
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
_repo_create_tag_protection: Operation[TagProtection] = Operation(
    id="repoCreateTagProtection",
    method="POST",
    path="/repos/{owner}/{repo}/tag_protections",
    resource="tags",
    name="create_protection",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=TagProtection,
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
_repo_delete_tag: Operation[None] = Operation(
    id="repoDeleteTag",
    method="DELETE",
    path="/repos/{owner}/{repo}/tags/{tag}",
    resource="tags",
    name="delete",
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
_repo_delete_tag_protection: Operation[None] = Operation(
    id="repoDeleteTagProtection",
    method="DELETE",
    path="/repos/{owner}/{repo}/tag_protections/{id}",
    resource="tags",
    name="delete_protection",
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
_repo_edit_tag_protection: Operation[TagProtection] = Operation(
    id="repoEditTagProtection",
    method="PATCH",
    path="/repos/{owner}/{repo}/tag_protections/{id}",
    resource="tags",
    name="update_protection",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=TagProtection,
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
_repo_get_tag: Operation[Tag] = Operation(
    id="repoGetTag",
    method="GET",
    path="/repos/{owner}/{repo}/tags/{tag}",
    resource="tags",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("tag", "tag", "path"),
    ),
    response=Tag,
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
_repo_get_tag_protection: Operation[TagProtection] = Operation(
    id="repoGetTagProtection",
    method="GET",
    path="/repos/{owner}/{repo}/tag_protections/{id}",
    resource="tags",
    name="get_protection",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=TagProtection,
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
_repo_list_tag_protection: Operation[List[TagProtection]] = Operation(
    id="repoListTagProtection",
    method="GET",
    path="/repos/{owner}/{repo}/tag_protections",
    resource="tags",
    name="list_protections",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[TagProtection],
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
_repo_list_tags: Operation[List[Tag]] = Operation(
    id="repoListTags",
    method="GET",
    path="/repos/{owner}/{repo}/tags",
    resource="tags",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Tag],
    returns_json=True,
    iterator="iter",
    item=_models.Tag,
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
    _repo_create_tag,
    _repo_create_tag_protection,
    _repo_delete_tag,
    _repo_delete_tag_protection,
    _repo_edit_tag_protection,
    _repo_get_tag,
    _repo_get_tag_protection,
    _repo_list_tag_protection,
    _repo_list_tags,
)


class TagsApi(Resource):
    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateTagOption, Mapping[str, Any]]] = None,
    ) -> Tag:
        """Create a tag (repoCreateTag)."""
        return self._call(
            _repo_create_tag,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def create_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateTagProtectionOption, Mapping[str, Any]]] = None,
    ) -> TagProtection:
        """Create a tag protection rule (repoCreateTagProtection)."""
        return self._call(
            _repo_create_tag_protection,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        tag: StrictStr,
    ) -> None:
        """Delete a tag (repoDeleteTag)."""
        return self._call(
            _repo_delete_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    def delete_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a tag protection rule (repoDeleteTagProtection)."""
        return self._call(
            _repo_delete_tag_protection,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def update_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditTagProtectionOption, Mapping[str, Any]]] = None,
    ) -> TagProtection:
        """Change a tag protection rule (repoEditTagProtection)."""
        return self._call(
            _repo_edit_tag_protection,
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
        tag: StrictStr,
    ) -> Tag:
        """Get a tag (repoGetTag)."""
        return self._call(
            _repo_get_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    def get_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> TagProtection:
        """Get a tag protection rule (repoGetTagProtection)."""
        return self._call(
            _repo_get_tag_protection,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def list_protections(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[TagProtection]:
        """List a repository's tag protection rules (repoListTagProtection)."""
        return self._call(
            _repo_list_tag_protection,
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
    ) -> List[Tag]:
        """List one page of a repository's tags (repoListTags)."""
        return self._call(
            _repo_list_tags,
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
    ) -> Iterator[_models.Tag]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_tags,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )


class AsyncTagsApi(AsyncResource):
    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateTagOption, Mapping[str, Any]]] = None,
    ) -> Tag:
        """Create a tag (repoCreateTag)."""
        return await self._call(
            _repo_create_tag,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def create_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateTagProtectionOption, Mapping[str, Any]]] = None,
    ) -> TagProtection:
        """Create a tag protection rule (repoCreateTagProtection)."""
        return await self._call(
            _repo_create_tag_protection,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        tag: StrictStr,
    ) -> None:
        """Delete a tag (repoDeleteTag)."""
        return await self._call(
            _repo_delete_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    async def delete_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete a tag protection rule (repoDeleteTagProtection)."""
        return await self._call(
            _repo_delete_tag_protection,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def update_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditTagProtectionOption, Mapping[str, Any]]] = None,
    ) -> TagProtection:
        """Change a tag protection rule (repoEditTagProtection)."""
        return await self._call(
            _repo_edit_tag_protection,
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
        tag: StrictStr,
    ) -> Tag:
        """Get a tag (repoGetTag)."""
        return await self._call(
            _repo_get_tag,
            owner=owner,
            repo=repo,
            tag=tag,
        )

    @checked
    async def get_protection(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> TagProtection:
        """Get a tag protection rule (repoGetTagProtection)."""
        return await self._call(
            _repo_get_tag_protection,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def list_protections(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[TagProtection]:
        """List a repository's tag protection rules (repoListTagProtection)."""
        return await self._call(
            _repo_list_tag_protection,
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
    ) -> List[Tag]:
        """List one page of a repository's tags (repoListTags)."""
        return await self._call(
            _repo_list_tags,
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
    ) -> AsyncIterator[_models.Tag]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_tags,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )
