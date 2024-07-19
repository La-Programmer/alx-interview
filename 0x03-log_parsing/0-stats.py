#!/usr/bin/env python3
"""LOG PARSING FOR STATS"""

import signal
import re
import sys
from functools import partial
from typing import List


# GLOBAL VARIABLES
total_file_size: int = 0
no_by_status_code: dict = {}


def check_line_format(input_string: str) -> bool:
    """Confirm the format of the line read from stdin"""
    ip: str = '^((:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]).{0,1}){4}$'
    date1_regex: str = r'\[\d{4}-\d{2}-\d{2}'
    date2_regex: str = r'\d{2}:\d{2}:\d{2}.\d{6}\]'
    mid_string_regex1: str = r'"GET'
    mid_string_regex2: str = r'/projects/260'
    mid_string_regex3: str = r'HTTP/1.1"'
    status_code_regex: str = r'200|301|400|401|403|404|405|500'
    file_size_regex: str = r'(?:10[0-2][0-4]|[1-9][0-9]{2}|[1-9][0-9]|[1-9])\n'
    input_string_array: List[str] = input_string.split(' ')
    # print(f'checking {input_string_array[0]}')
    if re.fullmatch(ip, input_string_array[0]) is None:
        return False
    # print(f'checking {input_string_array[1]}')
    if re.fullmatch(r'-', input_string_array[1]) is None:
        return False
    # print(f'checking {input_string_array[2]}')
    if re.fullmatch(date1_regex, input_string_array[2]) is None:
        return False
    # print(f'checking {input_string_array[3]}')
    if re.fullmatch(date2_regex, input_string_array[3]) is None:
        return False
    # print(f'checking {input_string_array[4]}')
    if re.fullmatch(mid_string_regex1, input_string_array[4]) is None:
        return False
    # print(f'checking {input_string_array[5]}')
    if re.fullmatch(mid_string_regex2, input_string_array[5]) is None:
        return False
    # print(f'checking {input_string_array[6]}')
    if re.fullmatch(mid_string_regex3, input_string_array[6]) is None:
        return False
    # print(f'checking {input_string_array[7]}')
    if re.fullmatch(status_code_regex, input_string_array[7]) is None:
        return False
    # print(f'checking {input_string_array[8]}')
    if re.fullmatch(file_size_regex, input_string_array[8]) is None:
        return False
    return True


def get_file_size(input_string: str) -> int:
    """Get file size from log statement"""
    file_size: int = int(input_string.split(' ')[-1])
    return file_size


def get_number_of_lines_by_status_code(input_string: str,
                                       no_by_status_code: dict) -> None:
    """Get the number of lines of each status code"""
    status_codes: List[int] = [200, 301, 400, 401, 403, 404, 405, 500]
    status_code: int = int(input_string.split(' ')[-2])
    if status_code in status_codes:
        if status_code in no_by_status_code.keys():
            no_by_status_code[status_code] += 1
        else:
            no_by_status_code[status_code] = 1


def print_stats(total_file_size: int,
                no_by_status_code: dict) -> None:
    """Print out the current computed stats"""
    print(f'File size: {total_file_size}')
    for key, value in no_by_status_code.items():
        print(f'{key}: {value}')


def handler(signum, frame):
    """Signal Interrupt Handler"""
    print_stats(total_file_size, no_by_status_code)


def main() -> None:
    """Main Function"""
    line_count: int = 0
    global total_file_size
    global no_by_status_code
    # print("Signl handler initialised")
    # print("Line by Line processing has begun")
    for line in sys.stdin:
        line_count += 1
        # print(line)
        # print(check_line_format(line))
        if check_line_format(line):
            file_size = get_file_size(line)
            total_file_size += file_size
            get_number_of_lines_by_status_code(line,
                                               no_by_status_code)
            if line_count % 10 == 0 and line_count != 0:
                print_stats(total_file_size, no_by_status_code)


signal.signal(signal.SIGINT, handler)

if __name__ == '__main__':
    main()
