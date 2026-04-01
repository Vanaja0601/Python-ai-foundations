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

#Slicing and Indexing 
a=[1,2,3,4]
print(a[:-1])

ab=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("1 st row in ab is ",ab[0,:])
print("1st column in ab is ",ab[:,0])
print(ab[:2,:2])
print(ab[::2,:])
print(ab[:,::2])
print(ab[:,:-1])
print(ab[:,-1])

data=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(data[1,2])
print(data[2,:])
print(data[:,1])
print(data[:2,3:])
print(data[2:, :3])
print("x IS",data[:,:-1])
print("Y is ",data[:,-1])
print("last row first",data[::-1])

#Numpy Methods and Operations
#we can add ,multiply ...all the arithmatic operations can be performed directly without using loops unlike lists
#Can perform scalar operastions which means if we add a single element it gets added to all the elements of the array ...so as the other operations
num1=np.array([1,2,3])
sq_num=num1*2
print("squares od num1 is ",sq_num)
num2=np.array([4,5,6])
sum=num1+num2
print(sum)
print("testing scalar operation", num1+3)

#Methods -Squareroot,power,cuberoot,absolute
a=np.array([1,2,3,4])
sa_root=np.sqrt(a)
print(sa_root)
sq=np.square(a)
print(sq)
cb=np.cbrt(a)
print(cb)
ab=[-2,-1,3,5]
ab=np.abs(ab)
print(ab)

##Exponential and Logarithm
a=np.array([1,2,3,4])
aexp=np.exp(a)
print("aexp is",aexp)
alog=np.log(a)
print("alog is ", alog)
alog10=np.log10(a)
print("alog10 is ",alog10)
alog2=np.log2(a)
print("alog 2i s",alog2)

##Comaprision operators -can oerform <,>,<=,>=,==,!= operationsd on all the elements of the array at once 
a=np.array([10,20,30,40,50,60])
print(a>30)
##to filter the above tru conditons we can use mask style
mask=a>30
print(a[mask])
##or condition directly in the index--one linear
print(a[a%30==0])

A=np.array([[1,2],[4,3]])
B=np.array([[2,3],[3,4]])
print("A@B is ", A@B)
print(np.dot(A,B))
print("transpose of A",A.T)

Angles_n=np.array([0,20,30,40])
radians_n=np.raidans(Angles_n)
sin_n=np.sin(radians_n)
print("sin_n is ",sin_n)































