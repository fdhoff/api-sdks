// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  GeneralAPISettings,
  GeneralAttachmentSettings,
  GeneralRepoSettings,
  GeneralUISettings,
  GitignoreTemplateInfo,
  LabelTemplate,
  LicenseTemplateInfo,
  LicensesTemplateListEntry,
  MarkdownOption,
  MarkupOption,
  ServerVersion,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getGeneralAPISettings: Operation = {
  id: 'getGeneralAPISettings',
  method: 'GET',
  path: '/settings/api',
  resource: 'misc',
  name: 'getApiSettings',
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

const getGeneralAttachmentSettings: Operation = {
  id: 'getGeneralAttachmentSettings',
  method: 'GET',
  path: '/settings/attachment',
  resource: 'misc',
  name: 'getAttachmentSettings',
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

const getGeneralRepositorySettings: Operation = {
  id: 'getGeneralRepositorySettings',
  method: 'GET',
  path: '/settings/repository',
  resource: 'misc',
  name: 'getRepositorySettings',
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

const getGeneralUISettings: Operation = {
  id: 'getGeneralUISettings',
  method: 'GET',
  path: '/settings/ui',
  resource: 'misc',
  name: 'getUiSettings',
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

const getGitignoreTemplateInfo: Operation = {
  id: 'getGitignoreTemplateInfo',
  method: 'GET',
  path: '/gitignore/templates/{name}',
  resource: 'misc',
  name: 'getGitignoreTemplate',
  params: [{ wire: 'name', name: 'name', location: 'path' }],
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

const getLabelTemplateInfo: Operation = {
  id: 'getLabelTemplateInfo',
  method: 'GET',
  path: '/label/templates/{name}',
  resource: 'misc',
  name: 'getLabelTemplate',
  params: [{ wire: 'name', name: 'name', location: 'path' }],
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

const getLicenseTemplateInfo: Operation = {
  id: 'getLicenseTemplateInfo',
  method: 'GET',
  path: '/licenses/{name}',
  resource: 'misc',
  name: 'getLicenseTemplate',
  params: [{ wire: 'name', name: 'name', location: 'path' }],
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

const getSigningKey: Operation = {
  id: 'getSigningKey',
  method: 'GET',
  path: '/signing-key.gpg',
  resource: 'misc',
  name: 'getSigningKey',
  params: [],
  returnsText: true,
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

const getSigningKeySSH: Operation = {
  id: 'getSigningKeySSH',
  method: 'GET',
  path: '/signing-key.pub',
  resource: 'misc',
  name: 'getSshSigningKey',
  params: [],
  returnsText: true,
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

const getVersion: Operation = {
  id: 'getVersion',
  method: 'GET',
  path: '/version',
  resource: 'misc',
  name: 'getVersion',
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

const listGitignoresTemplates: Operation = {
  id: 'listGitignoresTemplates',
  method: 'GET',
  path: '/gitignore/templates',
  resource: 'misc',
  name: 'listGitignoreTemplates',
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

const listLabelTemplates: Operation = {
  id: 'listLabelTemplates',
  method: 'GET',
  path: '/label/templates',
  resource: 'misc',
  name: 'listLabelTemplates',
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

const listLicenseTemplates: Operation = {
  id: 'listLicenseTemplates',
  method: 'GET',
  path: '/licenses',
  resource: 'misc',
  name: 'listLicenseTemplates',
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

const renderMarkdown: Operation = {
  id: 'renderMarkdown',
  method: 'POST',
  path: '/markdown',
  resource: 'misc',
  name: 'renderMarkdown',
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

const renderMarkdownRaw: Operation = {
  id: 'renderMarkdownRaw',
  method: 'POST',
  path: '/markdown/raw',
  resource: 'misc',
  name: 'renderMarkdownRaw',
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

const renderMarkup: Operation = {
  id: 'renderMarkup',
  method: 'POST',
  path: '/markup',
  resource: 'misc',
  name: 'renderMarkup',
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

export const OPERATIONS: readonly Operation[] = [
  getGeneralAPISettings,
  getGeneralAttachmentSettings,
  getGeneralRepositorySettings,
  getGeneralUISettings,
  getGitignoreTemplateInfo,
  getLabelTemplateInfo,
  getLicenseTemplateInfo,
  getSigningKey,
  getSigningKeySSH,
  getVersion,
  listGitignoresTemplates,
  listLabelTemplates,
  listLicenseTemplates,
  renderMarkdown,
  renderMarkdownRaw,
  renderMarkup,
];

export class MiscApi extends Resource {
  /** Get the instance's API settings (getGeneralAPISettings). */
  getApiSettings(options?: RequestOptions): Promise<GeneralAPISettings> {
    return this.call(getGeneralAPISettings, undefined, {}, options);
  }

  /** Get the instance's attachment settings (getGeneralAttachmentSettings). */
  getAttachmentSettings(options?: RequestOptions): Promise<GeneralAttachmentSettings> {
    return this.call(getGeneralAttachmentSettings, undefined, {}, options);
  }

  /** Get the instance's repository settings (getGeneralRepositorySettings). */
  getRepositorySettings(options?: RequestOptions): Promise<GeneralRepoSettings> {
    return this.call(getGeneralRepositorySettings, undefined, {}, options);
  }

  /** Get the instance's UI settings (getGeneralUISettings). */
  getUiSettings(options?: RequestOptions): Promise<GeneralUISettings> {
    return this.call(getGeneralUISettings, undefined, {}, options);
  }

  /** Get a .gitignore template (getGitignoreTemplateInfo). */
  getGitignoreTemplate(name: string, options?: RequestOptions): Promise<GitignoreTemplateInfo> {
    return this.call(getGitignoreTemplateInfo, undefined, { name }, options);
  }

  /** Get a label template (getLabelTemplateInfo). */
  getLabelTemplate(name: string, options?: RequestOptions): Promise<Array<LabelTemplate>> {
    return this.call(getLabelTemplateInfo, undefined, { name }, options);
  }

  /** Get a license template (getLicenseTemplateInfo). */
  getLicenseTemplate(name: string, options?: RequestOptions): Promise<LicenseTemplateInfo> {
    return this.call(getLicenseTemplateInfo, undefined, { name }, options);
  }

  /** Get the GPG key the instance signs commits with (getSigningKey). */
  getSigningKey(options?: RequestOptions): Promise<string> {
    return this.call(getSigningKey, undefined, {}, options);
  }

  /** Get the SSH key the instance signs commits with (getSigningKeySSH). */
  getSshSigningKey(options?: RequestOptions): Promise<string> {
    return this.call(getSigningKeySSH, undefined, {}, options);
  }

  /** Get the instance's Gitea version (getVersion). */
  getVersion(options?: RequestOptions): Promise<ServerVersion> {
    return this.call(getVersion, undefined, {}, options);
  }

  /** List the .gitignore templates (listGitignoresTemplates). */
  listGitignoreTemplates(options?: RequestOptions): Promise<Array<string>> {
    return this.call(listGitignoresTemplates, undefined, {}, options);
  }

  /** List the label templates (listLabelTemplates). */
  listLabelTemplates(options?: RequestOptions): Promise<Array<string>> {
    return this.call(listLabelTemplates, undefined, {}, options);
  }

  /** List the license templates (listLicenseTemplates). */
  listLicenseTemplates(options?: RequestOptions): Promise<Array<LicensesTemplateListEntry>> {
    return this.call(listLicenseTemplates, undefined, {}, options);
  }

  /** Render Markdown as HTML (renderMarkdown). */
  renderMarkdown(body?: MarkdownOption, options?: RequestOptions): Promise<string> {
    return this.call(renderMarkdown, body, {}, options);
  }

  /** Render a raw Markdown body as HTML (renderMarkdownRaw). */
  renderMarkdownRaw(body: string, options?: RequestOptions): Promise<string> {
    return this.call(renderMarkdownRaw, body, {}, options);
  }

  /** Render a markup language, such as Markdown or AsciiDoc, as HTML (renderMarkup). */
  renderMarkup(body?: MarkupOption, options?: RequestOptions): Promise<string> {
    return this.call(renderMarkup, body, {}, options);
  }
}
