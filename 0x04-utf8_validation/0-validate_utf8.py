#!/usr/bin/python3
"""The function validUTF8 module"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Representation of validUTF8 function"""
    count = 0

    for byte in data:
        binary_representation = format(byte, '08b')

        if binary_representation.startswith("0") and count == 0:
            continue
        elif binary_representation.startswith("110") and count == 0:
            count = 1
        elif binary_representation.startswith("1110") and count == 0:
            count = 2
        elif binary_representation.startswith("11110") and count == 0:
            count = 3
        elif binary_representation.startswith("10") and count > 0:
            count -= 1
        else:
            return False

    return count == 0
