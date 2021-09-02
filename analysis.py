def analysis(elements):
  tuple_list = ([])
  counter_list = []
  
  for i in (range(min(elements), max(elements) + 1)): # iterates through smallest num to largest num
    counter = 0
    for element in elements: # iterates through each element
      if i == element: # if i matches element... increment counter
        counter = counter + 1
    counter_list.append(counter) # add counter to counter list

  # create tuple list
  for i in range(0, len(counter_list)):
    new_tuple = tuple([i + 1, counter_list[i]]) # number, num occurrences 
    tuple_list.append(new_tuple) # add new_tuple to tuple_list
  
  return tuple_list

# test case:
print(analysis([1, 2, 3, 2, 3, 4, 5, 6, 6, 7, 6, 5])) # 1 2 2 1 2 3 1
