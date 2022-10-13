from typing import Any

from typing_extensions import Self

from .Event import Event
from .Importer import Importer


class EventManager:
    
    def __init__(self) -> None:
        self.events: dict[str,Event] = dict()

    def setup(self, events_path:str) -> Self:
        try:
            self.events = Importer().import_from(events_path, superclass= Event, verboose=True)
        except Exception as err:
            print(err)
        return self

    def add_event(self, event_class: Event) -> None:
        if event_class.name not in self.events:
            self.events[event_class.name] = event_class
            print(f'[!] Event {event_class.name:10s} Charged succesfully.')
        else:
            print(f'[!] Event {event_class.name:10s} Charged yet.')

    def run_event(self, event_name: str,*params: Any,**kparams: Any):
        """run the event if the `event_name` exists in the dict of events"""
        if event_name in self.events:
            self.events[event_name].run(*params, **kparams)
        else:
            raise Exception(f"Event [{event_name}] not found.")