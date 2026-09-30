'''
MODULE:
---------

A file consist of python code like variable ,function, object ,class is called as module
Two types of module:
1. Pre defined module-->Inbuilt module
we can't change any module, it is fixed
  ex- os module,csv module,itertools module,datetime module,random,math module

2. User Defined Module
-We are the users and we are creating the module.
syntax:
--------------------------------------
import module_name
module_name.function()

OR

import module_name as Alias_name
module_name.function

OR

from module_name import FunctionName
functionName()

OR

from module_name import *

--------------------------------------

Ex- i have two file:
A.py---->def Spam():
            print("spam function")
    
B.py--->import A        or import A as New
        A.Spam()

If i run B.py the output will be --> spam function

Syntax 2: 
A.py---->def Add(a,b):
            return a+b

B.py---> import A as new
        print(A.Add(2,2))
    
Syntax3:
A.py---->
def Add(a,b):
    return a+b

def Test():
    print("welcome")

B.py---->
from A import Test,Add
print(Add(2,2))
Test()


Syntax4:
A.py---->
def Add(a,b):
    return a+b

def Test():
    print("welcome")

B.py---->
from A import *
print(Add(5,5))
Test()

-------------------------------------

**datetime module
--->import datetime
    print(datetime.datetime.now())

strftime----->will take 1 argument 
and will give the particular operation in date and time.
We have to use % operator

'''
# import datetime
# print(datetime.datetime.now())
# 2026-05-18 09:30:35.746658

import datetime
x=datetime.datetime.now()
y=x.strftime("%Y")
print(y)   #2026   
y1=x.strftime("%y")
print(y1)

y2=x.strftime("%d")
print(y2)   #18  date

y3=x.strftime("%m")
print(y3)     #05  month

y4=x.strftime("%M")
print(y4)   #minute

y5=x.strftime("%H")
print(y4)

y6=x.strftime("%I")
print(y6)   #09 hour

y7=x.strftime("%S")
print(y7)   #22 seconds

'''
%d----->day
%m----->month
%y----->two digit year
%Y----->four digit year
%H----->Hour(24 hours)
%I----->Hour (12 hour)
%M----->Minute
%S----->Seconds
%p----->AM or PM
%A----->Weekday full name
%a----->weekday short name
%B----->Month full name
%b----->month short name
'''

'''
Random module:
-------------

from random as r
print(r.random(num))
'''

import random as r
print(r.random())   #0.10157561535878668
print(r.randint(1,5))  #2  will generate random no. from starting no. to ending no.....
#                           end value will be excluded.....output will be in int format
print(r.randrange(1,20,2))

#choice--->will accept only 
#it will give one one element in the group... what element it will print is not predictable
print(r.choice([10,45,"abc","hi"]))


#shuffle
x=[1,2,3,"a",90,45.8,True,False]
r.shuffle(x)
print(x)
# [1, True, 2, 90, 45.8, 3, False, 'a']

#uniform
print(r.uniform(1,5))
# 1.9947463437962445
#it is same as randint but will be in the form of decimal

'''
Math module:
-----------
'''
import math
print(math.sqrt(4))  #2.0
print(math.isqrt(4))  #2

print(math.cbrt(27))   #3.0

print(pow(3,2)) #9

print(math.factorial(5))  #120

print(math.floor(11.34526))  #11

print(math.ceil(12.5))    #13   round off to the next no.
print(math.ceil(19.1))   #20

print(math.fabs(-90.8765))  #90.8765   convert negative to positive

print(math.fsum([1,3,5,7]))   #16.0
print(math.pi)    #3.141592653589793

