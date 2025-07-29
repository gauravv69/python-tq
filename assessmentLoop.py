'''
# WAP to print even numbers from 121 to 229 using a for loop.
for i in range(121, 230):
    if i % 2 == 0:
        print(i)
'''


'''
# WAP to print odd numbers from 521 to 229 using a while loop.
i = 521

while i >= 229:
    if i % 2 != 0:
        print(i)
    
    i-=1
'''


'''
# Write a Python program to print all alphabets from a to z  using  for loop
for i in range (97, 123):
    print(chr(i))
'''
'''
import string
print(string.ascii_uppercase)
'''


'''
# Write a Python program to find the sum of all even numbers between 1 to n.
i = int(input("Enter value of n: "))
even_sum = 0
for i in range(2, i+1, 2):
    even_sum += i
print("Sum of even numbers:", even_sum)
'''



'''
# Write a Python program to find the sum of all odd numbers between 1 to n.
i = int(input("Enter value of n: "))
odd_sum = 0
for i in range(1, i+1, 2):
    odd_sum += i
print("Sum of odd numbers:", odd_sum)
'''



'''
# Write a Python program to count number of digits in any number
i = int(input("Enter a number: "))
count = 0
while i != 0:
    count += 1
    i //= 10
print("Number of digits:", count)
'''



'''
# WAP to print table of given no
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f'{num * i}')
'''


'''
# WAP to print squares from 1 to20
for i in range(1, 21):
    print(i ** 2)
'''    












        
