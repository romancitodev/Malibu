import abc
import logging
import os
from typing import Any


class Event(abc.ABC):
    "Abstract class what represents an Event"    
    def __init__(self, name_event: str) -> None:
        self.name = name_event
        self.logging = logging
        self.logging.basicConfig(filename= f'{os.getcwd()}/logs/logs.log', filemode= 'a', encoding="UTF-8", level=logging.DEBUG)
        
    @abc.abstractmethod
    def run(self, *args: Any, **kwargs: Any):
        """run method to use in a specific event"""
        ...
