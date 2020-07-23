#1 Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”
'''
sample = "1234abcd"
print(sample[::-1])
# OR
sample = "1234abcd"
def sam():
    print(sample[::-1])

print(sam())


'''
# 2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

'''
x = input("enter some: ")

def somevale(x):
    count_u = 0
    count_l = 0
    for i in x:
        #print(i)
        if i.isupper():
            count_u += 1
            
            #print(i)
        else:
            count_l += 1
            
            #print(i)
    print(f"no of upper cases are : {count_u}")
    print("no of lower cases are: " , count_l)


somevale(x)
'''
# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
'''
# x = [1,20,5,7,70,1,50,70,30,20]
# y = [one, two, three, one]
# def unique(first):
#     new_list = []
#     for i in x:
#         if i in new_list:
#             continue
#         else:
#             new_list.append(i)

#     return new_list


# print(unique(x))  
''' 

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a
#  hyphen-separated sequence after sorting them alphabetically.
'''

u_input = list(input().split("-"))

def sorting(u_input):
    u_input.sort()
    return "-".join(u_input)


res = sorting(u_input)
print(res)
'''

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT
'''
x = int(input("number of sentences"))

def sent(x):
    ans = ""
    for l in x:
     ans = ans + l.upper()
    return ans

for i in range(x):
  uinput = input("Enter seq. of statements: ")
  print(sent(uinput))
'''
#6. Define a function that can receive two integral numbers in string form and compute their sum and print it in console.
'''
def sum():
    first_no = input("Enter the first number: ")
    second_no = input("Enter the second number: ")
    result = int(first_no) + int(second_no)
    return result


res = sum()
print(res)
'''
#7. Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line.
'''
def strm():
    str1 = input("Enter String1: ")
    str2 = input("Enter String2: ")
    if len(str1) > len(str2):
        print(" Maximum length string is: ", str1)
    elif len(str1) == len(str2):
        print(" Equal length: \n", str1, "\n", str2)
    else:
        print(" Maximum length string is: ", str2)


strm()

'''

#8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
'''
def sq():
    demo_list = []
    for value in range(2,20):
        sq = value*value
        demo_list.append(sq)
        demo_tuple = tuple(demo_list)
    return demo_tuple


res = sq()
print(res)
'''

#9. Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
#Example: If the limit is 3 , it should print:
#0 EVEN
#1 ODD
#2 EVEN
#3 ODD
'''
limit = int(input("Enter the limit: "))

def showNumbers(limit):
    for no in range(0, limit+1):
        if no%2 == 0:
            print(no, "EVEN")
        else:
            print(no, "ODD")

showNumbers(limit)

'''
#10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
'''
x = []
for i in range(1,21):
    x.append(i)

def filtering(d):
    if d%2 == 0:
        return d

result_list = list(filter(filtering, x))
print(result_list)

'''
#11 Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
#Hints: Use map() to generate a list.
# Use filter() to filter elements of a list
# Use lambda to define anonymous functions
'''
prac = list(map(int, range(1,11)))

def even_number(n):
        if n%2 == 0:
            return n
    
filter_list = list(filter(lambda x:(x%2==0), prac))

print("The list of even numbers : ",filter_list)
#squared = lambda x: x*x
print("The squared list: ", list(map(lambda n:n*n, filter_list)))
'''
#12. Write a function to compute 5/0 and use try/except to catch the exceptions
'''
try:
    def compute():
        res = 5/0
        return res



    result = compute()
    print(result)

except ZeroDivisionError:
    print("The number in the denominator is zero, which is why it cannot be calculated....Sorry!")
'''

#13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#Goal : Turn [1,2,3,4,5,6,7] to 1234567 
'''
from functools import reduce

ex = [[1,2,3],[4,5],[6,7,8]]

result = (reduce((lambda x,y: x + y), ex))
print(result)
'''
# 14. (i) 

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

'''
Abv block of code prints 2 which is in the finally block
'''
# (ii) 
def a():
    try:
        f(x, 4)
    finally:

        print('after f')
    print('after f?')
a()

'''
The abv block of gives an error
'''
