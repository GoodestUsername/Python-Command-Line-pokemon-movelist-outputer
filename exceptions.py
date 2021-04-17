"""
Module contains custom exceptions.
"""


class InvalidObjectException(Exception):
    """
    Custom exception class for invalid objects.
    """
    def __init__(self, name: str):
        """
        Constructor.
        :param name: Error message.
        """
        super().__init__()
        self.name = name

    def __str__(self):
        """
        toString method.
        :return: String representation of this instance.
        """
        return f'Invalid Object: "{self.name}"'
