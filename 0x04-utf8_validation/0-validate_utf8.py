#!/usr/bin/python3
"""The function validUTF8 module"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing 1 byte of data each.
    :return: True if data is a valid UTF-8 encoding, else return False.
    """
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    def is_follow_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        if (data[i] & 0b10000000) == 0b00000000:
            i += 1
        elif (data[i] & 0b11100000) == 0b11000000:
            if i + 1 < len(data)\
                    and is_follow_byte(data[i + 1]):
                i += 2
            else:
                return False
        elif (data[i] & 0b11110000) == 0b11100000:
            if i + 2 < len(data)\
                    and is_follow_byte(data[i + 1])\
                    and is_follow_byte(data[i + 2]):
                i += 3
            else:
                return False
        elif (data[i] & 0b11111000) == 0b11110000:
            if i + 3 < len(data)\
                    and is_follow_byte(data[i + 1])\
                    and is_follow_byte(data[i + 2])\
                    and is_follow_byte(data[i + 3]):
                i += 4
            else:
                return False
        else:
            return False

    return True
