# π (Pi) is a magical number. One method to estimate its value(3.141592...) is by using a Monte Carlo method.
# Assume we have a circle of radius 0.5, enclosed by a 1 × 1 square. The area of the circle is π*r^2=π/4,
# the area of the square is 1.

# For simplicity, you can imagine a two dimensional coordinate grid, with one vertex of the square being the origin
# point, (0,0). And a circle with a 0.5 radius centered at (0.5, 0.5).

# We then generate a large number of uniformly distributed random points, throughout the unit square.
# We keep track of the total number of points M, and the number of points that are inside the unit circle N.
# If we divide the number of points within the circle, N by the total number of points, M, we should get
# a value that is an approximation of the ratio of the areas between the circle and square.

#
#   N       pi * (0.5)^2       pi
# ----- = -------------- = ----------
#   M         1 x 1            4

# Simplifying this we get

#
# 4 N
# --- = pi
#  M

# Write a function estimate_pi(M) that using the Monte Carlo method to estimate the value of Pi with total M sampling.
# Generate a total of M points randomly inside the unit square. Check how many of those points lie within the
# enclosed circle, N. Return the value of 4*N divided by M as the estimate of π.
#
# This being the final lab means we expect your code to NOT crash. That means use default arguments, try catch blocks,
# do enough error checking so as to handle any call to your function without crashing. In case of a bad argument,
# your function should return None.
#
# Input: 1 input
#   - M: the number of samples to be generated. Type: int
#
# Output: 1 output
# estimated value of π. Type: float
#
# Example:
# estimate_pi(10) -> 3.2
# estimate_pi(1000) -> 3.18
# estimate_pi() -> None
# estimate_pi('hi') -> None
import random
from random import random

def estimate_pi(M):
  circle_n_points = 0
  square_m_points = 0

  if type(M) != int:
    return None

  i = 0
  while i < M:
    x_coord = random()
    y_coord = random()

    distance = x_coord**2 + y_coord**2

    if distance <= 1:
      circle_n_points = circle_n_points + 1
    square_m_points = square_m_points + 1

    pi = (4 * circle_n_points) / square_m_points

    i = i + 1

  return pi

print(estimate_pi(1000))
