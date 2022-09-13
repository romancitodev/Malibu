from typing import NewType
import enum

class TypesEmployee(enum.Enum):
    '''
    types for customer privilegies
    '''
    CASHIER = enum.auto()
    SUPERVISOR = enum.auto()

EmployeeDict = NewType('EmployeeDict', dict)
'''
    username: str,
    passsword: ValidPassword
'''
