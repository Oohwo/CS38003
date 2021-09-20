# This question shall make use of a file similar to the sample.csv
#
# The company with this data wants to know how much is an employee being paid. Their pay rate is $7.25 per hour.
# You are required to write a function compute_pay(filename, employee) which uses Pandas
# to do the following:
# 1. read the file pointed to by the filename into a Pandas dataframe
# 2. filter the dataframe in 1. to include only the records of a particular employee passed as input
# 3. compute the pay in dollars for every record of the employee, e.g. if a record is 3/2/2019, Jd, SALES, 2.8,
#    then 2.8*7.25 = 20.3. So the record should become 3/2/2019, Jd, SALES, 2.8, 20.3.
# 4. insert into the dataframe after filtering in step 2., a new column titled 'pay'. This column should have
#    the pay for the employee's records.
# 5. return the appended dataframe from 4
#
# function compute_pay(filename, employee)
# Inputs: 2 inputs
#   - filename: the file to be read, type string
#   - employee: the name of the employee, type string
# Outputs: One output
#   a Pandas dataframe that has the pay column appended to it
#
# E.g. if after filtering the dataframe by 'Jd', you get
#          date employee department  hours
# 0    3/2/2019      Jd      SALES    2.8
# 1    3/4/2019      Jd       SHIP    4.5
# 2  12/12/2019      Jd       SHIP    0.8
#
# then the result of your compute_pay(filename, 'Tony') function should be
#          date employee department  hours     pay
# 0    3/2/2019     Tony      SALES    2.8     20.3
#
# or if running compute_pay(filename, 'Leo')
# then the result of your compute_pay(filename, 'Leo') function should be
#          date employee department  hours     pay
# 1    3/4/2019      Leo       SHIP    4.5    36.625

import pandas as pd

def compute_pay(filename, employee):
  data = pd.read_csv(filename)
  employee_data = data[data.employee == employee]

  data['pay'] = employee_data.hours * 7.25
  return(data[data.employee == employee])
