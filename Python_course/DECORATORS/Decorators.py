'''
DECORATORS:
------------
-adding the functinality without changing/touching the main function, we can do the modification
-also called it as a MetaProgramming:we can take one part of the program 
                                     try to do the modification in another part of the program, 
                                     without changing main function
            
Use cases: -Login logout
           -Username and password

-----------------------------------------------------------------------------------------------------------------
#Decorator function(syntax)

def Outer(func):                  #NOTE decorator outer function will accept one argument-->func......func is pointing to main function
    def inner(*args,**kwargs):
        statement
        func(*args,**kwargs)
    return inner

@Outer                      #To connect both decorator and main function

#Main function
def MainFunction(Parameters):
    statement
    statement
    .
    .
MainFunction(Arguments)
-------------------------------------------------------------------------------------------------------
IMP POINTS:
-#NOTE decorator outer function will accept one argument-->func......
func is pointing to main function
-If we write Main function name instead of func then also it will be working
-------->func==MainFunction

#NOTE Decorator function have nested function it will accept variable & positional argument,
but it will be optional.
Three ways:
1. *args,**kwargs---->optional
2. Mainfunction parameters---->use same parameters
3. Mainfunction no parameters--->then too we can use *args **kwargs

#NOTE while writting decorator...always write main function and then decorator function
But while exceution... first decorator will execute and then Main Function



'''

#ex1 
def Outer(func):                                              #1
    def inner(a,b):                                           #3
        print("Addition Operation")                           #6
        func(a,b)                                             #7                                       
    return inner    #write function name without parameters   #4

@Outer      #internally Outer(func)--->Outer(Add)             #2

def Add(a,b):
    print(a+b)                                                #8
Add(4,5)                                                      #5
print()
#Output---->
# Addition Operation
# 9

'''
First Class program:
-function only we call it as a first class program.
-Because in function we have parameters,
'''

#ex2 
# output should be:
# Welcome to all 
# Good morning Guyss
def Outer(func):
    def inner():
        print("Welcome to all")
        func()
    return inner
@Outer

def MainFunction():
    print("Good Morning Guysss")
MainFunction()
print()
# Welcome to all
# Good Morning Guysss
print("-------------------------")

#ex3 Single Decorator + Multiple Main functions

#  ***  "delay decorator" ***
#i want to take 5 sec then display welcome to all then take 3sec and then display good morning guyss
# import time
# def Outer(func):
#     def inner():
#         time.sleep(5)
#         print("Welcome to all")
#         time.sleep(3)
#         func()
#     return inner

# @Outer

# def MainFunction():    #main function1
#     print("Good Morning Guysss")
# MainFunction()
# print()

# @Outer
# def Demo():    #main function2
#     print("Display class")
# Demo()

# Welcome to all
# Good Morning Guysss   --->first main function

# Welcome to all
# Display class    ------>second main function
print("----------------------------")

#ex4
#Here i want to print the Mainfunction name before executing main function
def Outer(func):
    def inner():
        print("Welcome to all")
        print(func.__name__)
        func()
    return inner
@Outer

def MainFunction():    #main function1
    print("Good Morning Guysss")
MainFunction()
print()

@Outer
def Demo():    #main function2
    print("Display class")
Demo()


# Welcome to all
# MainFunction
# Good Morning Guysss

# Welcome to all
# Demo
# Display class

print("-------------------------------")

#ex5
# import time
def outer(func):
    def inner(a,b):
        print(func.__name__)
        # time.sleep(3)
        print("Multiplication operation on going")
        # time.sleep(3)
        func(a,b)
        print("Multiplication done")
    return inner
@outer

def Mul(a,b):
    print(a*b)
Mul(7,3)

# Mul
# Multiplication operation on going
# 21
# Multiplication done
print("------------------------------------")

#Single decorator + Multiple main function

def Outer(func):
    def inner(*args):
        print(func.__name__)
        func(*args)
    return inner
@Outer

def Spam():
    print("spam 1")

@Outer
def Demo():
    print("demo 1")

@Outer
def Test(a,b):
    print("test 1",a+b)

@Outer
def Show(x,y):
    print("Show 1",x*y)

Spam()
Demo()
Test(10,20)
Show(5,5)

# Spam
# spam 1
# Demo
# demo 1
# Test
# test 1 30
# Show
# Show 1 25
print("-----------------------------------------")

#NOTE: DRAWBACK-----> we cannot give separate statements for any one particular main function...
# i.e. we have to give same statement to all the main function in the decorator 
#To avoid this we go for   Parameterized Decorator
#--------------------------------------------------------------------------------------

# *** Multiple Decorator with Single Main Function.***
def Outer(func):
    def inner(*args):
        print("welcome")
        func(*args)
    return inner

def Outer1(func):
    def inner1(*args):
        print("To all")
        func(*args)
    return inner1
@Outer                     #NOTE first which decorator we are connecting that decorator will be executing
@Outer1
def Student(name,sub):
    print("student name is :",name)
    print("subject is :",sub)
Student("Riya","m1")

# welcome
# To all
# student name is : Riya
# subject is : m1
print("----------------------------------")


'''
***wap to check execution calculation of the program(how much time i am taking to execute the program)
 ****time.time method*****
-------->it will be showing the current time of the system
 '''

#ex1
import time
def Outer(func):
    def inner(*args):
        start=time.time()
        func(*args)
        time.sleep(2)
        end=time.time()
        print(end-start)
    return inner
@Outer

def Student(name,sub):
    print("student name is :",name)
    print("subject is :",sub)
Student("Priyaaa","m1")

# student name is : Priyaaa
# subject is : m1
# 2.0009663105010986
print("------------------------------")

# import datetime
# print(datetime.datetime.date.now())

'''
PARAMETERIZED DECORATOR:
-------------------------
-Here for each main function we can give different different statements.

Syntax:
-------------------------------------
def outer_most(parameter):
    def outer(func):
        def inner(*args,**kwargs):
            statement
            func(*args,**kwargs)
        return inner
    return outer

@outer_most(parameter)

def MainFunction(p):
    statement
MainFunction(arguments)
--------------------------------------

NOTE while connecting only we need to pass the statement(parameter)

    
'''

#ex1
def Outer_most(n):
    def Outer(func):
        def inner(*args):
            print(n)
            #time.sleep(n)
            func(*args)
        return inner
    return Outer

@Outer_most("Addition operation")
def Add(a,b):
    print(a+b)

@Outer_most("Sub--->operation")
def Sub(a,b):
    print(a-b)

@Outer_most("Mul--->operation")
def Mul(a,b):
    print(a*b)

@Outer_most("Div--->operation")
def Div(a,b):
    print(a/b)

Add(10,20)
Sub(10,5)
Mul(5,5)
Div(20,5)

# Addition operation
# 30
# Sub--->operation
# 5
# Mul--->operation
# 25
# Div--->operation
# 4.0
print("-----------------------------------")

