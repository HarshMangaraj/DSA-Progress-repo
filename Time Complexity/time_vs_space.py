
#O of n^2 time complexity because it uses a nested loop to compare each element with every other element in the list. The outer loop runs n times and for each iteration of the outer loop, the inner loop also runs up to n times, resulting in n * n = n^2 comparisons in the worst case.

def duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if i != j and numbers[i] == numbers[j] :
                return True
    return False

numbers_list = [1, 2, 3, 4, 5, 2]
result = duplicates(numbers_list)

if result:
    print("Duplicates found in the list.")
else:    print("No duplicates found in the list.")