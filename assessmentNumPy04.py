'''Task4.

Generate a 5x5 matrix with random integers between 1 and 100.


Find the maximum and minimum value in the matrix


Find the sum of each row


Replace all values greater than 50 with -1
'''

import numpy as np


# Generate a 5x5 matrix with random integers between 1 and 100.
matrix = np.random.randint(1,101,(5,5))
print(matrix)



# Find the maximum and minimum value in the matrix
print("-----Minimum-----")
print(np.min(matrix))
print(np.min(matrix,axis=0))
print(np.min(matrix,axis=1))



# Find the sum of each row
print("-----Sum of each row-----")
print(np.sum(matrix,axis=1))



# Replace all values greater than 50 with -1
print("-------Replaced value > 50 with -1----------")
matrix[matrix > 50] = -1
print(matrix)







