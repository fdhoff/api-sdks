# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated

from gitea_rest import models as _models
from gitea_rest._runtime import (
    AsyncResource,
    FileInput,
    LinkHeader,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from gitea_rest.models.add_time_option import AddTimeOption
from gitea_rest.models.attachment import Attachment
from gitea_rest.models.comment import Comment
from gitea_rest.models.create_issue_comment_option import CreateIssueCommentOption
from gitea_rest.models.create_issue_option import CreateIssueOption
from gitea_rest.models.edit_attachment_options import EditAttachmentOptions
from gitea_rest.models.edit_deadline_option import EditDeadlineOption
from gitea_rest.models.edit_issue_comment_option import EditIssueCommentOption
from gitea_rest.models.edit_issue_option import EditIssueOption
from gitea_rest.models.edit_reaction_option import EditReactionOption
from gitea_rest.models.issue import Issue
from gitea_rest.models.issue_assignees_option import IssueAssigneesOption
from gitea_rest.models.issue_deadline import IssueDeadline
from gitea_rest.models.issue_labels_option import IssueLabelsOption
from gitea_rest.models.issue_meta import IssueMeta
from gitea_rest.models.label import Label
from gitea_rest.models.lock_issue_option import LockIssueOption
from gitea_rest.models.reaction import Reaction
from gitea_rest.models.timeline_comment import TimelineComment
from gitea_rest.models.tracked_time import TrackedTime
from gitea_rest.models.user import User
from gitea_rest.models.watch_info import WatchInfo

_issue_add_assignees: Operation[Issue] = Operation(
    id="issueAddAssignees",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/assignees",
    resource="issues",
    name="add_assignees",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_add_label: Operation[List[Label]] = Operation(
    id="issueAddLabel",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/labels",
    resource="issues",
    name="add_labels",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=List[Label],
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
_issue_add_subscription: Operation[None] = Operation(
    id="issueAddSubscription",
    method="PUT",
    path="/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}",
    resource="issues",
    name="subscribe",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("user", "user", "path"),
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
_issue_add_time: Operation[TrackedTime] = Operation(
    id="issueAddTime",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/times",
    resource="issues",
    name="add_tracked_time",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=TrackedTime,
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
_issue_check_assignee: Operation[None] = Operation(
    id="issueCheckAssignee",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/assignees/{assignee}",
    resource="issues",
    name="check_assignee",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("assignee", "assignee", "path"),
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
_issue_check_subscription: Operation[WatchInfo] = Operation(
    id="issueCheckSubscription",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/subscriptions/check",
    resource="issues",
    name="check_subscription",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=WatchInfo,
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
_issue_clear_labels: Operation[None] = Operation(
    id="issueClearLabels",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/labels",
    resource="issues",
    name="clear_labels",
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
_issue_create_comment: Operation[Comment] = Operation(
    id="issueCreateComment",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/comments",
    resource="issues",
    name="create_comment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Comment,
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
_issue_create_issue: Operation[Issue] = Operation(
    id="issueCreateIssue",
    method="POST",
    path="/repos/{owner}/{repo}/issues",
    resource="issues",
    name="create",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=Issue,
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
_issue_create_issue_attachment: Operation[Attachment] = Operation(
    id="issueCreateIssueAttachment",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/assets",
    resource="issues",
    name="upload_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_issue_create_issue_blocking: Operation[Issue] = Operation(
    id="issueCreateIssueBlocking",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/blocks",
    resource="issues",
    name="add_blocked",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_create_issue_comment_attachment: Operation[Attachment] = Operation(
    id="issueCreateIssueCommentAttachment",
    method="POST",
    path="/repos/{owner}/{repo}/issues/comments/{id}/assets",
    resource="issues",
    name="upload_comment_attachment",
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
_issue_create_issue_dependencies: Operation[Issue] = Operation(
    id="issueCreateIssueDependencies",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/dependencies",
    resource="issues",
    name="add_dependency",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_delete: Operation[None] = Operation(
    id="issueDelete",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}",
    resource="issues",
    name="delete",
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
_issue_delete_comment: Operation[None] = Operation(
    id="issueDeleteComment",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/comments/{id}",
    resource="issues",
    name="delete_comment",
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
_issue_delete_comment_reaction: Operation[None] = Operation(
    id="issueDeleteCommentReaction",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/comments/{id}/reactions",
    resource="issues",
    name="remove_comment_reaction",
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
_issue_delete_issue_attachment: Operation[None] = Operation(
    id="issueDeleteIssueAttachment",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}",
    resource="issues",
    name="delete_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_issue_delete_issue_comment_attachment: Operation[None] = Operation(
    id="issueDeleteIssueCommentAttachment",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}",
    resource="issues",
    name="delete_comment_attachment",
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
_issue_delete_issue_reaction: Operation[None] = Operation(
    id="issueDeleteIssueReaction",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/reactions",
    resource="issues",
    name="remove_reaction",
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
_issue_delete_stop_watch: Operation[None] = Operation(
    id="issueDeleteStopWatch",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/stopwatch/delete",
    resource="issues",
    name="delete_stopwatch",
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
_issue_delete_subscription: Operation[None] = Operation(
    id="issueDeleteSubscription",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}",
    resource="issues",
    name="unsubscribe",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("user", "user", "path"),
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
_issue_delete_time: Operation[None] = Operation(
    id="issueDeleteTime",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/times/{id}",
    resource="issues",
    name="delete_tracked_time",
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
_issue_edit_comment: Operation[Comment] = Operation(
    id="issueEditComment",
    method="PATCH",
    path="/repos/{owner}/{repo}/issues/comments/{id}",
    resource="issues",
    name="update_comment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Comment,
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
_issue_edit_issue: Operation[Issue] = Operation(
    id="issueEditIssue",
    method="PATCH",
    path="/repos/{owner}/{repo}/issues/{index}",
    resource="issues",
    name="update",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_edit_issue_attachment: Operation[Attachment] = Operation(
    id="issueEditIssueAttachment",
    method="PATCH",
    path="/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}",
    resource="issues",
    name="update_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_issue_edit_issue_comment_attachment: Operation[Attachment] = Operation(
    id="issueEditIssueCommentAttachment",
    method="PATCH",
    path="/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}",
    resource="issues",
    name="update_comment_attachment",
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
_issue_edit_issue_deadline: Operation[IssueDeadline] = Operation(
    id="issueEditIssueDeadline",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/deadline",
    resource="issues",
    name="set_deadline",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=IssueDeadline,
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
_issue_get_comment: Operation[Comment] = Operation(
    id="issueGetComment",
    method="GET",
    path="/repos/{owner}/{repo}/issues/comments/{id}",
    resource="issues",
    name="get_comment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Comment,
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
_issue_get_comment_reactions: Operation[List[Reaction]] = Operation(
    id="issueGetCommentReactions",
    method="GET",
    path="/repos/{owner}/{repo}/issues/comments/{id}/reactions",
    resource="issues",
    name="list_comment_reactions",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=List[Reaction],
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
_issue_get_comments: Operation[List[Comment]] = Operation(
    id="issueGetComments",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/comments",
    resource="issues",
    name="list_comments",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
    ),
    response=List[Comment],
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
_issue_get_comments_and_timeline: Operation[List[TimelineComment]] = Operation(
    id="issueGetCommentsAndTimeline",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/timeline",
    resource="issues",
    name="list_timeline",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("since", "since", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("before", "before", "query"),
    ),
    response=List[TimelineComment],
    returns_json=True,
    iterator="iter_timeline",
    item=_models.TimelineComment,
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
_issue_get_issue: Operation[Issue] = Operation(
    id="issueGetIssue",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}",
    resource="issues",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_get_issue_attachment: Operation[Attachment] = Operation(
    id="issueGetIssueAttachment",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}",
    resource="issues",
    name="get_attachment",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_issue_get_issue_comment_attachment: Operation[Attachment] = Operation(
    id="issueGetIssueCommentAttachment",
    method="GET",
    path="/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}",
    resource="issues",
    name="get_comment_attachment",
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
_issue_get_issue_reactions: Operation[List[Reaction]] = Operation(
    id="issueGetIssueReactions",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/reactions",
    resource="issues",
    name="list_reactions",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Reaction],
    returns_json=True,
    iterator="iter_reactions",
    item=_models.Reaction,
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
_issue_get_labels: Operation[List[Label]] = Operation(
    id="issueGetLabels",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/labels",
    resource="issues",
    name="list_labels",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=List[Label],
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
_issue_get_repo_comments: Operation[List[Comment]] = Operation(
    id="issueGetRepoComments",
    method="GET",
    path="/repos/{owner}/{repo}/issues/comments",
    resource="issues",
    name="list_repo_comments",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Comment],
    returns_json=True,
    iterator="iter_repo_comments",
    item=_models.Comment,
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
_issue_list_blocks: Operation[List[Issue]] = Operation(
    id="issueListBlocks",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/blocks",
    resource="issues",
    name="list_blocked",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Issue],
    returns_json=True,
    iterator="iter_blocked",
    item=_models.Issue,
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
_issue_list_issue_attachments: Operation[List[Attachment]] = Operation(
    id="issueListIssueAttachments",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/assets",
    resource="issues",
    name="list_attachments",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
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
_issue_list_issue_comment_attachments: Operation[List[Attachment]] = Operation(
    id="issueListIssueCommentAttachments",
    method="GET",
    path="/repos/{owner}/{repo}/issues/comments/{id}/assets",
    resource="issues",
    name="list_comment_attachments",
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
_issue_list_issue_dependencies: Operation[List[Issue]] = Operation(
    id="issueListIssueDependencies",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/dependencies",
    resource="issues",
    name="list_dependencies",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Issue],
    returns_json=True,
    iterator="iter_dependencies",
    item=_models.Issue,
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
_issue_list_issues: Operation[List[Issue]] = Operation(
    id="issueListIssues",
    method="GET",
    path="/repos/{owner}/{repo}/issues",
    resource="issues",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("state", "state", "query"),
        Param("labels", "labels", "query"),
        Param("q", "q", "query"),
        Param("type", "type", "query"),
        Param("milestones", "milestones", "query"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
        Param("created_by", "created_by", "query"),
        Param("assigned_by", "assigned_by", "query"),
        Param("mentioned_by", "mentioned_by", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Issue],
    returns_json=True,
    iterator="iter",
    item=_models.Issue,
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
_issue_lock_issue: Operation[None] = Operation(
    id="issueLockIssue",
    method="PUT",
    path="/repos/{owner}/{repo}/issues/{index}/lock",
    resource="issues",
    name="lock",
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
_issue_post_comment_reaction: Operation[Reaction] = Operation(
    id="issuePostCommentReaction",
    method="POST",
    path="/repos/{owner}/{repo}/issues/comments/{id}/reactions",
    resource="issues",
    name="add_comment_reaction",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("id", "id", "path"),
    ),
    response=Reaction,
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
_issue_post_issue_reaction: Operation[Reaction] = Operation(
    id="issuePostIssueReaction",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/reactions",
    resource="issues",
    name="add_reaction",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Reaction,
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
_issue_remove_assignees: Operation[Issue] = Operation(
    id="issueRemoveAssignees",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/assignees",
    resource="issues",
    name="remove_assignees",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_remove_issue_blocking: Operation[Issue] = Operation(
    id="issueRemoveIssueBlocking",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/blocks",
    resource="issues",
    name="remove_blocked",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_remove_issue_dependencies: Operation[Issue] = Operation(
    id="issueRemoveIssueDependencies",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/dependencies",
    resource="issues",
    name="remove_dependency",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=Issue,
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
_issue_remove_label: Operation[None] = Operation(
    id="issueRemoveLabel",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/labels/{id}",
    resource="issues",
    name="remove_label",
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
_issue_replace_labels: Operation[List[Label]] = Operation(
    id="issueReplaceLabels",
    method="PUT",
    path="/repos/{owner}/{repo}/issues/{index}/labels",
    resource="issues",
    name="replace_labels",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
    ),
    response=List[Label],
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
_issue_reset_time: Operation[None] = Operation(
    id="issueResetTime",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/times",
    resource="issues",
    name="reset_tracked_time",
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
_issue_search_issues: Operation[List[Issue]] = Operation(
    id="issueSearchIssues",
    method="GET",
    path="/repos/issues/search",
    resource="issues",
    name="search",
    params=(
        Param("state", "state", "query"),
        Param("labels", "labels", "query"),
        Param("milestones", "milestones", "query"),
        Param("q", "q", "query"),
        Param("type", "type", "query"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
        Param("assigned", "assigned", "query"),
        Param("created", "created", "query"),
        Param("mentioned", "mentioned", "query"),
        Param("review_requested", "review_requested", "query"),
        Param("reviewed", "reviewed", "query"),
        Param("owner", "owner", "query"),
        Param("created_by", "created_by", "query"),
        Param("team", "team", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Issue],
    returns_json=True,
    iterator="iter_search",
    item=_models.Issue,
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
_issue_start_stop_watch: Operation[None] = Operation(
    id="issueStartStopWatch",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/stopwatch/start",
    resource="issues",
    name="start_stopwatch",
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
_issue_stop_stop_watch: Operation[None] = Operation(
    id="issueStopStopWatch",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/stopwatch/stop",
    resource="issues",
    name="stop_stopwatch",
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
_issue_subscriptions: Operation[List[User]] = Operation(
    id="issueSubscriptions",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/subscriptions",
    resource="issues",
    name="list_subscribers",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_subscribers",
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
_issue_tracked_times: Operation[List[TrackedTime]] = Operation(
    id="issueTrackedTimes",
    method="GET",
    path="/repos/{owner}/{repo}/issues/{index}/times",
    resource="issues",
    name="list_tracked_times",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("user", "user", "query"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[TrackedTime],
    returns_json=True,
    iterator="iter_tracked_times",
    item=_models.TrackedTime,
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
_issue_unlock_issue: Operation[None] = Operation(
    id="issueUnlockIssue",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/lock",
    resource="issues",
    name="unlock",
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
_move_issue_pin: Operation[None] = Operation(
    id="moveIssuePin",
    method="PATCH",
    path="/repos/{owner}/{repo}/issues/{index}/pin/{position}",
    resource="issues",
    name="move_pin",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("index", "index", "path"),
        Param("position", "position", "path"),
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
_pin_issue: Operation[None] = Operation(
    id="pinIssue",
    method="POST",
    path="/repos/{owner}/{repo}/issues/{index}/pin",
    resource="issues",
    name="pin",
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
_repo_list_pinned_issues: Operation[List[Issue]] = Operation(
    id="repoListPinnedIssues",
    method="GET",
    path="/repos/{owner}/{repo}/issues/pinned",
    resource="issues",
    name="list_pinned",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
    ),
    response=List[Issue],
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
_unpin_issue: Operation[None] = Operation(
    id="unpinIssue",
    method="DELETE",
    path="/repos/{owner}/{repo}/issues/{index}/pin",
    resource="issues",
    name="unpin",
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

OPERATIONS = (
    _issue_add_assignees,
    _issue_add_label,
    _issue_add_subscription,
    _issue_add_time,
    _issue_check_assignee,
    _issue_check_subscription,
    _issue_clear_labels,
    _issue_create_comment,
    _issue_create_issue,
    _issue_create_issue_attachment,
    _issue_create_issue_blocking,
    _issue_create_issue_comment_attachment,
    _issue_create_issue_dependencies,
    _issue_delete,
    _issue_delete_comment,
    _issue_delete_comment_reaction,
    _issue_delete_issue_attachment,
    _issue_delete_issue_comment_attachment,
    _issue_delete_issue_reaction,
    _issue_delete_stop_watch,
    _issue_delete_subscription,
    _issue_delete_time,
    _issue_edit_comment,
    _issue_edit_issue,
    _issue_edit_issue_attachment,
    _issue_edit_issue_comment_attachment,
    _issue_edit_issue_deadline,
    _issue_get_comment,
    _issue_get_comment_reactions,
    _issue_get_comments,
    _issue_get_comments_and_timeline,
    _issue_get_issue,
    _issue_get_issue_attachment,
    _issue_get_issue_comment_attachment,
    _issue_get_issue_reactions,
    _issue_get_labels,
    _issue_get_repo_comments,
    _issue_list_blocks,
    _issue_list_issue_attachments,
    _issue_list_issue_comment_attachments,
    _issue_list_issue_dependencies,
    _issue_list_issues,
    _issue_lock_issue,
    _issue_post_comment_reaction,
    _issue_post_issue_reaction,
    _issue_remove_assignees,
    _issue_remove_issue_blocking,
    _issue_remove_issue_dependencies,
    _issue_remove_label,
    _issue_replace_labels,
    _issue_reset_time,
    _issue_search_issues,
    _issue_start_stop_watch,
    _issue_stop_stop_watch,
    _issue_subscriptions,
    _issue_tracked_times,
    _issue_unlock_issue,
    _move_issue_pin,
    _pin_issue,
    _repo_list_pinned_issues,
    _unpin_issue,
)


class IssuesApi(Resource):
    @checked
    def add_assignees(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[IssueAssigneesOption, Mapping[str, Any]],
    ) -> Issue:
        """Assign users to an issue (issueAddAssignees)."""
        return self._call(
            _issue_add_assignees,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def add_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[IssueLabelsOption, Mapping[str, Any]]] = None,
    ) -> List[Label]:
        """Add labels to an issue (issueAddLabel)."""
        return self._call(
            _issue_add_label,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def subscribe(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        user: StrictStr,
    ) -> None:
        """Subscribe a user to an issue (issueAddSubscription)."""
        return self._call(
            _issue_add_subscription,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
        )

    @checked
    def add_tracked_time(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[AddTimeOption, Mapping[str, Any]]] = None,
    ) -> TrackedTime:
        """Track time spent on an issue (issueAddTime)."""
        return self._call(
            _issue_add_time,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def check_assignee(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        assignee: StrictStr,
    ) -> None:
        """Check whether a user is assigned to an issue (issueCheckAssignee)."""
        return self._call(
            _issue_check_assignee,
            owner=owner,
            repo=repo,
            index=index,
            assignee=assignee,
        )

    @checked
    def check_subscription(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> WatchInfo:
        """Check whether you are subscribed to an issue (issueCheckSubscription)."""
        return self._call(
            _issue_check_subscription,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def clear_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Remove every label from an issue (issueClearLabels)."""
        return self._call(
            _issue_clear_labels,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def create_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[CreateIssueCommentOption, Mapping[str, Any]]] = None,
    ) -> Comment:
        """Comment on an issue (issueCreateComment)."""
        return self._call(
            _issue_create_comment,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateIssueOption, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Open an issue (issueCreateIssue)."""
        return self._call(
            _issue_create_issue,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    def upload_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        attachment: FileInput,
        name: Optional[StrictStr] = None,
    ) -> Attachment:
        """Upload an attachment to an issue (issueCreateIssueAttachment)."""
        return self._call(
            _issue_create_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            name=name,
            attachment=attachment,
        )

    @checked
    def add_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Make an issue block another (issueCreateIssueBlocking)."""
        return self._call(
            _issue_create_issue_blocking,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def upload_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        attachment: FileInput,
        name: Optional[StrictStr] = None,
    ) -> Attachment:
        """Upload an attachment to an issue comment (issueCreateIssueCommentAttachment)."""
        return self._call(
            _issue_create_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            name=name,
            attachment=attachment,
        )

    @checked
    def add_dependency(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Make an issue depend on another (issueCreateIssueDependencies)."""
        return self._call(
            _issue_create_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Delete an issue (issueDelete)."""
        return self._call(
            _issue_delete,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def delete_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an issue comment (issueDeleteComment)."""
        return self._call(
            _issue_delete_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def remove_comment_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove a reaction from an issue comment (issueDeleteCommentReaction)."""
        return self._call(
            _issue_delete_comment_reaction,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def delete_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        attachment_id: StrictInt,
    ) -> None:
        """Delete an issue attachment (issueDeleteIssueAttachment)."""
        return self._call(
            _issue_delete_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            attachment_id=attachment_id,
        )

    @checked
    def delete_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> None:
        """Delete an issue comment attachment (issueDeleteIssueCommentAttachment)."""
        return self._call(
            _issue_delete_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    def remove_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove a reaction from an issue (issueDeleteIssueReaction)."""
        return self._call(
            _issue_delete_issue_reaction,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def delete_stopwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Cancel an issue's stopwatch without tracking its time (issueDeleteStopWatch)."""
        return self._call(
            _issue_delete_stop_watch,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def unsubscribe(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        user: StrictStr,
    ) -> None:
        """Unsubscribe a user from an issue (issueDeleteSubscription)."""
        return self._call(
            _issue_delete_subscription,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
        )

    @checked
    def delete_tracked_time(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> None:
        """Delete one tracked time entry from an issue (issueDeleteTime)."""
        return self._call(
            _issue_delete_time,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    def update_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditIssueCommentOption, Mapping[str, Any]]] = None,
    ) -> Comment:
        """Change an issue comment (issueEditComment)."""
        return self._call(
            _issue_edit_comment,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditIssueOption, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Change an issue or pull request (issueEditIssue)."""
        return self._call(
            _issue_edit_issue,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def update_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        attachment_id: StrictInt,
        body: Optional[Union[EditAttachmentOptions, Mapping[str, Any]]] = None,
    ) -> Attachment:
        """Rename an issue attachment (issueEditIssueAttachment)."""
        return self._call(
            _issue_edit_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            attachment_id=attachment_id,
            _body=body,
        )

    @checked
    def update_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
        body: Optional[Union[EditAttachmentOptions, Mapping[str, Any]]] = None,
    ) -> Attachment:
        """Rename an issue comment attachment (issueEditIssueCommentAttachment)."""
        return self._call(
            _issue_edit_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
            _body=body,
        )

    @checked
    def set_deadline(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditDeadlineOption, Mapping[str, Any]]] = None,
    ) -> IssueDeadline:
        """Set or clear an issue's due date (issueEditIssueDeadline)."""
        return self._call(
            _issue_edit_issue_deadline,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def get_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Comment:
        """Get an issue comment (issueGetComment)."""
        return self._call(
            _issue_get_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def list_comment_reactions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> List[Reaction]:
        """List an issue comment's reactions (issueGetCommentReactions)."""
        return self._call(
            _issue_get_comment_reactions,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def list_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
    ) -> List[Comment]:
        """List an issue's comments (issueGetComments)."""
        return self._call(
            _issue_get_comments,
            owner=owner,
            repo=repo,
            index=index,
            since=since,
            before=before,
        )

    @checked
    def list_timeline(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        since: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        before: Optional[datetime] = None,
    ) -> List[TimelineComment]:
        """List one page of an issue's comments and events (issueGetCommentsAndTimeline)."""
        return self._call(
            _issue_get_comments_and_timeline,
            owner=owner,
            repo=repo,
            index=index,
            since=since,
            page=page,
            limit=limit,
            before=before,
        )

    @checked
    def iter_timeline(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        since: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        before: Optional[datetime] = None,
    ) -> Iterator[_models.TimelineComment]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_comments_and_timeline,
            owner=owner,
            repo=repo,
            index=index,
            since=since,
            page=page,
            limit=limit,
            before=before,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> Issue:
        """Get an issue or pull request (issueGetIssue)."""
        return self._call(
            _issue_get_issue,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def get_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        attachment_id: StrictInt,
    ) -> Attachment:
        """Get an issue attachment (issueGetIssueAttachment)."""
        return self._call(
            _issue_get_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            attachment_id=attachment_id,
        )

    @checked
    def get_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> Attachment:
        """Get an issue comment attachment (issueGetIssueCommentAttachment)."""
        return self._call(
            _issue_get_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    def list_reactions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Reaction]:
        """List one page of an issue's reactions (issueGetIssueReactions)."""
        return self._call(
            _issue_get_issue_reactions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_reactions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Reaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_issue_reactions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def list_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> List[Label]:
        """List an issue's labels (issueGetLabels)."""
        return self._call(
            _issue_get_labels,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def list_repo_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Comment]:
        """List one page of the comments on a repository's issues (issueGetRepoComments)."""
        return self._call(
            _issue_get_repo_comments,
            owner=owner,
            repo=repo,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repo_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Comment]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_repo_comments,
            owner=owner,
            repo=repo,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def list_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues that an issue blocks (issueListBlocks)."""
        return self._call(
            _issue_list_blocks,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_blocks,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def list_attachments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> List[Attachment]:
        """List an issue's attachments (issueListIssueAttachments)."""
        return self._call(
            _issue_list_issue_attachments,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def list_comment_attachments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> List[Attachment]:
        """List an issue comment's attachments (issueListIssueCommentAttachments)."""
        return self._call(
            _issue_list_issue_comment_attachments,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    def list_dependencies(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues that block an issue (issueListIssueDependencies)."""
        return self._call(
            _issue_list_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_dependencies(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        labels: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        created_by: Optional[StrictStr] = None,
        assigned_by: Optional[StrictStr] = None,
        mentioned_by: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of a repository's issues and pull requests (issueListIssues)."""
        return self._call(
            _issue_list_issues,
            owner=owner,
            repo=repo,
            state=state,
            labels=labels,
            q=q,
            type=type,
            milestones=milestones,
            since=since,
            before=before,
            created_by=created_by,
            assigned_by=assigned_by,
            mentioned_by=mentioned_by,
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
        labels: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        created_by: Optional[StrictStr] = None,
        assigned_by: Optional[StrictStr] = None,
        mentioned_by: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_issues,
            owner=owner,
            repo=repo,
            state=state,
            labels=labels,
            q=q,
            type=type,
            milestones=milestones,
            since=since,
            before=before,
            created_by=created_by,
            assigned_by=assigned_by,
            mentioned_by=mentioned_by,
            page=page,
            limit=limit,
        )

    @checked
    def lock(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[LockIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Lock an issue's conversation (issueLockIssue)."""
        return self._call(
            _issue_lock_issue,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def add_comment_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> Reaction:
        """React to an issue comment (issuePostCommentReaction)."""
        return self._call(
            _issue_post_comment_reaction,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    def add_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> Reaction:
        """React to an issue (issuePostIssueReaction)."""
        return self._call(
            _issue_post_issue_reaction,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def remove_assignees(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[IssueAssigneesOption, Mapping[str, Any]],
    ) -> Issue:
        """Unassign users from an issue (issueRemoveAssignees)."""
        return self._call(
            _issue_remove_assignees,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def remove_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Stop an issue blocking another (issueRemoveIssueBlocking)."""
        return self._call(
            _issue_remove_issue_blocking,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def remove_dependency(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Stop an issue depending on another (issueRemoveIssueDependencies)."""
        return self._call(
            _issue_remove_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def remove_label(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> None:
        """Remove a label from an issue (issueRemoveLabel)."""
        return self._call(
            _issue_remove_label,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    def replace_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[IssueLabelsOption, Mapping[str, Any]]] = None,
    ) -> List[Label]:
        """Replace an issue's labels (issueReplaceLabels)."""
        return self._call(
            _issue_replace_labels,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    def reset_tracked_time(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Delete all of your tracked time on an issue (issueResetTime)."""
        return self._call(
            _issue_reset_time,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def search(
        self,
        *,
        state: Optional[StrictStr] = None,
        labels: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        assigned: Optional[StrictBool] = None,
        created: Optional[StrictBool] = None,
        mentioned: Optional[StrictBool] = None,
        review_requested: Optional[StrictBool] = None,
        reviewed: Optional[StrictBool] = None,
        owner: Optional[StrictStr] = None,
        created_by: Optional[StrictStr] = None,
        team: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> List[Issue]:
        """Get one page of the issues and pull requests that match a search, across repositories (issueSearchIssues)."""
        return self._call(
            _issue_search_issues,
            state=state,
            labels=labels,
            milestones=milestones,
            q=q,
            type=type,
            since=since,
            before=before,
            assigned=assigned,
            created=created,
            mentioned=mentioned,
            review_requested=review_requested,
            reviewed=reviewed,
            owner=owner,
            created_by=created_by,
            team=team,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        *,
        state: Optional[StrictStr] = None,
        labels: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        assigned: Optional[StrictBool] = None,
        created: Optional[StrictBool] = None,
        mentioned: Optional[StrictBool] = None,
        review_requested: Optional[StrictBool] = None,
        reviewed: Optional[StrictBool] = None,
        owner: Optional[StrictStr] = None,
        created_by: Optional[StrictStr] = None,
        team: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_search_issues,
            state=state,
            labels=labels,
            milestones=milestones,
            q=q,
            type=type,
            since=since,
            before=before,
            assigned=assigned,
            created=created,
            mentioned=mentioned,
            review_requested=review_requested,
            reviewed=reviewed,
            owner=owner,
            created_by=created_by,
            team=team,
            page=page,
            limit=limit,
        )

    @checked
    def start_stopwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Start a stopwatch on an issue (issueStartStopWatch)."""
        return self._call(
            _issue_start_stop_watch,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def stop_stopwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Stop an issue's stopwatch and track its time (issueStopStopWatch)."""
        return self._call(
            _issue_stop_stop_watch,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def list_subscribers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of an issue's subscribers (issueSubscriptions)."""
        return self._call(
            _issue_subscriptions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_subscribers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_subscriptions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def list_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[TrackedTime]:
        """List one page of the time tracked on an issue (issueTrackedTimes)."""
        return self._call(
            _issue_tracked_times,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.TrackedTime]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_tracked_times,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def unlock(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Unlock an issue's conversation (issueUnlockIssue)."""
        return self._call(
            _issue_unlock_issue,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def move_pin(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        position: StrictInt,
    ) -> None:
        """Move a pinned issue to another position (moveIssuePin)."""
        return self._call(
            _move_issue_pin,
            owner=owner,
            repo=repo,
            index=index,
            position=position,
        )

    @checked
    def pin(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Pin an issue (pinIssue)."""
        return self._call(
            _pin_issue,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    def list_pinned(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[Issue]:
        """List a repository's pinned issues (repoListPinnedIssues)."""
        return self._call(
            _repo_list_pinned_issues,
            owner=owner,
            repo=repo,
        )

    @checked
    def unpin(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Unpin an issue (unpinIssue)."""
        return self._call(
            _unpin_issue,
            owner=owner,
            repo=repo,
            index=index,
        )


class AsyncIssuesApi(AsyncResource):
    @checked
    async def add_assignees(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[IssueAssigneesOption, Mapping[str, Any]],
    ) -> Issue:
        """Assign users to an issue (issueAddAssignees)."""
        return await self._call(
            _issue_add_assignees,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def add_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[IssueLabelsOption, Mapping[str, Any]]] = None,
    ) -> List[Label]:
        """Add labels to an issue (issueAddLabel)."""
        return await self._call(
            _issue_add_label,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def subscribe(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        user: StrictStr,
    ) -> None:
        """Subscribe a user to an issue (issueAddSubscription)."""
        return await self._call(
            _issue_add_subscription,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
        )

    @checked
    async def add_tracked_time(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[AddTimeOption, Mapping[str, Any]]] = None,
    ) -> TrackedTime:
        """Track time spent on an issue (issueAddTime)."""
        return await self._call(
            _issue_add_time,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def check_assignee(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        assignee: StrictStr,
    ) -> None:
        """Check whether a user is assigned to an issue (issueCheckAssignee)."""
        return await self._call(
            _issue_check_assignee,
            owner=owner,
            repo=repo,
            index=index,
            assignee=assignee,
        )

    @checked
    async def check_subscription(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> WatchInfo:
        """Check whether you are subscribed to an issue (issueCheckSubscription)."""
        return await self._call(
            _issue_check_subscription,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def clear_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Remove every label from an issue (issueClearLabels)."""
        return await self._call(
            _issue_clear_labels,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def create_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[CreateIssueCommentOption, Mapping[str, Any]]] = None,
    ) -> Comment:
        """Comment on an issue (issueCreateComment)."""
        return await self._call(
            _issue_create_comment,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def create(
        self,
        owner: StrictStr,
        repo: StrictStr,
        body: Optional[Union[CreateIssueOption, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Open an issue (issueCreateIssue)."""
        return await self._call(
            _issue_create_issue,
            owner=owner,
            repo=repo,
            _body=body,
        )

    @checked
    async def upload_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        attachment: FileInput,
        name: Optional[StrictStr] = None,
    ) -> Attachment:
        """Upload an attachment to an issue (issueCreateIssueAttachment)."""
        return await self._call(
            _issue_create_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            name=name,
            attachment=attachment,
        )

    @checked
    async def add_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Make an issue block another (issueCreateIssueBlocking)."""
        return await self._call(
            _issue_create_issue_blocking,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def upload_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        *,
        attachment: FileInput,
        name: Optional[StrictStr] = None,
    ) -> Attachment:
        """Upload an attachment to an issue comment (issueCreateIssueCommentAttachment)."""
        return await self._call(
            _issue_create_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            name=name,
            attachment=attachment,
        )

    @checked
    async def add_dependency(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Make an issue depend on another (issueCreateIssueDependencies)."""
        return await self._call(
            _issue_create_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def delete(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Delete an issue (issueDelete)."""
        return await self._call(
            _issue_delete,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def delete_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> None:
        """Delete an issue comment (issueDeleteComment)."""
        return await self._call(
            _issue_delete_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def remove_comment_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove a reaction from an issue comment (issueDeleteCommentReaction)."""
        return await self._call(
            _issue_delete_comment_reaction,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def delete_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        attachment_id: StrictInt,
    ) -> None:
        """Delete an issue attachment (issueDeleteIssueAttachment)."""
        return await self._call(
            _issue_delete_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            attachment_id=attachment_id,
        )

    @checked
    async def delete_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> None:
        """Delete an issue comment attachment (issueDeleteIssueCommentAttachment)."""
        return await self._call(
            _issue_delete_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    async def remove_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove a reaction from an issue (issueDeleteIssueReaction)."""
        return await self._call(
            _issue_delete_issue_reaction,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def delete_stopwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Cancel an issue's stopwatch without tracking its time (issueDeleteStopWatch)."""
        return await self._call(
            _issue_delete_stop_watch,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def unsubscribe(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        user: StrictStr,
    ) -> None:
        """Unsubscribe a user from an issue (issueDeleteSubscription)."""
        return await self._call(
            _issue_delete_subscription,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
        )

    @checked
    async def delete_tracked_time(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> None:
        """Delete one tracked time entry from an issue (issueDeleteTime)."""
        return await self._call(
            _issue_delete_time,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    async def update_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditIssueCommentOption, Mapping[str, Any]]] = None,
    ) -> Comment:
        """Change an issue comment (issueEditComment)."""
        return await self._call(
            _issue_edit_comment,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def update(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditIssueOption, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Change an issue or pull request (issueEditIssue)."""
        return await self._call(
            _issue_edit_issue,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def update_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        attachment_id: StrictInt,
        body: Optional[Union[EditAttachmentOptions, Mapping[str, Any]]] = None,
    ) -> Attachment:
        """Rename an issue attachment (issueEditIssueAttachment)."""
        return await self._call(
            _issue_edit_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            attachment_id=attachment_id,
            _body=body,
        )

    @checked
    async def update_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
        body: Optional[Union[EditAttachmentOptions, Mapping[str, Any]]] = None,
    ) -> Attachment:
        """Rename an issue comment attachment (issueEditIssueCommentAttachment)."""
        return await self._call(
            _issue_edit_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
            _body=body,
        )

    @checked
    async def set_deadline(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditDeadlineOption, Mapping[str, Any]]] = None,
    ) -> IssueDeadline:
        """Set or clear an issue's due date (issueEditIssueDeadline)."""
        return await self._call(
            _issue_edit_issue_deadline,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def get_comment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> Comment:
        """Get an issue comment (issueGetComment)."""
        return await self._call(
            _issue_get_comment,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def list_comment_reactions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> List[Reaction]:
        """List an issue comment's reactions (issueGetCommentReactions)."""
        return await self._call(
            _issue_get_comment_reactions,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def list_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
    ) -> List[Comment]:
        """List an issue's comments (issueGetComments)."""
        return await self._call(
            _issue_get_comments,
            owner=owner,
            repo=repo,
            index=index,
            since=since,
            before=before,
        )

    @checked
    async def list_timeline(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        since: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        before: Optional[datetime] = None,
    ) -> List[TimelineComment]:
        """List one page of an issue's comments and events (issueGetCommentsAndTimeline)."""
        return await self._call(
            _issue_get_comments_and_timeline,
            owner=owner,
            repo=repo,
            index=index,
            since=since,
            page=page,
            limit=limit,
            before=before,
        )

    @checked
    def iter_timeline(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        since: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        before: Optional[datetime] = None,
    ) -> AsyncIterator[_models.TimelineComment]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_comments_and_timeline,
            owner=owner,
            repo=repo,
            index=index,
            since=since,
            page=page,
            limit=limit,
            before=before,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> Issue:
        """Get an issue or pull request (issueGetIssue)."""
        return await self._call(
            _issue_get_issue,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def get_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        attachment_id: StrictInt,
    ) -> Attachment:
        """Get an issue attachment (issueGetIssueAttachment)."""
        return await self._call(
            _issue_get_issue_attachment,
            owner=owner,
            repo=repo,
            index=index,
            attachment_id=attachment_id,
        )

    @checked
    async def get_comment_attachment(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        attachment_id: StrictInt,
    ) -> Attachment:
        """Get an issue comment attachment (issueGetIssueCommentAttachment)."""
        return await self._call(
            _issue_get_issue_comment_attachment,
            owner=owner,
            repo=repo,
            id=id,
            attachment_id=attachment_id,
        )

    @checked
    async def list_reactions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Reaction]:
        """List one page of an issue's reactions (issueGetIssueReactions)."""
        return await self._call(
            _issue_get_issue_reactions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_reactions(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Reaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_issue_reactions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    async def list_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> List[Label]:
        """List an issue's labels (issueGetLabels)."""
        return await self._call(
            _issue_get_labels,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def list_repo_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Comment]:
        """List one page of the comments on a repository's issues (issueGetRepoComments)."""
        return await self._call(
            _issue_get_repo_comments,
            owner=owner,
            repo=repo,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repo_comments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Comment]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_get_repo_comments,
            owner=owner,
            repo=repo,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    async def list_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues that an issue blocks (issueListBlocks)."""
        return await self._call(
            _issue_list_blocks,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_blocks,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    async def list_attachments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> List[Attachment]:
        """List an issue's attachments (issueListIssueAttachments)."""
        return await self._call(
            _issue_list_issue_attachments,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def list_comment_attachments(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
    ) -> List[Attachment]:
        """List an issue comment's attachments (issueListIssueCommentAttachments)."""
        return await self._call(
            _issue_list_issue_comment_attachments,
            owner=owner,
            repo=repo,
            id=id,
        )

    @checked
    async def list_dependencies(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of the issues that block an issue (issueListIssueDependencies)."""
        return await self._call(
            _issue_list_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_dependencies(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    async def list(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        state: Optional[StrictStr] = None,
        labels: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        created_by: Optional[StrictStr] = None,
        assigned_by: Optional[StrictStr] = None,
        mentioned_by: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Issue]:
        """List one page of a repository's issues and pull requests (issueListIssues)."""
        return await self._call(
            _issue_list_issues,
            owner=owner,
            repo=repo,
            state=state,
            labels=labels,
            q=q,
            type=type,
            milestones=milestones,
            since=since,
            before=before,
            created_by=created_by,
            assigned_by=assigned_by,
            mentioned_by=mentioned_by,
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
        labels: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        created_by: Optional[StrictStr] = None,
        assigned_by: Optional[StrictStr] = None,
        mentioned_by: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_list_issues,
            owner=owner,
            repo=repo,
            state=state,
            labels=labels,
            q=q,
            type=type,
            milestones=milestones,
            since=since,
            before=before,
            created_by=created_by,
            assigned_by=assigned_by,
            mentioned_by=mentioned_by,
            page=page,
            limit=limit,
        )

    @checked
    async def lock(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[LockIssueOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Lock an issue's conversation (issueLockIssue)."""
        return await self._call(
            _issue_lock_issue,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def add_comment_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        id: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> Reaction:
        """React to an issue comment (issuePostCommentReaction)."""
        return await self._call(
            _issue_post_comment_reaction,
            owner=owner,
            repo=repo,
            id=id,
            _body=body,
        )

    @checked
    async def add_reaction(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[EditReactionOption, Mapping[str, Any]]] = None,
    ) -> Reaction:
        """React to an issue (issuePostIssueReaction)."""
        return await self._call(
            _issue_post_issue_reaction,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def remove_assignees(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Union[IssueAssigneesOption, Mapping[str, Any]],
    ) -> Issue:
        """Unassign users from an issue (issueRemoveAssignees)."""
        return await self._call(
            _issue_remove_assignees,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def remove_blocked(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Stop an issue blocking another (issueRemoveIssueBlocking)."""
        return await self._call(
            _issue_remove_issue_blocking,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def remove_dependency(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictStr,
        body: Optional[Union[IssueMeta, Mapping[str, Any]]] = None,
    ) -> Issue:
        """Stop an issue depending on another (issueRemoveIssueDependencies)."""
        return await self._call(
            _issue_remove_issue_dependencies,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def remove_label(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        id: StrictInt,
    ) -> None:
        """Remove a label from an issue (issueRemoveLabel)."""
        return await self._call(
            _issue_remove_label,
            owner=owner,
            repo=repo,
            index=index,
            id=id,
        )

    @checked
    async def replace_labels(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        body: Optional[Union[IssueLabelsOption, Mapping[str, Any]]] = None,
    ) -> List[Label]:
        """Replace an issue's labels (issueReplaceLabels)."""
        return await self._call(
            _issue_replace_labels,
            owner=owner,
            repo=repo,
            index=index,
            _body=body,
        )

    @checked
    async def reset_tracked_time(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Delete all of your tracked time on an issue (issueResetTime)."""
        return await self._call(
            _issue_reset_time,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def search(
        self,
        *,
        state: Optional[StrictStr] = None,
        labels: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        assigned: Optional[StrictBool] = None,
        created: Optional[StrictBool] = None,
        mentioned: Optional[StrictBool] = None,
        review_requested: Optional[StrictBool] = None,
        reviewed: Optional[StrictBool] = None,
        owner: Optional[StrictStr] = None,
        created_by: Optional[StrictStr] = None,
        team: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> List[Issue]:
        """Get one page of the issues and pull requests that match a search, across repositories (issueSearchIssues)."""
        return await self._call(
            _issue_search_issues,
            state=state,
            labels=labels,
            milestones=milestones,
            q=q,
            type=type,
            since=since,
            before=before,
            assigned=assigned,
            created=created,
            mentioned=mentioned,
            review_requested=review_requested,
            reviewed=reviewed,
            owner=owner,
            created_by=created_by,
            team=team,
            page=page,
            limit=limit,
        )

    @checked
    def iter_search(
        self,
        *,
        state: Optional[StrictStr] = None,
        labels: Optional[StrictStr] = None,
        milestones: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        assigned: Optional[StrictBool] = None,
        created: Optional[StrictBool] = None,
        mentioned: Optional[StrictBool] = None,
        review_requested: Optional[StrictBool] = None,
        reviewed: Optional[StrictBool] = None,
        owner: Optional[StrictStr] = None,
        created_by: Optional[StrictStr] = None,
        team: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.Issue]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_search_issues,
            state=state,
            labels=labels,
            milestones=milestones,
            q=q,
            type=type,
            since=since,
            before=before,
            assigned=assigned,
            created=created,
            mentioned=mentioned,
            review_requested=review_requested,
            reviewed=reviewed,
            owner=owner,
            created_by=created_by,
            team=team,
            page=page,
            limit=limit,
        )

    @checked
    async def start_stopwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Start a stopwatch on an issue (issueStartStopWatch)."""
        return await self._call(
            _issue_start_stop_watch,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def stop_stopwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Stop an issue's stopwatch and track its time (issueStopStopWatch)."""
        return await self._call(
            _issue_stop_stop_watch,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def list_subscribers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of an issue's subscribers (issueSubscriptions)."""
        return await self._call(
            _issue_subscriptions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    def iter_subscribers(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_subscriptions,
            owner=owner,
            repo=repo,
            index=index,
            page=page,
            limit=limit,
        )

    @checked
    async def list_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[TrackedTime]:
        """List one page of the time tracked on an issue (issueTrackedTimes)."""
        return await self._call(
            _issue_tracked_times,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_tracked_times(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        *,
        user: Optional[StrictStr] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.TrackedTime]:
        """Iterate every item across all pages."""
        return self._paginate(
            _issue_tracked_times,
            owner=owner,
            repo=repo,
            index=index,
            user=user,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    async def unlock(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Unlock an issue's conversation (issueUnlockIssue)."""
        return await self._call(
            _issue_unlock_issue,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def move_pin(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
        position: StrictInt,
    ) -> None:
        """Move a pinned issue to another position (moveIssuePin)."""
        return await self._call(
            _move_issue_pin,
            owner=owner,
            repo=repo,
            index=index,
            position=position,
        )

    @checked
    async def pin(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Pin an issue (pinIssue)."""
        return await self._call(
            _pin_issue,
            owner=owner,
            repo=repo,
            index=index,
        )

    @checked
    async def list_pinned(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> List[Issue]:
        """List a repository's pinned issues (repoListPinnedIssues)."""
        return await self._call(
            _repo_list_pinned_issues,
            owner=owner,
            repo=repo,
        )

    @checked
    async def unpin(
        self,
        owner: StrictStr,
        repo: StrictStr,
        index: StrictInt,
    ) -> None:
        """Unpin an issue (unpinIssue)."""
        return await self._call(
            _unpin_issue,
            owner=owner,
            repo=repo,
            index=index,
        )
