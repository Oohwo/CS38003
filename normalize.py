# Matrices are frequently used in data science to store and process information.
# However most of the times, raw data needs to be pre-processed to be normalized.
# This is done to get the values in a desirable range, center them, etc.
# In this question you would write a Python function normalize(A, B) who would take
# two numpy matrices A and B, and shall normalize both of these so that every value
# in them is between 0 and 1. Then your function should return the product of
# the two normalized matrices.
# A matrix M is normalized as follows:
# Step 1: find the minimum value of M and subtract it from each of the elements of M
# Step 2: from the matrix resulting from step 1 after subtraction, find its maximum element, say m
# Step 3: divide every element of the matrix from step 1 by the element m from step 2
#
# function normalize(A, B)
# Inputs: 2 inputs
#   - A: a numpy matrix
#   - B: a numpy matrix
# Outputs: 1 output
#   - a numpy matrix
#
# Example:
# Let A = [[-42 -26]
#         [ 17  53]]
#
#     B = [[-24  55]
#         [-34  18]]
#
# The minimum element of A is - 42.
# After subtracting -42 from all elements of A, it becomes [[ 0 16]
#                                                           [59 95]]
# The maximum element of this matrix is 95
# Dividing every element of this by 95 gives us [[0.         0.16842105]
#                                                [0.62105263 1.        ]]
# which is the normalized version of A.
#
# Similarly, normalizing B should give us [[0.11235955 1.        ]
#                                          [0.         0.58426966]]
#
# The product of normalized version of A and B then is [[0.         0.09840331]
#                                                       [0.06978119 1.20532229]]

import numpy as np

def normalize(A, B):
  a_matrix = A
  b_matrix = B

  min_a = a_matrix.min()
  min_b = b_matrix.min()
  a_matrix -= min_a
  b_matrix -= min_b

  max_a = a_matrix.max()
  max_b = b_matrix.max()
  
  a_matrix = np.divide(a_matrix, max_a)
  b_matrix = np.divide(b_matrix, max_b)

  return(a_matrix.dot(b_matrix))
