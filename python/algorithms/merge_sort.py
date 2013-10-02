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


def mergesort(lst):
    if len(lst) <= 1:
        return lst

    # Get the index of the middle element
    mid_point = len(lst) // 2

    # Divide the list
    left = mergesort(lst[:mid_point])
    right = mergesort(lst[mid_point:])

    return merge(left, right)


if __name__ == "__main__":
    print mergesort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5])
