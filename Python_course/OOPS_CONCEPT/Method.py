'''
Method:
-A function inside the class

Types of method:
1. Instance method
2. Class method
3. Static method


1. INstance method  (instance means object)
-->is a method it will work on object data
   By default it will take a parameter that is (self)
   without self instance method it will won't work

-->A method it will accept first argument of an object address
                           ----------------------------------
                           (              self                   )


---------------------------------------
syntax: class ClassName:
            def method_name(self):        #instance method
                statement       
        new_var=ClassName()               #obj creation{this obj is always pointing to self}...object creation is mandatory

        #by using obj name
        new_var.MethodName()              #internally-->new_var=methodName(new_var)...explicitly no need to pass the object name

        #by using class name
        ClassName.MethodName(ObjectName-->i.e var)  #it is optional method...explicitly we should pass objectName


---------------------------------------

'''

class Demo:
    def show(self):
        print('instance method')
d=Demo()
d.show()
Demo.show(d)

#self is always pointing to current object
class Hii:
    def Hello(self):
        print(self)
h=Hii()
print(h)  #<__main__.Hii object at 0x000001F3A1201A30>
h.Hello()  #<__main__.Hii object at 0x000001F3A1201A30>
print()

'''
self:is special parameter....and we can use any character instead of self
But according to PEP8 we should use self only for standard

DIFFERNCE BETWEEN FUNC. AND METHOD

FUNCTION                                        METHOD
------------------------------------------------------------
-it will not be in the class                    -It will be present in class
-By default it will not take any parameter      -By default it will take it as a self
ex-                                              -ex:
def display():                                    class T:
    print('hi')                                         def display(self):
display()                                                  print('hi')
                                                         t=T()
                                                         t.display()

'''
# def sum(a,b):
#     print('sum')
# sum(x=100,y=200)  --->typeerror

class Morning:
    def show(self):
        print(self)
m=Morning()
print(m)      #<__main__.Morning object at 0x0000023A0BA51EE0>
m.show()      #<__main__.Morning object at 0x0000023A0BA51EE0>
Morning.show(m)   #<__main__.Morning object at 0x0000023A0BA51EE0>

print()

# we can use any character instead of self
# But according to PEP8 we should use self only for standard
class Morning:
    def show(Q):
        print(Q)
m=Morning()
print(m)      #<__main__.Morning object at 0x000002A8685721E0>
m.show()      #<__main__.Morning object at 0x000002A8685721E0>
Morning.show(m)  #<__main__.Morning object at 0x000002A8685721E0>

print()
# without using any parameters
class Employee:
    def Details(self):
        print('Collecting the data')
e=Employee()
e.Details()
Employee.Details(e)
print()

# using parameters
# whenever we are passing different different data we need to use instance variable
class Student:
    def details(self,name,sub,marks):
        print(f'{name},{sub},{marks}')
s=Student()
s.details('divya','maths',100)
Student.details(s,'pranjal','maths',99)
print()

'''Instance Variable:
- whenever we are passing different different data(unique data) we need to 
use instance variable

---------------------------------
syntax---> self.new_varname=value
---------------------------------
-in place of value use same data that is used as parameters
ex-
class Std:
    def det(self,name,sub,marks):
        self.x=name   #self.name=name
        self.y=sub    #self.sub=sub
        self.z=marks  #self.marks=marks
        print(self.x,self.y,self.z)
s=Std()
s.det('pallavi','python',90)
Std.det(s,'sakshi','python',90)

-when we have common data then no need to go for class var.

'''
class Std:
    def det(self,name,sub,marks):
        self.x=name   #self.name=name
        self.y=sub    #self.sub=sub
        self.z=marks  #self.marks=marks
        # print(self.x,self.y,self.z)
    
    def std_info(self):
        print(f'{self.x}\n {self.y}\n {self.z}')
s=Std()
s.det('pallavi','python',90)
Std.det(s,'sakshi','python',90)
# s.std_info('anuradha','python',90)

# class Pyspider:
#     def Python(self):
#         print('python subject')
#     def SQL(self):
#         print('sql sub')
#     def powerbi(self):
#         print('power bi')
#     def web(self):
#         print('web tech')
# p=Pyspider()
# p.Python()
# p.SQL()
# p.powerbi()
# p.web()

# whenever we are creating class we can create n no. of instance methods
class Pyspider:
    def Python(self):
        print('python subject')
    def SQL(self):
        print('sql sub')
    def powerbi(self):
        print('power bi')
    def web(self):
        print('web tech')
        # self.powerbi()  #usning object
        # self.Python()
        # self.SQL()
        Pyspider.Python(p)    #className.MethodName(object_name)
        Pyspider.SQL(p)
        Pyspider.powerbi(p)
p=Pyspider()
p.web()
print()

class Flipkart:
    product_name='iPhone'
    total_prod=5
    colour="black"

    def Prdouct_info(self):
        print(f'{self.product_name}')
        print(f'{self.total_prod}')
        print(f'{self.colour}')
p=Flipkart()
p.Prdouct_info()

print()

class Flipkart:
    product_name='iPhone'
    total_prod=5
    colour="black"

    def Prdouct_info(self):
        print(f'{Flipkart.product_name}')
        print(f'{Flipkart.total_prod}')
        print(f'{Flipkart.colour}')
p=Flipkart()
Flipkart.total_prod=10
p.colour="white"  #it will not affect the main class because we are calling the 
                  # class var. by the help of class name  {Flipkart.colour}
p.Prdouct_info()
'''Prefer to do modification using object name in the instance method..
-if we do modification  using object name then it will get affected 
for both class name and object
-But if we do modification using class name then only class name's will be affected ,
and again if do modification in object name it will not affected the object '''
print()

class Test1:
    def Add(self,a,b):
        return a+b
t=Test1()
print(Test1.Add(t,10,20))

#palindrome
# class Palindrome:
#     def palin(name):
#         if name==name[::-1]:
#             print('palindrome')
#         else:
#             print('not palindrome')
# p=Palindrome()
# p.palin('mom')
            
print()

#Create a class marks,store marks of 3subjects,calculate total and average
class Marks:
    def score(self,m1,m2,m3):
        self.maths=m1
        self.english=m2
        self.science=m3
    def total_avg(self):
        total=self.maths+self.english+self.science
        avg=total/3
        print('Total score:',total)
        print('Average score:',avg)
#object creation
m=Marks()
#calling using object
m.score(70,80,90)
m.total_avg()

#using class name
Marks.score(m,50,60,70)
Marks.total_avg(m)

print()

#wap to create class name as Bank,create account(name,balance),
# deposit memory,withdraw money,display bal
class Bank:
    def account(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,ammount):
        print(f'Before deposit total ammount:{self.balance}')
        self.balance+=ammount
        print(f'after deposit total ammount:{self.balance}')
    def withdraw(self,ammount):
        self.balance-=ammount
    def display(self):
        print(f'account holder name:{self.name}\n total bal:{self.balance}')
b=Bank()
#calling using object
b.account("divya",10000)
b.deposit(7000)
b.withdraw(5000)
b.display()
print()
#calling using class name
Bank.account(b,"pranjal",15000)
Bank.deposit(b,5000)
Bank.withdraw(b,3000)
Bank.display(b)
print()

#class name Student,instance method-student_info , inside method pass (school_name,sname,subject,marks)
#grade_info--if s=90 a+,85-A  70-B+  65-B  50-C  49-F
#method3:result school_name,sname,sub and grade
class Student:
    def std_info(self,school,sname,subject,marks):
        self.school=school
        self.sname=sname
        self.subject=subject
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print("Grade A+")
        elif self.marks>=85:
            print("Grade A")
        elif self.marks>=70:
            print("Grade B+")
        elif self.marks>=65:
            print("Grade B")
        elif self.marks>=50:
            print("Grade F")
    def result(self):
        print(f'School name is {self.school}\n student name is {self.sname}\n subject name is {self.subject} ')
        self.grade()
        # Student.grade(self)
ss=Student()
#using object
ss.std_info("py","divya","python",59)
ss.result()
print()
#using class name
Student.std_info(ss,"py","divya","python",59)
Student.result(ss)
print()


#ex
class Subject:
    sub="python"
    rating=1
    def Data(self):
        print(Subject.sub)
        print(Subject.rating)
        # print(self.sub)
        # print(self.rating)
x=Subject()
Subject.rating="1*"     #here the value will get updated as we are calling and modifying using class name
x.rating="2*"  #it will not get updated because we are calling class variable in instance method using class name
                #but we are doing modification using object to solve this call the instance var using obj name
x.Data()
print()

'''CLASS METHOD(class variable)
-any method it will decorated with @class method it is called as class method
-it will work for class variable data 
-----------------
syntax:
-----------------------------
class ClassName:
    @classmethod
    def methodName(cls):   #cls is special parameter
        statement
object=ClassName()         #obj creation
#by using obj
object.methodName()

#by using class name
ClassName.methodName()---------->internally: ClassName.methodName(object)
-----------------------------------------
here,-object creation is optional
     -cls is nothing but class, it will always pointing to main class

***differnce between class method and instance method




'''
#ex1
class Test:
    @classmethod
    def demo(cls):
        print("Demo method")
Test.demo()
#obj creation is optional, it will work withou abject creation
t=Test()
t.demo()     #optional
Test.demo()  #recommended

#ex2
class Show:
    @classmethod
    def display(cls):
        print(cls)
s=Show()
print(s)
Show.display()   #<class '__main__.Show'>
s.display()      #<class '__main__.Show'>----->cls id pointing to main class
print()

#ex2
class Show:
    @classmethod
    def display(Q):
        print(Q)
s=Show()
print(s)
Show.display()   #<class '__main__.Show'>
s.display()      #<class '__main__.Show'>----->cls id pointing to main class
print()

'''1.if we don't use @classmethod it will act as a instance method
2.while calling through class name if we explicitly pass the object as parameter then
it will show the error ex-Show.display(s)---->typeError
'''

#ex3
class Team:
    tname="MI"  #class var.
    @classmethod
    def data(cls):
        #accessing class var inside class method(two ways)
        #1. using cls---->recommended
        print(cls.tname)
        #2. using class name
        print(Team.tname)
Team.data()   #calling through class name

'''If i want to do modification in class variable data:

'''

class Pyspiders:
    sub="java"
    @classmethod
    def new_sub(cls,new):
        cls.sub=new
        print(cls.sub)
x=Pyspiders()
x.new_sub("python")
Pyspiders.new_sub("web")
print()

class Exam:
    date='31-03-2026'
    @classmethod
    def subject1(cls):
        print('sub1 date is ',cls.date)
    @classmethod
    def subject2(cls):
        print('sub 2 date is',cls.date)
    @classmethod
    def subject3(cls):
        print('sub 3 date is',cls.date)
    @classmethod
    def subject4(cls):
        y=cls()          #alternaive way of constructor->>>[new_var=cls()]
        y.date='01-04-2026'
        print('sub 4  date is',y.date)   
e=Exam()
#modification using object--->it will not affected for main class
# e.date='01-04-2026'

#modification using class name--->it will affected for whole data
# Exam.date='01-04-2026'
e.subject1()
e.subject2()
e.subject3()
e.subject4()
Exam.subject1()
Exam.subject2()
Exam.subject3()
Exam.subject4()
print()

#combinaton:instance method+class method
class Amazon:
    addr='Pyspiders Deccan'    #class var.
    def Product_details(self,pname,price,color):       #instance method
        self.pname=pname                               #instance var.
        self.price=price
        self.color=color
    def info(self):
        print(f'product name is {self.pname}, price is {self.price} and product color is {self.color}')

    @classmethod
    def data_infor(cls,new_add):
        cls.addr=new_add
        print("current address is",cls.addr)
        # print("current address is",Amazon.addr)
a=Amazon()
a.Product_details("Iphone",120000,"white")
a.info()
# a.addr="pune"      #we will not get the updated address through this because we are accessing 
                     # class var. in class method through class name
                     #and we are doing modification thorugh object name, so it will not affect the main class 
a.data_infor("Deccan")
print()

'''STATIC METHOD
----------------
-also known as independent method
-Static method, it will won't accept self as well as cls.
-It will look like a normal function, for code utitlity purpose we go for static method
-To maintain structure of code inside the class normal func. cannot 
maintain the structure so we go for static method
===>

***In static method we can't do any modification(no self, no cls)

-------------------------------------------------
syntax------->
class ClassName:
    @staticmethod              #decorator
    def MethodName():
        statement
object=ClassName()   #obj creation
object.MethodName()
ClassName.MethodName()
-------------------------------------------------


'''
#ex1:
class Test:
    @staticmethod
    def data():
        print('hiii')
t=Test()
t.data()
Test.data()
print()

#ex2
class Calculate:
    @staticmethod
    def add(a,b):
        return a+b
    def sub(x,y):
        return x-y
print(Calculate.add(10,20))
# print(Calculate.sub(100,20))
#using obj
# c=Calculate()
# print(c.add(2,2))
# print(c.sub(6,3))

print()

#all methods
class Joy:
    sub="python"
    def course(self):
        print(self.sub)
    @classmethod
    def demo(cls):
        print(cls.sub)
    @staticmethod
    def spam(w):
        print(w.sub)     #illegal way modification in worst case scenario
        # print(Joy.sub)     by ClassName.var modification(not preferrable)
        print('no method')
j=Joy()
j.course()
j.demo()
j.spam(j)
# Joy.course(j)
# Joy.demo()
# Joy.spam()
#in static method whenever we are passing parameters that parameter is always pointing to 
# the object (that is it will become instance method only).













        
