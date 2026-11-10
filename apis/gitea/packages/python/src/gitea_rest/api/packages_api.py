# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, List, Optional

from pydantic import StrictInt, StrictStr

from gitea_rest import models as _models
from gitea_rest._runtime import (
    AsyncResource,
    LinkHeader,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from gitea_rest.models.package import Package
from gitea_rest.models.package_file import PackageFile

_delete_package: Operation[None] = Operation(
    id="deletePackage",
    method="DELETE",
    path="/packages/{owner}/{type}/{name}",
    resource="packages",
    name="delete",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
    ),
    response=None,
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
_delete_package_version: Operation[None] = Operation(
    id="deletePackageVersion",
    method="DELETE",
    path="/packages/{owner}/{type}/{name}/{version}",
    resource="packages",
    name="delete_version",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
        Param("version", "version", "path"),
    ),
    response=None,
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
_get_latest_package_version: Operation[Package] = Operation(
    id="getLatestPackageVersion",
    method="GET",
    path="/packages/{owner}/{type}/{name}/-/latest",
    resource="packages",
    name="get_latest_version",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
    ),
    response=Package,
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
_get_package: Operation[Package] = Operation(
    id="getPackage",
    method="GET",
    path="/packages/{owner}/{type}/{name}/{version}",
    resource="packages",
    name="get",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
        Param("version", "version", "path"),
    ),
    response=Package,
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
_link_package: Operation[None] = Operation(
    id="linkPackage",
    method="POST",
    path="/packages/{owner}/{type}/{name}/-/link/{repo_name}",
    resource="packages",
    name="link",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
        Param("repo_name", "repo_name", "path"),
    ),
    response=None,
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
_list_package_files: Operation[List[PackageFile]] = Operation(
    id="listPackageFiles",
    method="GET",
    path="/packages/{owner}/{type}/{name}/{version}/files",
    resource="packages",
    name="list_files",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
        Param("version", "version", "path"),
    ),
    response=List[PackageFile],
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
_list_package_versions: Operation[List[Package]] = Operation(
    id="listPackageVersions",
    method="GET",
    path="/packages/{owner}/{type}/{name}",
    resource="packages",
    name="list_versions",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
    ),
    response=List[Package],
    returns_json=True,
    iterator="iter_versions",
    item=_models.Package,
    paging=LinkHeader(
        items="$",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
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
_list_packages: Operation[List[Package]] = Operation(
    id="listPackages",
    method="GET",
    path="/packages/{owner}",
    resource="packages",
    name="list",
    params=(
        Param("owner", "owner", "path"),
        Param("page", "page", "query"),
        Param("limit", "limit", "query"),
        Param("type", "type", "query"),
        Param("q", "q", "query"),
    ),
    response=List[Package],
    returns_json=True,
    iterator="iter",
    item=_models.Package,
    paging=LinkHeader(
        items="$",
        rel="next",
        params=(
            "page",
            "limit",
        ),
    ),
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
_unlink_package: Operation[None] = Operation(
    id="unlinkPackage",
    method="POST",
    path="/packages/{owner}/{type}/{name}/-/unlink",
    resource="packages",
    name="unlink",
    params=(
        Param("owner", "owner", "path"),
        Param("type", "type", "path"),
        Param("name", "name", "path"),
    ),
    response=None,
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
    _delete_package,
    _delete_package_version,
    _get_latest_package_version,
    _get_package,
    _link_package,
    _list_package_files,
    _list_package_versions,
    _list_packages,
    _unlink_package,
)


class PackagesApi(Resource):
    @checked
    def delete(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
    ) -> None:
        """Delete a package and all its versions (deletePackage)."""
        return self._call(
            _delete_package,
            owner=owner,
            type=type,
            name=name,
        )

    @checked
    def delete_version(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        version: StrictStr,
    ) -> None:
        """Delete a package version (deletePackageVersion)."""
        return self._call(
            _delete_package_version,
            owner=owner,
            type=type,
            name=name,
            version=version,
        )

    @checked
    def get_latest_version(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
    ) -> Package:
        """Get a package's latest version (getLatestPackageVersion)."""
        return self._call(
            _get_latest_package_version,
            owner=owner,
            type=type,
            name=name,
        )

    @checked
    def get(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        version: StrictStr,
    ) -> Package:
        """Get a package version (getPackage)."""
        return self._call(
            _get_package,
            owner=owner,
            type=type,
            name=name,
            version=version,
        )

    @checked
    def link(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        repo_name: StrictStr,
    ) -> None:
        """Link a package to a repository (linkPackage)."""
        return self._call(
            _link_package,
            owner=owner,
            type=type,
            name=name,
            repo_name=repo_name,
        )

    @checked
    def list_files(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        version: StrictStr,
    ) -> List[PackageFile]:
        """List a package version's files (listPackageFiles)."""
        return self._call(
            _list_package_files,
            owner=owner,
            type=type,
            name=name,
            version=version,
        )

    @checked
    def list_versions(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Package]:
        """List one page of a package's versions (listPackageVersions)."""
        return self._call(
            _list_package_versions,
            owner=owner,
            type=type,
            name=name,
            page=page,
            limit=limit,
        )

    @checked
    def iter_versions(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> Iterator[_models.Package]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_package_versions,
            owner=owner,
            type=type,
            name=name,
            page=page,
            limit=limit,
        )

    @checked
    def list(
        self,
        owner: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> List[Package]:
        """List one page of an owner's packages (listPackages)."""
        return self._call(
            _list_packages,
            owner=owner,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> Iterator[_models.Package]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_packages,
            owner=owner,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    def unlink(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
    ) -> None:
        """Unlink a package from its repository (unlinkPackage)."""
        return self._call(
            _unlink_package,
            owner=owner,
            type=type,
            name=name,
        )


class AsyncPackagesApi(AsyncResource):
    @checked
    async def delete(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
    ) -> None:
        """Delete a package and all its versions (deletePackage)."""
        return await self._call(
            _delete_package,
            owner=owner,
            type=type,
            name=name,
        )

    @checked
    async def delete_version(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        version: StrictStr,
    ) -> None:
        """Delete a package version (deletePackageVersion)."""
        return await self._call(
            _delete_package_version,
            owner=owner,
            type=type,
            name=name,
            version=version,
        )

    @checked
    async def get_latest_version(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
    ) -> Package:
        """Get a package's latest version (getLatestPackageVersion)."""
        return await self._call(
            _get_latest_package_version,
            owner=owner,
            type=type,
            name=name,
        )

    @checked
    async def get(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        version: StrictStr,
    ) -> Package:
        """Get a package version (getPackage)."""
        return await self._call(
            _get_package,
            owner=owner,
            type=type,
            name=name,
            version=version,
        )

    @checked
    async def link(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        repo_name: StrictStr,
    ) -> None:
        """Link a package to a repository (linkPackage)."""
        return await self._call(
            _link_package,
            owner=owner,
            type=type,
            name=name,
            repo_name=repo_name,
        )

    @checked
    async def list_files(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        version: StrictStr,
    ) -> List[PackageFile]:
        """List a package version's files (listPackageFiles)."""
        return await self._call(
            _list_package_files,
            owner=owner,
            type=type,
            name=name,
            version=version,
        )

    @checked
    async def list_versions(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> List[Package]:
        """List one page of a package's versions (listPackageVersions)."""
        return await self._call(
            _list_package_versions,
            owner=owner,
            type=type,
            name=name,
            page=page,
            limit=limit,
        )

    @checked
    def iter_versions(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.Package]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_package_versions,
            owner=owner,
            type=type,
            name=name,
            page=page,
            limit=limit,
        )

    @checked
    async def list(
        self,
        owner: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> List[Package]:
        """List one page of an owner's packages (listPackages)."""
        return await self._call(
            _list_packages,
            owner=owner,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    def iter(
        self,
        owner: StrictStr,
        *,
        page: Optional[StrictInt] = None,
        limit: Optional[StrictInt] = None,
        type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Package]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_packages,
            owner=owner,
            page=page,
            limit=limit,
            type=type,
            q=q,
        )

    @checked
    async def unlink(
        self,
        owner: StrictStr,
        type: StrictStr,
        name: StrictStr,
    ) -> None:
        """Unlink a package from its repository (unlinkPackage)."""
        return await self._call(
            _unlink_package,
            owner=owner,
            type=type,
            name=name,
        )
