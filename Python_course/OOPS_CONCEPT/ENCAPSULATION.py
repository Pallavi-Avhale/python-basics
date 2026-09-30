'''
Encapsulation:
---------------
Wrapping up or binding up a data into a single unit is called as encapsulation

when to use encapsulation--->
-for security purpose
-if we want to hide the data

ex Banking domains



ACCESS SPECIFIER:
1. Public
2. Protected(_a=10)
3. Private(__a=10)

In python we call this as a access specifier/ Access modifiers.
In java this are considered as a keyword

1. PUBLIC ACCESS SPECIFIER:
----------------------------
- before the variable/ before the method if we don't assign any _ then it is public
-we can access this anywhere

2.PROTECTED ACCESS SPECIFIER:
----------------------------
-called as semi private
--> Before the variable or before the method if we use _ that type of variables or method
are called as protected access specifier
-we can access them inside the class only
-if we access outside the class it will work but according to the convention 
we should not use it outside the class

3. PRIVATE ACCESS SPECIFIER:
-----------------------------
---> Before the variable or before the method if we use __  it is called as private a.s
-We can access them within the class only.
-it will show error (attribute error) if we try to access them outside the class

NOTE: In python we cannot achieve 100% encapsulation

'''

#ex1
print("PUBLIC ACCESS SPECIFIER")
class Test:
    name="python"
    def demo(self):
        print(f"name is {self.name}")
t=Test()
#modification
t.name="SQL"
print(t.name)
t.demo()
print("-----------------------------")

#ex2 
class Data:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def demo(self):
        print(self.name)
        print(self.age)
d=Data("riyaa",20)
#modification
d.name="diyaaa"
d.demo()
print("--------------------------------")

#ex3
print("PROTECTED ACCESS SPECIFIER")
class Bank:
    _bank_name="sbi"   #protected
    def _info(self):
        print(f"bank name is {self._bank_name}")
b=Bank()
#modification
b._bank_name="ICICI"
print(b._bank_name) #it will work but it not a proper way
print(b._bank_name)
b._info()
print("--------------------------------")

'''
In encapsulation if we want to modification  inside then we have to follow this three ways:

1.getter()---for getting the values/receive the values
2.setter()----for setting the values-->modification
3.deleter()---for deleting purpose

'''
#ex4
class Account:
    def __init__(self,name,amount):
        self._name=name
        self._amount=amount   #protected
    def Getter(self):   #getting the values
        print(self._name)
        print(self._amount)
    def Setter(self,new_name,total_amount):    #for doing modification
        self._name=new_name
        self._amount=total_amount     #updation
    #for deleting both the variables
    def deleter(self):
        del self._name              # del self._variable
        del self._amount
a=Account("abc",1000)
a.Getter()
a.Setter("divyaa",10000)
#after doing modification again we need to get the values then call getter method 
a.Getter()
a.deleter()
# a.Getter()
print("---------------------------")

#ex using return keyword
class Holder:
    def __init__(self,bank,name,bal):
        self._bank=bank
        self._name=name
        self._bal=bal
    def Getter(self):
        return self._bank,self._name,self._bal
    def Setter(self,bname,new_name,balance):
        self._bank=bname
        self._name=new_name
        self._bal=balance
    #delete the variable
    def Deleter(self):
        del self._bank
h=Holder("SBI","Hinaa",10000)
# print(h.Getter())
h.Setter("HDFC","DITYAA",15000)
#after doing modification again we need to get the values then call getter method 
print(h.Getter())
# h.Deleter()
# print(h.Getter())
print("--------------------------")

'''getattr method
------------------
if we have to delete any one / two particular variables and other remaining should be displayed then we use getattr

syntax--> getattr(object,"varname","comment")

'''
class Holder:
    def __init__(self,bank,name,bal):
        self._bank=bank
        self._name=name
        self._bal=bal
    def Getter(self):
        return (getattr(self,"_bank","bankname"),
                getattr(self,"_name","name is missing"),
                getattr(self,"_bal","balance is missing"))    
    def Deleter(self):
        del self._name
        del self._bal
h1=Holder("sbi","riyaa",1200)
h.Deleter()
print(h1.Getter())
print("--------------------------")

class Student:
    def __init__(self,name,sub,marks):
        self._name=name
        self._sub=sub
        self._marks=marks
    def Getter(self):
        return (getattr(self,"_name","name"),
                getattr(self,"_sub","subject is missing"),
                getattr(self,"_marks","marks"))
    def Setter(self,sname,subject,score):
        self._name=sname
        self._sub=subject
        self._marks=score
    def Deleter(self):
        del self._sub
s=Student("Rinaa","Maths",90)
print(s.Getter())
s.Setter("Priyanka","python",88)
print(s.Getter())
s.Deleter()
print(s.Getter())
print("----------------------------------")

print("PRIVATE ACCESS SPECIFIER")
class Data:
    __sub="python"    #PRIVATE
    def subject(self):
        print(F' SUBJECT IS {self.__sub}')
d=Data()
d.subject()
#accesing private var. through two ways--> classname and object
#using object
print(d._Data__sub)

#using class name
print(Data._Data__sub)
print(Data.__dict__)

# print(d.__sub)   #AttributeError: 'Data' object has no attribute '__sub'  we can't access directly 
print("---------------------------------")
'''if we are accessing private variable outside this phenomenon is called as 
name mangling'''

class Test:
    x=100
    def demo(self,name):
        self.name=name
        print(self.name)
    def modify(self,new):
        self.name=new
        print(self.name)
t=Test()
t.demo("xyz")  #old
t.modify("abc")  #new
print("---------------------------------")

#PUBLIC
class A:
    x=100
    def spam(self):
        print(f" value of x is {self.x}")
class B(A):
    def demo(self):
        print("demo class")
b=B()
b.demo()
b.spam()
print(b.x)
'''public access specifier can be accessed inside the subclass 
as well as outside the class/method also'''
print("---------------------------")

#PROTECTED
class Test:
    _x=200
    def _data(self):
        print(self._x)
class Two(Test):
    _y=800
    def _spam(self):
        print(self._y)
t=Two()
t._data()
t._spam()
print(t._x)
'''Protected access specifier we can access into the class as well as we can access
   protected variable inside the subclass also.
 -We can't do modification outside ...it will work but according to convention we should not do that'''

#PRIVATE
class A:
    __x=15
    def spam(self):
        print(self.__x)
class B(A):
    def demo(self):
        print(self.__x)
b=B()
# b.demo()#AttributeError: 'B' object has no attribute '_B__x'. Did you mean: '_A__x'?
print("---------------------------------")


'''Private variable we can access inside the class but

***Private variable we can't access inside the sub class.
Reason---->private access specifier will store the data internally as
           _ClassName__VariableName
           (Name mangling)
'''

'''PROPERTY DECORATOR
---------------------

---> @property (we can call it as getter method)

-Getter setter deleter are called as methods.
But @property we call it as a property

syntax: <@property_method_name>.Setter
(syntax for setter method using property)
--->property means previous property name 

note-- all property name should be same

for deleter:
syntax: <@property_method_name>.deleter

'''
#ex
class Test:
    def __init__(self,name,sub,marks):
        self.name=name
        self._sub=sub
        self.__marks=marks

    @property    #getter method
    def Data(self):
        return (getattr(self,"name","name is missing"),
                getattr(self,"_sub","sub is missing"),
                getattr(self,"_Test__marks","marks is missing"))
    
    @Data.setter    #setter method....<property name> is previous method  name
    def Data(self,x):       #it won't accept multiple parameters...it will accept single parameter
        self.name,self._sub,self.__marks=x
    
    @Data.deleter
    def Data(self):
        del self.__marks

t=Test("abc","py",88)
#calling getter method
print(t.Data)

#setting the values
t.Data=("b","sql",99)
print(t.Data)

#calling deleter property
del t.Data
print(t.Data)
print("---------------------------------")

class Bank:
    def __init__(self,name,acc_no,bal):
        self.name=name
        self._acc_no=acc_no
        self.__bal=bal
    @property
    def info(self):
        return (getattr(self,"name","name is missing"),
                getattr(self,"_acc_no","account no missing"),
                getattr(self,"_Bank__bal","balance is missing"))
    
    @info.setter
    def info(self,x):
        self.name,self._acc_no,self.__bal=x
    
    @info.deleter
    def info(self):
        del self.__bal
b=Bank("priya","600ydgfh",12000)
print(b.info)

#setter
b.info=("priyanka","57389",20000)
print(b.info)

#deleter
del b.info
print(b.info)
print("-------------------------------")

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @property
    def Data(self):
        return(getattr(self,'a','value of a is missing'),
               getattr(self,'b','value of b is missing'))
    @Data.setter
    def Data(self,x):
        self.a,self.b=x
    @Data.deleter
    def Data(self):
        del self.a
t=Test(10,20)
print(t.Data)

t.Data=(25,35)
print(t.Data)

del t.Data
print(t.Data)
print('----------------')

        



    


        





        

        




        







