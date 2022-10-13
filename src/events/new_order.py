
import functools

from src.models.Event import Event
from src.models.Order import Order


class NewOrder(Event):

    def __init__(self, name_event: str = 'NewOrder') -> None:
        super().__init__(name_event)
    
    def run(self, order:Order): #type: ignore
        try:
            # Customer data
            self.logging.info(' Order Generated '.center(50, '-'))
            self.logging.info(f'[Customer]: {order.customer.customer_info.lastname.capitalize()}, {order.customer.customer_info.name.capitalize()}')
            self.logging.info(f'[Customer]: {order.customer.customer_info.id}') 
            # Employee data
            self.logging.info(f'[Employee]: {order.employee.employee_info.username.capitalize()}')
            self.logging.info(f'[Employee]: {order.employee.employee_info.id}')
            # Ticket data
            self.logging.info("[Order]: Products:\n\t* " + '\n\t* '.join([f'{p.name} - {p.price}' for p in order.products]))
            self.logging.info(f'[Order]: {len(order.products)} products in total')
            self.logging.info(f'[Order]: ${functools.reduce(lambda curr, prev: curr + prev, [p.price for p in order.products])}')
            if order.discount:
                total = sum(p.price for p in order.products)
                self.logging.info(f'[Order] discount: ${total -  (total * order.customer.avaiable_discount)}')
        except Exception as e:
            self.logging.error(f'[NewOrder] {e.with_traceback(None)}')