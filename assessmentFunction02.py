'''
# Write a program to create a function that takes two arguments, name and age, and print their value.
def info(name, age):
    print("Name:",name)
    print("Age:",age)
    
info("Gaurav", 23)
'''



'''
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call
def calculation(a,b):
    add = a + b
    sub = a - b
    return add, sub

result = calculation(10, 5)
print("Addition:",result[0])
print("Substraction:",result[1])
'''




'''
Write a program to create a function show_employee() using the following conditions.
●  	It should accept the employee’s name and salary and display both.
●  	If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary = 9000):
    print("Employee Name:",name)
    print("Salary:",salary)
    
show_employee("Gaurav")
show_employee("Aditya", 150000)
'''



'''
Accept a number from the user, create a function isPrime(), which accepts a number 
from a parameter & check prime or not. If number is prime return True & number else return 
false & number
'''

    

'''
# Create menu driven calculation (add,sub,multiply, divide, mod) using function
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def mod(a,b):
    return a % b

print("1. Add \n2.Substract \n3.Multiply \n4.Divide \n5.Modulus")
choice = int(input("Enter a choice between 1 -5: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if choice == 1:
    print("Result:",add(a,b))
elif choice == 2:
    print("Result:",sub(a,b))
elif choice == 3:
    print("Result:",mul(a,b))
elif choice == 4:
    print("Result:",div(a,b))
elif choice == 5:
    print("Result:",mod(a,b))
else:
    print("Invalid Choice!")
'''




'''
# Create a function to accept a number & return its factorial    
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

number = int(input("Enter a number:"))
print("Factorial:",factorial(number))
'''




'''
Create a function that accept student data, calculate the total & percentage,
return total & percentage
def student(m1, m2, m3):
    total = m1 + m2 + m3
    percent = total / 3
    return total, percent

tot, per = student(75, 80, 92)
print("Total:",tot)
print("Percentage:",per)
'''





'''
Create a login function, that accept username & password,
if username is ‘admin’ & password is ‘admin@123’ then return true, else return false
'''
def login(username, password):
    if username == 'admin' and password == 'admin@123':
        return True
    else:
        return False
    
user = input("Enter username: ")
pass = input("Enter password: ")

if login(user, pass):
    print("Login Successful")
else:
    print("Login Failed")
















