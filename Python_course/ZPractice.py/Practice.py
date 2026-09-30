
# Python-->
# Introducton
# Data Types
# Operators
# Type casting
# Control flow statement 
#   1. conditional flow control
#   2. loop flow control
# Transfer staements
#     1.Break 
#     2. continue
#     3. pass
# pattern problems
# comprehension
#     1.list
#         A)nested list
#     2.set 
#         B)nested set
#     3.dictionary
#         c)nested dictionary
# function
#     Pre-defined
#     User-define
# 7 types of arguments
#     1.Positional arguments
#     2. Keyword Argumnets
#     3. Variable posional arg (*args)
#     4. Variable keyword arg  (**kwargs)
#     5.combination of variable positional arg (*args) and variable keyword (**kwargs)
#     6.only positional
#     7.only keyword
#     8.combination of only positional (/) and only keyword (*)
# Local variable
# global variable
# Recursion
# oops
# Generator
# filter map
# file handling
# Regular expression
# Decorators

# result_type
# type
# dtype
# shape
# size
# nbyte
# flatten
# flatten(order="C")
# flatten(Order="F")
# tile
# ndim
# repeat
# reshape(r,c)
# reshape(-1)
# itemsize
# T
#copy
#view



# Bool-->Int-->Float-->Complex-->str

# import numpy as np
# a=np.array(10)    
# print(a)           #single array/ zero dimensional array
# print()
# print(a.ndim)

# | Property / Method    | Meaning                                      | Syntax                 | Example                         | Output                      |
# | -------------------- | -------------------------------------------- | ---------------------- | ------------------------------- | --------------------------- |
# | `type()`             | Checks object type                           | `type(x)`              | `type(x)`                       | `<class 'numpy.ndarray'>`   |
# | `dtype`              | Data type of array elements                  | `x.dtype`              | `x.dtype`                       | `int64`                     |
# | `shape`              | Shows rows & columns                         | `x.shape`              | `x.shape`                       | `(2,3)`                     |
# | `ndim`               | Number of dimensions                         | `x.ndim`               | `x.ndim`                        | `2`                         |
# | `size`               | Total elements                               | `x.size`               | `x.size`                        | `6`                         |
# | `itemsize`           | Memory per element (bytes)                   | `x.itemsize`           | `x.itemsize`                    | `8`                         |
# | `nbytes`             | Total memory used                            | `x.nbytes`             | `x.nbytes`                      | `48`                        |
# | `T`                  | Transpose (rows ↔ columns)                   | `x.T`                  | `x.T`                           | `[[10 40],[20 50],[30 60]]` |
# | `reshape(r,c)`       | Change shape                                 | `x.reshape(3,2)`       | `x.reshape(3,2)`                | New shape `(3,2)`           |
# | `reshape(-1)`        | Convert to 1D array                          | `x.reshape(-1)`        | `x.reshape(-1)`                 | `[10 20 30 40 50 60]`       |
# | `flatten()`          | Convert multidimensional array into 1D       | `x.flatten()`          | `x.flatten()`                   | `[10 20 30 40 50 60]`       |
# | `flatten(order="C")` | Row-wise flattening                          | `x.flatten(order="C")` | `x.flatten(order="C")`          | `[10 20 30 40 50 60]`       |
# | `flatten(order="F")` | Column-wise flattening                       | `x.flatten(order="F")` | `x.flatten(order="F")`          | `[10 40 20 50 30 60]`       |
# | `repeat()`           | Repeat each element                          | `np.repeat(x,n)`       | `np.repeat([1,2],3)`            | `[1 1 1 2 2 2]`             |
# | `tile()`             | Repeat whole array                           | `np.tile(x,n)`         | `np.tile([1,2],3)`              | `[1 2 1 2 1 2]`             |
# | `result_type()`      | Predict final datatype after combining types | `np.result_type()`     | `np.result_type("int","float")` | `float64`                   |


# Difference Between reshape(-1) and flatten() in NumPy
# | Feature                        | `reshape(-1)`                        | `flatten()`                          |
# | ------------------------------ | ------------------------------------ | ------------------------------------ |
# | Purpose                        | Converts array into 1D array         | Converts array into 1D array         |
# | Returns                        | Usually a **view** of original array | Always a **copy** of original array  |
# | Memory Usage                   | Less memory                          | More memory                          |
# | Speed                          | Faster                               | Slightly slower                      |
# | Changes Affect Original Array? | Yes (if view is returned)            | No                                   |
# | Syntax                         | `arr.reshape(-1)`                    | `arr.flatten()`                      |
# | Order Option                   | No direct order parameter            | Supports `order="C"` and `order="F"` |


# import numpy as np
# s=np.array([[[[10,20,30],[50,60,70]]]])

# print(s.shape)

# k=np.array([True, 3+4j, "Hii", 10, 10.9])

# print(k)

# w=np.array([True,False,1000,5.5])
# print(w) 


# import numpy as np

# p=np.result_type("bool","float","str")
# print(p)

# p=np.array([True, 3+4j , 1.0, False, "hi"])
# print(p)


# for loop--->

# basic for loop
# range()
# enumerate()
# reversed()
# sorted()
# zip()
# zip_longest()


# basic for loop

# x=[1,2,3,4,5,6,7,8]

# for i in x:
#     print(i)

# print()

# for i in x:
#     if i%2==0:
#         print(i)


# range()

# for i in range(25,101,1):
#     print(i,end=" ")

# enumerate()-->

# for i in enumerate("pallavi"):             #--> if use only one variable it return output in tuple 
#     print(i,end="")              #---> (0, 'p')(1, 'a')(2, 'l')(3, 'l')(4, 'a')(5, 'v')(6, 'i')
# print()
# for i,j in enumerate("pallavi"):             #i,j--> i for index position, j for value or elements.
#     print(i,j)

# 0 p
# 1 a
# 2 l
# 3 l
# 4 a
# 5 v
# 6 i

# reversed()-->

'''
k=[20,80,10,40,30,50,70,60]

for i in reversed(k):          #--> 20,80,10,40,30,50,70,60
    print(i, end=" ")          #--> 60 70 50 30 40 10 80 20 

print()

s="shreeyas"

for i in reversed(s):         #--> s h r e e y a s
    print(i, end=" ")         #--> s a y e e r h s

print()

p="pallavi"

for i in reversed(p):
    print(i, end=" ")

print()

''' 

# sorted()-->

''' 
z=[20,80,10,40,30,50,70,60]

for i in sorted(z):               #--> 20,80,10,40,30,50,70,60
    print(i,end=" ")              #--> 10 20 30 40 50 60 70 80     --> Descending --> ascending

print()

for i in sorted(z,reverse=True):   #--> 20,80,10,40,30,50,70,60
    print(i, end=" ")              #--> 80 70 60 50 40 30 20 10    --> Ascending to descending

print()

for i in sorted(z,reverse=False):   #--> 20,80,10,40,30,50,70,60
    print(i,end=" ")                #--> 10 20 30 40 50 60 70 80   --> Descending --> ascending

'''
'''
x="hey"
y="hi"

for i in zip(x,y):
    print(i,end=" ")                #--> ('h', 'h') ('e', 'i') 

print()

from itertools import zip_longest
for i in zip_longest(x,y):
    print(i,end=" ")                 #--> ('h', 'h') ('e', 'i') ('y', None)
''' 

# z='pallavi'
# print(enumerate(z))                    #<enumerate object at 0x0000025D28E90590>

# print()
# z='pallavi'
# print(list(enumerate(z)))              #[(0, 'p'), (1, 'a'), (2, 'l'), (3, 'l'), (4, 'a'), (5, 'v'), (6, 'i')]

 

# 1.wap to print the number form 1 -20 segregate even and odd number into list

# even=[]
# odd=[]

# for i in range(1,20+1,1):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)                       #even--> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(odd)                        #odd-->  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# # 2.wap to extract vowels and digits in a string
# s="hello123"

# alpha=[]
# digit=[]
# for i in s:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         digit.append(i)

# print(alpha)                         #Alpha---> ['h', 'e', 'l', 'l', 'o']
# print(digit)                         #Digit---> ['1', '2', '3']


# 3.wap to capitalize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]

# for i in l:
#     print(i.capitalize(),end=" ")          #Vaidegi Rahul Shivam Kapil Patil 
    

# 4.wap to extract only individual data types form the list

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

# for i in l:
#     if type(i) in (int,float,complex,bool):
#         print(i)

# 1
# 23.4
# (5+6j)
# True
# False

# print()

# for i in l:
#     if isinstance(i,(int,float,complex,bool)):
#         print(i)

# 1
# 23.4
# (5+6j)
# True
# False

# 5.wap to extract only individual data types from the list and sum all the individual data types

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]




# 6.wap to print the count of alphabets and numbers and space in the given string

# s="india got the independence in the year 1947"


# 7.wap to check how many words are present in the given sentence

# s="hello world sentence"


# 8.wap to create a dictionary and print the characters 
# and its Ascii value pair
# s="hello world
# output:--> {"h":ascii value,"e":ascii value........}


# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it

# names=["apple","google","yahoo","microsoft","gmail","walmart"]

# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}



# 10.wap to print series of factorial(take user input)

# a="pallavi"

# for i in range(len(a)):
#     print(i,a[-i])

# 0 p
# 1 a
# 2 l
# 3 l
# 4 a
# 5 v
# 6 i

import matplotlib.pyplot as plt
Name=["Virat","Rohit","Hardik","Abhishek"]
IPL=[150,100,99,88]
T20=[50,70,45,100]
plt.barh(Name,IPL)
plt.barh(Name,T20, color="pink")
plt.show()