// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  CreateEmailOption,
  CreateGPGKeyOption,
  CreateKeyOption,
  CreateOAuth2ApplicationOptions,
  CreateRepoOption,
  CurrentAccessToken,
  DeleteEmailOption,
  Email,
  GPGKey,
  OAuth2Application,
  Organization,
  PublicKey,
  Repository,
  StopWatch,
  Team,
  TrackedTime,
  UpdateUserAvatarOption,
  User,
  UserSettings,
  UserSettingsOptions,
  WatchInfo,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createCurrentUserRepo: Operation = {
  id: 'createCurrentUserRepo',
  method: 'POST',
  path: '/user/repos',
  resource: 'currentUser',
  name: 'createRepo',
  params: [],
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

const deleteCurrentToken: Operation = {
  id: 'deleteCurrentToken',
  method: 'DELETE',
  path: '/token',
  resource: 'currentUser',
  name: 'deleteToken',
  params: [],
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

const getCurrentToken: Operation = {
  id: 'getCurrentToken',
  method: 'GET',
  path: '/token',
  resource: 'currentUser',
  name: 'getToken',
  params: [],
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

const getUserSettings: Operation = {
  id: 'getUserSettings',
  method: 'GET',
  path: '/user/settings',
  resource: 'currentUser',
  name: 'getSettings',
  params: [],
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

const getVerificationToken: Operation = {
  id: 'getVerificationToken',
  method: 'GET',
  path: '/user/gpg_key_token',
  resource: 'currentUser',
  name: 'getGpgVerificationToken',
  params: [],
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

const orgListCurrentUserOrgs: Operation = {
  id: 'orgListCurrentUserOrgs',
  method: 'GET',
  path: '/user/orgs',
  resource: 'currentUser',
  name: 'listOrgs',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterOrgs',
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

const updateUserSettings: Operation = {
  id: 'updateUserSettings',
  method: 'PATCH',
  path: '/user/settings',
  resource: 'currentUser',
  name: 'updateSettings',
  params: [],
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

const userAddEmail: Operation = {
  id: 'userAddEmail',
  method: 'POST',
  path: '/user/emails',
  resource: 'currentUser',
  name: 'addEmails',
  params: [],
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

const userBlockUser: Operation = {
  id: 'userBlockUser',
  method: 'PUT',
  path: '/user/blocks/{username}',
  resource: 'currentUser',
  name: 'blockUser',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'note', name: 'note', location: 'query' },
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

const userCheckUserBlock: Operation = {
  id: 'userCheckUserBlock',
  method: 'GET',
  path: '/user/blocks/{username}',
  resource: 'currentUser',
  name: 'checkBlockedUser',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const userCreateOAuth2Application: Operation = {
  id: 'userCreateOAuth2Application',
  method: 'POST',
  path: '/user/applications/oauth2',
  resource: 'currentUser',
  name: 'createOauth2App',
  params: [],
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

const userCurrentCheckFollowing: Operation = {
  id: 'userCurrentCheckFollowing',
  method: 'GET',
  path: '/user/following/{username}',
  resource: 'currentUser',
  name: 'checkFollowing',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const userCurrentCheckStarring: Operation = {
  id: 'userCurrentCheckStarring',
  method: 'GET',
  path: '/user/starred/{owner}/{repo}',
  resource: 'currentUser',
  name: 'checkStarred',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
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

const userCurrentCheckSubscription: Operation = {
  id: 'userCurrentCheckSubscription',
  method: 'GET',
  path: '/repos/{owner}/{repo}/subscription',
  resource: 'currentUser',
  name: 'checkWatching',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
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

const userCurrentDeleteFollow: Operation = {
  id: 'userCurrentDeleteFollow',
  method: 'DELETE',
  path: '/user/following/{username}',
  resource: 'currentUser',
  name: 'unfollow',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const userCurrentDeleteGPGKey: Operation = {
  id: 'userCurrentDeleteGPGKey',
  method: 'DELETE',
  path: '/user/gpg_keys/{id}',
  resource: 'currentUser',
  name: 'deleteGpgKey',
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

const userCurrentDeleteKey: Operation = {
  id: 'userCurrentDeleteKey',
  method: 'DELETE',
  path: '/user/keys/{id}',
  resource: 'currentUser',
  name: 'deleteKey',
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

const userCurrentDeleteStar: Operation = {
  id: 'userCurrentDeleteStar',
  method: 'DELETE',
  path: '/user/starred/{owner}/{repo}',
  resource: 'currentUser',
  name: 'unstar',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
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

const userCurrentDeleteSubscription: Operation = {
  id: 'userCurrentDeleteSubscription',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/subscription',
  resource: 'currentUser',
  name: 'unwatch',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
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

const userCurrentGetGPGKey: Operation = {
  id: 'userCurrentGetGPGKey',
  method: 'GET',
  path: '/user/gpg_keys/{id}',
  resource: 'currentUser',
  name: 'getGpgKey',
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

const userCurrentGetKey: Operation = {
  id: 'userCurrentGetKey',
  method: 'GET',
  path: '/user/keys/{id}',
  resource: 'currentUser',
  name: 'getKey',
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

const userCurrentListFollowers: Operation = {
  id: 'userCurrentListFollowers',
  method: 'GET',
  path: '/user/followers',
  resource: 'currentUser',
  name: 'listFollowers',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFollowers',
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

const userCurrentListFollowing: Operation = {
  id: 'userCurrentListFollowing',
  method: 'GET',
  path: '/user/following',
  resource: 'currentUser',
  name: 'listFollowing',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFollowing',
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

const userCurrentListGPGKeys: Operation = {
  id: 'userCurrentListGPGKeys',
  method: 'GET',
  path: '/user/gpg_keys',
  resource: 'currentUser',
  name: 'listGpgKeys',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterGpgKeys',
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

const userCurrentListKeys: Operation = {
  id: 'userCurrentListKeys',
  method: 'GET',
  path: '/user/keys',
  resource: 'currentUser',
  name: 'listKeys',
  params: [
    { wire: 'fingerprint', name: 'fingerprint', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterKeys',
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

const userCurrentListRepos: Operation = {
  id: 'userCurrentListRepos',
  method: 'GET',
  path: '/user/repos',
  resource: 'currentUser',
  name: 'listRepos',
  params: [
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

const userCurrentListStarred: Operation = {
  id: 'userCurrentListStarred',
  method: 'GET',
  path: '/user/starred',
  resource: 'currentUser',
  name: 'listStarred',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStarred',
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

const userCurrentListSubscriptions: Operation = {
  id: 'userCurrentListSubscriptions',
  method: 'GET',
  path: '/user/subscriptions',
  resource: 'currentUser',
  name: 'listWatched',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterWatched',
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

const userCurrentPostGPGKey: Operation = {
  id: 'userCurrentPostGPGKey',
  method: 'POST',
  path: '/user/gpg_keys',
  resource: 'currentUser',
  name: 'addGpgKey',
  params: [],
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

const userCurrentPostKey: Operation = {
  id: 'userCurrentPostKey',
  method: 'POST',
  path: '/user/keys',
  resource: 'currentUser',
  name: 'addKey',
  params: [],
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

const userCurrentPutFollow: Operation = {
  id: 'userCurrentPutFollow',
  method: 'PUT',
  path: '/user/following/{username}',
  resource: 'currentUser',
  name: 'follow',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const userCurrentPutStar: Operation = {
  id: 'userCurrentPutStar',
  method: 'PUT',
  path: '/user/starred/{owner}/{repo}',
  resource: 'currentUser',
  name: 'star',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
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

const userCurrentPutSubscription: Operation = {
  id: 'userCurrentPutSubscription',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/subscription',
  resource: 'currentUser',
  name: 'watch',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
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

const userCurrentTrackedTimes: Operation = {
  id: 'userCurrentTrackedTimes',
  method: 'GET',
  path: '/user/times',
  resource: 'currentUser',
  name: 'listTrackedTimes',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTrackedTimes',
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

const userDeleteAvatar: Operation = {
  id: 'userDeleteAvatar',
  method: 'DELETE',
  path: '/user/avatar',
  resource: 'currentUser',
  name: 'deleteAvatar',
  params: [],
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

const userDeleteEmail: Operation = {
  id: 'userDeleteEmail',
  method: 'DELETE',
  path: '/user/emails',
  resource: 'currentUser',
  name: 'deleteEmails',
  params: [],
  hasBody: true,
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

const userDeleteOAuth2Application: Operation = {
  id: 'userDeleteOAuth2Application',
  method: 'DELETE',
  path: '/user/applications/oauth2/{id}',
  resource: 'currentUser',
  name: 'deleteOauth2App',
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

const userGetCurrent: Operation = {
  id: 'userGetCurrent',
  method: 'GET',
  path: '/user',
  resource: 'currentUser',
  name: 'get',
  params: [],
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

const userGetOAuth2Application: Operation = {
  id: 'userGetOAuth2Application',
  method: 'GET',
  path: '/user/applications/oauth2/{id}',
  resource: 'currentUser',
  name: 'getOauth2App',
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

const userGetOauth2Application: Operation = {
  id: 'userGetOauth2Application',
  method: 'GET',
  path: '/user/applications/oauth2',
  resource: 'currentUser',
  name: 'listOauth2Apps',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterOauth2Apps',
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

const userGetStopWatches: Operation = {
  id: 'userGetStopWatches',
  method: 'GET',
  path: '/user/stopwatches',
  resource: 'currentUser',
  name: 'listStopwatches',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStopwatches',
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

const userListBlocks: Operation = {
  id: 'userListBlocks',
  method: 'GET',
  path: '/user/blocks',
  resource: 'currentUser',
  name: 'listBlockedUsers',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterBlockedUsers',
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

const userListEmails: Operation = {
  id: 'userListEmails',
  method: 'GET',
  path: '/user/emails',
  resource: 'currentUser',
  name: 'listEmails',
  params: [],
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

const userListTeams: Operation = {
  id: 'userListTeams',
  method: 'GET',
  path: '/user/teams',
  resource: 'currentUser',
  name: 'listTeams',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTeams',
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

const userUnblockUser: Operation = {
  id: 'userUnblockUser',
  method: 'DELETE',
  path: '/user/blocks/{username}',
  resource: 'currentUser',
  name: 'unblockUser',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const userUpdateAvatar: Operation = {
  id: 'userUpdateAvatar',
  method: 'POST',
  path: '/user/avatar',
  resource: 'currentUser',
  name: 'updateAvatar',
  params: [],
  hasBody: true,
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

const userUpdateOAuth2Application: Operation = {
  id: 'userUpdateOAuth2Application',
  method: 'PATCH',
  path: '/user/applications/oauth2/{id}',
  resource: 'currentUser',
  name: 'updateOauth2App',
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

const userVerifyGPGKey: Operation = {
  id: 'userVerifyGPGKey',
  method: 'POST',
  path: '/user/gpg_key_verify',
  resource: 'currentUser',
  name: 'verifyGpgKey',
  params: [],
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

export const OPERATIONS: readonly Operation[] = [
  createCurrentUserRepo,
  deleteCurrentToken,
  getCurrentToken,
  getUserSettings,
  getVerificationToken,
  orgListCurrentUserOrgs,
  updateUserSettings,
  userAddEmail,
  userBlockUser,
  userCheckUserBlock,
  userCreateOAuth2Application,
  userCurrentCheckFollowing,
  userCurrentCheckStarring,
  userCurrentCheckSubscription,
  userCurrentDeleteFollow,
  userCurrentDeleteGPGKey,
  userCurrentDeleteKey,
  userCurrentDeleteStar,
  userCurrentDeleteSubscription,
  userCurrentGetGPGKey,
  userCurrentGetKey,
  userCurrentListFollowers,
  userCurrentListFollowing,
  userCurrentListGPGKeys,
  userCurrentListKeys,
  userCurrentListRepos,
  userCurrentListStarred,
  userCurrentListSubscriptions,
  userCurrentPostGPGKey,
  userCurrentPostKey,
  userCurrentPutFollow,
  userCurrentPutStar,
  userCurrentPutSubscription,
  userCurrentTrackedTimes,
  userDeleteAvatar,
  userDeleteEmail,
  userDeleteOAuth2Application,
  userGetCurrent,
  userGetOAuth2Application,
  userGetOauth2Application,
  userGetStopWatches,
  userListBlocks,
  userListEmails,
  userListTeams,
  userUnblockUser,
  userUpdateAvatar,
  userUpdateOAuth2Application,
  userVerifyGPGKey,
];

export class CurrentUserApi extends Resource {
  /** Create a repository of your own (createCurrentUserRepo). */
  createRepo(body?: CreateRepoOption, options?: RequestOptions): Promise<Repository> {
    return this.call(createCurrentUserRepo, body, {}, options);
  }

  /** Delete the access token you are authenticated with (deleteCurrentToken). */
  deleteToken(options?: RequestOptions): Promise<void> {
    return this.call(deleteCurrentToken, undefined, {}, options);
  }

  /** Get the access token you are authenticated with (getCurrentToken). */
  getToken(options?: RequestOptions): Promise<CurrentAccessToken> {
    return this.call(getCurrentToken, undefined, {}, options);
  }

  /** Get your user settings (getUserSettings). */
  getSettings(options?: RequestOptions): Promise<UserSettings> {
    return this.call(getUserSettings, undefined, {}, options);
  }

  /** Get the token to sign to verify a GPG key (getVerificationToken). */
  getGpgVerificationToken(options?: RequestOptions): Promise<string> {
    return this.call(getVerificationToken, undefined, {}, options);
  }

  /** List one page of your organizations (orgListCurrentUserOrgs). */
  listOrgs(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Organization>> {
    return this.call(orgListCurrentUserOrgs, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterOrgs(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Organization, void, undefined> {
    return this.paginate(orgListCurrentUserOrgs, undefined, { ...params }, options);
  }

  /** Change your user settings (updateUserSettings). */
  updateSettings(body?: UserSettingsOptions, options?: RequestOptions): Promise<UserSettings> {
    return this.call(updateUserSettings, body, {}, options);
  }

  /** Add email addresses (userAddEmail). */
  addEmails(body?: CreateEmailOption, options?: RequestOptions): Promise<Array<Email>> {
    return this.call(userAddEmail, body, {}, options);
  }

  /** Block a user (userBlockUser). */
  blockUser(username: string, params: { note?: string } = {}, options?: RequestOptions): Promise<void> {
    return this.call(userBlockUser, undefined, { username, ...params }, options);
  }

  /** Check whether you block a user (userCheckUserBlock). */
  checkBlockedUser(username: string, options?: RequestOptions): Promise<void> {
    return this.call(userCheckUserBlock, undefined, { username }, options);
  }

  /** Create an OAuth2 application (userCreateOAuth2Application). */
  createOauth2App(body: CreateOAuth2ApplicationOptions, options?: RequestOptions): Promise<OAuth2Application> {
    return this.call(userCreateOAuth2Application, body, {}, options);
  }

  /** Check whether you follow a user (userCurrentCheckFollowing). */
  checkFollowing(username: string, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentCheckFollowing, undefined, { username }, options);
  }

  /** Check whether you starred a repository (userCurrentCheckStarring). */
  checkStarred(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentCheckStarring, undefined, { owner, repo }, options);
  }

  /** Check whether you watch a repository (userCurrentCheckSubscription). */
  checkWatching(owner: string, repo: string, options?: RequestOptions): Promise<WatchInfo> {
    return this.call(userCurrentCheckSubscription, undefined, { owner, repo }, options);
  }

  /** Stop following a user (userCurrentDeleteFollow). */
  unfollow(username: string, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentDeleteFollow, undefined, { username }, options);
  }

  /** Delete one of your GPG keys (userCurrentDeleteGPGKey). */
  deleteGpgKey(id: number, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentDeleteGPGKey, undefined, { id }, options);
  }

  /** Delete one of your SSH keys (userCurrentDeleteKey). */
  deleteKey(id: number, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentDeleteKey, undefined, { id }, options);
  }

  /** Unstar a repository (userCurrentDeleteStar). */
  unstar(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentDeleteStar, undefined, { owner, repo }, options);
  }

  /** Stop watching a repository (userCurrentDeleteSubscription). */
  unwatch(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentDeleteSubscription, undefined, { owner, repo }, options);
  }

  /** Get one of your GPG keys (userCurrentGetGPGKey). */
  getGpgKey(id: number, options?: RequestOptions): Promise<GPGKey> {
    return this.call(userCurrentGetGPGKey, undefined, { id }, options);
  }

  /** Get one of your SSH keys (userCurrentGetKey). */
  getKey(id: number, options?: RequestOptions): Promise<PublicKey> {
    return this.call(userCurrentGetKey, undefined, { id }, options);
  }

  /** List one page of your followers (userCurrentListFollowers). */
  listFollowers(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<User>> {
    return this.call(userCurrentListFollowers, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFollowers(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(userCurrentListFollowers, undefined, { ...params }, options);
  }

  /** List one page of the users you follow (userCurrentListFollowing). */
  listFollowing(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<User>> {
    return this.call(userCurrentListFollowing, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFollowing(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(userCurrentListFollowing, undefined, { ...params }, options);
  }

  /** List one page of your GPG keys (userCurrentListGPGKeys). */
  listGpgKeys(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<GPGKey>> {
    return this.call(userCurrentListGPGKeys, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterGpgKeys(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.GPGKey, void, undefined> {
    return this.paginate(userCurrentListGPGKeys, undefined, { ...params }, options);
  }

  /** List one page of your SSH keys (userCurrentListKeys). */
  listKeys(
    params: { fingerprint?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<PublicKey>> {
    return this.call(userCurrentListKeys, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterKeys(
    params: { fingerprint?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PublicKey, void, undefined> {
    return this.paginate(userCurrentListKeys, undefined, { ...params }, options);
  }

  /** List one page of the repositories you own or can access (userCurrentListRepos). */
  listRepos(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Repository>> {
    return this.call(userCurrentListRepos, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRepos(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(userCurrentListRepos, undefined, { ...params }, options);
  }

  /** List one page of the repositories you starred (userCurrentListStarred). */
  listStarred(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Repository>> {
    return this.call(userCurrentListStarred, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStarred(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(userCurrentListStarred, undefined, { ...params }, options);
  }

  /** List one page of the repositories you watch (userCurrentListSubscriptions). */
  listWatched(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Repository>> {
    return this.call(userCurrentListSubscriptions, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterWatched(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(userCurrentListSubscriptions, undefined, { ...params }, options);
  }

  /** Add a GPG key (userCurrentPostGPGKey). */
  addGpgKey(body?: CreateGPGKeyOption, options?: RequestOptions): Promise<GPGKey> {
    return this.call(userCurrentPostGPGKey, body, {}, options);
  }

  /** Add an SSH key (userCurrentPostKey). */
  addKey(body?: CreateKeyOption, options?: RequestOptions): Promise<PublicKey> {
    return this.call(userCurrentPostKey, body, {}, options);
  }

  /** Follow a user (userCurrentPutFollow). */
  follow(username: string, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentPutFollow, undefined, { username }, options);
  }

  /** Star a repository (userCurrentPutStar). */
  star(owner: string, repo: string, options?: RequestOptions): Promise<void> {
    return this.call(userCurrentPutStar, undefined, { owner, repo }, options);
  }

  /** Watch a repository (userCurrentPutSubscription). */
  watch(owner: string, repo: string, options?: RequestOptions): Promise<WatchInfo> {
    return this.call(userCurrentPutSubscription, undefined, { owner, repo }, options);
  }

  /** List one page of the time you tracked (userCurrentTrackedTimes). */
  listTrackedTimes(
    params: { page?: number; limit?: number; since?: string; before?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<TrackedTime>> {
    return this.call(userCurrentTrackedTimes, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTrackedTimes(
    params: { page?: number; limit?: number; since?: string; before?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TrackedTime, void, undefined> {
    return this.paginate(userCurrentTrackedTimes, undefined, { ...params }, options);
  }

  /** Remove your avatar (userDeleteAvatar). */
  deleteAvatar(options?: RequestOptions): Promise<void> {
    return this.call(userDeleteAvatar, undefined, {}, options);
  }

  /** Remove email addresses (userDeleteEmail). */
  deleteEmails(body?: DeleteEmailOption, options?: RequestOptions): Promise<void> {
    return this.call(userDeleteEmail, body, {}, options);
  }

  /** Delete one of your OAuth2 applications (userDeleteOAuth2Application). */
  deleteOauth2App(id: number, options?: RequestOptions): Promise<void> {
    return this.call(userDeleteOAuth2Application, undefined, { id }, options);
  }

  /** Get the user you are authenticated as (userGetCurrent). */
  get(options?: RequestOptions): Promise<User> {
    return this.call(userGetCurrent, undefined, {}, options);
  }

  /** Get one of your OAuth2 applications (userGetOAuth2Application). */
  getOauth2App(id: number, options?: RequestOptions): Promise<OAuth2Application> {
    return this.call(userGetOAuth2Application, undefined, { id }, options);
  }

  /** List one page of your OAuth2 applications (userGetOauth2Application). */
  listOauth2Apps(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<OAuth2Application>> {
    return this.call(userGetOauth2Application, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterOauth2Apps(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.OAuth2Application, void, undefined> {
    return this.paginate(userGetOauth2Application, undefined, { ...params }, options);
  }

  /** List one page of your running stopwatches (userGetStopWatches). */
  listStopwatches(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<StopWatch>> {
    return this.call(userGetStopWatches, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStopwatches(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.StopWatch, void, undefined> {
    return this.paginate(userGetStopWatches, undefined, { ...params }, options);
  }

  /** List one page of the users you block (userListBlocks). */
  listBlockedUsers(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<User>> {
    return this.call(userListBlocks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterBlockedUsers(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(userListBlocks, undefined, { ...params }, options);
  }

  /** List your email addresses (userListEmails). */
  listEmails(options?: RequestOptions): Promise<Array<Email>> {
    return this.call(userListEmails, undefined, {}, options);
  }

  /** List one page of the teams you are in (userListTeams). */
  listTeams(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Team>> {
    return this.call(userListTeams, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTeams(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Team, void, undefined> {
    return this.paginate(userListTeams, undefined, { ...params }, options);
  }

  /** Unblock a user (userUnblockUser). */
  unblockUser(username: string, options?: RequestOptions): Promise<void> {
    return this.call(userUnblockUser, undefined, { username }, options);
  }

  /** Set your avatar (userUpdateAvatar). */
  updateAvatar(body?: UpdateUserAvatarOption, options?: RequestOptions): Promise<void> {
    return this.call(userUpdateAvatar, body, {}, options);
  }

  /** Change one of your OAuth2 applications (userUpdateOAuth2Application). */
  updateOauth2App(
    id: number,
    body: CreateOAuth2ApplicationOptions,
    options?: RequestOptions,
  ): Promise<OAuth2Application> {
    return this.call(userUpdateOAuth2Application, body, { id }, options);
  }

  /** Verify a GPG key with a signed token (userVerifyGPGKey). */
  verifyGpgKey(options?: RequestOptions): Promise<GPGKey> {
    return this.call(userVerifyGPGKey, undefined, {}, options);
  }
}
