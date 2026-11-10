# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import AsyncIterator, Iterator, List, Optional

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
from gitea_rest.models.notification_count import NotificationCount
from gitea_rest.models.notification_thread import NotificationThread

_notify_get_list: Operation[List[NotificationThread]] = Operation(
    id="notifyGetList",
    method="GET",
    path="/notifications",
    resource="notifications",
    name="list",
    params=(
        Param("all", "all", "query"),
        Param("status-types", "status_types", "query"),
        Param("subject-type", "subject_type", "query"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[NotificationThread],
    returns_json=True,
    iterator="iter",
    item=_models.NotificationThread,
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
_notify_get_repo_list: Operation[List[NotificationThread]] = Operation(
    id="notifyGetRepoList",
    method="GET",
    path="/repos/{owner}/{repo}/notifications",
    resource="notifications",
    name="list_for_repo",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("all", "all", "query"),
        Param("status-types", "status_types", "query"),
        Param("subject-type", "subject_type", "query"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[NotificationThread],
    returns_json=True,
    iterator="iter_for_repo",
    item=_models.NotificationThread,
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
_notify_get_thread: Operation[NotificationThread] = Operation(
    id="notifyGetThread",
    method="GET",
    path="/notifications/threads/{id}",
    resource="notifications",
    name="get_thread",
    params=(Param("id", "id", "path"),),
    response=NotificationThread,
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
_notify_new_available: Operation[NotificationCount] = Operation(
    id="notifyNewAvailable",
    method="GET",
    path="/notifications/new",
    resource="notifications",
    name="count_unread",
    params=(),
    response=NotificationCount,
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
_notify_read_list: Operation[List[NotificationThread]] = Operation(
    id="notifyReadList",
    method="PUT",
    path="/notifications",
    resource="notifications",
    name="mark_read",
    params=(
        Param("last_read_at", "last_read_at", "query"),
        Param("all", "all", "query"),
        Param("status-types", "status_types", "query"),
        Param("to-status", "to_status", "query"),
    ),
    response=List[NotificationThread],
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
_notify_read_repo_list: Operation[List[NotificationThread]] = Operation(
    id="notifyReadRepoList",
    method="PUT",
    path="/repos/{owner}/{repo}/notifications",
    resource="notifications",
    name="mark_repo_read",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
        Param("all", "all", "query"),
        Param("status-types", "status_types", "query"),
        Param("to-status", "to_status", "query"),
        Param("last_read_at", "last_read_at", "query"),
    ),
    response=List[NotificationThread],
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
_notify_read_thread: Operation[NotificationThread] = Operation(
    id="notifyReadThread",
    method="PATCH",
    path="/notifications/threads/{id}",
    resource="notifications",
    name="mark_thread_read",
    params=(
        Param("id", "id", "path"),
        Param("to-status", "to_status", "query"),
    ),
    response=NotificationThread,
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
    _notify_get_list,
    _notify_get_repo_list,
    _notify_get_thread,
    _notify_new_available,
    _notify_read_list,
    _notify_read_repo_list,
    _notify_read_thread,
)


class NotificationsApi(Resource):
    @checked
    def list(
        self,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[NotificationThread]:
        """List one page of your notification threads (notifyGetList)."""
        return self._call(
            _notify_get_list,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.NotificationThread]:
        """Iterate every item across all pages."""
        return self._paginate(
            _notify_get_list,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def list_for_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[NotificationThread]:
        """List one page of your notification threads on a repository (notifyGetRepoList)."""
        return self._call(
            _notify_get_repo_list,
            owner=owner,
            repo=repo,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.NotificationThread]:
        """Iterate every item across all pages."""
        return self._paginate(
            _notify_get_repo_list,
            owner=owner,
            repo=repo,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def get_thread(
        self,
        id: StrictStr,
    ) -> NotificationThread:
        """Get a notification thread (notifyGetThread)."""
        return self._call(
            _notify_get_thread,
            id=id,
        )

    @checked
    def count_unread(
        self,
    ) -> NotificationCount:
        """Count your unread notification threads (notifyNewAvailable)."""
        return self._call(
            _notify_new_available,
        )

    @checked
    def mark_read(
        self,
        *,
        last_read_at: Optional[datetime] = None,
        all: Optional[StrictStr] = None,
        status_types: Optional[List[StrictStr]] = None,
        to_status: Optional[StrictStr] = None,
    ) -> List[NotificationThread]:
        """Mark your notification threads read (notifyReadList)."""
        return self._call(
            _notify_read_list,
            last_read_at=last_read_at,
            all=all,
            status_types=status_types,
            to_status=to_status,
        )

    @checked
    def mark_repo_read(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        all: Optional[StrictStr] = None,
        status_types: Optional[List[StrictStr]] = None,
        to_status: Optional[StrictStr] = None,
        last_read_at: Optional[datetime] = None,
    ) -> List[NotificationThread]:
        """Mark your notification threads on a repository read (notifyReadRepoList)."""
        return self._call(
            _notify_read_repo_list,
            owner=owner,
            repo=repo,
            all=all,
            status_types=status_types,
            to_status=to_status,
            last_read_at=last_read_at,
        )

    @checked
    def mark_thread_read(
        self,
        id: StrictStr,
        *,
        to_status: Optional[StrictStr] = None,
    ) -> NotificationThread:
        """Mark a notification thread read (notifyReadThread)."""
        return self._call(
            _notify_read_thread,
            id=id,
            to_status=to_status,
        )


class AsyncNotificationsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[NotificationThread]:
        """List one page of your notification threads (notifyGetList)."""
        return await self._call(
            _notify_get_list,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.NotificationThread]:
        """Iterate every item across all pages."""
        return self._paginate(
            _notify_get_list,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    async def list_for_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[NotificationThread]:
        """List one page of your notification threads on a repository (notifyGetRepoList)."""
        return await self._call(
            _notify_get_repo_list,
            owner=owner,
            repo=repo,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    def iter_for_repo(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        all: Optional[StrictBool] = None,
        status_types: Optional[List[StrictStr]] = None,
        subject_type: Optional[List[StrictStr]] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.NotificationThread]:
        """Iterate every item across all pages."""
        return self._paginate(
            _notify_get_repo_list,
            owner=owner,
            repo=repo,
            all=all,
            status_types=status_types,
            subject_type=subject_type,
            since=since,
            before=before,
            page=page,
            limit=limit,
        )

    @checked
    async def get_thread(
        self,
        id: StrictStr,
    ) -> NotificationThread:
        """Get a notification thread (notifyGetThread)."""
        return await self._call(
            _notify_get_thread,
            id=id,
        )

    @checked
    async def count_unread(
        self,
    ) -> NotificationCount:
        """Count your unread notification threads (notifyNewAvailable)."""
        return await self._call(
            _notify_new_available,
        )

    @checked
    async def mark_read(
        self,
        *,
        last_read_at: Optional[datetime] = None,
        all: Optional[StrictStr] = None,
        status_types: Optional[List[StrictStr]] = None,
        to_status: Optional[StrictStr] = None,
    ) -> List[NotificationThread]:
        """Mark your notification threads read (notifyReadList)."""
        return await self._call(
            _notify_read_list,
            last_read_at=last_read_at,
            all=all,
            status_types=status_types,
            to_status=to_status,
        )

    @checked
    async def mark_repo_read(
        self,
        owner: StrictStr,
        repo: StrictStr,
        *,
        all: Optional[StrictStr] = None,
        status_types: Optional[List[StrictStr]] = None,
        to_status: Optional[StrictStr] = None,
        last_read_at: Optional[datetime] = None,
    ) -> List[NotificationThread]:
        """Mark your notification threads on a repository read (notifyReadRepoList)."""
        return await self._call(
            _notify_read_repo_list,
            owner=owner,
            repo=repo,
            all=all,
            status_types=status_types,
            to_status=to_status,
            last_read_at=last_read_at,
        )

    @checked
    async def mark_thread_read(
        self,
        id: StrictStr,
        *,
        to_status: Optional[StrictStr] = None,
    ) -> NotificationThread:
        """Mark a notification thread read (notifyReadThread)."""
        return await self._call(
            _notify_read_thread,
            id=id,
            to_status=to_status,
        )
