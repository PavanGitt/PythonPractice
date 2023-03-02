import numpy
import pandas

df = pandas.read_csv('adult.csv')
print(df.columns)

print(df.shape)
print(df.info())

# Fetch Random Sample From the Dataset (50%)
print(df.sample(frac=0.50))  #this gives random data from DF and frac decides how much % of random data

#Check Null Values In The Dataset
print(df.isnull().sum())

#Perform Data Cleaning [ Replace '?' with NaN ]

data = (df.replace('?', numpy.NAN))
print(data.tail(20))

# Drop all The Missing Values
df = pandas.read_csv('adult.csv')
print("shape before dropping %s", df.shape)
df.dropna(how='any', inplace=True)
print("Shape after dropping %s", df.shape)

#9. Check For Duplicate Data and Drop Them

var = df.duplicated().any()
print(var)

df.drop_duplicates(inplace=True)
print(df.tail(20))
print("shape %s", df.shape)

#drop coliumns
df.drop(columns=['age', 'workclass'], inplace=True)
print(df.tail())

