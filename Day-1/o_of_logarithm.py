def find_name(names, target):
    left = 0
    right = len(names) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if names[mid] == target:
            return mid
        elif names[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# This function uses binary search, which runs in O(log n) time.
# Each loop iteration halves the search range, so the number of steps
# grows logarithmically with the list size.