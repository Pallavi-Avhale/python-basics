
'''
VARIABLE:
TYPES OF VARIABLES:

1.CLASS VARIABLE
-A variable that is present inside the class is called as class var.


class Employee:
    name="Divya"   #class var.
    age=21
    sal=10000
    location="pune"
e=Employee()        #object-this obj is pointing to whole class object address
e1=Employee         #object is poitnig to main class not to whole class object address
# print(name) nameerror

How to access inside class data outside:
---------------------------------------
Inside the class whatever data is present it is not possible to access the class members outside the 
class directly(we will get NameError),to access this we have two ways:
1.By the help of Class name
syntax--->className.classVariable

ex--> print(Employee.name)
ex--> print(Employee.sal)
ex--> print(Employee.age)
ex--> print(Employee.location)


2. By the help of Object Name

syntax--->ObjectName.classVariable
ex->print(e.name)
ex->print(e.sal)
ex->print(e.location)
ex->print(e.age)
'''

class Employee:
    '''Employee Information'''  #doc string
    name="Divya"   #class var.
    age=21
    sal=10000
    location="pune"
e=Employee()        
print(Employee.name)
print(e.age)
print(Employee.__doc__)  #we will get the heading for the class

'''
NOTE: whenever we are creating any class data will be arrange in key and value pair internally
key-->variable name
value--> element will be present
This structure we call it as NameSpace
syntax:(ClassName.__dict__)

Magic method
print(Employee.__dict__) #key-value pair
print(e.__dict__)         #we will et empty dict.

**DOC string**
---------------
always present in triple qoutes('''''')
-It is description of the class.

ex:print(Employee.__doc__)  #we will get the heading for the class

'''
# class Employee:
#     name="Divya"   #class var.
#     age=21
#     sal=10000
#     location="pune"
# help(Employee)   #gives the complete info about class

#whenever we are creating the class  it won't create a memory address(as it is blueprint of object)
#but when we create object  then it will create memory address

'''how internally the key and value pair are allocated'''
class Test:
    x=100
    y=200
t=Test()
t1=Test()
print(id(Test))
print(id(t))
print(id(t1))
print(id(t.x))
print(id(t.y))

'''
Test----->   key       value           address
(400*500)    ----------------------------------
             x         100              1*100
             y          200             2*200


t-(object)-------->key    address
(100*200)          -------------------
                  x        1*100
                  y        2*200

                  
t1-(object) ---------> key     address
(300*400)            -------------------
                       x        1*100
                       y        2*200
             

'''

'''Point1___if we done any modification in main class it will be affected for both object'''

# before modification
class Test:
    x=100
t=Test()
t1=Test()
print(Test.x)  #100
print(t.x)    #100
print(t1.x)    #100

#modication in main class
# ---->syntax: ClassName.Variable_name=value
Test.x=1000
print(Test.x) #1000
print(t.x)   #1000
print(t1.x)   #1000

print()


'''Point2_____If we done any modification in one oject only affected for that object, 
it will not affect for other object as well as main class'''

#object modification (t)
# --->syntax: Oject_name.Var_name=value
t.x=5000
print(t.x) #5000
print(Test.x)  #1000
print(t1.x)    #1000

#whenever we are doing separate modification in 
# the object then the memory address connection will be lost with the main class

'''Point3_____  Again If we done any modification in main class it will be
 affected for the main class and other object
it will won't affected for previous object ---the reason when we done separate
 modification connection (i.e. separate memory will be created) will be lost'''

#again modification in main class
Test.x="Python"
print(Test.x)   #python
print(t1.x)     #python
print(t.x)      #5000

print()
#ex2:
class Employee:
    name="divya"
    location="pune"
e=Employee()
e1=Employee()

#before modificaton
print(Employee.location)
print(e1.location)
print(e.location)

print()

#modification in class
Employee.location="Deccan"
print(Employee.location)
print(e1.location)
print(e.location)

print()

#modification in one obj
e1.location="Delhi"
print(Employee.location) #deccan
print(e1.location)     #delhi
print(e.location)      #deccan

#again modification in main class
Employee.location="***"
print(Employee.location)   #***
print(e1.location)         #delhi
print(e.location)          #***

print()

#ex3:
class Student:
    sname="divyaa"
    prn=1000
s=Student()
s1=Student()

#before modification
print(Student.prn) #1000
print(s.prn)       #1000
print(s1.prn)      #1000

print()

#modificatin in main class
Student.prn=1500
print(Student.prn) #1500
print(s.prn)       #1500
print(s1.prn)      #1500

print()

#modification in one obj
s.prn=2000
print(Student.prn) #1500
print(s.prn)       #2000
print(s1.prn)      #1500

print()

#again modification in main class
Student.prn=5000
print(Student.prn) #5000
print(s.prn)       #2000
print(s1.prn)      #5000

print()

