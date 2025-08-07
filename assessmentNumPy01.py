'''
Task 1.
Create a NumPy array with values from 10 to 50.


Extract elements greater than 30


Multiply the array by 2


Find mean and standard deviation of the array
'''

import numpy as np

# Create a NumPy array with values from 10 to 50.
arr = np.arange(10,51)
print(arr)


# Extract elements greater than 30
arr1 = arr[arr > 30]
print("Elements greater that 30:",arr1)


# Multiply the array by 2
arr3 = arr * 2
print(arr3)


# Find mean and standard deviation of the array
arr4 = np.mean(arr)
arr5 = np.std(arr)
print("Mean:",arr4)
print("Std Deviation:",arr5)

