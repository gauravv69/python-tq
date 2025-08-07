'''
Task2:
Create a 3x3 matrix with numbers from 1 to 9.
 
 
Reshape it to a 1D array


Access the middle row from the original matrix


Replace the last element of reshaped array with 100
'''
import numpy as np

# Create a 3x3 matrix with numbers from 1 to 9.
matrix = np.arange(1,10)
print(matrix)

matrix1 = matrix.reshape(3,3)
print(matrix1)


# Reshape it to a 1D array
arr1 = matrix1.flatten()
print(arr1)


# Access the middle row from the original matrix
middle_row = matrix[1]
print(middle_row)



# Replace the last element of reshaped array with 100
matrix[-1] = 100
print(matrix)


















