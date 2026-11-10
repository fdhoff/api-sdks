# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, List, Mapping, Optional, Union

from pydantic import StrictStr

from gitea_rest._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from gitea_rest.models.general_api_settings import GeneralAPISettings
from gitea_rest.models.general_attachment_settings import GeneralAttachmentSettings
from gitea_rest.models.general_repo_settings import GeneralRepoSettings
from gitea_rest.models.general_ui_settings import GeneralUISettings
from gitea_rest.models.gitignore_template_info import GitignoreTemplateInfo
from gitea_rest.models.label_template import LabelTemplate
from gitea_rest.models.license_template_info import LicenseTemplateInfo
from gitea_rest.models.licenses_template_list_entry import LicensesTemplateListEntry
from gitea_rest.models.markdown_option import MarkdownOption
from gitea_rest.models.markup_option import MarkupOption
from gitea_rest.models.server_version import ServerVersion

_get_general_api_settings: Operation[GeneralAPISettings] = Operation(
    id="getGeneralAPISettings",
    method="GET",
    path="/settings/api",
    resource="misc",
    name="get_api_settings",
    params=(),
    response=GeneralAPISettings,
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
_get_general_attachment_settings: Operation[GeneralAttachmentSettings] = Operation(
    id="getGeneralAttachmentSettings",
    method="GET",
    path="/settings/attachment",
    resource="misc",
    name="get_attachment_settings",
    params=(),
    response=GeneralAttachmentSettings,
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
_get_general_repository_settings: Operation[GeneralRepoSettings] = Operation(
    id="getGeneralRepositorySettings",
    method="GET",
    path="/settings/repository",
    resource="misc",
    name="get_repository_settings",
    params=(),
    response=GeneralRepoSettings,
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
_get_general_ui_settings: Operation[GeneralUISettings] = Operation(
    id="getGeneralUISettings",
    method="GET",
    path="/settings/ui",
    resource="misc",
    name="get_ui_settings",
    params=(),
    response=GeneralUISettings,
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
_get_gitignore_template_info: Operation[GitignoreTemplateInfo] = Operation(
    id="getGitignoreTemplateInfo",
    method="GET",
    path="/gitignore/templates/{name}",
    resource="misc",
    name="get_gitignore_template",
    params=(Param("name", "name", "path"),),
    response=GitignoreTemplateInfo,
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
_get_label_template_info: Operation[List[LabelTemplate]] = Operation(
    id="getLabelTemplateInfo",
    method="GET",
    path="/label/templates/{name}",
    resource="misc",
    name="get_label_template",
    params=(Param("name", "name", "path"),),
    response=List[LabelTemplate],
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
_get_license_template_info: Operation[LicenseTemplateInfo] = Operation(
    id="getLicenseTemplateInfo",
    method="GET",
    path="/licenses/{name}",
    resource="misc",
    name="get_license_template",
    params=(Param("name", "name", "path"),),
    response=LicenseTemplateInfo,
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
_get_signing_key: Operation[str] = Operation(
    id="getSigningKey",
    method="GET",
    path="/signing-key.gpg",
    resource="misc",
    name="get_signing_key",
    params=(),
    response=str,
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
_get_signing_key_ssh: Operation[str] = Operation(
    id="getSigningKeySSH",
    method="GET",
    path="/signing-key.pub",
    resource="misc",
    name="get_ssh_signing_key",
    params=(),
    response=str,
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
_get_version: Operation[ServerVersion] = Operation(
    id="getVersion",
    method="GET",
    path="/version",
    resource="misc",
    name="get_version",
    params=(),
    response=ServerVersion,
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
_list_gitignores_templates: Operation[List[str]] = Operation(
    id="listGitignoresTemplates",
    method="GET",
    path="/gitignore/templates",
    resource="misc",
    name="list_gitignore_templates",
    params=(),
    response=List[str],
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
_list_label_templates: Operation[List[str]] = Operation(
    id="listLabelTemplates",
    method="GET",
    path="/label/templates",
    resource="misc",
    name="list_label_templates",
    params=(),
    response=List[str],
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
_list_license_templates: Operation[List[LicensesTemplateListEntry]] = Operation(
    id="listLicenseTemplates",
    method="GET",
    path="/licenses",
    resource="misc",
    name="list_license_templates",
    params=(),
    response=List[LicensesTemplateListEntry],
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
_render_markdown: Operation[str] = Operation(
    id="renderMarkdown",
    method="POST",
    path="/markdown",
    resource="misc",
    name="render_markdown",
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
_render_markdown_raw: Operation[str] = Operation(
    id="renderMarkdownRaw",
    method="POST",
    path="/markdown/raw",
    resource="misc",
    name="render_markdown_raw",
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
_render_markup: Operation[str] = Operation(
    id="renderMarkup",
    method="POST",
    path="/markup",
    resource="misc",
    name="render_markup",
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

OPERATIONS = (
    _get_general_api_settings,
    _get_general_attachment_settings,
    _get_general_repository_settings,
    _get_general_ui_settings,
    _get_gitignore_template_info,
    _get_label_template_info,
    _get_license_template_info,
    _get_signing_key,
    _get_signing_key_ssh,
    _get_version,
    _list_gitignores_templates,
    _list_label_templates,
    _list_license_templates,
    _render_markdown,
    _render_markdown_raw,
    _render_markup,
)


class MiscApi(Resource):
    @checked
    def get_api_settings(
        self,
    ) -> GeneralAPISettings:
        """Get the instance's API settings (getGeneralAPISettings)."""
        return self._call(
            _get_general_api_settings,
        )

    @checked
    def get_attachment_settings(
        self,
    ) -> GeneralAttachmentSettings:
        """Get the instance's attachment settings (getGeneralAttachmentSettings)."""
        return self._call(
            _get_general_attachment_settings,
        )

    @checked
    def get_repository_settings(
        self,
    ) -> GeneralRepoSettings:
        """Get the instance's repository settings (getGeneralRepositorySettings)."""
        return self._call(
            _get_general_repository_settings,
        )

    @checked
    def get_ui_settings(
        self,
    ) -> GeneralUISettings:
        """Get the instance's UI settings (getGeneralUISettings)."""
        return self._call(
            _get_general_ui_settings,
        )

    @checked
    def get_gitignore_template(
        self,
        name: StrictStr,
    ) -> GitignoreTemplateInfo:
        """Get a .gitignore template (getGitignoreTemplateInfo)."""
        return self._call(
            _get_gitignore_template_info,
            name=name,
        )

    @checked
    def get_label_template(
        self,
        name: StrictStr,
    ) -> List[LabelTemplate]:
        """Get a label template (getLabelTemplateInfo)."""
        return self._call(
            _get_label_template_info,
            name=name,
        )

    @checked
    def get_license_template(
        self,
        name: StrictStr,
    ) -> LicenseTemplateInfo:
        """Get a license template (getLicenseTemplateInfo)."""
        return self._call(
            _get_license_template_info,
            name=name,
        )

    @checked
    def get_signing_key(
        self,
    ) -> str:
        """Get the GPG key the instance signs commits with (getSigningKey)."""
        return self._call(
            _get_signing_key,
        )

    @checked
    def get_ssh_signing_key(
        self,
    ) -> str:
        """Get the SSH key the instance signs commits with (getSigningKeySSH)."""
        return self._call(
            _get_signing_key_ssh,
        )

    @checked
    def get_version(
        self,
    ) -> ServerVersion:
        """Get the instance's Gitea version (getVersion)."""
        return self._call(
            _get_version,
        )

    @checked
    def list_gitignore_templates(
        self,
    ) -> List[str]:
        """List the .gitignore templates (listGitignoresTemplates)."""
        return self._call(
            _list_gitignores_templates,
        )

    @checked
    def list_label_templates(
        self,
    ) -> List[str]:
        """List the label templates (listLabelTemplates)."""
        return self._call(
            _list_label_templates,
        )

    @checked
    def list_license_templates(
        self,
    ) -> List[LicensesTemplateListEntry]:
        """List the license templates (listLicenseTemplates)."""
        return self._call(
            _list_license_templates,
        )

    @checked
    def render_markdown(
        self,
        body: Optional[Union[MarkdownOption, Mapping[str, Any]]] = None,
    ) -> str:
        """Render Markdown as HTML (renderMarkdown)."""
        return self._call(
            _render_markdown,
            _body=body,
        )

    @checked
    def render_markdown_raw(
        self,
        body: Union[str, Mapping[str, Any]],
    ) -> str:
        """Render a raw Markdown body as HTML (renderMarkdownRaw)."""
        return self._call(
            _render_markdown_raw,
            _body=body,
        )

    @checked
    def render_markup(
        self,
        body: Optional[Union[MarkupOption, Mapping[str, Any]]] = None,
    ) -> str:
        """Render a markup language, such as Markdown or AsciiDoc, as HTML (renderMarkup)."""
        return self._call(
            _render_markup,
            _body=body,
        )


class AsyncMiscApi(AsyncResource):
    @checked
    async def get_api_settings(
        self,
    ) -> GeneralAPISettings:
        """Get the instance's API settings (getGeneralAPISettings)."""
        return await self._call(
            _get_general_api_settings,
        )

    @checked
    async def get_attachment_settings(
        self,
    ) -> GeneralAttachmentSettings:
        """Get the instance's attachment settings (getGeneralAttachmentSettings)."""
        return await self._call(
            _get_general_attachment_settings,
        )

    @checked
    async def get_repository_settings(
        self,
    ) -> GeneralRepoSettings:
        """Get the instance's repository settings (getGeneralRepositorySettings)."""
        return await self._call(
            _get_general_repository_settings,
        )

    @checked
    async def get_ui_settings(
        self,
    ) -> GeneralUISettings:
        """Get the instance's UI settings (getGeneralUISettings)."""
        return await self._call(
            _get_general_ui_settings,
        )

    @checked
    async def get_gitignore_template(
        self,
        name: StrictStr,
    ) -> GitignoreTemplateInfo:
        """Get a .gitignore template (getGitignoreTemplateInfo)."""
        return await self._call(
            _get_gitignore_template_info,
            name=name,
        )

    @checked
    async def get_label_template(
        self,
        name: StrictStr,
    ) -> List[LabelTemplate]:
        """Get a label template (getLabelTemplateInfo)."""
        return await self._call(
            _get_label_template_info,
            name=name,
        )

    @checked
    async def get_license_template(
        self,
        name: StrictStr,
    ) -> LicenseTemplateInfo:
        """Get a license template (getLicenseTemplateInfo)."""
        return await self._call(
            _get_license_template_info,
            name=name,
        )

    @checked
    async def get_signing_key(
        self,
    ) -> str:
        """Get the GPG key the instance signs commits with (getSigningKey)."""
        return await self._call(
            _get_signing_key,
        )

    @checked
    async def get_ssh_signing_key(
        self,
    ) -> str:
        """Get the SSH key the instance signs commits with (getSigningKeySSH)."""
        return await self._call(
            _get_signing_key_ssh,
        )

    @checked
    async def get_version(
        self,
    ) -> ServerVersion:
        """Get the instance's Gitea version (getVersion)."""
        return await self._call(
            _get_version,
        )

    @checked
    async def list_gitignore_templates(
        self,
    ) -> List[str]:
        """List the .gitignore templates (listGitignoresTemplates)."""
        return await self._call(
            _list_gitignores_templates,
        )

    @checked
    async def list_label_templates(
        self,
    ) -> List[str]:
        """List the label templates (listLabelTemplates)."""
        return await self._call(
            _list_label_templates,
        )

    @checked
    async def list_license_templates(
        self,
    ) -> List[LicensesTemplateListEntry]:
        """List the license templates (listLicenseTemplates)."""
        return await self._call(
            _list_license_templates,
        )

    @checked
    async def render_markdown(
        self,
        body: Optional[Union[MarkdownOption, Mapping[str, Any]]] = None,
    ) -> str:
        """Render Markdown as HTML (renderMarkdown)."""
        return await self._call(
            _render_markdown,
            _body=body,
        )

    @checked
    async def render_markdown_raw(
        self,
        body: Union[str, Mapping[str, Any]],
    ) -> str:
        """Render a raw Markdown body as HTML (renderMarkdownRaw)."""
        return await self._call(
            _render_markdown_raw,
            _body=body,
        )

    @checked
    async def render_markup(
        self,
        body: Optional[Union[MarkupOption, Mapping[str, Any]]] = None,
    ) -> str:
        """Render a markup language, such as Markdown or AsciiDoc, as HTML (renderMarkup)."""
        return await self._call(
            _render_markup,
            _body=body,
        )
