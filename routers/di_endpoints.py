import gc

from fastapi import Depends
from dependency_injector.wiring import Provide, inject

from di_base_service import BaseService
from di_container import Container

from fastapi import APIRouter

router = APIRouter(
    prefix="",
    redirect_slashes=False,
)


@router.get("/sync/di-container")
@inject
def sync_di_container(
    base_service: BaseService = Depends(Provide[Container.base_service]),
):
    return {
        "router_name": "/sync/di-container",
        "item": base_service.hello_world(),
        "object_count": len(gc.get_objects()),
    }
