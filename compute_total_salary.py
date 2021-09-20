# This question shall make use of a file similar to the sample.csv
# The company whose data is in the file, has different pay rate per hour for different departments.
# As the employees in the company rotate between departments, the company wishes to find the total pay
# for an employee. The per hour pay rate per department is stored in a Python dictionary, called pay_scale
# which looks like {'SALES': 50.0, 'TECH': 100.0, ...}.
# You are required to write a function compute_salary(filename, employee, pay_scale) which uses pandas to
# do the following:
# 1. read the file pointed to by the filename
# 2. filters the data read in 1. by the employee as argument
# 3. find out the total salary this employee will earn, based on the total number of hours they worked in
#    each department, and the hourly pay rate for the departments in pay_scale dictionary.
# 4. return the total salary computed for the employee
#
# function summary(filename, employee, pay_scale)
# Inputs: 3 inputs
#   - filename : the file to be read, type String
#   - employee : the name of an employee, type String
#   - pay_scale: per hour pay rates for each department, type Dictionary.
# Outputs: 1 output
#   the total salary earned by the employee, type Float.
#
# Example:
# say pay_scale is {'SALES': 15.0, 'SHIP': 20.0, 'TECH': 100.0, 'ADMIN': 150.0}
# For an employee John, who worked for 5, 10, 15, and 20 hours in SALES, SHIP, TECH, and ADMIN departments
# respectively, John's salaries would be 5*15.0 = 75.0, 10*20.0 = 200.0, 15*100.0 = 1500.0, and
# 20*150.0 = 3000.0 for SALES, SHIP, TECH, and ADMIN respectively. The total salary earned by Jd then is
# 75.0 + 200.0 + 1500.0 + 3000.0 = 4775.0

import pandas as pd

def compute_salary(filename, employee, pay_scale):
  list_of_hours = []
  data = pd.read_csv(filename)
  
  for department in pay_scale:
    list_of_hours.append((data[(data.department == department) & (data.employee == employee)].hours.sum()) * pay_scale[department])

  return(sum(list_of_hours))

print(compute_salary("sample.csv", "Jd", {'SALES': 15.0, 'SHIP': 20.0, 'TECH': 100.0, 'ADMIN': 150.0}))
