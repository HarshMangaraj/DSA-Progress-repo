def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if i != j and numbers[i] == numbers[j] :
                return True
    return False

numbers_list = [1, 2, 3, 4, 5, 2]
result = find_duplicates(numbers_list)

if result:
    print("Duplicates found in the list.")
else:    print("No duplicates found in the list.")

    # This function uses a nested loop to compare each element with every other element, resulting in O(n^2) time complexity.