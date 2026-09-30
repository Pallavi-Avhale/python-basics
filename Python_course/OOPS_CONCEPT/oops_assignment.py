'''1.Create a class Person
Store name and age
Display details


2.Create a class Dog
Store name and breed
Print dog details


3.Create a class Fan
Store brand and price
Display details


4.Create a class Employee
Store name and salary
Increase salary by 5000
Display details


5.Create a class Gameplayer
Store player name and score
Increase score
Display score

6.	BANK CLASS
Question:
WAP TO CREATE A CLASS NAME AS A BANK
Create a class Bank:
Create account (name, balance)
Deposit money
Withdraw money
Display balance

7.	STUDENT CLASS
Question:
Create a class Student:
Store marks
Calculate grade


http://8.MOBILE CLASS
Question:
Create a class Mobile:
Store brand & price
Update price
Display details



9.	ACCOUNT CLASS
Question:
Create a class Account:
Store account number & balance
Check balance


10.Create a class Marks
Store marks of 3 subjects
Calculate total and average'''

 #1.Create a class Person
# Store name and age
# Display details
class Person:
    def info(self,name,age):
        self.name=name
        self.age=age
        print(f'name is {self.name} and age is {self.age}')
p=Person()
p.info('divya',21)
print()
# 2.Create a class Dog
# Store name and breed
# Print dog details
class Dog:
    def dog_info(self,name,breed):
        self.name=name
        self.breed=breed
        print(f'Dog name is {self.name} and breed is {self.breed}')
d=Dog()
d.dog_info('genny','german')
print()

# 3.Create a class Fan Store brand and price Display details
class Fan:
    def details(self,brand,price):
        self.brand=brand
        self.price=price
        print(f'fan brand is {self.brand} and price is {self.price}')
f=Fan()
f.details('samsung',5000)
print()

# 4.Create a class Employee,Store name and salary Increase salary by 5000
# Display details
class Employee:
    def emp_info(self,name,sal):
        self.name=name
        self.sal=sal
    def inc_sal(self):
        self.sal+=5000
        print(f'name is {self.name} and increased sal is {self.sal}')
e=Employee()
e.emp_info('dityaa',15000)
e.inc_sal()
print()

# 5.Create a class Gameplayer,Store player name and score
# Increase score Display score
class Gameplayer:
    def player(self,pname,score):
        self.pname=pname
        self.score=score
    def inc_score(self):
        self.score+=300
        print(f'player name is {self.pname} and increase sal is {self.score}')
g=Gameplayer()
g.player('kohli',500)
g.inc_score()

# 6.	BANK CLASS
# Question:WAP TO CREATE A CLASS NAME AS A BANK Create a class Bank:
# Create account (name, balance) Deposit money Withdraw money
# Display balance
# class Bank:
#     def account(self,name,bal):
#         self.name=name
#         self.bal=bal
#     def deposit(self,amount):
#         self.amount=self.bal
#     def withdraw(self)

class Test:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def Getter(self):
        return(getattr(self,'n',"name is missing"),
               getattr(self,"a","age is missing")) 
    def Setter(self,newn,newa):
        self.n=newn
        self.a=newa
    def Deleter(self):
        del self.a
t=Test("divyaaa",22)
print(t.Getter())  #('divyaaa', 22)
t.Setter("pallavi",25)
print(t.Getter())  #('pallavi', 25)
t.Deleter()
print(t.Getter())  #('pallavi', 'age is missing')
print("--------")

class Test:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    @property
    def Getter(self):
        return(getattr(self,'n','name is missing'),
               getattr(self,'a','age  is missing'))
    @Getter.setter
    def Getter(self,x):
        self.n,self.a=x
    @Getter.deleter
    def Getter(self):
        del self.a
t=Test("diuu",20)
print(t.Getter) #('diuu', 20)
t.Getter=("piuuu",18)
print(t.Getter)  #('piuuu', 18) 

del t.Getter
print(t.Getter)  #('piuuu', 'age  is missing')
print('------')  




#1
class Test:
	x=100
	def __init__(self):
		print("hiiii")
class Child(Test):
	def demo(self):
		print("Child class")
c=Child()
# c.__init__()
c.demo()

#modification
c.x=200
print(c.x)

#modification
Child.x=300
print(Child.x)
print("----------")

class Test:
     def show(self,a):
          self.a=a
          print("value of x" ,self.a)
class Two(Test):
     def show(self,b):
          self.b=b
          super().show(10)    #method chaining
          print("value of b is",self.b)
t=Two()
t.show(10)
print('--------')

class Demo:
     def __init__(self):
          print("demo class")
class Two(Demo):
     def __init__(self):
          super().__init__()  #constructor chaining
          print("child class")
t=Two()
print('-----')

class Super:
     def show(self):
          print("super parent class")
class Parent(Super):
     def show(self):
          super().show()
          print("parent class")
class Child(Parent):
     def show(self):
          Parent.show(self)   #avoid method overriding
          print("child class")
c=Child()
c.show()
print("--------")


#without using keyword argument
class School:
    def __init__(self, sname):
        self.sname = sname

    def show(self):
        print(f"school name is {self.sname}")
class Student(School):
    def __init__(self, sname,name, age):
        super().__init__(sname)
        self.name = name
        self.age = age

    def display(self):
        print(f"student name is {self.name}")
        print(f"student age is {self.age}")


s = Student("DIEMS","divya", 21)
s.display()
s.show()

print()

#with using
class School:
    def __init__(self, sname):
        self.sname = sname

    def show(self):
        print(f"school name is {self.sname}")
class Student(School):
    def __init__(self, name, age):
        super().__init__(sname="JKIS")
        self.name = name
        self.age = age

    def display(self):
        print(f"student name is {self.name}")
        print(f"student age is {self.age}")
s=Student("saurav",22)
s.display()
s.show()
print()


class A:
     def show(self):
          super().show()
          print("dad class")
class B:
     def show(self):
          print("mom class")
class C(A,B):
     def show(self):
          super().show()
          print("child class")
c=C()
c.show()
print()

class A:
     def __init__(self):
          super().__init__()
          print("dad class")
class B:
     def __init__(self):
          print("mom class")
class C(A,B):
     def __init__(self):
          super().__init__()
          print("child class")
c=C()
print()


class Emp:
    def __init__(self,ename,dept):
        self.ename=ename
        self.dept=dept
    def display(self):
        print(f"emp name is {self.ename}")
        print(f"emp dept is {self.dept}")
class Team:
    def __init__(self,tname):
         self.tname=tname
    def team_info(self):
         print(f"team name is {self.tname}")
class Manager(Emp,Team):
     def __init__(self, mname):
          Emp.__init__(self,ename="smith",dept="IT")
          Team.__init__(self,tname="t1")
          self.mname=mname
     def spam(self):
          print(f"manager name is {self.mname}")
m=Manager("manager")
m.spam()
m.team_info()
m.display()
print()


'''polymorphism'''
#*args
class Example:
    def show(self,a,*args):
        self.a=a
        print(args)
        print(f"value of a is {self.a}")
    def display(self,*args):
         print(args)
e=Example()
e.show('hi','hello',50,12)
e.display(7000,)

#**kwargs
class Example:
    def show(self,a,**kwargs):
        self.a=a
        print(kwargs)
        print(f"value of a is {self.a}")
    def display(self,**kwargs):
         print(kwargs)
e=Example()
e.show('hi',b='hello',c=50,d=12)
e.display(x=7000,)
print()

#operator overloding
class Demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
         return self.a+other.a,self.b+other.b
    def __sub__(self, other):
         return self.a-other.a,self.b-other.b
    def __mul__(self, other):
         return self.a*other.a,self.b*other.b
    def __truediv__(self, other):
         return self.a/other.a,self.b/other.b
    def __floordiv__(self, other):
         return self.a//other.a,self.b//other.b
    def __mod__(self, other):
         return self.a%other.a,self.b%other.b
    def __pow__(self, other):
         return self.a**other.a,self.b**other.b
    def __gt__(self, other):
         return self.a>other.a,self.b>other.b
    def __lt__(self, other):
         return self.a<other.a,self.b<other.b
    def __eq__(self, other):
         return self.a==other.a,self.b==other.b
d=Demo(10,20)
d1=Demo(5,15)
print(f"addition is {d+d1}")
print(f"substraction is {d-d1}")
print(f"multiplication is {d*d1}")
print(f"true division is {d/d1}")
print(f"floor division is {d//d1}")
print(f"modulus is {d%d1}")
print(f"power is {d**d1}")
print(f"greater than is {d>d1}")
print(f"less than is {d<d1}")
print(f"equals to {d==d1}")
print()

class Operations:
     def __init__(self,num1,num2):
          self.num1=num1
          self.num2=num2
     def __add__(self, other):
          return Operations(self.num1+other.num1,self.num2+other.num2)
     def __str__(self):
          return f"{self.num1} and {self.num2}"
a=Operations(10,20)
a1=Operations(5,5)
print("additon is",a+a1)  #additon is <__main__.Operations object at 0x000001CD456C5A00> we will get address use __str__
print()

class Operations:
     def __init__(self,num1,num2):
          self.num1=num1
          self.num2=num2
     def __add__(self, other):
          return Operations(self.num1+other.num1,self.num2+other.num2)
     def __repr__(self):
          return f"{self.num1} and {self.num2}"
a=Operations(10,20)
a1=Operations(5,5)
print("additon is",a+a1)
print()
          

#duck type
#way 1 loop
class Car:
    def speed(self):
         print('car speed')
class Bike:
    def speed(self):
         print('bike speed')
class Train:
     def speed(self):
          print('train speed')
obj=[Car(),Bike(),Train()]
for i in obj:
     i.speed()
print('---')

#function
class Car:
    def speed(self):
         print('car speed')
class Bike:
    def speed(self):
         print('bike speed')
class Train:
     def speed(self):
          print('train speed')
def vehicle(x):
     x.speed()
#using obj
c=Car()
vehicle(c)

b=Bike()
vehicle(b)

t=Train()
vehicle(t)
print()
#using classname
vehicle(Car())
vehicle(Bike())
vehicle(Train())
print("---")

'''ENCAPSULATION'''

#public
class First:
     a=10
     def demo(self):
          print('value of a is ',self.a)
f=First()
#modification
f.a=120
print(f.a)
f.demo()
# 120
# value of a is  120

#protected
class Two:
     _x=100
     def _demo(self,y):
          self._y=y
          print('value of x is',self._x)
          print('value of y is',self._y)
t=Two()
t._demo(200)

#modification
t._x=150
t._y=250
print(t._x)
print(t._y)
t._demo(250)
print('------')
'''mofication will work but it is not proper way
so go for modification inside the function
by getter setter deleter'''

class One:
    #  _x=10
     def __init__(self,x,y):
          self._y=y
          self._x=x
     def Getter(self):
          return(getattr(self,'_x','x is missing'),
                 getattr(self,'_y','y is missing'))
     def Setter(self,newa,newb):
          self._x=newa
          self._y=newb
     def Deleter(self):
          del self._x
o=One(10,20)
print(o.Getter())
o.Setter(70,80)
print(o.Getter())
o.Deleter()
print(o.Getter())  #('x is missing', 80)
print('------')

#private 
class Private:
     __a=10
     def demo(self,b):
          self.__b=b
          print('value of a is',self.__a)
          print('value of b is',self.__b)
p=Private()
# p.__demo(200) #AttributeError: 'Private' object has no attribute '__demo'
#accessing privat var by obj
p.demo(20)
print(p._Private__b)

#using class 
Private.demo(p,25)
print(Private._Private__a)
print("------")

#public in inheritance
class One:
     def demo(self,x):
          self.x=x
          print("x is ",self.x)
class Two(One):
     def show(self):
          print("child")
t=Two()
t.show()
t.demo(100)
'we can access public var in subclass also'
print()

#protected in inheritance
class Hey:
     _num=66
     def show(self):
          print('value of x is', self._num)
class Hello(Hey):
     def display(self):
          print(self._num)
          print('helloo')
h=Hello()
h.display()
h.show()
'we can acces protected in subclass also but not proper way'

#private in inheritance
class Hi:
     __a=12
     def show(self):
          print('value of a is ,',self.__a)
class Two(Hi):
     def display(self):
          print('a is accesssible',self.__a)
t=Two()
print("-----")
# t.display() #AttributeError: 'Two' object has no attribute '_Two__a'
'''private var are not accessible inside subclass class as they are stored as _ClassName___varname'''

'''prperty decorator'''
class P:
     def __init__(self,name,age,id):
          self.name=name
          self._age=age
          self.__id=id
     @property  #getter
     def Data(self):
          return(getattr(self,'name','name is missing'),
                 getattr(self,'_age','age is missing'),
                 getattr(self,'_P__id','id is missing'))
     @Data.setter
     def Data(self,x):
          self.name,self._age,self.__id=x
     @Data.deleter
     def Data(self):
          del self.__id
p=P('riyaaa',22,12348765)
print(p.Data)
#setter
p.Data=("divyaa",21,98765)
print(p.Data)
#deleter
del p.Data
print(p.Data)
# ('riyaaa', 22, 12348765)
# ('divyaa', 21, 98765)
# ('divyaa', 21, 'id is missing')
print("----------")

'''abstraction'''

from abc import ABC,abstractmethod
# class A(ABC):
#      @abstractmethod
#      def spam(self):
#           print("abstact method")
# a=A()
# a.spam() #TypeError: Can't instantiate abstract class A without an implementation for abstract method 'spam'

from abc import ABC,abstractmethod
class A:    #remove ABC class
     @abstractmethod
     def spam(self):
          print("abstact method")
a=A()
a.spam()  #abstact method

from abc import ABC,abstractmethod
class B(ABC):   #keep ABC class and remove abstract method
     def show(self):
          print("helloooo")
b=B()
b.show() #helloooo
print('--------')

from abc import ABC,abstractmethod
class Bank(ABC):   #no implementation
     @abstractmethod
     def __init__(self,bname,bal):
          pass
     @abstractmethod
     def Deposit(self,amount):
          pass
     @abstractmethod
     def Withraw(self,amount):
          pass
class Customer(Bank):
     def __init__(self,bname,bal):
          self.b=bname
          self.bal=bal
          print(f"bank name is {self.b}\n"
                f"balance is {self.bal}")
     def Deposit(self, amount):
          self.bal+=amount
          print(f"deposit amount is {self.bal}")
     def Withraw(self, amount):
          self.bal-=amount
          print(f"withrawal amount is {self.bal}")
c=Customer("SBI",12000)
c.Deposit(2000)
c.Withraw(4000)
# bank name is SBI
# balance is 12000
# deposit amount is 14000
# withrawal amount is 10000
print("-----------")

from abc import ABC,abstractmethod
class Amazon(ABC):
     @abstractmethod
     def __init__(self,pname,price):
          pass
     @abstractmethod
     def delivery(self,add):
          pass
class Customer(Amazon):
     def __init__(self, pname, price):
          self.n=pname
          self.p=price
          print(f"product name is {self.n}\n"
                f"product price is {self.p}")
     def delivery(self, add):
          self.a=add
          print(f"delivery address is {self.a}")
c=Customer('watch',1500)
c.delivery("pune")
# product name is watch
# product price is 1500
# delivery address is pune
print("------")

class Dad:
     def show(self):
          # Mom.show(self)
          super().show()
          print("dad class")
class Mom:
     def show(self):
          print("mom class")
class Child(Dad,Mom):
     def show(self):
          # Dad.show(self)
          super().show()
          print("child class")
c=Child()
c.show()
print("--------")

class Product:
     def __init__(self,pname,**kwargs):
          self.pname=pname
          super().__init__(**kwargs)
          super().show()
     def show(self):
          print(f"prod name is {self.pname}")
class Delivery:
     def __init__(self, add,**kwargs):  
          self.add=add
          super().__init__(**kwargs)
     def show(self):
          print(f"addrees is {self.add}")
class Customer(Product,Delivery):
     def __init__(self, cname,**kwargs):
          super().__init__(**kwargs)
          super().show()
          self.cname=cname
     def show(self):
          print(f"customer name is {self.cname}")
c=Customer(cname="divyaa",pname="iphone",add="pune")
c.show()
print("---------")


     
        



     
    
    
          

     
    

        
    
          

          
     
          






    
        





