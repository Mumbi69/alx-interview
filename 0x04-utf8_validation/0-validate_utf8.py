#!/usr/bin/python3
"""The function validUTF8 module"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Representation of validUTF8 function"""
    count = 0
    for s in data:
        binary = bin(s)[2:].zfill(8)
        if binary.startswith("0") and count == 0:
            continue
        if binary.startswith("110") and count == 0:
            count = 1
            continue
        if binary.startswith("1110") and count == 0:
            count = 2
            continue
        if binary.startswith("11110") and count == 0:
            count = 3
            continue
        if binary.startswith("10") and count > 0:
            count -= 1
            continue
        return False
    return count == 0
