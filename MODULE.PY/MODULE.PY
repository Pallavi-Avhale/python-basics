# Module---
# define---- A file consist of python code like variable,function,object
# -----> types---->
# ----> 1. Predefined Module
# -----> 2. Userdefined Module
# ----> 1. Predefined Module(inbuild module---- learn in file handling) ---- 
# 1. OS Module 
# 2. CSV Module 
# 3. itertool Module 
# 4. datetime Module
# 5. random Module
# 6. math Module

# -----> 2. User defined Module ----> 

# two files are created
# 1. A.py
# def Spam():
# print("Spam")

# 2.  B.py----- file 2nd we call A file function in B file by import module name 
# import A 
# A.Spam()

# example---->

# evening.PY file 
# def add(a,b):
#     return a+b

# access in file B.PY

# import evening 
# print(A.add(3,4))

# -----unique  file ( import evening as P)

# import module ----> 1st way

# import module name as alias name (import evening as P ) ---->  (using alias name) 2nd way

# from Module import operations (function name,varname(we need to print coz it working as a normal way)) ----> 3rd way

# from module name import * (* means eveything included) ----> 4th way

# ---------------------> # 4. datetime Module-----------------------

# 4. datetime Module

# import datetime
# print(datetime.datetime.now())                     #(modulename.modulename.now())    now used to show functions current time of system

# ---o/p---> 2026-05-18 09:31:30.825217


# for fecting all the things at a Time 

# import datetime
# x=datetime.datetime.now()
# y=x.strftime("%Y")               #uppercase for whole year like 2026
# print(y)                  #---->  o/p---> 2026

# import datetime

# x=datetime.datetime.now()
# y=x.strftime("%y")               #lowercase for  year 26 
# print(y)                          #---o/p--> 26


import datetime

# x=datetime.datetime.now()
# y=x.strftime("%d")               #lowercase for  date 18
# print(y)                         #---o/p---> 18

# import datetime

# x=datetime.datetime.now()
# y=x.strftime("%D")               #uppercase for  whole date 05/18/26
# print(y)                           #---o/p--> 05/18/26


# import datetime

# x=datetime.datetime.now()
# # y=x.strftime("%M")               #uppercase for  whole date 05/18/26
# # print(y)

# y1=x.strftime("%Y")
# print(y1)                           #2026

# y2=x.strftime("%y")
# print(y2)                           #26

# y3=x.strftime("%h")
# print(y3)                           #May

# y4=x.strftime("%H")
# print(y4)                            #09







# %M----minute
# %s----> seconds
# %p---- AM/PM 
# %A---> weekday full name---like monday
# %a----> weekday short namev (mod)
# %B----> Month full Name
# %b----> Month short name 


# Random Module--------------->

# ramdon won't accept any argument

# import random
# print(random.random())            #0.26609040671486683

# ------------------


# randint accept 2 arguments---
# import random as r
# print(r.randint(2,8))                    #randome numbers in between 2 to 8---- it will show any number if we refresh


# -----randrang-----

import random as r
# print(r.randrange(1,10))

# print(r.choice([10,45,"abc",95.45]))               #choice----- in the container it will through 1 1 element

# x=[1,2,3,4,5,"a","k",90,45.1,True,False]          

# r.shuffle(x)                                     #change the order of the element 
# print(x)


# print(r.uniform(1,5))                           #4.886684222396498 give  o/p in decimal---- it include 1 to 5 
#what is difference bet uniform and random
# randrange and randint




# ---------------------------- MATH MODULE------------------------->

import math
# print(math.sqrt(4))                     #2.0

# for pure integer output 

# print(math.isqrt(4))                      #2

# print(math.cbrt(27))                        #3.0

# print(math.factorial(6))                      #720

# print(math.floor(11.33333))                       #11

# print(math.ceil(1.7))                                #2           round up no to next number like 1.1,1.2 (won't roundup if 1.0)

# print(math.fabs(-90.9999))                               #90.9999

# print(math.fsum([1,2,3,4]))                               #10.0

# print(math.pi())