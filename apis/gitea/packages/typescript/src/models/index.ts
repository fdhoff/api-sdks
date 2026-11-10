// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface APIError {
  message?: string;
  url?: string;
}

export type AccessLevelName = 'none' | 'read' | 'write' | 'admin' | 'owner';

export interface AccessToken {
  created_at?: string;
  id?: number;
  last_used_at?: string;
  name?: string;
  scopes?: Array<string>;
  sha1?: string;
  token_last_eight?: string;
}

export interface ActionArtifact {
  archive_download_url?: string;
  created_at?: string;
  expired?: boolean;
  expires_at?: string;
  id?: number;
  name?: string;
  size_in_bytes?: number;
  updated_at?: string;
  url?: string;
  workflow_run?: ActionWorkflowRun;
}

export interface ActionArtifactsResponse {
  artifacts?: Array<ActionArtifact>;
  total_count?: number;
}

export interface ActionRunner {
  busy?: boolean;
  disabled?: boolean;
  ephemeral?: boolean;
  id?: number;
  labels?: Array<ActionRunnerLabel>;
  name?: string;
  status?: string;
}

export interface ActionRunnerLabel {
  id?: number;
  name?: string;
  type?: string;
}

export interface ActionRunnersResponse {
  runners?: Array<ActionRunner>;
  total_count?: number;
}

export interface ActionTask {
  created_at?: string;
  display_title?: string;
  event?: string;
  head_branch?: string;
  head_sha?: string;
  id?: number;
  name?: string;
  run_number?: number;
  run_started_at?: string;
  status?: string;
  updated_at?: string;
  url?: string;
  workflow_id?: string;
}

export interface ActionTaskResponse {
  total_count?: number;
  workflow_runs?: Array<ActionTask>;
}

export interface ActionVariable {
  data?: string;
  description?: string;
  name?: string;
  owner_id?: number;
  repo_id?: number;
}

export interface ActionWorkflow {
  badge_url?: string;
  created_at?: string;
  deleted_at?: string;
  html_url?: string;
  id?: string;
  name?: string;
  path?: string;
  state?: string;
  updated_at?: string;
  url?: string;
}

export interface ActionWorkflowJob {
  completed_at?: string;
  conclusion?: string;
  created_at?: string;
  head_branch?: string;
  head_sha?: string;
  html_url?: string;
  id?: number;
  labels?: Array<string>;
  name?: string;
  run_attempt?: number;
  run_id?: number;
  run_url?: string;
  runner_id?: number;
  runner_name?: string;
  started_at?: string;
  status?: string;
  steps?: Array<ActionWorkflowStep>;
  url?: string;
}

export interface ActionWorkflowJobsResponse {
  jobs?: Array<ActionWorkflowJob>;
  total_count?: number;
}

export interface ActionWorkflowResponse {
  total_count?: number;
  workflows?: Array<ActionWorkflow>;
}

export interface ActionWorkflowRun {
  actor?: User;
  artifacts_url?: string;
  cancel_url?: string;
  completed_at?: string;
  conclusion?: string;
  created_at?: string;
  display_title?: string;
  event?: string;
  head_branch?: string;
  head_repository?: Repository;
  head_sha?: string;
  html_url?: string;
  id?: number;
  jobs_url?: string;
  logs_url?: string;
  path?: string;
  previous_attempt_url?: string;
  pull_requests?: Array<PullRequestMinimal>;
  repository?: Repository;
  repository_id?: number;
  rerun_url?: string;
  run_attempt?: number;
  run_number?: number;
  started_at?: string;
  status?: string;
  trigger_actor?: User;
  updated_at?: string;
  url?: string;
}

export interface ActionWorkflowRunsResponse {
  total_count?: number;
  workflow_runs?: Array<ActionWorkflowRun>;
}

export interface ActionWorkflowStep {
  completed_at?: string;
  conclusion?: string;
  name?: string;
  number?: number;
  started_at?: string;
  status?: string;
}

export interface Activity {
  act_user?: User;
  act_user_id?: number;
  comment?: Comment;
  comment_id?: number;
  content?: string;
  created?: string;
  id?: number;
  is_private?: boolean;
  op_type?: ActivityOpTypeEnum;
  ref_name?: string;
  repo?: Repository;
  repo_id?: number;
  user_id?: number;
}

export type ActivityOpTypeEnum =
  | 'create_repo'
  | 'rename_repo'
  | 'star_repo'
  | 'watch_repo'
  | 'commit_repo'
  | 'create_issue'
  | 'create_pull_request'
  | 'transfer_repo'
  | 'push_tag'
  | 'comment_issue'
  | 'merge_pull_request'
  | 'close_issue'
  | 'reopen_issue'
  | 'close_pull_request'
  | 'reopen_pull_request'
  | 'delete_tag'
  | 'delete_branch'
  | 'mirror_sync_push'
  | 'mirror_sync_create'
  | 'mirror_sync_delete'
  | 'approve_pull_request'
  | 'reject_pull_request'
  | 'comment_pull'
  | 'publish_release'
  | 'pull_review_dismissed'
  | 'pull_request_ready_for_review'
  | 'auto_merge_pull_request';

export interface AddCollaboratorOption {
  permission?: RepoWritePermission;
}

export interface AddTimeOption {
  created?: string;
  time: number;
  user_name?: string;
}

export interface AnnotatedTag {
  message?: string;
  object?: AnnotatedTagObject;
  sha?: string;
  tag?: string;
  tagger?: CommitUser;
  url?: string;
  verification?: PayloadCommitVerification;
}

export interface AnnotatedTagObject {
  sha?: string;
  type?: string;
  url?: string;
}

export interface ApplyDiffPatchFileOptions {
  author?: Identity;
  branch?: string;
  committer?: Identity;
  content: string;
  dates?: CommitDateOptions;
  force_push?: boolean;
  message?: string;
  new_branch?: string;
  signoff?: boolean;
}

export interface Attachment {
  browser_download_url?: string;
  created_at?: string;
  download_count?: number;
  id?: number;
  name?: string;
  size?: number;
  uuid?: string;
}

export interface Badge {
  description?: string;
  id?: number;
  image_url?: string;
  slug?: string;
}

export interface Branch {
  commit?: PayloadCommit;
  effective_branch_protection_name?: string;
  enable_status_check?: boolean;
  name?: string;
  _protected?: boolean;
  required_approvals?: number;
  status_check_contexts?: Array<string>;
  user_can_merge?: boolean;
  user_can_push?: boolean;
}

export interface BranchProtection {
  approvals_whitelist_teams?: Array<string>;
  approvals_whitelist_username?: Array<string>;
  block_admin_merge_override?: boolean;
  block_on_codeowner_reviews?: boolean;
  block_on_official_review_requests?: boolean;
  block_on_outdated_branch?: boolean;
  block_on_rejected_reviews?: boolean;
  branch_name?: string;
  bypass_allowlist_teams?: Array<string>;
  bypass_allowlist_usernames?: Array<string>;
  created_at?: string;
  dismiss_stale_approvals?: boolean;
  enable_approvals_whitelist?: boolean;
  enable_bypass_allowlist?: boolean;
  enable_force_push?: boolean;
  enable_force_push_allowlist?: boolean;
  enable_merge_whitelist?: boolean;
  enable_push?: boolean;
  enable_push_whitelist?: boolean;
  enable_status_check?: boolean;
  force_push_allowlist_deploy_keys?: boolean;
  force_push_allowlist_teams?: Array<string>;
  force_push_allowlist_usernames?: Array<string>;
  ignore_stale_approvals?: boolean;
  merge_whitelist_teams?: Array<string>;
  merge_whitelist_usernames?: Array<string>;
  priority?: number;
  protected_file_patterns?: string;
  push_whitelist_deploy_keys?: boolean;
  push_whitelist_teams?: Array<string>;
  push_whitelist_usernames?: Array<string>;
  require_signed_commits?: boolean;
  required_approvals?: number;
  rule_name?: string;
  status_check_contexts?: Array<string>;
  unprotected_file_patterns?: string;
  updated_at?: string;
}

export interface ChangeFileOperation {
  content?: string;
  from_path?: string;
  operation: ChangeFileOperationOperationEnum;
  path: string;
  sha?: string;
}

export type ChangeFileOperationOperationEnum = 'create' | 'update' | 'upload' | 'rename' | 'delete';

export interface ChangeFilesOptions {
  author?: Identity;
  branch?: string;
  committer?: Identity;
  dates?: CommitDateOptions;
  files: Array<ChangeFileOperation>;
  force_push?: boolean;
  message?: string;
  new_branch?: string;
  signoff?: boolean;
}

export interface ChangedFile {
  additions?: number;
  changes?: number;
  contents_url?: string;
  deletions?: number;
  filename?: string;
  html_url?: string;
  previous_filename?: string;
  raw_url?: string;
  status?: string;
}

export interface CombinedStatus {
  commit_url?: string;
  repository?: Repository;
  sha?: string;
  state?: CommitStatusState;
  statuses?: Array<CommitStatus>;
  total_count?: number;
  url?: string;
}

export interface Comment {
  assets?: Array<Attachment>;
  body?: string;
  created_at?: string;
  html_url?: string;
  id?: number;
  issue_url?: string;
  original_author?: string;
  original_author_id?: number;
  pull_request_url?: string;
  updated_at?: string;
  user?: User;
}

export interface Commit {
  author?: User;
  commit?: RepoCommit;
  committer?: User;
  created?: string;
  files?: Array<CommitAffectedFiles>;
  html_url?: string;
  parents?: Array<CommitMeta>;
  sha?: string;
  stats?: CommitStats;
  url?: string;
}

export interface CommitAffectedFiles {
  filename?: string;
  status?: string;
}

export interface CommitDateOptions {
  author?: string;
  committer?: string;
}

export interface CommitMeta {
  created?: string;
  sha?: string;
  url?: string;
}

export interface CommitStats {
  additions?: number;
  deletions?: number;
  total?: number;
}

export interface CommitStatus {
  context?: string;
  created_at?: string;
  creator?: User;
  description?: string;
  id?: number;
  status?: CommitStatusState;
  target_url?: string;
  updated_at?: string;
  url?: string;
}

export type CommitStatusState = 'pending' | 'success' | 'error' | 'failure' | 'warning' | 'skipped';

export interface CommitUser {
  date?: string;
  email?: string;
  name?: string;
}

export interface Compare {
  commits?: Array<Commit>;
  total_commits?: number;
}

export interface ContentsExtResponse {
  dir_contents?: Array<ContentsResponse>;
  file_contents?: ContentsResponse;
}

export interface ContentsResponse {
  _links?: FileLinksResponse;
  content?: string;
  download_url?: string;
  encoding?: string;
  git_url?: string;
  html_url?: string;
  last_author_date?: string;
  last_commit_message?: string;
  last_commit_sha?: string;
  last_committer_date?: string;
  lfs_oid?: string;
  lfs_size?: number;
  mode?: string;
  name?: string;
  path?: string;
  sha?: string;
  size?: number;
  submodule_git_url?: string;
  target?: string;
  type?: string;
  url?: string;
}

export interface CreateAccessTokenOption {
  name: string;
  scopes?: Array<string>;
}

export interface CreateActionWorkflowDispatch {
  inputs?: { [key: string]: string };
  ref: string;
}

export interface CreateBranchProtectionOption {
  approvals_whitelist_teams?: Array<string>;
  approvals_whitelist_username?: Array<string>;
  block_admin_merge_override?: boolean;
  block_on_codeowner_reviews?: boolean;
  block_on_official_review_requests?: boolean;
  block_on_outdated_branch?: boolean;
  block_on_rejected_reviews?: boolean;
  branch_name?: string;
  bypass_allowlist_teams?: Array<string>;
  bypass_allowlist_usernames?: Array<string>;
  dismiss_stale_approvals?: boolean;
  enable_approvals_whitelist?: boolean;
  enable_bypass_allowlist?: boolean;
  enable_force_push?: boolean;
  enable_force_push_allowlist?: boolean;
  enable_merge_whitelist?: boolean;
  enable_push?: boolean;
  enable_push_whitelist?: boolean;
  enable_status_check?: boolean;
  force_push_allowlist_deploy_keys?: boolean;
  force_push_allowlist_teams?: Array<string>;
  force_push_allowlist_usernames?: Array<string>;
  ignore_stale_approvals?: boolean;
  merge_whitelist_teams?: Array<string>;
  merge_whitelist_usernames?: Array<string>;
  priority?: number;
  protected_file_patterns?: string;
  push_whitelist_deploy_keys?: boolean;
  push_whitelist_teams?: Array<string>;
  push_whitelist_usernames?: Array<string>;
  require_signed_commits?: boolean;
  required_approvals?: number;
  rule_name?: string;
  status_check_contexts?: Array<string>;
  unprotected_file_patterns?: string;
}

export interface CreateBranchRepoOption {
  new_branch_name: string;
  old_branch_name?: string;
  old_ref_name?: string;
}

export interface CreateDeployKeyTokenOption {
  read_only?: boolean;
  title: string;
}

export interface CreateEmailOption {
  emails?: Array<string>;
}

export interface CreateFileOptions {
  author?: Identity;
  branch?: string;
  committer?: Identity;
  content: string;
  dates?: CommitDateOptions;
  force_push?: boolean;
  message?: string;
  new_branch?: string;
  signoff?: boolean;
}

export interface CreateForkOption {
  name?: string;
  organization?: string;
}

export interface CreateGPGKeyOption {
  armored_public_key: string;
  armored_signature?: string;
}

export interface CreateHookOption {
  active?: boolean;
  authorization_header?: string;
  branch_filter?: string;
  config: { [key: string]: string };
  events?: Array<string>;
  name?: string;
  type: CreateHookOptionTypeEnum;
}

export type CreateHookOptionTypeEnum =
  'dingtalk' | 'discord' | 'gitea' | 'gogs' | 'msteams' | 'slack' | 'telegram' | 'feishu' | 'wechatwork' | 'packagist';

export interface CreateIssueCommentOption {
  body: string;
}

export interface CreateIssueOption {
  assignee?: string;
  assignees?: Array<string>;
  body?: string;
  closed?: boolean;
  due_date?: string;
  labels?: Array<number>;
  milestone?: number;
  projects?: Array<number>;
  ref?: string;
  title: string;
}

export interface CreateKeyOption {
  key: string;
  read_only?: boolean;
  title: string;
}

export interface CreateLabelOption {
  color: string;
  description?: string;
  exclusive?: boolean;
  is_archived?: boolean;
  name: string;
}

export interface CreateMilestoneOption {
  description?: string;
  due_on?: string;
  state?: StateType;
  title?: string;
}

export interface CreateOAuth2ApplicationOptions {
  confidential_client?: boolean;
  name?: string;
  redirect_uris?: Array<string>;
  skip_secondary_authorization?: boolean;
}

export interface CreateOrUpdateSecretOption {
  data: string;
  description?: string;
}

export interface CreateOrgOption {
  description?: string;
  email?: string;
  full_name?: string;
  location?: string;
  repo_admin_change_team_access?: boolean;
  username: string;
  visibility?: VisibilityString;
  website?: string;
}

export interface CreateProjectColumnOption {
  color?: string;
  title: string;
}

export interface CreateProjectOption {
  card_type?: string;
  description?: string;
  template_type?: string;
  title: string;
}

export interface CreatePullRequestOption {
  allow_maintainer_edit?: boolean;
  assignee?: string;
  assignees?: Array<string>;
  base?: string;
  body?: string;
  due_date?: string;
  head?: string;
  labels?: Array<number>;
  milestone?: number;
  reviewers?: Array<string>;
  team_reviewers?: Array<string>;
  title?: string;
}

export interface CreatePullReviewComment {
  body?: string;
  new_position?: number;
  old_position?: number;
  path?: string;
}

export interface CreatePullReviewCommentReplyOptions {
  body?: string;
}

export interface CreatePullReviewOptions {
  body?: string;
  comments?: Array<CreatePullReviewComment>;
  commit_id?: string;
  event?: ReviewStateType;
}

export interface CreatePushMirrorOption {
  interval?: string;
  remote_address?: string;
  remote_password?: string;
  remote_username?: string;
  sync_on_commit?: boolean;
}

export interface CreateReleaseOption {
  body?: string;
  draft?: boolean;
  name?: string;
  prerelease?: boolean;
  tag_message?: string;
  tag_name: string;
  target_commitish?: string;
}

export interface CreateRepoOption {
  auto_init?: boolean;
  default_branch?: string;
  description?: string;
  gitignores?: string;
  issue_labels?: string;
  license?: string;
  name: string;
  object_format_name?: ObjectFormatName;
  _private?: boolean;
  readme?: string;
  template?: boolean;
  trust_model?: CreateRepoOptionTrustModelEnum;
}

export type CreateRepoOptionTrustModelEnum = 'default' | 'collaborator' | 'committer' | 'collaboratorcommitter';

export interface CreateStatusOption {
  context?: string;
  description?: string;
  state?: CommitStatusState;
  target_url?: string;
}

export interface CreateTagOption {
  message?: string;
  tag_name: string;
  target?: string;
}

export interface CreateTagProtectionOption {
  name_pattern?: string;
  whitelist_teams?: Array<string>;
  whitelist_usernames?: Array<string>;
}

export interface CreateTeamOption {
  can_create_org_repo?: boolean;
  description?: string;
  includes_all_repositories?: boolean;
  name: string;
  permission?: RepoWritePermission;
  units?: Array<string>;
  units_map?: { [key: string]: string };
  visibility?: TeamVisibility;
}

export interface CreateUserOption {
  created_at?: string;
  email: string;
  full_name?: string;
  login_name?: string;
  must_change_password?: boolean;
  password?: string;
  restricted?: boolean;
  send_notify?: boolean;
  source_id?: number;
  username: string;
  visibility?: VisibilityString;
}

export interface CreateVariableOption {
  description?: string;
  value: string;
}

export interface CreateWikiPageOptions {
  content_base64?: string;
  message?: string;
  title?: string;
}

export interface Cron {
  exec_times?: number;
  name?: string;
  next?: string;
  prev?: string;
  schedule?: string;
}

export interface CurrentAccessToken {
  created_at?: string;
  id?: number;
  last_used_at?: string;
  name?: string;
  scopes?: Array<string>;
  user?: UserMeta;
}

export interface DeleteEmailOption {
  emails?: Array<string>;
}

export interface DeleteFileOptions {
  author?: Identity;
  branch?: string;
  committer?: Identity;
  dates?: CommitDateOptions;
  force_push?: boolean;
  message?: string;
  new_branch?: string;
  sha: string;
  signoff?: boolean;
}

export interface DeployKey {
  created_at?: string;
  fingerprint?: string;
  id?: number;
  key?: string;
  key_id?: number;
  key_type?: DeployKeyKeyTypeEnum;
  read_only?: boolean;
  repository?: Repository;
  title?: string;
  token?: string;
  url?: string;
}

export type DeployKeyKeyTypeEnum = 'ssh' | 'token';

export interface DismissPullReviewOptions {
  message?: string;
  priors?: boolean;
}

export interface EditActionRunnerOption {
  disabled: boolean;
}

export interface EditAttachmentOptions {
  name?: string;
}

export interface EditBranchProtectionOption {
  approvals_whitelist_teams?: Array<string>;
  approvals_whitelist_username?: Array<string>;
  block_admin_merge_override?: boolean;
  block_on_codeowner_reviews?: boolean;
  block_on_official_review_requests?: boolean;
  block_on_outdated_branch?: boolean;
  block_on_rejected_reviews?: boolean;
  bypass_allowlist_teams?: Array<string>;
  bypass_allowlist_usernames?: Array<string>;
  dismiss_stale_approvals?: boolean;
  enable_approvals_whitelist?: boolean;
  enable_bypass_allowlist?: boolean;
  enable_force_push?: boolean;
  enable_force_push_allowlist?: boolean;
  enable_merge_whitelist?: boolean;
  enable_push?: boolean;
  enable_push_whitelist?: boolean;
  enable_status_check?: boolean;
  force_push_allowlist_deploy_keys?: boolean;
  force_push_allowlist_teams?: Array<string>;
  force_push_allowlist_usernames?: Array<string>;
  ignore_stale_approvals?: boolean;
  merge_whitelist_teams?: Array<string>;
  merge_whitelist_usernames?: Array<string>;
  priority?: number;
  protected_file_patterns?: string;
  push_whitelist_deploy_keys?: boolean;
  push_whitelist_teams?: Array<string>;
  push_whitelist_usernames?: Array<string>;
  require_signed_commits?: boolean;
  required_approvals?: number;
  status_check_contexts?: Array<string>;
  unprotected_file_patterns?: string;
}

export interface EditDeadlineOption {
  due_date: string;
}

export interface EditGitHookOption {
  content?: string;
}

export interface EditHookOption {
  active?: boolean;
  authorization_header?: string;
  branch_filter?: string;
  config?: { [key: string]: string };
  events?: Array<string>;
  name?: string;
}

export interface EditIssueCommentOption {
  body: string;
}

export interface EditIssueOption {
  assignee?: string;
  assignees?: Array<string>;
  body?: string;
  content_version?: number;
  due_date?: string;
  milestone?: number;
  projects?: Array<number>;
  ref?: string;
  state?: string;
  title?: string;
  unset_due_date?: boolean;
}

export interface EditLabelOption {
  color?: string;
  description?: string;
  exclusive?: boolean;
  is_archived?: boolean;
  name?: string;
}

export interface EditMilestoneOption {
  description?: string;
  due_on?: string;
  state?: StateType;
  title?: string;
}

export interface EditOrgOption {
  description?: string;
  email?: string;
  full_name?: string;
  location?: string;
  repo_admin_change_team_access?: boolean;
  visibility?: VisibilityString;
  website?: string;
}

export interface EditProjectColumnOption {
  color?: string;
  sorting?: number;
  title?: string;
}

export interface EditProjectOption {
  card_type?: string;
  description?: string;
  state?: StateType;
  title?: string;
}

export interface EditPullRequestOption {
  allow_maintainer_edit?: boolean;
  assignee?: string;
  assignees?: Array<string>;
  base?: string;
  body?: string;
  content_version?: number;
  due_date?: string;
  labels?: Array<number>;
  milestone?: number;
  state?: string;
  title?: string;
  unset_due_date?: boolean;
}

export interface EditReactionOption {
  content?: string;
}

export interface EditReleaseOption {
  body?: string;
  draft?: boolean;
  name?: string;
  prerelease?: boolean;
  tag_name?: string;
  target_commitish?: string;
}

export interface EditRepoOption {
  allow_fast_forward_only_merge?: boolean;
  allow_manual_merge?: boolean;
  allow_merge_commits?: boolean;
  allow_merge_update?: boolean;
  allow_rebase?: boolean;
  allow_rebase_explicit?: boolean;
  allow_rebase_update?: boolean;
  allow_squash_merge?: boolean;
  archived?: boolean;
  autodetect_manual_merge?: boolean;
  default_allow_maintainer_edit?: boolean;
  default_branch?: string;
  default_delete_branch_after_merge?: boolean;
  default_merge_style?: string;
  default_update_style?: string;
  description?: string;
  enable_prune?: boolean;
  external_tracker?: ExternalTracker;
  external_wiki?: ExternalWiki;
  has_actions?: boolean;
  has_code?: boolean;
  has_issues?: boolean;
  has_packages?: boolean;
  has_projects?: boolean;
  has_pull_requests?: boolean;
  has_releases?: boolean;
  has_wiki?: boolean;
  ignore_whitespace_conflicts?: boolean;
  internal_tracker?: InternalTracker;
  mirror_interval?: string;
  mirror_password?: string;
  mirror_token?: string;
  mirror_username?: string;
  name?: string;
  _private?: boolean;
  projects_mode?: string;
  template?: boolean;
  website?: string;
}

export interface EditTagProtectionOption {
  name_pattern?: string;
  whitelist_teams?: Array<string>;
  whitelist_usernames?: Array<string>;
}

export interface EditTeamOption {
  can_create_org_repo?: boolean;
  description?: string;
  includes_all_repositories?: boolean;
  name: string;
  permission?: RepoWritePermission;
  units?: Array<string>;
  units_map?: { [key: string]: string };
  visibility?: TeamVisibility;
}

export interface EditUserOption {
  active?: boolean;
  admin?: boolean;
  allow_create_organization?: boolean;
  allow_git_hook?: boolean;
  allow_import_local?: boolean;
  description?: string;
  email?: string;
  full_name?: string;
  location?: string;
  login_name?: string;
  max_repo_creation?: number;
  must_change_password?: boolean;
  password?: string;
  prohibit_login?: boolean;
  restricted?: boolean;
  source_id: number;
  type?: UserTypeString;
  visibility?: VisibilityString;
  website?: string;
}

export interface Email {
  email?: string;
  primary?: boolean;
  user_id?: number;
  username?: string;
  verified?: boolean;
}

export interface ExternalTracker {
  external_tracker_format?: string;
  external_tracker_regexp_pattern?: string;
  external_tracker_style?: string;
  external_tracker_url?: string;
}

export interface ExternalWiki {
  external_wiki_url?: string;
}

export interface FileCommitResponse {
  author?: CommitUser;
  committer?: CommitUser;
  created?: string;
  html_url?: string;
  message?: string;
  parents?: Array<CommitMeta>;
  sha?: string;
  tree?: CommitMeta;
  url?: string;
}

export interface FileDeleteResponse {
  commit?: FileCommitResponse;
  content?: any | null;
  verification?: PayloadCommitVerification;
}

export interface FileLinksResponse {
  git?: string;
  html?: string;
  self?: string;
}

export interface FileResponse {
  commit?: FileCommitResponse;
  content?: ContentsResponse;
  verification?: PayloadCommitVerification;
}

export interface FilesResponse {
  commit?: FileCommitResponse;
  files?: Array<ContentsResponse>;
  verification?: PayloadCommitVerification;
}

export interface GPGKey {
  can_certify?: boolean;
  can_encrypt_comms?: boolean;
  can_encrypt_storage?: boolean;
  can_sign?: boolean;
  created_at?: string;
  emails?: Array<GPGKeyEmail>;
  expires_at?: string;
  id?: number;
  key_id?: string;
  primary_key_id?: string;
  public_key?: string;
  subkeys?: Array<GPGKey>;
  verified?: boolean;
}

export interface GPGKeyEmail {
  email?: string;
  verified?: boolean;
}

export interface GeneralAPISettings {
  default_git_trees_per_page?: number;
  default_max_blob_size?: number;
  default_max_response_size?: number;
  default_paging_num?: number;
  max_response_items?: number;
}

export interface GeneralAttachmentSettings {
  allowed_types?: string;
  enabled?: boolean;
  max_files?: number;
  max_size?: number;
}

export interface GeneralRepoSettings {
  http_git_disabled?: boolean;
  lfs_disabled?: boolean;
  migrations_disabled?: boolean;
  mirrors_disabled?: boolean;
  stars_disabled?: boolean;
  time_tracking_disabled?: boolean;
}

export interface GeneralUISettings {
  allowed_reactions?: Array<string>;
  custom_emojis?: Array<string>;
  default_theme?: string;
}

export interface GenerateRepoOption {
  avatar?: boolean;
  default_branch?: string;
  description?: string;
  git_content?: boolean;
  git_hooks?: boolean;
  labels?: boolean;
  name: string;
  owner: string;
  _private?: boolean;
  protected_branch?: boolean;
  topics?: boolean;
  webhooks?: boolean;
}

export interface GetFilesOptions {
  files?: Array<string>;
}

export interface GitBlobResponse {
  content?: string;
  encoding?: string;
  lfs_oid?: string;
  lfs_size?: number;
  sha?: string;
  size?: number;
  url?: string;
}

export interface GitEntry {
  mode?: string;
  path?: string;
  sha?: string;
  size?: number;
  type?: string;
  url?: string;
}

export interface GitHook {
  content?: string;
  is_active?: boolean;
  name?: string;
}

export interface GitObject {
  sha?: string;
  type?: string;
  url?: string;
}

export interface GitTreeResponse {
  page?: number;
  sha?: string;
  total_count?: number;
  tree?: Array<GitEntry>;
  truncated?: boolean;
  url?: string;
}

export interface GitignoreTemplateInfo {
  name?: string;
  source?: string;
}

export interface Hook {
  active?: boolean;
  authorization_header?: string;
  branch_filter?: string;
  config?: { [key: string]: string };
  created_at?: string;
  events?: Array<string>;
  id?: number;
  name?: string;
  type?: string;
  updated_at?: string;
}

export interface Identity {
  email?: string;
  name?: string;
}

export interface InternalTracker {
  allow_only_contributors_to_track_time?: boolean;
  enable_issue_dependencies?: boolean;
  enable_time_tracker?: boolean;
}

export interface Issue {
  assets?: Array<Attachment>;
  assignee?: User;
  assignees?: Array<User>;
  body?: string;
  closed_at?: string;
  comments?: number;
  content_version?: number;
  created_at?: string;
  due_date?: string;
  html_url?: string;
  id?: number;
  is_locked?: boolean;
  labels?: Array<Label>;
  milestone?: Milestone;
  number?: number;
  original_author?: string;
  original_author_id?: number;
  pin_order?: number;
  projects?: Array<Project>;
  pull_request?: PullRequestMeta;
  ref?: string;
  repository?: RepositoryMeta;
  state?: StateType;
  time_estimate?: number;
  title?: string;
  updated_at?: string;
  url?: string;
  user?: User;
}

export interface IssueAssigneesOption {
  assignees?: Array<string>;
}

export interface IssueConfig {
  blank_issues_enabled?: boolean;
  contact_links?: Array<IssueConfigContactLink>;
}

export interface IssueConfigContactLink {
  about?: string;
  name?: string;
  url?: string;
}

export interface IssueConfigValidation {
  message?: string;
  valid?: boolean;
}

export interface IssueDeadline {
  due_date?: string;
}

export interface IssueFormField {
  attributes?: { [key: string]: any };
  id?: string;
  type?: IssueFormFieldTypeEnum;
  validations?: { [key: string]: any };
  visible?: Array<IssueFormFieldVisibleEnum>;
}

export type IssueFormFieldTypeEnum = 'markdown' | 'textarea' | 'input' | 'dropdown' | 'checkboxes';

export type IssueFormFieldVisibleEnum = 'form' | 'content';

export interface IssueLabelsOption {
  labels?: Array<any>;
}

export interface IssueMeta {
  index?: number;
  owner?: string;
  repo?: string;
}

export interface IssueTemplate {
  about?: string;
  assignees?: Array<string>;
  body?: Array<IssueFormField>;
  content?: string;
  file_name?: string;
  labels?: Array<string>;
  name?: string;
  ref?: string;
  title?: string;
}

export interface Label {
  color?: string;
  description?: string;
  exclusive?: boolean;
  id?: number;
  is_archived?: boolean;
  name?: string;
  url?: string;
}

export interface LabelTemplate {
  color?: string;
  description?: string;
  exclusive?: boolean;
  name?: string;
}

export interface LicenseTemplateInfo {
  body?: string;
  implementation?: string;
  key?: string;
  name?: string;
  url?: string;
}

export interface LicensesTemplateListEntry {
  key?: string;
  name?: string;
  url?: string;
}

export interface LockIssueOption {
  lock_reason?: string;
}

export interface MarkdownOption {
  Context?: string;
  Mode?: string;
  Text?: string;
  Wiki?: boolean;
}

export interface MarkupOption {
  Context?: string;
  FilePath?: string;
  Mode?: string;
  Text?: string;
  Wiki?: boolean;
}

export interface MergePullRequestOption {
  delete_branch_after_merge?: boolean;
  _do: MergePullRequestOptionDoEnum;
  force_merge?: boolean;
  head_commit_id?: string;
  merge_commit_id?: string;
  merge_message_field?: string;
  merge_title_field?: string;
  merge_when_checks_succeed?: boolean;
}

export type MergePullRequestOptionDoEnum =
  'merge' | 'rebase' | 'rebase-merge' | 'squash' | 'fast-forward-only' | 'manually-merged';

export interface MergeUpstreamRequest {
  branch?: string;
  ff_only?: boolean;
}

export interface MergeUpstreamResponse {
  merge_type?: string;
}

export interface MigrateRepoOptions {
  auth_password?: string;
  auth_token?: string;
  auth_username?: string;
  aws_access_key_id?: string;
  aws_secret_access_key?: string;
  clone_addr: string;
  description?: string;
  issues?: boolean;
  labels?: boolean;
  lfs?: boolean;
  lfs_endpoint?: string;
  milestones?: boolean;
  mirror?: boolean;
  mirror_interval?: string;
  _private?: boolean;
  pull_requests?: boolean;
  releases?: boolean;
  repo_name: string;
  repo_owner?: string;
  service?: MigrateRepoOptionsServiceEnum;
  uid?: number;
  wiki?: boolean;
}

export type MigrateRepoOptionsServiceEnum =
  'git' | 'github' | 'gitea' | 'gitlab' | 'gogs' | 'onedev' | 'gitbucket' | 'codebase' | 'codecommit';

export interface Milestone {
  closed_at?: string;
  closed_issues?: number;
  created_at?: string;
  description?: string;
  due_on?: string;
  id?: number;
  open_issues?: number;
  state?: StateType;
  title?: string;
  updated_at?: string;
}

export interface MoveProjectColumnsOption {
  column_ids: Array<number>;
}

export interface MoveProjectIssueOption {
  column_id: number;
  sorting?: number;
}

export interface NewIssuePinsAllowed {
  issues?: boolean;
  pull_requests?: boolean;
}

export interface Note {
  commit?: Commit;
  message?: string;
}

export interface NotificationCount {
  _new?: number;
}

export interface NotificationSubject {
  html_url?: string;
  latest_comment_html_url?: string;
  latest_comment_url?: string;
  state?: NotificationSubjectStateEnum;
  title?: string;
  type?: NotificationSubjectTypeEnum;
  url?: string;
}

export type NotificationSubjectStateEnum = 'open' | 'closed' | 'merged';

export type NotificationSubjectTypeEnum = 'Issue' | 'Pull' | 'Commit' | 'Repository';

export interface NotificationThread {
  id?: number;
  pinned?: boolean;
  repository?: Repository;
  subject?: NotificationSubject;
  unread?: boolean;
  updated_at?: string;
  url?: string;
}

export interface OAuth2Application {
  client_id?: string;
  client_secret?: string;
  confidential_client?: boolean;
  created?: string;
  id?: number;
  name?: string;
  redirect_uris?: Array<string>;
  skip_secondary_authorization?: boolean;
}

export type ObjectFormatName = 'sha1' | 'sha256';

export interface Organization {
  avatar_url?: string;
  description?: string;
  email?: string;
  full_name?: string;
  id?: number;
  location?: string;
  name?: string;
  repo_admin_change_team_access?: boolean;
  username?: string;
  visibility?: VisibilityString;
  website?: string;
}

export interface OrganizationPermissions {
  can_create_repository?: boolean;
  can_read?: boolean;
  can_write?: boolean;
  is_admin?: boolean;
  is_owner?: boolean;
}

export interface PRBranchInfo {
  label?: string;
  ref?: string;
  repo?: Repository;
  repo_id?: number;
  sha?: string;
}

export interface Package {
  created_at?: string;
  creator?: User;
  html_url?: string;
  id?: number;
  name?: string;
  owner?: User;
  repository?: Repository;
  type?: string;
  version?: string;
}

export interface PackageFile {
  id?: number;
  md5?: string;
  name?: string;
  sha1?: string;
  sha256?: string;
  sha512?: string;
  size?: number;
}

export interface PayloadCommit {
  added?: Array<string>;
  author?: PayloadUser;
  committer?: PayloadUser;
  id?: string;
  message?: string;
  modified?: Array<string>;
  removed?: Array<string>;
  timestamp?: string;
  url?: string;
  verification?: PayloadCommitVerification;
}

export interface PayloadCommitVerification {
  payload?: string;
  reason?: string;
  signature?: string;
  signer?: PayloadUser;
  verified?: boolean;
}

export interface PayloadUser {
  email?: string;
  name?: string;
  username?: string;
}

export interface Permission {
  admin?: boolean;
  pull?: boolean;
  push?: boolean;
}

export interface Project {
  card_type?: string;
  closed_at?: string;
  created_at?: string;
  creator?: User;
  creator_id?: number;
  description?: string;
  html_url?: string;
  id?: number;
  is_closed?: boolean;
  num_closed_issues?: number;
  num_issues?: number;
  num_open_issues?: number;
  owner_id?: number;
  repo_id?: number;
  state?: StateType;
  template_type?: string;
  title?: string;
  type?: string;
  updated_at?: string;
}

export interface ProjectColumn {
  color?: string;
  created_at?: string;
  creator?: User;
  _default?: boolean;
  id?: number;
  project_id?: number;
  sorting?: number;
  title?: string;
  updated_at?: string;
}

export interface PublicKey {
  created_at?: string;
  fingerprint?: string;
  id?: number;
  key?: string;
  key_type?: string;
  last_used_at?: string;
  read_only?: boolean;
  title?: string;
  url?: string;
  user?: User;
}

export interface PullRequest {
  additions?: number;
  allow_maintainer_edit?: boolean;
  assignee?: User;
  assignees?: Array<User>;
  base?: PRBranchInfo;
  body?: string;
  changed_files?: number;
  closed_at?: string;
  comments?: number;
  content_version?: number;
  created_at?: string;
  deletions?: number;
  diff_url?: string;
  draft?: boolean;
  due_date?: string;
  head?: PRBranchInfo;
  html_url?: string;
  id?: number;
  is_locked?: boolean;
  labels?: Array<Label>;
  merge_base?: string;
  merge_commit_sha?: string;
  mergeable?: boolean;
  merged?: boolean;
  merged_at?: string;
  merged_by?: User;
  milestone?: Milestone;
  number?: number;
  patch_url?: string;
  pin_order?: number;
  requested_reviewers?: Array<User>;
  requested_reviewers_teams?: Array<Team>;
  review_comments?: number;
  state?: StateType;
  title?: string;
  updated_at?: string;
  url?: string;
  user?: User;
}

export interface PullRequestMeta {
  draft?: boolean;
  html_url?: string;
  merged?: boolean;
  merged_at?: string;
}

export interface PullRequestMinimal {
  base?: PullRequestMinimalHead;
  head?: PullRequestMinimalHead;
  id?: number;
  number?: number;
  url?: string;
}

export interface PullRequestMinimalHead {
  ref?: string;
  repo?: PullRequestMinimalHeadRepo;
  sha?: string;
}

export interface PullRequestMinimalHeadRepo {
  id?: number;
  name?: string;
  url?: string;
}

export interface PullReview {
  body?: string;
  comments_count?: number;
  commit_id?: string;
  dismissed?: boolean;
  html_url?: string;
  id?: number;
  official?: boolean;
  pull_request_url?: string;
  stale?: boolean;
  state?: ReviewStateType;
  submitted_at?: string;
  team?: Team;
  updated_at?: string;
  user?: User;
}

export interface PullReviewComment {
  body?: string;
  commit_id?: string;
  created_at?: string;
  diff_hunk?: string;
  html_url?: string;
  id?: number;
  original_commit_id?: string;
  original_position?: number;
  path?: string;
  position?: number;
  pull_request_review_id?: number;
  pull_request_url?: string;
  resolver?: User;
  updated_at?: string;
  user?: User;
}

export interface PullReviewRequestOptions {
  reviewers?: Array<string>;
  team_reviewers?: Array<string>;
}

export interface PushMirror {
  created?: string;
  interval?: string;
  last_error?: string;
  last_update?: string;
  remote_address?: string;
  remote_name?: string;
  repo_name?: string;
  sync_on_commit?: boolean;
}

export interface Reaction {
  content?: string;
  created_at?: string;
  user?: User;
}

export interface Reference {
  object?: GitObject;
  ref?: string;
  url?: string;
}

export interface Release {
  assets?: Array<Attachment>;
  author?: User;
  body?: string;
  created_at?: string;
  draft?: boolean;
  html_url?: string;
  id?: number;
  name?: string;
  prerelease?: boolean;
  published_at?: string;
  tag_name?: string;
  tarball_url?: string;
  target_commitish?: string;
  upload_url?: string;
  url?: string;
  zipball_url?: string;
}

export interface RenameBranchRepoOption {
  name: string;
}

export interface RenameOrgOption {
  new_name: string;
}

export interface RenameUserOption {
  new_username: string;
}

export interface RepoCollaboratorPermission {
  permission?: AccessLevelName;
  role_name?: string;
  user?: User;
}

export interface RepoCommit {
  author?: CommitUser;
  committer?: CommitUser;
  message?: string;
  tree?: CommitMeta;
  url?: string;
  verification?: PayloadCommitVerification;
}

export interface RepoTopicOptions {
  topics?: Array<string>;
}

export interface RepoTransfer {
  doer?: User;
  recipient?: User;
  teams?: Array<Team>;
}

export type RepoWritePermission = 'read' | 'write' | 'admin';

export interface Repository {
  allow_fast_forward_only_merge?: boolean;
  allow_manual_merge?: boolean;
  allow_merge_commits?: boolean;
  allow_merge_update?: boolean;
  allow_rebase?: boolean;
  allow_rebase_explicit?: boolean;
  allow_rebase_update?: boolean;
  allow_squash_merge?: boolean;
  archived?: boolean;
  archived_at?: string;
  autodetect_manual_merge?: boolean;
  avatar_url?: string;
  branch_count?: number;
  clone_url?: string;
  created_at?: string;
  default_allow_maintainer_edit?: boolean;
  default_branch?: string;
  default_delete_branch_after_merge?: boolean;
  default_merge_style?: string;
  default_target_branch?: string;
  default_update_style?: string;
  description?: string;
  empty?: boolean;
  external_tracker?: ExternalTracker;
  external_wiki?: ExternalWiki;
  fork?: boolean;
  forks_count?: number;
  full_name?: string;
  has_actions?: boolean;
  has_code?: boolean;
  has_issues?: boolean;
  has_packages?: boolean;
  has_projects?: boolean;
  has_pull_requests?: boolean;
  has_releases?: boolean;
  has_wiki?: boolean;
  html_url?: string;
  id?: number;
  ignore_whitespace_conflicts?: boolean;
  internal?: boolean;
  internal_tracker?: InternalTracker;
  language?: string;
  languages_url?: string;
  licenses?: Array<string>;
  link?: string;
  mirror?: boolean;
  mirror_interval?: string;
  mirror_last_sync_at?: string;
  mirror_updated?: string;
  name?: string;
  object_format_name?: ObjectFormatName;
  open_issues_count?: number;
  open_pr_counter?: number;
  original_url?: string;
  owner?: User;
  parent?: Repository;
  permissions?: Permission;
  _private?: boolean;
  projects_mode?: string;
  release_counter?: number;
  repo_transfer?: RepoTransfer;
  size?: number;
  ssh_url?: string;
  stars_count?: number;
  template?: boolean;
  topics?: Array<string>;
  updated_at?: string;
  url?: string;
  watchers_count?: number;
  website?: string;
}

export interface RepositoryMeta {
  full_name?: string;
  id?: number;
  name?: string;
  owner?: string;
}

export type ReviewStateType = 'APPROVED' | 'PENDING' | 'COMMENT' | 'REQUEST_CHANGES' | 'REQUEST_REVIEW';

export interface RunDetails {
  html_url?: string;
  run_url?: string;
  workflow_run_id?: number;
}

export interface SearchResults {
  data?: Array<Repository>;
  ok?: boolean;
}

export interface Secret {
  created_at?: string;
  description?: string;
  name?: string;
}

export interface ServerVersion {
  version?: string;
}

export type StateType = 'open' | 'closed';

export interface StopWatch {
  created?: string;
  duration?: string;
  issue_index?: number;
  issue_title?: string;
  repo_name?: string;
  repo_owner_name?: string;
  seconds?: number;
}

export interface SubmitPullReviewOptions {
  body?: string;
  event?: ReviewStateType;
}

export interface Tag {
  commit?: CommitMeta;
  id?: string;
  message?: string;
  name?: string;
  tarball_url?: string;
  zipball_url?: string;
}

export interface TagProtection {
  created_at?: string;
  id?: number;
  name_pattern?: string;
  updated_at?: string;
  whitelist_teams?: Array<string>;
  whitelist_usernames?: Array<string>;
}

export interface Team {
  can_create_org_repo?: boolean;
  description?: string;
  id?: number;
  includes_all_repositories?: boolean;
  name?: string;
  organization?: Organization;
  permission?: AccessLevelName;
  units?: Array<string>;
  units_map?: { [key: string]: string };
  visibility?: TeamVisibility;
}

export interface TeamSearchResults {
  data?: Array<Team>;
  ok?: boolean;
}

export type TeamVisibility = 'public' | 'limited' | 'private';

export interface TimelineComment {
  assignee?: User;
  assignee_team?: Team;
  body?: string;
  created_at?: string;
  dependent_issue?: Issue;
  html_url?: string;
  id?: number;
  issue_url?: string;
  label?: Label;
  milestone?: Milestone;
  new_ref?: string;
  new_title?: string;
  old_milestone?: Milestone;
  old_project_id?: number;
  old_ref?: string;
  old_title?: string;
  project_id?: number;
  pull_request_url?: string;
  ref_action?: string;
  ref_comment?: Comment;
  ref_commit_sha?: string;
  ref_issue?: Issue;
  removed_assignee?: boolean;
  resolve_doer?: User;
  review_id?: number;
  tracked_time?: TrackedTime;
  type?: string;
  updated_at?: string;
  user?: User;
}

export interface TopicListResponse {
  topics?: Array<TopicResponse>;
}

export interface TopicName {
  topics?: Array<string>;
}

export interface TopicResponse {
  created?: string;
  id?: number;
  repo_count?: number;
  topic_name?: string;
  updated?: string;
}

export interface TrackedTime {
  created?: string;
  id?: number;
  issue?: Issue;
  issue_id?: number;
  time?: number;
  user_id?: number;
  user_name?: string;
}

export interface TransferRepoOption {
  new_owner: string;
  team_ids?: Array<number>;
}

export interface UpdateBranchProtectionPriories {
  ids?: Array<number>;
}

export interface UpdateBranchRepoOption {
  force?: boolean;
  new_commit_id: string;
  old_commit_id?: string;
}

export interface UpdateFileOptions {
  author?: Identity;
  branch?: string;
  committer?: Identity;
  content: string;
  dates?: CommitDateOptions;
  force_push?: boolean;
  from_path?: string;
  message?: string;
  new_branch?: string;
  sha?: string;
  signoff?: boolean;
}

export interface UpdateRepoAvatarOption {
  image?: string;
}

export interface UpdateUserAvatarOption {
  image?: string;
}

export interface UpdateVariableOption {
  description?: string;
  name?: string;
  value: string;
}

export interface User {
  active?: boolean;
  avatar_url?: string;
  created?: string;
  description?: string;
  email?: string;
  followers_count?: number;
  following_count?: number;
  full_name?: string;
  html_url?: string;
  id?: number;
  is_admin?: boolean;
  language?: string;
  last_login?: string;
  location?: string;
  login?: string;
  login_name?: string;
  prohibit_login?: boolean;
  restricted?: boolean;
  source_id?: number;
  starred_repos_count?: number;
  type?: UserTypeString;
  visibility?: VisibilityString;
  website?: string;
}

export interface UserBadgeOption {
  badge_slugs?: Array<string>;
}

export interface UserHeatmapData {
  contributions?: number;
  timestamp?: number;
}

export interface UserMeta {
  id?: number;
  login?: string;
}

export interface UserSearchResults {
  data?: Array<User>;
  ok?: boolean;
}

export interface UserSettings {
  description?: string;
  diff_view_style?: string;
  full_name?: string;
  hide_activity?: boolean;
  hide_email?: boolean;
  language?: string;
  location?: string;
  theme?: string;
  website?: string;
}

export interface UserSettingsOptions {
  description?: string;
  diff_view_style?: string;
  full_name?: string;
  hide_activity?: boolean;
  hide_email?: boolean;
  language?: string;
  location?: string;
  theme?: string;
  website?: string;
}

export type UserTypeString = 'User' | 'Organization' | 'Bot';

export type VisibilityString = 'public' | 'limited' | 'private';

export interface WatchInfo {
  created_at?: string;
  ignored?: boolean;
  reason?: any | null;
  repository_url?: string;
  subscribed?: boolean;
  url?: string;
}

export interface WikiCommit {
  author?: CommitUser;
  commiter?: CommitUser;
  message?: string;
  sha?: string;
}

export interface WikiCommitList {
  commits?: Array<WikiCommit>;
  count?: number;
}

export interface WikiPage {
  commit_count?: number;
  content_base64?: string;
  footer?: string;
  html_url?: string;
  last_commit?: WikiCommit;
  sidebar?: string;
  sub_url?: string;
  title?: string;
}

export interface WikiPageMetaData {
  html_url?: string;
  last_commit?: WikiCommit;
  sub_url?: string;
  title?: string;
}
