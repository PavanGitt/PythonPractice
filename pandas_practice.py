import pandas as pd
import os

df = pd.read_csv('C:\\Users\\admin\\OneDrive\\Desktop\\My_Git\\Numpy\\nyc_taxis.csv')

# df1 = df['pickup_year'].head(4) #directly by giving columns name we can access its data.
# print(df1)
#
# df1_1 = df.pickup_year.tail(4) # it also do the same job.#in numpy we have to access them using R , C indexes.
# print(df1_1)
#
# df1_2 = df[['pickup_month', 'pickup_day']].head(2) #multiple object fetching
# print(df1_2)
# df2 = (df.tolls_amount.head(2)).max() #max toll amount in first 2 columns
# print(df2)
#
# df2_1 =(df['tolls_amount']).max()
# print(df2_1)
#
# mean_value = (df['payment_type'].head(5)).mean()/;
# print(mean_value)
#
# median_value = (df['payment_type'].head(5)).median()
# print(median_value)
#
# tip = (df[df.tip_amount ==52.8].total_amount).head(4)
# #where tip_amount is 69.99 give me first 4 its total_amount values
# #in numpy it is done with indeces here errors while using index , directly column name works.
# print(tip)
#
# toll_row = df[df.total_amount==131.99]  #give the row where total_amount =131.99
# print(toll_row)

# d1 = df[['trip_distance','trip_length','total_amount']].head(4)
# print(d1)
#
# excel_data = pd.read_excel('C:/Users/admin/Downloads/Excel_test.xlsx', 'Sheet2')
# excel_data.set_index('Sales', inplace=True) #making sales as index and that change will be affected on original data
#as we made inplace flag to True.
# print(excel_data)
#

#csv = pd.read_csv('C:/Users/admin/Downloads/myFile0.csv', delimiter=',')
# csv.set_index('firstname', inplace=True)
# print(csv[csv['profession']=='firefighter']) #only printing details whose profession is firefighter
csv = pd.read_csv('C:/Users/admin/Downloads/myFile0.csv', delimiter=',', index_col='firstname', nrows=4)#it sets index as firstname and then print data accrd to that
#similar to setindex function, this will do same but at the time of reading we are doing that, nrows = no of rows u want to read.
#print(csv[csv['profession'] == ('developer' or 'doctor')]) #print id of people whose profession is developer

#print(csv)

#===========Accesing rows data=============

# print(csv.iloc[[1]]) #prints data related to row 1
# print(csv.iloc[[2,6]]) #prints data form rows 2 to 5 index
# print(csv.loc[['Flory', 'Gilda']]) # prints data where it found 'Flory' string

#print(csv[csv['lastname'].str.contains('Poll')]) #contains method is supported for string formats.

#====================Converting a dict to a DF====================
# my_dict = {'name': ["a", "b", "c", "d", "e","f", "nan"],
#             'age' : [20,27, 35, 55, 18, 21, 35],
#             'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
# #if length is not same then Value Error
#
# dict_to_df = pd.DataFrame(my_dict)
#
# print(dict_to_df)
# #+++++++Writing to a CSV file
# dict_to_df.to_csv('dict_to_csv', index=False, sep="\t", columns=['name', 'age'])

# #Read from clipboard
#
# clip = pd.read_clipboard()
# print(clip)  #copied content convertd to DF formt
#
# #REad from excel

exl = pd.read_excel('C:/Users/admin/Downloads/Employee+Sample+Data/EmployeeSampleData.xlsx', sheet_name='Data', nrows=15)
#sheetname is must,
exl.to_excel(excel_writer='Employee.xlsx', sheet_name='EmployeeData', na_rep="NA")
#excel_writer -> need to provide file name with extension,

exl_data = pd.read_excel('Employee.xlsx', sheet_name='EmployeeData', index_col=0)
print(exl_data.columns)
d1 = exl_data[exl_data['Annual Salary'] > 100000]['Full Name']
print(d1)