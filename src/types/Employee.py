import enum
from typing import NamedTuple
from uuid import UUID

class TypesEmployee(enum.Enum):
    '''
    types for customer privilegies
    '''
    CASHIER = enum.auto()
    SUPERVISOR = enum.auto()

class EmployeeDict(NamedTuple):
    username:str
    password:str
    type:TypesEmployee= TypesEmployee.CASHIER
    id: int | UUID = 0 