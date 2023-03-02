import numpy as np
import pandas

df = pandas.read_csv('Salaries.csv', low_memory=False)
print(df.head())
print(df.columns)

#4.Getting Information About Our Dataset Like Total Number Rows,
# Total Number of Columns, Datatypes of Each Column And Memory Requirement

print(df.info())

#5. Check Null Values In The Dataset
print(df.isnull().sum()) #sum will give total null values in each column

#6.Drop ID, Notes, Agency, and Status Columns
#by default axis =0 (Rows, will get keyerror coz 'testing' is a column so axis =1
df.drop(['testing'], axis=1, inplace=True)
print(df.head(2))

#7. Get Overall Statistics About The Dataframe

print(df.describe())

#8.Find Occurrence of The Employee Names  (Top 5)
print(df['EmployeeName'].value_counts().head())

#9. Find The Number of Unique Job Titles
print(df['JobTitle'].nunique())

#10.Total Number of Job Titles Contain Captain
#if case is not provided it will consider only exact match with CAPTAIN
print(len(df[df['JobTitle'].str.contains("CAPTAIN", case=False)]))

#11. Display All the Employee Names From Fire Department
print(len(df[df['JobTitle'].str.contains('FIRE DEPARTMENT', case=False)]['EmployeeName']))

#12. Find Minimum, Maximum, and Average BasePay
print(df['BasePay'].describe())

#13. Replace 'Not Provided' in EmployeeName' Column to NaN
import numpy
df['EmployeeName'] = df['EmployeeName'].replace('Not provided', numpy.NAN)
print(df['EmployeeName'].tail())

#15. Find Job Title of ALBERT PARDINI
print(df[df['EmployeeName'] == 'ALBERT PARDINI']['JobTitle'])

#16. How Much ALBERT PARDINI Make (Include Benefits)?
print(df[df['EmployeeName'] == "ALBERT PARDINI"]['TotalPayBenefits'])

#17.Display Name of The Person Having The Highest BasePay
#print(df[df['BasePay'].max()]['EmployeeName'])
#print(df[df['BasePay'].max() == df['BasePay']]['EmployeeName'])

#18.Find Average BasePay of All Employee Per Year
#print(df.groupby('Year').mean()['BasePay'])

#19. Find Average BasePay of All Employee Per JobTitle
#print(df.groupby('JobTitle').mean()['BasePay'])

#20. Find Average BasePay of Employee Having Job Title ACCOUNTANT
print(df[df['JobTitle'] == "ACCOUNTANT"].mean())

#21. Find Top 5 Most Common Jobs

print(df['JobTitle'].value_counts().head())
