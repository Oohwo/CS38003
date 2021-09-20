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
