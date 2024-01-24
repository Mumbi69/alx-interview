#!/usr/bin/python3
"""Log parsing"""
from sys import stdin

status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
count = 0


def print_all_statistics():
    """Prints total file size and counts of each status code."""
    print("File size:", total_file_size)
    for key, value in status_code_counts.items():
        if value:
            print("{}: {}".format(key, value))


try:
    for line in stdin:
        count += 1

        try:
            line_parts = line.split(" ")
            status_code = int(line_parts[7])
            file_size = int(line_parts[8])
        except (IndexError, ValueError):
            continue

        status_code_counts[status_code] += 1
        total_file_size += file_size

        if count == 10:
            print_all_statistics()
            count = 0

    print_all_statistics()

except KeyboardInterrupt:
    print_all_statistics()
