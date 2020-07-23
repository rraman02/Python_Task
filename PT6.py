#1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

while True:
    try:
        x = int(input("Enetr a Number: "))
        break
    except SyntaxError:
        print("Oops!  That was no valid number. \n Try again...")





#2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect 
# throw an exception and ask them to enter the name again. Make sure to use read only mode.



#3. Write a program to handle an error if the user entered the number more than four digits it should return 
# “Please length is too short/long !!! Please provide only four digits” 

value = input("Enter the numbers here: ")
while True:
    try:
        if len(value) < 5:
            print(value)
            break
        else:
            raise Exception
    except:
        print("Please length is too short/long !!! Please provide only four digits")
        value = input("Enter again: ")





#4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and 
# if the password is incorrect give chance to enter it again but it should not be more than 3 times.

