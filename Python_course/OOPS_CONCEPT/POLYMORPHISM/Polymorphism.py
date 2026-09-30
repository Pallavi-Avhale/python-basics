'''
POLYMORPHISM:(many forms)
-------------------------
-An object showing different behaviour at different stages of life cycle.

TYPES OF POLYMORPHISM:
1. METHOD OVERLOADING (Compiler time polymorphism)/ Static polymorphism
-developing a multiple method with same name and variations in parameters
concept---->method overloading
            constructor overloading 
            operator overloading

2. METHOD OVERRIDING (Runtime polymorphism)/ Dynamic polymorphism**
-developing a multiple method with same name and different implementation
concepts----->method overriding
              constructot overriding
              Duck overriding
-----------------------------------------------------------------------------

1.METHOD OVERLOADING:
-we can't achieve 100% method overloading...
we can do partial


'''
#EX1
class Total:
    def demo(self,x):
        print("first demo",x)
    def demo(self,x,y):
        print("seconf demo",x,y)
    def demo(self,x=0,y=0,z=0):   #to avoid method overloading use deafult parameters...in place of x=0,.. we can use any other no.
        print("third demo ",x,y,z)
t=Total()
t.demo(10,20)
print("-----------------------------------")

#ex1 without using default parameter---using *args
class Team:
    def demo(self,*args):
        print(args)
t=Team()
t.demo(1,2,3)
print("-------------------------------------")



#constructor overloading
#ex
class Data:
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        print(self.a,self.b,self.c,self.d)
d=Data()
d=Data(1)
d=Data(1,2)
d=Data(1,2,3)
d=Data(1,2,3,4)
print("--------------------------------------")

'''
2.METHOD OVERRIDING
-------------------
-if we want to achieve 100% method overriding , inheritance concept is required
'''
class A:
    def __init__(self,name):
        self.name=name
        print(self.name)
class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print(self.age)
b=B(name="abc",age=21)
print("------------------------------------")


'''
OPERATOR OVERLOADING:
---------------------
-In java we cannot achieve operator overloading.
But in python we achieve it using the magic method

magic method:
1. __add__(self,other)
2. __Sub__(self,other)
3. __mul__(self,other)
4. __truediv__(self,other)
5. __floordiv__(self,other)
6. __pow__(self,other)
7. __mod__(self,other)
8. __gt__(self,other)
9.__lt__(self,other)
10. __eq__(self,other)
'''

#ex   addition
class Total:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x     #accessing constructor variables in other method-->use return keyword-->return self.x
    def __sub__(self, other):
        return self.x- other.x
t=Total(100)
t1=Total(300)
print(t+t1)   #TypeError: unsupported operand type(s) for +: 'Total' and 'Total'
print(t-t1)
print("-----------------------------------")

#ex  without using return keyword--->use print function
class Total:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        print(self.x+other.x )
    def __truediv__(self, other):
        print(self.x/other.x)
    def __floordiv__(self, other):
        print(self.x//other.x)
t=Total(100)
t1=Total(200)
t+t1
t/t1
t//t1
print("-----------------------------------")

#ex2
class Data:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        # return Data(self.x+other.x, self.y+other.y)
        return self.x+other.x, self.y+other.y
d=Data(10,20)  #self.x=10,self.y=20
d1=Data(5,6)   #other.x=5, other.y=6
print(d+d1)    #(15, 26)
print("----------------------------------")

# if we are calling instance var. by the help of class name ,
# all data will be converted into object address....again if we have to convert 
# address data into readable format then we have to use magic method __str__() and __repr__()

# ---using __str__()     better go for this method
class Data:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Data(self.x+other.x, self.y+other.y)
        # return self.x+other.x, self.y+other.y
    def __str__(self):
        return f"{self.x} and {self.y}"   #mandatory use return keyword only
d=Data(10,20)  #self.x=10,self.y=20
d1=Data(5,6)   #other.x=5, other.y=6
print(d+d1)    #(15, 26)
print("----------------------------------")

# using __repr__()  ---> another way instead of __str__
class Data:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Data(self.x+other.x, self.y+other.y)
        # return self.x+other.x, self.y+other.y
    def __repr__(self):
        return (f"{self.x} and {self.y}")   #mandatory use return keyword only
d=Data(10,20)  #self.x=10,self.y=20
d1=Data(5,6)   #other.x=5, other.y=6
print(d+d1)    #(15, 26)
print("----------------------------------")


#ex2 all magic methods in operator loading
class Total:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return self.a+other.a, self.b+other.b
    
    def __sub__(self, other):
        return self.a-other.a, self.b-other.b
    
    def __mul__(self, other):
        return self.a*other.a, self.b*other.b
    
    def __truediv__(self, other):
        return self.a/other.a, self.b/other.b
    
    def __floordiv__(self, other):
        return self.a//other.a, self.b//other.b
    
    def __mod__(self, other):
        return self.a%other.a, self.b%other.b
    
    def __pow__(self,other):
        return self.a**other.a, self.b**other.b
    
    def __gt__(self, other):
        return self.a>other.a, self.b>other.b
    
    def __lt__(self, other):
        return self.a<other.a, self.b<other.b
    
    def __eq__(self, other):
        return self.a==other.a, self.b==other.b
    
t=Total(10,20)
t1=Total(15,10)
print("addition",t+t1)
print("substraction",t-t1)
print("multiplication",t*t1)
print("true division",t/t1)
print("power",t**t1)
print("floor division",t//t1)
print("modulus",t%t1)
print("greater than",t>t1)
print("less than ",t<t1)
print("equals to",t==t1)
print("----------------------------------------------")

'''
DUCK TYPE:
-----------

when we are taking decisons in duck type---->while runtime
'''
#ex1  using for loop   
class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("sound")
class Goat:
    def sound(self):
        print("goat sound")
data=[Dog(),Cat(),Goat()] #data=Dog()  data=Cat()  data=Goat()

for i in data:
    print(i)
    i.sound()
print("----------------------------")

#ex1  uaing function
class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("sound")
class Goat:
    def sound(self):
        print("goat sound")
def Animal(x):
    x.sound()
Animal(Dog())     
Animal(Cat())     
Animal(Goat())  
print()   
#using object
a=Dog()
c=Cat()
g=Goat()
Animal(a)
Animal(c)
Animal(g)
print("----------------------------")

#ex2 using function
class File:
    def Read(self):
        print("Reading file")
class Pdf:
    def Read(self):
        print("Reading pdf")
class Newspaper:
    def Read(Self):
        print("newspaper reading")
def Data(q):
    q.Read()
Data(File())
Data(Pdf())
Data(Newspaper())
print()

#using object
f=File()
p=Pdf()
n=Newspaper()
Data(f)
Data(p)
Data(n)
print("-------------------------------------")

#ex3 using looping
class File:
    def Read(self):
        print("Reading file")
class Pdf:
    def Read(self):
        print("Reading pdf")
class Newspaper:
    def Read(Self):
        print("newspaper reading")
data=[File(),Pdf(),Newspaper()]
for i in data:
    # print(i)
    i.Read()
print("------------------------------")

#ex4 using looping
class CreditCard:
    def pay(self,name,amount):
        print(f"{name} and {amount}")
class PhonePay:
    def pay(self,name,amount):
        print(f"{name} and {amount}")
class Gpay:
    def pay(self,name,amount):
        print(f"{name} and {amount}")
payment=[CreditCard(),PhonePay(),Gpay()]
for i in payment:
    i.pay("xyz",10000)
print()

#ex4 using function
class CreditCard:
    def pay(self,name,amount):
        print(f"{name} and {amount}")
class PhonePay:
    def pay(self,name,amount):
        print(f"{name} and {amount}")
class Gpay:
    def pay(self,name,amount):
        print(f"{name} and {amount}")
def payment(p):
    p.pay("Divyaa",15000)
payment(CreditCard())
payment(PhonePay())
payment(Gpay())
print("---------------------------------------")



'''
what is polymorphism and what are their types

'''

class Operators:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a, self.b+other.b
    def __sub__(self, other):
        return self.a-other.a, self.b-other.b
c=Operators(10,20)
c1=Operators(5,30)
print("addition of a and b is",c+c1)
print("substraction of a and b is",c-c1)
print('-------------------------------')

class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("Meoww")
class Goat:
    def sound(self):
        print("mehhhh")
def Animal(x):
    x.sound()
Animal(Dog())        
Animal(Cat())
Animal(Goat())

d=Dog()
c=Cat()
g=Goat()
Animal(d)
Animal(c)
Animal(g)
print('-------------------------')


#using function
class Car:
    def speed(self):
        print("speed of car")
class Bike:
    def speed(self):
        print("speed of bike")
class Train:
    def speed(self):
        print("speed of train")
def vehicle(x):
    x.speed()
#class
vehicle(Car())
vehicle(Bike())
vehicle(Train())
print()
#object
c=Car()
b=Bike()
t=Train()
vehicle(Car())
vehicle(Bike())
vehicle(Train())
print('-----------------------------')

#using looping
class Car:
    def speed(self):
        print("speed of car")
class Bike:
    def speed(self):
        print("speed of bike")
class Train:
    def speed(self):
        print("speed of train")
d=[Car(),Bike(),Train()]
for i in d:
    i.speed()
print('------------------------')









