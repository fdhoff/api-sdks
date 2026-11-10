# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from gitea_rest._runtime import AsyncTransport, Operation, SyncTransport
from gitea_rest.api import (
    actions_api,
    admin_api,
    branches_api,
    commits_api,
    contents_api,
    current_user_api,
    git_api,
    hooks_api,
    issues_api,
    labels_api,
    milestones_api,
    misc_api,
    notifications_api,
    orgs_api,
    packages_api,
    projects_api,
    pulls_api,
    releases_api,
    repos_api,
    tags_api,
    teams_api,
    users_api,
    wiki_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        actions_api.OPERATIONS,
        admin_api.OPERATIONS,
        branches_api.OPERATIONS,
        commits_api.OPERATIONS,
        contents_api.OPERATIONS,
        current_user_api.OPERATIONS,
        git_api.OPERATIONS,
        hooks_api.OPERATIONS,
        issues_api.OPERATIONS,
        labels_api.OPERATIONS,
        milestones_api.OPERATIONS,
        misc_api.OPERATIONS,
        notifications_api.OPERATIONS,
        orgs_api.OPERATIONS,
        packages_api.OPERATIONS,
        projects_api.OPERATIONS,
        pulls_api.OPERATIONS,
        releases_api.OPERATIONS,
        repos_api.OPERATIONS,
        tags_api.OPERATIONS,
        teams_api.OPERATIONS,
        users_api.OPERATIONS,
        wiki_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.actions = actions_api.ActionsApi(transport)
        self.admin = admin_api.AdminApi(transport)
        self.branches = branches_api.BranchesApi(transport)
        self.commits = commits_api.CommitsApi(transport)
        self.contents = contents_api.ContentsApi(transport)
        self.current_user = current_user_api.CurrentUserApi(transport)
        self.git = git_api.GitApi(transport)
        self.hooks = hooks_api.HooksApi(transport)
        self.issues = issues_api.IssuesApi(transport)
        self.labels = labels_api.LabelsApi(transport)
        self.milestones = milestones_api.MilestonesApi(transport)
        self.misc = misc_api.MiscApi(transport)
        self.notifications = notifications_api.NotificationsApi(transport)
        self.orgs = orgs_api.OrgsApi(transport)
        self.packages = packages_api.PackagesApi(transport)
        self.projects = projects_api.ProjectsApi(transport)
        self.pulls = pulls_api.PullsApi(transport)
        self.releases = releases_api.ReleasesApi(transport)
        self.repos = repos_api.ReposApi(transport)
        self.tags = tags_api.TagsApi(transport)
        self.teams = teams_api.TeamsApi(transport)
        self.users = users_api.UsersApi(transport)
        self.wiki = wiki_api.WikiApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.actions = actions_api.AsyncActionsApi(transport)
        self.admin = admin_api.AsyncAdminApi(transport)
        self.branches = branches_api.AsyncBranchesApi(transport)
        self.commits = commits_api.AsyncCommitsApi(transport)
        self.contents = contents_api.AsyncContentsApi(transport)
        self.current_user = current_user_api.AsyncCurrentUserApi(transport)
        self.git = git_api.AsyncGitApi(transport)
        self.hooks = hooks_api.AsyncHooksApi(transport)
        self.issues = issues_api.AsyncIssuesApi(transport)
        self.labels = labels_api.AsyncLabelsApi(transport)
        self.milestones = milestones_api.AsyncMilestonesApi(transport)
        self.misc = misc_api.AsyncMiscApi(transport)
        self.notifications = notifications_api.AsyncNotificationsApi(transport)
        self.orgs = orgs_api.AsyncOrgsApi(transport)
        self.packages = packages_api.AsyncPackagesApi(transport)
        self.projects = projects_api.AsyncProjectsApi(transport)
        self.pulls = pulls_api.AsyncPullsApi(transport)
        self.releases = releases_api.AsyncReleasesApi(transport)
        self.repos = repos_api.AsyncReposApi(transport)
        self.tags = tags_api.AsyncTagsApi(transport)
        self.teams = teams_api.AsyncTeamsApi(transport)
        self.users = users_api.AsyncUsersApi(transport)
        self.wiki = wiki_api.AsyncWikiApi(transport)
