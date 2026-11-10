# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
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
from gitea_rest.models.create_email_option import CreateEmailOption
from gitea_rest.models.create_gpg_key_option import CreateGPGKeyOption
from gitea_rest.models.create_key_option import CreateKeyOption
from gitea_rest.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from gitea_rest.models.create_repo_option import CreateRepoOption
from gitea_rest.models.current_access_token import CurrentAccessToken
from gitea_rest.models.delete_email_option import DeleteEmailOption
from gitea_rest.models.email import Email
from gitea_rest.models.gpg_key import GPGKey
from gitea_rest.models.o_auth2_application import OAuth2Application
from gitea_rest.models.organization import Organization
from gitea_rest.models.public_key import PublicKey
from gitea_rest.models.repository import Repository
from gitea_rest.models.stop_watch import StopWatch
from gitea_rest.models.team import Team
from gitea_rest.models.tracked_time import TrackedTime
from gitea_rest.models.update_user_avatar_option import UpdateUserAvatarOption
from gitea_rest.models.user import User
from gitea_rest.models.user_settings import UserSettings
from gitea_rest.models.user_settings_options import UserSettingsOptions
from gitea_rest.models.watch_info import WatchInfo

_create_current_user_repo: Operation[Repository] = Operation(
    id="createCurrentUserRepo",
    method="POST",
    path="/user/repos",
    resource="current_user",
    name="create_repo",
    params=(),
    response=Repository,
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
_delete_current_token: Operation[None] = Operation(
    id="deleteCurrentToken",
    method="DELETE",
    path="/token",
    resource="current_user",
    name="delete_token",
    params=(),
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
_get_current_token: Operation[CurrentAccessToken] = Operation(
    id="getCurrentToken",
    method="GET",
    path="/token",
    resource="current_user",
    name="get_token",
    params=(),
    response=CurrentAccessToken,
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
_get_user_settings: Operation[UserSettings] = Operation(
    id="getUserSettings",
    method="GET",
    path="/user/settings",
    resource="current_user",
    name="get_settings",
    params=(),
    response=UserSettings,
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
_get_verification_token: Operation[str] = Operation(
    id="getVerificationToken",
    method="GET",
    path="/user/gpg_key_token",
    resource="current_user",
    name="get_gpg_verification_token",
    params=(),
    response=str,
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
_org_list_current_user_orgs: Operation[List[Organization]] = Operation(
    id="orgListCurrentUserOrgs",
    method="GET",
    path="/user/orgs",
    resource="current_user",
    name="list_orgs",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Organization],
    returns_json=True,
    iterator="iter_orgs",
    item=_models.Organization,
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
_update_user_settings: Operation[UserSettings] = Operation(
    id="updateUserSettings",
    method="PATCH",
    path="/user/settings",
    resource="current_user",
    name="update_settings",
    params=(),
    response=UserSettings,
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
_user_add_email: Operation[List[Email]] = Operation(
    id="userAddEmail",
    method="POST",
    path="/user/emails",
    resource="current_user",
    name="add_emails",
    params=(),
    response=List[Email],
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
_user_block_user: Operation[None] = Operation(
    id="userBlockUser",
    method="PUT",
    path="/user/blocks/{username}",
    resource="current_user",
    name="block_user",
    params=(
        Param("username", "username", "path"),
        Param("note", "note", "query"),
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
_user_check_user_block: Operation[None] = Operation(
    id="userCheckUserBlock",
    method="GET",
    path="/user/blocks/{username}",
    resource="current_user",
    name="check_blocked_user",
    params=(Param("username", "username", "path"),),
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
_user_create_o_auth2_application: Operation[OAuth2Application] = Operation(
    id="userCreateOAuth2Application",
    method="POST",
    path="/user/applications/oauth2",
    resource="current_user",
    name="create_oauth2_app",
    params=(),
    response=OAuth2Application,
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
_user_current_check_following: Operation[None] = Operation(
    id="userCurrentCheckFollowing",
    method="GET",
    path="/user/following/{username}",
    resource="current_user",
    name="check_following",
    params=(Param("username", "username", "path"),),
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
_user_current_check_starring: Operation[None] = Operation(
    id="userCurrentCheckStarring",
    method="GET",
    path="/user/starred/{owner}/{repo}",
    resource="current_user",
    name="check_starred",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
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
_user_current_check_subscription: Operation[WatchInfo] = Operation(
    id="userCurrentCheckSubscription",
    method="GET",
    path="/repos/{owner}/{repo}/subscription",
    resource="current_user",
    name="check_watching",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
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
_user_current_delete_follow: Operation[None] = Operation(
    id="userCurrentDeleteFollow",
    method="DELETE",
    path="/user/following/{username}",
    resource="current_user",
    name="unfollow",
    params=(Param("username", "username", "path"),),
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
_user_current_delete_gpg_key: Operation[None] = Operation(
    id="userCurrentDeleteGPGKey",
    method="DELETE",
    path="/user/gpg_keys/{id}",
    resource="current_user",
    name="delete_gpg_key",
    params=(Param("id", "id", "path"),),
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
_user_current_delete_key: Operation[None] = Operation(
    id="userCurrentDeleteKey",
    method="DELETE",
    path="/user/keys/{id}",
    resource="current_user",
    name="delete_key",
    params=(Param("id", "id", "path"),),
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
_user_current_delete_star: Operation[None] = Operation(
    id="userCurrentDeleteStar",
    method="DELETE",
    path="/user/starred/{owner}/{repo}",
    resource="current_user",
    name="unstar",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
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
_user_current_delete_subscription: Operation[None] = Operation(
    id="userCurrentDeleteSubscription",
    method="DELETE",
    path="/repos/{owner}/{repo}/subscription",
    resource="current_user",
    name="unwatch",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
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
_user_current_get_gpg_key: Operation[GPGKey] = Operation(
    id="userCurrentGetGPGKey",
    method="GET",
    path="/user/gpg_keys/{id}",
    resource="current_user",
    name="get_gpg_key",
    params=(Param("id", "id", "path"),),
    response=GPGKey,
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
_user_current_get_key: Operation[PublicKey] = Operation(
    id="userCurrentGetKey",
    method="GET",
    path="/user/keys/{id}",
    resource="current_user",
    name="get_key",
    params=(Param("id", "id", "path"),),
    response=PublicKey,
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
_user_current_list_followers: Operation[List[User]] = Operation(
    id="userCurrentListFollowers",
    method="GET",
    path="/user/followers",
    resource="current_user",
    name="list_followers",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_followers",
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
_user_current_list_following: Operation[List[User]] = Operation(
    id="userCurrentListFollowing",
    method="GET",
    path="/user/following",
    resource="current_user",
    name="list_following",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_following",
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
_user_current_list_gpg_keys: Operation[List[GPGKey]] = Operation(
    id="userCurrentListGPGKeys",
    method="GET",
    path="/user/gpg_keys",
    resource="current_user",
    name="list_gpg_keys",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[GPGKey],
    returns_json=True,
    iterator="iter_gpg_keys",
    item=_models.GPGKey,
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
_user_current_list_keys: Operation[List[PublicKey]] = Operation(
    id="userCurrentListKeys",
    method="GET",
    path="/user/keys",
    resource="current_user",
    name="list_keys",
    params=(
        Param("fingerprint", "fingerprint", "query"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[PublicKey],
    returns_json=True,
    iterator="iter_keys",
    item=_models.PublicKey,
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
_user_current_list_repos: Operation[List[Repository]] = Operation(
    id="userCurrentListRepos",
    method="GET",
    path="/user/repos",
    resource="current_user",
    name="list_repos",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Repository],
    returns_json=True,
    iterator="iter_repos",
    item=_models.Repository,
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
_user_current_list_starred: Operation[List[Repository]] = Operation(
    id="userCurrentListStarred",
    method="GET",
    path="/user/starred",
    resource="current_user",
    name="list_starred",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Repository],
    returns_json=True,
    iterator="iter_starred",
    item=_models.Repository,
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
_user_current_list_subscriptions: Operation[List[Repository]] = Operation(
    id="userCurrentListSubscriptions",
    method="GET",
    path="/user/subscriptions",
    resource="current_user",
    name="list_watched",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Repository],
    returns_json=True,
    iterator="iter_watched",
    item=_models.Repository,
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
_user_current_post_gpg_key: Operation[GPGKey] = Operation(
    id="userCurrentPostGPGKey",
    method="POST",
    path="/user/gpg_keys",
    resource="current_user",
    name="add_gpg_key",
    params=(),
    response=GPGKey,
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
_user_current_post_key: Operation[PublicKey] = Operation(
    id="userCurrentPostKey",
    method="POST",
    path="/user/keys",
    resource="current_user",
    name="add_key",
    params=(),
    response=PublicKey,
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
_user_current_put_follow: Operation[None] = Operation(
    id="userCurrentPutFollow",
    method="PUT",
    path="/user/following/{username}",
    resource="current_user",
    name="follow",
    params=(Param("username", "username", "path"),),
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
_user_current_put_star: Operation[None] = Operation(
    id="userCurrentPutStar",
    method="PUT",
    path="/user/starred/{owner}/{repo}",
    resource="current_user",
    name="star",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
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
_user_current_put_subscription: Operation[WatchInfo] = Operation(
    id="userCurrentPutSubscription",
    method="PUT",
    path="/repos/{owner}/{repo}/subscription",
    resource="current_user",
    name="watch",
    params=(
        Param("owner", "owner", "path"),
        Param("repo", "repo", "path"),
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
_user_current_tracked_times: Operation[List[TrackedTime]] = Operation(
    id="userCurrentTrackedTimes",
    method="GET",
    path="/user/times",
    resource="current_user",
    name="list_tracked_times",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("since", "since", "query"),
        Param("before", "before", "query"),
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
_user_delete_avatar: Operation[None] = Operation(
    id="userDeleteAvatar",
    method="DELETE",
    path="/user/avatar",
    resource="current_user",
    name="delete_avatar",
    params=(),
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
_user_delete_email: Operation[None] = Operation(
    id="userDeleteEmail",
    method="DELETE",
    path="/user/emails",
    resource="current_user",
    name="delete_emails",
    params=(),
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
_user_delete_o_auth2_application: Operation[None] = Operation(
    id="userDeleteOAuth2Application",
    method="DELETE",
    path="/user/applications/oauth2/{id}",
    resource="current_user",
    name="delete_oauth2_app",
    params=(Param("id", "id", "path"),),
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
_user_get_current: Operation[User] = Operation(
    id="userGetCurrent",
    method="GET",
    path="/user",
    resource="current_user",
    name="get",
    params=(),
    response=User,
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
_user_get_o_auth2_application: Operation[OAuth2Application] = Operation(
    id="userGetOAuth2Application",
    method="GET",
    path="/user/applications/oauth2/{id}",
    resource="current_user",
    name="get_oauth2_app",
    params=(Param("id", "id", "path"),),
    response=OAuth2Application,
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
_user_get_oauth2_application: Operation[List[OAuth2Application]] = Operation(
    id="userGetOauth2Application",
    method="GET",
    path="/user/applications/oauth2",
    resource="current_user",
    name="list_oauth2_apps",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[OAuth2Application],
    returns_json=True,
    iterator="iter_oauth2_apps",
    item=_models.OAuth2Application,
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
_user_get_stop_watches: Operation[List[StopWatch]] = Operation(
    id="userGetStopWatches",
    method="GET",
    path="/user/stopwatches",
    resource="current_user",
    name="list_stopwatches",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[StopWatch],
    returns_json=True,
    iterator="iter_stopwatches",
    item=_models.StopWatch,
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
_user_list_blocks: Operation[List[User]] = Operation(
    id="userListBlocks",
    method="GET",
    path="/user/blocks",
    resource="current_user",
    name="list_blocked_users",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[User],
    returns_json=True,
    iterator="iter_blocked_users",
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
_user_list_emails: Operation[List[Email]] = Operation(
    id="userListEmails",
    method="GET",
    path="/user/emails",
    resource="current_user",
    name="list_emails",
    params=(),
    response=List[Email],
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
_user_list_teams: Operation[List[Team]] = Operation(
    id="userListTeams",
    method="GET",
    path="/user/teams",
    resource="current_user",
    name="list_teams",
    params=(
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Team],
    returns_json=True,
    iterator="iter_teams",
    item=_models.Team,
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
_user_unblock_user: Operation[None] = Operation(
    id="userUnblockUser",
    method="DELETE",
    path="/user/blocks/{username}",
    resource="current_user",
    name="unblock_user",
    params=(Param("username", "username", "path"),),
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
_user_update_avatar: Operation[None] = Operation(
    id="userUpdateAvatar",
    method="POST",
    path="/user/avatar",
    resource="current_user",
    name="update_avatar",
    params=(),
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
_user_update_o_auth2_application: Operation[OAuth2Application] = Operation(
    id="userUpdateOAuth2Application",
    method="PATCH",
    path="/user/applications/oauth2/{id}",
    resource="current_user",
    name="update_oauth2_app",
    params=(Param("id", "id", "path"),),
    response=OAuth2Application,
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
_user_verify_gpg_key: Operation[GPGKey] = Operation(
    id="userVerifyGPGKey",
    method="POST",
    path="/user/gpg_key_verify",
    resource="current_user",
    name="verify_gpg_key",
    params=(),
    response=GPGKey,
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
    _create_current_user_repo,
    _delete_current_token,
    _get_current_token,
    _get_user_settings,
    _get_verification_token,
    _org_list_current_user_orgs,
    _update_user_settings,
    _user_add_email,
    _user_block_user,
    _user_check_user_block,
    _user_create_o_auth2_application,
    _user_current_check_following,
    _user_current_check_starring,
    _user_current_check_subscription,
    _user_current_delete_follow,
    _user_current_delete_gpg_key,
    _user_current_delete_key,
    _user_current_delete_star,
    _user_current_delete_subscription,
    _user_current_get_gpg_key,
    _user_current_get_key,
    _user_current_list_followers,
    _user_current_list_following,
    _user_current_list_gpg_keys,
    _user_current_list_keys,
    _user_current_list_repos,
    _user_current_list_starred,
    _user_current_list_subscriptions,
    _user_current_post_gpg_key,
    _user_current_post_key,
    _user_current_put_follow,
    _user_current_put_star,
    _user_current_put_subscription,
    _user_current_tracked_times,
    _user_delete_avatar,
    _user_delete_email,
    _user_delete_o_auth2_application,
    _user_get_current,
    _user_get_o_auth2_application,
    _user_get_oauth2_application,
    _user_get_stop_watches,
    _user_list_blocks,
    _user_list_emails,
    _user_list_teams,
    _user_unblock_user,
    _user_update_avatar,
    _user_update_o_auth2_application,
    _user_verify_gpg_key,
)


class CurrentUserApi(Resource):
    @checked
    def create_repo(
        self,
        body: Optional[Union[CreateRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Create a repository of your own (createCurrentUserRepo)."""
        return self._call(
            _create_current_user_repo,
            _body=body,
        )

    @checked
    def delete_token(
        self,
    ) -> None:
        """Delete the access token you are authenticated with (deleteCurrentToken)."""
        return self._call(
            _delete_current_token,
        )

    @checked
    def get_token(
        self,
    ) -> CurrentAccessToken:
        """Get the access token you are authenticated with (getCurrentToken)."""
        return self._call(
            _get_current_token,
        )

    @checked
    def get_settings(
        self,
    ) -> UserSettings:
        """Get your user settings (getUserSettings)."""
        return self._call(
            _get_user_settings,
        )

    @checked
    def get_gpg_verification_token(
        self,
    ) -> str:
        """Get the token to sign to verify a GPG key (getVerificationToken)."""
        return self._call(
            _get_verification_token,
        )

    @checked
    def list_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of your organizations (orgListCurrentUserOrgs)."""
        return self._call(
            _org_list_current_user_orgs,
            page=page,
            limit=limit,
        )

    @checked
    def iter_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_current_user_orgs,
            page=page,
            limit=limit,
        )

    @checked
    def update_settings(
        self,
        body: Optional[Union[UserSettingsOptions, Mapping[str, Any]]] = None,
    ) -> UserSettings:
        """Change your user settings (updateUserSettings)."""
        return self._call(
            _update_user_settings,
            _body=body,
        )

    @checked
    def add_emails(
        self,
        body: Optional[Union[CreateEmailOption, Mapping[str, Any]]] = None,
    ) -> List[Email]:
        """Add email addresses (userAddEmail)."""
        return self._call(
            _user_add_email,
            _body=body,
        )

    @checked
    def block_user(
        self,
        username: StrictStr,
        *,
        note: Optional[StrictStr] = None,
    ) -> None:
        """Block a user (userBlockUser)."""
        return self._call(
            _user_block_user,
            username=username,
            note=note,
        )

    @checked
    def check_blocked_user(
        self,
        username: StrictStr,
    ) -> None:
        """Check whether you block a user (userCheckUserBlock)."""
        return self._call(
            _user_check_user_block,
            username=username,
        )

    @checked
    def create_oauth2_app(
        self,
        body: Union[CreateOAuth2ApplicationOptions, Mapping[str, Any]],
    ) -> OAuth2Application:
        """Create an OAuth2 application (userCreateOAuth2Application)."""
        return self._call(
            _user_create_o_auth2_application,
            _body=body,
        )

    @checked
    def check_following(
        self,
        username: StrictStr,
    ) -> None:
        """Check whether you follow a user (userCurrentCheckFollowing)."""
        return self._call(
            _user_current_check_following,
            username=username,
        )

    @checked
    def check_starred(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Check whether you starred a repository (userCurrentCheckStarring)."""
        return self._call(
            _user_current_check_starring,
            owner=owner,
            repo=repo,
        )

    @checked
    def check_watching(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> WatchInfo:
        """Check whether you watch a repository (userCurrentCheckSubscription)."""
        return self._call(
            _user_current_check_subscription,
            owner=owner,
            repo=repo,
        )

    @checked
    def unfollow(
        self,
        username: StrictStr,
    ) -> None:
        """Stop following a user (userCurrentDeleteFollow)."""
        return self._call(
            _user_current_delete_follow,
            username=username,
        )

    @checked
    def delete_gpg_key(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your GPG keys (userCurrentDeleteGPGKey)."""
        return self._call(
            _user_current_delete_gpg_key,
            id=id,
        )

    @checked
    def delete_key(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your SSH keys (userCurrentDeleteKey)."""
        return self._call(
            _user_current_delete_key,
            id=id,
        )

    @checked
    def unstar(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Unstar a repository (userCurrentDeleteStar)."""
        return self._call(
            _user_current_delete_star,
            owner=owner,
            repo=repo,
        )

    @checked
    def unwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Stop watching a repository (userCurrentDeleteSubscription)."""
        return self._call(
            _user_current_delete_subscription,
            owner=owner,
            repo=repo,
        )

    @checked
    def get_gpg_key(
        self,
        id: StrictInt,
    ) -> GPGKey:
        """Get one of your GPG keys (userCurrentGetGPGKey)."""
        return self._call(
            _user_current_get_gpg_key,
            id=id,
        )

    @checked
    def get_key(
        self,
        id: StrictInt,
    ) -> PublicKey:
        """Get one of your SSH keys (userCurrentGetKey)."""
        return self._call(
            _user_current_get_key,
            id=id,
        )

    @checked
    def list_followers(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of your followers (userCurrentListFollowers)."""
        return self._call(
            _user_current_list_followers,
            page=page,
            limit=limit,
        )

    @checked
    def iter_followers(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_followers,
            page=page,
            limit=limit,
        )

    @checked
    def list_following(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users you follow (userCurrentListFollowing)."""
        return self._call(
            _user_current_list_following,
            page=page,
            limit=limit,
        )

    @checked
    def iter_following(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_following,
            page=page,
            limit=limit,
        )

    @checked
    def list_gpg_keys(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[GPGKey]:
        """List one page of your GPG keys (userCurrentListGPGKeys)."""
        return self._call(
            _user_current_list_gpg_keys,
            page=page,
            limit=limit,
        )

    @checked
    def iter_gpg_keys(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.GPGKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_gpg_keys,
            page=page,
            limit=limit,
        )

    @checked
    def list_keys(
        self,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PublicKey]:
        """List one page of your SSH keys (userCurrentListKeys)."""
        return self._call(
            _user_current_list_keys,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def iter_keys(
        self,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.PublicKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_keys,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def list_repos(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories you own or can access (userCurrentListRepos)."""
        return self._call(
            _user_current_list_repos,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_repos,
            page=page,
            limit=limit,
        )

    @checked
    def list_starred(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories you starred (userCurrentListStarred)."""
        return self._call(
            _user_current_list_starred,
            page=page,
            limit=limit,
        )

    @checked
    def iter_starred(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_starred,
            page=page,
            limit=limit,
        )

    @checked
    def list_watched(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories you watch (userCurrentListSubscriptions)."""
        return self._call(
            _user_current_list_subscriptions,
            page=page,
            limit=limit,
        )

    @checked
    def iter_watched(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_subscriptions,
            page=page,
            limit=limit,
        )

    @checked
    def add_gpg_key(
        self,
        body: Optional[Union[CreateGPGKeyOption, Mapping[str, Any]]] = None,
    ) -> GPGKey:
        """Add a GPG key (userCurrentPostGPGKey)."""
        return self._call(
            _user_current_post_gpg_key,
            _body=body,
        )

    @checked
    def add_key(
        self,
        body: Optional[Union[CreateKeyOption, Mapping[str, Any]]] = None,
    ) -> PublicKey:
        """Add an SSH key (userCurrentPostKey)."""
        return self._call(
            _user_current_post_key,
            _body=body,
        )

    @checked
    def follow(
        self,
        username: StrictStr,
    ) -> None:
        """Follow a user (userCurrentPutFollow)."""
        return self._call(
            _user_current_put_follow,
            username=username,
        )

    @checked
    def star(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Star a repository (userCurrentPutStar)."""
        return self._call(
            _user_current_put_star,
            owner=owner,
            repo=repo,
        )

    @checked
    def watch(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> WatchInfo:
        """Watch a repository (userCurrentPutSubscription)."""
        return self._call(
            _user_current_put_subscription,
            owner=owner,
            repo=repo,
        )

    @checked
    def list_tracked_times(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
    ) -> List[TrackedTime]:
        """List one page of the time you tracked (userCurrentTrackedTimes)."""
        return self._call(
            _user_current_tracked_times,
            page=page,
            limit=limit,
            since=since,
            before=before,
        )

    @checked
    def iter_tracked_times(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
    ) -> Iterator[_models.TrackedTime]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_tracked_times,
            page=page,
            limit=limit,
            since=since,
            before=before,
        )

    @checked
    def delete_avatar(
        self,
    ) -> None:
        """Remove your avatar (userDeleteAvatar)."""
        return self._call(
            _user_delete_avatar,
        )

    @checked
    def delete_emails(
        self,
        body: Optional[Union[DeleteEmailOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove email addresses (userDeleteEmail)."""
        return self._call(
            _user_delete_email,
            _body=body,
        )

    @checked
    def delete_oauth2_app(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your OAuth2 applications (userDeleteOAuth2Application)."""
        return self._call(
            _user_delete_o_auth2_application,
            id=id,
        )

    @checked
    def get(
        self,
    ) -> User:
        """Get the user you are authenticated as (userGetCurrent)."""
        return self._call(
            _user_get_current,
        )

    @checked
    def get_oauth2_app(
        self,
        id: StrictInt,
    ) -> OAuth2Application:
        """Get one of your OAuth2 applications (userGetOAuth2Application)."""
        return self._call(
            _user_get_o_auth2_application,
            id=id,
        )

    @checked
    def list_oauth2_apps(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[OAuth2Application]:
        """List one page of your OAuth2 applications (userGetOauth2Application)."""
        return self._call(
            _user_get_oauth2_application,
            page=page,
            limit=limit,
        )

    @checked
    def iter_oauth2_apps(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.OAuth2Application]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_get_oauth2_application,
            page=page,
            limit=limit,
        )

    @checked
    def list_stopwatches(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[StopWatch]:
        """List one page of your running stopwatches (userGetStopWatches)."""
        return self._call(
            _user_get_stop_watches,
            page=page,
            limit=limit,
        )

    @checked
    def iter_stopwatches(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.StopWatch]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_get_stop_watches,
            page=page,
            limit=limit,
        )

    @checked
    def list_blocked_users(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users you block (userListBlocks)."""
        return self._call(
            _user_list_blocks,
            page=page,
            limit=limit,
        )

    @checked
    def iter_blocked_users(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_blocks,
            page=page,
            limit=limit,
        )

    @checked
    def list_emails(
        self,
    ) -> List[Email]:
        """List your email addresses (userListEmails)."""
        return self._call(
            _user_list_emails,
        )

    @checked
    def list_teams(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Team]:
        """List one page of the teams you are in (userListTeams)."""
        return self._call(
            _user_list_teams,
            page=page,
            limit=limit,
        )

    @checked
    def iter_teams(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Team]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_teams,
            page=page,
            limit=limit,
        )

    @checked
    def unblock_user(
        self,
        username: StrictStr,
    ) -> None:
        """Unblock a user (userUnblockUser)."""
        return self._call(
            _user_unblock_user,
            username=username,
        )

    @checked
    def update_avatar(
        self,
        body: Optional[Union[UpdateUserAvatarOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Set your avatar (userUpdateAvatar)."""
        return self._call(
            _user_update_avatar,
            _body=body,
        )

    @checked
    def update_oauth2_app(
        self,
        id: StrictInt,
        body: Union[CreateOAuth2ApplicationOptions, Mapping[str, Any]],
    ) -> OAuth2Application:
        """Change one of your OAuth2 applications (userUpdateOAuth2Application)."""
        return self._call(
            _user_update_o_auth2_application,
            id=id,
            _body=body,
        )

    @checked
    def verify_gpg_key(
        self,
    ) -> GPGKey:
        """Verify a GPG key with a signed token (userVerifyGPGKey)."""
        return self._call(
            _user_verify_gpg_key,
        )


class AsyncCurrentUserApi(AsyncResource):
    @checked
    async def create_repo(
        self,
        body: Optional[Union[CreateRepoOption, Mapping[str, Any]]] = None,
    ) -> Repository:
        """Create a repository of your own (createCurrentUserRepo)."""
        return await self._call(
            _create_current_user_repo,
            _body=body,
        )

    @checked
    async def delete_token(
        self,
    ) -> None:
        """Delete the access token you are authenticated with (deleteCurrentToken)."""
        return await self._call(
            _delete_current_token,
        )

    @checked
    async def get_token(
        self,
    ) -> CurrentAccessToken:
        """Get the access token you are authenticated with (getCurrentToken)."""
        return await self._call(
            _get_current_token,
        )

    @checked
    async def get_settings(
        self,
    ) -> UserSettings:
        """Get your user settings (getUserSettings)."""
        return await self._call(
            _get_user_settings,
        )

    @checked
    async def get_gpg_verification_token(
        self,
    ) -> str:
        """Get the token to sign to verify a GPG key (getVerificationToken)."""
        return await self._call(
            _get_verification_token,
        )

    @checked
    async def list_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Organization]:
        """List one page of your organizations (orgListCurrentUserOrgs)."""
        return await self._call(
            _org_list_current_user_orgs,
            page=page,
            limit=limit,
        )

    @checked
    def iter_orgs(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Organization]:
        """Iterate every item across all pages."""
        return self._paginate(
            _org_list_current_user_orgs,
            page=page,
            limit=limit,
        )

    @checked
    async def update_settings(
        self,
        body: Optional[Union[UserSettingsOptions, Mapping[str, Any]]] = None,
    ) -> UserSettings:
        """Change your user settings (updateUserSettings)."""
        return await self._call(
            _update_user_settings,
            _body=body,
        )

    @checked
    async def add_emails(
        self,
        body: Optional[Union[CreateEmailOption, Mapping[str, Any]]] = None,
    ) -> List[Email]:
        """Add email addresses (userAddEmail)."""
        return await self._call(
            _user_add_email,
            _body=body,
        )

    @checked
    async def block_user(
        self,
        username: StrictStr,
        *,
        note: Optional[StrictStr] = None,
    ) -> None:
        """Block a user (userBlockUser)."""
        return await self._call(
            _user_block_user,
            username=username,
            note=note,
        )

    @checked
    async def check_blocked_user(
        self,
        username: StrictStr,
    ) -> None:
        """Check whether you block a user (userCheckUserBlock)."""
        return await self._call(
            _user_check_user_block,
            username=username,
        )

    @checked
    async def create_oauth2_app(
        self,
        body: Union[CreateOAuth2ApplicationOptions, Mapping[str, Any]],
    ) -> OAuth2Application:
        """Create an OAuth2 application (userCreateOAuth2Application)."""
        return await self._call(
            _user_create_o_auth2_application,
            _body=body,
        )

    @checked
    async def check_following(
        self,
        username: StrictStr,
    ) -> None:
        """Check whether you follow a user (userCurrentCheckFollowing)."""
        return await self._call(
            _user_current_check_following,
            username=username,
        )

    @checked
    async def check_starred(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Check whether you starred a repository (userCurrentCheckStarring)."""
        return await self._call(
            _user_current_check_starring,
            owner=owner,
            repo=repo,
        )

    @checked
    async def check_watching(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> WatchInfo:
        """Check whether you watch a repository (userCurrentCheckSubscription)."""
        return await self._call(
            _user_current_check_subscription,
            owner=owner,
            repo=repo,
        )

    @checked
    async def unfollow(
        self,
        username: StrictStr,
    ) -> None:
        """Stop following a user (userCurrentDeleteFollow)."""
        return await self._call(
            _user_current_delete_follow,
            username=username,
        )

    @checked
    async def delete_gpg_key(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your GPG keys (userCurrentDeleteGPGKey)."""
        return await self._call(
            _user_current_delete_gpg_key,
            id=id,
        )

    @checked
    async def delete_key(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your SSH keys (userCurrentDeleteKey)."""
        return await self._call(
            _user_current_delete_key,
            id=id,
        )

    @checked
    async def unstar(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Unstar a repository (userCurrentDeleteStar)."""
        return await self._call(
            _user_current_delete_star,
            owner=owner,
            repo=repo,
        )

    @checked
    async def unwatch(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Stop watching a repository (userCurrentDeleteSubscription)."""
        return await self._call(
            _user_current_delete_subscription,
            owner=owner,
            repo=repo,
        )

    @checked
    async def get_gpg_key(
        self,
        id: StrictInt,
    ) -> GPGKey:
        """Get one of your GPG keys (userCurrentGetGPGKey)."""
        return await self._call(
            _user_current_get_gpg_key,
            id=id,
        )

    @checked
    async def get_key(
        self,
        id: StrictInt,
    ) -> PublicKey:
        """Get one of your SSH keys (userCurrentGetKey)."""
        return await self._call(
            _user_current_get_key,
            id=id,
        )

    @checked
    async def list_followers(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of your followers (userCurrentListFollowers)."""
        return await self._call(
            _user_current_list_followers,
            page=page,
            limit=limit,
        )

    @checked
    def iter_followers(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_followers,
            page=page,
            limit=limit,
        )

    @checked
    async def list_following(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users you follow (userCurrentListFollowing)."""
        return await self._call(
            _user_current_list_following,
            page=page,
            limit=limit,
        )

    @checked
    def iter_following(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_following,
            page=page,
            limit=limit,
        )

    @checked
    async def list_gpg_keys(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[GPGKey]:
        """List one page of your GPG keys (userCurrentListGPGKeys)."""
        return await self._call(
            _user_current_list_gpg_keys,
            page=page,
            limit=limit,
        )

    @checked
    def iter_gpg_keys(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.GPGKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_gpg_keys,
            page=page,
            limit=limit,
        )

    @checked
    async def list_keys(
        self,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[PublicKey]:
        """List one page of your SSH keys (userCurrentListKeys)."""
        return await self._call(
            _user_current_list_keys,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    def iter_keys(
        self,
        *,
        fingerprint: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.PublicKey]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_keys,
            fingerprint=fingerprint,
            page=page,
            limit=limit,
        )

    @checked
    async def list_repos(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories you own or can access (userCurrentListRepos)."""
        return await self._call(
            _user_current_list_repos,
            page=page,
            limit=limit,
        )

    @checked
    def iter_repos(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_repos,
            page=page,
            limit=limit,
        )

    @checked
    async def list_starred(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories you starred (userCurrentListStarred)."""
        return await self._call(
            _user_current_list_starred,
            page=page,
            limit=limit,
        )

    @checked
    def iter_starred(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_starred,
            page=page,
            limit=limit,
        )

    @checked
    async def list_watched(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Repository]:
        """List one page of the repositories you watch (userCurrentListSubscriptions)."""
        return await self._call(
            _user_current_list_subscriptions,
            page=page,
            limit=limit,
        )

    @checked
    def iter_watched(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Repository]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_list_subscriptions,
            page=page,
            limit=limit,
        )

    @checked
    async def add_gpg_key(
        self,
        body: Optional[Union[CreateGPGKeyOption, Mapping[str, Any]]] = None,
    ) -> GPGKey:
        """Add a GPG key (userCurrentPostGPGKey)."""
        return await self._call(
            _user_current_post_gpg_key,
            _body=body,
        )

    @checked
    async def add_key(
        self,
        body: Optional[Union[CreateKeyOption, Mapping[str, Any]]] = None,
    ) -> PublicKey:
        """Add an SSH key (userCurrentPostKey)."""
        return await self._call(
            _user_current_post_key,
            _body=body,
        )

    @checked
    async def follow(
        self,
        username: StrictStr,
    ) -> None:
        """Follow a user (userCurrentPutFollow)."""
        return await self._call(
            _user_current_put_follow,
            username=username,
        )

    @checked
    async def star(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> None:
        """Star a repository (userCurrentPutStar)."""
        return await self._call(
            _user_current_put_star,
            owner=owner,
            repo=repo,
        )

    @checked
    async def watch(
        self,
        owner: StrictStr,
        repo: StrictStr,
    ) -> WatchInfo:
        """Watch a repository (userCurrentPutSubscription)."""
        return await self._call(
            _user_current_put_subscription,
            owner=owner,
            repo=repo,
        )

    @checked
    async def list_tracked_times(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
    ) -> List[TrackedTime]:
        """List one page of the time you tracked (userCurrentTrackedTimes)."""
        return await self._call(
            _user_current_tracked_times,
            page=page,
            limit=limit,
            since=since,
            before=before,
        )

    @checked
    def iter_tracked_times(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        since: Optional[datetime] = None,
        before: Optional[datetime] = None,
    ) -> AsyncIterator[_models.TrackedTime]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_current_tracked_times,
            page=page,
            limit=limit,
            since=since,
            before=before,
        )

    @checked
    async def delete_avatar(
        self,
    ) -> None:
        """Remove your avatar (userDeleteAvatar)."""
        return await self._call(
            _user_delete_avatar,
        )

    @checked
    async def delete_emails(
        self,
        body: Optional[Union[DeleteEmailOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Remove email addresses (userDeleteEmail)."""
        return await self._call(
            _user_delete_email,
            _body=body,
        )

    @checked
    async def delete_oauth2_app(
        self,
        id: StrictInt,
    ) -> None:
        """Delete one of your OAuth2 applications (userDeleteOAuth2Application)."""
        return await self._call(
            _user_delete_o_auth2_application,
            id=id,
        )

    @checked
    async def get(
        self,
    ) -> User:
        """Get the user you are authenticated as (userGetCurrent)."""
        return await self._call(
            _user_get_current,
        )

    @checked
    async def get_oauth2_app(
        self,
        id: StrictInt,
    ) -> OAuth2Application:
        """Get one of your OAuth2 applications (userGetOAuth2Application)."""
        return await self._call(
            _user_get_o_auth2_application,
            id=id,
        )

    @checked
    async def list_oauth2_apps(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[OAuth2Application]:
        """List one page of your OAuth2 applications (userGetOauth2Application)."""
        return await self._call(
            _user_get_oauth2_application,
            page=page,
            limit=limit,
        )

    @checked
    def iter_oauth2_apps(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.OAuth2Application]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_get_oauth2_application,
            page=page,
            limit=limit,
        )

    @checked
    async def list_stopwatches(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[StopWatch]:
        """List one page of your running stopwatches (userGetStopWatches)."""
        return await self._call(
            _user_get_stop_watches,
            page=page,
            limit=limit,
        )

    @checked
    def iter_stopwatches(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.StopWatch]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_get_stop_watches,
            page=page,
            limit=limit,
        )

    @checked
    async def list_blocked_users(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[User]:
        """List one page of the users you block (userListBlocks)."""
        return await self._call(
            _user_list_blocks,
            page=page,
            limit=limit,
        )

    @checked
    def iter_blocked_users(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.User]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_blocks,
            page=page,
            limit=limit,
        )

    @checked
    async def list_emails(
        self,
    ) -> List[Email]:
        """List your email addresses (userListEmails)."""
        return await self._call(
            _user_list_emails,
        )

    @checked
    async def list_teams(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Team]:
        """List one page of the teams you are in (userListTeams)."""
        return await self._call(
            _user_list_teams,
            page=page,
            limit=limit,
        )

    @checked
    def iter_teams(
        self,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Team]:
        """Iterate every item across all pages."""
        return self._paginate(
            _user_list_teams,
            page=page,
            limit=limit,
        )

    @checked
    async def unblock_user(
        self,
        username: StrictStr,
    ) -> None:
        """Unblock a user (userUnblockUser)."""
        return await self._call(
            _user_unblock_user,
            username=username,
        )

    @checked
    async def update_avatar(
        self,
        body: Optional[Union[UpdateUserAvatarOption, Mapping[str, Any]]] = None,
    ) -> None:
        """Set your avatar (userUpdateAvatar)."""
        return await self._call(
            _user_update_avatar,
            _body=body,
        )

    @checked
    async def update_oauth2_app(
        self,
        id: StrictInt,
        body: Union[CreateOAuth2ApplicationOptions, Mapping[str, Any]],
    ) -> OAuth2Application:
        """Change one of your OAuth2 applications (userUpdateOAuth2Application)."""
        return await self._call(
            _user_update_o_auth2_application,
            id=id,
            _body=body,
        )

    @checked
    async def verify_gpg_key(
        self,
    ) -> GPGKey:
        """Verify a GPG key with a signed token (userVerifyGPGKey)."""
        return await self._call(
            _user_verify_gpg_key,
        )
