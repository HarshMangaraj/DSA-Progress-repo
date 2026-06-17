marks = [88,72,95,61,79]

for mark in marks:
    print(mark)

for i in range(len(marks)):
    print(marks[i])

#two ways to traverse an array from left to right

for mark in reversed(marks):
    print(mark)

for mark in marks[::-1]:
    print(mark)

for i in range(len(marks)-1, -1, -1):
    print(marks[i])

#three ways to traverse an array from right to left
