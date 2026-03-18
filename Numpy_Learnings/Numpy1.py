import numpy as np
#print (np.__version__)
a=np.array([1,2,3]) #-data in a single row 
print(a)
data=np.array([[1,2,3],[4,5,6]]) #list of sublists for 2d -lets say a table-rows and colums 
print(data)
#data stored in 3d-for example to store images in ml--lets say it as list of tables
ThreeD=np.array([[[1,2],[3,4]],[[5,6],[6,7]]])
print(ThreeD)
print(ThreeD.shape)
all_Zeroes=np.zeros((3,3))
print(all_Zeroes)
all_Ones=np.ones((2,3))
print(all_Ones)
Identity_matrix=np.eye(3)
print(Identity_matrix)
#Evenly spaced numbers like a range-Start,end,step
r=np.arange(1,10,2)
print(r)
#Evenly spaces numbers bw 2 numbers - here u can print 5 numbers between 0,1 including them
l=np.linspace(0,1,5)
print(l)

#Num_1_10=np.array([i for in range(1,11)])
num_1_10=np.arange(1,11)
print(num_1_10)
Array_3_0=np.zeros((3,3))
print(Array_3_0)
Even_1_100=np.linspace(1,100,6)
print(Even_1_100)
table_c=np.array([[1,25,88],[2,30,95],[3,22,78]])
print(table_c)
##
a=np.array([[10,20,30,40],[50,60,70,80,],[90,100,110,120]])
print("no of dimentions is ",a.ndim)
print("no of samples and features ",a.shape)
print("total no of elemts ",a.size)
print("data typw of a is ",a.dtype)
print("item size of data stored is ",a.itemsize)
print("total size is ",a.size*a.itemsize)
a=a.astype(np.float32)
print("datatpe of a after convertion is ",a.dtype)
print("item sixe afte convertion ",a.itemsize)
print("total size occupied after converuton ",a.size*a.itemsize)


