#!/usr/bin/env python3
"""Log parsing"""
import sys
import signal


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
lines_processed = 0


def print_statistics():
    """represents print statistics"""
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


def signal_handler(sig, frame):
    """represents signal handler"""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) == 10 and parts[5].isdigit() and parts[8].isdigit():
            status_code = int(parts[8])
            file_size = int(parts[9])

            total_file_size += file_size

            status_code_counts[status_code] += 1

            lines_processed += 1

            if lines_processed % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
