import abc
from src.models.Error import NotValidKeys
from src.utils.functions import generate_random_id 
from src.types.Customer import CustomerDict, TypesCustomer


class CustomerBase(abc.ABC):
    
    def __init__(self, data: CustomerDict) -> None:
        self.__id = generate_random_id()
        self.__data = data
        self.__data.update({'id': self.__id})
        if not self.__check_data(data): raise NotValidKeys('keys of @data is not the spectated.')

    def __check_data(self, data: CustomerDict) -> bool:
        return all([x in data for x in ['name','lastname','email','phone']])

    @property
    def customer_info(self):
        return self.__data

    @property
    def avaiable_discount(self):
        discounts = {
            TypesCustomer.BASIC : 0.1,
            TypesCustomer.PREMIUM : 0.2,
            TypesCustomer.ELITE : 0.5
        }
        return discounts.get(self.customer_info['type'], 0.0) 


class CustomerBasic(CustomerBase):
    def __init__(self, data: CustomerDict) -> None:
        super().__init__(data | {"type":TypesCustomer.BASIC})

class CustomerPremium(CustomerBase):
    def __init__(self, data: CustomerDict) -> None:
        super().__init__(data | {"type": TypesCustomer.PREMIUM})

class CustomerElite(CustomerBase):
    def __init__(self, data: CustomerDict) -> None:
        super().__init__(data | {"type": TypesCustomer.ELITE})