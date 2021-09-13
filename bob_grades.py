# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/887088945354113024/unknown.png

def improve_semester(bob_grades):
  class_avg_dict = {} 
  output_list = [] # returns [class with lowest avg, and the new rounded average after improvement]

  if len(bob_grades) == 0:
    return None # if bob_grades is empty

  # iterates through each course in bob_grades. if a course has no grades, we ignore (delete) the course
  # otherwise, we take the average of each non-empty course
  for course in bob_grades: 
    isEmpty = True
    if len(bob_grades[course].values()) != 0:
      isEmpty = False
      avg = 0.0
      for grade in bob_grades[course].values():
        avg = avg + grade
      avg = avg / len(bob_grades[course].values())
      class_avg_dict[course] = avg
  if isEmpty:
    del bob_grades[course]

  # iterates and grabs each average and class and puts them in respective lists
  class_avg_list = [] # list of averages (float)
  class_list = [] # list of classes
  for key in class_avg_dict:
    class_list.append(key)
    class_avg_list.append(class_avg_dict[key])
  
  # adds the class with the lowest average onto our output list
  output_list.append(class_list[class_avg_list.index(min(class_avg_list))])

  # improves the worst average by 15 points (up to a max of 100)
  class_avg_dict[class_list[class_avg_list.index(min(class_avg_list))]] = class_avg_dict[class_list[class_avg_list.index(min(class_avg_list))]] + 15
  if class_avg_dict[class_list[class_avg_list.index(min(class_avg_list))]] > 100:
    class_avg_dict[class_list[class_avg_list.index(min(class_avg_list))]] = 100

  # creates the new and improved grade average, rounded and capped at 100, and adds it to the output list
  new_avg = 0.0
  for average_value in class_avg_dict.values():
    new_avg = new_avg + average_value
  new_avg = round(new_avg / len(class_avg_dict))
  if new_avg > 100:
    new_avg = 100
  output_list.append(new_avg)

  # returns desired output
  return(output_list)

# test cases
print(improve_semester({"Math": {1: 86, 2: 81}, "English": {1: 60, 2: 71}, "Science": {1: 90}}))
print(improve_semester({"Spanish": {1: 97}, "English": {1: 100}, "Science": {1: 90}}))
print(improve_semester({"Spanish": {1: 50}, "English": {}}))
print(improve_semester({}))
