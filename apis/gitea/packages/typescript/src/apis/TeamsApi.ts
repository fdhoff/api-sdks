// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  Activity,
  CreateTeamOption,
  EditTeamOption,
  Repository,
  Team,
  TeamSearchResults,
  User,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const orgAddTeamMember: Operation = {
  id: 'orgAddTeamMember',
  method: 'PUT',
  path: '/teams/{id}/members/{username}',
  resource: 'teams',
  name: 'addMember',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgAddTeamRepository: Operation = {
  id: 'orgAddTeamRepository',
  method: 'PUT',
  path: '/teams/{id}/repos/{org}/{repo}',
  resource: 'teams',
  name: 'addRepo',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgCreateTeam: Operation = {
  id: 'orgCreateTeam',
  method: 'POST',
  path: '/orgs/{org}/teams',
  resource: 'teams',
  name: 'create',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgDeleteTeam: Operation = {
  id: 'orgDeleteTeam',
  method: 'DELETE',
  path: '/teams/{id}',
  resource: 'teams',
  name: 'delete',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgEditTeam: Operation = {
  id: 'orgEditTeam',
  method: 'PATCH',
  path: '/teams/{id}',
  resource: 'teams',
  name: 'update',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgGetTeam: Operation = {
  id: 'orgGetTeam',
  method: 'GET',
  path: '/teams/{id}',
  resource: 'teams',
  name: 'get',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgListTeamActivityFeeds: Operation = {
  id: 'orgListTeamActivityFeeds',
  method: 'GET',
  path: '/teams/{id}/activities/feeds',
  resource: 'teams',
  name: 'listActivityFeeds',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'date', name: 'date', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterActivityFeeds',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgListTeamMember: Operation = {
  id: 'orgListTeamMember',
  method: 'GET',
  path: '/teams/{id}/members/{username}',
  resource: 'teams',
  name: 'getMember',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgListTeamMembers: Operation = {
  id: 'orgListTeamMembers',
  method: 'GET',
  path: '/teams/{id}/members',
  resource: 'teams',
  name: 'listMembers',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterMembers',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgListTeamRepo: Operation = {
  id: 'orgListTeamRepo',
  method: 'GET',
  path: '/teams/{id}/repos/{org}/{repo}',
  resource: 'teams',
  name: 'getRepo',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgListTeamRepos: Operation = {
  id: 'orgListTeamRepos',
  method: 'GET',
  path: '/teams/{id}/repos',
  resource: 'teams',
  name: 'listRepos',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRepos',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgListTeams: Operation = {
  id: 'orgListTeams',
  method: 'GET',
  path: '/orgs/{org}/teams',
  resource: 'teams',
  name: 'list',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgRemoveTeamMember: Operation = {
  id: 'orgRemoveTeamMember',
  method: 'DELETE',
  path: '/teams/{id}/members/{username}',
  resource: 'teams',
  name: 'removeMember',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'username', name: 'username', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const orgRemoveTeamRepository: Operation = {
  id: 'orgRemoveTeamRepository',
  method: 'DELETE',
  path: '/teams/{id}/repos/{org}/{repo}',
  resource: 'teams',
  name: 'removeRepo',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const teamSearch: Operation = {
  id: 'teamSearch',
  method: 'GET',
  path: '/orgs/{org}/teams/search',
  resource: 'teams',
  name: 'search',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'include_desc', name: 'includeDesc', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSearch',
  paging: { style: 'link_header', items: 'data', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  orgAddTeamMember,
  orgAddTeamRepository,
  orgCreateTeam,
  orgDeleteTeam,
  orgEditTeam,
  orgGetTeam,
  orgListTeamActivityFeeds,
  orgListTeamMember,
  orgListTeamMembers,
  orgListTeamRepo,
  orgListTeamRepos,
  orgListTeams,
  orgRemoveTeamMember,
  orgRemoveTeamRepository,
  teamSearch,
];

export class TeamsApi extends Resource {
  /** Add a member to a team (orgAddTeamMember). */
  addMember(id: number, username: string, options?: RequestOptions): Promise<void> {
    return this.call(orgAddTeamMember, undefined, { id, username }, options);
  }

  /** Give a team access to a repository (orgAddTeamRepository). */
  addRepo(id: number, org: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(orgAddTeamRepository, undefined, { id, org, repo }, options);
  }

  /** Create a team (orgCreateTeam). */
  create(org: string, body?: CreateTeamOption, options?: RequestOptions): Promise<Team> {
    return this.call(orgCreateTeam, body, { org }, options);
  }

  /** Delete a team (orgDeleteTeam). */
  delete(id: number, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteTeam, undefined, { id }, options);
  }

  /** Change a team (orgEditTeam). */
  update(id: number, body?: EditTeamOption, options?: RequestOptions): Promise<Team> {
    return this.call(orgEditTeam, body, { id }, options);
  }

  /** Get a team (orgGetTeam). */
  get(id: number, options?: RequestOptions): Promise<Team> {
    return this.call(orgGetTeam, undefined, { id }, options);
  }

  /** List one page of a team's activity (orgListTeamActivityFeeds). */
  listActivityFeeds(
    id: number,
    params: { date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Activity>> {
    return this.call(orgListTeamActivityFeeds, undefined, { id, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterActivityFeeds(
    id: number,
    params: { date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Activity, void, undefined> {
    return this.paginate(orgListTeamActivityFeeds, undefined, { id, ...params }, options);
  }

  /** Get a member of a team (orgListTeamMember). */
  getMember(id: number, username: string, options?: RequestOptions): Promise<User> {
    return this.call(orgListTeamMember, undefined, { id, username }, options);
  }

  /** List one page of a team's members (orgListTeamMembers). */
  listMembers(
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(orgListTeamMembers, undefined, { id, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterMembers(
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(orgListTeamMembers, undefined, { id, ...params }, options);
  }

  /** Get a repository that a team has access to (orgListTeamRepo). */
  getRepo(id: number, org: string, repo: string, options?: RequestOptions): Promise<Repository> {
    return this.call(orgListTeamRepo, undefined, { id, org, repo }, options);
  }

  /** List one page of a team's repositories (orgListTeamRepos). */
  listRepos(
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Repository>> {
    return this.call(orgListTeamRepos, undefined, { id, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRepos(
    id: number,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(orgListTeamRepos, undefined, { id, ...params }, options);
  }

  /** List one page of an organization's teams (orgListTeams). */
  list(org: string, params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Team>> {
    return this.call(orgListTeams, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Team, void, undefined> {
    return this.paginate(orgListTeams, undefined, { org, ...params }, options);
  }

  /** Remove a member from a team (orgRemoveTeamMember). */
  removeMember(id: number, username: string, options?: RequestOptions): Promise<void> {
    return this.call(orgRemoveTeamMember, undefined, { id, username }, options);
  }

  /** Remove a team's access to a repository (orgRemoveTeamRepository). */
  removeRepo(id: number, org: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(orgRemoveTeamRepository, undefined, { id, org, repo }, options);
  }

  /** Get one page of an organization's teams that match a search (teamSearch). */
  search(
    org: string,
    params: { q?: string; includeDesc?: boolean; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<TeamSearchResults> {
    return this.call(teamSearch, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSearch(
    org: string,
    params: { q?: string; includeDesc?: boolean; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Team, void, undefined> {
    return this.paginate(teamSearch, undefined, { org, ...params }, options);
  }
}
