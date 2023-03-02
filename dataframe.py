#Converting a dictionary into DATAFRAME and performing operations on it
import pandas

dict1 = {'Name': ['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Zrchana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }

df = pandas.DataFrame(dict1)

print("no of Rows ={R} and columns ={C} DF".format(R=df.shape[0], C=df.shape[1]))
print("Information about DF", df.info())#All info like R,C,dtype etc..
print("DEscribe DF ", df.describe())#Stats of numerical columns like std,mean,min,max....

print("Unique data in a particular column", df['Gender'].unique())
print("No of Unique data in a particular column", df['Gender'].nunique())
print("Unique data in a particular column with count", df['Gender'].value_counts())

male_df = df[(df['Marks'] >=90) & (df['Marks'] <=100) & (df['Gender']=="Male")].__len__()
print(male_df)
female_df = len(df[(df['Marks'] >=90) & (df['Marks'] <=100) & (df['Gender']=="Female")])
print(female_df)

btwn_methd = df[df['Marks'].between(90, 100)]
print(btwn_methd)

avg_marks = df['Marks'].sum()/df.shape[0]
print("Average marks of all studs", avg_marks)
avg_marks_1 = df['Marks'].mean()
print("Average marjs usig MEan methd", avg_marks_1)

#We have used inbuilt methods till now, how to write a method and apply that to columns

def half_marks(x):
    return x/2

print(df['Marks'].apply(half_marks))  # just provide func name without braces.
print("Lambda .......", df['Marks'].apply(lambda x : x+2))
#if i want to add new column to DF

df['Half_marks'] = df['Marks'].apply(half_marks)

print(df)

#Print name and Marks of Female students???

fem_info = df[df['Gender'] == 'Female'][['Name','Marks']]
print(fem_info)

#Sorting

# df2 = pandas.DataFrame(dict1)
# print(df2)
# df3 = df2.copy() #copying same DF to df3
# # df3.sort_values(ascending=True, inplace=True)
# print("DF3 \n", df3)
# df3 = df3['Marks'].sort_values()  #only marks column is sorted and copied to df3
# print(df3)
# df4 = df2.copy()
# df4 = df4.sort_values('Marks') # if we want to copy complete DF after sorting
# print(df4)
# df5 = df4.sort_values(['Marks', 'Name'], ascending=False) #first sort MArks then NAme; simply comb of M & N sorting
# print(df5)