'''
MULTIPLE INHERITANCE:
--------------------
-Single child will take the properties from multiple parents.

DAD                       MOM
 ^                         ^
 |                         |
 |                         |
 -----------  CHILD--------

 -----------------------------------------------
Syntax:
class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1,Parent2):
    pass
object=Child()
------------------------------------------------

-Here two classes are independent(i.e.Parent1 and Parent2)

***-Multiple Inheritance always it will work based on the MRO fromat
***MRO-method resolution order
--->That is tracing part:
     Always it will execute Child class, then parent1 class
     then parent2 class
     After that it will execute object 
     (First child,super parent, then parent class)

     
'''
#ex1
class Father:
    def skill(self):
        print("Dad's skill")
class Mom:
    def show(self):
        print("Mom's skill")
class Child(Father,Mom):
    def display(self):
        print("Child's skill")
c1=Child()
c1.skill()
c1.show()
c1.display()
print("--------------------")

#ex2     method overloading
class A:
    def spam(self):
        super().spam()
        print("Class A")
class B:
    def spam(self):
        print("Class B")
class C(A,B):
    def spam(self):
        super().spam()
        print("Class C")
c=C()
c.spam()#Class C
print(C.__mro__)    #ClassName.__mro__   o/p:(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print("-----------------------------------")
'''Internally MRO will execute the program as:
First Child class (C)--->Then Parent1 class(A)------>Then Parent2 class(B)
Because we are inheriting the parents as C(A,B)
'''

#ex2  using constructor-----constructor overloading
class A:
    def __init__(self):
        super().__init__()
        print("Class A")
class B:
    def __init__(self):
        print("Class B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("Class C")
c=C()
print("---------------------------")

'''CONSTRUCTOR + METHOD'''
#ex 1   constructor overloading using class name--->ClassName.Method_name(self)--->most preferred
class Python:
    def __init__(self,rating):
        self.rating=rating
    def show_data(self):
        print(f"Python subject rating:{self.rating}")
class SQL:
    def __init__(self,total_class,trainer):
        self.total_class=total_class
        self.trainer=trainer
    def info(self):
        print(f"SqL total class are {self.total_class}\n"
              f"SQL Trainer name is {self.trainer}")
class Student(Python,SQL):
    def __init__(self,rating,total_class,trainer,std_name,age):
        #normal way through class
        Python.__init__(self,rating)
        SQL.__init__(self,total_class,trainer)
        self.std_name=std_name
        self.age=age
    def display(self):
        print(f"Student name is {self.std_name}\n"
              f"Student age is {self.age}")
s=Student(rating="*",total_class=40,trainer="SV",std_name="Divya",age=21)
s.show_data()
s.info()
s.display()
print("-------------------------------------------")

#ex  1  constructor overloading using super() and class name (combination)
class Python:
    def __init__(self,rating):
        self.rating=rating
    def show_data(self):
        print(f"Python subject rating:{self.rating}")
class SQL:
    def __init__(self,total_class,trainer):
        self.total_class=total_class
        self.trainer=trainer
    def info(self):
        print(f"SqL total class are {self.total_class}\n"
              f"SQL Trainer name is {self.trainer}")
class Student(Python,SQL):
    def __init__(self,rating,total_class,trainer,std_name,age):
        #using super()for one class
        super().__init__(rating)
        #using class name for another class
        SQL.__init__(self,total_class,trainer)
        # Python.__init__(self,rating)
        # SQL.__init__(self,total_class,trainer)
        self.std_name=std_name
        self.age=age
    def display(self):
        print(f"Student name is {self.std_name}\n"
              f"Student age is {self.age}")
s=Student(rating="*",total_class=40,trainer="SV",std_name="Divya",age=21)
s.show_data()
s.info()
s.display()
print("-------------------------------------------")


#ex 1   constructor overloading using only super() ----->not preferrable
class Python:
    def __init__(self,rating,*args):
        self.rating=rating
        super().__init__(*args)
    def show_data(self):
        print(f"Python subject rating:{self.rating}")
class SQL:
    def __init__(self,total_class,trainer,*args):
        self.total_class=total_class
        self.trainer=trainer
        super().__init__(*args)
    def info(self):
        print(f"SqL total class are {self.total_class}\n"
              f"SQL Trainer name is {self.trainer}")
class Student(Python,SQL):
    def __init__(self,rating,total_class,trainer,std_name,age,):
        #using super()for one class
        super().__init__(rating,total_class,trainer)
        # Python.__init__(self,rating)
        # SQL.__init__(self,total_class,trainer)
        self.std_name=std_name
        self.age=age
    def display(self):
        print(f"Student name is {self.std_name}\n"
              f"Student age is {self.age}")
s=Student(rating="1*",total_class=45,trainer="SV",std_name="Dishaa",age=21)
s.show_data()
s.info()
s.display()
# print(s.Q)   #attribute error

class X:
    def spam(self):
        super().spam()
        print('Show X')     
class Y:
    def spam(self):
        print('Show Y')             
class Z(X,Y):
    def spam(self):
        super().spam()
        print('Show Z')
z=Z() 
z.spam() 
print("-----------------------------------------")
 
 
# Pass Parameter 
# class name
class Product:
    def __init__(self,P_name,Price):
        self.P_name=P_name
        self.Price=Price
        
    def P_Data(self):
        print(f'Product Name : {self.P_name}')
        print(f'Price : {self.Price}') 
        
class Order:
    def __init__(self,NO_Product,add):
        self.NO_Product=NO_Product
        self.add=add
        
    def order_data(self):
        print(f'Total Product : {self.NO_Product}')
        print(f'Address : {self.add}')
        
class Result(Product,Order):
    def __init__(self,P_name,Price,NO_Product,add,cust_name,rating):  
        Product.__init__(self,P_name,Price)
        Order.__init__(self,NO_Product,add)         
        self.cust_name=cust_name
        self.rating=rating
        
    def Cust_data(self):
        print(f'Customer Data : {self.cust_name}')
        print(f'Rating : {self.rating}')    
x=Result('Marker',25,100,'Pune','Ram','*')    
x.P_Data()
x.order_data()
x.Cust_data()  
print("---------------------------------------")                              


# combination super() and classname
class Product:
    def __init__(self,P_name,Price):
        self.P_name=P_name
        self.Price=Price
        
    def P_Data(self):
        print(f'Product Name : {self.P_name}')
        print(f'Price : {self.Price}') 
        
class Order:
    def __init__(self,NO_Product,add):
        self.NO_Product=NO_Product
        self.add=add
        
    def order_data(self):
        print(f'Total Product : {self.NO_Product}')
        print(f'Address : {self.add}')
        
class Result(Product,Order):
    def __init__(self,P_name,Price,NO_Product,add,cust_name,rating):
        super().__init__(P_name,Price)     #super()   
        Order.__init__(self,NO_Product,add)     #using class name      
        self.cust_name=cust_name
        self.rating=rating
        
    def Cust_data(self):
        print(f'Customer Data : {self.cust_name}')
        print(f'Rating : {self.rating}')    
x=Result('Marker',25,100,'Pune','Ram','*')    
x.P_Data()
x.order_data()
x.Cust_data()
print("----------------------------------------")


# *args
class Product:
    def __init__(self,P_name,Price,*args):
        self.P_name=P_name
        self.Price=Price
        super().__init__(*args)        #pass extra info to avoid the error
        
    def P_Data(self):
        print(f'Product Name : {self.P_name}')
        print(f'Price : {self.Price}') 
        
class Order:
    def __init__(self,NO_Product,add,*args):
        self.NO_Product=NO_Product
        self.add=add
        super().__init__(*args)
        
    def order_data(self):
        print(f'Total Product : {self.NO_Product}')
        print(f'Address : {self.add}')
        
class Result(Product,Order):     #multiple inheritance
    def __init__(self,P_name,Price,NO_Product,add,cust_name,rating):
        super().__init__(P_name,Price,NO_Product,add)        
        self.cust_name=cust_name
        self.rating=rating
        
    def Cust_data(self):
        print(f'Customer Data : {self.cust_name}')
        print(f'Rating : {self.rating}')    
x=Result('Marker',25,100,'Pune','Ram','*')    
x.P_Data()
x.order_data()
x.Cust_data()
print("------------------------------------")


# **kwargs
class Product:
    def __init__(self,P_name,Price,**kwargs):
        self.P_name=P_name
        self.Price=Price
        super().__init__(**kwargs)        
        
    def P_Data(self):
        print(f'Product Name : {self.P_name}')
        print(f'Price : {self.Price}') 
        
class Order:
    def __init__(self,NO_Product,add,**kwargs):
        self.NO_Product=NO_Product
        self.add=add
        super().__init__(**kwargs)
        
    def order_data(self):
        print(f'Total Product : {self.NO_Product}')
        print(f'Address : {self.add}')
        
class Result(Product,Order):
    def __init__(self,P_name,Price,NO_Product,add,cust_name,rating):
        super().__init__(P_name=P_name,Price=Price,NO_Product=NO_Product,add=add)        
        self.cust_name=cust_name
        self.rating=rating
        
    def Cust_data(self):
        print(f'Customer Data : {self.cust_name}')
        print(f'Rating : {self.rating}')    
x=Result('Marker',25,100,'Pune','Ram','*')    
x.P_Data()
x.order_data()
x.Cust_data()
print("------------------------------------")






        


