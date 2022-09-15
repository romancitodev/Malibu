
import functools
import src.models as mods


class NewOrder(mods.Event.Event):

    def __init__(self, name_event: str) -> None:
        super().__init__(name_event)
    
    def run(self, order:mods.Order.Order): #type: ignore
        try:
            # Customer data
            self.logging.info(' Order Generated '.center(50, '-'))
            self.logging.info(f'[Customer]: {order.customer.customer_info.get("lastname","U.").capitalize()}, {order.customer.customer_info.get("name","U.").capitalize()}')
            self.logging.info(f'[Customer]: {order.customer.customer_info.get("id")}') 
            # Employee data
            self.logging.info(f'[Employee]: {order.employee.employee_info.get("username","Uknown").capitalize()}')
            self.logging.info(f'[Employee]: {order.employee.employee_info.get("id")}')
            # Ticket data
            self.logging.info(f'[Order]: {len(order.products)}')
            self.logging.info(f'[Order]: ${functools.reduce(lambda curr, prev: curr + prev, [p.price for p in order.products])}')
            self.logging.info(f"[Order]: {order.__dict__}")
        except Exception as e:
            self.logging.error(f'[NewOrder] {e.with_traceback(None)}')