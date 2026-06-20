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

# how to find linear time complexity within 30 seconds suppose the code is like above code here find the dominating part or the part which will take the most time to execute in this case it is the for loop because it runs n times and the print statement inside the for loop takes n unit of time so the total is 1+1+n+n which is 2n + 2 so it see wee solved to show linear equation. so the dominating part is n so we can say that the time complexity of this code is O(n) which is linear time complexity.

# lets take another example of linear time complexity suppose we have a code like this

n = 5
for i in range (0, n):
    print("the value of i is : ", i)
for j in range (0, n):
    print("the value of j is : ", j)
for k in range (0, n):
    print("the value of k is : ", k)

# here the time complexity of this code is O(n) which is linear time complexity because the value of y is linear and depends on the variable x which is 5 as the x value increases in an linear manner.

# how because first line n = 5 takes 1 unit of time then the first loop takes n units of time because it runs n times and the print statement inside the first for loop takes n unit of time so the total is 1+n+n which is 2n + 1 then the second loop takes n units of time because it runs n times and the print statement inside the second for loop takes n unit of time so the total is 1+n+n which is 2n + 1 then the third loop takes n units of time because it runs n times and the print statement inside the third for loop takes n unit of time so the total is 1+n+n which is 2n + 1 so the total time complexity of this code is 2n + 1 + 2n + 1 + 2n + 1 which is 6n + 3 so we can say that the time complexity of this code is O(n) which is linear time complexity.


# 3 -> QUADRATIC TIME COMPLEXITY

# here the equation is y = x^2 + 5x + 10, y = 2x^2 + 3x + 1000, y = 4x^2 + 10x + 10000 here the dominating part is x^2 so the time complexity of this equation is O(n^2) which is quadratic time complexity.

n = 5;
m = 10;

for i in range (0, n):
    for j in range (0, m):
        print("the value of i is : ", i, " and the value of j is : ", j)

# here the time complexity of this code is O(n^2) which is quadratic time complexity because the value of y is quadratic and depends on the variable x which is 5 as the x value increases in an quadratic manner.

# how because the first line n = 5 takes 1 unit of time then the second line m = 10 takes 1 unit of time then the first loop takes n units of time because it runs n times and then the loop inside the first loop takes m units of time because it runs m times but on an assumption we can say the both loops will run n times outside then n times inside so it is n*n which is n^2 so the total time complexity of this code is O(n^2) which is quadratic time complexity.

# why n * n because the first loop runs n times and for each iteration of the first loop the second loop runs n times so it is n*n which is n^2 so the total time complexity of this code is O(n^2) which is quadratic time complexity.