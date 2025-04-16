# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 08:14:07 2025

@author: sakuc
"""

#1.	Write a NumPy program to create an element-wise  
#comparison (greater, greater_equal, less and less_equal) of 
#two given arrays.
import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([15, 20, 25, 50, 45])

greater = np.greater(array1, array2)
greater_equal = np.greater_equal(array1, array2)
less = np.less(array1, array2)
less_equal = np.less_equal(array1, array2)

print("Greater comparison:\n", greater)
print("Greater equal comparison:\n", greater_equal)
print("Less comparison:\n", less)
print("Less equal comparison:\n", less_equal)







#2.
'''2.	You are given the following data about employees in a company:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 45, 28],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining_Year': [2018, 2016, 2015, 2019, 2020]
            }
'''


'''Create a DataFrame from the above dictionary and Display the following:
o	The first 2 rows
o	The column names
o	Data types of each column
o	Summary statistics for numeric columns.
'''
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 45, 28],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining_Year': [2018, 2016, 2015, 2019, 2020]
            }

empl_data=pd.DataFrame(data)
empl_data
empl_data[0:2]

empl_data.columns.values

empl_data.dtypes


empl_data.describe()


'''3.	Extend the DataFrame from Question 2:
•	Add a new column called Salary with values: [50000, 60000, 70000, 65000, 48000].
•	Calculate a new column Experience as 2025 - Joining_Year.
•	Create a new column Seniority:
o	'Junior' if experience < 5 years
o	'Mid' if 5 <= experience < 8 years
o	'Senior' if experience >= 8 years
'''
empl_data['Salary']=[50000,60000,70000, 65000, 48000]
empl_data

empl_data['Experience']=2025-empl_data['Joining_Year']


lst=[]

for i in empl_data['Experience']:
    if i<5:
        lst.append('Junior')
    if 5<=i and i<8:
        lst.append('Mid')
    else :
        lst.append('Senior')
        
empl_data['Seniority']=lst


'''4.	Write a NumPy program to compute the multiplication of two given matrixes.
 p = [[1, 0], [0, 1]]
 q = [[4, 2], [1, 3]]
'''
import numpy as np

p = np.array([[1, 0], [0, 1]])
q = np.array([[4, 2], [1, 3]])

result = np.multiply(p, q)

print(result)














