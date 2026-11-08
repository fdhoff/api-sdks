# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.stores.models.add_store_category_request_type import AddStoreCategoryRequestType
from ebay_sell.stores.models.delete_store_category_request_type import DeleteStoreCategoryRequestType
from ebay_sell.stores.models.get_store_categories_response_type import GetStoreCategoriesResponseType
from ebay_sell.stores.models.get_store_response_type import GetStoreResponseType
from ebay_sell.stores.models.get_store_task_response_type import GetStoreTaskResponseType
from ebay_sell.stores.models.get_store_tasks_response_type import GetStoreTasksResponseType
from ebay_sell.stores.models.move_store_category_request_type import MoveStoreCategoryRequestType
from ebay_sell.stores.models.rename_store_category_request_type import RenameStoreCategoryRequestType

_add_store_category: Operation[None] = Operation(
    id="addStoreCategory",
    method="POST",
    path="/sell/stores/v1/store/categories",
    resource="store",
    name="add_category",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)
_delete_store_category: Operation[None] = Operation(
    id="deleteStoreCategory",
    method="DELETE",
    path="/sell/stores/v1/store/categories/{category_id}",
    resource="store",
    name="delete_category",
    params=(Param("category_id", "category_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)
_get_store: Operation[GetStoreResponseType] = Operation(
    id="getStore",
    method="GET",
    path="/sell/stores/v1/store",
    resource="store",
    name="get",
    params=(),
    response=GetStoreResponseType,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)
_get_store_categories: Operation[GetStoreCategoriesResponseType] = Operation(
    id="getStoreCategories",
    method="GET",
    path="/sell/stores/v1/store/categories",
    resource="store",
    name="list_categories",
    params=(),
    response=GetStoreCategoriesResponseType,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)
_get_store_task: Operation[GetStoreTaskResponseType] = Operation(
    id="getStoreTask",
    method="GET",
    path="/sell/stores/v1/store/tasks/{task_id}",
    resource="store",
    name="get_task",
    params=(Param("task_id", "task_id", "path"),),
    response=GetStoreTaskResponseType,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)
_get_store_tasks: Operation[GetStoreTasksResponseType] = Operation(
    id="getStoreTasks",
    method="GET",
    path="/sell/stores/v1/store/tasks",
    resource="store",
    name="list_tasks",
    params=(),
    response=GetStoreTasksResponseType,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)
_move_store_category: Operation[None] = Operation(
    id="moveStoreCategory",
    method="POST",
    path="/sell/stores/v1/store/categories/move_category",
    resource="store",
    name="move_category",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)
_rename_store_category: Operation[None] = Operation(
    id="renameStoreCategory",
    method="PUT",
    path="/sell/stores/v1/store/categories/{category_id}",
    resource="store",
    name="rename_category",
    params=(Param("category_id", "category_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.stores",)),),),
    host="api",
)

OPERATIONS = (
    _add_store_category,
    _delete_store_category,
    _get_store,
    _get_store_categories,
    _get_store_task,
    _get_store_tasks,
    _move_store_category,
    _rename_store_category,
)


class StoreApi(Resource):
    @checked
    def add_category(
        self,
        body: Optional[Union[AddStoreCategoryRequestType, Mapping[str, Any]]] = None,
    ) -> None:
        """Start a task that adds a store category."""
        return self._call(
            _add_store_category,
            _body=body,
        )

    @checked
    def delete_category(
        self,
        category_id: StrictStr,
        body: Optional[Union[DeleteStoreCategoryRequestType, Mapping[str, Any]]] = None,
    ) -> None:
        """Start a task that deletes a store category."""
        return self._call(
            _delete_store_category,
            category_id=category_id,
            _body=body,
        )

    @checked
    def get(
        self,
    ) -> GetStoreResponseType:
        """Get the seller's eBay store."""
        return self._call(
            _get_store,
        )

    @checked
    def list_categories(
        self,
    ) -> GetStoreCategoriesResponseType:
        """List the categories of the seller's store."""
        return self._call(
            _get_store_categories,
        )

    @checked
    def get_task(
        self,
        task_id: StrictStr,
    ) -> GetStoreTaskResponseType:
        """Get one store category task."""
        return self._call(
            _get_store_task,
            task_id=task_id,
        )

    @checked
    def list_tasks(
        self,
    ) -> GetStoreTasksResponseType:
        """List the seller's store category tasks."""
        return self._call(
            _get_store_tasks,
        )

    @checked
    def move_category(
        self,
        body: Union[MoveStoreCategoryRequestType, Mapping[str, Any]],
    ) -> None:
        """Start a task that moves a store category."""
        return self._call(
            _move_store_category,
            _body=body,
        )

    @checked
    def rename_category(
        self,
        category_id: StrictStr,
        body: Optional[Union[RenameStoreCategoryRequestType, Mapping[str, Any]]] = None,
    ) -> None:
        """Rename a store category."""
        return self._call(
            _rename_store_category,
            category_id=category_id,
            _body=body,
        )


class AsyncStoreApi(AsyncResource):
    @checked
    async def add_category(
        self,
        body: Optional[Union[AddStoreCategoryRequestType, Mapping[str, Any]]] = None,
    ) -> None:
        """Start a task that adds a store category."""
        return await self._call(
            _add_store_category,
            _body=body,
        )

    @checked
    async def delete_category(
        self,
        category_id: StrictStr,
        body: Optional[Union[DeleteStoreCategoryRequestType, Mapping[str, Any]]] = None,
    ) -> None:
        """Start a task that deletes a store category."""
        return await self._call(
            _delete_store_category,
            category_id=category_id,
            _body=body,
        )

    @checked
    async def get(
        self,
    ) -> GetStoreResponseType:
        """Get the seller's eBay store."""
        return await self._call(
            _get_store,
        )

    @checked
    async def list_categories(
        self,
    ) -> GetStoreCategoriesResponseType:
        """List the categories of the seller's store."""
        return await self._call(
            _get_store_categories,
        )

    @checked
    async def get_task(
        self,
        task_id: StrictStr,
    ) -> GetStoreTaskResponseType:
        """Get one store category task."""
        return await self._call(
            _get_store_task,
            task_id=task_id,
        )

    @checked
    async def list_tasks(
        self,
    ) -> GetStoreTasksResponseType:
        """List the seller's store category tasks."""
        return await self._call(
            _get_store_tasks,
        )

    @checked
    async def move_category(
        self,
        body: Union[MoveStoreCategoryRequestType, Mapping[str, Any]],
    ) -> None:
        """Start a task that moves a store category."""
        return await self._call(
            _move_store_category,
            _body=body,
        )

    @checked
    async def rename_category(
        self,
        category_id: StrictStr,
        body: Optional[Union[RenameStoreCategoryRequestType, Mapping[str, Any]]] = None,
    ) -> None:
        """Rename a store category."""
        return await self._call(
            _rename_store_category,
            category_id=category_id,
            _body=body,
        )
