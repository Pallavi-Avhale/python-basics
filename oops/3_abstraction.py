#ABSTRACTION :
#hiding the complexity feature to display only required things to the end user
#atm - hiding mechanism only dislpay required things that we want 

#all parent class method we have to mandatory to declare in child class but we can add extra method in child class it will working 

'''
1)abstraction class
2)abstract method 
step 1:
from abc import ABC,abstractmethod     #ABC[classname] present inside abc [module]'''


'''#abstraction class: some time we dont know about implementation still declare partial class the type of class we can call it as a abstraction class
#abstraction class always derivied from ABC class
#no need to print statement if you want to achieve abstraction with help of child class (inheritance)

from abc import ABC,abstractmethod

#abstract class
class Morning(ABC):
  pass  #implementation'''
  
#we take parent and child classs but in child class we used normal method (it consist of both declaration and implementation)

#abstact method : some time we dont know about implementation still declaring the method that type method known as abstract method 
#always used in parent class
#to achieve abstraction we used child class 
#no need to create any object

'''
from abc import ABC,abstractmethod
class test(ABC):
    @abstractmethod
    def spam(Self):
        pass #no implementation '''
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
'''
from abc import ABC,abstractmethod
class test(ABC): #abstraction_class
    @abstractmethod
    def spam(Self): #abstract_method
        pass #no implementation '''
#--------------------------------------------------------------------------------------------

#case1: 
'''from abc import ABC,abstractmethod
class test(ABC): #abstraction_class
    @abstractmethod
    def spam(Self): #abstract_method
        print("welcome")
t=test()
t.spam()
#o/p->    t=test()
#TypeError:'''

#--------------------------------------------------------------------------------------------------
#case 2: #by removing @abstractmethod
'''from abc import ABC,abstractmethod
class test(ABC):
    def spam(Self): 
        print("welcome")
t=test()
t.spam()
#o/p-> welcome'''
#----------------------------------------------------------------------------------------------
#case 3: remove abc

'''from abc import ABC,abstractmethod
class test:
    def spam(Self): 
        print("welcome")
t=test()
t.spam()
#o/p-> welcome
'''
#-----------------------------------------------------------------------------------------------
'''from abc import ABC,abstractmethod

class student(ABC): #parent here we hiding a data 
    @abstractmethod
    def subject_one(self,sub):
        pass

    @abstractmethod
    def subject_two(Self,sub):
        pass
class subject_info(student): #conctract class it consisit of both implementation and declaration 
    def subject_one(self, sub): #declaration
        print(f'subject one name --> {sub}') #implementaion
    def subject_two(self,sub):
        print(f'subject two name -->{sub}')

x=subject_info()
x.subject_one("python")
x.subject_two("sql")'''

#--------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
''''
from abc import ABC,abstractmethod

class bank(ABC): #parent
    @abstractmethod
    def __init__(self,holder_name,bal): #hiding balance
        pass

    @abstractmethod
    def deposit(self,amount): #hiding amount
        pass
    
    @abstractmethod
    def withdrawal(self,amount):
        pass

class account_holder(bank):
    def __init__(self,holder_name,bal):
        self.h=holder_name
        self.b=bal
        print(f' holder name is {self.h}')
        print(f'total balance is {self.b}')

    def deposit(self,amount):
        self.b+=amount
        print(f'after deposit total bal ,{self.b}')
    
    def withdrawal(self, amount):
        self.b-=amount
        print(f'after withdrawal total bal ,{self.b}')

a=account_holder("shreyy",20000)
a.deposit(5000)
'''

#-----------------------------------------------------------------------------
'''
from abc import ABC,abstractmethod

class amazon(ABC): #parent
    @abstractmethod
    def __init__(self,product_n,t_p,price):
        pass

    @abstractmethod
    def delivery(self,address):
        pass

    @abstractmethod
    def paymentmode(self,mode):
        pass

class product_info(amazon):
     def __init__(self,product_n,t_p,price):
        self.p=product_n
        self.totalproduct=t_p
        self.price=price
        print(f' holder name is {self.p}')
        print(f'total balance is {self.totalproduct}')
        print(f'total price {self.price}')
    
     def delivery(self,address):
         self.address=address
         print(f'adress is {self.address}')

     def paymentmode(self,mode):
         self.mode=mode
         print(f'payment mode type {self.mode}')

x=product_info("mobile",12,5000)
x.delivery("pune")
x.paymentmode("cash")
'''
#--------------------------------------------------------------------

#python we dont have interface 
#in jva we use interface same work abstraction in python