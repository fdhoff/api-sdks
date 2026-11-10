# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated

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
from gitea_rest.models.changed_file import ChangedFile
from gitea_rest.models.commit import Commit
from gitea_rest.models.create_pull_request_option import CreatePullRequestOption
from gitea_rest.models.create_pull_review_comment_reply_options import CreatePullReviewCommentReplyOptions
from gitea_rest.models.create_pull_review_options import CreatePullReviewOptions
from gitea_rest.models.dismiss_pull_review_options import DismissPullReviewOptions
from gitea_rest.models.edit_pull_request_option import EditPullRequestOption
from gitea_rest.models.merge_pull_request_option import MergePullRequestOption
from gitea_rest.models.pull_request import PullRequest
from gitea_rest.models.pull_review import PullReview
from gitea_rest.models.pull_review_comment import PullReviewComment
from gitea_rest.models.pull_review_request_options import PullReviewRequestOptions
from gitea_rest.models.submit_pull_review_options import SubmitPullReviewOptions

_repo_cancel_scheduled_auto_merge: Operation[None] = Operation(
    id="repoCancelScheduledAutoMerge",
    method="DELETE",
    path="/repos/{owner}/{repo}/pulls/{index}/merge",
    resource="pulls",
    name="cancel_auto_merge",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_repo_create_pull_request: Operation[PullRequest] = Operation(
    id="repoCreatePullRequest",
    method="POST",
    path="/repos/{owner}/{repo}/pulls",
    resource="pulls",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
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
_repo_create_pull_review: Operation[PullReview] = Operation(
    id="repoCreatePullReview",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews",
    resource="pulls",
    name="create_review",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=PullReview,
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
_repo_create_pull_review_comment_reply: Operation[PullReviewComment] = Operation(
    id="repoCreatePullReviewCommentReply",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/comments/{id}/replies",
    resource="pulls",
    name="reply_to_review_comment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("id", "id", "path"),
    ),
    response=PullReviewComment,
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
_repo_create_pull_review_requests: Operation[List[PullReview]] = Operation(
    id="repoCreatePullReviewRequests",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/requested_reviewers",
    resource="pulls",
    name="request_reviews",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=List[PullReview],
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
_repo_delete_pull_review: Operation[None] = Operation(
    id="repoDeletePullReview",
    method="DELETE",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}",
    resource="pulls",
    name="delete_review",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_repo_delete_pull_review_requests: Operation[None] = Operation(
    id="repoDeletePullReviewRequests",
    method="DELETE",
    path="/repos/{owner}/{repo}/pulls/{index}/requested_reviewers",
    resource="pulls",
    name="cancel_review_requests",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_repo_dismiss_pull_review: Operation[PullReview] = Operation(
    id="repoDismissPullReview",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals",
    resource="pulls",
    name="dismiss_review",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("id", "id", "path"),
    ),
    response=PullReview,
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
_repo_download_pull_diff_or_patch: Operation[str] = Operation(
    id="repoDownloadPullDiffOrPatch",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}.{diffType}",
    resource="pulls",
    name="get_diff",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("diffType", "diff_type", "path"),
        Param("binary", "binary", "query"),
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
_repo_edit_pull_request: Operation[PullRequest] = Operation(
    id="repoEditPullRequest",
    method="PATCH",
    path="/repos/{owner}/{repo}/pulls/{index}",
    resource="pulls",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_repo_get_pull_request: Operation[PullRequest] = Operation(
    id="repoGetPullRequest",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}",
    resource="pulls",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_repo_get_pull_request_by_base_head: Operation[PullRequest] = Operation(
    id="repoGetPullRequestByBaseHead",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{base}/{head}",
    resource="pulls",
    name="get_by_branches",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("base", "base", "path"),
        Param("head", "head", "path"),
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
_repo_get_pull_request_commits: Operation[List[Commit]] = Operation(
    id="repoGetPullRequestCommits",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}/commits",
    resource="pulls",
    name="list_commits",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("verification", "verification", "query"),
        Param("files", "files", "query"),
    ),
    response=List[Commit],
    returns_json=True,
    iterator="iter_commits",
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
_repo_get_pull_request_files: Operation[List[ChangedFile]] = Operation(
    id="repoGetPullRequestFiles",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}/files",
    resource="pulls",
    name="list_files",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("skip-to", "skip_to", "query"),
        Param("whitespace", "whitespace", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[ChangedFile],
    returns_json=True,
    iterator="iter_files",
    item=_models.ChangedFile,
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
_repo_get_pull_review: Operation[PullReview] = Operation(
    id="repoGetPullReview",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}",
    resource="pulls",
    name="get_review",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("id", "id", "path"),
    ),
    response=PullReview,
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
_repo_get_pull_review_comments: Operation[List[PullReviewComment]] = Operation(
    id="repoGetPullReviewComments",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments",
    resource="pulls",
    name="list_review_comments",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("id", "id", "path"),
    ),
    response=List[PullReviewComment],
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
_repo_list_pinned_pull_requests: Operation[List[PullRequest]] = Operation(
    id="repoListPinnedPullRequests",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/pinned",
    resource="pulls",
    name="list_pinned",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[PullRequest],
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
_repo_list_pull_requests: Operation[List[PullRequest]] = Operation(
    id="repoListPullRequests",
    method="GET",
    path="/repos/{owner}/{repo}/pulls",
    resource="pulls",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("base_branch", "base_branch", "query"),
        Param("state", "state", "query"),
        Param("sort", "sort", "query"),
        Param("milestone", "milestone", "query"),
        Param("labels", "labels", "query"),
        Param("poster", "poster", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[PullRequest],
    returns_json=True,
    iterator="iter",
    item=_models.PullRequest,
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
_repo_list_pull_reviews: Operation[List[PullReview]] = Operation(
    id="repoListPullReviews",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews",
    resource="pulls",
    name="list_reviews",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[PullReview],
    returns_json=True,
    iterator="iter_reviews",
    item=_models.PullReview,
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
_repo_merge_pull_request: Operation[None] = Operation(
    id="repoMergePullRequest",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/merge",
    resource="pulls",
    name="merge",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_repo_pull_request_is_merged: Operation[None] = Operation(
    id="repoPullRequestIsMerged",
    method="GET",
    path="/repos/{owner}/{repo}/pulls/{index}/merge",
    resource="pulls",
    name="check_merged",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_repo_resolve_pull_review_comment: Operation[None] = Operation(
    id="repoResolvePullReviewComment",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/comments/{id}/resolve",
    resource="pulls",
    name="resolve_review_comment",
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
_repo_submit_pull_review: Operation[PullReview] = Operation(
    id="repoSubmitPullReview",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}",
    resource="pulls",
    name="submit_review",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("id", "id", "path"),
    ),
    response=PullReview,
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
_repo_un_dismiss_pull_review: Operation[PullReview] = Operation(
    id="repoUnDismissPullReview",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals",
    resource="pulls",
    name="undismiss_review",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("id", "id", "path"),
    ),
    response=PullReview,
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
_repo_unresolve_pull_review_comment: Operation[None] = Operation(
    id="repoUnresolvePullReviewComment",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/comments/{id}/unresolve",
    resource="pulls",
    name="unresolve_review_comment",
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
_repo_update_pull_request: Operation[None] = Operation(
    id="repoUpdatePullRequest",
    method="POST",
    path="/repos/{owner}/{repo}/pulls/{index}/update",
    resource="pulls",
    name="update_branch",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("style", "style", "query"),
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

OPERATIONS = (
    _repo_cancel_scheduled_auto_merge,
    _repo_create_pull_request,
    _repo_create_pull_review,
    _repo_create_pull_review_comment_reply,
    _repo_create_pull_review_requests,
    _repo_delete_pull_review,
    _repo_delete_pull_review_requests,
    _repo_dismiss_pull_review,
    _repo_download_pull_diff_or_patch,
    _repo_edit_pull_request,
    _repo_get_pull_request,
    _repo_get_pull_request_by_base_head,
    _repo_get_pull_request_commits,
    _repo_get_pull_request_files,
    _repo_get_pull_review,
    _repo_get_pull_review_comments,
    _repo_list_pinned_pull_requests,
    _repo_list_pull_requests,
    _repo_list_pull_reviews,
    _repo_merge_pull_request,
    _repo_pull_request_is_merged,
    _repo_resolve_pull_review_comment,
    _repo_submit_pull_review,
    _repo_un_dismiss_pull_review,
    _repo_unresolve_pull_review_comment,
    _repo_update_pull_request,
)


class PullsApi(Resource):
    @checked
    def cancel_auto_merge(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Cancel a pull request's scheduled merge (repoCancelScheduledAutoMerge)."""
        return self._call(
            _repo_cancel_scheduled_auto_merge,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreatePullRequestOption, Mapping[str, Any]]] = None,
    ) -> PullRequest:
        """Open a pull request (repoCreatePullRequest)."""
        return self._call(
            _repo_create_pull_request,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def create_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[CreatePullReviewOptions, Mapping[str, Any]],
    ) -> PullReview:
        """Start a review of a pull request (repoCreatePullReview)."""
        return self._call(
            _repo_create_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def reply_to_review_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
        body: Union[CreatePullReviewCommentReplyOptions, Mapping[str, Any]],
    ) -> PullReviewComment:
        """Reply to a review comment (repoCreatePullReviewCommentReply)."""
        return self._call(
            _repo_create_pull_review_comment_reply,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
            _body=body,
        )

    @checked
    def request_reviews(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[PullReviewRequestOptions, Mapping[str, Any]],
    ) -> List[PullReview]:
        """Ask users or teams to review a pull request (repoCreatePullReviewRequests)."""
        return self._call(
            _repo_create_pull_review_requests,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def delete_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> None:
        """Delete a pull request review (repoDeletePullReview)."""
        return self._call(
            _repo_delete_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    def cancel_review_requests(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[PullReviewRequestOptions, Mapping[str, Any]],
    ) -> None:
        """Withdraw review requests from a pull request (repoDeletePullReviewRequests)."""
        return self._call(
            _repo_delete_pull_review_requests,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def dismiss_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
        body: Union[DismissPullReviewOptions, Mapping[str, Any]],
    ) -> PullReview:
        """Dismiss a pull request review (repoDismissPullReview)."""
        return self._call(
            _repo_dismiss_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
            _body=body,
        )

    @checked
    def get_diff(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        diff_type: StrictStr,
        *,
        binary: Optional[StrictBool] = None,
    ) -> str:
        """Get a pull request's diff or patch as text (repoDownloadPullDiffOrPatch)."""
        return self._call(
            _repo_download_pull_diff_or_patch,
            owner=owner,
            repo=repo,
            index=index,
            diff_type=diff_type,
            binary=binary,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditPullRequestOption, Mapping[str, Any]]] = None,
    ) -> PullRequest:
        """Change a pull request (repoEditPullRequest)."""
        return self._call(
            _repo_edit_pull_request,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> PullRequest:
        """Get a pull request (repoGetPullRequest)."""
        return self._call(
            _repo_get_pull_request,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def get_by_branches(
        self,
        owner: StrictStr,
        repo: StrictStr,
        base: StrictStr,
        head: StrictStr,
    ) -> PullRequest:
        """Get the pull request from a head branch into a base branch (repoGetPullRequestByBaseHead)."""
        return self._call(
            _repo_get_pull_request_by_base_head,
            owner=owner,
            repo=repo,
            base=base,
            head=head,
        )

    @checked
    def list_commits(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> List[Commit]:
        """List one page of a pull request's commits (repoGetPullRequestCommits)."""
        return self._call(
            _repo_get_pull_request_commits,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
            verification=verification,
            files=files,
        )

    @checked
    def iter_commits(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> Iterator[_models.Commit]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_pull_request_commits,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
            verification=verification,
            files=files,
        )

    @checked
    def list_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        skip_to: Optional[StrictStr] = None,
        whitespace: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ChangedFile]:
        """List one page of the files a pull request changes (repoGetPullRequestFiles)."""
        return self._call(
            _repo_get_pull_request_files,
            owner=owner,
            repo=repo,
            index=index,
            skip_to=skip_to,
            whitespace=whitespace,
            page=page,
            limit=limit,
        )

    @checked
    def iter_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        skip_to: Optional[StrictStr] = None,
        whitespace: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.ChangedFile]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_pull_request_files,
            owner=owner,
            repo=repo,
            index=index,
            skip_to=skip_to,
            whitespace=whitespace,
            page=page,
            limit=limit,
        )

    @checked
    def get_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> PullReview:
        """Get a pull request review (repoGetPullReview)."""
        return self._call(
            _repo_get_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    def list_review_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> List[PullReviewComment]:
        """List a review's comments (repoGetPullReviewComments)."""
        return self._call(
            _repo_get_pull_review_comments,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    def list_pinned(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[PullRequest]:
        """List a repository's pinned pull requests (repoListPinnedPullRequests)."""
        return self._call(
            _repo_list_pinned_pull_requests,
            owner=owner,
            repo=repo,
        )

    @checked
    def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        base_branch: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        milestone: Optional[StrictInt] = None,
        labels: Optional[List[StrictInt]] = None,
        poster: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> List[PullRequest]:
        """List one page of a repository's pull requests (repoListPullRequests)."""
        return self._call(
            _repo_list_pull_requests,
            owner=owner,
            repo=repo,
            base_branch=base_branch,
            state=state,
            sort=sort,
            milestone=milestone,
            labels=labels,
            poster=poster,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        base_branch: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        milestone: Optional[StrictInt] = None,
        labels: Optional[List[StrictInt]] = None,
        poster: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.PullRequest]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_pull_requests,
            owner=owner,
            repo=repo,
            base_branch=base_branch,
            state=state,
            sort=sort,
            milestone=milestone,
            labels=labels,
            poster=poster,
            page=page,
            limit=limit,
        )

    @checked
    def list_reviews(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PullReview]:
        """List one page of a pull request's reviews (repoListPullReviews)."""
        return self._call(
            _repo_list_pull_reviews,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_reviews(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.PullReview]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_pull_reviews,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def merge(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[MergePullRequestOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Merge a pull request (repoMergePullRequest)."""
        return self._call(
            _repo_merge_pull_request,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def check_merged(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Check whether a pull request is merged (repoPullRequestIsMerged)."""
        return self._call(
            _repo_pull_request_is_merged,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def resolve_review_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Mark a review comment's conversation resolved (repoResolvePullReviewComment)."""
        return self._call(
            _repo_resolve_pull_review_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def submit_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
        body: Union[SubmitPullReviewOptions, Mapping[str, Any]],
    ) -> PullReview:
        """Submit a pending pull request review (repoSubmitPullReview)."""
        return self._call(
            _repo_submit_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
            _body=body,
        )

    @checked
    def undismiss_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> PullReview:
        """Restore a dismissed pull request review (repoUnDismissPullReview)."""
        return self._call(
            _repo_un_dismiss_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    def unresolve_review_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Mark a review comment's conversation unresolved (repoUnresolvePullReviewComment)."""
        return self._call(
            _repo_unresolve_pull_review_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def update_branch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        style: Optional[StrictStr] = None,
    ) -> None:
        """Merge or rebase a pull request's base branch into its head branch (repoUpdatePullRequest)."""
        return self._call(
            _repo_update_pull_request,
            owner=owner,
            repo=repo,
            index=index,
            style=style,
        )


class AsyncPullsApi(AsyncResource):
    @checked
    async def cancel_auto_merge(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Cancel a pull request's scheduled merge (repoCancelScheduledAutoMerge)."""
        return await self._call(
            _repo_cancel_scheduled_auto_merge,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreatePullRequestOption, Mapping[str, Any]]] = None,
    ) -> PullRequest:
        """Open a pull request (repoCreatePullRequest)."""
        return await self._call(
            _repo_create_pull_request,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def create_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[CreatePullReviewOptions, Mapping[str, Any]],
    ) -> PullReview:
        """Start a review of a pull request (repoCreatePullReview)."""
        return await self._call(
            _repo_create_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def reply_to_review_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
        body: Union[CreatePullReviewCommentReplyOptions, Mapping[str, Any]],
    ) -> PullReviewComment:
        """Reply to a review comment (repoCreatePullReviewCommentReply)."""
        return await self._call(
            _repo_create_pull_review_comment_reply,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
            _body=body,
        )

    @checked
    async def request_reviews(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[PullReviewRequestOptions, Mapping[str, Any]],
    ) -> List[PullReview]:
        """Ask users or teams to review a pull request (repoCreatePullReviewRequests)."""
        return await self._call(
            _repo_create_pull_review_requests,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def delete_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> None:
        """Delete a pull request review (repoDeletePullReview)."""
        return await self._call(
            _repo_delete_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    async def cancel_review_requests(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[PullReviewRequestOptions, Mapping[str, Any]],
    ) -> None:
        """Withdraw review requests from a pull request (repoDeletePullReviewRequests)."""
        return await self._call(
            _repo_delete_pull_review_requests,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def dismiss_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
        body: Union[DismissPullReviewOptions, Mapping[str, Any]],
    ) -> PullReview:
        """Dismiss a pull request review (repoDismissPullReview)."""
        return await self._call(
            _repo_dismiss_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
            _body=body,
        )

    @checked
    async def get_diff(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        diff_type: StrictStr,
        *,
        binary: Optional[StrictBool] = None,
    ) -> str:
        """Get a pull request's diff or patch as text (repoDownloadPullDiffOrPatch)."""
        return await self._call(
            _repo_download_pull_diff_or_patch,
            owner=owner,
            repo=repo,
            index=index,
            diff_type=diff_type,
            binary=binary,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditPullRequestOption, Mapping[str, Any]]] = None,
    ) -> PullRequest:
        """Change a pull request (repoEditPullRequest)."""
        return await self._call(
            _repo_edit_pull_request,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> PullRequest:
        """Get a pull request (repoGetPullRequest)."""
        return await self._call(
            _repo_get_pull_request,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def get_by_branches(
        self,
        owner: StrictStr,
        repo: StrictStr,
        base: StrictStr,
        head: StrictStr,
    ) -> PullRequest:
        """Get the pull request from a head branch into a base branch (repoGetPullRequestByBaseHead)."""
        return await self._call(
            _repo_get_pull_request_by_base_head,
            owner=owner,
            repo=repo,
            base=base,
            head=head,
        )

    @checked
    async def list_commits(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> List[Commit]:
        """List one page of a pull request's commits (repoGetPullRequestCommits)."""
        return await self._call(
            _repo_get_pull_request_commits,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
            verification=verification,
            files=files,
        )

    @checked
    def iter_commits(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        verification: Optional[StrictBool] = None,
        files: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.Commit]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_pull_request_commits,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
            verification=verification,
            files=files,
        )

    @checked
    async def list_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        skip_to: Optional[StrictStr] = None,
        whitespace: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[ChangedFile]:
        """List one page of the files a pull request changes (repoGetPullRequestFiles)."""
        return await self._call(
            _repo_get_pull_request_files,
            owner=owner,
            repo=repo,
            index=index,
            skip_to=skip_to,
            whitespace=whitespace,
            page=page,
            limit=limit,
        )

    @checked
    def iter_files(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        skip_to: Optional[StrictStr] = None,
        whitespace: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.ChangedFile]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_get_pull_request_files,
            owner=owner,
            repo=repo,
            index=index,
            skip_to=skip_to,
            whitespace=whitespace,
            page=page,
            limit=limit,
        )

    @checked
    async def get_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> PullReview:
        """Get a pull request review (repoGetPullReview)."""
        return await self._call(
            _repo_get_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    async def list_review_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> List[PullReviewComment]:
        """List a review's comments (repoGetPullReviewComments)."""
        return await self._call(
            _repo_get_pull_review_comments,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    async def list_pinned(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[PullRequest]:
        """List a repository's pinned pull requests (repoListPinnedPullRequests)."""
        return await self._call(
            _repo_list_pinned_pull_requests,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        base_branch: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        milestone: Optional[StrictInt] = None,
        labels: Optional[List[StrictInt]] = None,
        poster: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> List[PullRequest]:
        """List one page of a repository's pull requests (repoListPullRequests)."""
        return await self._call(
            _repo_list_pull_requests,
            owner=owner,
            repo=repo,
            base_branch=base_branch,
            state=state,
            sort=sort,
            milestone=milestone,
            labels=labels,
            poster=poster,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        base_branch: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        milestone: Optional[StrictInt] = None,
        labels: Optional[List[StrictInt]] = None,
        poster: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.PullRequest]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_pull_requests,
            owner=owner,
            repo=repo,
            base_branch=base_branch,
            state=state,
            sort=sort,
            milestone=milestone,
            labels=labels,
            poster=poster,
            page=page,
            limit=limit,
        )

    @checked
    async def list_reviews(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PullReview]:
        """List one page of a pull request's reviews (repoListPullReviews)."""
        return await self._call(
            _repo_list_pull_reviews,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_reviews(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.PullReview]:
        """Iterate every item across all pages."""
        return self._paginate(
            _repo_list_pull_reviews,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    async def merge(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[MergePullRequestOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Merge a pull request (repoMergePullRequest)."""
        return await self._call(
            _repo_merge_pull_request,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def check_merged(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Check whether a pull request is merged (repoPullRequestIsMerged)."""
        return await self._call(
            _repo_pull_request_is_merged,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def resolve_review_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Mark a review comment's conversation resolved (repoResolvePullReviewComment)."""
        return await self._call(
            _repo_resolve_pull_review_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def submit_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
        body: Union[SubmitPullReviewOptions, Mapping[str, Any]],
    ) -> PullReview:
        """Submit a pending pull request review (repoSubmitPullReview)."""
        return await self._call(
            _repo_submit_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
            _body=body,
        )

    @checked
    async def undismiss_review(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> PullReview:
        """Restore a dismissed pull request review (repoUnDismissPullReview)."""
        return await self._call(
            _repo_un_dismiss_pull_review,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    async def unresolve_review_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Mark a review comment's conversation unresolved (repoUnresolvePullReviewComment)."""
        return await self._call(
            _repo_unresolve_pull_review_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def update_branch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        style: Optional[StrictStr] = None,
    ) -> None:
        """Merge or rebase a pull request's base branch into its head branch (repoUpdatePullRequest)."""
        return await self._call(
            _repo_update_pull_request,
            owner=owner,
            repo=repo,
            index=index,
            style=style,
        )
