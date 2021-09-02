# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/882946534235340821/unknown.png
def remove_indices(word, list1):
  new_word = "" # output

  if len(word) == 0: # if input is an empty string, return ""
    return new_word

  rid_letters = set(list1) # indices to get rid of
  keep_letters = set(range(0, len(word))) - rid_letters # keep_letters = range - rid_letters
  keep_letters = list(keep_letters) # turns set -> list so keep_letters is subscriptable
  
  index = 0
  while index < len(keep_letters): # iterates through keep_letters
    new_word = new_word + word[keep_letters[index]] # creates new word out of keep_letters
    index = index + 1 # increments
  
  return new_word # output

# test cases
print(remove_indices('Napolean',[1,3,4]))
print(remove_indices('bAllOon',[0,1]))
print(remove_indices('Hymn',[]))
