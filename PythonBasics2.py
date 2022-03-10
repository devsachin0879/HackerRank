### Task1
'''
Minion Game
1:- Both players are given the same string S.
2:- Both players have to make substrings using the letters of the string S.
3:- Stuart has to make words starting woth consonants.
4:- Kevin has to make words starting with vowel.
5:- The game ends when both players have made all possible substrings.
Player gets +1 point for each occurence of the substring in the String S
'''
def minion(string):
    vow = "AEIOU"
    k = 0
    s = 0
    for i in range(len(string)):
        if string[i] in vow:
            ###let string  = BANANA
            ### string[0] = B len(string) - i ==> 6-0 = 6(BANANA) --S
            ### string[1] = A len(string) -i ==> 6-1 = 5(ANANA) -- K
            ### string[2] = N len(string) -i ==> 6-2 = 4(NANA)--- S
            ### string[3] = A len(string) -i ==> 6-3 = 3(ANA)--- K
            ### string[4] = N len(string) -i ==> 6-4 = 2(NA)--- S
            ### string[5] = A len(string) -i ==> 6-5 = 1(A)--- K
            k += len(string) - i
        else:
            s += len(string) - i
    if k > s:
        print("Kevin: ",k)
    elif k < s:
        print("Stuart: ",s)
    else:
        print("Draw")


### Task2
'''
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.
'''

import itertools

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

print(*itertools.product(A,B))

#### OR ####

A = list(input().split())
B = list(input().split())

lst = []
for i in A:
    for j in B:
        lst.append((int(i),int(j)))



### Task3
'''
You are given a string S.
Your task is to print all possible permutations of size k 
of the string in lexicographic sorted order.
'''

from itertools import permutations
string,num = input().split()
for i in permutations(sorted(string),int(num)):
    print(*[''.join(i)],sep = "\n")




### Task4
'''
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of all the plants 
with distinct heights in her greenhouse.
'''
def average(array):
    # your code goes here
    s = set(array)
    total = 0
    for i in s:
        total += i
        
    average = total/len(s)
    return average



####Task5
T = int(input("Please enter number of test cases: "))
for i in range(T):
    a,b = map(int,input().split())
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print("Error Code",e)


### Task6
'''
Dr. John Wesley has a spreadsheet containing a list of 
student's IDs,marks,class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.
Note:
1. Columns can be in any order. IDs, marks, class and name 
can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. 
(The spelling and case type of these names won't change.)
Print the average marks of the list corrected to 2 decimal places.
'''

from collections import namedtuple
n = int(input())
fields = input().split()
total = 0

for i in range(n):
    students = namedtuple("Students",fields)
    field1,field2,field3,field4 = input().split()
    student = students(field1,field2,field3,field4)
    total += int(student.MARKS)
avg = total/n
print("{:.2f}".format(avg))
