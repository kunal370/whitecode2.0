def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms to generate

    Returns:
        list: List containing Fibonacci sequence
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): Number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True