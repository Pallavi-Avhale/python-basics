'''
GENERATOR:
----------

-Generator is a type of function it will generate the sequence of element one by one
instead of all once
-In generator we are using yield keyword

-Why generator means here we can save the memory
-Genarator is also called as "LAZY ITERABLE"

-In generator to print one by one element we can take the help of next() function and it will accept 
one argument 
syntax--->next(object)

Syntax: def Generator_Function_name(Parameter):
            yield statement1
            yield statement2
        new_varname= Generator_function_name(argument)
        print(new_varname)--->Generator object address

here, def is keyword
      Generator_Function_name is name of program
      parameter is the variable name.....it is optional
      yield is keyword
      new_varname is generator object
      argument is variable value
      Generator object address--->to avoid object address two ways:
                                    1.Typecasting
                                    2.Looping
'''
#ex1
def Morning():
    return 'A'
    return 'B'
num=Morning()
print(num)
print('-----------------------')
#o/p-->A

def Morning(a):
    yield 'A'
    yield 'B'
num=Morning(10)
print(num)   #<generator object Morning at 0x0000017E04F34A90>
print('---------------------------------')

#how much memory function is consuming
# import sys
# def Check(n):
#     k=[]
#     for i in range(1000):

'''
**how to check how much memory is used by the program
syntax: import sys
        sys.getsizeof(object)

'''

import sys
def Gen_fun(n):
    for i in range(n):
        yield i
new=Gen_fun(1000)
print(new) #<generator object Gen_fun at 0x0000019DE1FCF6B0> to avoid object address use next()
print(next(new))   #it will give the output one by one...0
print(next(new))   #1
print(next(new))   #2
print()
print(sys.getsizeof(new))  #200
print('-----------------------')

def demo():
    for i in range(10):
        yield i
e=demo()
#to avoid object address use looping
for i in e:
    print(i)
print('------------------')

def Check():
    k=[]
    for i in range(5):
        k.append(i)
    yield k
t=Check()
for i in t:
    print(i)
print('-------------------')
#[0, 1, 2, 3, 4]

'''
**RETURN KEYWORD:
return used in function
we can't use multiple times return keyword
it will terminate the code

**YIELD KEYWORD:
yield used in generator
we can use multiple times yield keyword
it will pause the execution/ hold the code execution
'''
#using function
def Data(a,b):
    x=a+b
    y=a*b
    z=a/b
    return x #only this will execute
    return y
    return z
e=Data(10,20)
print(e)
print('-------------------')
#30

#to get all addition,multiplication,division.....then use single line return
def Data(a,b):
    x=a+b
    y=a*b
    z=a/b
    return x ,y,z
e=Data(10,20)
print(e)
print('-------------------')
#(30, 200, 0.5)

#using generator
def Data(a,b):
    x=a+b
    y=a*b
    z=a/b
    yield x
    yield y
    yield z
e=Data(10,20)
print(next(e))
print(next(e))
print(next(e))
# print(next(e)) #StopIteration error
print('-------------------')
# 30
# 200
# 0.5

'''
There are three ways toe avoid the object address in the generator
1.using next() function
2.Looping
3. Type casting

But if we use loop and typecasting then we will get the output all at a time
If we use next() then we will get one by one output
'''

#ex
x=[10,True,"hi",{1,2,3},[1,2,3],90.45,2+4j]
def Data(x):
    for i in x:
        if isinstance(i,(str,list,tuple,dict,set)):
            print(i)
Data([10,True,"hi",{1,2,3},[1,2,3],90.45,2+4j])
print('---------------------------')

x=[10,True,"hi",{1,2,3},[1,2,3],90.45,2+4j]
def Data(x):
    for i in x:
        if isinstance(i,(str,list,tuple,dict,set)):
            yield i 
s=Data([10,True,"hi",{1,2,3},[1,2,3],90.45,2+4j])
print(next(s))
print(next(s))
print(next(s))
print('--------------------------')

#ex2
# s=[1,2,3,4,5,6,7]
# def Square(s):
#     k=[]
#     for i in s:
#         if i%2==0:
#             k.append(i**2)
#         return k
# s=Square([1,2,3,4,5,6,7])
# print(s)

# s=[1,2,3,4,5,6,7]
# def Square(s):
#     k=[]
#     for i in s:
#         if i%2==0:
#             k.append(i**2)
#         yield k
# s=Square([1,2,3,4,5,6,7])
# print(next(s))

#ex4 in list even len word-as it is...odd len word----reverse
e=["welcome","spam","demo","sql","pen","men","hi"]
def Spam(e):
    k=[]
    for i in e:
        if len(i)%2==1:
            k.append(i[::-1])
        else:
            k.append(i)
    return k
s=Spam(["welcome","spam","demo","sql","pen","men","hi"])
print(s)
print('----------------')


#using generator
e=["welcome","spam","demo","sql","pen","men","hi"]
def Spam(e):
    k=[]
    for i in e:
        if len(i)%2==1:
            k.append(i[::-1])
        else:
            k.append(i)
    yield k
s=Spam(["welcome","spam","demo","sql","pen","men","hi"])
print(next(s))
print('----------------')
# ['emoclew', 'spam', 'demo', 'lqs', 'nep', 'nem', 'hi']

#wap to print 1 to 10 elements inside the list
#looping
for i in range(1,5):
    print(i,end=" ")
print()


#comprehension
print([i for i in range(1,5) ])
print(i for i in range(1,5) )#<generator object <genexpr> at 0x000001D53DE24A00>

'''
wap to generate a+b,a-b,a*b,a/b by taking a and b from user

wap to generate only values which are divisible by 5

l=[34,55,60,56,78,90,25,40]


wap to return a iterator which is having square root of values present in the list

l=[25,36,49,81,9,16]


wap to return a iterator having tuples of word and its len pair and typecast into dictionary

l=["instagram","facebook","whatsapp","meta","oracle"]


wap to generate only numeric values in given list

l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]


wap to generate a list if it is individual data type reverse it else return as it is

l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]


wap to generate only the string with odd length in given list

l=["alexa","siri","google","cortrena"]


wap to create a list of numbers if number are even square it else cube it
l=[2,3,4,5,6,7]


wap to return a list if words is of even length reverse it

l=["hello","world","python","apple","google","walmart"]


wap to generate the first letter of the word as key and words starting with letter as value
s="python is a programming language and programming is part of life"

output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]
'''
print("assignmentj")
#1.wap to generate a+b,a-b,a*b,a/b by taking a and b from user
def Spam(a,b):
    a=int(input("enter a no. a:"))
    b=int(input("enter a no. b:"))
    yield a+b
    yield a-b
    yield a*b
    yield a/b
res=Spam(11,11)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))  #StopIteration
# Spam(11,12)
    

# wap to generate only values which are divisible by 5
l=[34,55,60,56,78,90,25,40]
def Val(l):
    for i in l:
        if i%5==0:
            yield i
v=Val([34,55,60,56,78,90,25,40])
print(list(v))

#3. wap to return a iterator which is having square root 
# of values present in the list
l=[25,36,49,81,9,16]
def SquareRoot(l):
    for i in l:
        yield i**0.5
s=SquareRoot([25,36,49,81,9,16])
print(list(s))
# [5.0, 6.0, 7.0, 9.0, 3.0, 4.0]


#4 wap to return a iterator having tuples of word and
#  its len pair and typecast into dictionary
l=["instagram","facebook","whatsapp","meta","oracle"]
def Func(l):
    for i in l:
        yield (i,len(i))
f=Func(["instagram","facebook","whatsapp","meta","oracle"])
print(dict(f))
# {'instagram': 9, 'facebook': 8, 'whatsapp': 8, 'meta': 4, 'oracle': 6}


#5. wap to generate only numeric values in given list
l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
def Num(l):
    for i in l:
        if isinstance(i,(int,float,complex)):
            yield i
n=Num(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])
print(list(n))
# [78, 78, 9.87, 45.36]

# 6.wap to generate only the string with odd length in given list

l=["alexa","siri","google","cortrena"]
def Spam(l):
    for i in l:
        if len(i)%2==1:
            yield i
s=Spam(["alexa","siri","google","cortrena"])
print(list(s))
# ['alexa']

# wap to create a list of numbers if number are even square it else cube it
# l=[2,3,4,5,6,7]

# wap to generate the first letter of the word as key and words starting with letter as value
s="python is a programming language and programming is part of life"


# output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]