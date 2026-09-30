#ENCAPSULATION :(security purpose)
#the wrapping of data or binding of data into a single unit 
#using in banking domain for security purpose 
#in python we cannot acheive 100 per internally how private variable assign 


#getter() ---> geeting the value / recieving the value
#setter()  --> setting the value/modification
#deletor() --> deleting the value
#getattr() ---> to avoid error [getattr(object,'v_n','comment')] object always self to get remaining data we use these
#without using getattr dont display anything here we display remaining easily delete select name
#to avoid attribute error we use one we dielte one it will show all deleted error
#Accesss specifier/modifier :
'''
1)Public  a=10
2)protected  _a=10
3)private   __a=10
'''

#public : before the variable  or before the method if we did it mention underscore we call it as a public access specifiers  a=10
#access anywhere inside as well outside class or method 
'''a=100
def spam(self):
    pass'''

'''
class test:
    name='python'
    def demo(self):
        print(f'name is {self.name}')
t=test()
t.name="sql" 
print(t.name)
t.demo()'''



'''class a:
    x=700
    def spam(self):
        print(self.x)
class b(a):
    def demo(self):
        print("demo class")
b=b()
b.demo()
b.spam()
print(b.x) # accessing outside '''


#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------

#protected : before the variable  or before the method if we did it mention single underscore(_) we call it as a public access specifiers  _a=10
#always access inside  indirectly we can show outside : 

'''class Parent:
    def __init__(self):
        self._salary = 50000   # protected

class Child(Parent):
    def show(self):
        print(self._salary)   # ✅ allowed

c = Child()
c.show()

print(c._salary)   # ⚠️ works but not recommended'''



'''_a=10
def _spam(self):
 pass
'''

'''class bank:
    _bankname="SBI"
    def _information(self): #protected access specifier
        print(f'bankname is {self. _bankname}')
x=bank()
print(x._bankname) #its not a proper way 
x._information()
x._bankname="ICICI"
x._information()
'''



'''class account:
    def __init__ (self,name,amount):
        self._name=name
        self._amount=amount
    def getter(self) : # getting the value 
        print(self._name)
        print(self._amount)
        # return self.b,self._bal,self._n
    def setter(self,newname,totalamount): #modification
        self._name=newname
        self._amount=totalamount
    def deleter(self):
        del self._name
        del self._amount


a=account('a',1000)
a.getter() # not display output we use return function inside we use print if you want to display print(a.getter()))
a.setter('b',2000)
a.getter()
a.deleter() 
a.getter()'''


#example 2:

'''class student:
    def __init__(self,name,sub,marks):
        self._name=name
        self._sub=sub
        self._marks=marks
    def getter(self): 
        return (getattr(self,"_name","name is missing"),
               getattr(self,"_sub","subject is missing"),
                getattr(self,"_marks","marks is missing"))
    
    def setter(self,new_name,new_sub,new_marks):
        self._name=new_name
        self._sub=new_sub
        self._marks=new_marks
    
    def deleter(self):
        del self._name
        del self._marks
        del self._sub

s=student("shreyas","python",100)
print(s.getter())
s.deleter()
print(s.getter())'''


#access inside  a class we can axcess easily on sub class also whenever we work on inheritance concept 
# class test:
#     _x=700  #protected only inside the class
#     def _data(self):
#      print(self._x)
# class two(test):
#     _y=800
#     def _spam(self):
#         print(self._y)
# t=two()
# t._spam()
# t._data()
# print(t._x)

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------


#private : before the variable  or before the method if we did it mention double underscore(_) we call it as a public access specifiers  _a=10
#always access inside 
#completing acess inside as well it show attribute error

'''__a=10
def__spam(self):
 pass'''

'''class data:
    __sub='python'
def subject(self):
    print(f'subject is { self.__sub}')

d=data()
print(d._data__sub)
print(data._data__sub)
d.subject() #inside class'''

#accessing private varaible outside is known as  name mangling (it through attribute error)
#we cannot access direct we can do indirectly we can do only inside
#we can access inside in single class but  cannot access in sub class 
#we hding the data 

#cannot access one class to another class 

#because of name mangling we cannt acheive 100 per just we show justification 
'''
class a:
    __x=700
    def spam(self):
        print(self.__x)
class b(a):
    def demo(self):
        print(a.__x) # wrong it is private 
b=b()
b.demo()
b.spam()
'''

#@property                        -> getter
#<@property>.setter
#<@property>.deleter

#it will accept single paramter 


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

#combination of all :
'''
class test:
    def __init__(self,name,sub,marks):
        self.name=name
        self._sub=sub
        self.__marks=marks
    
    @property #called as property above the method it act like property   # getter()
    def data(self):
       return (getattr(self,"name","name is missing"),
               getattr(self,"_sub","subject is missing"),
                getattr(self,"_test__marks","marks is missing")) #the format written in private variable internally 
    @data.setter
    def data(self,x):
        self.name,self._sub,self.__marks=x #it will accept single paramter
    
    @data.deleter #name should be fixed
    def data(self):
        del self.__marks 

t=test("a","py",77)
print(t.data) #here no nned to use () because it is not method it is property
t.data=("b","sql",99)
print(t.data)
del t.data
print(t.data)'''

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#real time example :
'''class bank:
    def __init__(self,name,accno,amount):
        self.name=name
        self._accno=accno
        self.__amount=amount
    
    @property 
    def data(self):
       return (getattr(self,"name","name is missing"),
               getattr(self,"_accno","account no is missing"),
                getattr(self,"_bank__amount","marks is missing")) 
    @data.setter
    def data(self,x):
        self.name,self._accno,self.__amount=x 
    
    @data.deleter 
    def data(self):
        del self.__amount 

t=bank("shreyas",9845651463,7000)
print(t.data) 
t.data=("bappu",85321245578,99)
print(t.data)
del t.data
print(t.data)'''