'''
Inheritance
---------------
-It is also known as Is-A Relationship(when we inherit the properties from one class to another class)
-Acquiring/inheriting the property's from one class to another class
 is known as inheritance

-TYPES OF INHERITANCE:
1. Single level inheritance
2. Multi level inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
6. Cycle inheritance(python does not support this)

-------------------------------------------------
1. Single level inheritance:
----> Child class will take the property's from it's parent class
is known as single level inheritance
(only one parent class and one child class is present in Single level inheritance)

-If we done any modification in parent class it will affected to the child class

-If we do any modification in child class it won't affect the parent class

Parent class/Base class/Super class
           |
           |
           v
Child class/Subclass/Derived Class

---------------------------------------------
Syntax:
class Parent:
    pass
    
class Child(Parent):  #class child_class_name(parent_class_name)-->inheritance
    pass
    
#whenever we are doing inheritance we have to create object for child class (mandatory)...
#so that we can access both parents class data as well as child class data
new_var=Child()

'''

'''
#ex1.
class Dad:
    def spam(self):
        print('Dad class')

class Child(Dad):
    def demo(self):
        print('child class')
c=Child()  #obj creation
#using object
c.spam()
c.demo()
#using class
Child.spam(c)
Child.demo(c)
print()

#ex2.
class Dad:
    land=100
    def villa(self):
        print("dad's villa")
class Child(Dad):
    name="divyaa"
    def study(self):
        print('no study')
c=Child()
print(c.land)
c.villa()
print(c.name)
c.study()
# print(dir(Dad))
# print(dir(Child))


#ex3.
class Dad:
    def show(self):
        print('method 1')
class Child(Dad):
    def show(self):
        super().show()     #if we are using super() function inside method is know as method chaining
        print('method 2')
c=Child()
c.show()  #method 2---------->method overloading(will take latest one)
'''
'''super()
#now, i want to break method overloading ....so we have to use one inbuilt function --->super().methodname
# super()-->if we want to access parent class data into child class 
#          it will avoid method overloading

#NOTE:
 #if we are using super() function inside method is known as method chaining
 #if we are using super() function inside constructor is known as constructor chaining

 #ex4.
class Mom:
    def __init__(self):
        print('constructor 1')   
class Child(Mom):
    def __init__(self):
        super().__init__()   #to avoid method overloading....use constructor chaining
        print('constructor 2')
c1=Child()
'''

#ex5...way1
# class Student:
#     def std_data(self,name,sub):
#         self.name=name
#         self.sub=sub
#         print(f'name is {self.name}\n sub is {self.sub}')
# class Information(Student):
#     def std_data(self,clg_name,marks):
#         super().std_data(name="divyaa",sub="python")   #to avoid method overloading
#         self.clg_name=clg_name
#         self.marks=marks
#         print(f'clg name is {self.clg_name}\n marks :{self.marks}')
# i=Information()
# i.std_data("diems",90)

#ex5...way2
# class Student:
#     def std_data(self,name,sub):
#         self.name=name
#         self.sub=sub
#         print(f'name is {self.name}\n sub is {self.sub}')
# class Information(Student):
#     def std_data(self,name,sub,clg_name,marks):
#         super().std_data(name,sub)
#         self.clg_name=clg_name
#         self.marks=marks
#         print(f'clg name is {self.clg_name}\n marks :{self.marks}\n')
# i=Information()
# # i.std_data("diems",90)
# i.std_data("riyaa","sql","mgm",80)
# i.std_data("ditya","manual","mgm",88)

# name is riyaa
#  sub is sql
# clg name is mgm
#  marks :80 

#ex6.  way1
# class Employee:
#     def details(self,ename,dept):
#         self.ename=ename
#         self.dept=dept
#         print(f'employee name is {self.ename}\n department is {self.dept}')
# class Emp_details(Employee):
#     def details(self,sal,loc):
#         super().details(ename="allen",dept="sales")
#         self.sal=sal
#         self.loc=loc
#         print(f'employee salary :{self.sal}\n location:{self.loc}')
# e=Emp_details()
# e.details(10000,"pune")

# @ex6   way2
# class Employee:
#     def details(self,ename,dept):
#         self.ename=ename
#         self.dept=dept
#         print(f'employee name is {self.ename}\n department is {self.dept}')
# class Emp_details(Employee):
#     def details(self,ename,dept,sal,loc):
#         super().details(ename,dept)
#         self.sal=sal
#         self.loc=loc
#         print(f'employee salary :{self.sal}\n location:{self.loc}')
# e=Emp_details()
# e.details("smith","production",20000,"pune")
# print()

#ex6 ....constructor chaining
class Employee:
    def __init__(self,ename,dept):
        self.ename=ename
        self.dept=dept
        print(f'employee name is {self.ename}\n department is {self.dept}')
class Emp_details(Employee):
    def __init__(self,ename,dept,sal,loc):
        super().__init__(ename,dept)           #constructor chaining
        self.sal=sal
        self.loc=loc
        print(f'employee salary :{self.sal}\n location:{self.loc}')
e=Emp_details("allen","sales",25000,"mumbai")
print()

'''Multi Level Inheritance:
----------------------------
-Child class will take the properties from it's parent in term parent class will take the
properties from it's parent class
-In multi level we can write n no. of classes.

---------------------------
GrandParent class 
--------------------------
      ^
      |
      |
-------------------
parent class
------------------
      ^
      |
      |
-----------------
Child Class
-----------------

----------------------------------------------
syntax:
class GrandParent:
    pass
class Parent(Grandparent):
    pass
class Child(parent):
    pass
object=Child()
----------------------------------------------

'''
#ex1
class GrandParent:
    def Hello(self):
        print('Hello from grand parent')
class Parent(GrandParent):
    def show(self):
        print('hello from parent')
class Child(Parent):
    def spam(self):
        print('Helloo from child')
c=Child()
#using object
c.Hello()
c.show()
c.spam()
print()

#ex2-------method overloading ----using super
class X:
    def show(self):
        print("class one")
class Y(X):
    def show(self):
        super().show()           #to avoid method overloading
        print("class two")
class Z(Y):
    def show(self):
        super().show()           #to avoid method overloading
        print("class three")
z=Z()
z.show()
print()

#ex2 ----method ovrrloading----using ClassName.methodName(self)
 #to avoid method overloading using class name--->syntax: ParentClassName.MethodName(self)
#  explicitly we need to pass self
class X:
    def show(self):
        print("class one")
class Y(X):
    def show(self):
        X.show(self)            #ParentName.MethodName(self)
        print("class two")
class Z(Y):
    def show(self):
        Y.show(self)    #to avoid method overloading using class name--->syntax: ParentClassName.MethodName(self)
        print("class three")
z=Z()
z.show()
print()

#ex2---constructor----avoid method overloading using super()---(way1)
class X:
    def __init__(self):
        print("class one")
class Y(X):
    def __init__(self):
        super().__init__()
        print("class two")
class Z(Y):
    def __init__(self):
        super().__init__()          #super().__init__()---->super().methodName()
        print("class three")
z=Z()
# z.show()
print()

#ex2---constructor----avoid method overloading using class name (way2)
class X:
    def __init__(self):
        print("class one")
class Y(X):
    def __init__(self):
        X.__init__(self)            #ParentName.MethodName(self)
        print("class two")
class Z(Y):
    def __init__(self):
        Y.__init__(self)    #to avoid method overloading using class name--->syntax: ParentClassName.MethodName(self)
        print("class three")
z=Z()
# z.show()
print()

print("-----------------------------------------------")

#ex3-------->without using keyword argument
class Team:
    def Employee(self,name,age):
        self.name=name
        self.age=age
    def Data(self):
        print(f'Employee name is {self.name}\n'
              f'Employee age is {self.age}')
class Team_2(Team):
    def Employee(self,dept,sal):
        super().Employee(name="anuu",age=21)
        self.dept=dept
        self.sal=sal
    def Info(self):
        print(f'Employee dept is {self.dept}\n'
              f'Employee sal is {self.sal}')
class Team_3(Team_2):
    def Employee(self,id,loc):
        super().Employee(dept="CS",sal=30000)
        self.id=id
        self.loc=loc
    def display(self):
        print(f'Employee ID is {self.id}\n'
              f'Employee location is {self.loc}')
t=Team_3()
t.Employee(id=10011,loc="Mumbai")
t.Data()
t.Info()
t.display()
print("--------------------------------")


#ex3-------->using keyword argument
class Team:
    def Employee(self,name,age):
        self.name=name
        self.age=age
    def Data(self):
        print(f'Employee name is {self.name}\n'
              f'Employee age is {self.age}')
class Team_2(Team):
    def Employee(self,name,age,dept,sal):
        super().Employee(name,age)
        self.dept=dept
        self.sal=sal
    def Info(self):
        print(f'Employee dept is {self.dept}\n'
              f'Employee sal is {self.sal}')
class Team_3(Team_2):
    def Employee(self,name,age,dept,sal,id,loc):
        super().Employee(name,age,dept,sal)
        self.id=id
        self.loc=loc
    def display(self):
        print(f'Employee ID is {self.id}\n'
              f'Employee location is {self.loc}')
t=Team_3()
t.Employee(name="Divsss",age=22,dept="CS",sal=50000,id=10022,loc="Pune")
t.Data()
t.Info()
t.display()
print("--------------------------------")

#ex4-----using constructor
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f'Employee name is {self.name}\n'
              f'Employee age is {self.age}')
class Student2(Student):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
        print(f'marks are {self.marks}')
class Student3(Student2):
    def __init__(self,name,age,marks,clg):
        super().__init__(name,age,marks)
        self.clg=clg
        print(f'College name is {self.clg}')
s=Student3(name="zoyaa",age=19,marks=80,clg="Diems")
print("----------------------------------")

#ex5---->combination of constructor and Method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'person name is {self.name}\n'
              f'age is {self.age}')
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
    def info(self):
        print(f'Roll no is {self.roll_no}')
class Result(Student):
    def __init__(self,name,age,roll_no,m1,m2,m3):
        super().__init__(name,age,roll_no)
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def calculation(self):
        total=self.m1+self.m2+self.m3
        avg=total/3
        print(f'total marks',total)
        print("average marks ",avg)

        if avg>=50:
            print("pass")
        else:
            print('fail')
r=Result(name='riyaa',age=23,roll_no=21,m1=55,m2=80,m3=70)
r.show()
r.info()
r.calculation()
print("--------------------------")

#ex6  way1 ----withou using keyword argument and super()
class Amazon:
    def __init__(self,prod,total_prod):
        self.prod=prod
        self.total_prod=total_prod
    def info(self):
        print(f'product name:{self.prod}\n'
              f'Total products :{self.total_prod}')
class Prod_info(Amazon):
    def __init__(self,prod,total_prod,color,price):
        super().__init__(prod,total_prod)
        self.color=color
        self.price=price
    def display(self):
        print(f'Product color is {self.color}\n'
              f'Price is {self.price}')
class Product(Prod_info):
    def __init__(self,prod,total_prod,color,price,address):
        super().__init__(prod,total_prod,color,price)
        self.address=address
    def show(self):
        print(f'Your Adress is {self.address}')
p=Product(prod="Watch",total_prod=1,color="black",price=800,address="Pune")
p.info()
p.display()
p.show()
print("----------------------------")


#ex6  way2 ----> using keyword argument and super()
class Amazon:
    def __init__(self,prod,total_prod):
        self.prod=prod
        self.total_prod=total_prod
    def info(self):
        print(f'product name:{self.prod}\n'
              f'Total products :{self.total_prod}')
class Prod_info(Amazon):
    def __init__(self,color,price):
        super().__init__(prod="iphone",total_prod=2)
        self.color=color
        self.price=price
    def display(self):
        print(f'Product color is {self.color}\n'
              f'Price is {self.price}')
class Product(Prod_info):
    def __init__(self,address):
        super().__init__(color="white",price=120000)
        self.address=address
    def show(self):
        print(f'Your Adress is {self.address}')
p=Product(address="Mumbai")
p.info()
p.display()
p.show()
print("----------------------------")

#ex6  way3 ----without using keyword argument and avoid method overloading using Classname.methodName(self)
class Amazon:
    def __init__(self,prod,total_prod):
        self.prod=prod
        self.total_prod=total_prod
    def info(self):
        print(f'product name:{self.prod}\n'
              f'Total products :{self.total_prod}')
class Prod_info(Amazon):
    def __init__(self,prod,total_prod,color,price):
        Amazon.__init__(self,prod,total_prod)
        self.color=color
        self.price=price
    def display(self):
        print(f'Product color is {self.color}\n'
              f'Price is {self.price}')
class Product(Prod_info):
    def __init__(self,prod,total_prod,color,price,address):
        Prod_info.__init__(self,prod,total_prod,color,price)
        self.address=address
    def show(self):
        print(f'Your Adress is {self.address}')
p=Product(prod="Laptop",total_prod=1,color="silver",price=80000,address="Pune")
p.info()
p.display()
p.show()
print("----------------------------")

#ex6  way4 ----> using keyword argument and avoid method overloading using ClassName
class Amazon:
    def __init__(self,prod,total_prod):
        self.prod=prod
        self.total_prod=total_prod
    def info(self):
        print(f'product name:{self.prod}\n'
              f'Total products :{self.total_prod}')
class Prod_info(Amazon):
    def __init__(self,color,price):
        Amazon.__init__(self,prod="Bag",total_prod=2)
        self.color=color
        self.price=price
    def display(self):
        print(f'Product color is {self.color}\n'
              f'Price is {self.price}')
class Product(Prod_info):
    def __init__(self,address):
        Prod_info.__init__(self,color="black",price=900)
        self.address=address
    def show(self):
        print(f'Your Adress is {self.address}')
p=Product(address="Mumbai")
p.info()
p.display()
p.show()
print("----------------------------")











    



