# Empty class:

# class ClassName:
#     pass

# Empty Object:

# New_variable_name=ClassName()

# Example--->

# class Morning:            #Morning----> ClassName
#     pass
# m=Morning()                #m-----> Object

# There are three (3) Members present inside the class :
#     1. variable
#     2. Method
#     3. Constructor


# 1. Variable -----> Variable is a container used to store the values
#       Types of variables--->
#     1. class variable ---> inside class---> access by both classname & object
#     2. Instance variable ---> 
#     3. Local variable

# 2. Method---------> Method present inside the class
#      Type of Methods---->
#     1. Class Method
#     2. Instance Method
#     3. Static Method

# 3. constuctor------> Constructor is special member of class
#    Types of Consturctor
#    1. Default constructor
#    2. Parameterised Constructor

# 1. variables
# Class Vriable:

#variable present inside the class:

# class Employee:
#     name="ravi"             #class variable  
#     age=45                   #class variable
#     sal=1000                  #class variable
#     location="pune"            #class variable

# e=Employee()                     #imp->Because name is a variable, not a function print(e.name) #o/p->ravi

# print(e.age)                     #o/p->45

# print(e)                         #<__main__.Employee object at 0x000002C7F1758980> pointing to main class

# print(Employee.__dict__)         #magic method #whole class object address

# #without paranthesis:
# e1=Employee                      #only pointing main class
# print(e1)                        #main class Object address #<class '__main__.Employee'> #main


# Example

# class Employee:
#     """ THIS CLASS STORE EMPLOYEE DETAILS """
#     name="ravi"             #class variable  
#     age=45                   #class variable
#     sal=1000                  #class variable
#     location="pune"            #class variable

# accessing the values present inside the class to outside

# By using object

# e=Employee()                #Object creation----> e(New_Var_Name)=Employee(ClassName())   
# print(e.name)                #ravi
# print(e.age)                 #45
# print(e.sal)                 #1000 
# print(e.location)            #pune

# By using ClassName

# print(Employee.name)           #ravi
# print(Employee.age)            #45
# print(Employee.location)       #pune
# print(Employee.sal)            #1000

# ---------------------------------> 

# print(Employee.__dict__)    #----------> It used to check how internally the data(variable values) are stored 
# __dict__ is a dictionary that stores all variables and their values of a class or object.

# o/p----> {'__module__': '__main__', 'name': 'ravi', 'age': 45, 'sal': 1000, 
# 'location': 'pune', '__dict__': <attribute '__dict__' of 'Employee' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

# NameSpace----> PLace where Variable and Functions are store

# ---------------------------------------------
# Docstring----->
# “It is a description (documentation) of your class/code”

# print(Employee.__doc__)           #o/p----> THIS CLASS STORE EMPLOYEE DETAILS 

# ----------------------------------------------

# help(Employee)                      
#help() is a built-in function that shows complete information about a class

# Help on class Employee in module __main__:                                                                                             

# Help on class Employee in module __main__:

# class Employee(builtins.object)
#  |  THIS CLASS STORE EMPLOYEE DETAILS
#  |
#  |  Data and other attributes:
#  |
#  |  age = 45
#  |  location = 'pune'
#  |  name = 'ravi'
#  |  sal = 1000


# ----------------------------------------------------

# class Test:
#     """Hello"""                 #doc 
#     x=10
#     y=20

# t=Test()
# T1=Test()

# # To check ID Add 

# print(id(t))                         
# print(id(T1))
# print(id(t.x))              #Same-->x
# print(id(T1.x))              #Same-->x
# print(id(t.y))                #Same-->for y
# print(id(T1.y))                #Same-->for y

# print(Test.__dict__)
# print(Test.__doc__)
# help(Test)

# examp--

# class info:
#     name="crazy"
#     age="15"
#     loc="pune"
# k=info()
# k1=info()

# info.name='shreyy'
# print(info.name)   same
# print(k.name)
# print(k1.name)
# print()
# k.name="ram"
# print(info.name)             #shreyy
# print(k.name)                #ram
# print(k1.name)               #shreyy
# print()
# info.name='shyam'
# print(info.name)             #shreyy
# print(k.name)                #shyam
# print(k1.name)               #shreyy


# instance

# class hello:
#    def hii(self):
#       print("shreyy")
# d=hello()
# d.hii()         #shreyy
# hello.hii(d)    #shreyy

