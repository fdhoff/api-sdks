# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

# import models into model package
from gitea_rest.models.api_error import APIError
from gitea_rest.models.access_level_name import AccessLevelName
from gitea_rest.models.access_token import AccessToken
from gitea_rest.models.action_artifact import ActionArtifact
from gitea_rest.models.action_artifacts_response import ActionArtifactsResponse
from gitea_rest.models.action_runner import ActionRunner
from gitea_rest.models.action_runner_label import ActionRunnerLabel
from gitea_rest.models.action_runners_response import ActionRunnersResponse
from gitea_rest.models.action_task import ActionTask
from gitea_rest.models.action_task_response import ActionTaskResponse
from gitea_rest.models.action_variable import ActionVariable
from gitea_rest.models.action_workflow import ActionWorkflow
from gitea_rest.models.action_workflow_job import ActionWorkflowJob
from gitea_rest.models.action_workflow_jobs_response import ActionWorkflowJobsResponse
from gitea_rest.models.action_workflow_response import ActionWorkflowResponse
from gitea_rest.models.action_workflow_run import ActionWorkflowRun
from gitea_rest.models.action_workflow_runs_response import ActionWorkflowRunsResponse
from gitea_rest.models.action_workflow_step import ActionWorkflowStep
from gitea_rest.models.activity import Activity
from gitea_rest.models.add_collaborator_option import AddCollaboratorOption
from gitea_rest.models.add_time_option import AddTimeOption
from gitea_rest.models.annotated_tag import AnnotatedTag
from gitea_rest.models.annotated_tag_object import AnnotatedTagObject
from gitea_rest.models.apply_diff_patch_file_options import ApplyDiffPatchFileOptions
from gitea_rest.models.attachment import Attachment
from gitea_rest.models.badge import Badge
from gitea_rest.models.branch import Branch
from gitea_rest.models.branch_protection import BranchProtection
from gitea_rest.models.change_file_operation import ChangeFileOperation
from gitea_rest.models.change_files_options import ChangeFilesOptions
from gitea_rest.models.changed_file import ChangedFile
from gitea_rest.models.combined_status import CombinedStatus
from gitea_rest.models.comment import Comment
from gitea_rest.models.commit import Commit
from gitea_rest.models.commit_affected_files import CommitAffectedFiles
from gitea_rest.models.commit_date_options import CommitDateOptions
from gitea_rest.models.commit_meta import CommitMeta
from gitea_rest.models.commit_stats import CommitStats
from gitea_rest.models.commit_status import CommitStatus
from gitea_rest.models.commit_status_state import CommitStatusState
from gitea_rest.models.commit_user import CommitUser
from gitea_rest.models.compare import Compare
from gitea_rest.models.contents_ext_response import ContentsExtResponse
from gitea_rest.models.contents_response import ContentsResponse
from gitea_rest.models.create_access_token_option import CreateAccessTokenOption
from gitea_rest.models.create_action_workflow_dispatch import CreateActionWorkflowDispatch
from gitea_rest.models.create_branch_protection_option import CreateBranchProtectionOption
from gitea_rest.models.create_branch_repo_option import CreateBranchRepoOption
from gitea_rest.models.create_deploy_key_token_option import CreateDeployKeyTokenOption
from gitea_rest.models.create_email_option import CreateEmailOption
from gitea_rest.models.create_file_options import CreateFileOptions
from gitea_rest.models.create_fork_option import CreateForkOption
from gitea_rest.models.create_gpg_key_option import CreateGPGKeyOption
from gitea_rest.models.create_hook_option import CreateHookOption
from gitea_rest.models.create_issue_comment_option import CreateIssueCommentOption
from gitea_rest.models.create_issue_option import CreateIssueOption
from gitea_rest.models.create_key_option import CreateKeyOption
from gitea_rest.models.create_label_option import CreateLabelOption
from gitea_rest.models.create_milestone_option import CreateMilestoneOption
from gitea_rest.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from gitea_rest.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from gitea_rest.models.create_org_option import CreateOrgOption
from gitea_rest.models.create_project_column_option import CreateProjectColumnOption
from gitea_rest.models.create_project_option import CreateProjectOption
from gitea_rest.models.create_pull_request_option import CreatePullRequestOption
from gitea_rest.models.create_pull_review_comment import CreatePullReviewComment
from gitea_rest.models.create_pull_review_comment_reply_options import CreatePullReviewCommentReplyOptions
from gitea_rest.models.create_pull_review_options import CreatePullReviewOptions
from gitea_rest.models.create_push_mirror_option import CreatePushMirrorOption
from gitea_rest.models.create_release_option import CreateReleaseOption
from gitea_rest.models.create_repo_option import CreateRepoOption
from gitea_rest.models.create_status_option import CreateStatusOption
from gitea_rest.models.create_tag_option import CreateTagOption
from gitea_rest.models.create_tag_protection_option import CreateTagProtectionOption
from gitea_rest.models.create_team_option import CreateTeamOption
from gitea_rest.models.create_user_option import CreateUserOption
from gitea_rest.models.create_variable_option import CreateVariableOption
from gitea_rest.models.create_wiki_page_options import CreateWikiPageOptions
from gitea_rest.models.cron import Cron
from gitea_rest.models.current_access_token import CurrentAccessToken
from gitea_rest.models.delete_email_option import DeleteEmailOption
from gitea_rest.models.delete_file_options import DeleteFileOptions
from gitea_rest.models.deploy_key import DeployKey
from gitea_rest.models.dismiss_pull_review_options import DismissPullReviewOptions
from gitea_rest.models.edit_action_runner_option import EditActionRunnerOption
from gitea_rest.models.edit_attachment_options import EditAttachmentOptions
from gitea_rest.models.edit_branch_protection_option import EditBranchProtectionOption
from gitea_rest.models.edit_deadline_option import EditDeadlineOption
from gitea_rest.models.edit_git_hook_option import EditGitHookOption
from gitea_rest.models.edit_hook_option import EditHookOption
from gitea_rest.models.edit_issue_comment_option import EditIssueCommentOption
from gitea_rest.models.edit_issue_option import EditIssueOption
from gitea_rest.models.edit_label_option import EditLabelOption
from gitea_rest.models.edit_milestone_option import EditMilestoneOption
from gitea_rest.models.edit_org_option import EditOrgOption
from gitea_rest.models.edit_project_column_option import EditProjectColumnOption
from gitea_rest.models.edit_project_option import EditProjectOption
from gitea_rest.models.edit_pull_request_option import EditPullRequestOption
from gitea_rest.models.edit_reaction_option import EditReactionOption
from gitea_rest.models.edit_release_option import EditReleaseOption
from gitea_rest.models.edit_repo_option import EditRepoOption
from gitea_rest.models.edit_tag_protection_option import EditTagProtectionOption
from gitea_rest.models.edit_team_option import EditTeamOption
from gitea_rest.models.edit_user_option import EditUserOption
from gitea_rest.models.email import Email
from gitea_rest.models.external_tracker import ExternalTracker
from gitea_rest.models.external_wiki import ExternalWiki
from gitea_rest.models.file_commit_response import FileCommitResponse
from gitea_rest.models.file_delete_response import FileDeleteResponse
from gitea_rest.models.file_links_response import FileLinksResponse
from gitea_rest.models.file_response import FileResponse
from gitea_rest.models.files_response import FilesResponse
from gitea_rest.models.gpg_key import GPGKey
from gitea_rest.models.gpg_key_email import GPGKeyEmail
from gitea_rest.models.general_api_settings import GeneralAPISettings
from gitea_rest.models.general_attachment_settings import GeneralAttachmentSettings
from gitea_rest.models.general_repo_settings import GeneralRepoSettings
from gitea_rest.models.general_ui_settings import GeneralUISettings
from gitea_rest.models.generate_repo_option import GenerateRepoOption
from gitea_rest.models.get_files_options import GetFilesOptions
from gitea_rest.models.git_blob_response import GitBlobResponse
from gitea_rest.models.git_entry import GitEntry
from gitea_rest.models.git_hook import GitHook
from gitea_rest.models.git_object import GitObject
from gitea_rest.models.git_tree_response import GitTreeResponse
from gitea_rest.models.gitignore_template_info import GitignoreTemplateInfo
from gitea_rest.models.hook import Hook
from gitea_rest.models.identity import Identity
from gitea_rest.models.internal_tracker import InternalTracker
from gitea_rest.models.issue import Issue
from gitea_rest.models.issue_assignees_option import IssueAssigneesOption
from gitea_rest.models.issue_config import IssueConfig
from gitea_rest.models.issue_config_contact_link import IssueConfigContactLink
from gitea_rest.models.issue_config_validation import IssueConfigValidation
from gitea_rest.models.issue_deadline import IssueDeadline
from gitea_rest.models.issue_form_field import IssueFormField
from gitea_rest.models.issue_labels_option import IssueLabelsOption
from gitea_rest.models.issue_meta import IssueMeta
from gitea_rest.models.issue_template import IssueTemplate
from gitea_rest.models.label import Label
from gitea_rest.models.label_template import LabelTemplate
from gitea_rest.models.license_template_info import LicenseTemplateInfo
from gitea_rest.models.licenses_template_list_entry import LicensesTemplateListEntry
from gitea_rest.models.lock_issue_option import LockIssueOption
from gitea_rest.models.markdown_option import MarkdownOption
from gitea_rest.models.markup_option import MarkupOption
from gitea_rest.models.merge_pull_request_option import MergePullRequestOption
from gitea_rest.models.merge_upstream_request import MergeUpstreamRequest
from gitea_rest.models.merge_upstream_response import MergeUpstreamResponse
from gitea_rest.models.migrate_repo_options import MigrateRepoOptions
from gitea_rest.models.milestone import Milestone
from gitea_rest.models.move_project_columns_option import MoveProjectColumnsOption
from gitea_rest.models.move_project_issue_option import MoveProjectIssueOption
from gitea_rest.models.new_issue_pins_allowed import NewIssuePinsAllowed
from gitea_rest.models.note import Note
from gitea_rest.models.notification_count import NotificationCount
from gitea_rest.models.notification_subject import NotificationSubject
from gitea_rest.models.notification_thread import NotificationThread
from gitea_rest.models.o_auth2_application import OAuth2Application
from gitea_rest.models.object_format_name import ObjectFormatName
from gitea_rest.models.organization import Organization
from gitea_rest.models.organization_permissions import OrganizationPermissions
from gitea_rest.models.pr_branch_info import PRBranchInfo
from gitea_rest.models.package import Package
from gitea_rest.models.package_file import PackageFile
from gitea_rest.models.payload_commit import PayloadCommit
from gitea_rest.models.payload_commit_verification import PayloadCommitVerification
from gitea_rest.models.payload_user import PayloadUser
from gitea_rest.models.permission import Permission
from gitea_rest.models.project import Project
from gitea_rest.models.project_column import ProjectColumn
from gitea_rest.models.public_key import PublicKey
from gitea_rest.models.pull_request import PullRequest
from gitea_rest.models.pull_request_meta import PullRequestMeta
from gitea_rest.models.pull_request_minimal import PullRequestMinimal
from gitea_rest.models.pull_request_minimal_head import PullRequestMinimalHead
from gitea_rest.models.pull_request_minimal_head_repo import PullRequestMinimalHeadRepo
from gitea_rest.models.pull_review import PullReview
from gitea_rest.models.pull_review_comment import PullReviewComment
from gitea_rest.models.pull_review_request_options import PullReviewRequestOptions
from gitea_rest.models.push_mirror import PushMirror
from gitea_rest.models.reaction import Reaction
from gitea_rest.models.reference import Reference
from gitea_rest.models.release import Release
from gitea_rest.models.rename_branch_repo_option import RenameBranchRepoOption
from gitea_rest.models.rename_org_option import RenameOrgOption
from gitea_rest.models.rename_user_option import RenameUserOption
from gitea_rest.models.repo_collaborator_permission import RepoCollaboratorPermission
from gitea_rest.models.repo_commit import RepoCommit
from gitea_rest.models.repo_topic_options import RepoTopicOptions
from gitea_rest.models.repo_transfer import RepoTransfer
from gitea_rest.models.repo_write_permission import RepoWritePermission
from gitea_rest.models.repository import Repository
from gitea_rest.models.repository_meta import RepositoryMeta
from gitea_rest.models.review_state_type import ReviewStateType
from gitea_rest.models.run_details import RunDetails
from gitea_rest.models.search_results import SearchResults
from gitea_rest.models.secret import Secret
from gitea_rest.models.server_version import ServerVersion
from gitea_rest.models.state_type import StateType
from gitea_rest.models.stop_watch import StopWatch
from gitea_rest.models.submit_pull_review_options import SubmitPullReviewOptions
from gitea_rest.models.tag import Tag
from gitea_rest.models.tag_protection import TagProtection
from gitea_rest.models.team import Team
from gitea_rest.models.team_search_results import TeamSearchResults
from gitea_rest.models.team_visibility import TeamVisibility
from gitea_rest.models.timeline_comment import TimelineComment
from gitea_rest.models.topic_list_response import TopicListResponse
from gitea_rest.models.topic_name import TopicName
from gitea_rest.models.topic_response import TopicResponse
from gitea_rest.models.tracked_time import TrackedTime
from gitea_rest.models.transfer_repo_option import TransferRepoOption
from gitea_rest.models.update_branch_protection_priories import UpdateBranchProtectionPriories
from gitea_rest.models.update_branch_repo_option import UpdateBranchRepoOption
from gitea_rest.models.update_file_options import UpdateFileOptions
from gitea_rest.models.update_repo_avatar_option import UpdateRepoAvatarOption
from gitea_rest.models.update_user_avatar_option import UpdateUserAvatarOption
from gitea_rest.models.update_variable_option import UpdateVariableOption
from gitea_rest.models.user import User
from gitea_rest.models.user_badge_option import UserBadgeOption
from gitea_rest.models.user_heatmap_data import UserHeatmapData
from gitea_rest.models.user_meta import UserMeta
from gitea_rest.models.user_search_results import UserSearchResults
from gitea_rest.models.user_settings import UserSettings
from gitea_rest.models.user_settings_options import UserSettingsOptions
from gitea_rest.models.user_type_string import UserTypeString
from gitea_rest.models.visibility_string import VisibilityString
from gitea_rest.models.watch_info import WatchInfo
from gitea_rest.models.wiki_commit import WikiCommit
from gitea_rest.models.wiki_commit_list import WikiCommitList
from gitea_rest.models.wiki_page import WikiPage
from gitea_rest.models.wiki_page_meta_data import WikiPageMetaData


__all__ = [
    "APIError",
    "AccessLevelName",
    "AccessToken",
    "ActionArtifact",
    "ActionArtifactsResponse",
    "ActionRunner",
    "ActionRunnerLabel",
    "ActionRunnersResponse",
    "ActionTask",
    "ActionTaskResponse",
    "ActionVariable",
    "ActionWorkflow",
    "ActionWorkflowJob",
    "ActionWorkflowJobsResponse",
    "ActionWorkflowResponse",
    "ActionWorkflowRun",
    "ActionWorkflowRunsResponse",
    "ActionWorkflowStep",
    "Activity",
    "AddCollaboratorOption",
    "AddTimeOption",
    "AnnotatedTag",
    "AnnotatedTagObject",
    "ApplyDiffPatchFileOptions",
    "Attachment",
    "Badge",
    "Branch",
    "BranchProtection",
    "ChangeFileOperation",
    "ChangeFilesOptions",
    "ChangedFile",
    "CombinedStatus",
    "Comment",
    "Commit",
    "CommitAffectedFiles",
    "CommitDateOptions",
    "CommitMeta",
    "CommitStats",
    "CommitStatus",
    "CommitStatusState",
    "CommitUser",
    "Compare",
    "ContentsExtResponse",
    "ContentsResponse",
    "CreateAccessTokenOption",
    "CreateActionWorkflowDispatch",
    "CreateBranchProtectionOption",
    "CreateBranchRepoOption",
    "CreateDeployKeyTokenOption",
    "CreateEmailOption",
    "CreateFileOptions",
    "CreateForkOption",
    "CreateGPGKeyOption",
    "CreateHookOption",
    "CreateIssueCommentOption",
    "CreateIssueOption",
    "CreateKeyOption",
    "CreateLabelOption",
    "CreateMilestoneOption",
    "CreateOAuth2ApplicationOptions",
    "CreateOrUpdateSecretOption",
    "CreateOrgOption",
    "CreateProjectColumnOption",
    "CreateProjectOption",
    "CreatePullRequestOption",
    "CreatePullReviewComment",
    "CreatePullReviewCommentReplyOptions",
    "CreatePullReviewOptions",
    "CreatePushMirrorOption",
    "CreateReleaseOption",
    "CreateRepoOption",
    "CreateStatusOption",
    "CreateTagOption",
    "CreateTagProtectionOption",
    "CreateTeamOption",
    "CreateUserOption",
    "CreateVariableOption",
    "CreateWikiPageOptions",
    "Cron",
    "CurrentAccessToken",
    "DeleteEmailOption",
    "DeleteFileOptions",
    "DeployKey",
    "DismissPullReviewOptions",
    "EditActionRunnerOption",
    "EditAttachmentOptions",
    "EditBranchProtectionOption",
    "EditDeadlineOption",
    "EditGitHookOption",
    "EditHookOption",
    "EditIssueCommentOption",
    "EditIssueOption",
    "EditLabelOption",
    "EditMilestoneOption",
    "EditOrgOption",
    "EditProjectColumnOption",
    "EditProjectOption",
    "EditPullRequestOption",
    "EditReactionOption",
    "EditReleaseOption",
    "EditRepoOption",
    "EditTagProtectionOption",
    "EditTeamOption",
    "EditUserOption",
    "Email",
    "ExternalTracker",
    "ExternalWiki",
    "FileCommitResponse",
    "FileDeleteResponse",
    "FileLinksResponse",
    "FileResponse",
    "FilesResponse",
    "GPGKey",
    "GPGKeyEmail",
    "GeneralAPISettings",
    "GeneralAttachmentSettings",
    "GeneralRepoSettings",
    "GeneralUISettings",
    "GenerateRepoOption",
    "GetFilesOptions",
    "GitBlobResponse",
    "GitEntry",
    "GitHook",
    "GitObject",
    "GitTreeResponse",
    "GitignoreTemplateInfo",
    "Hook",
    "Identity",
    "InternalTracker",
    "Issue",
    "IssueAssigneesOption",
    "IssueConfig",
    "IssueConfigContactLink",
    "IssueConfigValidation",
    "IssueDeadline",
    "IssueFormField",
    "IssueLabelsOption",
    "IssueMeta",
    "IssueTemplate",
    "Label",
    "LabelTemplate",
    "LicenseTemplateInfo",
    "LicensesTemplateListEntry",
    "LockIssueOption",
    "MarkdownOption",
    "MarkupOption",
    "MergePullRequestOption",
    "MergeUpstreamRequest",
    "MergeUpstreamResponse",
    "MigrateRepoOptions",
    "Milestone",
    "MoveProjectColumnsOption",
    "MoveProjectIssueOption",
    "NewIssuePinsAllowed",
    "Note",
    "NotificationCount",
    "NotificationSubject",
    "NotificationThread",
    "OAuth2Application",
    "ObjectFormatName",
    "Organization",
    "OrganizationPermissions",
    "PRBranchInfo",
    "Package",
    "PackageFile",
    "PayloadCommit",
    "PayloadCommitVerification",
    "PayloadUser",
    "Permission",
    "Project",
    "ProjectColumn",
    "PublicKey",
    "PullRequest",
    "PullRequestMeta",
    "PullRequestMinimal",
    "PullRequestMinimalHead",
    "PullRequestMinimalHeadRepo",
    "PullReview",
    "PullReviewComment",
    "PullReviewRequestOptions",
    "PushMirror",
    "Reaction",
    "Reference",
    "Release",
    "RenameBranchRepoOption",
    "RenameOrgOption",
    "RenameUserOption",
    "RepoCollaboratorPermission",
    "RepoCommit",
    "RepoTopicOptions",
    "RepoTransfer",
    "RepoWritePermission",
    "Repository",
    "RepositoryMeta",
    "ReviewStateType",
    "RunDetails",
    "SearchResults",
    "Secret",
    "ServerVersion",
    "StateType",
    "StopWatch",
    "SubmitPullReviewOptions",
    "Tag",
    "TagProtection",
    "Team",
    "TeamSearchResults",
    "TeamVisibility",
    "TimelineComment",
    "TopicListResponse",
    "TopicName",
    "TopicResponse",
    "TrackedTime",
    "TransferRepoOption",
    "UpdateBranchProtectionPriories",
    "UpdateBranchRepoOption",
    "UpdateFileOptions",
    "UpdateRepoAvatarOption",
    "UpdateUserAvatarOption",
    "UpdateVariableOption",
    "User",
    "UserBadgeOption",
    "UserHeatmapData",
    "UserMeta",
    "UserSearchResults",
    "UserSettings",
    "UserSettingsOptions",
    "UserTypeString",
    "VisibilityString",
    "WatchInfo",
    "WikiCommit",
    "WikiCommitList",
    "WikiPage",
    "WikiPageMetaData",
]
