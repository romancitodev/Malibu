import src.models as mods


class OrderGen:
    
    def make_order(self, customer: mods.Customer.CustomerBase, employee: mods.Employee.EmployeeBase, apply_discount: bool = False):
        limit = int(input("digit the number of products: "))
        products = [mods.Product.Product(input(f'Product name ({_}): '), int(input(f'Product price ({_}): '))) for _ in range(1,limit + 1)]
        return mods.Order.Order(customer, employee, *products, discount=apply_discount)

        
