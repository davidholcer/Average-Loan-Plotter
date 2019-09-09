#importing libraries
import pandas as pd
import numpy as np
from IPython.display import display, HTML
import matplotlib.pyplot as plt

#reads data
a = pd.read_csv('./data/home_ownership_data.csv')
b = pd.read_csv('./data/loan_data.csv')

#merges files (considering the same id)
hs = pd.merge(a, b)

#showing the mean of the loan amnts organized by home_ownership.
c=hs.groupby(['home_ownership'], as_index=False).agg({'loan_amnt':'mean','int_rate':'mean'})

my_colors = [(0.235, 0.478, 0.537), (0.933, 0.960, 0.858),(0.996, 0.372, 0.333)]
#plots the merged data on a bar graph
c.plot.bar(lw=2, legend=False,color=my_colors,x='home_ownership',y='loan_amnt',fontsize=11)
#formatting
plt.xlabel('Household Type',fontname='Aller',fontsize=12)
plt.title('Average Loan Amounts per Household Type',fontname='Arial',fontsize=15)
plt.ylabel('Average loan amounts ($)',fontname='Arial',fontsize=12)
#showing the plot
plt.show()
