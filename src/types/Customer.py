import enum
from typing import NamedTuple
from uuid import UUID

class TypesCustomer(enum.Enum):
    '''
    types for customer privilegies
    '''
    BASIC = enum.auto()
    PREMIUM = enum.auto()
    ELITE = enum.auto()

class CustomerDict(NamedTuple):
    name: str
    lastname: str
    email: str
    phone: str
    type: TypesCustomer = TypesCustomer.BASIC
    id: int | UUID = 0

