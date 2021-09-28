# You need to write a function called remove_sub_list, which takes two lists (list1, list2) as arguments This function should find if list2 is a sublist of list1, and remove the sublist from list1. If list2 is not a sublist of list1, find_sub_list should return -1. If list2 is a sublist of list1, remove_sub_list should return the list1 with the first instance of list2 removed. That is, if there are multiple instances of the sublist, you do not need to do it multiple times. Remember, the order of occurrence of elements in lists matter. An empty list is a sublist.

# Examples: print(remove_sub_list([1, 2, 3], [])) > [1,2,3]

# print(remove_sub_list([4, 2, 3, 1, 2, 3], [2, 3])) > [4, 1, 2, 3]

# print(remove_sub_list([3, 4, 1, 2, 5], [4, 2, 5])) > -1

# print(remove_sub_list([1, 2, 5, 4, 3, 6, 7], [3, 6, 7])) > [1, 2, 5, 4]

def remove_sub_list(list1, list2):
  if len(list2) == 0:
    return list1
  
  match = False
  found_indexes_list = []

  counter = 0
  another_counter = 0
  list2_counter = 0
  while counter < len(list1):
    if list1[counter] == list2[0]:
      for num in list2:
        another_counter = counter
        match = True
        while another_counter < len(list1) and match == True and list2_counter < len(list2):
          if list1[another_counter] == list2[list2_counter]:
            found_indexes_list.append(another_counter)
            another_counter = another_counter + 1
            list2_counter = list2_counter + 1
          else:
            match = False
    counter = counter + 1

  if match == False:
    return -1
  
  counter = len(found_indexes_list) - 1
  while counter >= 0:
    del list1[found_indexes_list[counter]]
    counter = counter - 1

  return list1

print(remove_sub_list([4, 2, 3, 1, 2, 3], [2, 3]))
print(remove_sub_list([3, 4, 1, 2, 5], [4, 2, 5]))
print(remove_sub_list([1, 2, 5, 4, 3, 6, 7], [3, 6, 7]))
