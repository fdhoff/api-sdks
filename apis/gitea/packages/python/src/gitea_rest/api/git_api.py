# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import List, Optional

from pydantic import StrictBool, StrictInt, StrictStr

from gitea_rest._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from gitea_rest.models.annotated_tag import AnnotatedTag
from gitea_rest.models.git_blob_response import GitBlobResponse
from gitea_rest.models.git_tree_response import GitTreeResponse
from gitea_rest.models.note import Note
from gitea_rest.models.reference import Reference

_get_annotated_tag: Operation[AnnotatedTag] = Operation(
    id="GetAnnotatedTag",
    method="GET",
    path="/repos/{owner}/{repo}/git/tags/{sha}",
    resource="git",
    name="get_tag",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
    ),
    response=AnnotatedTag,
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
_get_blob: Operation[GitBlobResponse] = Operation(
    id="GetBlob",
    method="GET",
    path="/repos/{owner}/{repo}/git/blobs/{sha}",
    resource="git",
    name="get_blob",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
    ),
    response=GitBlobResponse,
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
_get_tree: Operation[GitTreeResponse] = Operation(
    id="GetTree",
    method="GET",
    path="/repos/{owner}/{repo}/git/trees/{sha}",
    resource="git",
    name="get_tree",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
        Param("recursive", "recursive", "query"),
        Param("page", "page", "query"),
        Param("per_page", "per_page", "query"),
    ),
    response=GitTreeResponse,
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
_repo_get_note: Operation[Note] = Operation(
    id="repoGetNote",
    method="GET",
    path="/repos/{owner}/{repo}/git/notes/{sha}",
    resource="git",
    name="get_note",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
        Param("verification", "verification", "query"),
        Param("files", "files", "query"),
    ),
    response=Note,
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
_repo_list_all_git_refs: Operation[List[Reference]] = Operation(
    id="repoListAllGitRefs",
    method="GET",
    path="/repos/{owner}/{repo}/git/refs",
    resource="git",
    name="list_refs",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[Reference],
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
_repo_list_git_refs: Operation[List[Reference]] = Operation(
    id="repoListGitRefs",
    method="GET",
    path="/repos/{owner}/{repo}/git/refs/{ref}",
    resource="git",
    name="list_refs_matching",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("ref", "ref", "path"),
    ),
    response=List[Reference],
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

OPERATIONS = (
    _get_annotated_tag,
    _get_blob,
    _get_tree,
    _repo_get_note,
    _repo_list_all_git_refs,
    _repo_list_git_refs,
)


class GitApi(Resource):
    @checked
    def get_tag(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
    ) -> AnnotatedTag:
        """Get an annotated tag object (GetAnnotatedTag)."""
        return self._call(
            _get_annotated_tag,
            owner=owner,
            repo=repo,
            sha=sha,
        )

    @checked
    def get_blob(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
    ) -> GitBlobResponse:
        """Get a blob (GetBlob)."""
        return self._call(
            _get_blob,
            owner=owner,
            repo=repo,
            sha=sha,
        )

    @checked
    def get_tree(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        recursive: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[StrictInt] = None,
    ) -> GitTreeResponse:
        """Get a tree (GetTree)."""
        return self._call(
            _get_tree,
            owner=owner,
            repo=repo,
            sha=sha,
            recursive=recursive,
            page=page,
            per_page=per_page,
        )

    @checked
    def get_note(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> Note:
        """Get the note attached to a commit (repoGetNote)."""
        return self._call(
            _repo_get_note,
            owner=owner,
            repo=repo,
            sha=sha,
            verification=verification,
            files=files,
        )

    @checked
    def list_refs(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[Reference]:
        """List a repository's refs (repoListAllGitRefs)."""
        return self._call(
            _repo_list_all_git_refs,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_refs_matching(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
    ) -> List[Reference]:
        """List the refs that start with a prefix, such as heads (repoListGitRefs)."""
        return self._call(
            _repo_list_git_refs,
            owner=owner,
            repo=repo,
            ref=ref,
        )


class AsyncGitApi(AsyncResource):
    @checked
    async def get_tag(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
    ) -> AnnotatedTag:
        """Get an annotated tag object (GetAnnotatedTag)."""
        return await self._call(
            _get_annotated_tag,
            owner=owner,
            repo=repo,
            sha=sha,
        )

    @checked
    async def get_blob(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
    ) -> GitBlobResponse:
        """Get a blob (GetBlob)."""
        return await self._call(
            _get_blob,
            owner=owner,
            repo=repo,
            sha=sha,
        )

    @checked
    async def get_tree(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        recursive: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[StrictInt] = None,
    ) -> GitTreeResponse:
        """Get a tree (GetTree)."""
        return await self._call(
            _get_tree,
            owner=owner,
            repo=repo,
            sha=sha,
            recursive=recursive,
            page=page,
            per_page=per_page,
        )

    @checked
    async def get_note(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> Note:
        """Get the note attached to a commit (repoGetNote)."""
        return await self._call(
            _repo_get_note,
            owner=owner,
            repo=repo,
            sha=sha,
            verification=verification,
            files=files,
        )

    @checked
    async def list_refs(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[Reference]:
        """List a repository's refs (repoListAllGitRefs)."""
        return await self._call(
            _repo_list_all_git_refs,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_refs_matching(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
    ) -> List[Reference]:
        """List the refs that start with a prefix, such as heads (repoListGitRefs)."""
        return await self._call(
            _repo_list_git_refs,
            owner=owner,
            repo=repo,
            ref=ref,
        )
