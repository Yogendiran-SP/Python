import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
weekday_data=pd.read_csv('weekday_data.csv')
weekday_data['Numeric-2']=weekday_data['Numeric-2'].astype(int)
weekday_data['Name']=weekday_data["Name"].astype('category')
sns.set(style="darkgrid")
sns.countplot(x='Name',data=weekday_data, hue='Numeric-2')
plt.show()