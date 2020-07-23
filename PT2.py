# Quention 1
num1=int(input("enter number:"))
if num1%3==0:
    print(num1, "consultadd")
    if num1%5==0:
        print("c")
        if num1%3==0 and num1%5==0:
            print("Consultadd Python Training")

# Question 2
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print ("you entered ",num1, " and" , num2, "Addition of this is ", num1+num2)
print ("you entered ",num1, " and" , num2, "Subtraction of this is ", num1-num2)
print ("you entered ",num1, " and" , num2, "Multiplication of this is ", num1*num2)
print ("you entered ",num1, " and" , num2, "Division of this is ", num1/num2)

# Question 3
Age = 38
if Age >= 11 :
    print("You are eligible to see the football match")
    if Age <=20 or Age >= 60:
        print("ticket price is $12")
    else:
        print("ticket price is $20")
else:
    print("you're not eligible to buy a ticket")
    
# Question 4
inputNo = int(input("enter a number:"))
loop = int(input("how many time you wish to run loop"))
runRound = 0
while True :
  if inputNo <= 0:
    print("game over")
    break
  elif inputNo > 0:
    print("good going")
    runRound = runRound + 1
    print("runRound  I am running :",runRound)
    if runRound == loop:
      break
    continue

# Question 5

print("Numbers that are divisible by 7 but are not multiples of 5")
for i in range (2000,3201):
    if i%7 == 0 and i%5 != 0:
        print (i, end = ", ") # how to remove , in last line?

# Question 6
# x=123
# for i in x :
#     print (i)

# As an output it gives a TypeError: 'int' object is not iterable
...
 
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print("error")

# Output : 0
        #    1
        #    2
        #    3

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Output: 0
        #   1
        #   2
        #   3
        #   4
        #   5
        

#question 7
for x in range(9):
    if (x == 3 or x==6):
        continue
    print(x,end=' ,')

#question 8
# Write a program that accepts a string as an input from the user and calculates the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

x = input("Enter a String: ")
d=l=0
for loop in x:
    if loop.isdigit():
        d=d+1
    elif loop.isalpha():
        l=l+1
print("Letters", l)
print("Digits", d)

# 9. Read the two parts of the question below: 
#  Write a program such that it asks users to “guess the lucky number”.
#  If the correct number is guessed the program stops, otherwise it continues forever. 
# Modify the program so that it asks users whether they want to guess again each time. 
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question of whether they want to continue guessing. 
# The program stops if the user guesses the correct number or answers “no”. 
# ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

# counter = 1
# while counter <= 5:
#     print("Type in the", counter, "number")
#     counter = counter + 1
#     if number == 3 :
#         print("good guess")
#         break
#     else:
#         print("game over")
import random
x = random.randrange(0,9)  
guess = int(input("guess the lucky number:"))
while guess != x :
    print(" no \n")
    guess = int(input("guess the lucky number:"))
print("correct no")

#questionn 10
# Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
#            		counter=1
# 		While counter <= 5:
# 			print(“Type in the”, counter, “number”
# 			counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). /
# If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. 
# After the fifth guess, it stops and prints “Game over!”.

luckyNum = 4
counter = 1
while counter <= 5:

  guessNum = input ("Guess the lucky number :")

  if guessNum == (luckyNum):
    print ("Good guess!")
  elif guessNum !=(luckyNum):
    print ("Try again!")




    

           

    
    