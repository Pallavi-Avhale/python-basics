# class Parent_1:
#     bal="3lac"

#     def House(self):
#         print("It's parent house")

# class Child(Parent_1):

#     def Study(self):
#         print("I'm studying ")

# c=Child()
# c.Study()
# print("-----")
# c.House()
# print("-----")
# print(c.bal)


class Parent_1:
    def __init__(self, name):
        self.name=name
        print(self.name)

class Child(Parent_1):
    def __init__(self, college):
        super().__init__("XYZ")
        self.college=college
        print(self.college)

c=Child("MIBS")


print()

class Student:                                      # Parent class ---> Student
    def student_data(self,name,sub): 
        self.name=name 
        self.sub=sub 
        print(f'Student Name is {self.name}') 
        print(f'SUbject Name is {self.sub}') 
class Information(Student):                         # Child class ---> Information
    def student_data(self,clg_name,marks): 
        super().student_data(name="XYZ",sub="SQL") 
        self.clg=clg_name 
        self.marks=marks 
        print(f'CLG Name is {self.clg}') 
        print(f'Total Marks is {self.marks}') 

i=Information() 
i.student_data("PYSPIDERS",99)

print()


class Amazon:                                          # Parent_Class

    def Product(self, Prod_Name, Prod_price):
        self.P_name=Prod_Name
        self.P_P=Prod_price
        print(f' Product name is {self.P_name}')
        print(f' Product Price is {self.P_P} ')

class Info(Amazon):                                   # Child_Class

    def Product(self, Loc, Delivery):
        super().Product("Laptop", "1 lac ")

        self.L=Loc
        self.D=Delivery
        print(f' Location is { self.L}')
        print(f' Delivered at {self.D}')

        


# Object Creation for child class

i=Info()

i.Product("Pune","01-09-2026")
print("-----")

print(i.P_name)                 # Laptop

print("-----")

print(i.P_P)                    # 1 lac
print("-----")

print(i.L)                     # Pune
print("-----")

print(i.D)                     # 01-09-2026


print("---   NEW   ---")

print()



print(" ------------ MULTI LEVEL INHERITANCE -----------")
print()

class Grand_parent:
    def Village(self, v_name):
        self.V=v_name
        print(f' Grand parents Village is {self.V}')

class Parent(Grand_parent):
    def Village(self, City):
        super().Village(v_name="Vaijapur")
        self.C=City
        print(f' Parents city name is {self.C}')

class Child(Parent):
    def Village(self, Town):
        super().Village("Pune")
        self.T=Town
        print(f' Child is from {self.T}')   

C=Child()

C.Village("MAXICO")
print("------------")


print(C.V)
print("------------")

print(C.C)
print("------------")

print(C.T)
print("------------")


print(" ------------ MULTI INHERITANCE -----------")

print()


class Parent_1:
    def Inf(self, parent_1):
        self.P_1=parent_1
        print(f' parent_1 name is {self.P_1}')

class Parent_2:
    def Inf(self, Parent_2):
        self.P_2=Parent_2
        print(f' Parent_2 name is {self.P_2}')

class Child_M(Parent_1,Parent_2):                      # MRO ---> METHOD RESOLUTION OBJECT  ----> CHILD ---> PARENT_1 ---> PARENT_2
    def Inf(self, Child_name):
        super().Inf("Father")
        Parent_2.Inf(self,"Mother")
        self.child=Child_name
        print(f' child name is {self.child}')


N=Child_M()

N.Inf("Ravi")


print("-------------------------------")

print()



class Parent1: 
    def __init__(self, name): 
        print(f"Parent1 Constructor: Hello {name}") 
 
    def show(self, age): 
        print(f"Parent1 Show: Age is {age}") 
 

class Parent2: 
    def __init__(self, city): 
        print(f"Parent2 Constructor: You live in {city}") 
 
    def show(self, country): 
        print(f"Parent2 Show: Country is {country}") 
 
class Child(Parent1, Parent2): 
    def __init__(self, name, city): 
        print("Child Constructor starts") 
        super().__init__(name)               # Calls Parent1 first (MRO) 
        Parent2.__init__(self, city)         # Manually call second parent 
        print("Child Constructor ends") 
 
    def show(self, age, country): 
        print("Child Show Method") 
        super().show(age)                    # Calls Parent1's show 
        Parent2.show(self, country)          # Manually call Parent2's show 
# Test 
c = Child("Prince", "Bangalore") 
c.show(25, "India")

print("-------------------------------")

print()

# Example 03  With __init__() Constructor 



class Company:                              # PARENT CLASS
    def __init__(self, name): 
        self.company_name = name 

    def show_company(self): 
        print(f"Company Name: {self.company_name}") 

class Employee(Company):                     # CHILD CLASS 1

    def __init__(self, emp_name, emp_id): 
        super().__init__("TECHCORP")
        self.emp_name = emp_name 
        self.emp_id = emp_id 

    def show_employee(self): 
        print(f"Employee: {self.emp_name}, ID: {self.emp_id}") 

class Manager(Company):                       # CHILD CLASS 2

    def __init__(self, name, mgr_name, dept): 
        super().__init__(name) 
        self.mgr_name = mgr_name 
        self.dept = dept 
    def show_manager(self): 
        print(f"Manager: {self.mgr_name}, Department: {self.dept}") 

# Creating objects 
e = Employee( "Alice", 101)
m = Manager("TechCorp", "Bob", "HR") 
e.show_company() 
e.show_employee() 
m.show_company() 
m.show_manager() 


print("----------DIFFERENT------------")
print()


class Company:                              # PARENT CLASS
    def __init__(self, name): 
        self.company_name = name 

    def show_company(self): 
        print(f"Company Name: {self.company_name}") 

class Employee(Company):                     # CHILD CLASS 1

    def __init__(self, name, emp_name, emp_id): 
        super().__init__(name)
        self.emp_name = emp_name 
        self.emp_id = emp_id 

    def show_employee(self): 
        print(f"Employee: {self.emp_name}, ID: {self.emp_id}") 

class Manager(Company):                       # CHILD CLASS 2

    def __init__(self, name, mgr_name, dept): 
        super().__init__(name) 
        self.mgr_name = mgr_name 
        self.dept = dept 
    def show_manager(self): 
        print(f"Manager: {self.mgr_name}, Department: {self.dept}") 

# Creating objects 
e = Employee("TECHCORP", "Alice", 101)
m = Manager("TechCorp", "Bob", "HR") 
e.show_company() 
e.show_employee() 
m.show_company() 
m.show_manager() 


print(" -----------------HYBRID INHERITANCE ------------------------------ ")

print()

 
# SINGLE LEVEL INHERITANCE  
# class A:                                     # Parent class
#    a = 10 
 

# HERARCHY INHERITANCE
# class B(A):                                  # child class 1---> single level
#    b = 20 
 
# class C(A):                                  # child class 2
#    c = 30 
 
# MULTIPLE INHERITANCE
# class D(B, C):                                 
#    d = 40

# Hybrid with super() & Method Resolution Order (MRO) 

class A: 
    def show(self): 
        print("A class method") 

# HIERARCHY 

class B(A): 
    def show(self): 
        print("B class method") 
        super().show() 

class C(A): 
    def show(self): 
        print("C class method") 
        super().show() 

# MULTIPLE 

class D(B, C):                     
    def show(self): 
        print("D class method") 
        super().show() 

d=D()
d.show()

print("------------")
print()

b=B()
b.show()

print("---------------------COMPOSITE KEY--------------------")
print()

class Engine: 
    def start(self): 
        print("Engine started...") 
    def stop(self): 
        print("Engine stopped...") 

# Class 2: Car uses Engine (Composition) 
class Car: 
    def __init__(self, brand): 
        self.brand = brand 
        self.engine = Engine()   # Composition: Car HAS an Engine 

    def drive(self): 
        print(f"Driving {self.brand} car") 
        self.engine.start() 

    def park(self): 
        print(f"Parking {self.brand} car") 
        self.engine.stop() 
 
# Using Car class 
c = Car("Tesla") 
c.drive() 
c.park() 



print("-------------------------------Encapsulation-------------------------------------")
print()
print("-------------------------------private-------------------------------------")

class Employee: 
    def __init__(self,name,pay): 
        self.name = name 
        self.pay = pay 
        print(self.name )
        print(self.pay)
    def disp(self): 
        print("in display") 
 
e = Employee("amith", 100) 
print(e.name)   
e.disp()    #in display
print()


print()
print("-------------------------------protected-------------------------------------")

 

class Emp: 
    _pin = 3245 
    def _disp(self): 
        print("in display") 

e = Emp() 
print(e._pin)  
e._disp()     
e._pin = 3322 
print(e._pin)       

print("--------------------------")

class Emp: 
    def __init__(self, name, pay): 
        self._name = name 
        self._pay = pay 
    def disp(self): 
        print("in display") 
e=Emp("PQR", 70000)
print(e._name)  
e.disp()
print(e._pay) 

print("-------------------")


class Emp: 
    _pin = 90000 
    def _disp(self): 
        print("in ---- display") 
    def getters(self): 
        return self._pin 
    def setters(self, pin): 
        self._pin = pin 
e = Emp()  
pin = e.getters() 
print(pin) 
e.setters(4444) 
pin = e.getters() 
print(pin) 
print("--------------------")

class Bank:
    _bal=3000

    def __init__(self):
        print("ZERO BALANCE AVAILABLE")

    def getters(self):                       # getting the values
        return self._bal

    def setters(self, B):
        self._bal=B

p=Bank()
print(p.getters())

print()
p.setters("pii")
print(p.getters())




print()
print("-------------------------------private-------------------------------------")
print()

class Emp: 
    def __init__(self, name, pay): 
        self.__name = name 
        self.__pay = pay 
    def display(self): 
        print("display") 
e = Emp("apu", 1000) 


# print(e.__name)     # ---> AttributeError: 'Emp' object has no attribute '__name'

print(e._Emp__name)  
print()
print(e._Emp__pay)
print()
e.display()
print()

print(e.__dict__)


print("-------------------------GETTER----------SETTER-----------DELETTER-----------------------------------")
print()

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
# #after doing modification again we need to get the values then call getter method 
print("-----")
a.Getter()
a.deleter()
# a.Getter()
print("---------------------------")

print()



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
print(h.Getter())
h.Setter("HDFC","DITYAA",15000)
print("---")
# #after doing modification again we need to get the values then call getter method 
print(h.Getter())
h.Deleter()
# print(getattr(h,_name))
print("--------------------------")
print()

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
h1.Deleter()
print(h1.Getter())
print("--------------------------")
