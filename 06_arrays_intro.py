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
