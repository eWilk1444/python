"""
    custom exception
"""


class InvalidLevelError(Exception):
    """Exception raised for errors in the input level value.

    Attributes:
        level -- input level which caused the error
        message -- explanation of the error
    """

    def __init__(self, level, message="Level is not valid"):
        self.level = level
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.level} -> {self.message}'

# Example usage


def set_level(new_level):
    if not (1 <= new_level <= 100):  # Assuming level should be between 1 and 100
        raise InvalidLevelError(new_level)
    print(f"Setting level to {new_level}")


try:
    set_level(101)
except InvalidLevelError as e:
    print(f"Error: {e}")
