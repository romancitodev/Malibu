from typing import Any
import src.models as mods
import src.types as types

class App:
    '''
    @TODO: aggregate plugins like (Validator, Login)
    '''
    listener = None
    def __init__(self) -> None:
        self.__validator = mods.Validator.Validator()
        self.__employee: mods.Employee.EmployeeBase | None  = None
    #type: ignore
    def __test_login(self, credentials: types.Employee.EmployeeDict = {}, level: int = 1):
        employees = {1: mods.Employee.EmployeeCashier,2: mods.Employee.EmployeeSupervisor}
        if credentials:
            try:
                for k, v in credentials.items():
                    if not self.__validator.validate(k, v):
                        raise mods.Error.InvalidRegistry(f'Invalid key or string:\n{k} - {v}')
                self.__employee = employees[level](credentials)
                print("[+] Login succesfully")
            except Exception as e:
                print("[-] Error on login:")
                print(e)
        else:
            try:
                for c in ['username','password']:
                    string = input(f'{c}: ')
                    if not self.__validator.validate(c, string):
                        raise mods.Error.InvalidRegistry(f'Invalid string:\n{string}')
                    credentials.update({c: string})
                self.__employee = employees[level](credentials)
    
            except Exception as e:
                print(e)
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
            order_generator = mods.OrderMaker.OrderGen()
            customer_credentials: dict[str, Any] = {}
            for c in ['name','lastname','email','phone']:
                        string = input(f'{c}: ')
                        if not self.__validator.validate(c, string):
                            raise mods.Error.InvalidRegistry(f'Invalid string:\n{string}')
                        customer_credentials.update({c: string})
            order = order_generator.make_order(self.__add_customer(customer_credentials), self.__employee)
            if self.listener != None:
                self.listener.run_event('NewOrder',order=order)
            print('[+] Order generated')
    
    def start(self, credentials: types.Employee.EmployeeDict = {}, level: int = 1):
        print("[!] setuping listener...")
        try:
            self.listener = mods.EventManager.EventManager().setup('./src/events')
            print('[+] listener OK')
        except Exception as e:
            print(f'[-] listener started with failures.\n[>] {e}')
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
                continue
            else:
                return opt
    
    def main(self):
        functions = {1: self.__add_order, 2: exit}
        option = self.choose_option()
        functions[option]()