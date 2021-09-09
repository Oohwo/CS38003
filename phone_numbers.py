# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/885624835340922911/unknown.png
# TODO: Add comments
import re
    
def find_phone_number(filename):
  my_file = open(filename, "r")
  lines = my_file.read().split('\n')
  output_list = []
  for line in lines:
    pattern = re.compile('\d{3,3}-\D{1,}-\w{1,}')
    potential_num = re.findall(pattern, line)
    if potential_num != []:
      output_list.append(line)
  my_file.close()
  return output_list

print(find_phone_number("file.txt"))
