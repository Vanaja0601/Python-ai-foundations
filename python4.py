square_num=lambda a:a*2
print(square_num(3))

multiply= lambda a,b:a*b
print(multiply(2,4))

#MAP,FILTER,REDUCE
##map is used for applying function to each element
numbers=[1,2,3]
def double(a):
    return a*2
result=map(double,numbers)
print(list(result))

#RECURSION:a function calling itself is called reccursion
def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)

print("factorial of n is  "+str(factorial(5)))

#Args and kwargs 
def add_numbers(*args):
    print(sum(args))

add_numbers(1,2,3,4)
##kwargs stores value as a dictionary where as args stores value as a tuple 
def std_info(**kwargs):
    print(kwargs)
std_info(name="van",age=24)

##Exceptions:excpetion is an error occured at execution time -it has to be handled to preven the program from crashing 
#we use try-except-finally for exceptiuon handling in python

try:
    result33=2/0
except ZeroDivisionError:
    print("its a division by zero")
finally:
    result33=0
    print(f'result is {result33}')
##we can create our own exception as below 
"""raise Exception("its a some errorrrrr")"""

#We can create a Excpetion call also 
class XnotFoundException(Exception):
    #pass
    print("inside exception class ")

try:
    raise XnotFoundException()
except XnotFoundException:
    print("exception excecuted ")
finally:
    print("it means finally block is executed")
    



