# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import AsyncResource, LinkHeader, Operation, Param, Resource, Scheme, checked
from gitea_rest.models.create_wiki_page_options import CreateWikiPageOptions
from gitea_rest.models.wiki_commit_list import WikiCommitList
from gitea_rest.models.wiki_page import WikiPage
from gitea_rest.models.wiki_page_meta_data import WikiPageMetaData

_repo_create_wiki_page: Operation[WikiPage] = Operation(
    id="repoCreateWikiPage",
    method="POST",
    path="/repos/{owner}/{repo}/wiki/new",
    resource="wiki",
    name="create_page",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=WikiPage,
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
_repo_delete_wiki_page: Operation[None] = Operation(
    id="repoDeleteWikiPage",
    method="DELETE",
    path="/repos/{owner}/{repo}/wiki/page/{pageName}",
    resource="wiki",
    name="delete_page",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("pageName", "page_name", "path"),
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
_repo_edit_wiki_page: Operation[WikiPage] = Operation(
    id="repoEditWikiPage",
    method="PATCH",
    path="/repos/{owner}/{repo}/wiki/page/{pageName}",
    resource="wiki",
    name="update_page",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("pageName", "page_name", "path"),
    ),
    response=WikiPage,
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
_repo_get_wiki_page: Operation[WikiPage] = Operation(
    id="repoGetWikiPage",
    method="GET",
    path="/repos/{owner}/{repo}/wiki/page/{pageName}",
    resource="wiki",
    name="get_page",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("pageName", "page_name", "path"),
    ),
    response=WikiPage,
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
_repo_get_wiki_page_revisions: Operation[WikiCommitList] = Operation(
    id="repoGetWikiPageRevisions",
    method="GET",
    path="/repos/{owner}/{repo}/wiki/revisions/{pageName}",
    resource="wiki",
    name="list_page_revisions",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("pageName", "page_name", "path"),
        Param("page", "page", "query"),
    ),
    response=WikiCommitList,
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
_repo_get_wiki_pages: Operation[List[WikiPageMetaData]] = Operation(
    id="repoGetWikiPages",
    method="GET",
    path="/repos/{owner}/{repo}/wiki/pages",
    resource="wiki",
    name="list_pages",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[WikiPageMetaData],
    returns_json=True,
    iterator="iter_pages",
    item=_models.WikiPageMetaData,
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
    _repo_create_wiki_page,
    _repo_delete_wiki_page,
    _repo_edit_wiki_page,
    _repo_get_wiki_page,
    _repo_get_wiki_page_revisions,
    _repo_get_wiki_pages,
)


class WikiApi(Resource):
    @checked
    def create_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateWikiPageOptions, Mapping[str, Any]]] = None,
    ) -> WikiPage:
        """Create a wiki page (repoCreateWikiPage)."""
        return self._call(
            _repo_create_wiki_page,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def delete_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
    ) -> None:
        """Delete a wiki page (repoDeleteWikiPage)."""
        return self._call(
            _repo_delete_wiki_page,
            owner=owner,
            repo=repo,
            page_name=page_name,
        )

    @checked
    def update_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
        body: Optional[Union[CreateWikiPageOptions, Mapping[str, Any]]] = None,
    ) -> WikiPage:
        """Change a wiki page (repoEditWikiPage)."""
        return self._call(
            _repo_edit_wiki_page,
            owner=owner,
            repo=repo,
            page_name=page_name,
            _body=body,
        )

    @checked
    def get_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
    ) -> WikiPage:
        """Get a wiki page (repoGetWikiPage)."""
        return self._call(
            _repo_get_wiki_page,
            owner=owner,
            repo=repo,
            page_name=page_name,
        )

    @checked
    def list_page_revisions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
        *,
        page: Optional[StrictInt] = None,
    ) -> WikiCommitList:
        """List a wiki page's revisions (repoGetWikiPageRevisions)."""
        return self._call(
            _repo_get_wiki_page_revisions,
            owner=owner,
            repo=repo,
            page_name=page_name,
            page=page,
        )

    @checked
    def list_pages(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[WikiPageMetaData]:
        """List one page of a repository's wiki pages (repoGetWikiPages)."""
        return self._call(
            _repo_get_wiki_pages,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_pages(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.WikiPageMetaData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_wiki_pages,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )


class AsyncWikiApi(AsyncResource):
    @checked
    async def create_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateWikiPageOptions, Mapping[str, Any]]] = None,
    ) -> WikiPage:
        """Create a wiki page (repoCreateWikiPage)."""
        return await self._call(
            _repo_create_wiki_page,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def delete_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
    ) -> None:
        """Delete a wiki page (repoDeleteWikiPage)."""
        return await self._call(
            _repo_delete_wiki_page,
            owner=owner,
            repo=repo,
            page_name=page_name,
        )

    @checked
    async def update_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
        body: Optional[Union[CreateWikiPageOptions, Mapping[str, Any]]] = None,
    ) -> WikiPage:
        """Change a wiki page (repoEditWikiPage)."""
        return await self._call(
            _repo_edit_wiki_page,
            owner=owner,
            repo=repo,
            page_name=page_name,
            _body=body,
        )

    @checked
    async def get_page(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
    ) -> WikiPage:
        """Get a wiki page (repoGetWikiPage)."""
        return await self._call(
            _repo_get_wiki_page,
            owner=owner,
            repo=repo,
            page_name=page_name,
        )

    @checked
    async def list_page_revisions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        page_name: StrictStr,
        *,
        page: Optional[StrictInt] = None,
    ) -> WikiCommitList:
        """List a wiki page's revisions (repoGetWikiPageRevisions)."""
        return await self._call(
            _repo_get_wiki_page_revisions,
            owner=owner,
            repo=repo,
            page_name=page_name,
            page=page,
        )

    @checked
    async def list_pages(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[WikiPageMetaData]:
        """List one page of a repository's wiki pages (repoGetWikiPages)."""
        return await self._call(
            _repo_get_wiki_pages,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )

    @checked
    def iter_pages(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.WikiPageMetaData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_wiki_pages,
            owner=owner,
            repo=repo,
            page=page,
            limit=limit,
        )
