# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, List, Mapping, Optional, Union

from pydantic import StrictStr

from gitea_rest._runtime import (
    AsyncDownload,
    AsyncResource,
    Download,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from gitea_rest.models.apply_diff_patch_file_options import ApplyDiffPatchFileOptions
from gitea_rest.models.change_files_options import ChangeFilesOptions
from gitea_rest.models.contents_ext_response import ContentsExtResponse
from gitea_rest.models.contents_response import ContentsResponse
from gitea_rest.models.create_file_options import CreateFileOptions
from gitea_rest.models.delete_file_options import DeleteFileOptions
from gitea_rest.models.file_delete_response import FileDeleteResponse
from gitea_rest.models.file_response import FileResponse
from gitea_rest.models.files_response import FilesResponse
from gitea_rest.models.get_files_options import GetFilesOptions
from gitea_rest.models.update_file_options import UpdateFileOptions

_repo_apply_diff_patch: Operation[FileResponse] = Operation(
    id="repoApplyDiffPatch",
    method="POST",
    path="/repos/{owner}/{repo}/diffpatch",
    resource="contents",
    name="apply_patch",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=FileResponse,
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
_repo_change_files: Operation[FilesResponse] = Operation(
    id="repoChangeFiles",
    method="POST",
    path="/repos/{owner}/{repo}/contents",
    resource="contents",
    name="change_files",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=FilesResponse,
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
_repo_create_file: Operation[FileResponse] = Operation(
    id="repoCreateFile",
    method="POST",
    path="/repos/{owner}/{repo}/contents/{filepath}",
    resource="contents",
    name="create_file",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
    ),
    response=FileResponse,
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
_repo_delete_file: Operation[FileDeleteResponse] = Operation(
    id="repoDeleteFile",
    method="DELETE",
    path="/repos/{owner}/{repo}/contents/{filepath}",
    resource="contents",
    name="delete_file",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
    ),
    response=FileDeleteResponse,
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
_repo_get_contents: Operation[ContentsResponse] = Operation(
    id="repoGetContents",
    method="GET",
    path="/repos/{owner}/{repo}/contents/{filepath}",
    resource="contents",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
        Param("ref", "ref", "query"),
    ),
    response=ContentsResponse,
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
_repo_get_contents_ext: Operation[ContentsExtResponse] = Operation(
    id="repoGetContentsExt",
    method="GET",
    path="/repos/{owner}/{repo}/contents-ext/{filepath}",
    resource="contents",
    name="get_extended",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
        Param("ref", "ref", "query"),
        Param("includes", "includes", "query"),
    ),
    response=ContentsExtResponse,
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
_repo_get_contents_list: Operation[List[ContentsResponse]] = Operation(
    id="repoGetContentsList",
    method="GET",
    path="/repos/{owner}/{repo}/contents",
    resource="contents",
    name="list_root",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("ref", "ref", "query"),
    ),
    response=List[ContentsResponse],
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
_repo_get_editor_config: Operation[None] = Operation(
    id="repoGetEditorConfig",
    method="GET",
    path="/repos/{owner}/{repo}/editorconfig/{filepath}",
    resource="contents",
    name="get_editorconfig",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
        Param("ref", "ref", "query"),
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
_repo_get_file_contents: Operation[List[ContentsResponse]] = Operation(
    id="repoGetFileContents",
    method="GET",
    path="/repos/{owner}/{repo}/file-contents",
    resource="contents",
    name="get_files",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("ref", "ref", "query"),
        Param("body", "body", "query"),
    ),
    response=List[ContentsResponse],
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
_repo_get_file_contents_post: Operation[List[ContentsResponse]] = Operation(
    id="repoGetFileContentsPost",
    method="POST",
    path="/repos/{owner}/{repo}/file-contents",
    resource="contents",
    name="get_files_by_body",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("ref", "ref", "query"),
    ),
    response=List[ContentsResponse],
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
_repo_get_raw_file: Operation[None] = Operation(
    id="repoGetRawFile",
    method="GET",
    path="/repos/{owner}/{repo}/raw/{filepath}",
    resource="contents",
    name="download_raw",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
        Param("ref", "ref", "query"),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
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
_repo_get_raw_file_or_lfs: Operation[None] = Operation(
    id="repoGetRawFileOrLFS",
    method="GET",
    path="/repos/{owner}/{repo}/media/{filepath}",
    resource="contents",
    name="download_media",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
        Param("ref", "ref", "query"),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
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
_repo_update_file: Operation[FileResponse] = Operation(
    id="repoUpdateFile",
    method="PUT",
    path="/repos/{owner}/{repo}/contents/{filepath}",
    resource="contents",
    name="update_file",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("filepath", "filepath", "path"),
    ),
    response=FileResponse,
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
    _repo_apply_diff_patch,
    _repo_change_files,
    _repo_create_file,
    _repo_delete_file,
    _repo_get_contents,
    _repo_get_contents_ext,
    _repo_get_contents_list,
    _repo_get_editor_config,
    _repo_get_file_contents,
    _repo_get_file_contents_post,
    _repo_get_raw_file,
    _repo_get_raw_file_or_lfs,
    _repo_update_file,
)


class ContentsApi(Resource):
    @checked
    def apply_patch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[ApplyDiffPatchFileOptions, Mapping[str, Any]],
    ) -> FileResponse:
        """Apply a diff in a new commit (repoApplyDiffPatch)."""
        return self._call(
            _repo_apply_diff_patch,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def change_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[ChangeFilesOptions, Mapping[str, Any]],
    ) -> FilesResponse:
        """Create, change or delete several files in one commit (repoChangeFiles)."""
        return self._call(
            _repo_change_files,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def create_file(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        body: Union[CreateFileOptions, Mapping[str, Any]],
    ) -> FileResponse:
        """Create a file in a new commit (repoCreateFile)."""
        return self._call(
            _repo_create_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            _body=body,
        )

    @checked
    def delete_file(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        body: Union[DeleteFileOptions, Mapping[str, Any]],
    ) -> FileDeleteResponse:
        """Delete a file in a new commit (repoDeleteFile)."""
        return self._call(
            _repo_delete_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            _body=body,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> ContentsResponse:
        """Get a file's content and metadata, or a directory's entries (repoGetContents)."""
        return self._call(
            _repo_get_contents,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    def get_extended(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
        includes: Optional[StrictStr] = None,
    ) -> ContentsExtResponse:
        """Get a file's or directory's metadata, with content as asked (repoGetContentsExt)."""
        return self._call(
            _repo_get_contents_ext,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
            includes=includes,
        )

    @checked
    def list_root(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> List[ContentsResponse]:
        """List the entries at the root of a repository (repoGetContentsList)."""
        return self._call(
            _repo_get_contents_list,
            owner=owner,
            repo=repo,
            ref=ref,
        )

    @checked
    def get_editorconfig(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> None:
        """Get the EditorConfig settings that apply to a file (repoGetEditorConfig)."""
        return self._call(
            _repo_get_editor_config,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    def get_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        body: StrictStr,
        ref: Optional[StrictStr] = None,
    ) -> List[ContentsResponse]:
        """Get the content and metadata of several files (repoGetFileContents)."""
        return self._call(
            _repo_get_file_contents,
            owner=owner,
            repo=repo,
            ref=ref,
            body=body,
        )

    @checked
    def get_files_by_body(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[GetFilesOptions, Mapping[str, Any]],
        *,
        ref: Optional[StrictStr] = None,
    ) -> List[ContentsResponse]:
        """Get the content and metadata of several files named in the body (repoGetFileContentsPost)."""
        return self._call(
            _repo_get_file_contents_post,
            owner=owner,
            repo=repo,
            _body=body,
            ref=ref,
        )

    @checked
    def download_raw(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> Download:
        """Download a file's raw content (repoGetRawFile). Close the download, or read it in a `with` block."""
        return self._download(
            _repo_get_raw_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    def download_media(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> Download:
        """Download a file's content, from Git LFS when it is stored there (repoGetRawFileOrLFS). Close the download, or read it in a `with` block."""
        return self._download(
            _repo_get_raw_file_or_lfs,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    def update_file(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        body: Union[UpdateFileOptions, Mapping[str, Any]],
    ) -> FileResponse:
        """Change a file in a new commit (repoUpdateFile)."""
        return self._call(
            _repo_update_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            _body=body,
        )


class AsyncContentsApi(AsyncResource):
    @checked
    async def apply_patch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[ApplyDiffPatchFileOptions, Mapping[str, Any]],
    ) -> FileResponse:
        """Apply a diff in a new commit (repoApplyDiffPatch)."""
        return await self._call(
            _repo_apply_diff_patch,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def change_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[ChangeFilesOptions, Mapping[str, Any]],
    ) -> FilesResponse:
        """Create, change or delete several files in one commit (repoChangeFiles)."""
        return await self._call(
            _repo_change_files,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def create_file(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        body: Union[CreateFileOptions, Mapping[str, Any]],
    ) -> FileResponse:
        """Create a file in a new commit (repoCreateFile)."""
        return await self._call(
            _repo_create_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            _body=body,
        )

    @checked
    async def delete_file(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        body: Union[DeleteFileOptions, Mapping[str, Any]],
    ) -> FileDeleteResponse:
        """Delete a file in a new commit (repoDeleteFile)."""
        return await self._call(
            _repo_delete_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            _body=body,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> ContentsResponse:
        """Get a file's content and metadata, or a directory's entries (repoGetContents)."""
        return await self._call(
            _repo_get_contents,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    async def get_extended(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
        includes: Optional[StrictStr] = None,
    ) -> ContentsExtResponse:
        """Get a file's or directory's metadata, with content as asked (repoGetContentsExt)."""
        return await self._call(
            _repo_get_contents_ext,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
            includes=includes,
        )

    @checked
    async def list_root(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> List[ContentsResponse]:
        """List the entries at the root of a repository (repoGetContentsList)."""
        return await self._call(
            _repo_get_contents_list,
            owner=owner,
            repo=repo,
            ref=ref,
        )

    @checked
    async def get_editorconfig(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> None:
        """Get the EditorConfig settings that apply to a file (repoGetEditorConfig)."""
        return await self._call(
            _repo_get_editor_config,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    async def get_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        body: StrictStr,
        ref: Optional[StrictStr] = None,
    ) -> List[ContentsResponse]:
        """Get the content and metadata of several files (repoGetFileContents)."""
        return await self._call(
            _repo_get_file_contents,
            owner=owner,
            repo=repo,
            ref=ref,
            body=body,
        )

    @checked
    async def get_files_by_body(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Union[GetFilesOptions, Mapping[str, Any]],
        *,
        ref: Optional[StrictStr] = None,
    ) -> List[ContentsResponse]:
        """Get the content and metadata of several files named in the body (repoGetFileContentsPost)."""
        return await self._call(
            _repo_get_file_contents_post,
            owner=owner,
            repo=repo,
            _body=body,
            ref=ref,
        )

    @checked
    async def download_raw(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> AsyncDownload:
        """Download a file's raw content (repoGetRawFile). Close the download, or read it in an `async with` block."""
        return await self._download(
            _repo_get_raw_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    async def download_media(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        *,
        ref: Optional[StrictStr] = None,
    ) -> AsyncDownload:
        """Download a file's content, from Git LFS when it is stored there (repoGetRawFileOrLFS). Close the download, or read it in an `async with` block."""
        return await self._download(
            _repo_get_raw_file_or_lfs,
            owner=owner,
            repo=repo,
            filepath=filepath,
            ref=ref,
        )

    @checked
    async def update_file(
        self,
        owner: StrictStr,
        repo: StrictStr,
        filepath: StrictStr,
        body: Union[UpdateFileOptions, Mapping[str, Any]],
    ) -> FileResponse:
        """Change a file in a new commit (repoUpdateFile)."""
        return await self._call(
            _repo_update_file,
            owner=owner,
            repo=repo,
            filepath=filepath,
            _body=body,
        )
