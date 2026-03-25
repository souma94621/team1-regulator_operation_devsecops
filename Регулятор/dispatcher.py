# dispatcher.py
import json
import logging
from typing import Dict, Any, Callable

logger = logging.getLogger(__name__)

class Dispatcher:
    def __init__(self):
        self.routes: Dict[str, Callable] = {}
    
    def register(self, topic: str, handler: Callable):
        self.routes[topic] = handler
    
    async def dispatch(self, topic: str, message: Dict[str, Any]):
        handler = self.routes.get(topic)
        if handler:
            await handler(message)
        else:
            logger.warning(f"No handler for topic {topic}")