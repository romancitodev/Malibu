from ..models.Event import Event
from ..models.EventManager import EventManager
from ..events.new_order import NewOrder
from ..events.new_customer import NewCustomer

def setup_listener(listener: EventManager, pre_events: list[Event] = [NewOrder('NewOrder'),NewCustomer('NewCustomer')]) -> EventManager:
    """
    setup the event manager
    `listener`: EventManager
    `pre_events`: list[Event] | None
    ### @example
    ```py
    # Example 1
    EM = EventManager()
    EM = setup_listener(EM)
    #Example 2
    EM = setup_listener(EventManager())

    #Example 3
    from events import Event1, Event2
    EM = setup_listener(EventManager(), [Event1, Event2])
    ```
    """
    try:
        for pre in pre_events:
            listener.add_event(pre)
        return listener
    except Exception as e:
        raise Exception(e) from None
    