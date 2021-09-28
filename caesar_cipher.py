# # Alphanumeric Caesar Cipher

# ## Problem Statement

# ### Caesar Cipher

# A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving `n` places down the alphabet. For example, assume the input plain text is the following:
# ```
# abcd xyz
# ```
# If the shift value, `n`, is 4, then the encrypted text would be the following:
# ```
# efgh bcd
# ```

# ### Alphanumeric Caesar Cipher

# In this question, you will be implementing an alphanumeric Caesar cipher which can not only handle lowercase letters, but also uppercase letters as well as numbers, with separate shift values for each different category.

# You will be implementing both the encrypter **and** the decrypter for the cipher.

# The functions you will need to implement are as follows:
# ```python
# def caesar_enc(message, shift_l, shift_u, shift_n):
#     '''
#     Encrypts the input message and returns the encrypted string.
#     Lowercase letters are by shifted by shift_l, uppercase letters by shift_u, and numbers by shift_n.
#     Other characters are not shifted.
#     -----------
#     Inputs:
#         message (str): Message to be encrypted.
#         shift_l (int): Shift amount for lowercase letters.
#         shift_u (int): Shift amount for uppercase letters.
#         shift_n (int): Shift amount for numbers.
#     Outputs:
#         (str): The encrypted message.
#     '''
    
# def caesar_dec(message, shift_l, shift_u, shift_n):
#     '''
#     Decrypts the input message and returns the decrypted string.
#     Lowercase letters are by un-shifted by shift_l, uppercase letters by shift_u, and numbers by shift_n.
#     Other characters are not shifted.
#     -----------
#     Inputs:
#         message (str): Message to be decrypted.
#         shift_l (int): Un-shift amount for lowercase letters.
#         shift_u (int): Un-shift amount for uppercase letters.
#         shift_n (int): Un-shift amount for numbers.
#     Outputs:
#         (str): The decrypted message.
#     '''
# ```

# ### Notes

# Inputs to `message` can include special symbols (such as spaces, commas, underscores, etc.). Do not shift special symbols.

# Inputs to `shift_l`, `shift_u` and `shift_n` can be any integer, including negative integers. You can assume that decimals (such as 3.4) will not be inputs.

# `caesar_enc` and `caesar_dec` should be implemented in a way such that, using the same shift values, decrypting an encrypted message returns the original message. In other words, `caesar_dec(caesar_enc(message, x, y, z), x, y, z) = message`

# **Hint**: You can use `string.uppercase`, `string.lowercase` and `string.digits`.

# ### Examples

# ```
# message = 'Hello World!!!111one'
# shift_l = 2
# shift_u = 1
# shift_n = -3

# caesar_enc(message, shift_l, shift_u, shift_n) =
# ```
# > `Ignnq Xqtnf!!!888qpg`

# ```
# message = 'Ignnq Xqtnf!!!888qpg'

# caesar_dec(message, shift_l, shift_u, shift_n) =
# ```
# > `Hello World!!!111one`

def caesar_enc(message, shift_l, shift_u, shift_n):
  encrypted_msg = ""
  shift_l = shift_l % 26
  shift_u = shift_u % 26
  shift_n = shift_n % 10
  for char in message:
    if (97 <= ord(char) and ord(char) <= 122):
      if (ord(char) + shift_l < 97):
        diff = ord(char) + shift_l
        diff = diff - 97 + 123
        char = chr(diff)
      elif (ord(char) + shift_l > 122):
        diff = ord(char) + shift_l
        diff = diff - 122 + 96
        char = chr(diff)
      else:
        char = chr(ord(char) + shift_l)
      encrypted_msg = encrypted_msg + char
    elif (65 <= ord(char) and ord(char) <= 90):
      if (ord(char) + shift_u < 65):
        diff = ord(char) + shift_u
        diff = diff - 65 + 91
        char = chr(diff)
      elif (ord(char) + shift_u > 90):
        diff = ord(char) + shift_u
        diff = diff - 90 + 64
        char = chr(diff)
      else:
        char = chr(ord(char) + shift_u)
      encrypted_msg = encrypted_msg + char
    elif (48 <= ord(char) and ord(char) <= 57):
      if (ord(char) + shift_n < 48):
        diff = ord(char) + shift_n
        diff = diff - 48 + 58
        char = chr(diff)
      elif (ord(char) + shift_n > 57):
        diff = ord(char) + shift_n
        diff = diff - 57 + 47
        char = chr(diff)
      else:
        char = chr(ord(char) + shift_n)
      encrypted_msg = encrypted_msg + char
    else:
      encrypted_msg = encrypted_msg + char
  
  return encrypted_msg

def caesar_dec(message, shift_l, shift_u, shift_n):
  decrypted_msg = ""
  shift_l = shift_l % 26
  shift_u = shift_u % 26
  shift_n = shift_n % 10
  for char in message:
    if (97 <= ord(char) and ord(char) <= 122):
      if (ord(char) - shift_l < 97):
        diff = ord(char) - shift_l
        diff = diff - 97 + 123
        char = chr(diff)
      elif (ord(char) - shift_l > 122):
        diff = ord(char) - shift_l
        diff = diff - 122 + 96
        char = chr(diff)
      else:
        char = chr(ord(char) - shift_l)
      decrypted_msg = decrypted_msg + char
    elif (65 <= ord(char) and ord(char) <= 90):
      if (ord(char) - shift_u < 65):
        diff = ord(char) - shift_u
        diff = diff - 65 + 91
        char = chr(diff)
      elif (ord(char) - shift_u > 90):
        diff = ord(char) - shift_u
        diff = diff - 90 + 64
        char = chr(diff)
      else:
        char = chr(ord(char) - shift_u)
      decrypted_msg = decrypted_msg + char
    elif (48 <= ord(char) and ord(char) <= 57):
      if (ord(char) - shift_n < 48):
        diff = ord(char) - shift_n
        diff = diff - 48 + 58
        char = chr(diff)
      elif (ord(char) - shift_n > 57):
        diff = ord(char) - shift_n
        diff = diff - 57 + 47
        char = chr(diff)
      else:
        char = chr(ord(char) - shift_n)
      decrypted_msg = decrypted_msg + char
    else:
      decrypted_msg = decrypted_msg + char
  
  return decrypted_msg
