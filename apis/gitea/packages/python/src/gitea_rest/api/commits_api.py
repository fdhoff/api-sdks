# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
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
from gitea_rest.models.combined_status import CombinedStatus
from gitea_rest.models.commit import Commit
from gitea_rest.models.commit_status import CommitStatus
from gitea_rest.models.compare import Compare
from gitea_rest.models.create_status_option import CreateStatusOption
from gitea_rest.models.pull_request import PullRequest

_repo_compare_diff: Operation[Compare] = Operation(
    id="repoCompareDiff",
    method="GET",
    path="/repos/{owner}/{repo}/compare/{basehead}",
    resource="commits",
    name="compare",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("basehead", "basehead", "path"),
        Param("output", "output", "query"),
        Param("verification", "verification", "query"),
        Param("files", "files", "query"),
    ),
    response=Compare,
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
_repo_create_status: Operation[CommitStatus] = Operation(
    id="repoCreateStatus",
    method="POST",
    path="/repos/{owner}/{repo}/statuses/{sha}",
    resource="commits",
    name="create_status",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
    ),
    response=CommitStatus,
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
_repo_download_commit_diff_or_patch: Operation[str] = Operation(
    id="repoDownloadCommitDiffOrPatch",
    method="GET",
    path="/repos/{owner}/{repo}/git/commits/{sha}.{diffType}",
    resource="commits",
    name="get_diff",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
        Param("diffType", "diff_type", "path"),
    ),
    response=str,
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
_repo_get_all_commits: Operation[List[Commit]] = Operation(
    id="repoGetAllCommits",
    method="GET",
    path="/repos/{owner}/{repo}/commits",
    resource="commits",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "query"),
        Param("path", "path", "query"),
        Param("since", "since", "query"),
        Param("until", "until", "query"),
        Param("stat", "stat", "query"),
        Param("verification", "verification", "query"),
        Param("files", "files", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("not", "var_not", "query"),
    ),
    response=List[Commit],
    returns_json=True,
    iterator="iter",
    item=_models.Commit,
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
_repo_get_combined_status_by_ref: Operation[CombinedStatus] = Operation(
    id="repoGetCombinedStatusByRef",
    method="GET",
    path="/repos/{owner}/{repo}/commits/{ref}/status",
    resource="commits",
    name="get_combined_status",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("ref", "ref", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=CombinedStatus,
    returns_json=True,
    iterator="iter_combined_status",
    item=_models.CommitStatus,
    paging=LinkHeader(
        items="statuses",
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
_repo_get_commit_pull_request: Operation[PullRequest] = Operation(
    id="repoGetCommitPullRequest",
    method="GET",
    path="/repos/{owner}/{repo}/commits/{sha}/pull",
    resource="commits",
    name="get_pull_request",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
    ),
    response=PullRequest,
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
_repo_get_single_commit: Operation[Commit] = Operation(
    id="repoGetSingleCommit",
    method="GET",
    path="/repos/{owner}/{repo}/git/commits/{sha}",
    resource="commits",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
        Param("stat", "stat", "query"),
        Param("verification", "verification", "query"),
        Param("files", "files", "query"),
    ),
    response=Commit,
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
_repo_list_statuses: Operation[List[CommitStatus]] = Operation(
    id="repoListStatuses",
    method="GET",
    path="/repos/{owner}/{repo}/statuses/{sha}",
    resource="commits",
    name="list_statuses",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("sha", "sha", "path"),
        Param("sort", "sort", "query"),
        Param("state", "state", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[CommitStatus],
    returns_json=True,
    iterator="iter_statuses",
    item=_models.CommitStatus,
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
_repo_list_statuses_by_ref: Operation[List[CommitStatus]] = Operation(
    id="repoListStatusesByRef",
    method="GET",
    path="/repos/{owner}/{repo}/commits/{ref}/statuses",
    resource="commits",
    name="list_statuses_for_ref",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("ref", "ref", "path"),
        Param("sort", "sort", "query"),
        Param("state", "state", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[CommitStatus],
    returns_json=True,
    iterator="iter_statuses_for_ref",
    item=_models.CommitStatus,
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
    _repo_compare_diff,
    _repo_create_status,
    _repo_download_commit_diff_or_patch,
    _repo_get_all_commits,
    _repo_get_combined_status_by_ref,
    _repo_get_commit_pull_request,
    _repo_get_single_commit,
    _repo_list_statuses,
    _repo_list_statuses_by_ref,
)


class CommitsApi(Resource):
    @checked
    def compare(
        self,
        owner: StrictStr,
        repo: StrictStr,
        basehead: StrictStr,
        *,
        output: Optional[StrictStr] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> Compare:
        """Compare two refs (repoCompareDiff)."""
        return self._call(
            _repo_compare_diff,
            owner=owner,
            repo=repo,
            basehead=basehead,
            output=output,
            verification=verification,
            files=files,
        )

    @checked
    def create_status(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        body: Optional[Union[CreateStatusOption, Mapping[str, Any]]] = None,
    ) -> CommitStatus:
        """Set a commit status (repoCreateStatus)."""
        return self._call(
            _repo_create_status,
            owner=owner,
            repo=repo,
            sha=sha,
            _body=body,
        )

    @checked
    def get_diff(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        diff_type: StrictStr,
    ) -> str:
        """Get a commit's diff or patch as text (repoDownloadCommitDiffOrPatch)."""
        return self._call(
            _repo_download_commit_diff_or_patch,
            owner=owner,
            repo=repo,
            sha=sha,
            diff_type=diff_type,
        )

    @checked
    def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        sha: Optional[StrictStr] = None,
        path: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        stat: Optional[StrictBool] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        var_not: Optional[StrictStr] = None,
    ) -> List[Commit]:
        """List one page of a repository's commits (repoGetAllCommits)."""
        return self._call(
            _repo_get_all_commits,
            owner=owner,
            repo=repo,
            sha=sha,
            path=path,
            since=since,
            until=until,
            stat=stat,
            verification=verification,
            files=files,
            page=page,
            limit=limit,
            var_not=var_not,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        sha: Optional[StrictStr] = None,
        path: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        stat: Optional[StrictBool] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        var_not: Optional[StrictStr] = None,
    ) -> Iterator[_models.Commit]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_all_commits,
            owner=owner,
            repo=repo,
            sha=sha,
            path=path,
            since=since,
            until=until,
            stat=stat,
            verification=verification,
            files=files,
            page=page,
            limit=limit,
            var_not=var_not,
        )

    @checked
    def get_combined_status(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> CombinedStatus:
        """Get the combined status of a branch, tag or commit, with one page of its statuses (repoGetCombinedStatusByRef)."""
        return self._call(
            _repo_get_combined_status_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            page=page,
            limit=limit,
        )

    @checked
    def iter_combined_status(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.CommitStatus]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_combined_status_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            page=page,
            limit=limit,
        )

    @checked
    def get_pull_request(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
    ) -> PullRequest:
        """Get the pull request that a commit was merged in (repoGetCommitPullRequest)."""
        return self._call(
            _repo_get_commit_pull_request,
            owner=owner,
            repo=repo,
            sha=sha,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        stat: Optional[StrictBool] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> Commit:
        """Get a commit (repoGetSingleCommit)."""
        return self._call(
            _repo_get_single_commit,
            owner=owner,
            repo=repo,
            sha=sha,
            stat=stat,
            verification=verification,
            files=files,
        )

    @checked
    def list_statuses(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[CommitStatus]:
        """List one page of a commit's statuses (repoListStatuses)."""
        return self._call(
            _repo_list_statuses,
            owner=owner,
            repo=repo,
            sha=sha,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_statuses(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.CommitStatus]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_statuses,
            owner=owner,
            repo=repo,
            sha=sha,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def list_statuses_for_ref(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[CommitStatus]:
        """List one page of the statuses of a branch, tag or commit (repoListStatusesByRef)."""
        return self._call(
            _repo_list_statuses_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_statuses_for_ref(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.CommitStatus]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_statuses_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )


class AsyncCommitsApi(AsyncResource):
    @checked
    async def compare(
        self,
        owner: StrictStr,
        repo: StrictStr,
        basehead: StrictStr,
        *,
        output: Optional[StrictStr] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> Compare:
        """Compare two refs (repoCompareDiff)."""
        return await self._call(
            _repo_compare_diff,
            owner=owner,
            repo=repo,
            basehead=basehead,
            output=output,
            verification=verification,
            files=files,
        )

    @checked
    async def create_status(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        body: Optional[Union[CreateStatusOption, Mapping[str, Any]]] = None,
    ) -> CommitStatus:
        """Set a commit status (repoCreateStatus)."""
        return await self._call(
            _repo_create_status,
            owner=owner,
            repo=repo,
            sha=sha,
            _body=body,
        )

    @checked
    async def get_diff(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        diff_type: StrictStr,
    ) -> str:
        """Get a commit's diff or patch as text (repoDownloadCommitDiffOrPatch)."""
        return await self._call(
            _repo_download_commit_diff_or_patch,
            owner=owner,
            repo=repo,
            sha=sha,
            diff_type=diff_type,
        )

    @checked
    async def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        sha: Optional[StrictStr] = None,
        path: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        stat: Optional[StrictBool] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        var_not: Optional[StrictStr] = None,
    ) -> List[Commit]:
        """List one page of a repository's commits (repoGetAllCommits)."""
        return await self._call(
            _repo_get_all_commits,
            owner=owner,
            repo=repo,
            sha=sha,
            path=path,
            since=since,
            until=until,
            stat=stat,
            verification=verification,
            files=files,
            page=page,
            limit=limit,
            var_not=var_not,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        sha: Optional[StrictStr] = None,
        path: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        stat: Optional[StrictBool] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        var_not: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Commit]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_all_commits,
            owner=owner,
            repo=repo,
            sha=sha,
            path=path,
            since=since,
            until=until,
            stat=stat,
            verification=verification,
            files=files,
            page=page,
            limit=limit,
            var_not=var_not,
        )

    @checked
    async def get_combined_status(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> CombinedStatus:
        """Get the combined status of a branch, tag or commit, with one page of its statuses (repoGetCombinedStatusByRef)."""
        return await self._call(
            _repo_get_combined_status_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            page=page,
            limit=limit,
        )

    @checked
    def iter_combined_status(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.CommitStatus]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_combined_status_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            page=page,
            limit=limit,
        )

    @checked
    async def get_pull_request(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
    ) -> PullRequest:
        """Get the pull request that a commit was merged in (repoGetCommitPullRequest)."""
        return await self._call(
            _repo_get_commit_pull_request,
            owner=owner,
            repo=repo,
            sha=sha,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        stat: Optional[StrictBool] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> Commit:
        """Get a commit (repoGetSingleCommit)."""
        return await self._call(
            _repo_get_single_commit,
            owner=owner,
            repo=repo,
            sha=sha,
            stat=stat,
            verification=verification,
            files=files,
        )

    @checked
    async def list_statuses(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[CommitStatus]:
        """List one page of a commit's statuses (repoListStatuses)."""
        return await self._call(
            _repo_list_statuses,
            owner=owner,
            repo=repo,
            sha=sha,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_statuses(
        self,
        owner: StrictStr,
        repo: StrictStr,
        sha: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.CommitStatus]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_statuses,
            owner=owner,
            repo=repo,
            sha=sha,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    async def list_statuses_for_ref(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[CommitStatus]:
        """List one page of the statuses of a branch, tag or commit (repoListStatusesByRef)."""
        return await self._call(
            _repo_list_statuses_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )

    @checked
    def iter_statuses_for_ref(
        self,
        owner: StrictStr,
        repo: StrictStr,
        ref: StrictStr,
        *,
        sort: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.CommitStatus]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_statuses_by_ref,
            owner=owner,
            repo=repo,
            ref=ref,
            sort=sort,
            state=state,
            page=page,
            limit=limit,
        )
