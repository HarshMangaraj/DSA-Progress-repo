def has_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

numbers_list = [1, 2, 3, 4, 5, 2]
result = has_duplicate(numbers_list)

if result:
    print("Duplicates found in the list.")
else:    print("No duplicates found in the list.")

    # This function uses a set to track seen numbers, which allows for O(1) average time complexity for lookups and insertions. The overall time complexity is O(n) because we iterate through the list once, and the space complexity is also O(n) in the worst case if all numbers are unique.