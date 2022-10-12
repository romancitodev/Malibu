import abc
from src.types.Customer import CustomerDict, TypesCustomer
from  src.utils.functions import generate_random_id


class CustomerBase(abc.ABC):
    def __init__(self, data: CustomerDict) -> None:
        self.__data = data
    @property
    def customer_info(self) -> CustomerDict:
        return self.__data

    @property
    def avaiable_discount(self) -> float:
        discounts = {
            TypesCustomer.BASIC : 0.1,
            TypesCustomer.PREMIUM : 0.2,
            TypesCustomer.ELITE : 0.5
        }
        return discounts.get(self.customer_info.type, 0.0)


class CustomerBasic(CustomerBase):
    def __init__(self, data: CustomerDict) -> None:
        super().__init__(CustomerDict(data.name, data.lastname, data.email, data.phone, TypesCustomer.BASIC, generate_random_id()))

class CustomerPremium(CustomerBase):
    def __init__(self, data: CustomerDict) -> None:
        super().__init__(CustomerDict(data.name, data.lastname, data.email, data.phone, TypesCustomer.PREMIUM, generate_random_id()))

class CustomerElite(CustomerBase):
    def __init__(self, data: CustomerDict) -> None:
        super().__init__(CustomerDict(data.name, data.lastname, data.email, data.phone, TypesCustomer.ELITE,  generate_random_id()))

