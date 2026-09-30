'''
OOPS:
------
OBJECT ORIENTED PROGRAMMING SYSTEM
-->OOPS is a programming system used To represent real world object in the software world 
using classes and objects.

WHY OOPS:
---------
-easily we can store the data/code
-easily we can access the data/code easily
-code reusability
-to maintain the code(code maintainance)
-security -Data hiding
------------------------------------------------------
-CLASS--->
is a blueprint/design/plan/model used to create objects.
------------------------------------------------------
-object--->
Physical existency of the class
OR
Object is a real world entity created from a class that contains 
attributes(data) and methods(behavior)
--------------------------------------------------------
NOTE-by using single class we can create multiple objects.
---------------------------------------------------------

HOW TO CREATE A CLASS:
---------------------
--> class ClassName

here, class is a keyword
    ClassName is name of class which should be in Pascal character.

Creating the class, into the class three members are present:
1.Variable (storing the property)
--->types of variable:i)Class variable
                      ii)Instance Variable
                      iii)Local variable

2. Method  (function inside the class)
-->Types of method:i)Instance method
                   ii)Class method
                   iii)Static method 

3. Constructor (special member in the class)
-->(__init__)
--->Types of constructor:i)With Parameterized  Constructor
                         ii)Without parameterized constructor

note-it is not compulsory that this 3 should be always present together

'''

'''Q1.
HOW TO CREATE EMPTY CLASS
-------------------------

class ClassName:
    # None
    pass'''

'''Q2.
HOW TO CREATE OBJECT
--------------------
new_varname=ClassName()
a=ClassName()


class Morning:
    pass
x=Morning()   #object creation

here,class-->keyword
    Morning--->class name
    x--->object

-----------------------------------------
**REFERENCE VARIABLE**:
A variable  reffered to the object
here, x is reference var.
------------------------------------------
'''


# class Qsp:
#     rating="2*"
#     sub="sql"
#     def display(self):
#         print(f'mock rating is {self.rating} and sub is {self.sub}')
# q=Qsp()
# q.display()    #2*, sql
# #modification using class name
# Qsp.rating="1"
# Qsp.sub="python"
# q.display()   #mock rating is 1 and sub is python
# # Qsp.display(q)     #mock rating is 1 and sub is python
# #modification using obj
# q.rating="3*"
# q.sub="java"
# q.display()  #mock rating is 3* and sub is java
# Qsp.display(q) #mock rating is 3* and sub is java

# #modification using class name
# Qsp.rating="4"
# Qsp.sub="manual"
# q.display()  #mock rating is 3* and sub is java
# Qsp.display(q)

'''
class Qsp:
    rating="2*"
    sub="sql"
    def display(self):
        print(f'mock rating is {Qsp.rating} and sub is {Qsp.sub}')
q=Qsp()

#modification using class name
Qsp.rating="3"
Qsp.sub="java"
Qsp.display(q)   #mock rating is 3 and sub is java
q.display()

#modification using obj
q.rating="4"
q.sub="manual"
q.display()  #mock rating is 3 and sub is java
'''

# class Constructor:
#     a=10
#     def __init__(self):
#         name="divya"
#         age=22
#         print(f'name is {name} and \n age is age {age} \n and a={self.a}')
# c=Constructor()
# # Constructor.__init__(c)

# class cons:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# c1=cons("wxyggs",20)
# cons.__init__(c1,"pallavi",23)


class Qsp:
    rating="2*"
    sub="sql"
    def display(self):
        print(f'mock rating is {Qsp.rating} and sub is {Qsp.sub}')
q=Qsp()
# q.rating="5"
# q.sub="py"

Qsp.rating="10"
Qsp.sub="PB"
q.display()
print()


#examples
class School:
    sname="Divyaa"
    sid=10
    def display(self):
        print("student name =",School.sname)
        print("ID is ",School.sid)
s=School()
s.display()
print()

class College:
    clg_name="DIEMS"
    def __init__(self):
        print("college name is ",College.clg_name)
c=College()
print()

