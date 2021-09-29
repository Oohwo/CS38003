# # LU Decomposition

# In big data and analytics, the speed of computation is very important.
# The amount of time spent on computation directly correlates with the possible profit a company earns.
# As such, it is important to make as many optimizations we can in our code.

# Today you will be implementing a method of factoring a matrix known as LU decomposition.
# It decomposes a square `N x N (A)` matrix into upper and lower triangular matrices.
# This factorization can then be reused later for multiple `Ax = y` computations.

# Why do this?
# Traditional Gaussian Elimination requires `O(n^3)` mathematical per solve.
# However with LU decomposition the factorization costs `O(n^3)` and each subsequent solve only requires `O(n^2)`
# mathematical operations per solve.
# In the case where `N` is in the millions and billions, one can imagine how much faster LU decomposition can be.

# A sample decomposition is shown below.


# ```
# A = [[2., 1.],
#      [8., 7.]]
# L = [[1. 0.],
#      [4. 1.]]
# U = [[2. 1.],
#      [0. 3.]]
# ```


# ## Function Prototype

# You may assume that we will always provide a valid numpy array as input

# ```Python
# def LU(A):
#     """
#     LU: LU Decomposition

#     :param A: An input np.array matrix
#     :return L, U: A lower and upper triangular matrix which is the decomposition of A.
#         If A is malformed please return None
#     """
# ```

import numpy as np

def LU(A):
  if A.shape[0] == 2:
    det = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    if det == 0:
      return None
  if A.shape[0] == 3:
    det = ((A[0][0]) * (A[1][1] * A[2][2] - A[1][2] * A[2][1])) - ((A[0][1]) * (A[1][0] * A[2][2] - A[1][2] * A[2][0])) + ((A[0][2]) * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    if det == 0:
      return None
