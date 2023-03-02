#Exercise on Ecommerce csv file
import pandas

df = pandas.read_csv('Ecommerce_Purchases') #delimiter=',', nrows=5)
# print(df[['Lot', 'Credit Card']])
# print(df.head(10)) #display top 10 rows, by default head() will display 5
# df.tail(10)  # ""     ""         ""           ""
# print(df.dtypes) # Dtype of each column
# print(df.isnull().sum()) #all null values in  dataset
# print(df.shape)
# print(df['Purchase Price'].max())
# print(df['Purchase Price'].min())
# print(df['Purchase Price'].sum()/df.shape[0])
# print(df['Purchase Price'].mean())
#
# print(df[df['Language'] == 'fr'].shape[0]) #No of french lang people
# print("len of Fr peo[ple", len(df[df['Language'] == 'fr'])) #using len
#
# print(df[df['Job'].str.contains('engineer', case=False)]['Job'].count()) #fetch all em=ngineers data
# #str.contains methjod will search in columnn & return T,  F
#
# print(df[df['IP Address'] == "132.207.160.22"]['Email']) #find mail of gut with that ip
#
# #people usimg MAstercard CC and purchased above 50$
# print(len(df[(df['CC Provider'] == "Mastercard") & (df['Purchase Price'] >= 50)]))
#
# #find email of person with CC number
# print(df[df['Credit Card'] == 6011456623207998]['Email'])
#
# #how many people purchased in AM , PM
# print(df['AM or PM'].value_counts())
#
# #how many people have CC expiry in 2020
# #print(df['CC Exp Date'].head())
# print(len(df[(df['CC Exp Date'].str.contains('/20'))]))
# print(len(df[df['CC Exp Date'].apply(lambda x:x[3:] == "20")]))

#top 5 email providers
#print(df['Email'].head())

# yahoo = 0
# gmail = 0
# other = 0
# def top_mail():
#     l1= []
#     for x in df['Email']:
#         if x.split('@')[1] == "yahoo.com":
#             l1.append()
#         elif x.split('@')[1] == "gmail.com":
#         else:
#             other = +1
#     print(f'Yahoo users {yahoo}\t Gmail users {gmail}\t other users{other}')
#
# top_mail()
print(df)
l1 = []
yahoo = (len(df[df['Email'].str.contains('yahoo.com')]))
gmail = (len(df[df['Email'].str.contains('gmail.com')]))
other = (len(df[df['Email'].str.contains('reed.com')]))
print(yahoo, "\t", gmail, "\t", other)

