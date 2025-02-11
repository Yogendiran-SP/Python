import pandas as pd
import numpy as np
weekday_data=pd.read_csv('weekday_data.csv')
weekday_data=weekday_data.reset_index()
copy_data2=weekday_data.copy(deep=False)
copy_data=weekday_data.copy(deep=False)
copy_data["Numeric"]=copy_data["Numeric"].fillna(copy_data["Numeric"].median().astype(int))
weekday_data["Numeric"]=copy_data["Numeric"]
copy_data["Abbreviation"]=copy_data["Abbreviation"].fillna(copy_data["Abbreviation"].value_counts().index[0])
weekday_data["Abbreviation"]=copy_data["Abbreviation"]
copy_data["Name"]=copy_data["Name"].fillna(copy_data["Name"].mode()[0])
weekday_data["Name"]=copy_data["Name"]
copy_data2=copy_data2.apply(lambda x:x.fillna(x.mean()) if(x.dtype =='int64') else x.fillna(x.value_counts().index[0]))
print(copy_data.isnull().sum())
print(copy_data, "\n",weekday_data)
print(weekday_data.isnull().sum())