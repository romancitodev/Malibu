from src.utils.functions import generate_random_id


class Product:
    """Class that represents a product"""
    def __init__(self, name: str, price: int) -> None:
        self.__id = generate_random_id()
        self.__name = name
        self.__price = price
    
    """Read Only properties"""
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
