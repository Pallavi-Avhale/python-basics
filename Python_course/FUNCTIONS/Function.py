

'''FUNCTION:
-----------------
-Function is a set of statements or block of code which are capable to perform some operations 
OR
-It is a name given to memory block where all the  instructions are stored which are capable to 
perform the operations.

TYPES OF FUNCTIONS:
1. USER DEFINED FUNC.
-are the functions which are defined/created by the user based upon the client requirement.
-HOW TO CREATE A USER DEFINED FUNC.----->using the 'def' keyword
----------------------------------------------------------
            {keyword}  {name of func.}  {any var}
Syntax--->  def  function_name(parameters):   #function declaration
                statement
                statement   {block of code}
                .
                .
                .
                return data <--------  {any value}{return-keyword}
            function_name(arguments) <------- #function calling
                           {value}
-----------------------------------------------------------

{if we print only---->function_name without paranthesis in function calling we will
 get the object address of function}

#NOTE===>
-Function will never get executed without calling.
-The no. of time we call the function that no. of time function will execute

2. PRE DEFINED FUNC./INBUILT FUNC. 
-are the functions which are already defined/created at the time of creating the software.
-ex-eval(),print(),len(),type(),isinstance(),etc.
-It is possible to access its functionality but 
we cannot modify their functionality.




'''

#USER DEFINED
#example1:
# {function without arguments and parameters}
def add():
    a=10
    b=20
    print(a+b)
add()

'''
# {Functions with arguments and parameters}
def sum(a,b):  #a,b parameters
    print(a+b)
sum(40,10)
sum(30,30)     #30,30 aruguments

NOTE: -Parameters are defined in func declaration and 
        #  arguments are defined in the func calling
     -no. of parameters should be equal to no. of arguments

#if no. of parameters != no. of arguments
def addition(a,b,c):
    print(a+b)
addition(10,80)
# TypeError: addition() missing 1 required positional argument: 'c'
'''

#2. wap to check string is palindrome or not by using user defined func
# def palindrome():
#     # name='madam'
#     name=eval(input('enter a string'))
#     if name==name[::-1]:
#         print('palindrome')
#     else:
#         print('not palindrome')
# palindrome()
# palindrome()

#here is the drawback, the control stopped when we take input from 
# the user even when the function is already called so to resolve this issue:
# name=eval(input('enter a name to check palindrome string:'))
# def palindrome(name):
#     if name==name[::-1]:
#         print('palindrome')
#     else:
#         print('not palindrome')
# palindrome(name)

#NOTE: in a func. if we don't use return keyword it will return None value
def addition(a,b,c):
    print(a+b)
addition(10,20,30) 
# addition(10,20)
print("----------")

'''RETURN KEYWORD'''
def printing():
    a=25
    print(a)
printing()
# print(a)  #NameError: name 'a' is not defined
#here we cannot access the a value due to a var is declared inside the function
# so we access this with return keyword
'''
-return keyword is the keyword which is used to access the value from inside of the 
function to outside the function 
-if func is returning the value then the value is return to that line who called that func.

-we can access the returned value by using two ways:
1. BY PRINTING THE FUNCTION CALLING STATEMENT
---> 
ex-- def printing():
        a=25
        print(a)
        return a
    print(printing())

2. BY STORING THE RETURNED VALUE IN NEW VARIABLE
ex-
def printing():
    a=25
    print(a)
    return a
res=printing()
print(res)

-by using return keyword we can return single or multiple values
-if we return single value then output will be in the same format 
but, if we return multiple values then output will be in the form of tuple
def printing():
    b=30
    a=20
    print(a)
    return a,b
res=printing()
print(res)
'''
print()

def printing():
    a=25
    print(a)
    return a
res=printing()
print(res)
# 25
# 25

print()

#printing multiple values--->o/p will be in the form of tuples
def printing():
    b=30
    a=20
    print(a)
    return a,b
res=printing()
print(res)
# 20
# (20, 30)

#note- after the return keyword any statemnet is written before the function calling 
# that statements are never executed(hidden)

#wap to take 1 iterable from the user if the len of the iterable is even
# then return last character/element but if len is odd then return 1st characters
# st=eval(input('enter an iterable'))
# def iterables(s):
#     for i in s:
#         if len(s)%2==0:
#             return s[-1]
#         else:
#             return s[0]
# print(iterables(st))

'''
TYPES OF ARGUMENTS
-------------------
Based upon arguments there are different ways to call the function
1. Normal func. with arguments
2. Positional only argument(indicated with '/')
3. Keyword only argument
4. Combination of Positional only and keyword only arguments
5. Variable positional argument
6. Variable Keyword only arguments
7. Combination of variable positional only argument and variable keywrod only arguments


'''

'''2. Positional only argument(indicated with '/')
-mention at the end of the parameters
-it will accept only positional arguments
'''
#ex-
def calculate(a,b,/):
    return a+b
print(calculate(20,30))

# positional only arguement follow the keyword argument
# def calculating(a,b,/):
#     return a+b
# print(calculating(a=10,19.5))
# SyntaxError: positional argument follows keyword argument

# def calculating(a,b,/):
#     return a+b
# print(calculating(10,b=19.5))
# TypeError: calculating() got some positional-only arguments
#  passed as keyword arguments: 'b'


'''3. Keyword only argument(*)'''
#ex1
def cal(*,a,b):
    return a,b
print(cal(a=10,b=40))

#ex2
def cal(*,a,b):
    return a+b
print(cal(b=10,a=40))

# def add(*,a,b,c,/):
#     return a+b,c
# print(a=10,b=20,30)
# SyntaxError: / must be ahead of *

#ex
# def Fun(*,x,y):
#     return x*y
# print(Fun(3,3))
# TypeError: Fun() takes 0 positional arguments but 2 were given

'''4. Combination of Positional only and keyword only arguments'''
# ex1
def calc(a,b,/,*,c):    #2positional and 1keyword
    return a+b,c
print(calc(10,20,c=60))   

# # ex2
# def calc(a,b,/,*,c):    #2positional and 1keyword
#     return a+b,c
# print(calc(c=60,10,20)) 
# SyntaxError: positional argument follows keyword argument
print("---------------------")

#positional
def Spam(a,b):
    return a/b
print(Spam(50,50))
print(Spam(b=20,a=10))
print()
# 1.0
# 0.5

#positional only
def Test(a,b,/):
    return a*b
print(Test(1,3))  #3
# print(Test(a=8,b=2))  #TypeError
print()

#keyword
def Demo(x,y):
    return x+y
print(Demo(x=2,y=2))
print(Demo(20,70))
# 4
# 90
print()

#keyword only
def Test1(*,p,q):
    return p*q
# print(Test1(4,4))  #TypeError
print(Test1(p=4,q=4))   #16
# print(Test1(p=9,6))    #SyntaxError: positional 
                      #argument follows keyword argument

#default argument
def Spam(name="Priya"):
    return (name)
print(Spam())
# print(name)   #NameError

print(Spam("Avni"))
# Priya
# Avni

print(Spam(name="riyaa"))
# riyaa

print()

#variable length positional arg.
def Total(*args):
    return (args)
print(Total(10,20,30,40,50))   #(10, 20, 30, 40, 50)
print(Total("hii","Hello","Heyyy"))   #('hii', 'Hello', 'Heyyy')
print(*Total("hii","Hello","Heyyy"))   
# hii Hello Heyyy

#variable length keyword argument
def Details(**kwargs):
    return kwargs
print(Details(a=90,b=80))  #{'a': 90, 'b': 80}


#combination of positional only and keyword only
def Combn(a,b,/,*,c,d):
    return f"Addition={a+b} and multiplication is {c*d}"
print(Combn(10,20,c=30,d=40))
# print(Combn(c=30,d=40,10,20))   #SyntaxError: positional 
                                #argument follows keyword argument


#ex
def Testing(*args):
    return args
# print(Testing(a=98877))  #TypeError

#local variable
def Var(a,b):
    c=100   #local var
    return a,b,c
print(Var(22,33))
# print(c)   #NameError
res=Var(22,23)
print(res)   #(22, 23, 100)

#global
a=10
def Global_var():
    global a
    a=200
    return a   #200
print(Global_var())
print(a)   #200

#non local
def Non_local():
    d=88
    return d
print(Non_local())   #80
# print(d)   #NameError

def Func(a):
    print(a)
print(Func(150))
# 150
# None

# print({[i]:i**2 for i in range(1,5) if i%2==0})
# TypeError: unhashable type: 'list'