from __future__ import division


def merge(left, right):
    result = []
    i, j = 0, 0

    # Sort elements into new bin
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remainder to the bin
    result += left[i:]
    result += right[j:]

    return result


def mergesort(values):
    if len(values) <= 1:
        return values

    # Get the index of the middle element
    mid_point = len(values) // 2

    # Divide the list
    left = mergesort(values[:mid_point])
    right = mergesort(values[mid_point:])

    return merge(left, right)
