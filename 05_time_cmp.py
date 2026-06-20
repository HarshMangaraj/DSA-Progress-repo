# 1 -> constant time complexity

x = 5 ;
print("the value of x is : ", x)


#here the time complexity of this code is O(1) which is constant time complexity because the value of x is constant and does not depend on any variable.

# why is it constant it is because we are not takiing any input from user and not using any for loop or while loop or any other loop to take input from user and the value of x is constant and does not depend on any variable.

#if else statement is also constant time complexity because it executes a fixed number of operations regardless of the input size.


# 2 -> linear time complexity

# example y = 2x + 5, y = 3x + 10, y = 4x + 1000

# o(n) which is linear time complexity because the value of y is linear and depends on the variable x.

x = 5

for i in range (0, x):
    print("the value of i is : ", i)


# here the time complexity of this code is O(n) which is linear time complexity because the value of y is linear and depends on the variable x which is 5 as the x value increases in an linear manner.

# how  is it related to the equation suppose x =5 takes 1 unit of time then seccond line print(x) takes 1 unit of time then the for loop takes n units of time because it runs n times and the print statement inside the for loop takes n unit of time so the total is 1+1+n+n which is 2n + 2 so it see wee solved to show linear equation.