'''
# Python program to remove given character from String.
s1 = input("Enter string: ")
ch = input("Enter character to remove: ")
result = s1.replace(ch, "")
print("Result:", result)
'''




'''
# Python Program to count occurrence of a given characters in string.
s1 = input("Enter string: ")
ch = input("Enter character to count: ")
print(f"{ch} occurred {s1.count(ch)} times")
'''



'''
# Python program to check if a String is palindrome or not
s1 = input("Enter name: ")
if s1 == s1[::-1]:
    print("The string is Palindrome")
else:
    print("Not Palindrome")
'''




'''
# Python program to check if a given character is vowel or consonant.
ch = input("Enter a character: ")
if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Constant")
else:
    print("Not an alphabet")
'''




'''
# Python program to check if a given character is digit or not.
ch = input("Enter a character: ")
if ch.isdigit():
    print("Digit")
else:
    print("Not a digit")
'''




'''
# Python program to replace the string space with a given character.
s1 = input("Enter string: ")
ch = input("Enter a charcater: ")
result = ""

for c in s1:
    if c == " ":
        result += ch
    else:
        result += c
print("Result:", result)
'''
    
    
    

'''
# Python program to replace the string space with a given character using replace() method.
s1 = input("Enter a string: ")
ch = input("Enter a character: ")
print(s1.replace("", ch))    
'''





'''
# Python program to convert lowercase char to uppercase of string.
s1 = input("Enter string: ")
print(s1.upper())    
'''




'''
# Python program to convert lowercase vowel to uppercase in string.
s1 = input("Enter string: ")
result = ""

for ch in s1:
    if ch in "aeiou":
        result += ch.upper()
    else:
        result += ch
print("Result:", result)
'''





'''
# Python program to delete vowels in a given string.
s1 = input("Enter string: ")
vowels = 'aeiouAEIOU'
result = ""
for c in s1:
    if c not in vowels:
        result += c
print("Without vowels:", result)
'''





# Python program to count Occurrence Of Vowels & Consonants in a String.


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    