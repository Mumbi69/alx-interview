#!/usr/bin/python3
"""log parsing"""

import sys
import signal


def print_stats(total_size, status_counts):
    """Prints total file size and counts of each status code"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    """main class"""
    total_size = 0
    status_counts = {}
    line_count = 0

    def signal_handler(sig, frame):
        """handling the signal class"""
        print_stats(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            ip_address = parts[0]
            date = parts[3][1:]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if parts[5] != "GET" or parts[6] != "/projects/260" or parts[7] != "HTTP/1.1":
                continue

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        except (IndexError, ValueError):
            continue


if __name__ == "__main__":
    main()
