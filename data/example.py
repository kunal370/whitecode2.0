def calculate_factorial(n):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number to calculate factorial for

    Returns:
        int: The factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


class StringUtils:
    """A collection of string utility functions"""

    @staticmethod
    def reverse_string(s):
        """
        Reverse a string.

        Args:
            s (str): The string to reverse

        Returns:
            str: The reversed string
        """
        return s[::-1]