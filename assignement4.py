# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 08:23:08 2025

@author: sakuc
"""

'''
1.	Create a heatmap of a correlation matrix for a dataset with numerical features.
•	Use the iris dataset from Seaborn.
•	Display the correlation matrix as a heatmap with annotations.
'''
#CODE::==>
import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset("iris")

corr_matrix = iris.corr(numeric_only=True)

plt.figure(figsize=(7,5))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt=".2f")
plt.title("Heatmap for coorrelation matrix")
plt.show()


#########################################################################################################
##########################################################################################################
#2.	Visualize the distribution of test scores for students from three different schools.
    #•	Data includes score and school columns.
    #•	Use a box plot to compare distributions

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data={
      'Scores':[50,56,74,70,56,30,98,80,86,45,30,65,85,84,50],
      'Schools':['A','A','C','A','B','B','C','B','A','C','B','B','A','C','C']}
df=pd.DataFrame(data)

plt.figure(figsize=(7,5))

sns.boxplot(x='Scores',y='Schools',data=df)
plt.title("Comparing Distribution of Scores From Different Schools")
plt.xlabel("Scores in test")
plt.ylabel("Schools")
plt.show()


#########################################################################################################
##########################################################################################################
#que 3
'''
3.	Plot a bar chart showing the number of products sold by a store across five different categories.
•	Categories: Electronics, Clothing, Groceries, Furniture, Toys
•	Add color to each bar.
•	Rotate x-axis labels and annotate the bars with their values.
Note: Use below data
categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
sales = [150, 200, 300, 120, 90]
colors = ['blue', 'green', 'orange', 'red', 'purple']

'''
categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
sales = [150, 200, 300, 120, 90]
colors = ['blue', 'green', 'orange', 'red', 'purple']

plt.figure(figsize=(8,5)) #width and height of the figure

bars=plt.bar(categories,sales,color=colors)
plt.title("Number of product sold by the stores")
plt.xlabel("Categories")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(axis='y')


for bar in bars:
    height=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2.,height+5,f'{height}',ha='center')
    
plt.tight_layout()
plt.show()



#########################################################################################################
##########################################################################################################
#que 4
'''
4.	Create a line chart showing the monthly average temperature of a city over a year.
•	x-axis: Months (January to December)
•	y-axis: Temperature (in Celsius)
•	Add a title, axis labels, and gridlines.
•	Customize the line style (e.g., dashed, color, markers)

'''
months=['jan','feb','mar','apr','may','jun','july','Aug','sep','acto','nov','Dec']
temperature=[16,17,19,26,27,28,17,15,13,10,13,17]

plt.figure(figsize=(9,5))

plt.plot(months,temperature,linestyle='--',color='red',marker='o')
plt.title("Diff Temparature Across diff Months")
plt.xlabel("Months")
plt.ylabel("Temparature in {c}")
plt.grid(True)
plt.show()


#########################################################################################################
##########################################################################################################
#que 5
'''
5.	Using the tips dataset from Seaborn:
•	Create a scatter plot showing the relationship between total_bill and tip.
•	Color the points by sex and vary the size by size (number of people at the table).
•	Add titles and axis labels.

'''
tips = sns.load_dataset("tips")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', size='size', palette='viridis', sizes=(20, 200))
plt.title("Tip vs Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.legend(title="Sex / Size", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()






















