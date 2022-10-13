import re

from src.models.Error import InvalidMode
from src.types.Validator import ValidConfig
from src.validator.regex import Config


class Validator:
    
    def __init__(self) -> None:
        self.__config = self.__load_config()

    def __load_config(self) -> dict[str, str]:
        return Config

    def validate(self, mode: str, string: str) -> bool:
        if mode not in ValidConfig:
            raise InvalidMode(f"Mode '{mode}' not supported, try another.")
        return bool(re.match(self.__config[mode], string))
