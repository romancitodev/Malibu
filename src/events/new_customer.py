from src.models.Event import Event
from src.models.Customer import CustomerBase


class NewCustomer(Event):
    '''
    NewCustomer Event
    '''
    def __init__(self, name_event: str) -> None:
        super().__init__(name_event)
    
    def run(self, customer: CustomerBase) -> None: # type: ignore
        self.logging.info(' New Customer '.center(50, '-'))
        self.logging.info(f'[Customer]: {customer.customer_info.get("name", "").capitalize()}')
        self.logging.info(f'[Customer]: {customer.customer_info.get("type")}') 
        self.logging.info(f'[Customer]: {customer.customer_info.get("id")}') 