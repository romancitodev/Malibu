from .Product import Product
from src.models.Customer import CustomerBase
from src.models.Employee import EmployeeBase


class Order:
    """
    Class what represents an Order with basic elements:
    `client` : class Client
    `seller`: class Seller
    `*products` : Tuple[Product]
    @optional-keys
    `discount`: bool
    """
    def __init__(self, customer: CustomerBase, employee: EmployeeBase ,*p: Product, discount: bool = False) -> None:
        self.customer = customer
        self.employee = employee
        self.products = p
        self.discount = discount

    def show_ticket_info(self) -> None:
        print([f'{p.id} - {p.name} - ${p.price}' for p in self.products])
