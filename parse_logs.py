# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/887213835818270720/unknown.png

import re
from typing import List

def parse_logs(file_path, log_types) -> List[str]:
  my_file = open(file_path, "r")
  lines = my_file.read().split('\n')
  output_list = []
  for line in lines:
    for log_type in log_types:
      regex = '\[' + '([0-1]?[0-9]|2[0-3])' + ':[0-5][0-9]:[0-5][0-9]' + re.escape(" ") + re.escape(log_type) + '\]' + re.escape(" ")
      pattern = re.compile(regex)
      potential_pattern = re.findall(pattern, line)
      if potential_pattern != []:
        output_list.append(line)
  my_file.close()
  return output_list

# test cases
print(parse_logs("file.txt", ["error"]))
