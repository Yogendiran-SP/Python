import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Importing the data
data_income = pd.read_csv('income.csv', na_values = ["?"])
data = data_income.copy()

# Exploratory Data Analysis
print(data.info())

#Converting the object data type to category
data['JobType'] = data['JobType'].astype('category')
data['EdType'] = data['EdType'].astype('category')
data['maritalstatus'] = data['maritalstatus'].astype('category')
data['occupation'] = data['occupation'].astype('category')
data['relationship'] = data['relationship'].astype('category')
data['gender'] = data['gender'].astype('category')
data['nativecountry'] = data['nativecountry'].astype('category')
data['SalStat'] = data['SalStat'].astype('category')

#Checking the data types
print(data.dtypes)

# Filling the missing values
print("\nMissing Values of occupation:")
data['occupation']=data['occupation'].fillna(data['occupation'].mode()[0])
print(data['occupation'].isnull().sum())
print("\nMissing Values of JobType:")
data['JobType']=data['JobType'].fillna(data['JobType'].mode()[0])
print(data['JobType'].isnull().sum())
print("\nMissing Values of gender:")
data['gender']=data['gender'].fillna(data['gender'].mode()[0])
print(data['gender'].isnull().sum())

# Printing Fill the missing values
print("\nOcupation:",data['occupation'].value_counts())
print("\nJobType:",data['JobType'].value_counts())
print("\nGender:",data['gender'].value_counts())

# Checking the datatype of occupation
print("\nOccupation:")
print(data['occupation'].unique())
print("\nJobType:")
print(data['JobType'].unique())
print("\ngender:")
print(data['gender'].unique())

# Checking datatype of missing values
print("\nMissing Rows of the whole data:")
missing = data[data.isnull().any(axis = 1)]
print(missing)

# Checking for missing values
print("Missing Values:",data.isnull().sum())

print("\nSummary of the data:",data.describe(include='all'))