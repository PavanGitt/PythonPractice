import numpy as np
#
# data = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=True)
#
# print("What is type of data.....\t", type(data))
# print("No of dimensions ...\t", data.ndim)
# print("Shape of data...\t", data.shape)
# print("Size of data...\t", data.size)
#
#
# # send_to_file = (data[:, 4]).astype(int)
# # print(send_to_file)
# # np.savetxt('data.txt', send_to_file, delimiter=',', newline='\t')
#
# #print fare amount recvd for total payment of 105.6
# d1 = data[data[:, -2] == 105.6, -6]
# print(d1)
# #if any value in particular column is given and to fetch its adjacent values
#
# #fetch longest distance travelled in Jan month
# jan_month_data = (data[data[:, 1] == 1, -8])
# print(max(jan_month_data))
# #this will give longest distance travelled in Jan month
#
#
# # Complete feb month data, like total distance,tip amount,total amount who paid through payment option 2
#
# feb_month = (data[data[:, 1] == 2, 1:16])   # this parses feb month details
# feb_2 = (feb_month[feb_month[:, -1] == 2, :]).astype('int')  # from feb month data it parses payment mode 2
# # astype('int') will change existing float to int and here assigned to feb_2
# # print(feb_month)
# print(feb_2)
# # np.savetxt('data.txt', feb_2, delimiter=',', newline='\n')
#
# total_distance = feb_2[:, 6]
# print(total_distance)
# print(total_distance.shape)
# print(np.sum(total_distance))   # total distance travelled in Feb month
#
# total_tip = feb_2[:, -3]
# print(np.sum(total_tip))    # total tip recvd in feb
#
# total_amount = (feb_2[:, -2]).sum()  #total amount
# print("total amount %s", total_amount)
#


data = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=True)

print("What is type of data.....\t", type(data))
print("No of dimensions ...\t", data.ndim)
print("Shape of data...\t", data.shape)
print("Size of data...\t", data.size)


# send_to_file = (data[:, 4]).astype(int)
# print(send_to_file)
# np.savetxt('data.txt', send_to_file, delimiter=',', newline='\t')

#print fare amount recvd for total payment of 105.6
d1 = data[data[:, -2] == 105.6, -6]
print(d1)
#if any value in particular column is given and to fetch its adjacent values

#fetch longest distance travelled in Jan month
jan_month_data = (data[data[:, 1] == 1, -8])
print(max(jan_month_data))
#this will give longest distance travelled in Jan month


# Complete feb month data, like total distance,tip amount,total amount who paid through payment option 2

feb_month = (data[data[:, 1] == 2, 1:16])   # this parses feb month details
feb_2 = (feb_month[feb_month[:, -1] == 2, :])   # from feb month data it parses payment mode 2
# print(feb_month)
print(feb_2)
# np.savetxt('data.txt', feb_2, delimiter=',', newline='\n')

total_distance = feb_2[:, 6]
print(total_distance)
print(total_distance.shape)
print(np.sum(total_distance))   # total distance travelled in Feb month

total_tip = feb_2[:, -3]
print(np.sum(total_tip))    # total tip recvd in feb

total_amount = (feb_2[:, -2]).sum()  #total amount
print("total amount %s", total_amount)


