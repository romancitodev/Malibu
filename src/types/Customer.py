import enum
from typing import Any

class TypesCustomer(enum.Enum):
    '''
    types for customer privilegies
    '''
    BASIC = enum.auto()
    PREMIUM = enum.auto()
    ELITE = enum.auto()

CustomerDict = dict[str, Any]
'''
    name: str,
    lastname: str
    email: ValidEmail
    phone: str
'''
