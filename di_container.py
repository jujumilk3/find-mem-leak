from dependency_injector import containers, providers
from di_base_service import BaseService


class Container(containers.DeclarativeContainer):
    print("container initialized")
    wiring_config = containers.WiringConfiguration(
        modules=[
            "routers.di_endpoints",
        ]
    )

    base_service = providers.Factory(BaseService)
