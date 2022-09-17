import abc
from src.types.Employee import  EmployeeDict, TypesEmployee
from src.utils.functions import generate_random_id
class EmployeeBase(abc.ABC):
    
    def __init__(self, data: EmployeeDict) -> None:
        self.__data = data

    
    @property
    def employee_info(self):
        return self.__data


class EmployeeCashier(EmployeeBase):

    def __init__(self, data: EmployeeDict) -> None:
        super().__init__(EmployeeDict(data.username, data.password, TypesEmployee.CASHIER, generate_random_id())) 


class EmployeeSupervisor(EmployeeBase):

    def __init__(self, data: EmployeeDict) -> None:
        super().__init__(EmployeeDict(data.username, data.password, TypesEmployee.SUPERVISOR, generate_random_id())) 
