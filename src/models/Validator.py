import re
from src.validator.regex import Config
from src.models.Error import InvalidMode
from src.types.Validator import ValidConfig

class Validator:
    
    def __init__(self) -> None:
        self.__config = self.__load_config()

    def __load_config(self) -> dict:
        return Config

    def validate(self, mode: ValidConfig, string: str) -> bool:
        if mode not in ValidConfig:
            raise InvalidMode(f"Mode '{mode}' not supported, try another.")
        return bool(re.match(self.__config[mode], string))
