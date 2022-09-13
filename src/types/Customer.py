from typing import NewType
import enum

class TypesCustomer(enum.Enum):
    '''
    types for customer privilegies
    '''
    BASIC = enum.auto()
    PREMIUM = enum.auto()
    ELITE = enum.auto()

CustomerDict = NewType('CustomerDict', dict)
'''
    name: str,
    lastname: str
    email: ValidEmail
    phone: str
'''
