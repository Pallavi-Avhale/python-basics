'''
COMPOISTION(Has-A Relationship)
-------------------------------------
-Has-A Relationship means Without acquiring we can access the data from one class to another class.

Advantages of Has-A Relationship
1. Code Reusability.


'''
#ex1 normal way---->method
class Test:
    a=1000
    def spam(self):
        print("welcome")
class Two:
    def demo(self):
        #if we want to create first class object into second class
        #now if i run/call second class both the 1st and 2nd class data will get executed
        x=Test()
        x.spam()
        print(x.a)     #accessing one class var. into another class
        print("demo class")
t=Two()
t.demo()
print("-------------------------------------------")


#ex1 normal way---->constructor
class A:
    def __init__(self):
        print("A class data")
    def demo(self):
        print("A class demo")
class B:
    def __init__(self):
        print("B class data")
    def show(self):
        print("B class show")
        a=A()
        a.demo()
b=B()
b.show()
print("-----------------------------------")

class A:
    def __init__(self):
        print("A class data")
    def demo(self):
        print("A class demo")
class B:
    def __init__(self):
        self.w=A()    #calling first class through self to execute constructor-------> {self.new_var=ClassName()}
        self.w.demo()    #calling the method of class A----> self.objecName.method_name()
        print("B class data")
    def show(self):
        print("B class show")
b=B()
b.show()
print("-----------------------------------")

class College:
    def __init__(self,name):
        self.name=name
    def demo(self):
        print("name is ",self.name)
class Student(College):
    def __init__(self,branch):
        self.b=branch
        super().__init__("diems")
        self.w=College("diems")
        self.w.demo()
        print("branch is",self.b)
s=Student("cse")

print('--------------------------') 

#ex2
class Demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def data(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
class Show:
    def __init__(self,marks):
        self.marks=marks
    def Marks(self):
        self.x=Demo("xyz",99)
        self.x.data()
        print(f"marks are {self.marks}")
e=Show(99)
e.Marks()
print("-------------------------------")

'''
Imp questions--->
DIFFERENCE BETWEEN IS-A RELATIONSHIP AND HAS-A RELATIONSHIP
What is composition and difference between inheritance and composition
'''

#how to create MRO Error
#Due to the data inconsistency we will get MRO error
class X:
    pass
class Y(X):
    pass
class Z(X):
    pass
class E(Y,Z):
    print("data is working")
e=E()
print("------------------------------------------")


class School:
    x=10
    def spam(self,a):
        self.a=a
        print("school class")
class Student(School):
    def demo(self):
        w=School()
        w.spam(10)
        print(w.a)
        print("student class")
s=Student()
s.spam(100)
s.demo()
print("----------------------------------")

class Student:
    x=10
    def spam(self,name,marks):
        self.n=name
        self.m=marks
    def printing(self):
        print(f"student name is {self.n}\n"
              f"marks = {self.m}")
class School:
    def demo(self,sname):
        self.s=sname
        print(f"school name is {self.s}")
        w=Student()
        w.spam("divya",88)
        w.printing()
s=School()
# s.spam("divya",88)
s.demo("JKIS")
print("-----------------------------------")


class Bank:
    def __init__(self,bank,bal):
        self.b=bank
        self.bal=bal
    def info(self):
        print(f"bank name is ",self.b)
        print(f"Balance name is ",self.bal)
class Account:
    def __init__(self,holder):
        self.h=holder
        # super().__init__("sbi",10000)
        self.q=Bank("sbi",10000)
        self.q.info()
        print(f"account holder is {self.h}")
a=Account("divyaaa")
print("---------------------------")

class Test:
    def spam(self,name):
        self.n=name
        print("name is ",self.n)
class Two:
    def demo(self,age):
        self.a=age
        p=Test()
        p.spam("priyaaa")
        print("age is ",self.a)
t=Two()
t.demo(21)
print("------------------------")

class Test:
    def __init__(self):
        print("welcome")
class Info:
    def demo(self):
        self.w=Test()
        print("class2")
i=Info()
i.demo()
print('----------------------------')
        
    
        

