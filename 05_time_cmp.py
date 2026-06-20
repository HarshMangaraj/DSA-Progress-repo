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





# 4 -> CUBIC TIME COMPLEXITY





n = 5;
m = 10;

for i in range (0, n):
    for j in range (0, m):
        for k in range (0, n):
            print("the value of i is : ", i, " and the value of j is : ", j, " and the value of k is : ", k)

# here the time complexity of this code is O(n^3) why because the first line n = 5 takes 1 unit of time then the second line m = 10 takes 1 unit of time then the first loop takes n units of time because it runs n times and then the loop inside the first loop takes m units of time because it runs m times but on an assumption we can say the both loops will run n times outside then n times inside so it is n*n which is n^2 and then the third loop takes n units of time because it runs n times so the total time complexity of this code is O(n^3) which is cubic time complexity.

# so on an average lets say if 3 loops ran n times then n*n*n which is n^3 so the total time complexity of this code is O(n^3) which is cubic time complexity.

# lets take an tough example suppose:

n = 5
if (n ==5):
    for i in range (0, n):
        for j in range (0, n):
            print("the value of i is : ", i, " and the value of j is : ", j)
else:
    for i in range (0, n):
        for j in range (0, n):
            for k in range (0, n):
                print("the value of i is : ", i, " and the value of j is : ", j, " and the value of k is : ", k)

# here the time complexity we are gonna take is o(n^3) why because we always take the worst case time complexity of an algorithm because it is the most important and most used time complexity in real world applications thats why we often use big O notation to denote time complexity of an algorithm.

# here we know that the if else statement is constant time complexity because it executes a fixed number of operations regardless of the input size. so we can ignore the if else statement and take the worst case time complexity which is O(n^3) which is cubic time complexity.




# 5 -> Logorithmic time complexity




# here the equation is y = log(x) + 5x^2 + 10x + 100, y = log(x) + 3x^2 + 1000, y = log(x) + 10x^2 + 10000 here the dominating part is log(x) so the time complexity of this equation is O(log n) which is logarithmic time complexity.

n = 10 
while (n > 1):
    print("the value of n is : ", n)
    n = n // 2

# here the time complexity of this code is O(log n) which is logarithmic time complexity because the value of y is logarithmic and depends on the variable x which is 10 as the x value increases in an logarithmic manner.

# how because the first line n = 10 takes 1 unit of time then the while loop takes log n units of time because it runs log n times and the print statement inside the while loop takes log n unit of time so the total is 1+log n+log n which is 2log n + 1 so we can say that the time complexity of this code is O(log n) which is logarithmic time complexity.

# what is log in simple words log is the number of times we have to divide a number by 2 to get 1. for example if we have a number 8 then we have to divide it by 2 three times to get 1 so log(8) = 3. if we have a number 16 then we have to divide it by 2 four times to get 1 so log(16) = 4. if we have a number 32 then we have to divide it by 2 five times to get 1 so log(32) = 5. and so on.

# for odd numbers we can take the floor value of log. for example if we have a number 7 then we have to divide it by 2 two times to get 1 so log(7) = 2. if we have a number 15 then we have to divide it by 2 three times to get 1 so log(15) = 3. if we have a number 31 then we have to divide it by 2 four times to get 1 so log(31) = 4. and so on.

# we often say o(k) where k is the number of times we have to divide a number by 2 to get 1.

# // is different from / because // is floor division which means it will give the quotient of the division and ignore the remainder. for example if we have a number 7 then 7//2 = 3 and 7/2 = 3.5. if we have a number 15 then 15//2 = 7 and 15/2 = 7.5. if we have a number 31 then 31//2 = 15 and 31/2 = 15.5. and so on.

# in simple words if ur loops is getting divided or getting halved then it is logarithmic time complexity.

# it also can be opposite or reverse like 
n =1
while (n < 10):
    print("the value of n is : ", n)
    n = n * 2
# here the time complexity of this code is O(log n) which is logarithmic time complexity because the value of y is logarithmic and depends on the variable x which is 10 as the x value increases in an logarithmic manner.

# but how because here the first line n = 1 takes 1 unit of time then the while loop takes log n units of time because it runs log n times and the print statement inside the while loop takes log n unit of time so the total is 1+log n+log n which is 2log n + 1 so we can say that the time complexity of this code is O(log n) which is logarithmic time complexity.

# how logn because the first time n = 1 then second time n = 2 then third time n = 4 then fourth time n = 8 then fifth time n = 16 so it is log(16) = 4 so the while loop runs log n times so the total time complexity of this code is O(log n) which is logarithmic time complexity.

# in simple words multiplying by 2 is the same as dividing by 2 in reverse so it is logarithmic time complexity.

# hence if u see a loop which is getting divided or getting halved then it is logarithmic time complexity and if u see a loop which is getting multiplied by 2 then it is also logarithmic time complexity.