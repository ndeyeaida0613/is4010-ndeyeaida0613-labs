def factorial(n):
    """Calculate the factorial of a non-negative integer.
    Parameters
    ----------
    n : int
        A non-negative integer to calculate the factorial of.
        Returns
        -------
        int
            The factorial of n. Returns 1 if n is 0.
        Examples
        --------
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(num):
    """Check if a number is prime.
    Parameters
    ----------
    num : int
        An integer to check for primality.
        Returns
        -------
        bool
            True if num is prime, False otherwise.
        Examples
        --------
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False"""
    
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_string(s):
    """Reverse a given string.
    Parameters
    ----------
    s : str
        The string to be reversed.
        Returns
        -------
        str
            The reversed string.
        Examples
        --------
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'"""
    return s[::-1]



    






