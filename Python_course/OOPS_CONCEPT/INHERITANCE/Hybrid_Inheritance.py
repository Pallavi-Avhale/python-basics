'''
HYBRID INHERITANCE:
-------------------
-combination of one/more inheritance.
parent class data will present in 2subclasses and
that 2 subclasses data will present in single child class.

-depending upon the child we can create the objects.

                 A

                 
    B                             C


                 D

class X:
    pass
class Y(X):
    pass
class Z(X):
    pass
class W(Y,Z):
    pass
e=W()
print(W.__mro__)
# o/p: (<class '__main__.W'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.X'>, <class 'object'>)

'''
print("-----------------------------------------")
#ex1
class Bank:
    def bank_name(self,name):
        self.name=name
        print(f"Bank name is {self.name}")
class Account(Bank):
    def bank_details(self,add):
        self.add=add
        print(f"current bank location is {self.add}")
class Loan:
    def loan_info(self,total_amount,interest):
        self.total_amount=total_amount
        self.interest=interest
        print(f"Total ammount is {self.interest}")
        print(f"interest rate is {self.interest}")
class Customer(Account,Loan):
    def customer_info(self,name,age,loc):
        self.name=name=name
        self.age=age 
        self.loc=loc
        print(f"customer name is {self.name}\n"
              f"customer age is {self.age}\n"
              f"customer locaton is {self.loc}")
x=Customer()
x.customer_info("divya",21,"pune")
x.loan_info(10000,1000)
x.bank_name("SBI")
x.bank_details("Parbhani")
print("--------------------------------------------")

#ex2
class First_day:
    def display(self):
        print("First day class info")
class Student(First_day):
    def stud_info(self,name):
        self.name=name
        print(f"student name is {self.name}")
class Clg_data(Student):
    def clg_info(self,cname):
        self.cname=cname
        print(f"college name is{self.cname}")
class Second_Day(First_day):
    def show(self):
        print(f"Second class info...")
class Exam:                 #independent class
    def exam_info(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
        print(f"First subject is {self.sub1}")
        print(f"second subject is {self.sub2}")
class Result(Clg_data,Exam):
    def demo(self):
        print("exam result out")
    def All_method_collection_in_one_class(self):
        self.display()
        self.stud_info("Priya")
        self.clg_info("MGM")
        # self.show()   #not possible it is independent class
        self.exam_info("math","science")
        self.demo()
r=Result()
r.display()   #First day class info
r.stud_info("Priyaa")   #student name is Priyaa
r.clg_info("MGM")       #college name isMGM
r.exam_info("math","science")  #second subject is science
r.demo()                  #exam result out
e=Second_Day()
e.show()                #Second class info...
print("-------------------------------------------")

#ex3
class Amazon:
    def welcome(self):
        print("welcome to amazon")
class ProdInfo(Amazon):
    def product(self,prod_name,price):
        self.prod_name=prod_name
        self.price=price
        print(f"product name is {self.prod_name}\n"
              f"product price is {self.price}")
class Delivery(ProdInfo):
    def delivery_add(self,add):
        self.add=add
        print(f"product delivery address is {self.add}")
class Payment(Amazon):
    def pay_mode(self,mode):
        self.mode=mode
        print(f"payment mode is {self.mode}")
class Prod_quality:
    def quality(self):
        print(f"Good product reviews")
class Customer(Delivery,Prod_quality):
    def customer_info(self,cname):
        self.cname=cname
        print(f"Customer name is {self.cname}")
c=Customer()
c.welcome()               #welcome to amazon
c.product("Iphone",80000) #product name is Iphone
                          # product price is 80000

# c.pay_mode("online")
c.quality()                  #Good product reviews
c.customer_info("divyaaa")   #Customer name is divyaaa
c.delivery_add("mumbai")     #product delivery address is mumbai
p=Payment()
p.pay_mode("online")         #payment mode is online
print("-----------------------------")


#ex4
class Player:
    def __init__(self,pname):
        self.pname=pname
    def playerName(self):
        print(f"player name is {self.pname}")
class Batsman(Player):
    def __init__(self,pname,runs):
        Player.__init__(self,pname)
        self.runs=runs
    def Runs(self):
        print(f"Total runs {self.runs}")
class Bowler(Player):
    def __init__(self,pname,wickets):
        Player.__init__(self,pname)
        self.wickets=wickets
    def Wicket(self):
        print(f"Total wickets are {self.wickets}")
class PlayerInfo(Batsman,Bowler):
    def __init__(self,pname,runs,wickets,country):
        Batsman.__init__(self,pname,runs)
        Bowler.__init__(self,pname,wickets)    
        self.country=country
    def Country(self):
        print(f"Player's country name is {self.country}")
        self.playerName()   #or Player.playerName(self)
        self.Runs()         #Batsman.Runs(self)
        self.Wicket()       #Bowler.Wicket(self)
p=PlayerInfo("RS",300,1,'India')
# p.playerName()
# p.Runs()
# p.Wicket()
p.Country()
print("--------------------------------------------")


#ex4
class Player:
    def __init__(self,pname):
        self.pname=pname
    def playerName(self):
        print(f"player name is {self.pname}")
class Batsman(Player):
    def __init__(self,pname,runs):
        Player.__init__(self,pname)
        self.runs=runs
    def Runs(self):
        print(f"Total runs {self.runs}")
class Bowler(Player):
    def __init__(self,pname,wickets):
        Player.__init__(self,pname)
        self.wickets=wickets
    def Wicket(self):
        print(f"Total wickets are {self.wickets}")
class PlayerInfo(Batsman,Bowler):
    def __init__(self,pname,runs,wickets,country):
        Batsman.__init__(self,pname,runs)
        Bowler.__init__(self,pname,wickets)    
        self.country=country
    def Country(self):
        print(f"Player's country name is {self.country}")
        Player.playerName(self)
        Batsman.Runs(self)
        Bowler.Wicket(self)
p=PlayerInfo("VK",500,1,'India')
# p.playerName()
# p.Runs()
# p.Wicket()
p.Country()
print("--------------------------------------------")

# #ex5
class One:
    def __init__(self,sname,marks):
        self.sname=sname
        self.marks=marks
    def one_info(self):
        print(f"student name {self.sname}")
        print(f"total marks are  {self.marks}")
class Two(One):
    def __init__(self,sname,marks,age):
        One.__init__(self,sname,marks)
        self.age=age
    def age_data(self):
        print(f"student age is {self.age}")
class Three(Two):
    def __init__(self,sname,marks,age,batch_code):
        Two.__init__(self,sname,marks,age)
        self.batch_code=batch_code
    def batch_data(self):
        print(f"student batch code is {self.batch_code}")
class Teacher:
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
    def subject_info(self):
        print(f"first sub is {self.sub1}")
        print(f"second sub is {self.sub2}")
class Four(Three,Teacher):
    def __init__(self,sname,marks,age,batch_code,sub1,sub2,clg_name):
        Three.__init__(self,sname,marks,age,batch_code)
        Teacher.__init__(self,sub1,sub2)
        self.clg_name=clg_name
    def clg_data(self):
        print(f"clg name is {self.clg_name}")
f=Four("tanvii",85,21,12334,"java","sql","py")
f.one_info()
f.age_data()
f.batch_data()
f.subject_info()
f.clg_data()
print("--------------------------------------------")

#ex5     with super()function to avoid constructor overloading and using **kwargs
class One:
    def __init__(self,sname,marks,**kwargs):
        self.sname=sname
        self.marks=marks
        super().__init__(**kwargs)
    def one_info(self):
        print(f"student name {self.sname}")
        print(f"total marks are  {self.marks}")
class Two(One):
    def __init__(self,sname,marks,age,**kwargs):
        super().__init__(sname,marks,**kwargs)
        self.age=age
    def age_data(self):
        print(f"student age is {self.age}")
class Three(Two):
    def __init__(self,sname,marks,age,batch_code,**kwargs):
        super().__init__(sname,marks,age,**kwargs)
        self.batch_code=batch_code
    def batch_data(self):
        print(f"student batch code is {self.batch_code}")
class Teacher:
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
    def subject_info(self):
        print(f"first sub is {self.sub1}")
        print(f"second sub is {self.sub2}")
class Four(Three,Teacher):
    def __init__(self,sname,marks,age,batch_code,sub1,sub2,clg_name,**kwargs):
        super().__init__(sname=sname,marks=marks,age=age,batch_code=batch_code,sub1=sub1,sub2=sub2,**kwargs)
        self.clg_name=clg_name
    def clg_data(self):
        print(f"clg name is {self.clg_name}")
f=Four(sname="tanvii",marks=85,age=21,batch_code=12334,sub1="java",sub2="sql",clg_name="py")
f.one_info()
f.age_data()
f.batch_data()
f.subject_info()
f.clg_data()
print("--------------------------------------------")


class Home:
    def family(self,members):
        self.members=members
        print("welcome home")
        print(f"family memebers are {self.members}")
class Dad(Home):
    def family(self,members,name):    
        super().family(members)
        self.name=name
        print(f"dad's name is {self.name}")
class Son(Dad):
    def family(self,members,name,sname):
        Dad.family(self,members,name)
        self.sname=sname
        print(f"Son name is {self.sname}")
class Mom(Home):
    def family(self, members,mom_n):
        Home.family(self,members)
        self.mom_n=mom_n
        print(f"mom name is {self.mom_n}")
class Daughter:
    def family(self,dname):
        self.dname=dname
        print(f"daughter name is {self.dname}")
class Child(Son,Daughter):
    def family(self,members,name,sname,dname,surname):
        Son.family(self,members,name,sname)
        Daughter.family(self,dname)
        self.surname=surname
        print(f"Surname is {self.surname}")
c=Child()
c.family(4,"laxman","Rohit","divya","choudhari")
m=Mom()
m.family(4,mom_n="meeraa")
print("---------------------------------------")









