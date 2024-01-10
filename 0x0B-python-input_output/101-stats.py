#!/usr/bin/python3
"""
Script for computing metrics from input lines.
"""

import signal
import sys

def print_metrics(stats):
    """
    Prints the computed metrics.

    Args:
        stats (dict): Dictionary containing the metrics.
    """
    print("File size: {:d}".format(stats['total_size']))
    for code in sorted(stats['status_codes']):
        print("{}: {}".format(code, stats['status_codes'][code]))

def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).

    Args:
        sig: Signal number.
        frame: Current stack frame.
    """
    print_metrics(stats)
    sys.exit(0)

def parse_line(line):
    """
    Parses a line to extract relevant information.

    Args:
        line (str): Input line.

    Returns:
        tuple: Tuple containing status code and file size.
    """
    parts = line.split()
    return int(parts[-2]), int(parts[-1])

if __name__ == "__main__":
    stats = {'total_size': 0, 'status_codes': {}}
    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            stats['total_size'] += file_size

            if status_code in stats['status_codes']:
                stats['status_codes'][status_code] += 1
            else:
                stats['status_codes'][status_code] = 1

            if line_count % 10 == 0:
                print_metrics(stats)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
