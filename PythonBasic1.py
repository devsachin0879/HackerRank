#### Task1
'''
You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following:
'''

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")



#### Task 2
'''
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
'''

def myfunc(string,sub_string):
    counter = 0
    j = len(sub_string)
    for i in range(len(string)):
        if string[i:i+j] == sub_string:
            counter += 1
    return counter


#### Task 3
'''
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters & vice versa.

eg:= Pythonist 2 → pYTHONIST 2 
'''

def swap_cases(string):
    mystring = []
    for i in range(len(string)):
        if string[i] == string[i].upper():
            mystring.append(string[i].lower())
        else:
            mystring.append(string[i].upper())
    return "".join(mystring)


### Task4
'''
You are given a string. 
Split the string on a " " (space) delimiter and join using a - hyphen.
'''

def split_and_join(line):
    a = line.split(" ")
    return "-".join(a)


#### Task5
'''
You are asked to ensure that the first and last names of people 
begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.
'''

def solve(s):
    a = s.split(" ")
    b = []
    for i in a:
        b.append(i.capitalize())
    return " ".join(b)


#### Task6
'''
We have seen that lists are mutable (they can be changed), 
and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.
'''
def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return "".join(string)


#### Task7
'''
You are given a string S.
Your task is to find out if the string S contains:
alphanumeric characters, alphabetical characters, 
digits, lowercase and uppercase characters.
'''

###The any() function returns True if any item in an iterable are true, otherwise it returns False

def myfunc():
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))



#### Task 8 
'''
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
'''
import textwrap
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string,max_width))

##----------OR-----------
import textwrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width = max_width)
    word_list = wrapper.wrap(text = string)
    
    for word in word_list:
        print(word)


#### Task9
'''
You are given a partial code that is used for generating the HackerRank Logo 
of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
'''

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))




#### Task10
'''
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''

N, M = map(int,input().split())
for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))


#### Task11
'''
Given an integer, n, print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary
'''

n = int(input("Please enter a number: "))
w = len(str(bin(n)).replace("0b",''))

for i in range(1,n+1):
    b = bin(i).replace('0b','').rjust(w,' ')
    o = oct(i).replace('0o','').rjust(w,' ')
    h = hex(i).replace('0x','').upper().rjust(w,' ')
    j = str(i).rjust(w,' ')
    print(j,o,h,b)


### TASK12
'''
The provided code stub will read in a dictionary containing key/value pairs of 
name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, 
showing 2 places after the decimal.
''' 

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
student_name = input("Please enter student name: ")

if student_name in student_marks.keys():
    marks = 0
    for i in student_marks[student_name]:
        marks += i
    result = marks/len(student_marks[query_name])
    
    print("{:.2f}".format(result))



#### Task13
'''
Given an interger n and n spced-seperated integers as input,
create a tuple t of those n intergers.
Then compute and print the result of hash(t).
'''

n = int(input())
## using map to convert input to int and splitting by whitespace
integer_list = map(int, input().split()) 
mytuple = tuple(integer_list)
print(hash(mytuple))


