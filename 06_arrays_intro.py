# Arrays are storing data in contigeous manner

# in other languages the array should hold similar types of data but in python we can hold different types of datas together also

# in other languages we can directly declare or use arrays but in python is not like this if we want to use array then there are two ways:

# 1> use python array module 2> Python numpy module u can use any one of this but the better option is numpy module as it has more functionality

# In python arrays are dynamic in default so we dont have to do separate memory management for it like in other languages

# arrays index start from 0 to n-1 so if we want to create an array of 5 elements then the indexes will be 0 1 2 3 4 and also we can access each index using example a[1] or arr[2] etc

# lets learn how to declare an array using array module in python and access the elements of the array

import array as arr
arr = arr.array("i", [1, 2, 3, 4, 5])

# here i is the type code which means integer and the second one is the array itself

print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

for i in range(0, len(arr)):
    print(arr[i], end=" ")
print()

# another way to import array is 

from array import array
arr = array("i", [1, 2, 3, 4, 5])
print(arr)


# Lets learn how to use the array module to perform various operations on the array like append insert delete 

# append - add the element to the end of the array
arr.append(6)
print(arr)

# insert - add the element to the specific index
arr.insert(0, 0)
print(arr)

# delete - delete the element from the specific index
arr.pop(0)
print(arr)

# delete - delete the element from the specific index
arr.remove(0)
print(arr)

# Lets learn how to use the numpy module to perform various operations on the array like append insert delete 

# pyrefly: ignore [missing-import]
from numpy import array as arr1
arr1 = arr1([1, 2, 3, 4, 5])
print(arr1)

arr1.append(6)
print(arr1)

arr1.insert(0, 0)
print(arr1)

arr1.pop(0)
print(arr1)

arr1.remove(0)
print(arr1)

# difference between both methods :
# array module is slower than numpy module and it has less functionality
# numpy module is faster than array module and it has more functionality

# why do we need array module or numpy module in python:
# 1. to perform fast operations on arrays
# 2. to perform various operations on arrays like append insert delete 
# 3. to perform various operations on arrays like append insert delete 

# why we attach prefix "# pyrefly: ignore [missing-import]" to the import statements:
# this is done to ignore the missing import error
# pyrefly is a static analysis tool that checks for missing imports


# question = "Given an array, find the maximum element in the array"


arr = arr.array("i", [1, 2, 3, 4, 5])

max_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print("Maximum element is:", max_element)


# approach 2 using numpy module


# pyrefly: ignore [missing-import]
from numpy import array as arr1
arr1 = arr1([1, 2, 3, 4, 5])

print("Maximum element is:", arr1.max())