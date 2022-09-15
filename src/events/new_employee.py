

# from typing import Any
from src.models.Event import Event
from src.models.Employee import EmployeeBase


class NewEmployee(Event):
    '''
    NewEmployee Event
    '''
    def __init__(self, name_event: str) -> None:
        super().__init__(name_event)
    
    def run(self, employee: EmployeeBase) -> None: #type: ignore
        self.logging.info(' Employee logged  '.center(50, '-'))
        self.logging.info(f'[Employee]: {employee.employee_info.get("username","").capitalize()}')
        self.logging.info(f'[Employee]: {employee.employee_info.get("type")}') 
        self.logging.info(f'[Employee]: {employee.employee_info.get("id")}')