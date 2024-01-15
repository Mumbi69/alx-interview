#!/usr/bin/python3
"""implementation for the minOperations function"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Parameters:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed, or 0 if
        impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1
        current_length += clipboard
        operations += 1

    return operations
