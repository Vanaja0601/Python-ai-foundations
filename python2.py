#Enums in python 
from enum import Enum
class States(Enum):
    INACTIVE=0
    ACTIVE=1
print(States.ACTIVE.value)
print(States(0))
print(States['INACTIVE'])
print(list(States))
print(len(States))

# complex numbers in python
complex_num=2+3j
num=complex(2,5)
print(complex_num.imag ,complex_num.real)
print(num.real,num.imag)
num2=abs(-5.5)
print(num2)
num3=round(5.078,2)
print(num3)

#                 **** About Lists in python ****
#Lists are mutable in nature and ordered and allows duplicates 
list1=["dogs",2,3,"pets",True]

print("dogs" in list1)
print(5 in list1)
print(list1[4]==True)
print(list1[-1])
print(list1[2:4])
list1[2]="van"
print(list1)
print(len(list1))
list1.append("Vannu")
print(list1)
list1.extend([5,6])
print(list1)
list1+=[8,9]
print(list1)
# to remove an element by value using remove method
list1.remove(5)
print(list1)
#pop method is used for removing any specifi value if specifed otherwise removes last element in the list
print(list1.pop(6))
print(list1)
#by using del method we can remove elements by using index 
del list1[1]
print(list1)
#at once we can remove multiple elemnts by using following methods
del list1[:4]
print(list1)
list1.insert(1,20)
print(list1)
list1=[x for x in list1 if x!=20 and x!=8 ]
print(list1)
#to insert one element ,list,tuple at a index we use insert method where index followed by value 
# where as to insert multiple va;lues at a particualr position we can use this slicing trick
list1[1:1]=[20,30]
print(list1)
list1[2:2]=[40,50]
print(list1)
#to sort a list we need to have same type of elements in the list
ran=["Bobby","hari","eagle","Cat","bob","Dog"]
rancopy=ran[:]
ran.sort()
print(ran)
#the above sorting gave me all the capital letter words sorted first and then small letters starting words later
#if i dont want this i can do the below irrespective of capital and lower
print(rancopy)
rancopy.sort(key=str.lower)
print(rancopy)
#withopout modifying if we want to sort a list we can do it in this way 
ran_new=["Bobby","hari","eagle","Cat","bob","Dog"]
print(sorted(ran_new,key=str.lower))
print(ran_new)

#          ***Tuples in python ***
#Tuples are immutable in nature, ordered collection of items and allows duplicate values 
names=("vannu","Vinnu","syam")
print(len(names))
#names.sort()
print(sorted(names,key=str.lower))
print(names)

#we cannot modify the orignal tuple but we can create new tuple by adding to another tuple
#new_fam=names+("Radha","SSN")
new_fam=()
new_fam+=names
print(new_fam)

#Dictionaries -are mutablke
dog={"name":"vv","age":2,"color":"white","weight":10}
print(dog["color"])
dog["color"]="brown"
print(dog["color"])
#by using get method we can return a value which is not in the dictioanry as below 
print(dog.get("height",4))
print(dog.pop("name"))
print(dog)
#print(dog.pop)-this doesn't work to remove last item -only specified item
#popitem method helps in removing the last item
print(dog.popitem())
print(dog)
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))
dog["gavfood"]="bisc"
print(dog)
dogcopy=dog.copy()
del dog["color"]
print(dog)
print(dogcopy)
#Sets-{} same like dict but not key value pairs,not ordered,no duplicates
set1={"Roger","bb","vv"}
set2={"bb","vv"}
intersect=set1 & set2
print(intersect)
print(type(intersect))
union=set1 | set2
print(union)
#a-b gives all the vlues in a which are not common in b
diff=set1-set2
print(diff)
#items present in a>b then we get true if all the items in b are present in a if not false and viceversa a<b
mod=set1>set2
print(mod)
print(list(set1))
print("vv" in set2)

##Functions
def changeVal(value):
    value=2
    #print(value)

val=1
changeVal(val)
print(val)
##in the above function val value is not changed as int,strng,tuple are immutable 
#where as in the below function val1 value gets changed as it points to same dictionary unstead of creating new as dict,set,list are mutable
def changeVal1(value):
    value["name"]="vv"
    #print(value)

val1={"name":"bb"}
changeVal1(val1)
print(val1)
#Nested Function
def ph(phrase):
    def say(word):
        print(word)
    words=phrase.split(' ')
    for word in words:
        say(word)
ph('i am gng to uni tmr')