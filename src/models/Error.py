
class Errors(Exception):
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.error_mesage = message

class NotValidKeys(Errors):
    
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidMode(Errors):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidRegistry(Errors):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NotStarted(Errors):
    def __init__(self, message: str) -> None:
        super().__init__(message)