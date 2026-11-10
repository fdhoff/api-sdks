// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { ActionsApi, OPERATIONS as ActionsApiOperations } from './apis/ActionsApi.js';
import { AdminApi, OPERATIONS as AdminApiOperations } from './apis/AdminApi.js';
import { BranchesApi, OPERATIONS as BranchesApiOperations } from './apis/BranchesApi.js';
import { CommitsApi, OPERATIONS as CommitsApiOperations } from './apis/CommitsApi.js';
import { ContentsApi, OPERATIONS as ContentsApiOperations } from './apis/ContentsApi.js';
import { CurrentUserApi, OPERATIONS as CurrentUserApiOperations } from './apis/CurrentUserApi.js';
import { GitApi, OPERATIONS as GitApiOperations } from './apis/GitApi.js';
import { HooksApi, OPERATIONS as HooksApiOperations } from './apis/HooksApi.js';
import { IssuesApi, OPERATIONS as IssuesApiOperations } from './apis/IssuesApi.js';
import { LabelsApi, OPERATIONS as LabelsApiOperations } from './apis/LabelsApi.js';
import { MilestonesApi, OPERATIONS as MilestonesApiOperations } from './apis/MilestonesApi.js';
import { MiscApi, OPERATIONS as MiscApiOperations } from './apis/MiscApi.js';
import { NotificationsApi, OPERATIONS as NotificationsApiOperations } from './apis/NotificationsApi.js';
import { OrgsApi, OPERATIONS as OrgsApiOperations } from './apis/OrgsApi.js';
import { PackagesApi, OPERATIONS as PackagesApiOperations } from './apis/PackagesApi.js';
import { ProjectsApi, OPERATIONS as ProjectsApiOperations } from './apis/ProjectsApi.js';
import { PullsApi, OPERATIONS as PullsApiOperations } from './apis/PullsApi.js';
import { ReleasesApi, OPERATIONS as ReleasesApiOperations } from './apis/ReleasesApi.js';
import { ReposApi, OPERATIONS as ReposApiOperations } from './apis/ReposApi.js';
import { TagsApi, OPERATIONS as TagsApiOperations } from './apis/TagsApi.js';
import { TeamsApi, OPERATIONS as TeamsApiOperations } from './apis/TeamsApi.js';
import { UsersApi, OPERATIONS as UsersApiOperations } from './apis/UsersApi.js';
import { WikiApi, OPERATIONS as WikiApiOperations } from './apis/WikiApi.js';
import type { Operation, Transport } from './runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...ActionsApiOperations,
    ...AdminApiOperations,
    ...BranchesApiOperations,
    ...CommitsApiOperations,
    ...ContentsApiOperations,
    ...CurrentUserApiOperations,
    ...GitApiOperations,
    ...HooksApiOperations,
    ...IssuesApiOperations,
    ...LabelsApiOperations,
    ...MilestonesApiOperations,
    ...MiscApiOperations,
    ...NotificationsApiOperations,
    ...OrgsApiOperations,
    ...PackagesApiOperations,
    ...ProjectsApiOperations,
    ...PullsApiOperations,
    ...ReleasesApiOperations,
    ...ReposApiOperations,
    ...TagsApiOperations,
    ...TeamsApiOperations,
    ...UsersApiOperations,
    ...WikiApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly actions: ActionsApi;
  readonly admin: AdminApi;
  readonly branches: BranchesApi;
  readonly commits: CommitsApi;
  readonly contents: ContentsApi;
  readonly currentUser: CurrentUserApi;
  readonly git: GitApi;
  readonly hooks: HooksApi;
  readonly issues: IssuesApi;
  readonly labels: LabelsApi;
  readonly milestones: MilestonesApi;
  readonly misc: MiscApi;
  readonly notifications: NotificationsApi;
  readonly orgs: OrgsApi;
  readonly packages: PackagesApi;
  readonly projects: ProjectsApi;
  readonly pulls: PullsApi;
  readonly releases: ReleasesApi;
  readonly repos: ReposApi;
  readonly tags: TagsApi;
  readonly teams: TeamsApi;
  readonly users: UsersApi;
  readonly wiki: WikiApi;

  constructor(transport: Transport) {
    this.actions = new ActionsApi(transport);
    this.admin = new AdminApi(transport);
    this.branches = new BranchesApi(transport);
    this.commits = new CommitsApi(transport);
    this.contents = new ContentsApi(transport);
    this.currentUser = new CurrentUserApi(transport);
    this.git = new GitApi(transport);
    this.hooks = new HooksApi(transport);
    this.issues = new IssuesApi(transport);
    this.labels = new LabelsApi(transport);
    this.milestones = new MilestonesApi(transport);
    this.misc = new MiscApi(transport);
    this.notifications = new NotificationsApi(transport);
    this.orgs = new OrgsApi(transport);
    this.packages = new PackagesApi(transport);
    this.projects = new ProjectsApi(transport);
    this.pulls = new PullsApi(transport);
    this.releases = new ReleasesApi(transport);
    this.repos = new ReposApi(transport);
    this.tags = new TagsApi(transport);
    this.teams = new TeamsApi(transport);
    this.users = new UsersApi(transport);
    this.wiki = new WikiApi(transport);
  }
}
