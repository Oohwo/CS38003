# Write a function named plate_generate(prefix, N) that generates license plate numbers with a given
# prefix and it has N (4 <= N <=6) characters in total. It contains a combination of numbers (0 – 9) 
# and letters (A – Z). For example, given N=6 and prefix '765', the function plate_generate() should
# return a valid license plate such as '765-AAA'. You may use string.ascii_uppercase to obtain all 
# uppercase letters.
#
# Input:
# a prefix (less than N digits). Type: string
# an integer N . Type: int
#
# Output:
# a license plate has N characters. Type: string (with the format '123-ABC'/'123-AB'/'123-A')
# Unless a prefix's first 3 characters has letters, you should randomly generate random numbers for it.
# Unless a prefix's last 3 characters has numbers, you should randomly generate characters for it
#
# Example: (these may not be the same in your case as there is some randomness in generating numbers/letters)
# plate_generate('76', 4) -> '767-I'
# plate_generate('831B', 6) -> '831-BGH'
# plate_generate('', 5) -> '417-BW'
# plate_generate('', 6) -> '923-JEI'
# plate_generate('ABC1', 6) -> 'ABC-1JE
# plate_generate('1B', 4) -> 1B3-ADE

import random
from random import randrange
import string

def plate_generate(prefix, N):
  i = 0
  first_three_letters = False
  last_three_num = False

  plate = ''
  if len(prefix) > 3:
    prefix_1 = prefix[0:3]
    prefix_2 = prefix[3:]

    plate = prefix_1 + '-' + prefix_2
    first_three_letters = any(i.isalpha() for i in prefix_1)
    # last_three_num = any(i.isnumber() for i in prefix_2)
    if first_three_letters:
      while len(plate) <= N:
        if len(plate) == 3:
          plate = plate + '-'
        plate = plate + str(randrange(0, 9))
    else:
      while len(plate) <= N:
        if len(plate) == 3:
          plate = plate + '-'
        plate = plate + random.choice(string.ascii_uppercase)
  else:
    plate = prefix
    first_three_letters = any(i.isalpha() for i in prefix)
    if first_three_letters:
      while len(plate) <= N:
        if len(plate) < 3:
          plate = plate + random.choice(string.ascii_uppercase)
        if len(plate) == 3:
          plate = plate + '-'
        if len(plate) > 3:
          plate = plate + str(randrange(0, 9))
    else:
      while len(plate) <= N:
        if len(plate) < 3:
          plate = plate + str(randrange(0, 9))
        if len(plate) == 3:
          plate = plate + '-'
        if len(plate) > 3:
          plate = plate + random.choice(string.ascii_uppercase)
        
  return plate

print(plate_generate('76', 4))
print(plate_generate('831B', 6))
print(plate_generate('', 5))
print(plate_generate('', 6))
print(plate_generate('ABC1', 6))
