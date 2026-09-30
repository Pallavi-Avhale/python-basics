#OBJECT ORIENTED PROGRAMMING SYSTEM:
'''to represent real world object in software world using classes and objects
1) we can store code in easy manner
2) we can access code easily
3) code reusebility purpose
4) data hiding(security purpose)
5) code maintance purpose'''

#CLASS: o/p(keyvalue pair )
'''
class is (blueprint /design /plan /module) for an object'''
#class test:

#OBJECT : o/p(dict())
'''
object is real world entity created from a class that contain attribute(data) and method(behaviour)
1)building(object) depand on class
2)physical existancy of class (object)'''
#t=test()
#t1=test() refernce object

#EG : PAN(EDLI) WHERE PAN IS STRUCTURE (MEAN CLASS)AND EDLI IS OBJECT WHERE WE CREATE N NO OF ELDI (MEAN OJBJECT)
#USING ONE CLASS WE CREATE N NUMBER OF OBJECT 

#Instance Variable: Variable unique to each object, created using self
#Each object has its own separate copy of instance variables
# ✔ Instance variables are stored separately
# ✔ Each object has its own data

#--------------------------------------------------------------------------------
# s1.marks = 95
#A constructor is a special method (__init__) that is automatically called when an object is created. It is used to initialize the attributes of the object. The constructor takes parameters that are used to set the initial values of the instance variables.
# print(s1.marks)  # 95
# print(s2.marks)  # 75
# 👉 Only s1 changes
# 👉 s2 remains same
# s1.age = 21
# print(s1.age)
# 👉 Python allows dynamic instance variables

#-----------------------------------------------------------------------
# class Demo:
#     x = 100   # class variable
# d1 = Demo()
# d2 = Demo()
# d1.x = 5000  # instance variable
# 👉 Now:
# d1.x → instance variable
# d2.x → class variable
# #-------------------------------------------------------------------------------------------------------


#class variable inside function : directly not possible to avoid error
# 1) by help of self
# 2) by help of cls

'''class Demo:
    pass

d = Demo()
d.x = 100

👉 Yes, possible dynamically'''

# HOW TO CREATE A CLASS:
'''
class ClassName  (syntax)

#TYPES :
1) variable --> storing the property-------=------> 
3 types 
[ 1)class variable 2)instance variable 3)local variable]
2) method --> the function present inside a class ----------> 3 types [1)instance  2)class 3)static ]
3)constructor --> special member inside a class -----> 
2types [1) with parameter as construction  2)without parameter as construction]
'''

#--------------------------------------------------------------------------------------------------------------------
#how to create empty class:
'''class ClassName:
    pass

#how to create empty object :
ne_var_name = ClassName()

#--------------------------------------------------------------------------------------------------------------------------------
#combo:
class Morning:
    pass
b=Morning()''' #object creation 

'''
class --> keyword
Morning --> class Name
b ----> object 
'''
#-----------------------------------------------------------------------------------------------------------------------------
#variable present inside the class:

'''class Employee:
    name="ravi"
    age=45
    sal=1000
    location="pune"
e=Employee()  imp->Because name is a variable, not a function print(e.name) #o/p->ravi
print(e.age) #o/p->45
print(e) #<__main__.Employee object at 0x000002C7F1758980> pointing to main class
print(Employee.__dict__) #magic method #whole class object address

#without paranthesis:
e1=Employee #only pointing main class
print(e1)'''#<class '__main__.Employee'> #main

#-------------------------------------------------------------------------------------------
#inside the class whatever data is present directly it is not possible access outside 
'''
how to access inside class data to outside:
1) by help of class_name
2) by help of object

ERROR : nameerror

ex:
print(Employee.name) #help of class
print(Employee.age)
print(e.name)#help of object 
print(e.location)'''

#imp:
#internally data store or arrange in form of key value pair 
#structure name as Namespace
#print(Employee.__dict__)
# o/p:{'__module__': '__main__', '__firstlineno__': 57, 'name': 'ravi', 'age': 45, 'sal': 1000, 'location': 'pune',
#  '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__'
#  : <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
#--------------------------------------------------------------------------------------------

#DOCSTRING : description of class (understanding purpose we use) store in triple quotes
class Employee: 
   '''EMPLOYEE INFORMATION'''
'''name="ravi"
age=45
sal=1000
location="pune"
e=Employee()
print(e)
print(Employee.__doc__)''' #ONLY tittle
#o/p->EMPLOYEE INFORMATION


#help(Employee) -> complete information about class 
'''o/p->
Help on class Employee in module __main__:

class Employee(builtins.object)
 |  EMPLOYEE INFORMATION
 |
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables 
-- More  --
'''
#------------------------------------------------------------------------------------------

'''
class test:
    x=100
    y=200 #class variable
t=test() #first object
t1=test() #refernce variable #second object
print(id(test))
print(id(t))
print(id(t1))
print(id(t1.x))
print(id(t1.y))'''

#------------------------------------------------------------------------------------
#variable modification in class and object :
#class and object variable modification :
'''# 1) if we  modification in mainclass it will affected for both objects
#before modification :
print(test.x)
print(t.x)
print(t1.x)
# o/p->
# 100
# 100
# 100

# after modification in mainclass:4
#syntax: class_name.varname=value
test.x=1000
print(test.x)
print(t.x)
print(t1.x)
#o/p->
# 1000
# 1000
# 1000


#2) if we done any modiciation in one object only effected for that object it will wont effected for other object or class
#it affected on only particular object only

#object modification:

#sytanx --> object_name.var_name=value

t.x=5000
print(test.x)
print(t.x)
print(t1.x)
#o/p->
# 1000
# 5000
# 1000

#3) again if we done any modification in main class it will effected for man_class and other object
#  but it will wont effected for previous object then when we done serate modificaton connection will be loss

#jis object ko modify kiya usma changes nhi hoga kyoki uska connection break ho jyanga uska alava sab object ma hoga 

test.x="python" #update syntax
print(test.x)
print(t.x)#not change we loss the connection when we do seprate modification
print(t1.x)'''
#------------------------------------------------------------------------------
#example :
'''class info:
    name="crazy"
    age="15"
    loc="pune"
k=info()
k1=info()

info.name='shreyy'
print(info.name)
print(k.name)
print(k1.name)
print()
k.name="ram"
print(info.name)
print(k.name)
print(k1.name)
print()
info.name='shyam'
print(info.name)
print(k.name)
print(k1.name)

'''
#-------------------------------------------------------------------------------------
#varible :Variables are used to store data inside a class.
#1) class variable : variable which is common for all object and created inside class directly
#2) instance variable : variable which is unique for each object and created inside method by using self
#3) local variable : variable which is created inside method and used only inside method

#1) example of class variable:
'''class Employee:
    company = "ABC Corp"  # class variable

    def __init__(self, name, salary):
        self.name = name  # instance variable
        self.salary = salary  # instance variable

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)   
print(e1.company)  # Output: ABC Corp
print(e2.company)  # Output: ABC Corp
print(e1.name)  # Output: Alice
print(e2.name)  # Output: Bob
print(e1.salary)  # Output: 50000
print(e2.salary)  # Output: 60000'''

#2) example of instance variable:
'''class Employee:   
      def __init__(self, name, salary):
         self.name = name  # instance variable
         self.salary = salary  # instance variable
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
print(e1.name)  # Output: Alice
print(e2.name)  # Output: Bob 
print(e1.salary)  # Output: 50000
print(e2.salary)  # Output: 60000'''

#3) example of local variable:
'''class Employee:   
      def __init__(self, name, salary):
         self.name = name  # instance variable
         self.salary = salary  # instance variable 
      def display(self):
         bonus = 5000  # local variable
         total_salary = self.salary + bonus  # local variable  
         print(f"Employee Name: {self.name}, Total Salary: {total_salary}")
e1 = Employee("Alice", 50000) 
e1.display()  # Output: Employee Name: Alice, Total Salary: 55000'''

#-----------------------------------------------------------------------------
#METHOD : FUNCTION INSIDE CLASS 

# 1) instance (object) [bydefault(self)] #whenever we have differnet different data then we use instANCE 
# 2) class method
# 3) static method

# 1) instance method -> it is method it will work on object data 
# * a method it will accept first argument of an object address [self is special pparameter][self is always point to object ]
#FIRST ARGUMENT OF THE OBJECT ADDRESS 

'''Syntax:
class classname:
def method_name(self):
   statement

new_v = classname() -->object creation 
 
1) by using object: instance work with only object [USE ALWAYS]
newvar.method_name()

#self is pointing to current object

2) by using class: only in class [OPTIONAL]
   classname.method-name(objectname)'''

#instance work for object not class data
#Example:
'''class Demo:
   def show(self):
      print("istance name") #self is pointing to current object 
k=Demo()
k.show() # by using object here we dont pass object internally present #k.show(d)
Demo.show(k) # by using class we have to pass objectname mandatory 

#example2:

class hello:
   def hii(self):
      print("shreyy")
d=hello()
d.hii()

#without parameter :

EXAMPLE 2:
class Morning():
  def show(self):
      print(self)
m=morning() #using object
m.show()
morning.show() #with using class


#with paramter but bydefault it will take self :
class Student:
  def details(self,name,sub,marks):
    print(f'student Name is {name}\n'
          f'subject Name is {sub}\n'
          f'Total marks is {marks}\n')
s=Student()
s.details("kiran","webtech",90)
'''
# class Qsp:
#     rating = "1*"
#     sub = "SQL"

#     def display_mock_rating(self):
#         print(f"ur mock rating is {Qsp.rating} in {Qsp.sub} in subject")

# q = Qsp()
# q.display_mock_rating()

# Qsp.sub = "MANUAL"
# Qsp.rating = "2"
# q.display_mock_rating()

# Qsp.sub = "Python"
# Qsp.rating = "3"
# q.display_mock_rating()


#where we use instance variable ??
#when we have different differnt data we use instance

#Example:

'''class Student:
   def details(self,name,sub,marks):
      self.x=name #self.name=name
      self.y=sub #self.sub=sub
      self.z=marks #self.marks=marks
      print(self.x)
      print(self.y)
      print(self.z)

s=Student()
s.details("xyz","py",56) '''

#OR
'''
class Student:
   def details(self,name,sub,marks):
      self.x=name #self.name=name
      self.y=sub #self.sub=sub
      self.z=marks #self.marks=marks

def Student_information(self):
    print(f'student Name is {self.x}\n'
    f'subject Name is {self.y}\n'
    f'Total marks is {self.z}\n')
s=Student()
s.details("xyz","py",56) 
s.Student_information()'''

#----------------------------------------------------------------
#----------------------------------------------------------------

'''class Pyspider:
   def Sql(self):
      print("sql subject")
   def Powerbi(self):
      print("powerbi subject")
   def Webtech(self):
      print("webtech subject")
   def Python(self):
      print("python subject")

p=Pyspider()
p.Python()
p.Sql()
p.Webtech()
p.Powerbi()'''

#----------------------------------------------
#by l'using object : acess mutiple method by calling one method using object

'''
class Pyspider:
   def Sql(self):
      print("sql subject")
   def Powerbi(self):
      print("powerbi subject")
   def Webtech(self):
      print("webtech subject")
      self.Python()
      self.Powerbi()
      self.Sql()
   def Python(self):
      print("python subject")

p=Pyspider()
p.Webtech()'''

#-----------------------------------------------------------
#by using class: acess mutiple method by calling one single method using class

'''class Pyspider:
   def Sql(self):
      print("sql subject")
   def Powerbi(self):
      print("powerbi subject")
   def Webtech(self):
      print("webtech subject")
      Pyspider.Python(p)
      Pyspider.Powerbi(p)
      Pyspider.Sql(p)
   def Python(self):
      print("python subject")

p=Pyspider()
p.Webtech()'''

#-------------------------------------------------------------------
#exmaple:  #class variable access into instance method two ways by help of object or help of class name  
'''
class Flipkart:
   product_name="pen"
   total_product=5
   color="black"

   def product_info(self):
      print(f'product name is {self.product_name}\n'
            f'total product is {self.total_product}\n'
            f'colour is {self.color}')
s=Flipkart()
s1=Flipkart()
s.color="green"
Flipkart.color="pink"
print(s1.color)
print(Flipkart.color)
print(s.color)
s.product_info()'''


#or

'''class Flipkart:
   product_name="pen"
   total_product=5
   color="black"

   def product_info(self):
      print(f'product name is {Flipkart.product_name}\n'
            f'total product is {Flipkart.total_product}\n'
            f'colour is {Flipkart.color}')
s=Flipkart()
Flipkart.total_product=15 #update the value (modification help of class)
s.color="red" #update the value (modification help of class) #IMP BUT THESE NOT CHANGE BEACUAUSE MODIFY IN OBJECT BEACAUSE WE MODIFY IN CLASS THAT WHY BUT IN UPPER IT WILL UPDATE IF THERE IS Flkpkart.color="red" 
s.product_info()
'''


#---------------------------------------------------------------------------------------------
#Example:

#create a class marks store marks of 3 subject and calculate total and avrage :
'''class Marks:
   def score_card(self,m1,m2,m3): #delcaring
      self.m1=m1
      self.m2=m2
      self.m3=m3
   def total_score(self):  #performing calculation 
      total = self.m1+self.m2+self.m3
      avg=total/3
      print("total score",total)
      print("average",avg)
x=Marks()
x.score_card(23,45,67)
x.total_score()

#using class:
Marks.score_card(x,34,76,54)
Marks.total_score(x)'''

#----------------------------------------------------------------------------------------------

#create a class name as bank
#create a class bank:
#create account(name,balance)
#deposit money
#withdrawal money
#check balance

'''class Bank:
   def account(self,name,balance):
      self.name=name
      self.balance=balance
   def deposit(self,amount):
      print(f'before deposit total amount {self.balance}')
      self.balance+=amount
      print(f'after deposit total amount{self.balance}')
   def Withdrawal(self,withdrawal):
      print(f'before withdrawal total amount {self.balance}')
      self.balance-=withdrawal
      print(f'before withdrawal total amount {self.balance}')
   def Display(self):
      print(f'account holder name {self,name}')
      print(f'total amount is account{self.balance}')

x=Bank()
x.account("shreyas",10000)
x.deposit(4000)
x.Withdrawal(5000)
x.Display()

#using class:
Bank.account(x,"ram",5000)
Bank.deposit(x,2000)
Bank.Withdrawal(x,1000)'''

#-------------------------------------------------------------------------------

'''
class Student:
   def student_data(self,school_name,sname,sub,marks):
      self.school=school_name
      self.name=sname
      self.subject=sub
      self.marks=marks
   def marks_grade(self):
      if self.marks>=90:
         print("grade-->A+")
      elif self.marks>=85:
         print("grade-->A")
      elif self.marks>=75:
         print("grade-->B+")
      elif self.marks>=65:
         print("grade-->B")
      elif self.marks>=50:
         print("grade-->C")
      elif self.marks>=40:
         print("grade-->FAIL")

   def Result(self):
      print(f'shcool name---> {self.school}')
      print(f'student name---> {self.name}')
      print(f'Subject Name-_-> {self.subject}')
      self.marks_grade()
      #Student.marks_grade(x)
x=Student()
x.student_data("qspider","shreyas","python",78)
x.Result()'''

#------------------------------------------------
# #One Method Calling Another
# class Demo:
#     def m1(self):
#         print("Hello")

#     def m2(self):
#         print("Calling m1")
#         self.m1()

# d = Demo()
# d.m2() 
#-----------------------------------------------
#sum of n natural number using method calling another method
'''class Data:
    def numbers(self,n):
        self.n=n
    def Data_Looping(self):
        count=0
        for i in range(1,self.n+1):  #6
            count=count+i
        print(count) 
d=Data()
d.numbers(5)  #1+2+3+4+5 #----
#or
class Data:
    def numbers(self,n):
        self.n=n
    def Data_Looping(self):
        count=0
        for i in range(1,self.n+1):  #6
            count=count+i
        print(count)
d=Data()
d.numbers(5)  #1+2+3+4+5 #----> 15
d.Data_Looping() '''

#-----------------------------------------------------
#ASSIGNMENT :
# 1.Create a class Person
# Store name and age
# Display details

'''class Person:
   def info(self,name,age):
      self.name=name
      self.age=age
   def check(self):
      print(f'name of person is {self.name}')
      print(f'age of person is {self.age}')
z=Person()
z.info("shreyas",23)
z.check()'''

# 2.Create a class Dog
# Store name and breed
# Print dog details

'''class Dog:
 def info(self,name,breed):
   self.name=name
   self.breed=breed
 def check(self):
   print(f'name of dog is {self.name}')
   print(f'breed of dog is {self.breed}')
z=Dog()
z.info("sheru","labra")
z.check()'''

# 3.Create a class Fan
# Store brand and price
# Display details
'''class Fan:
 def info(self,brand,price):
   self.brand=brand
   self.price=price
 def check(self):
   print(f'name of brand is {self.brand}')
   print(f'price of fan  is {self.price}')
z=Fan()
z.info("philips",5000)
z.check()'''

# 4.Create a class Employee
# Store name and salary
# Increase salary by 5000
# Display details


# 5.Create a class Gameplayer
# Store player name and score
# Increase score
# Display score

# 6.	BANK CLASS
# Question:
# WAP TO CREATE A CLASS NAME AS A BANK
# Create a class Bank:
# Create account (name, balance)
# Deposit money
# Withdraw money
# Display balance

# 7.	STUDENT CLASS
# Question:
# Create a class Student:
# Store marks
# Calculate grade


# http://8.MOBILE CLASS
# Question:
# Create a class Mobile:
# Store brand & price
# Update price
# Display details



# 9.	ACCOUNT CLASS
# Question:
# Create a class Account:
# Store account number & balance
# Check balance


# 10.Create a class Marks
# Store marks of 3 subjects
# Calculate total and average


'''class Employee:
    name="ravi"
    age=45
    sal=1000
    location="pune"
e=Employee()
print(e.name)'''


'''class Student:
  def details(self,name,sub,marks):
    print(f'student Name is {name}\n'
    f'subject Name is {sub}\n'
    f'Total marks is {marks}\n')
s=Student()
s.details("kiran","webtech",90)'''

'''
class Amazon:
    pname = "watch"
    price = 2300
    cname = "Amith"
    caddr = "#123 Banglore-561900"

    def orderlist(self):
        print(f"Product {self.pname} is ordered the price is Rs.{self.price}")

    def delivery_product(self):
        print(f"Customer{self.cname} is ordered a product {self.pname} and delevring to {caddr}")

a = Amazon()
Amazon.orderlist(a)
'''

#-------------------------------------------------------------------------------
#CLASS METHOD: only work on class variable
#any method decorated with @classmethod is called class method
#class method working on class variable
#class method object creatin is not required
#it pointing to main class not to object
#cls-> pointing to main class
#self -> object
#cls pointing to main class
#class variable is required for class method
# self->cls 
# cls-> self
#syntax:

'''class className:
    @class_method #not mentioning class method it act like instance by default taking self  parameter
    def method_name(cls):   #cls->special parmater
        statement
    
    obect=className()

    #by calling through object:
    object.method_name()

    #by calling through class name:
    className.method_name()
'''

#in instance method object creation is mandatory but in class method object creation is not mandatory

#special parameter:
#self->object
#cls-> main class

'''class Test:
    @classmethod
    def demo(cls):
        print("this is class method")
        #print(cls)  #pointing to main class #<class '__main__.Test'>
Test.demo() #object creation is not mandatory for class method but in instance method object creation is mandatory


t=Test()
t.demo() '''#class method can be called by object also but it is not recommended because it is not object method it is class method so it is recommended to call by class name
#print(t) #pointing to object #<__main__.Test object at 0x000002020D638830>

#why we use class method: to create alternative way of constructor
#1. to access class variable    
#2. to create alternative way of constructor
#modification in class variable we use these class method

#class variable inside function : directly not possible to avoid error
# 1) by help of cls [recommended way]
# 2) by help of class name



'''class Team:
    team_name="INDIA"
    @classmethod
    def Data(cls):
        print("team name is:",cls.team_name)
        print("team name is:",Team.team_name) #by help of class name also we can access class variable but it is not recommended because it is not object method it is class method so it is recommended to call by class name
Team.Data()''' #calling through class name

'''
class pyspider:
    subject="java"
    @classmethod
    def new_subject(cls,new_one_subject): #new_one_subject->local variable for update class variable(subject=>java)
        print("subject is:",cls.subject)
        cls.subject=new_one_subject
        print("new subject is:",cls.subject)
pyspider.new_subject("python") #calling through class name it is recommended to call by class name because it is class method not object method
#here we pass direct paramter not object mention jst lke instance'''


'''class Exam:
    date="20-06-2024"
    @classmethod
    def subject_one(cls):
        print("subject_one is:",cls.date)
    @classmethod
    def subject_two(cls):
        print("subject_two is:",cls.date)
    @classmethod
    def subject_three(cls):
        print("subject_three is:",cls.date)
    @classmethod
    def subject_four(cls):
        print("subject_four is:",cls.date)

#BY USING OBJECT:
z=Exam()
#z.date="22-06-2024" #modification with object it will not change  same as itr is
z.subject_one()
z.subject_two() 
z.subject_three()
z.subject_four()

#BY USING CLASS NAME:
Exam.date="21-06-2024" #modification in class variable by help of class name
Exam.subject_one()
Exam.subject_two()  
Exam.subject_three()
Exam.subject_four()
#only focus on clss variable data
#if we modification in class variable by help of object it will not change because it is not object variable it is class variable but if we modification in class variable by help of class name it will change because it is class variable and class method working on class variable so
'''


#------------------------------------------------------------------------------------------------------------------
#IMPORTANT:
#ALTERNATIVE WAY OF CONSTRUCTOR:
'''class Exam:
    date="20-06-2024"
    @classmethod
    def subject_one(cls):
        print("subject_one is:",cls.date)
    @classmethod
    def subject_two(cls):
        print("subject_two is:",cls.date)
    @classmethod
    def subject_three(cls):
        print("subject_three is:",cls.date)
    @classmethod
    def subject_four(cls):
    #new varible=class name() #object creation inside class method [alternative way of constructor] pointing to main class
        y=cls() #object creation inside class method [alternative way of constructor]
        y.date="1-04-2024" #modification with object it will not change  same as itr is
        print("subject_four is:",y.date) # wr have to change calling also with new variable because we are using object for calling not class name

#BY USING OBJECT:
z=Exam()
z.subject_one()
z.subject_two() 
z.subject_three()
z.subject_four()

#BY USING CLASS NAME:
Exam.subject_one()
Exam.subject_two()  
Exam.subject_three()
Exam.subject_four()'''

#======================================================================================
#COMBINATION OF CLASS METHOD AND INSTANCE METHOD:
'''class Test:
    @classmethod
    def demo(cls):
        print("this is class method")
        cls.demo1(cls) #calling instance method by help of cls
    def demo1(self):
        print("this is instance method")
t=Test()
t.demo()
Test.demo1()'''

#------------------------------------------------------------------------------------------
#sir:
'''class Amazon:
    add="pyspider" #class variable

    def product_detail(self,product_name,price ,color): #instance method
        self.name=product_name
        self.price=price
        self.color=color
    
    def information(self):
        print("product name is:",self.name)
        print("product price is:",self.price)
        print("product color is:",self.color)

    @classmethod
    def datainfo(cls,new_add): #class method
        cls.add=new_add #modification in class variable by [helpof cls or by help of class name example [cls.add or Amazon.add]
        print("current address is:",cls.add)

#object creation for instance method
p1=Amazon() 
p1.product_detail("mobile",20000,"black")
p1.information()
p1.datainfo("delhi") #calling class method by object but it is not recommended because it is class method not object method so it is recommended to call by class name
Amazon.datainfo("pune")

#calling class method by class name
Amazon.datainfo("mumbai")
'''
#--------------------------------------------------------------------------------------------------------------------------

#static method: static method is not working on class variable and instance variable
#static method also known as independent method
#decorated with @staticmethod
#static method is not taking any special parameter like self or cls [important point]
#to maintain structure purpose we are using static method
#u can pass manually it wil work but it is not recommended because it is not taking any special parameter like self or cls
#in static method we can do any modification[important point] because it is not working on class variable and instance variable

#there is  no connection it use for independent work
 #print(self) #error because static method is not taking any special parameter like self or cls
 #print(cls) #error because static method is not taking any special parameter like self or cls

 #call with help of both class and object 

#------------------------------------------------------------------------------------------
#sytax:
'''
class Test:
    @staticmethod
    def method_name():
        print("this is static method")
Test.method_name() #calling static method by class name it is recommended to call by class name because it is static method not object method so it is recommended to call by class name
t=Test()
t.method_name() #static method can be called by object also but it is not recommended because it is static method not object method so it is recommended to call by class name
'''
#_---------------------------------------------------------------------------

'''class Test:
    @staticmethod
    def add(a,b): #ALL METHOD WORK INDEPENDENTLY
        return a + b
    
    @staticmethod
    def sub(a,b):
        return a - b
    
    @staticmethod
    def mul(a,b):
        return a * b   
     
    @staticmethod
    def div(a,b):
        return a / b

#by using class name:   
print(Test.add(10,5))
print(Test.sub(10,5)) 
print(Test.mul(10,5))
print(Test.div(10,5))

#by using object:
t=Test()    
print(t.add(10,5))
print(t.sub(10,5))  
print(t.mul(10,5))
print(t.div(10,5))'''

#-------------------------------------------------------------------------------------------------------------
#COMBINATION OF CLASS METHOD AND STATIC METHOD:
'''class Joy:
    sub = "python"  # class variable

    def Show(self, sub):  # instance method
        self.sub = Joy.sub  # accessing class variable by help of class name
        print("subject is:", self.sub)

    @classmethod
    def demo(cls):
        print(cls.sub)

    @staticmethod
    def info():
        print(Joy.sub) #accessing class variable by help of class name because static method is not taking any special parameter like self or cls
        #these is not recommended because it is static method not object method so it is recommended to call by class name but here we are calling by help of class name but it is not recommended because it is static method not object method so it is recommended to call by class name


# by using object:
j = Joy()
j.Show("java")
j.demo()
j.info()'''

 #instance modification help of class dont affected only any modification using object it will modify+