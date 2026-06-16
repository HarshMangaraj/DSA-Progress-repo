marks = [88,72,95,61,79]
# Creating an array (list) of marks

marks.append(85)
# Appending a new mark to the end of the list
print(marks)

marks.insert(2, 90)
# Inserting a mark at index 2 (third position)
print(marks)

marks.remove(61)
# Removing the mark with value 61 from the list
print(marks)

marks.pop(1)
# Removing the mark at index 1 (second position)
print(marks)

marks[1] = 75
# Updating the mark at index 1 to 75
print(marks)


# Arrays in Python are implemented as lists, which are dynamic and can hold elements of different types. They provide various methods for manipulation, such as appending, inserting, removing, and popping elements. Lists are mutable, meaning their contents can be changed after creation.


print(marks[0:3])

# Slicing the list to get the first three marks (index 0 to 2) it is o(k) where k is the number of elements in the slice. In this case, it will be O(3) which simplifies to O(1) since it's a constant number of elements.

# access can be done on any position in O(1) time, making it efficient for random access.
# inserting at end of the list is O(1) on average, while inserting at the beginning or middle is O(n) because it requires shifting elements.
# deletion if done from end then O(1) but if done from beginning or middle then O(n) because of shifting elements.

