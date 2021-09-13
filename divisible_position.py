def divisible_position(list1, num):
  # Determine the length of each list in list1, if the length is more than 3
  # keep the first three elements by slicing the list
  counter = 0
  while counter < len(list1):
    if len(list1[counter]) > 3:
      list1[counter] = list1[counter][0:3]
    counter = counter + 1

  # Compute the sum of the elements in every list separately, add each sum to a list
  sum_list = []
  for each_list in list1:
    sum_of = 0
    for number in each_list:
      sum_of = sum_of + number
    sum_list.append(sum_of)
  
  # Use a new list to save all the positions of those lists whose sums are divisible by 'num'
  # If you can't find a position of a list or 'list1' has no list, return False...
  # If a list in list1 has no element, do NOT add its index to the new list
  divisible_position_list = []
  counter = 0
  while counter < len(sum_list):
    if (sum_list[counter] % num == 0) and (sum_list[counter] != 0):
      divisible_position_list.append(counter)
    counter = counter + 1
  
  if len(divisible_position_list) == 0:
    return False
  return divisible_position_list
  
# test cases
print(divisible_position([[3,8],[2,4],[1,2,3]],2))
print(divisible_position([[3,4,2,1],[6,3],[2,7,1],[9],[]],5))
print(divisible_position([],4))
print(divisible_position([[2,6],[1,3,8],[1,1,1,1],[10]],7))
