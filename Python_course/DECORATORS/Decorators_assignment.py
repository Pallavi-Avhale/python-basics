# 1 WADF TO CHECK IF THE 1ST ARGUMENT IS LESSER THAN 2ND ARGUMENT
#  IF THEN SWAP THEM AND PERFORM DIVISION BUT THE CONDITION IS YOU
#  SHOULD NOT MODIFY THE ORIGINAL FUNC


def outer(func):   #func= div   1
    def inner(a,b):    #a---> 2 , b ----> 4           3
        if a<b:       #2<4     (True)
            a,b=b,a      #2,4=4,2

        return func(a,b)   #a=4,b=2    #func()

    return inner

@outer            #2

def div(a,b):     #a,b ----> parameters     #a=4,b=2
    print(a/b)      #4/2----> 2.0
div(2,4)    #2,4 ----> arguments
print("---------------------------------")

#2. WADF TO ADD 2 NUMBERS AND DISPLAY THE MESSAGE
# BEFORE AND AFTER PERFORMING THE ADDITION

def addition(func):   #func==add            #1
    def inner(*args):                       #3
        print("im performing addition")     #6
        func(*args)                         #7
        print("addition is done")           #10
    return inner                          #4 variables only
@addition                         #2
def add(*args):
    c=sum(args)#8
    print(c)       #9
add(1,2,3,4,5,3,4,6,8)                   #5 variable value

# output--->
# im performing addition
# 36
# addition is done
print("-----------------------")

#3. CREATE A DECORATOR TO RETURN ONLY POSITIVE OUT FROM ANY SUBTRACTION

def outer(func):                        #1
    def inner(*args,**kwargs):          #3
        res = func(*args,**kwargs)    #res = -22   #6
        return (abs(res))                #8
    return inner                          #4 variables only
@outer                                  #2
def sub(a,b):
    return a-b                              #7
print(sub(-20,2))                         #5 values

#output---------->22
print("--------------------------")

#4. WAP TO CREATE A DECORATOR FUNCTION THAT MEASURES
# THE EXECUTION TIME OF THE FUNCTION AND PRINT IT

import time 
def outer(func):                      #1
    def inner():                      #3
        start= time.time()   #current laptop time  #6
        func()               #func is called       #7
        end = time.time()    #again it will take the laptop time
        execution_time = end-start  #10
        print(f"{func.__name__} took {execution_time} seconds")  #11
    return inner                         #4 variables

@outer                                    #2
def display():
    time.sleep(3)            #8
    for i in range(1,10):    #9
        ...
display()                                #5 values

# output---->display took 3.0010857582092285 seconds
print('----------------------------')


#5. WRITE A DECORATIVE FUNCTION TO PRINT THE TYPE OF DATA TYPE BEFORE
# PERFORMING THE ACTION

def outer(func):           #1
    def inner(*args,**kwargs):  #3
        for i in args:        #6
            print(type(i))           #7
        func(*args,**kwargs)       #8
    return inner                 #4 variables
@outer                        #2
def display(*args):
    print(sum(args))         #9
display(2,3)                     #5 values

# output-----------><class 'int'>
# <class 'int'>
# 5
print('--------------------------')


#6. WAP TO SUM THE POSITIONAL ARGUMENTS AND GET THE LENGTH OF THE KEYWORD ARGUMENTS


def pos_key_modify(func):                 #1
    def wrapper(*args,**kwargs):         #3
        print(f"the total sum of args are : {sum(args)}")#6
        func(*args,**kwargs)         #7
    return wrapper                    #4 variables
@pos_key_modify                        #2
def pos_key(*args,**kwargs):
    print(f"the length of keyword arguments are : {len(kwargs)}")    #8
pos_key(2,4,5,a=1,b=2,c=3)     #5 values

# output---------->
# the total sum of args are : 11
# the length of keyword arguments are : 3
print('--------------------')

#7. WADF TO DO ARITHMETIC OPERATIONS ON THE GIVEN NUMBER AND THE CONDITION IS  A>B THEN PERFORM MULTIPLICATION IN DECORATOR FUNCTION  ELSE CUBE IT IN DECORATOR

def outer(func):      #1
    def inner(a,b):   #3
        if a>b:       #6    True then
            print(f"performing multiplication {a*b}")   #7
        else:    #if a>b false then  
            print(f"performing cubing of the number {a**3}, {b**3}")  #7
        func(a,b)  #8
    return inner      #4

@outer                               #2
def arth(a,b):    #a=5 , b=3    if a>b
    print(f"performing addition {a+b}")   #--->5+3=8    #9
    print(f"performing subtraction {a-b}")   #2
arth(5,3)           #5

# output
# performing multiplication 15
# performing addition 8
# performing subtraction 2
print("--------------------")

'''
DELAY DECORATORS:
'''
#1. WARD TO CHECK HOW MUCH TIME IT IS TAKING TO PERFORM EACH TASK
#I WILL BE PERFORM TWO TASK
#2 MAIN FUNCTIONS ----> DECORATED BY STANDARD DECORATOR

import time
def outer(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(2)
        func(*args,**kwargs)
        end=time.time()
        print(end-start)
    return inner
@outer
def add(a,b):
    print(f"addition of a and b is {a+b}")
add(2,4)

@outer
def sub(a,b):
    print(f"subtraction of a and b is {a-b}")
sub(5,4)

# output--->
# addition of a and b is 6
# 2.001573085784912
# subtraction of a and b is 1
# 2.0005407333374023
print("----------------------------")
'''
#2. WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME
# , DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS ,
# DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER

import time
def outer(func):
    def inner(*args,**kwargs):
        time.sleep(3)
        func(*args,**kwargs)
    return inner

@outer
def name():
    n=input("enter employee name :")
    print(n)
name()

@outer
def email():
    e=input("enter email: ")
    print(e)
email()

@outer
def phone():
    p=int(input("enter a phone no. "))
    print(p)
phone()

# enter employee name :divya
# divya
# enter email: d@gmail.com
# d@gmail.com
# enter a phone no. 98765432345
# 98765432345'''
print("------------------------")


#3. WAP TO CREATE A DECORATOR TO WHICH PRINTS
# THE NAME OF THE CALLED FUNCTION ALONG WITH IT SHOULD
# CHECK IF THE NUMBER IS EVEN OR ODD


def outer(func):                #1
    def inner(*args,**kwargs):   #3
        print(f"the function is {func.__name__}")  #6
        res= func(*args,**kwargs)   #7
        return res    #10
    return inner               #4 var
@outer                          #2
def display(num):
    if num%2==0:  #8 if true
        return "num is even" #9
    else:   #if false
        return "num is odd" #9
print(display(3))              #5 value

# the function is display
# num is odd
print("-------------------------")

#4.wadf to count number of arguments passed to a function

def outer(func):
    def inner(*args):
        print(f"number of arguments passed to function is {len(args)}")
        func(*args)
    return inner
@outer

def add(a,b,c,d,e):
    print(a+b+c+d+e)
add(1,2,3,4,5)

# output------->
# number of arguments passed to function is 5
# 15
print("------------------------------")
'''
# 5..wadf to input 5 seconds before executing function?
import time
def delay(func):
    def inner(*args):
        time.sleep(3)
        func(*args)
    return inner
@delay

def even():
    for i in range(1,11):
        time.sleep(2)
        print(i)
even()
'''