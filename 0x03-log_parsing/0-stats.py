#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys

# Initialize variables to store metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


# Read input line by line
for line in sys.stdin:
    # Check if line matches the specified format
    parts = line.split()
    if len(parts) != 6:
        continue
    ip, date, request, status, code, size = parts
    status_code = int(code)
    # Check if status code is in the list of possible codes
    if status_code not in status_codes:
        continue
    # Update metrics
    total_size += int(size)
    status_codes[status_code] += 1
    line_count += 1
    # Print metrics every 10 lines
    if line_count % 10 == 0:
        print("Total file size: ", total_size)
        for code in sorted(status_codes):
            print(f"{code}: {status_codes[code]}")
