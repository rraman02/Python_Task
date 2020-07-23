#1 Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
x = [1,2,3.20,1+2j,"rucha"]
print(x)

#2 Create a list of size 5 and execute the slicing structure 
x = [0,1,2,3,4,5]
left:right
print(x[:])
#left:
print(x[0:])
#:right
print(x[:-1])
print(x[1:-1])
print(x[:-2])

#3 Create a list of given structure and run 
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x)
Access list [1, 2, 3, 4]
print(x[5][:-5])
Access list [600,  700]
print(x[-3:-1])
Access list [100, 300, 500, 600, 800]
print(x[0::2])
Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[-1::-1])
x.reverse()
print(x)
Access list [10]
print(x[5][5][0])

# 4. Create a list of thousand numbers using range and xrange and see the difference between each other.
r = range(1,1000)
for i in range(1,1001,1):
    print(i, end =",")

# Note #4 abv code is for python 3, in P3 xrange dosent exist 


# 5. How Tuple is beneficial as compared to the list?
#We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types. 
# Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost. 
# Tuples that contain immutable elements can be used as a key for a dictionary.

# 6. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is 
#    divisible by 3 and a multiple of 2.
r = range(1,101,1)
for i in r:
    if (i%3==0 and i%2==0):
        print(i)

# 7. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.

sentence = list(input("Enter the String"))
print("Number of Vowels in Given strign is:",len([ i for i in sentence if i in "aeiouAEIOU"])) #online solution

s = "rucha"

# Reverse the string
strRev = s[::-1]

lst = []

# Declare array containing vowels
vowels = ['a', 'e', 'i', 'o', 'u']

index = 0

# Iterate over your reverse string 
for i in strRev:
  if i in vowels:
    print("Vowel is:- "+i)
    print("Index is:- "+str(index))
  index = index+1

# 8. Write a program in Python to iterate through the string “hello my name is Abcde” and print the string which has even length of the word.
s = "hello my name is Abcde"

# Split the string by spaces
listS = s.split()

print(listS)

for i in listS:
  if(len(i)%2 == 0):
    print(i)


# 9. Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]

target = 8

l = len(x)

for i in range(0, l-1):
  for j in range(i+1, l):
    if(x[i]+x[j] == target):
      print("["+str(x[i])+","+str(x[j])+"]")


# x=[1,2,3,4,5,6,7,8,9,-1]

# 10.Write a program in Python to complete the following task:
# Create two different lists as in even_list and odd_list
# Ask the user to enter the number in the range of 1,50 and make sure if the entered number is even appended it to the even_list and 
# if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 elements calculate the sum of the list and return the maximum out of the list.
evenList = []
oddList = []

while(len(evenList) < 5 or len(oddList) < 5):
  inputNumber = int(input())
  if(inputNumber % 2 == 0):
    evenList.append(inputNumber)
  else if(len(oddList) < 5):
    oddList.append(inputNumber)

print(sum(evenList))
print(sum(oddList))

print(max(evenList))
print(max(oddList))

# 11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement. 
# Example: 12abcbacbaba344ab  
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
s = '12abcbacbaba344ab'


d = {}
for i in s:
  if(not i.isdigit()):
    if i in d:
      d[i] = d[i] + 1
    else:
      d[i] = 1


print(d)

# 12.Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


