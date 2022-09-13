import abc
from src.models.Error import NotValidKeys
from src.utils.functions import generate_random_id 
from src.types.Employee import  EmployeeDict, TypesEmployee

class EmployeeBase(abc.ABC):
    
    def __init__(self, data: EmployeeDict) -> None:
        self.__id = generate_random_id()
        if not self.__check_data(data): raise NotValidKeys('keys of @data is not the spectated.')
        self.__data = data | {"id" : self.__id}

    def __check_data(self, data: EmployeeDict) -> bool:
        return all([x in data for x in ['username','password']])
    
    @property
    def employee_info(self):
        return self.__data


class EmployeeCashier(EmployeeBase):

    def __init__(self, data: EmployeeDict) -> None:
        super().__init__(data | {"type" : TypesEmployee.CASHIER})


class EmployeeSupervisor(EmployeeBase):

    def __init__(self, data: EmployeeDict) -> None:
        super().__init__(data | {"type" : TypesEmployee.SUPERVISOR})
