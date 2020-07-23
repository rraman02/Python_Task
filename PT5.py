#1. Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. 
# Make sure to use only higher order function.
'''
l1 = []
for i in range(1,101):
    l1.append(i)

x1 = list(filter(lambda x: x%3!=0, l1))
x2 = list(filter(lambda y : y%7==0, x1))
print(x2)
'''

#2.Write a program in Python to  multiple the element of list by itself using a traditional function and pass the function to map 
# to complete the operation.
'''
x = [1,2,3,4,5,6,7,8,9]

#lambda x : x*x

def sq(x):
    return x*x

print(list(map(sq,x)))

'''

#3. Write a program to Python find out the character in a string which is uppercase using list comprehension.
'''

string_demo = "i LiKe PytHOn"


x = [i for i in string_demo if i.isupper()]
print(x)
'''
#4. 	Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
#Student = ['Smit', 'Jaya', 'Rayyan']
#capital = ['CSE', 'Networking', 'Operating System']
'''
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']


print(dict(zip(Student, capital)))
'''

#6. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
'''
demo = "Rucha"
x = (i for i in demo[::-1])

b = ""
while True:
    try:
        a = next(x)
        b += a
        
    except:
        break

print(b)


input_string = "Consultadd Training"

def rev(x):

    for i in x[::-1]:
        yield(i)
y = ""
res=rev(input_string)
# print(list(next(res))
while True:
    try:
        a=next(res)
        y += a


    except:
        break
print(y)

'''

#7. Write any example on decorators.
'''
def tile1(sum):
    print("Hello I am new here")
    sum()
    return sum

    

@tile1
def ordinary():
    print("Hello i am from the old one ")

ordinary()
'''

#8. 	Learn about What is FRONT END and its Technologies and Tools
#Make sure to mention at least 5 top notch technologies of Frontend.
#Also mentioned the name of companies using those 5 technologies individually
'''
5 Front Technologies. -React.js , Angular.js , HTML , CSS , javascript
5 Companies using these technologies - React (Facebook), Angular (Bank of america), HTML (Airbnb), CSS (Cisco), Javascript ( Amazon).