#!/usr/bin/python3
"""Check for valid UTF-8 code point"""

from typing import List
import re
# - check if the binary representation of the integer is a multiple of 8
# - if it is not a multiple of 8 pad it with zeros till it is
# - divide the binary string into an array of sets of 8 characters
# - no. of bytes = length(binary_string)/8
# - if no. of bytes > 6 return false
# - if no. of bytes == 1
# - check that the first character of the first byte is 0
# - else use regex to check that the first byte
# is 1[no. of bytes - 1]0/d[8 - no. of bytes]
# - check that every other byte (member of the array) follow the format 10/d[6]


def is_integer_valid_utf(input_int: int) -> bool:
    """Checks if an integer is valid UTF-8 code point"""
    if input_int < 0:
        return False
    binary_str: str = bin(input_int)[2:]
    byte_no_mod: int = len(binary_str) % 8
    if (byte_no_mod != 0):
        pad_zeros: str = '0' * (8 - byte_no_mod)
        binary_str = pad_zeros + binary_str
    byte_sets: List[str] = split_string_into_eight_sets(binary_str)
    byte_no: int = int(len(binary_str) / 8)
    if byte_no > 6:
        return False
    if byte_no == 1 and byte_sets[0][0] != '0':
        return False
    elif byte_no > 1:
        byte_str: str = str(byte_no)
        remainder: str = str(8 - byte_no - 1)
        first_byte_regex = r'1{' + byte_str + r'}0\d{' + remainder + r'}'
        continuation_bytes_regex = r'10\d{6}'
        if re.fullmatch(first_byte_regex, byte_sets[0]) is None:
            return False
        for i in range(1, len(byte_sets)):
            if not re.fullmatch(continuation_bytes_regex, byte_sets[i]):
                return False
    return True


def split_string_into_eight_sets(binary_str: str) -> List[str]:
    """Split a binary string into eight characters each"""
    byte_no: int = len(binary_str)
    byte_sets: List[str] = []
    while byte_no > 8:
        byte: str = binary_str[0:9]
        byte_sets.append(byte)
        binary_str = binary_str[9:]
        byte_no = len(binary_str)
    byte_sets.append(binary_str)
    return byte_sets


def validUTF8(data: List[int]) -> bool:
    """Validate a list of integers for UTF-8"""
    are_all_valid: List[bool] = [
        is_integer_valid_utf(number) for number in data
    ]
    return all(are_all_valid)
