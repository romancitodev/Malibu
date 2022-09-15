import enum
from typing import Any

class TypesEmployee(enum.Enum):
    '''
    types for customer privilegies
    '''
    CASHIER = enum.auto()
    SUPERVISOR = enum.auto()

EmployeeDict = dict[str, Any]

'''
    username: str,
    passsword: ValidPassword
'''
