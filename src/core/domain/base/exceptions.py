class OperationalException(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)


class InvalidEmailError(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)
