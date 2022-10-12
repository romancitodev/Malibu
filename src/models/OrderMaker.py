from src.models import Employee, Customer, Product, Order


class OrderMaker:
    
    def make_order(self, customer: Customer.CustomerBase, employee: Employee.EmployeeBase, apply_discount: bool = False):
        limit = int(input("digit the number of products: "))
        products = [Product.Product(input(f'Product name ({_}): '), int(input(f'Product price ({_}): '))) for _ in range(1,limit + 1)]
        return Order.Order(customer, employee, *products, discount=apply_discount)

        
