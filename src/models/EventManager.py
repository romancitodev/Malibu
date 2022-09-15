import os
import sys
from typing import Any
from typing_extensions import Self
from .Event import Event
from pathlib import Path

class EventManager:
    
    def __init__(self) -> None:
        self.events: dict[str,Event] = dict()

    def setup(self, events_path:Path | str | None = None) -> Self:
        """setup the event manager with pre-charged events"""
        if events_path:
            events_files = [f for f in os.listdir(events_path) if os.path.isfile(os.path.join(events_path, f))]
            for c in events_files:
                file = open(f'{events_path}/{c}', 'r')
                c = c.split('.')[0]
                text = file.read()
                if len(text) > 0:
                    class_declaration = text.find('class') + 6
                    class_name = text.find('(', class_declaration)
                    class_name = text[class_declaration:class_name]
                    sys.path.append(r'{}'.format(events_path))
                    a = __import__(r'{}'.format(c))
                    if not getattr(a, class_name).__base__ == Event:
                        continue
                    self.events[class_name] = getattr(a, class_name)(class_name)
                    print(f'[!] Event {class_name:10s} Charged succesfully.')
        else:
            raise Exception(f'{events_path} is not a valid Path.')
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