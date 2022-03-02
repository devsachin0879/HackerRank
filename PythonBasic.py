### Task1

'''
Task
Given an integer, , perform the following conditional actions:

--> If  is odd, print Weird
-->If  is even and in the inclusive range of  to , print Not Weird
-->If  is even and in the inclusive range of  to , print Weird
-->If  is even and greater than , print Not Weird
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    

if n%2 != 0:
    print("Weird")
elif n%2 == 0 and (n>=2 or n<=5):
    print("Not Weird")
elif n%2==0 and (n>=6 and n<=20):
    print("Weird")
else:
    print("Not Weird")



### Task2

'''
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
-->The first line contains the sum of the two numbers.
-->The second line contains the difference of the two numbers (first - second).
-->The third line contains the product of the two numbers.
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)


### Task3

'''
The provided code stub reads two integers,a and b, from STDIN.

Add logic to print two lines. 
The first line should contain the result of integer division, a // b. 
The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.
'''

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)



#### Task4

'''
The provided code stub reads and integer,n, from STDIN. 
For all non-negative integers i<n, print i^2 
'''

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)



### Task 5

'''
Without using any string methods, try to print the following:
123....n
Note that "..." represents the consecutive values in between
'''

if __name__ == '__main__':
    n = int(raw_input())

    mylist = []
    for i in range(1,n+1):
        mylist.append(i)
        
    for j in mylist:
        print(j,end="")

### Task6

'''
An extra day is added to the calendar almost every four years as February 29,
and the day is called a leap day. 
It corrects the calendar for the fact that our planet takes approx 365.25 days 
to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
'''

def is_leap(year):
    leap = False
    
    if year%400 == 0 and year%100 ==0:
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap  = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))


### Task 7

'''
Let's learn about list comprehensions! 
You are given three integers x,y and z representing the dimensions of a cuboid 
along with an integer n.

Print a list of all possible coordinates given by (i,j,k) on a 3D grid 
where the sum of i+j+k is not equal to n.
0<=i<=x; 0<=j<=y; 0<=k<=z.
'''

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])


### Task8
'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score.
You are given n scores. 
Store them in a list and find the score of the runner-up.

The first line contains n. The second line contains an array A[]  of n integers
'''

def myfunc():
    n = int(input())
    arr = list(map(int, input()))
    
    print(type(arr))
    print(arr)
    
    z = max(arr)
    print(z)
    while z == max(arr):
        arr.remove(z)
        
    print(max(arr))

#### Task9

'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.
'''

lst = []
for i in range(int(input("Please enter a number: "))):
    name = input("Name: ")
    scores = float(input("Score: "))
    
    lst.append([name,scores])
    
    sorted_score = sorted([x[1] for x in lst])
    
second_lowest = sorted_score[1]

lowest_score = []
for i in lst:
    if second_lowest == i[1]:
        lowest_score.append(i[0])
        
for name in lowest_score:
    print(name)