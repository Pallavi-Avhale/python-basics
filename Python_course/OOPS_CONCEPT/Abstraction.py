'''
ABSTRACTION:
-----------
-Hiding the complexity/features to display only required things to the end users.

1. Abstraction class
2.Abstraction method

to follow the abstraction we need to follow the step:   
   ---> from abc import ABC,abstract_method

   here, abc is module
         ABC is classname.....ABC always it will present in abc module
         abstract_method is a normal method.
         NOTE: abc, ABC are fixed we cannot change the character

         
1.ABSTRACTION CLASS:
--------------------
-some time we don't know about implementation , still we declare partial class,
that type of class is called as abstraction class.
-Abstraction class always derived from ABC class

syntax:
from  abc import ABC,abstractmethod
class ClassName(ABC):
    pass
'''

from abc import ABC,abstractmethod
class Morning(ABC):
    pass 

'''
2. ABSTRACT METHOD:
-------------------
-some time we don't know about implementation , still we declare  method,
that type of method is called as abstraction method.
-Above the method it is mandatory to use @abstractmethod 

syntax:
@abstractmethod
def method_name(self):
    pass
'''
class Test(ABC):
    @abstractmethod
    def spam(self):
        pass
#NOTE: In abstract class and abstract method it is mandatory to use no implementation

'''
syntax for both:
class ClassName:
    @abstractmethod
    def method_name(self):
        pass or ...

'''

'''
WHERE TO DO IMPLEMENTATION:
--------------------------

In the above examples we are passing pass that is no implementation.
But if we have to do implementation then we need to do it in the Child class.
No need to do in the parent class

CASE 1]
from abc import ABC,abstractmethod
class Test(ABC):
    @abstractmethod
    def spam(self):
        print("welcome")
t=Test()
# t.spam()  #TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'spam'

CASE2]   removing ABC class

from abc import ABC,abstractmethod
class Test:
    @abstractmethod
    def spam(self):
        print("welcome")
t=Test()
t.spam()  #welcome

CASE3] removing abstract method
from abc import ABC,abstractmethod
class Test(ABC):
    def spam(self):
        print("welcome")
t=Test()
t.spam()  #welcome


In abstract class we cannot create object it will show TypeError.
If we want to create object then there are two scenarios:
1. Using ABC and removing abstarct method
2. Using abstarct method and removing ABC
'''

#ex
from abc import ABC,abstractmethod
class Student(ABC):
    @abstractmethod
    def sub_one(self,sub):
        pass

    @abstractmethod
    def sub_two(self,sub):
        pass

class SubjectInfo(Student):   #to do implementation create child class...it will be normal class 
    def sub_one(self, sub,name,age,rollno):
        self.name=name
        self.age=age
        self.r=rollno
        print(f"subject 1 is {sub}, name is {self.name} and age is {self.age} roll no is {self.r}")
    def sub_two(self, sub):
        print(f"sub 2 is {sub}")
s=SubjectInfo()
s.sub_one("python","divya",21,32456)
s.sub_two("sql")
print("--------------------------")


#ex2
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def __init__(self,holdername,bal):
        pass
    @abstractmethod
    def Deposit(self,amount):
        pass
    @abstractmethod
    def Withdraw(self,amount):
        pass
class AccHolder(Bank):
    def __init__(self, holdername, bal):
        self.holdername=holdername
        self.bal=bal
        print(f"holder name is {self.holdername}\n"
              f"Total bal is {self.bal}")
    def Deposit(self, amount):
        self.bal+=amount
        print(f"after depositing total bal {self.bal}")
    def Withdraw(self, amount):
        self.bal-=amount
        print(f"after withdrawal total bal {self.bal}")
a=AccHolder("allen",10000)
a.Deposit(2000)
a.Withdraw(5000)
print("----------------------------------")

'''
CONCRETE CLASS
--------------
The class consist of declaration as well as implementation

class Test:
    def spam(self):
        print("hiiii)


CONCRETE METHOD:

'''

from abc import ABC,abstractmethod
class Myntra(ABC):
    @abstractmethod
    def __init__(self,product,total_prod,price):
        pass
    @abstractmethod
    def Delivery(self,add):
        pass
    @abstractmethod
    def Payment(self,mode):
        pass
class Customer(Myntra):
    def __init__(self,product,total_prod,price):
        self.product=product
        self.total_prod=total_prod
        self.price=price
        print(f"product name is {self.product}\n"
              f"Total products are {self.total_prod}\n"
              f"Price is {self.price}")
    def Delivery(self, add):
        self.add=add
        print(f"Delivery address is {self.add}")
    def Payment(self, mode):
        self.mode=mode
        print(f"payment mode is {self.mode}")
c=Customer("watch",1,1000)
c.Delivery("pune")
c.Payment("online")
print("---------------------------------")


#ex
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        ...

class Car(Vehicle):
    def __init__(self,brand,speed,color):
        self.brand=brand
        self._speed=speed
        self.__color=color
    def Getter(self):
        return self.brand,self._speed,self.__color
    def Setter(self,speed):
        if speed>0:
            print(self._speed)
        else:
            print("invalid speed")
    def start(self):
        print(f"{self.brand} car is starting")
    def moving(self):
        print(f"{self.brand} car is moving on road")

class Bike(Vehicle):
    def start(self):
        print(f"bike is starting")
    def moving(self):
        print(f"Bike is moving on road...")

c=Car("BMW",150,'Blue')
c.Setter(80)
c.Getter()
c.moving()
c.start()
print()
b=Bike()
b.start()
b.moving()
print("----------------------------------")

#banking domain
'''
from abc import ABC
class bank(Abc):
    @abstractmethod
    def acc holder Info
    acc Type
        saving acc
    deposit
    withdrawal
class person:
    accType(current account)
           (business acc)

'''