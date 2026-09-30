#INHERITANCE :
''' [is relation ]
inheriting the properties from one class to another class

    or

acquiring the property from one class to another class

IS-A relationship--> it is a relationship between parent and child class (same as inheritance) it is a relationship between super class and sub class

inheritance also can be called as a IS-A relationship


#inhettance another name is is-a relationship

##types of inheritance

1)single level inheritance [2 class-> parent and child class]
2)multi level inheritance
3)multiple inheritance
4)hierarchical inheritance
5)hybrid inheritance

#super()-->it is a inbuilt function which is used to access the parent class data in child class
#if we miss it used latest one only it is called as method overloading
whenever we are working with inheritance always create object for child class not the parent class

'''
###################################################################################################################################333

#1)single level inheritance: two class are involved in this type of inheritance i.e parent and child class
'''
single child class will take the properties from single parent class

only it consists of 2 class i.e parent and child class


if we done any modification in parent class it affected to child class    
but modification in child class it wont affect to parent class



syntax:
        
        class parent:
            pass
            
        class child(parent): #inheritance
             pass

       new_var=child() #object  #you can called both child and parent class data  
                                  if we create parent class object only you have to access parent class
      


'''
'''
class Dad:
    def spam(self):
        print("Dad'S class")


class Child(Dad):
    def demo(self):
        print("Child class")

#by the help of object
x=Child()
x.spam()
x.demo()
'''

# print()
# #by the help of class name(always mention here child class)
# Child.spam(x)
# Child.demo(x)


##############################################################################################################################33
#
# class Dad:
#     agree_land=100
#     def villa(self):
#         print("Dad's Villa") 
#
#
# class child(Dad):
#     name="Joy"
#     def study(self):
#         print("No study")
# #
# #
# x=child()
# # print(x.agree_land)
# # x.villa()
# print(x.name)
# x.study()
# # print(dir(Dad)) #only display agreeland,villa
# #
# # print()
# #
# # print(dir(child)) #display all  i.e 'agree_land', 'name', 'study', 'villa'
#####################################################################################################################################3
#
# class Dad:
#     def show(self):
#         print("method 1")
#
# class child(Dad):
#
#     def show(self):
#         super().show() #without this method overloading happen
#         print("method 2")
#
# x=child()
# x.show()  #method overloading happen here -->always executing latest one
#
# #i want to break method overloading
#
# #super
# #for this one inbuilt_function--->super().method_name-->if you want to access to parent class data in child class
# # super function avoid method overloading
#
# #method chaining-->if i m using suoer function inside a method called as method chaining
#
# #constrcutor_chaining -->if i am super function inside a constructor is called as constructor chaining
#
# class parent:
#     def __init__(self):
#         print("constructor class 1")
#
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("constructor class 2")
#
# c=child() #constructor loading happens without super only child class data display

##################################################################################################################################
'''class student:
    def student_data(self,name,sub):
        self.name=name
        self.sub=sub

        print(f"student name is-->{self.name}")
        print(f"subject name is -->{self.sub}")

class info(student):
    def student_data(self,clg_name,marks):
        super().student_data(name="XYZ",sub="SQL")
        self.clg=clg_name
        self.marks=marks

        print(f"college name is--> {self.clg}")
        print(f"total marks-->{self.marks}")

x=info()
x.student_data("jspm tathwade",99)



class student:
    def student_data(self,name,sub):
        self.name=name
        self.sub=sub
        print(f'student name is --> {self.name}')
        print(f'lf.sub--> {self.sub}')
class teacher(student):
    def teacher_data(self,name,sub,t_name,clg_name):
        super().student_data(name,sub)
        self.teachename=t_name
        self.collegename=clg_name
        print(f'teacher name is {self.teachename}')
        print(f'collagename is {self.collegename}')
z=teacher()
z.teacher_data("shreyas","python","tnu","usa")


class student:
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
        print(f'student name is --> {self.name}')
        print(f'lf.sub--> {self.sub}')
class teacher(student):
    def __init__(self,name,sub,t_name,clg_name):
        super().__init__(name,sub)
        self.teachename=t_name
        self.collegename=clg_name
        print(f'teacher name is {self.teachename}')
        print(f'collagename is {self.collegename}')
z=teacher("shreyas","python","tnu","usa")
'''

'''class student:
    def std(self,name,id):
        self.name=name
        self.id=id
    def std_info(self):
        print(f'student name is -->{self.name}')
        print(f'student id is {self.id}')
class teacher(student):
    def ram(self,t_name,sub):
        self.teachername=t_name
        self.subject=sub
    def ram_d(self):
        print(f'teacher name is {self.teachername}')
        print(f'teacher sub {self.subject}')

z=teacher()
z.std("shreyas",1)
z.ram("radha","python")
z.std_info()
z.ram_d()'''

##################################################################################################################################33
#another way to executing previous one #without keyword arguments #better to go second one
# class student:
#     def student_data(self,name,sub):
#         self.name=name
#         self.sub=sub
#
#         print(f"student name is-->{self.name}")
#         print(f"subject name is -->{self.sub}")
#
# class info(student):
#     def student_data(self,name,sub,clg_name,marks):# directly pass parent class parameter
#         super().student_data(name,sub)
#         self.clg=clg_name
#         self.marks=marks
#
#         print(f"college name is--> {self.clg}")
#         print(f"total marks-->{self.marks}")
#
# x=info()
# x.student_data("xyz","Maths","IMCC",99)

##############################################################################################################################

#with keyword arguments

# class player:
#     def show(self,name,country):
#         self.name=name
#         self.country=country
#
#         print(f"the player name is -->{self.name}")
#         print(f"the player country is --->{self.country}")
#
#
#
# class info(player):
#     def show(self,age,ipl_team_name):
#         super().show(name="stoinis",country="Australia")
#         self.age=age
#         self.t_name=ipl_team_name
#
#         print(f"the player age is-->{self.age}")
#         print(f"the ipl team is -->{self.t_name}")
#
#
# x=info()
# x.show(23,"PBKS")


##################################################################################################################3

#without keyword

# class player:
#     def show(self,name,country):
#         self.name=name
#         self.country=country
#
#         print(f"the player name is -->{self.name}")
#         print(f"the player country is --->{self.country}")
#
#
#
# class info(player):
#     def show(self,name,country,age,ipl_team_name):
#         super().show(name,country)
#         self.age=age
#         self.t_name=ipl_team_name
#
#         print(f"the player age is-->{self.age}")
#         print(f"the ipl team is -->{self.t_name}")
#
#
# x=info()
# x.show("stoinis","Australia",29,"PBKS")

###############################################################################################################333333333
# class student:
#     def __init__(self,name,sub):
#         self.name=name
#         self.sub=sub
#
#         print(f"student name is-->{self.name}")
#         print(f"subject name is -->{self.sub}")
#
# class info(student):
#     def __init__(self,name,sub,clg_name,marks):# directly pass parent class parameter
#         super().__init__(name,sub)
#         self.clg=clg_name
#         self.marks=marks
#
#         print(f"college name is--> {self.clg}")
#         print(f"total marks-->{self.marks}")
#
# x=info("shardul","phy","jspm","web")
###################################################################################################################################
#with using constructor #wihthout keyword arguments

# class student:
#     def __init__(self,name,sub):
#         self.name=name
#         self.sub=sub
#
#         print(f"student name is-->{self.name}")
#         print(f"subject name is -->{self.sub}")
#
# class info(student):
#     def __init__(self,name,sub,clg_name,marks):# directly pass parent class parameter
#         super().__init__(name,sub)
#         self.clg=clg_name
#         self.marks=marks
#
#         print(f"college name is--> {self.clg}")
#         print(f"total marks-->{self.marks}")
#
# x=info("shardul","phy","jspm","web")

###################################################################################################################333
#with using keyword arguments

# class student:
#     def __init__(self,name,sub):
#         self.name=name
#         self.sub=sub
#
#         print(f"student name is-->{self.name}")
#         print(f"subject name is -->{self.sub}")
#
# class info(student):
#     def __init__(self,clg_name,marks):# directly pass parent class parameter
#         super().__init__(name="shardul",sub="physics")
#         self.clg=clg_name
#         self.marks=marks
#
#         print(f"college name is--> {self.clg}")
#         print(f"total marks-->{self.marks}")
#
# x=info("jspm",93)

###############################################################################################################################

# 1.Create a class Employee with attributes name and salary.
# Create a child class Manager that prints both values.

# class Employee:
#     name="Rahul"
#     salary=93000
#
# class Manager(Employee):
#     def show(self):
#         print(f"the employee name is {self.name}")
#         print(f"the salary is {self.salary}")
#
# x=Manager()
# x.show()



###################################################################################################################################


# 2.Create a class Bank with attribute balance.
#  Create a child class SavingsAccount with methods:
# deposit()
# withdraw()
# class Bank:
#     balance = 50000
#
# class Saving_Account(Bank):
#     def deposit(self, amount):
#         print(f"Balance before deposit: {self.balance}")
#         self.balance += amount
#         print(f"After depositing: {self.balance}")
#
#     def withdraw(self, amount):
#         print(f"Balance before withdrawal: {self.balance}")
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"After withdrawal: {self.balance}")
#
# x = Saving_Account()
# x.deposit(5000)
# x.withdraw(10000)


#
#
# 3.Create a class Person with a constructor.
# Create a child class Student and use super() to initialize parent data.
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# class student(Person):







#
#
#
# 4.Create a class Vehicle with method start().
# Override this method in child class Bike.

# #example:

# class team:
#     def employee(self,name,age):
#         self.name=name
#         self.age=age
#     def data(self):
#         print(f"employee name is -->{self.name}")
#         print(f"employee age is -->{self.age}")

# class team_two(team):
#     def employee(self,dept,salary):
#         super().employee(name="Rahul",age=23)
#         self.dept=dept
#         self.salary=salary
#     def information(self):
#         print(f"department is -->{self.dept}")
#         print(f"salary is -->{self.salary}")

# x=team_two()
# x.employee("IT",93000)
# x.information()
# x.data()

#------------------------------------------------------------------------------------------------------

#MULTILEVEL INHERITANCE: inturn [method resolution order] child class take property from parent class and parent class take property from grand father class it is called as multilevel inheritance
#child class take property from parent class and parent class take property from grand father class it is called as multilevel inheritance
 
'''
multilevel when wde have more than two classes involved in inheritance it is called as multilevel inheritance
In inheritance, there are three or more classes involved, where one class serves as the base class, another class is derived from it, and a third class is derived from the second class.


#Sytax:

class grandfather:
    pass
class father(grandfather):
    pass
class son(father):
    pass
object=son() #you can access all the data from grandfather,father and son class
'''

#--------------------------------------------------------
#example:

'''class grandfather:
    def hello(self):
        print("grandfather class")

class father(grandfather):
    def show(self):
        print("father class")

class son(father):
    def spam(self):
        print("son class")

c=son()
c.hello()   
c.show()
c.spam()'''

#---------------------------------------------------------
#METHOD OVERLOADING AND METHOD OVERRIDING: python dynamic language it take latest one 
# methodoverloading: creating multile method with same name but different parameter is called as method overloading [default argument,kwargs]
#method overriding: developing a method with  same method name and same parameter  [super,classname]

'''class x:
    def show(self):
        print("class one")
class y(x):
    def show(self):
        print("class two")
class z(y):
    def show(self):
        print("class three")

a=z()  #IMP
a.show() #method overriding happen here always executing latest one [o/p->class three  ->  only one due to overriding to avoid we used super function]
#o/p=->class three'''

#------------------------------------------
#SUPER FUNCTION: to avoid method overloading we used super function
# after using super function: to access parent class data in child class we used super function
'''class x:
    def show(self):
        print("class one")
class y(x):
    def show(self):
        print("class two")
        super().show() #method chaining
class z(y):

    def show(self):
        print("class three")
        super().show() #method chaining

a=z()  #IMP
a.show()'''
#o/p->
'''class three
class two
class one'''


#ANTHOR way to method chaining without using super function: with using function calling 

'''class x:
    def show(self):
        print("class one")
class y(x):
    def show(self):
        print("class two")
        x.show(self) #method chaining without super function
class z(y):
    def show(self):
        print("class three")
        y.show(self) #method chaining without super function

a=z()  #IMP
a.show()'''

#------------------------------------------------------------------------------
#WITH USING CONSTRUCTOR: constructor chaining
#with using constructor #wihthout keyword arguments:


'''class x:
    def __init__(self):
        print("constructor class 1")
class y(x):
    def __init__(self):
        super().__init__() #constructor chaining
        print("constructor class 2")
class z(y):
    def __init__(self):
        super().__init__() #constructor chaining
        print("constructor class 3")

object=z()''' #constructor loading happens here without super only child class data display

#OR
'''
class x:
    def __init__(self):
        print("constructor class 1")

class y(x):
    def __init__(self):
        x.__init__(self) #constructor chaining
        print("constructor class 2")
class z(y):
    def __init__(self):
        y.__init__(self) #constructor chaining
        print("constructor class 3")
k=z() #constructor loading happens here without super only child class data display
'''

#-----------------------------------------------------------------------------
#---------------------------------------------------------------------

# EXAMPLE:

'''class student:
    def __init__(self,name,sub):
        self.name=name    
        self.sub=sub
        print(f"student name is-->{self.name}")
        print(f"subject name is -->{self.sub}")
class info(student):
    def __init__(self,name,sub,clg_name,marks):# directly pass parent class parameter
        super().__init__(name,sub)                            
        self.clg=clg_name
        self.marks=marks      
        print(f"college name is--> {self.clg}")
        print(f"total marks-->{self.marks}")                                      
x=info("shardul","phy","jspm","web")
'''
#or

'''class student:
    def __init__(self,name,sub):
        self.name=name    
        self.sub=sub
        print(f"student name is-->{self.name}")
        print(f"subject name is -->{self.sub}")
class info(student):
    def __init__(self,clg_name,marks):# directly pass parent class parameter
        super().__init__(name="shreyas",sub="math")                            
        self.clg=clg_name
        self.marks=marks      
        print(f"college name is--> {self.clg}")
        print(f"total marks-->{self.marks}")                                      
x=info("jspm","web")
'''
                                            
#---------------------------------------------------------------------------------------

#example:

'''class team:
    def employee(self,name,age):
        self.name=name
        self.age=age
    def data(self):
        print(f"employee name is -->{self.name}")
        print(f"employee age is -->{self.age}")

class team_two(team):
    def employee(self,dept,salary):
        super().employee(name="Rahul",age=23)
        self.dept=dept
        self.salary=salary
    def information(self):
        print(f"department is -->{self.dept}")
        print(f"salary is -->{self.salary}")

class team_three(team_two):
    def employee(self,id,exp,project):
        super().employee(dept="IT",salary=93000)
        self.id=id
        self.experience=exp    
        self.project=project
    def details(self):
        print(f"the project name is -->{self.project}")
        print(f"the experience is -->{self.experience}")
        print(f"the employee id is -->{self.id}")

x=team_three()
x.employee(101,5,"web")
x.details()
x.information()
x.data()
'''

print()

#using parameter in parent class:
#without keyword arguments:

'''class team:
    def employee(self,name,age):
        self.name=name
        self.age=age
    def data(self):
        print(f"employee name is -->{self.name}")
        print(f"employee age is -->{self.age}")
class team_two(team):
    def employee(self,name,age,dept,salary):
        super().employee(name,age)
        self.dept=dept
        self.salary=salary
    def information(self):
        print(f"department is -->{self.dept}")
        print(f"salary is -->{self.salary}")

class team_three(team_two):
    def employee(self,name,age,dept,salary,id,exp,project):
        super().employee(name,age,dept,salary)
        self.id=id
        self.experience=exp    
        self.project=project
    def details(self):
        print(f"the project name is -->{self.project}")
        print(f"the experience is -->{self.experience}")
        print(f"the employee id is -->{self.id}")

x=team_three()
x.employee("Rahul",23,"IT",93000,101,5,"web")
x.details()
x.information()
x.data()'''


#using constructor :
'''class team:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def data(self):
        print(f"employee name is -->{self.name}")
        print(f"employee age is -->{self.age}") 
class team_two(team):
    def __init__(self,name,age,dept,salary):
        super().__init__(name,age)
        self.dept=dept
        self.salary=salary
    def information(self):
        print(f"department is -->{self.dept}")
        print(f"salary is -->{self.salary}")

class team_three(team_two):
    def __init__(self,name,age,dept,salary,id,exp,project):
        super().__init__(name,age,dept,salary)
        self.id=id
        self.experience=exp    
        self.project=project
    def details(self):
        print(f"the project name is -->{self.project}")
        print(f"the experience is -->{self.experience}")
        print(f"the employee id is -->{self.id}")
        
x=team_three("Rahul",23,"IT",93000,101,5,"web")
x.details()
x.information()
x.data()
'''

#using class method:
'''class team:
    @classmethod
    def employee(cls,name,age):
        cls.name=name
        cls.age=age
    def data(self):
        print(f"employee name is -->{self.name}")
        print(f"employee age is -->{self.age}")
class team_two(team):
    @classmethod
    def employee(cls,name,age,dept,salary):
        super().employee(name,age)
        cls.dept=dept
        cls.salary=salary
    def information(self):
        print(f"department is -->{self.dept}")
        print(f"salary is -->{self.salary}")

class team_three(team_two):

    @classmethod
    def employee(cls,name,age,dept,salary,id,exp,project):
        super().employee(name,age,dept,salary)
        cls.id=id
        cls.experience=exp    
        cls.project=project
    def details(self):
        print(f"the project name is -->{self.project}")
        print(f"the experience is -->{self.experience}")
        print(f"the employee id is -->{self.id}")   
x=team_three()
x.employee("Rahul",23,"IT",93000,101,5,"web")
x.details()
x.information()
x.data()'''
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

#EXAMPLE:
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"the person name is -->{self.name}")
        print(f"the person age is -->{self.age}")
        
class student(person): #inheritance
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def information(self):
        print(f"the roll number is -->{self.rollno}")

class result(student):
    def __init__(self,name,age,rollno,m1,m2,m3): #constructor chaining
        super().__init__(name,age,rollno)
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
    def calculate(self):
        total=self.marks1+self.marks2+self.marks3
        print(f"total marks is -->{total}")
        avg=total/3
        print(f"total average marks is -->{avg}")

        if avg>=50:
            print("pass")
        else:
            print("fail")
x=result(name="Rahul",age=23,rollno=101,m1=80,m2=90,m3=95)
x.information() 
x.show()
x.calculate()'''
'''
#ecommerce website-->customer-->order-->payment 

class ecommerce:
    def website(self,productname,id):
        self.product=productname
        self.id=id
    def demo(self):
        print(f'product name is {self.product}')
        print(f'product id is {self.id}')
class customer(ecommerce):
    def customerinfo(self,productname,id,customername,address):
        super().website(productname,id)
        self.customername=customername
        self.address=address
    def display(self):
        print(f'customer name :{self.customername}')
        print(f'customer address : {self.address}')
class order(customer):
    def orderinfo(self,productname,id,customername,address,oid,ordercategory):
        super().customerinfo(productname,id,customername,address)
        self.id=id
        self.orderid=oid
        self.ordercategory=ordercategory
    def ordin(self):
        print(f'order id is : {self.orderid}')
        print(f'order category : {self.ordercategory}')
class payment(order):
    def paymentinfo(self,productname,id,customername,address,oid,ordercategory,paymenttype, amount):
        super().orderinfo(productname,id,customername,address,oid,ordercategory)
        self.paymenttype=paymenttype
        self.amount=amount
    def plan(self):
        print(f'payment type is : {self.paymenttype}')
        print(f'total amount is : {self.amount}')

x=payment()
x.paymentinfo("maggi",354,"shreyas","pune",12,"snacks","cash",4566)
x.demo()
x.display()
x.ordin()
x.plan()
'''
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#MULTIPLE INHERIANCE: [method resolution order] 
# when child class take property from more than one parent class it is called as multiple inheritance
#ex-> child take property from both mom and dad
#MRO--> child->p1->p2->object [left->right]

#multiple child take property from single parent 
'''
#syntax:
class parent1:
    pass
class parent2:
    pass
class child(parent1,parent2): #work based on MRO
    pass
object=child()
#first child execute p1 --> p2 --> object
#MRO->method resolution order

#example:
class Father:
    def skill(self):
        print('dad skill')
class Mom:
    def show(self):
        print('extra skill')
class Child(Father,Mom):
    def joy(self):
        print('child class')

x=Child()
x.show()
x.skill()
x.joy()'''

#----------------------------------------------------------------------
#method chaining : it is a process of calling multiple method in single line it is possible only when we are using super function in method(if we add super function in that)
#method chaining is possible only when we are using super function in method

#constructor chaining: it is a process of calling multiple constructor in single line it is possible only when we are using super function in constructor(if we add super function in that)
#constructor chaining is possible only when we are using super function in constructor
#using method: method overloading :
'''class A:  #superparent
    def spam(self):
        super().spam()
        print('A class') #now i will work with the base of MRO
class B:  #parent
    def spam(self):
        print('B class')

class C (A,B): #child
    def spam(self):
        super().spam() #it give output A class not b   -->  execution based on mro -->[child --> p1 --> p2 --> object] to prevent we write super function in a class
        print('c class')

x=C()
x.spam()



class A:  #superparent
    def spam(self):
        print('A class') #now i will work with the base of MRO
        super().spam()
class B:  #parent
    def spam(self):
        print('B class')

class C (A,B): #child
    def spam(self):
                               #it give output A class not b   -->  execution based on mro -->[child --> p1 --> p2 --> object] to prevent we write super function in a class
        print('c class')
        super().spam()
x=C()
x.spam()


#these is mandatory to understand MRO: method resolution order
and also used super function in method to avoid method overloading and also to access parent class data in child class  
print(C.__mro__)
#child-> superparent->parent [C-->A-->B] 
#if we want execute [C->B->A] then we change child class class c(b,a)'''

#----------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#constructor overloading :
'''class A:  #superparent
    def __init__(self):
        print('A class') #now i will work with the base of MRO
        super().__init__()
class B:  #parent
    def __init__(self):
        print('B class')

class C (A,B): #child
    def __init__(self):
      print('c class')
      super().__init__()
        
        
x=C() '''

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

#EXAMPLE --> combination of both 
'''
class Python:
    def __init__(self,rating):
        self.r=rating
    def python_data(self):
        print(f'python subject rating{self.r}')

class sql:
    def __init__ (self,totalclass,t_n):
        self.t=totalclass
        self.n=t_n
    def information(self):
        print(f'total class count is {self.t}')
        print(f'trainer name is {self.n}')
class student(Python,sql):
    def __init__ (self,rating,totalclass,t_n,s_n,age):
        self.student=s_n
        self.age=age
#by help of class also add self in it ------> [recomended]
        # Python.__init__(self,rating)
        # sql.__init__(self,totalclass,t_n)
#by using super function and class name : no requied of self only in class 
        #super().__init__(rating)
        #super().__init__(totalclass,t_n)
#by using only super function:
#at next
    def student_information(self) :
        print(f'student name {self.student} ')
        print(f'student age:{self.age}')

x=student('*',20,'sv','abc',19)
x.student_information()
x.information()
x.python_data()
'''
#-----------------------------------------------
#using only super:
'''class python:
    def __init__(self,rating,*args):
        self.r=rating
        super().__init__(*args)
    def python_data(self):
        print(f'python subject rating{self.r}')

class sql:
    def __init__ (self,totalclass,t_n,*args):
        self.t=totalclass
        self.n=t_n
        super().__init__(*args)
    def information(self):
        print(f'total class count is {self.t}')
        print(f'trainer name is {self.n}')
        
class student(python,sql): #it wok on mro go to python 
    def __init__ (self,rating,totalclass,t_n,s_n,age):
        self.student=s_n
        self.age=age
        super.__init__ (rating,totalclass,t_n)
    def student_information(self) :
        print(f'student name {self.student} ')
        print(f'student age:{self.age}')

x=student('*',20,'sv','abc',19)
x.student_information()
x.information()
x.python_data()
'''
#**kwargs '''

# class p:
#     def __init__(self):
#         print("parent class")
# class q:
#     def __init__(self):
#         print("child class")
#         super().__init__()
# class r(q,p): #r->q->p we use super function in q class so it execute parent class constructor as latest one
#     def __init__(self):
#         print("grand child class")
#         super().__init__()
# x=r()

#IMP:
'''class product: #parent class
    def __init__(self,productname,price):
        self.productname=productname
        self.price=price
    def product_data(self):
        print(f'product name is {self.productname}')
        print(f'product price is {self.price}')
class order: #parent class
        def __init__(self,orderid,ordercategory):
            self.orderid=orderid
            self.ordercategory=ordercategory
        def order_data(self):
            print(f'order id is {self.orderid}')
            print(f'order category is {self.ordercategory}')

class payment(product,order): #child class
    def __init__(self,productname,price,orderid,ordercategory,paymenttype,amount):
        self.paymenttype=paymenttype
        self.amount=amount
        product.__init__(self,productname,price)#using class mandatory to pass self          # super().__init__(productname,price)  [combination of both class method with using super function and class name]
        order.__init__(self,orderid,ordercategory)#using class                               # super().__init__(orderid,ordercategory)
    def payment_data(self):
        print(f'payment type is {self.paymenttype}')
        print(f'total amount is {self.amount}')
x=payment("maggi",20,101,"snacks","cash",4566) #not need to use combined class method because we are using super function in constructor
x.payment_data()
x.product_data()
x.order_data()'''

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

#args: to avoid extra information in constructor we used *args in parent class and child class also to avoid error
'''class product: #parent class
    def __init__(self,productname,price,*args):
        self.productname=productname
        self.price=price
        super().__init__(*args)
    def product_data(self):
        print(f'product name is {self.productname}')
        print(f'product price is {self.price}')
class order: #parent class
        def __init__(self,orderid,ordercategory,*args):
            self.orderid=orderid
            self.ordercategory=ordercategory
            super().__init__(*args)
        def order_data(self):
            print(f'order id is {self.orderid}')
            print(f'order category is {self.ordercategory}')

class payment(product,order): #child class
    def __init__(self,productname,price,orderid,ordercategory,paymenttype,amount):
        self.paymenttype=paymenttype
        self.amount=amount
        super().__init__(productname,price,orderid,ordercategory)  #using super function in constructor
    def payment_data(self):
        print(f'payment type is {self.paymenttype}')
        print(f'total amount is {self.amount}')
x=payment("maggi",20,101,"snacks","cash",4566)
x.payment_data()
x.product_data()
x.order_data()'''

#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------ 
#IMP
#**kwargs: to avoid extra information in constructor we used **kwargs in parent class and child class also to avoid error
'''class product: #parent class
    def __init__(self,productname,price,**kwargs):
        self.productname=productname
        self.price=price
        super().__init__(**kwargs)
    def product_data(self):
        print(f'product name is {self.productname}')
        print(f'product price is {self.price}')

class order: #parent class
        def __init__(self,orderid,ordercategory,**kwargs):
            self.orderid=orderid
            self.ordercategory=ordercategory
            super().__init__(**kwargs)
        def order_data(self):
            print(f'order id is {self.orderid}')
            print(f'order category is {self.ordercategory}')

class payment(product,order): #child class
    def __init__(self,productname,price,orderid,ordercategory,paymenttype,amount):
        self.paymenttype=paymenttype
        self.amount=amount
        super().__init__(productname=productname,price=price,orderid=orderid,ordercategory=ordercategory)  #using super function in constructor
    def payment_data(self):
        print(f'payment type is {self.paymenttype}')
        print(f'total amount is {self.amount}')
x=payment(productname="maggi",price=20,orderid=101,ordercategory="snacks",paymenttype="cash",amount=4566)
x.payment_data()    
x.product_data()
x.order_data()'''

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

#hierachical inheritnce:
#depending upon condition we create an object 
#multiple child take property from single parent 

#syntax: 

'''class parent:
    pass
class child1(parent):
    pass
class child2(parent):
    pass
class child3(parent):
    pass
c=child1()
c1=child2(2)
c2=child3()'''

#example:

'''class Father:
    def Money(self):
        print("dad's money")
class BOY(Father):
    def Bike(self):
        print("new bike")
class Girl(Father):
    def car(self):
        print("new car")

b=BOY()
b.Money()
b.Bike()

g=Girl()
g.Money()
g.car()
'''
#---------------------------------------------------------------------
#method overloading : #imp

#self work inside the class
'''class Father:
    def honey(self):
        print("dad's money")
class BOY(Father):
    def Money(self):
        super().honey()
        #Father.Money(self)
        print("new bike")
class Girl(Father):
    def Money(self):
        super().honey()
       # Father.Money(self) #object is mandatory to pass self in class method
        print("new car")

b=BOY()
b.Money()

g=Girl()
g.Money()'''

#------------------------------------------------------------------------------
#using constructor:
'''class Father:
    def __init__(self):
        print("dad's money")
class BOY(Father):
    def __init__(self):
        super().__init__()
        #Father.Money(self)
        print("new bike")
class Girl(Father):
    def __init__(self):
        super().__init__()
        print("new car")

b=BOY()
g=Girl()
'''
#---------------------------------------------------------------------

# using paramter: method with paramter
'''
class school:
    def school_information(self,s_name,add,fees,contact) :
        self.n=s_name
        self.add=add
        self.f=fees
        self.m=contact
    def data(self):
        print(f'school name {self.n}')
        print(f'school address{self.add}')
        print(f'school fees {self.f}')
        print(f'school contact {self.m}')

class student(school):
    def school_information(self,s_name,add,fees,contact,name,score):
        super().school_information(s_name,add,fees,contact)
        self.student=name
        self.marks=score
    def student_info(self):
        print(f'student name {self.student}')
        print(f'student score{self.marks}')

class teacher(school):
    def school_information(self,s_name,add,fees,contact,t_name,sal):
        super().school_information(s_name,add,fees,contact)
        self.teachername=t_name
        self.salary=sal
    def teacher_data(self):
         print(f'teacher name {self.teachername}')
         print(f'teacher salary{self.salary}')

x=student()
x.school_information("usa","pune",5000,6876595765,"shreyas",78)
x.data()
x.student_info()

y=teacher()
y.school_information("usa","pune",5000,6876595765,"ram",78000)
y.data()
y.teacher_data()'''

#--------------------------------------------------------------------------------
#using constructor:
'''class school:
    def __init__(self,s_name,add,fees,contact) :
        self.n=s_name
        self.add=add
        self.f=fees
        self.m=contact

    def data(self):
        print(f'school name {self.n}')
        print(f'school address{self.add}')
        print(f'school fees {self.f}')
        print(f'school contact {self.m}')

class student(school):
    def __init__(self,s_name,add,fees,contact,name,score):
        super().__init__(s_name,add,fees,contact)
        self.student=name
        self.marks=score

        self.student_info()
        school.data(self)
    def student_info(self):
        print(f'student name {self.student}')
        print(f'student score{self.marks}')

class teacher(school):
    def __init__(self,s_name,add,fees,contact,t_name,sal):
        super().__init__(s_name,add,fees,contact)
        self.teachername=t_name
        self.salary=sal
 
        self.teacher_data()
        school.data(self)
    def teacher_data(self):
         print(f'teacher name {self.teachername}')
         print(f'teacher salary{self.salary}')
        
x=student("usa","pune",5000,6876595765,"shreyas",78)
y=teacher("usa","pune",5000,6876595765,"ram",78000)'''

#-------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

#Hybrid : it is a combination of more than one inheritance method it is called as hybrid inheritance
# combination of one or more inhertiance (combination of all inheritance method)
#print(w.__mro__) #check the execution flow of hybrid inheritance it work left to right
#combination of one more than one inheritance

'''class bank:
    def bank_name(self,name):
        self.name=name
        print(f'bankname is -->{self.name}')
class Account(bank):
    def bank_details(self,add):
        self.add=add
        print(f'current bank location--> {self.add}')
class loan: #independent class (no connection)
    def loan_information(self,totalamount,intrestrate):
        self.t=totalamount
        self.i=intrestrate
        print(f'total amount is-{self.t}')
        print(f'total intrestrate ->{ self.i}')
class customer(Account,loan): #multiple inheritance
    def customer_information(self,name,age,location):
        self.name=name
        self.age=age
        self.l=location
        print(f'customer name is: {self.name}')
        print(f'customer age is {self.age}')
        print(f'customer loaction is :{self.l}')
x=customer()
x.customer_information("shreyas",23,"pune")
x.loan_information(1234,10)
x.bank_details("pune")
x.bank_name("SBI")'''

#------------------------------------------------------------------

#Example 2:
'''
class first_day: #parent class
    def display(self):
        print("first class")
class student(first_day): #single level #child class
    def student_information(self,name):
        self.name=name
        print(f'student name is {self.name}')
class collage_data(student):
    def collage_information(self,cname):
        self.collagename=cname
        print(f'collage name is :{self.collagename}')
class second_day(first_day): #child class #hirrarchacy #independent
    def show(self):
        print("second day")
class Exam_data:
    def exam_data(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
        print(f'first day subject is {self.sub1}')
        print(f'second subject is{self.sub2}')
class result(collage_data,Exam_data): #mutiple inhertiance
    def demo(self,examresultout):
        self.examresult=examresultout
    def all_method_collection_in_one_class(self):# in single method all method should we called here
        self.display()
        self.student_information("usa")
        self.collage_information("st paul")
        self.exam_data("python","java")
        self.demo("yes")

r=result()
r.all_method_collection_in_one_class()

e=second_day() #independent 
e.show()'''


'''
class first_day: #parent class
    def display(self):
        print("first class")
class student(first_day): #single level #child class
    def student_information(self,name):
        self.name=name
        print(f'student name is {self.name}')
class collage_data(student):
    def collage_information(self,name,cname):
        super().student_information(name)
        self.collagename=cname
        print(f'collage name is :{self.collagename}')
class second_day(first_day): #child class #hirrarchacy #independent
    def show(self):
        print("second day")
class Exam_data:
    def exam_data(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
        print(f'first day subject is {self.sub1}')
        print(f'second subject is{self.sub2}')
class result(collage_data,Exam_data): #mutiple inhertiance
    def demo(self,name,cname,sub1,sub2,examresultout):
        super().collage_information(name,cname)
        super().exam_data(sub1,sub2)
        self.examresult=examresultout
    def all_method_collection_in_one_class(self):# in single method all method should we called here
        self.display()
        self.demo("shreyas","usa","python","sql","yes")

r=result()
r.all_method_collection_in_one_class()

e=second_day() #independent 
e.show()
'''
#hirrarchyy method: when we have more than one child class take property from single parent class it is called as hirrarchy method
class first_day:   # Parent
    def display(self):
        print("first class")

class student(first_day):   # Child 1
    ...

class second_day(first_day):   # Child 2
    ...
#-----------------------------------------------------------------------------------------

#Example:
'''
class Amazon:
    def display(self):
        print("wlecome to amazon ")
class product_information(Amazon):
   def product_data(self,productname,totalproduct,price):
       self.productname=productname
       self.totalproduct=totalproduct
       self.price=price
   def product_display(self):
       print(f'product name is {self.productname}')
       print(f'total product :{self.productname}')
       print(f'total price :{self.price}')
class delivery(product_information):
    def location(self,add):
        self.address=add
        print(f'current loaction is {self.address}')
class paymentmode(Amazon): #hirrarcy method need to create seprate objectg
    def mode(self,paymentmode):
        self.paymentmode=paymentmode
        print(f'payment mode cash or online (y/n):{self.paymentmode}')
class product_quality:#indepent class
    def feedback(self,rating):
        self.rating=rating
        print(f'product feedback rating is {self.rating}')
class customer(delivery, paymentmode):
    def customer_info(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(f'customer name is {self.name}')
        print(f'customer age : {self.age}')
        print(f'gender : {self.gender}')

x=customer()
x.display()
x.product_data("toys",15,2000)
x.location("pune")
x.customer_info("shreyas",22,"male")
#x.mode("online")
x.feedback("good") #error because product quality is independent class to access this we need to create seprate object

# z = product_quality()
# z.feedback("good")


'''
#-------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

#using constructor:
'''
class Amazon:
    def __init__(self):
        print("wlecome to amazon ")

class product_information(Amazon):
   def __init__ (self,productname,totalproduct,price):
       self.productname=productname
       self.totalproduct=totalproduct
       self.price=price
   def __init__ (self):
       print(f'product name is {self.productname}')
       print(f'total product :{self.productname}')
       print(f'total price :{self.price}')

class delivery(product_information):
    def __init__(self,add):
        self.address=add
        print(f'current loaction is {self.address}')

class paymentmode(Amazon): #hirrarcy method need to create seprate object
    def __init__ (self,paymentmode):
        self.paymentmode=paymentmode
        print(f'payment mode cash or online (y/n):{self.paymentmode}')

class product_quality:#indepent class
    def __init__(self,rating):
        self.rating=rating
        print(f'product feedback rating is {self.rating}')

class customer(delivery,product_quality):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(f'customer name is {self.name}')
        print(f'customer age : {self.age}')
        print(f'gender : {self.gender}')

x=customer()
x.display()
x.product_data("toys",15,2000)
x.location("pune")
x.customer_info("shreyas",22,"male")

z = product_quality()
z.feedback("good")

k=paymentmode()'''
# k.mode("online")


#Example 2:
'''class player:
    def __init__(self, player_n):
        self.playername = player_n

    def display_playername(self):
        print(f'playername is {self.playername}')


class batsman(player):
    def __init__(self, player_n, runs):
        player.__init__(self, player_n)   # ✅ direct call
        self.runs = runs

    def display_runs(self):
        print(f'total runs --> {self.runs}')


class bowler(player):
    def __init__(self, player_n, wicket):
        player.__init__(self, player_n)   # ✅ direct call
        self.wicket = wicket

    def display_wickets(self):
        print(f'no of wicket -> {self.wicket}')


class player_information(batsman, bowler):
    def __init__(self, player_n, runs, wicket, country):
        batsman.__init__(self, player_n, runs)
        bowler.__init__(self, player_n, wicket)
        self.country = country

    def display_country(self):
        print(f'country name is {self.country}')


x = player_information("shreyas", 100, 4, "india")

x.display_playername()
x.display_runs()
x.display_wickets()
x.display_country()'''
'''
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------


#EXAMPLE : IMP 
class one:
    def __init__ (self,s_n,marks):
        self.s=s_n
        self.m=marks
    def onedata(self):
        print(f'student_name--> {self.s}')
        print(f'total marks is {self.m}')
class two(one):
    def __init__(self,s_n,marks,age):
        one.__init__(self,s_n,marks) #constructor overloading using class to avoid we use
        self.age=age
    def age_data(self):
        print(f'age is {self.age}')
class three(two):
    def __init__(self,s_n,marks,age,batchcode):
        two.__init__(self,s_n,marks,age)
        self.batchcode=batchcode
    def batchcode_info(self):
        print(f'batch code is -->{self.batchcode}')
class teacher: #independent class
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
    def subject_info(self):
        print(f'first_subject name is {self.sub1}')
        print(f'second_ subject name is {self.sub2}')
class four(three,teacher):
    def __init__(self,s_n,marks,age,batchcode,sub1,sub2,clgname):
        three.__init__(self,s_n,marks,age,batchcode)
        teacher.__init__(self,sub1,sub2)
        self.clg_name=clgname
    def clg_data(self):
        print(f'clg_name is {self.clg_name}')

q=four("shreyas",55,22,12,"python","sql","usa")
q.onedata()
q.age_data()
q.batchcode_info()
q.subject_info()
q.clg_data()'''

#----------------------------------------------------------------------------------

#using kwrgs:
'''class one:
    def __init__ (self,s_n,marks,**kwargs): # we pass extra paramter we used kwargs
        self.s=s_n
        self.m=marks
        super().__init__(**kwargs)
    def onedata(self):
        print(f'student_name--> {self.s}')
        print(f'total marks is {self.m}')
class two(one):
    def __init__(self,s_n,marks,age,**kwargs):
        self.age=age
        super().__init__(s_n,marks,**kwargs)
    def age_data(self):
        print(f'age is {self.age}')
class three(two):
    def __init__(self,s_n,marks,age,batchcode,**kwargs):
        self.batchcode=batchcode
        super().__init__(s_n,marks,age,**kwargs) #constructor overloading avoid
    def batchcode_info(self):
        print(f'batch code is -->{self.batchcode}')
class teacher: #independent class
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
    def subject_info(self):
        print(f'first_subject name is {self.sub1}')
        print(f'second_ subject name is {self.sub2}')
class four(three,teacher):
    def __init__(self,s_n,marks,age,batchcode,sub1,sub2,clgname,**kwargs):
        self.clg_name=clgname
        super().__init__(s_n = s_n,marks=marks,age=age,batchcode=batchcode,sub1=sub1,sub2=sub2,**kwargs)#constructor overloading avoid
    def clg_data(self):
        print(f'clg_name is {self.clg_name}')

q=four("shreyas",55,22,12,"python","sql","usa")
q.onedata()
q.age_data()
q.batchcode_info()
q.subject_info()
q.clg_data()
'''
#-------------------------------------------------------------
#HAS - A RELATIONSHIP:class test data acess using another class (aqlso known composition )

'''class one:
    def spam(self):

class two:
    def demo(self):
        s=test()
        s.spam()
        print(s.x)
        print("demo classes")

t=two()
t.demo()'''

#--------------------------------------------------
'''class a:
    def __init__(self):
        print("a class data")

class b:
    def __init__ (self):
        print("b class data")
    def show(self):
        A=a()
        A.demo()
        print("show class data")

x=b()
x.demo()

what is inheitance difference betwwen multilevel and multiple inheritance how to achieve using mro how compostion dfference from is - a relationship
class x: #parent
class y(x):
class z(y): error  class z(x) these correct diamond program


#diamond shape :
class a:
class b(a):
class c(a):
class d(b,c:)

#in hirarciichal object creation differenr differnt
#different implementation overloading'''