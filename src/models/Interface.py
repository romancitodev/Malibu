from typing import Any

import src.models as mods
import src.types as types
from src.types.Customer import TypesCustomer


class App:
    '''
    @TODO: aggregate plugins like (Validator, Login)
    '''
    listener = None
    def __init__(self) -> None:
        self.__validator = mods.Validator.Validator()
        self.__employee: mods.Employee.EmployeeBase | None  = None
    
    def __test_login(self, credentials: types.Employee.EmployeeDict, level: int = 1):
        employees = {1: mods.Employee.EmployeeCashier,2: mods.Employee.EmployeeSupervisor}
       
        v = {'username': credentials.username, 'password': credentials.password}
        try:
            for k in v:
                if not self.__validator.validate(k, v[k]):
                    raise mods.Error.InvalidRegistry(f'Invalid key or string:\n{k} - {v[k]}')
            self.__employee = employees[level](credentials)
            print("[+] Login succesfully")
        except AttributeError as e:
            print("[-] Error on login:")
            print(e)
            exit()
        if self.listener != None:
            self.listener.run_event('NewEmployee', self.__employee)

    def __add_customer(self, customer_credentials: types.Customer.CustomerDict, level: int = 1) -> mods.Customer.CustomerBase:
        customers = {1: mods.Customer.CustomerBasic, 2: mods.Customer.CustomerPremium, 3: mods.Customer.CustomerElite}
        customer = customers[level](customer_credentials)
        if self.listener != None:
            self.listener.run_event('NewCustomer', customer)
        print('[+] Customer aggregated')
        return customer

    def __add_order(self):
        if self.__employee != None:
            order_generator = mods.OrderMaker.OrderMaker()
            customer_credentials :dict[str, Any] = {}  
            for c in ['name','lastname','email','phone']:
                        string = input(f'{c}: ')
                        if not self.__validator.validate(c, string):
                            raise mods.Error.InvalidRegistry(f'Invalid string:\n{string}')
                        customer_credentials.update({c: string})
            discount = input("[>] Apply discount? : ").lower() in "yes"
            customer_types = {1: TypesCustomer.BASIC, 2:TypesCustomer.PREMIUM, 3: TypesCustomer.ELITE}
            customer_type = int(input("[>] Membership of customer: "))
            customer_credentials.update({"type": customer_types[customer_type]})
            print(customer_credentials)
            order = order_generator.make_order(self.__add_customer(types.Customer.CustomerDict(**customer_credentials), customer_credentials['type'].value), self.__employee, discount)
            if self.listener != None:
                self.listener.run_event('NewOrder', order)
            print('[+] Order generated')
    
    def start(self, credentials: types.Employee.EmployeeDict, level: int = 1):
        print("[!] setuping listener...")
        try:
            self.listener = mods.EventManager.EventManager().setup('./src/events')
            print('[+] listener OK')
        except Exception as e:
            print(f'[-] listener started with failures.\n\t* {e}')
        self.__test_login(credentials, level)
        self.main()

    def choose_option(self) -> int:
        AO = mods.AppOptions.AvaiableOptions
        options = {AO.CREATE_ORDER: "Create new order.", AO.EXIT: "Exit."}
        while True:
            for [key, value] in options.items():
                print(f"{key.value}. {value}")
            opt = int(input("Select a choice: "))
            if opt not in [x.value for x in options.keys()]:
                print(f"{opt} not valid.")
                continue
            else:
                return opt
    
    def main(self):
        while True:
            functions = {1: self.__add_order, 2: exit}
            option = self.choose_option()
            functions[option]()