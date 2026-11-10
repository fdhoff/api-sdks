// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APIError, Package, PackageFile } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const deletePackage: Operation = {
  id: 'deletePackage',
  method: 'DELETE',
  path: '/packages/{owner}/{type}/{name}',
  resource: 'packages',
  name: 'delete',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

const deletePackageVersion: Operation = {
  id: 'deletePackageVersion',
  method: 'DELETE',
  path: '/packages/{owner}/{type}/{name}/{version}',
  resource: 'packages',
  name: 'deleteVersion',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
    { wire: 'version', name: 'version', location: 'path' },
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

const getLatestPackageVersion: Operation = {
  id: 'getLatestPackageVersion',
  method: 'GET',
  path: '/packages/{owner}/{type}/{name}/-/latest',
  resource: 'packages',
  name: 'getLatestVersion',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

const getPackage: Operation = {
  id: 'getPackage',
  method: 'GET',
  path: '/packages/{owner}/{type}/{name}/{version}',
  resource: 'packages',
  name: 'get',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
    { wire: 'version', name: 'version', location: 'path' },
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

const linkPackage: Operation = {
  id: 'linkPackage',
  method: 'POST',
  path: '/packages/{owner}/{type}/{name}/-/link/{repo_name}',
  resource: 'packages',
  name: 'link',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
    { wire: 'repo_name', name: 'repoName', location: 'path' },
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

const listPackageFiles: Operation = {
  id: 'listPackageFiles',
  method: 'GET',
  path: '/packages/{owner}/{type}/{name}/{version}/files',
  resource: 'packages',
  name: 'listFiles',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
    { wire: 'version', name: 'version', location: 'path' },
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

const listPackageVersions: Operation = {
  id: 'listPackageVersions',
  method: 'GET',
  path: '/packages/{owner}/{type}/{name}',
  resource: 'packages',
  name: 'listVersions',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterVersions',
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

const listPackages: Operation = {
  id: 'listPackages',
  method: 'GET',
  path: '/packages/{owner}',
  resource: 'packages',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
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

const unlinkPackage: Operation = {
  id: 'unlinkPackage',
  method: 'POST',
  path: '/packages/{owner}/{type}/{name}/-/unlink',
  resource: 'packages',
  name: 'unlink',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'type', name: 'type', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

export const OPERATIONS: readonly Operation[] = [
  deletePackage,
  deletePackageVersion,
  getLatestPackageVersion,
  getPackage,
  linkPackage,
  listPackageFiles,
  listPackageVersions,
  listPackages,
  unlinkPackage,
];

export class PackagesApi extends Resource {
  /** Delete a package and all its versions (deletePackage). */
  delete(owner: string, type: string, name: string, options?: RequestOptions): Promise<void> {
    return this.call(deletePackage, undefined, { owner, type, name }, options);
  }

  /** Delete a package version (deletePackageVersion). */
  deleteVersion(owner: string, type: string, name: string, version: string, options?: RequestOptions): Promise<void> {
    return this.call(deletePackageVersion, undefined, { owner, type, name, version }, options);
  }

  /** Get a package's latest version (getLatestPackageVersion). */
  getLatestVersion(owner: string, type: string, name: string, options?: RequestOptions): Promise<Package> {
    return this.call(getLatestPackageVersion, undefined, { owner, type, name }, options);
  }

  /** Get a package version (getPackage). */
  get(owner: string, type: string, name: string, version: string, options?: RequestOptions): Promise<Package> {
    return this.call(getPackage, undefined, { owner, type, name, version }, options);
  }

  /** Link a package to a repository (linkPackage). */
  link(owner: string, type: string, name: string, repoName: string, options?: RequestOptions): Promise<void> {
    return this.call(linkPackage, undefined, { owner, type, name, repoName }, options);
  }

  /** List a package version's files (listPackageFiles). */
  listFiles(
    owner: string,
    type: string,
    name: string,
    version: string,
    options?: RequestOptions,
  ): Promise<Array<PackageFile>> {
    return this.call(listPackageFiles, undefined, { owner, type, name, version }, options);
  }

  /** List one page of a package's versions (listPackageVersions). */
  listVersions(
    owner: string,
    type: string,
    name: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Package>> {
    return this.call(listPackageVersions, undefined, { owner, type, name, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterVersions(
    owner: string,
    type: string,
    name: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Package, void, undefined> {
    return this.paginate(listPackageVersions, undefined, { owner, type, name, ...params }, options);
  }

  /** List one page of an owner's packages (listPackages). */
  list(
    owner: string,
    params: {
      page?: number;
      limit?: number;
      type?:
        | 'alpine'
        | 'cargo'
        | 'chef'
        | 'composer'
        | 'conan'
        | 'conda'
        | 'container'
        | 'cran'
        | 'debian'
        | 'generic'
        | 'go'
        | 'helm'
        | 'maven'
        | 'npm'
        | 'nuget'
        | 'pub'
        | 'pypi'
        | 'rpm'
        | 'rubygems'
        | 'swift'
        | 'terraform'
        | 'vagrant';
      q?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<Package>> {
    return this.call(listPackages, undefined, { owner, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    params: {
      page?: number;
      limit?: number;
      type?:
        | 'alpine'
        | 'cargo'
        | 'chef'
        | 'composer'
        | 'conan'
        | 'conda'
        | 'container'
        | 'cran'
        | 'debian'
        | 'generic'
        | 'go'
        | 'helm'
        | 'maven'
        | 'npm'
        | 'nuget'
        | 'pub'
        | 'pypi'
        | 'rpm'
        | 'rubygems'
        | 'swift'
        | 'terraform'
        | 'vagrant';
      q?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Package, void, undefined> {
    return this.paginate(listPackages, undefined, { owner, ...params }, options);
  }

  /** Unlink a package from its repository (unlinkPackage). */
  unlink(owner: string, type: string, name: string, options?: RequestOptions): Promise<void> {
    return this.call(unlinkPackage, undefined, { owner, type, name }, options);
  }
}
