#Assgn 0.1
print("Hello World")
s="Hello Earth"
#Assgn 0.2
i=1
type(i)
i+=3
print(i)
#Assign 0.3
mylist=[1,2,3,4,5]
first_element=mylist[0]
fourth_element=mylist[3]
print("First element is "+ str(first_element) +" 4th element is "+str(fourth_element))
mylist.remove(3)            
print(mylist)
mylist.insert(2,3)
print("list after inserting 3 ")
print(mylist)
mylist.pop(2)
print(mylist)
#by slicing 
firsthalf=mylist[0:2]
secondhalf=mylist[2:]
mylist=firsthalf+[3]+secondhalf
print(mylist)
del mylist[2]
print(mylist)
#Assign 0.4
for i in range(3,11):
    print(i)
for i in range(12):
    if(i%2==0):
        print(i)
mylist2=[1,"Jack",5.0,6,9,13]
a=0
for i in mylist2:
    print(str(i) +"-----" + str(a) )
    a+=1
mylist3=[2,3,5,3.0,7,3,9,3.0]
for v in mylist3:
    if not v==3:
        mylist3.remove(v)
print(mylist3)

#Assign 0.5
mylist4= [n for n in range(2,21) if i%2==0]
print(mylist4)
mylist5=[(n,n*n) for n in range(1,10)]
print(mylist5)
mylist6=[n for n in range(1,1001)if n%36==0]
print(mylist6)  
mylist7=[(i,j)for i in range(1,11) for j in range(1,11) if i+j<50 and (i%j==0 or j%i==0)]
print(mylist7)
mylist8=[i for i in mylist3 if i==3]
print(mylist8)

#Assgn 0.6
def sqr(x):
    return x*x
sqr_num=sqr(3)
print(sqr_num)

def modify(li):
    li[-1]="modified"
    return li
new_li=modify(["23",6,4,6,3])
print(new_li)

a=3
def fun(a):
    print(a)
print(a)
print(fun(2))

#calling a function without passing a parameter(not even the () bracket) gave none as output
def fun(x):
    return 2*x
f=fun

def left():
    print("left")
def right():
    print("right")
def walk():
    for i in range (1,11):
        if i%2==0:
            right()
        else:
            left()
walk()

#I did not got any error on using more than 1 return but i got o/p as 1 for all the 3 prints
#oncce the first return is hit ,the rest is dead code not executed
def triple_fun():
    return 1
    return 2
    return 3
print(triple_fun())
print(triple_fun())
print(triple_fun())

#Yield is a generator which pauses the function and continues with next iteration where as return stops the function execution
def triple_yield():
    yield 1
    yield 2
    yield 3
print(triple_yield()) #o/p--<generator object triple_yield at 0x0000022AF85F5480> it is not a normal function it results in generator object which continues the execution of function
for i in triple_yield():
    print(i)

#Assign 0.8





