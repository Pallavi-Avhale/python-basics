#POLYMORPHISM : 

#POLY->many MORPHISM->forms
#an object showing different behaviour at different stages of life cycle


#types of polymorphism:
#1) method overloading / compile time polymorphism / static polymorphism
#2) method overriding / runtime polymorphism / dynamic polymorphism 

#method overloading , constructor overloading, operator overloading[magic]
#method overrriding , constructor overloading , duck typeing 

#constructor chaining

#overloading: we cannot show 100 per we can show partially by help of default (beacase it consist only latest one)
'''
class total: 
    def demo(self,x):
        print("first method ",x)
    def demo(self,x,y):
        print("second method ",x,y)
    def demo(self,x,y,z):
        print("third method ",x,y,z) #take latest one
t=total()
t.demo(10,20,30)

#o/p->third method  10 20 30

#default argument
class total: 
    def demo(self,x):
        print("first method ",x)
    def demo(self,x,y):
        print("second method ",x,y)
    def demo(self,x=0,y=0,z=0):
        print("third method ",x,y,z) #take latest one
t=total()
t.demo(10)
t.demo(10,20)
t.demo(10,20,30)

# *args:
class team:
    def demo(self,*args):
        print(args)
x=team()
x.demo()
x.demo(1) 
#o/p-> (),(1,) [in form of tuple]


#constructor overloading :  beacaouse python is dynamic type language

class data:
    def __init__(self,a):
        self.a=a
        print(self.a)
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b)
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a,\self.b,self.c)
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        print(self.a,self.b,self.c,self.d)
z=data()
z=data(1)
z=data(1,2)
z=data(2,3,4)

#o/p->
# 0 0 0 0
# 1 0 0 0
# 1 2 0 0
# 2 3 4 0'''

#overriding : to achieve 100 per we need inheritance concept 
 

'''class a:
    def __init__(self,name):
        self.name=name
        print(self.name)
class b(a):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print(self.age)
z=b("shreyas",12)
'''

#operator overloading: direct not posible using ,Magic method only.
#in java we cant acheive operator overloading but in python we can acheive using magic method 

#magic method :
'''
__add__(self,other)
__sub__(self,other)
__mul__(self,other)
__truedivision__(self,other)
__floordivison__(self,other)
__mod__(self,other)
__pow__(self,other)
__gt__(self , other) greater than (boolean value we get)
__lt__(self,other )
 __eq__(self,other):'''
#-------------------------------------------------------------------------
##add :
# class total:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x+other.x
# t=total(100) #self.x
# t1=total(200) #other.x
# print(t+t1)

# #another way
# class total: #in place of other you can take another name also
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         print(self.x+other.x)
# t=total(100) #self.x
# t1=total(200) #other.x
# t+t1
# #-------------------------------------------------------------------

# #sub:
# class total:
#     def __init__(self,x):
#         self.x=x
#     def __sub__(self,other):
#         return self.x-other.x
# t=total(100) #self.x
# t1=total(200) #other.x
# print(t-t1)

# #----------------------------------------------------------------------

# #mul:
# class total:
#     def __init__(self,x):
#         self.x=x
#     def __mul__(self,other):
#         return self.x*other.x
# t=total(100) #self.x
# t1=total(200) #other.x
# print(t*t1)

#----------------------------------------------------------------------

#mod:
# class total:
#     def __init__(self,x):
#         self.x=x
#     def __mod__(self,other):
#         return self.x%other.x
# t=total(100) #self.x
# t1=total(200) #other.x
# print(t%t1)

# #---------------------------------------------------------------
# #pow:

# class total:
#     def __init__(self,x):
#         self.x=x
#     def __pow__(self,other):
#         return self.x**other.x
# t=total(2) #self.x
# t1=total(3) #other.x
# print(t**t1)
#--------------------------------------------------------------


#WITH USING TWO PARAMETER: when we perform multiple operation output in tuple form

'''class data:
    def __init__(self,x,y):
     self.x=x
     self.y=y
    def __add__(self,other):
       return self.x+other.x,self.y+other.y
d=data(10,20)
d1=data(5,10)
print(d+d1)

#o/p->(15, 30)'''

#---------------------------------------------------------------

'''#if you want to convert object data into readable format using str(__str__)

class data:
    def __init__(self,x,y):
     self.x=x
     self.y=y
    def __add__(self,other):
       return data(self.x+other.x,self.y+other.y) #it give object address not output 
    def __str__(self):
       return f'{self.x} and {self.y}'
d=data(10,20)
d1=data(5,10)
print(d+d1)

 #it give object address not output to avoid none we use str 
 #15 and 30
'''

#------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
'''class total:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __add__(self,other):
      return self.a+other.a,self.b+other.b
   def __sub__(self,other):
      return self.a-other.a,self.b-other.b
   def __mul__(self,other):
      return self.a*other.a,self.b*other.b
   def __truediv__(self,other):
      return self.a/other.a,self.b/other.b
   def __floordiv__(self,other):
      return self.a//other.a,self.b//other.b
   def __mod__(self,other):
      return self.a%other.a,self.b%other.b
   def __pow__(self,other):
      return self.a**other.a,self.b**other.b
   def __gt__(self,other):
      return self.a>other.a,self.b>other.b
   def __lt__(self,other):
      return self.a<other.a,self.b<other.b
   def __eq__(self,other):
      return self.a==other.a,self.b==other.b
   
t=total(10,20)
t1=total(15,10)
print("add",t+t1)
print("sub",t-t1)
print("multiplication",t*t1)
print("truediv",t/t1)
print("floordiv",t//t1)
print("mod",t%t1)
print("power",t**t1)
print("greater than",t>t1)
print("less than",t<t1)
print("equal",t==t1)
'''
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

#duck type : we not checking object only behaviour [object-> duck--->[walk,talk,swim](behaviour)]
#with help of loop or function
'''class dog:
    def sound(self):
        print("barkk.....")
class cat:
    def sound(self):
        print("meoww....")
class goat:
    def sound(self):
        print("hhhaaa...")
data=[dog(),cat(),goat()] #internally->data->dog(),data--->cat()
for i in data:
    i.sound()'''

#help of function:

'''class dog:
    def sound(self):
        print("barkk.....")
class cat:
    def sound(self):
        print("meoww....")
class goat:
    def sound(self):
        print("hhhaaa...")

def animal(x):
    x.sound()
#behaviour same object different 
animal(dog())
animal(cat())
animal(goat())'''

#OR
'''
class dog:
    def sound(self):
        print("barkk.....")
class cat:
    def sound(self):
        print("meoww....")
class goat:
    def sound(self):
        print("hhhaaa...")
a=dog()
b=cat()
c=goat()
def animal(x):
    x.sound()
#behaviour same object different 
animal(a)
animal(b)
animal(c)'''

#in method riding we do inheritance but in duck type we dont inherite we use function 
#---------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

# class file:
#     def read(self):
#         print('reading the file')
# class pdf:
#     def read(self):
#         print('pdf reading')
# class newspaper:
#     def read(self):
#         print("newspaper reading")
# f=file()
# p=pdf()
# n=newspaper()
# def data(x):
#     x.read()
# data(f)
# data(p)
# data(n)

#-----------------------------------------------------------------------------------------------

class creditcard:
    def pay(self,name,amount):
        self.n=name
        self.a=amount
        print(f'the person name {self.n}')
        print(f'the total amount {self.a}')

class phonepay:
     def pay(self,name,amount):
        self.n=name
        self.a=amount
        print(f'the person name {self.n}')
        print(f'the total amount {self.a}')

class gpay:
     def pay(self,name,amount):
        self.n=name
        self.a=amount
        print(f'the person name {self.n}')
        print(f'the total amount {self.a}')

payment=[creditcard(),phonepay(),gpay()]
for i in payment:
    i.pay('a',5000)
#output will be same:
'''the person name a
the total amount 5000
the person name a
the total amount 5000
the person name a
the total amount 5000'''

class creditcard:
    def pay(self,name,amount):
        self.n=name
        self.a=amount
        print(f'the person name {self.n}')
        print(f'the total amount {self.a}')

class phonepay:
     def pay(self,name,amount):
        self.n=name
        self.a=amount
        print(f'the person name {self.n}')
        print(f'the total amount {self.a}')

class gpay:
     def pay(self,name,amount):
        self.n=name
        self.a=amount
        print(f'the person name {self.n}')
        print(f'the total amount {self.a}')

c=creditcard()
p=phonepay()
n=gpay()

def payment(x):
    x.pay('a',5000)
payment(c)
payment(p)
payment(n)