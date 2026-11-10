// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  ApplyDiffPatchFileOptions,
  ChangeFilesOptions,
  ContentsExtResponse,
  ContentsResponse,
  CreateFileOptions,
  DeleteFileOptions,
  FileDeleteResponse,
  FileResponse,
  FilesResponse,
  GetFilesOptions,
  UpdateFileOptions,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const repoApplyDiffPatch: Operation = {
  id: 'repoApplyDiffPatch',
  method: 'POST',
  path: '/repos/{owner}/{repo}/diffpatch',
  resource: 'contents',
  name: 'applyPatch',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
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

const repoChangeFiles: Operation = {
  id: 'repoChangeFiles',
  method: 'POST',
  path: '/repos/{owner}/{repo}/contents',
  resource: 'contents',
  name: 'changeFiles',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
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

const repoCreateFile: Operation = {
  id: 'repoCreateFile',
  method: 'POST',
  path: '/repos/{owner}/{repo}/contents/{filepath}',
  resource: 'contents',
  name: 'createFile',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
  ],
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

const repoDeleteFile: Operation = {
  id: 'repoDeleteFile',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/contents/{filepath}',
  resource: 'contents',
  name: 'deleteFile',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
  ],
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

const repoGetContents: Operation = {
  id: 'repoGetContents',
  method: 'GET',
  path: '/repos/{owner}/{repo}/contents/{filepath}',
  resource: 'contents',
  name: 'get',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
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

const repoGetContentsExt: Operation = {
  id: 'repoGetContentsExt',
  method: 'GET',
  path: '/repos/{owner}/{repo}/contents-ext/{filepath}',
  resource: 'contents',
  name: 'getExtended',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
    { wire: 'includes', name: 'includes', location: 'query' },
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

const repoGetContentsList: Operation = {
  id: 'repoGetContentsList',
  method: 'GET',
  path: '/repos/{owner}/{repo}/contents',
  resource: 'contents',
  name: 'listRoot',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
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

const repoGetEditorConfig: Operation = {
  id: 'repoGetEditorConfig',
  method: 'GET',
  path: '/repos/{owner}/{repo}/editorconfig/{filepath}',
  resource: 'contents',
  name: 'getEditorconfig',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
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

const repoGetFileContents: Operation = {
  id: 'repoGetFileContents',
  method: 'GET',
  path: '/repos/{owner}/{repo}/file-contents',
  resource: 'contents',
  name: 'getFiles',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
    { wire: 'body', name: 'body', location: 'query' },
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

const repoGetFileContentsPost: Operation = {
  id: 'repoGetFileContentsPost',
  method: 'POST',
  path: '/repos/{owner}/{repo}/file-contents',
  resource: 'contents',
  name: 'getFilesByBody',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
  ],
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

const repoGetRawFile: Operation = {
  id: 'repoGetRawFile',
  method: 'GET',
  path: '/repos/{owner}/{repo}/raw/{filepath}',
  resource: 'contents',
  name: 'downloadRaw',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
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

const repoGetRawFileOrLFS: Operation = {
  id: 'repoGetRawFileOrLFS',
  method: 'GET',
  path: '/repos/{owner}/{repo}/media/{filepath}',
  resource: 'contents',
  name: 'downloadMedia',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
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

const repoUpdateFile: Operation = {
  id: 'repoUpdateFile',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/contents/{filepath}',
  resource: 'contents',
  name: 'updateFile',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'filepath', name: 'filepath', location: 'path' },
  ],
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

export const OPERATIONS: readonly Operation[] = [
  repoApplyDiffPatch,
  repoChangeFiles,
  repoCreateFile,
  repoDeleteFile,
  repoGetContents,
  repoGetContentsExt,
  repoGetContentsList,
  repoGetEditorConfig,
  repoGetFileContents,
  repoGetFileContentsPost,
  repoGetRawFile,
  repoGetRawFileOrLFS,
  repoUpdateFile,
];

export class ContentsApi extends Resource {
  /** Apply a diff in a new commit (repoApplyDiffPatch). */
  applyPatch(
    owner: string,
    repo: string,
    body: ApplyDiffPatchFileOptions,
    options?: RequestOptions,
  ): Promise<FileResponse> {
    return this.call(repoApplyDiffPatch, body, { owner, repo }, options);
  }

  /** Create, change or delete several files in one commit (repoChangeFiles). */
  changeFiles(owner: string, repo: string, body: ChangeFilesOptions, options?: RequestOptions): Promise<FilesResponse> {
    return this.call(repoChangeFiles, body, { owner, repo }, options);
  }

  /** Create a file in a new commit (repoCreateFile). */
  createFile(
    owner: string,
    repo: string,
    filepath: string,
    body: CreateFileOptions,
    options?: RequestOptions,
  ): Promise<FileResponse> {
    return this.call(repoCreateFile, body, { owner, repo, filepath }, options);
  }

  /** Delete a file in a new commit (repoDeleteFile). */
  deleteFile(
    owner: string,
    repo: string,
    filepath: string,
    body: DeleteFileOptions,
    options?: RequestOptions,
  ): Promise<FileDeleteResponse> {
    return this.call(repoDeleteFile, body, { owner, repo, filepath }, options);
  }

  /** Get a file's content and metadata, or a directory's entries (repoGetContents). */
  get(
    owner: string,
    repo: string,
    filepath: string,
    params: { ref?: string } = {},
    options?: RequestOptions,
  ): Promise<ContentsResponse> {
    return this.call(repoGetContents, undefined, { owner, repo, filepath, ...params }, options);
  }

  /** Get a file's or directory's metadata, with content as asked (repoGetContentsExt). */
  getExtended(
    owner: string,
    repo: string,
    filepath: string,
    params: { ref?: string; includes?: string } = {},
    options?: RequestOptions,
  ): Promise<ContentsExtResponse> {
    return this.call(repoGetContentsExt, undefined, { owner, repo, filepath, ...params }, options);
  }

  /** List the entries at the root of a repository (repoGetContentsList). */
  listRoot(
    owner: string,
    repo: string,
    params: { ref?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<ContentsResponse>> {
    return this.call(repoGetContentsList, undefined, { owner, repo, ...params }, options);
  }

  /** Get the EditorConfig settings that apply to a file (repoGetEditorConfig). */
  getEditorconfig(
    owner: string,
    repo: string,
    filepath: string,
    params: { ref?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoGetEditorConfig, undefined, { owner, repo, filepath, ...params }, options);
  }

  /** Get the content and metadata of several files (repoGetFileContents). */
  getFiles(
    owner: string,
    repo: string,
    params: { ref?: string; body: string },
    options?: RequestOptions,
  ): Promise<Array<ContentsResponse>> {
    return this.call(repoGetFileContents, undefined, { owner, repo, ...params }, options);
  }

  /** Get the content and metadata of several files named in the body (repoGetFileContentsPost). */
  getFilesByBody(
    owner: string,
    repo: string,
    body: GetFilesOptions,
    params: { ref?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<ContentsResponse>> {
    return this.call(repoGetFileContentsPost, body, { owner, repo, ...params }, options);
  }

  /** Download a file's raw content (repoGetRawFile). */
  downloadRaw(
    owner: string,
    repo: string,
    filepath: string,
    params: { ref?: string } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(repoGetRawFile, undefined, { owner, repo, filepath, ...params }, options);
  }

  /** Download a file's content, from Git LFS when it is stored there (repoGetRawFileOrLFS). */
  downloadMedia(
    owner: string,
    repo: string,
    filepath: string,
    params: { ref?: string } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(repoGetRawFileOrLFS, undefined, { owner, repo, filepath, ...params }, options);
  }

  /** Change a file in a new commit (repoUpdateFile). */
  updateFile(
    owner: string,
    repo: string,
    filepath: string,
    body: UpdateFileOptions,
    options?: RequestOptions,
  ): Promise<FileResponse> {
    return this.call(repoUpdateFile, body, { owner, repo, filepath }, options);
  }
}
