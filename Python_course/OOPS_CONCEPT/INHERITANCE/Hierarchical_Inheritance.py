'''
HIERARCHICAL INHERITANCE:
--------------------------
-Multiple children will take the properties from single parent

                       parent
                       |
                       |
        ------------------------------------               
       |               |                   |
    child1           child2              child3


------------------------------------------------
syntax:
class Parent:
    pass
class Child1(Parent):
    pass
class Child2(Parent):
    pass
class Child3(Parent):
    pass
c1=Child1()
c2=Child2()
c3=Child3()
----------------------------------------------
-NOTE: depending upon childrens we have to create object.



'''
#ex1
class Father:
    def Money(self):
        print("Dad's money")
class Son(Father):
    def bike(self):
        print("new--bike")
class Daughter(Father):
    def Car(self):
        print("new----car")
s=Son()   #for son obj
s.bike()
s.Money()
d=Daughter()   #for daughter obj
d.Car()
d.Money()
print("----------------------------------")

#ex2   method overloading
class Father:
    def Money(self):
        print("Dad's money")
class Son(Father):
    def Money(self):
        # super().Money()  #using super
        Father.Money(self)   #class name
        print("son's money")
class Daughter(Father):
    def Money(self):
        Father.Money(self)
        print("Daughter's money")
s=Son()   #for son obj
s.Money()
print()
#for daughter class
d=Daughter()
d.Money()
print("-----------------------")

#ex2   constructor overloading
class Father:
    def __init__(self):
        print("Dad's money")
class Son(Father):
    def __init__(self):
        # super().Money()  #using super
        Father.__init__(self)   #class name
        print("son's money")
class Daughter(Father):
    def __init__(self):
        Father.__init__(self)
        print("Daughter's money")
s=Son()   #for son obj
print()
#for daughter class
d=Daughter()
print("-----------------------")

#ex3-----method overloading
class School:   #---parent class
    def school_info(self,sname,add,fees):
        self.sname=sname
        self.add=add
        self.fees=fees
    def data(self):
        print(f"school name is {self.sname}\n"
              f"school address is {self.add}\n"
              f"fees is {self.fees}")
class Student(School):
    def school_info(self,sname,add,fees,std_name,score):
        super().school_info(sname,add,fees)
        self.std_name=std_name
        self.score=score
    def std_info(self):
        print(f"student name is {self.std_name}\n"
              f"total marks are {self.score}")
class Teacher(School):
    def school_info(self, sname, add, fees,tname,sal):
        super().school_info(sname,add,fees)
        self.tname=tname
        self.sal=sal
    def teacher_data(self):
        print(f"Teacher name:{self.tname}\n"
              f"teacher salary :{self.sal}")
#for student child class
s=Student()
s.school_info(sname="JKIS",add="Parbhani",fees=30000,std_name="divyaa",score=88)
s.data()
s.std_info()
print()

#for teacher child class
t=Teacher()
t.school_info(sname="JKIS",add="Parbhani",fees=30000,tname="XYZ",sal="80k")
t.data()
t.teacher_data()
print("------------------------------------------------")

#ex3   constructor overloading
class School:   #---parent class
    def __init__(self,sname,add,fees):
        self.sname=sname
        self.add=add
        self.fees=fees
    def data(self):
        print(f"school name is {self.sname}\n"
              f"school address is {self.add}\n"
              f"fees is {self.fees}")
class Student(School):
    def __init__(self,sname,add,fees,std_name,score):
        super().__init__(sname,add,fees)
        self.std_name=std_name
        self.score=score
    def std_info(self):
        print(f"student name is {self.std_name}\n"
              f"total marks are {self.score}")
class Teacher(School):
    def __init__(self, sname, add, fees,tname,sal):
        super().__init__(sname,add,fees)
        self.tname=tname
        self.sal=sal
    def teacher_data(self):
        print(f"Teacher name:{self.tname}\n"
              f"teacher salary :{self.sal}")
#for student child class
s=Student(sname="JKIS",add="Parbhani",fees=30000,std_name="divyaa",score=88)
s.data()
s.std_info()
print()

#for teacher child class
t=Teacher(sname="JKIS",add="Parbhani",fees=30000,tname="XYZ",sal="30k")
t.data()
t.teacher_data()
print("------------------------------------------------")

class Employee:
    def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
    def emp_data(self):
        print(f"employee name is {self.ename}\n"
              f"employee id is {self.eid}")
class Team1(Employee):
    def __init__(self,position):
        super().__init__(ename="smith",eid=10001)
        self.position=position
    def team_data(self):
        print(f"employee position in team is {self.position}")
class Team2(Employee):
    def __init__(self,role):
        super().__init__(name="allen",eid=3002)
        self.role=role
    def team2_data(self):
        print(f"employee role is{self.role}")
t1=Team1("leader")
t1.emp_data()
t1.team_data()
print()
t2=Team2()
# t2.emp_data()
t2.team2_data()



        


