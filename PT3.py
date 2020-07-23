#1 Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
x = [1.0,2,"string", 1+2j]

for val in x :
    print (type (val))

#2 Create a list of size 5 and execute the slicing structure
x = ["a", "b", "c","d", "e","f"]
print(x[0:3])
print(x[-3:])
print(x[0:5:3])
print(x[:-2])
print(x[2:])
print(x[:-4:2])

#3 Write a program to get the sum and multiply of all the items in a given list.
y = [1,2,3,4,5]
total = 0
product = 1
for val in y :
    total = total + val 
print (total)

for val in y :
    product = product * val
    print (product)

for val in y:
    print (val + 2)

#4 Find the largest and smallest number from a given list
a = [1,2,3,4,10,0]
print(min(a))
print(max (a))

#5 Create a new list that contains the specified numbers after removing the even numbers from a predefined list. 
b = [1,2,3,4,5,6,7,8,9,10]
c = []
for val in b:
    if val % 2 == 0 :
        c.append(val)
print (c)

#6 Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
d = [*range(1,31,1)]
print (d)
e = []
for val in d[:5]:
    e.append(val ** 2)
for val in d[25:]:
    e.append(val ** 2)

print(e)

#7 Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

a = [1,3,5,7,9,10]
# b=[2,4,6,8]
a.extend([2,4,6,8])
# a [-1:] = b
print(a)    

#8 Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}
# Result: {1:10,2:20,3:30,4:40}
a.update(b)
print(a)


#9 Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}
n=int(input("Input a number "))
d = dict()
	
for x in range(1,n+1):
    d[x]=x*x
	
print(d)
# Note: Above solution found on net, but i am not able to understand it 


#10 Write a program which accepts a sequence of comma-separated numbers from the console and generate 
# a list and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)
x = 34,67,55,33,12,98
x = input("Enter 5 numbers:")
x = tuple(x)
# x = list(x)
print(x)


    
        

