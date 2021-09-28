# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/892513849067048980/unknown.png
import pandas as pd

def diamond_stat(file_path, attribute, min_val):
  unit_price_list = []

  price_list = []
  attribute_list = []

  data = pd.read_csv(file_path)
  data = data[data[attribute] > min_val]
  
  for price in data.price:
    price_list.append(price)
  for col in data.columns:
    if col == attribute:
      for num in data[col]:
        attribute_list.append(num)
  
  counter = 0
  while counter < len(price_list):
    unit_price = price_list[counter] / attribute_list[counter]
    unit_price_list.append(unit_price)
    counter = counter + 1
  
  data['avg_' + attribute] = unit_price_list

  output_dict = {}
  for col in data.columns:
    output_dict[col] = data[col].max()
  
  return(data, output_dict)
