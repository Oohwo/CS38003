# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/882947153029374022/unknown.png
def increasing_dict(dictionary):
  key_value_list = []

  if len(dictionary) == 0:
    return None

  for key in dictionary: # appends each key and value the key_value_list
    key_value_list.append(int(key))
    key_value_list.append(int(dictionary[key]))
  
  # checks if key_value_list is increasing
  # if increasing, return true... otherwise, return false
  i = 0
  while i < len(key_value_list) - 1:
    if key_value_list[i] > key_value_list[i + 1]:
      return False
    i = i + 1
  
  return True

# test cases
print(increasing_dict({1: 2, 3: 5, 9: 6, 7: 8}))
print(increasing_dict({1: 2, 3: 4, 5: 6, 7: 8}))
print(increasing_dict({-5: -7, 6: 8}))
print(increasing_dict({-5: -6, 7: 8}))
