'''

**Magic method:any method starting with __ and ends with __(double underscore) 
is known as magic method
--------------------------------------------------------------------------------
CONSTRUCTOR:
-----------
-It is a special member  in the class
-It is defined as ----> __init__
-Once declaring constructor and we create the object automatically 
 the constructor will be executing.
-No need to call manually.
-Without object we cannot execute constructor
-Therefore, Object creation is mandatory
-By default it will accept self as a parameter.

---------------------------------------------------
syntax:
class ClassName:
    def __init1__(self):
        statement
object=ClassName()

#by calling thorugh class name
ClassName.__init__(Object)
--------------------------------------

HOW CONSTRUCTOR IS EXECUTING---->
Two ways:
1. creating object and automatically executing constructor
2. Manually calling using Class name
------>syntax: ClassName.__init__(objectName)

TWO TYPES OF CONSTRUCTOR:
1.Default constructor(without parameter--i.e. self)
2. Parameterized constructor (with parameters...
                             it will accept variable name i.e. parameters)






'''
#ex1
class Test:
    def __init__(self):
        print('constructor method')
t=Test()     #automatically constructor will be executed...no need to call manually
Test.__init__(t)   #we can call manually using class name (explicitly we need to pass object)
print()
#ex2
class Student:
    def __init__(self):          #constructor
        print('Student class')
    def __init__(self):          #constructor
        print('Student class 2')
s=Student()                      #object creation
#calling through class name
Student.__init__(s)
#NOTE: for one class create only one constructor .Because onl y latest one constructor will 
#get executed---->bcoz python is dynamically typed language.

print()
'''
class Student:
    def __init__(self):          #constructor
        print('Student class')
    def __init__(self):          #constructor
        print('Student class 2')
    def Show(self):
        print('show method')
s=Student()                      #object creation
s.Show()
#calling through class name
# Student.__init__(s)
# Student.Show(s)
'''

'''DEFAULT CONSTRUCTOR'''
#ex3
class Employee:
    def __init__(self):
        print('employee class')
e=Employee()
Employee.__init__(e)
print()
        

#ex4
class Employee:
    def __init__(self):
        self.name="Divyaa"              #{sel.new_var=value}
        self.age=21
        print(f'Employee name : {self.name}')
        print(f'employee age is {self.age}')
e1=Employee()
e2=Employee()
e3=Employee()
'''Drawback of default constructor:
in default parameter when we assign the value we cannot change the value again.
That is we will get the same o/p:
Employee name : Divyaa
employee age is 21
Employee name : Divyaa
employee age is 21
Employee name : Divyaa
employee age is 21 '''

#ex5
class Account:
    def __init__(self):
        self.bank_name="sbi"
        self.holder_name="xyz"
        self.bal=10000
        self.add="pune"
        print(f'bank name is {self.bank_name}\n'
              f'acc holder name is {self.holder_name}\n'
              f'balane is {self.bal}\n'
              f'address is {self.add}\n')
a=Account()
print()
# bank name is sbi
# acc holder name is xyz
# balane is 10000
# address is pune

#ex6
class Account:
    def __init__(self):
        self.bank_name="sbi"
        self.holder_name="xyz"
        self.bal=10000
        self.add="pune"
    def Details(self):
        print(f'bank name is {self.bank_name}\n'
              f'acc holder name is {self.holder_name}\n'
              f'balane is {self.bal}\n'
              f'address is {self.add}\n')
e=Employee()
# e.Details()

# class Flipkart:
#     def __init__(self):
#         self.prod_name="iphone"
#         self.total_prod=5
#         self.ammount=70000
#         self.color="black"
#         self.add="pune"
#         print(f'product name is {self.prod_name}\n'
#               f'total products are {self.total_prod}\n'
#               f'price is {self.ammount}\n'
#               f'color is {self.color}\n'
#               f'address is {self.add}')
# f=Flipkart()
print()

#ex7
class Flipkart:
    def __init__(self):
        self.prod_name="iphone"
        self.total_prod=5
        self.ammount=70000
        self.color="black"
        self.add="pune"
    def details(self):
            print(f'product name is {self.prod_name}\n'
              f'total products are {self.total_prod}\n'
              f'price is {self.ammount}\n'
              f'color is {self.color}\n'
              f'address is {self.add}')
f=Flipkart()
Flipkart.details(f)
print()


'''when we need differnet different output then we go for parameterized constructor

'''
#ex8
class Student:
    def __init__(self,name,age,marks,clg_name,dept):
        self.name=name
        self.age=age
        self.marks=marks
        self.clg_name=clg_name
        self.dept=dept
        print(f'std name is {self.name}\n'
              f'age is {self.age}\n'
              f'marks: {self.marks}\n'
              f'college name is {self.clg_name}\n'
              f'dept name is {self.dept}')
s=Student('Divya',21,80,"Diems","CSE")
print()
s1=Student('Riya',21,90,"mgm","cse")
print()
Student.__init__(s,"Diya",22,99,"mgm","entc")
print()

#ex9
#when we pass extra arguments then use *args(for n no. of positional arguments)
class Car:
    def __init__(self,cname,price,model,color,*args):
        self.cname=cname
        self.price=price
        self.model=model
        self.color=color
        print(f'car name is {self.cname}\n price:{self.price}\n model is {self.model}\n color:{self.color}\n'
              f'extra information',args)
c=Car("bmw",1500000,'bmw',"black","bmw2X",'2026')
print()

'''
METHOD OVERLOADING:
---------------------
-->creating the same methods with variations in the arguments or input 
-we cannot achieve method overloading in python
-But we can partially achieve method overloading by using default argument..............................
--------------------------------------
syntax:
class ClassName:
    def method_name(var_name=0,var=0,var=0):
        statement
object=ClassName()
------------------------------------

-FOR CONSTRUCTOR:
syntax
-------------------------------------
class ClassName:
    def __init__(self,var=0,var=0,var=0):
        statement
object=ClassName()
--------------------------------------

'''
class Test:
    def add(self,a=0):
        print(a)
    def add(self,a=0,b=0,c=0):
        print(a,b,c)
t=Test()
t.add(1)
t.add(1,2)
t.add(1,2,3)
print()

class Data:
    def __init__(self,a):
        print(a)
    def __init__(self,a,b):
        print(a,b)
    def __init__(self,a,b,c):
        print(a,b,c)
d=Data(10,20,30)
print()

class Bank:
    def __init__(self):
        self.bal=1000
    def deposit(self,amount):
        self.bal+=amount
        print('total amount is ',self.bal)
b=Bank()
#modification for instance var. by using object
b.bal=4000
#modification using class name
Bank.bal=2000   # it will not affect bcoz we are using instance var.
b.deposit(5000)    

#we can't do any modification for the instance variable using class name
#if we do modification for instance var. using object it will work
'''
class  xyz:
    class var
    def __init__(self,...,parameters):
        declare
    instance method:
        print
    class method :
        
'''  
class BookMyShow:
    tname="pvr"
    def __init__(self,movie,ticket,total_ticket,snacks_price):
        self.movie=movie
        self.ticket=ticket
        self.total_ticket=total_ticket
        self.snacks_price=snacks_price
    def movie_info(self):
        print(f'movie name is {self.movie}\n ticket price {self.ticket}\n Total tickets:{self.total_ticket}\n'
              f'snacks price:{self.snacks_price}')
    @classmethod
    def new_th(cls,new):
        cls.theator=new
        print('updated theatre name',cls.theator)
    @staticmethod
    def Name():
        print('movie')
b=BookMyShow('Dhurandar',500,2,199)
BookMyShow.new_th('inox')
BookMyShow.Name()





        