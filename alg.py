# Original brute-force approach

def find_element(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Suggested binary search approach

import bisect

def optimized_find_element(data, target):
    index = bisect.bisect_left(data, target)
    if index < len(data) and data[index] == target:
        return index

    return -1