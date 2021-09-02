def find_students(dict_list, common_interest):
  set_list = [] # list of set_interests
  student_list = [] # list of students in dict_list
  found_students_int_list = [] # list of indexes of found_students
  found_students = [] # output

  # if the dict_list is empty, we return nothing
  if len(dict_list) == 0:
    return None

  # appends students' names into a student list and sets of interests into a set_list
  # helps with organization for the function
  for dict in dict_list: # for each dictionary in the dict_list
    set_interests = set() # create a new set of interests for each student
    for student in dict:
      student_list.append(student) # adds student's name to student_list
      for interest in dict[student]:
        set_interests.add(interest) # adds each interest to the set of interests
    set_list.append(set_interests) # adds each student's set of interests

  # iterates through the interest sets in the set list and
  # grabs indexes used to find students with the same interest
  counter = 0
  for set_interest in set_list:
    if (common_interest in set_interest):
      found_students_int_list.append(counter) # if common_interest is found in set, add index to found index list
      counter = counter + 1
    else:
      counter = counter + 1 
    
  # iterates through each index in the found index list, appends to found_students
  for index in found_students_int_list:
    found_students.append(student_list[index])
  
  return found_students # returns the desired output
    
# Test cases
find_students([{'Anne': ['NLP', 'Networks']}, 
{'Bob': ['Computer Vision', 'Networks']}, 
{'Charlie': ['Data Science']}], 'Networks')

find_students([], 'yo')

find_students([{'Danny': ['Parallel Computing']},{'Eva': ['VR']}], 'Reinforcement Learning')

find_students([{'Me': ['Data Science']},{'Anne': ['NLP', 'Networks']}, 
{'Bob': ['Computer Vision', 'Networks']}, 
{'Charlie': ['Data Science']}], 'Networks')
