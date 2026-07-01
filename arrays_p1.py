from array import *
arr = array("i", [1, 2, 3, 4, 5])

for i in range(0, len(arr)):
    print(arr[i], end=" ")

# lets say if we want to take input for elements in the array from the user then we can do it like this
n = int(input("Enter the number of elements in the array: "))

# after taking the input for the number of elements in the array we can create an empty array and then take input for each element in the array and append it to the array

arr1 = array("i", [])

for i in range(n):
    arr1.append(int(input("Enter the element: "))) 

# here we are taking input for each element in the array and appending it to the array

for i in range(0, len(arr1)):
    print(arr1[i], end=" ")

# now we prrint the array using the print function