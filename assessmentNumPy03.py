'''
Task3.
arr = np.array([5, 12, 17, 23, 45, 50, 66])
Find all even numbers


Count how many numbers are greater than 20


Replace all values less than 20 with 0
'''

import numpy as np
arr = np.array([5, 12, 17, 23, 45, 50, 66])
print(arr)


# Find all even numbers
even_no = arr[arr % 2 == 0]
print("Even Numbers:",even_no)



# Count how many numbers are greater than 20
no = np.sum(arr > 20)
print("Count:",no)


# Replace all values less than 20 with 0
arr[arr < 20] = 0
print(arr)

