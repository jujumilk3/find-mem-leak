from loguru import logger


class BaseService:
    def __init__(self):
        logger.info("base service initialized")
        self._base_service = None

    def hello_world(self):
        return "Hello World"
