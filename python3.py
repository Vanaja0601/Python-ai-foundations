#Object Oriented Programming in Python
#Class is a blue print
#Object is an instance of a class
#Self is used to refer current object-must be specified with a method in a class
class dog:
    def __init__(self,name,age): #constructor can be created by using __init__
        self.name=name
        self.age=age

    def bark(self):
        print("woof")
    
Roger=dog("vv",2) # creating object of a class
print(type(Roger))
print(Roger.name)
Roger.bark()

##Inheritance -acquiring properties from parwents class to chikd class
class Animal:
    def walk(self):
        print("Animal cam walk")

class Cat(Animal): #for inheriting a  class we just need to give the parent class name in the brackets of child class declaration 
        
    def __init__(self,name,age):
        self.name=name
        self.age=3

    def run(self):
        print("cat can run")
        
cc=Cat("catc",1)
print(cc.name)
print(cc.age)
cc.run()
cc.walk()

##Modules
#we can create python file with some functions and we can use thw functions from that file by importing the file or particular function
#import dog (dog.py is my file name )
#if file created is in a library or a folder (lib)then u have to create __init__.py file so that the created file can be accessed as below
#from lib import dog or from lib.dog import bark(for specific function)
#import math
#print(math.sqrt(3))
from math import sqrt
print(sqrt(2))














    
    

    

