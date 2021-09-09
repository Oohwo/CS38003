# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/885619510370000936/unknown.png
# Note: Create separate files for each file you test
# TODO: Add comments
import re
    
def extract_email(filename):
  my_file = open(filename, "r")
  lines = my_file.read().split('\n')
  output_dict = {}
  email_list_of_lists = []
  for line in lines:
    pattern = re.compile('\w*@\w*.com')
    potential_email = re.findall(pattern, line)
    if potential_email != []:
      email_list_of_lists.append(potential_email)
    pattern = re.compile('\w*@\w*.net')
    potential_email = re.findall(pattern, line)
    if potential_email != []:
      email_list_of_lists.append(potential_email)
  print(email_list_of_lists)
  for email_list in email_list_of_lists:
    for email in email_list:
      if email in output_dict:
        output_dict[email] = output_dict[email] + 1
      else:
        output_dict[email] = 1
  my_file.close()
  return output_dict
