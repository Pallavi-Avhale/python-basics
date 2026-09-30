# ---> NUMPY 
# ---> List | Array
# ---> List accept Homo as well as Heterogenus
# ---> Array accept only Homogenous elements
# ---> List will take more memory
# ---> Array take less memory
# ---> List datatype is slower
# ---> Array will be faster
# ---> List we perform less operations
# ---> Array we perform more operations---> it perform differents inbuild methods at a time  (60+)
# ---> List to perform any operstion loop is required
# ---> Array looping concept is not required (working on --> vectorised operation, matrix operations, Numberical operations, ML & AL also using, liner algebra )
# ---> 
# ---> Step --1 --> import numpy  or import numpy as np
# --->
# ---> To check current version of the Numpy
# import numpy as np

# print(np.__version__)                        #2.3.2
  

# ---> 
# array(): To convert sequence data type into array we use array():
# ---> Syntax for array ---> New_var=np.array(iterable)    #Sequence datatype--> String/List/Tuple



# x=[10,20,30,40]
# print(x)                        #[10 20 30 40]
# print()
# print(type(x))                  #<class 'list'> #Datatype


# import numpy as np

# y=np.array([10,20,30,40])
# print(y)                          #[10 20 30 40]
# print()
# print(type(y))                    #<class 'numpy.ndarray'>  Datatype

# r=np.array([100,200,300,400])
# print(r)                             #[100,200,300,400]
# print()
# print(r.dtype)                       #int64

# ---> Scale  ---> Pass data type like wise 
# bool
#  | 
# interger
#   |
# float
#   |
# complex
#   |
# String    <u32 ---> latine indian character Unicode 

# Bool --> Complex --> Here all remaining data type is converting into the complexdatatype

#float--> interger


# Result_type() ---> whenever we use combination datatype , that time to check which data type it will give the output

# import numpy as np

# n=np.result_type("bool","int")
# print(n)                                               #int64
# print()
# m=np.result_type("int","bool")
# print(m)                                                #int64
# print()
# n=np.result_type("int","float")
# print(n)                                               #float64
# print()
# n=np.result_type("float","complex")
# print(n)                                                #complex128 ---->    64+64
# print()
# n=np.result_type("complex","str")
# print(n)                                                 #<U64
# print()



# import numpy as np

# w=np.array([True,False,1000])
# print(w)                                            #[   1    0 1000]  --> it will convert bool to int datatype
# print()
# w=np.array([True,False,1000,5.5])
# print(w)                                            #[   1.     0.  1000.     5.5]  --> it will convert all into float

# print()
# w=np.array([True,False,1000,5.5, 2+4j])
# print(w)                                            # [   1. +0.j    0. +0.j 1000. +0.j    5.5+0.j    2. +4.j]   --> it will convert all into complex Datatype
# print()
# w=np.array([True,False,1000,5.5, 2+4j, "Hii"])
# print(w)                                             #['True' 'False' '1000' '5.5' '(2+4j)' 'Hii']   --> it will convert all into string datatype
# print()

# 
# ---> How to create a empty array
# ---> Zeop/Empty array---> New_Var=np.array(value)   #not use []

# import numpy as np
# a=np.array(10)
# print(a)                      #10
# print()
# print(type(a))                #<class 'numpy.ndarray'>
# print()
# print(a.dtype)                #int64
# print()
# print(a.ndim)                 #0
# print()
# print(a.shape)                #()  --> empty structure 

# How to create single array 
# 1 Dimensional array---> New_Var=np.array([list])

''' 
import numpy as np
a=np.array([10,20,30,40])
print(a)                      #[10 20 30 40]
print()
print(type(a))                #<class 'numpy.ndarray'>
print()
print(a.dtype)                #int64
print()
print(a.ndim)                 #1 --> 1 dimensional array  
print()
print(a.shape)                #(4,) ---> Show rows
'''

# How to create two dimensional array 
# 2 Dimensional array---> New_Var=np.array([list],[List])

# import numpy as np
# s=np.array([[10,20,30],[50,60,70]])

# print(s)                      #[[10 20 30]
#                               # [50 60 70]]
# print()
# print(type(s))                #<class 'numpy.ndarray'>
# print()
# print(s.dtype)                #int64
# print()
# print(s.ndim)                  #2 dimensional 
# print()
# print(s.shape)                 #(2, 3)  ----> Num rows , Num columns---> it will show matrix structure

# import numpy as np
# s=np.array([[10,20,30],[50,60,70],[1,2,3]])

# print(s)                      [[10 20 30]
#                               [50 60 70]
#                               [ 1  2  3]]
# print()
# print(type(s))                #<class 'numpy.ndarray'>
# print()
# print(s.dtype)                #int64
# print()
# print(s.ndim)                  #2 dimensional 
# print()
# print(s.shape)                 #(3, 3)  ----> Num rows , Num columns---> it will show matrix structure

#How to create a 3 Dimensional array

# import numpy as np
# s=np.array([[[10,20,30],[50,60,70]]])

# print(s)                      #[[[10 20 30]
#                               #[50 60 70]]]
# print()
# print(type(s))                #<class 'numpy.ndarray'>
# print()
# print(s.dtype)                #int64
# print()
# print(s.ndim)                  #3 dimensional 
# print()
# print(s.shape)                 #(1, 2, 3)  ----> Num rows , Num columns---> it will show matrix structure


#.__version__ 

# Properties-->
# shape
# ndim
# dtype
# size

# function
# type
# result_type

''' 
import numpy as np

x=np.array([1,2,3,4,5])
print(x)                  #[1 2 3 4 5]
print()
print(x.shape)            #(5,)
print()
print(x.ndim)             #1
print()
print(x.dtype)           #int64
print()
print(x.size)            #5
print()
print(x.nbytes)          #40  #---How?
print()
print(x.itemsize)        #8   #---How?
'''

# import numpy as np
# s=np.array([[10,20,30],[50,60,70]])

# print(s)                      #[[10 20 30]
#                               # [50 60 70]]
# print()
# print(type(s))                #<class 'numpy.ndarray'>
# print()
# print(s.dtype)                #int64
# print()
# print(s.ndim)                  #2 dimensional 
# print()
# print(s.shape)                 #(2, 3)  ----> Num rows , Num columns---> it 
# print()
# print(s.T)                     #[[10 50]        #T--> transpos--> rows to colmun
#                                 #[20 60]
#                                  #[30 70]]   


# convert 2 Dimensional array to 1 Dimensional

''' 
import numpy as np

p=np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]])
print(p)

# o/p-->
# [[ 1  2  3  4]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(p.shape)                #(3, 4)
print()
print(p.reshape(2,6))
print()

# o/p-->
# [[ 1  2  3  4  4  5]
#  [ 6  7  8  9 10 11]]

print(p.reshape(1,12))
print()

# o/p-->
# [[ 1  2  3  4  4  5  6  7  8  9 10 11]]

print(p.reshape(4,3))
print()

# o/p-->
# [[ 1  2  3]
#  [ 4  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

print(p.reshape(6,2))
print()

# o/p-->
# [[ 1  2]
#  [ 3  4]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]]

print(p.reshape(12,1))
print()

# o/p-->
# [[ 1]
#  [ 2]
#  [ 3]
#  [ 4]
#  [ 4]
#  [ 5]
#  [ 6]
#  [ 7]
#  [ 8]
#  [ 9]
#  [10]
#  [11]]

'''
'''
import numpy as np

z=np.array([[[10,20,30],[100,20,20],['a','b','c'],[40,50,60]]])
print(z)
print()

# o/p-->
# [[['10' '20' '30']
#   ['100' '20' '20']
#   ['a' 'b' 'c']
#   ['40' '50' '60']]]

# Multi dimesional array into single dimesional

print(z.reshape(-1))       #---> Multi dimesional array into single dimesional   

# o/p--> ['10' '20' '30' '100' '20' '20' 'a' 'b' 'c' '40' '50' '60'] --> Multi dimesional array into single dimesional

# standard method to convert  Multi dimesional array into single dimesional   

print()
print(z.flatten())          

# o/p--> ['10' '20' '30' '100' '20' '20' 'a' 'b' 'c' '40' '50' '60']

print()
print(z.reshape(2,6))        

# o/p-->
# [['10' '20' '30' '100' '20' '20']
#  ['a' 'b' 'c' '40' '50' '60']]

print()
print(z.flatten())          #['10' '20' '30' '100' '20' '20' 'a' 'b' 'c' '40' '50' '60']
print()

#   Order="C" (uppercase "C" )---> Rows
print(z.flatten(order="C"))       #['10' '20' '30' '100' '20' '20' 'a' 'b' 'c' '40' '50' '60']

#   Order="F" (uppercase "F" )---> Columns
print(z.flatten(order="F"))       #['10' '100' 'a' '40' '20' '20' 'b' '50' '30' '20' 'c' '60']

''' 


# import numpy as np

# z=np.array([[[10,20,30],[100,20,20],[30,20,10],[40,50,60]]])
# print(z)
# print()


# import numpy as np

# z=np.array([11,12,13,14])
# print(z)                           #o/p--> [11 12 13 14]
# print()

# repeat()--> Used To repeat the elements in give times 
# N_var=np.repeat(repeated_var, time)

# s=np.repeat(z,5)                 
# print(s)                           #o/p--> [11 11 11 11 11 12 12 12 12 12 13 13 13 13 13 14 14 14 14 14]

# tile--> it will repeate complete array

# a=np.tile(z,2)                      # Whole array is repeated 2 times.
# print(a)                             #o/p--> [11 12 13 14 11 12 13 14]

# Question--> Differ repeate and tile
# Question--> Differ range and nrange

# repeat() → repeats each element individually.

# tile() → repeats the complete array/pattern. 

# | Feature     | `repeat()`           | `tile()`               |
# | ----------- | -------------------- | ---------------------- |
# | Meaning     | Repeats each element | Repeats complete array |
# | Works On    | Individual elements  | Whole array            |
# | Syntax      | `np.repeat(array,n)` | `np.tile(array,n)`     |
# | Output Size | Element × n times    | Entire array × n times |
# | Use Case    | Duplicate values     | Duplicate pattern      |


# Copy------> copy from one variable to another variable, id address of both the variable is different , like Shallow copy
# New_var=old_var.copy() 

# import numpy as np
# x=np.array([10,11,12,13])
# y=x.copy()
# print(x)                      #-->[10 11 12 13]
# print(y)                      #-->[10 11 12 13]
# print()
# print("after modification in x")

# # --->[10 11 12 13] -->x

# x[0]=100                     #--> If we done any modification in 1 variable it won't affecet another one
# print(x)                     #--> [100  11  12  13]
# print()
# print(y)                     #--> [10 11 12 13]

# print("after modification in y")

# y[1]=200

# print(x)                   #--> [100  11  12  13]
# print()
# print(y)                   #--> [ 10 200  12  13]


# View------> Syntax--> New_var=old_var.view() 
# copy from one variable to another variable, 
# id address of both the variable is different , 
# but if we do any modification in one variable it will affect to another variable also.

# import numpy as np
# x=np.array([10,11,12,13])
# y=x.view()
# print(x)                      #-->[10 11 12 13]
# print(y)                      #-->[10 11 12 13]
# print()
# print("after modification in x")

# --->[10 11 12 13] -->x

# x[0]=100                     #--> If we done any modification in 1 variable it will affecet another one also 
# print(x)                     #--> [100  11  12  13]
# print()
# print(y)                     #--> [100  11  12  13]

# print("after modification in y")

# y[1]=200

# print(x)                   #--> [100 200  12  13]
# print()
# print(y)                   #--> [100 200  12  13]

'''
import numpy as np

s=np.array(["a","b","c","d"])
# new_var=old_var.copy()
t=s.copy()
print(s)                      #-->['a' 'b' 'c' 'd']
print()
print(t)                      #-->['a' 'b' 'c' 'd']
print()
print("Modification in s variable")
print()
s[3]="x"                        #-->Modification in s variable
print(s)                        #-->['a' 'b' 'c' 'x']
print()
print(t)                        #-->['a' 'b' 'c' 'd']
print("Modification in t variable")
print()
t[0]="y"                        #-->Modification in t variable 
print(s)                        #-->['a' 'b' 'c' 'x']
print()
print(t)                        #-->['y' 'b' 'c' 'd']
''' 

# import numpy as np

# s=np.array(["a","b","c","d"])
# new_var=old_var.view()
# t=s.view()
# print(s)                      #-->['a' 'b' 'c' 'd']
# print()
# print(t)                      #-->['a' 'b' 'c' 'd']
# print()
# print("Modification in s var")
# print()
# s[3]="x"                        #-->Modification in s variable
# print(s)                        #-->['a' 'b' 'c' 'x']
# print()
# print(t)                        #-->['a' 'b' 'c' 'x']
# print("Modification in t var")
# print()
# t[0]="y"                        #-->Modification in t variable 
# print(s)                        #-->['y' 'b' 'c' 'x']
# print()
# print(t)                        #-->['y' 'b' 'c' 'x']


# 2D Array ([[],[]])

# import numpy as np
# p=np.array([[1,2,3,4],[5,6,7,8]])
# print(p)

# o/p-->
# [[1 2 3 4]
#  [5 6 7 8]]

print()

# Flatten()--> multi--dimensional array to the single or 1 Dimensional 
# Mofification in flatten--> If we done any modification in flatten array it will only affected for the flatten new variable , 
# It won't affected for the privious/old var
# new_var=old_var(order="C") ---> C--> ROW
# new_var=old_var(order="F") ---> F--> coloumn

# y=p.flatten()
# print(y)               #--> [1 2 3 4 5 6 7 8]
# print()
# print(" Modification In Flatten")
# print()
# y[2]=300               # Modification In Flatten
# print(y)               #--> [  1   2 300   4   5   6   7   8]
# print()
# print(p)

# o/p-->
# [[1 2 3 4]
#  [5 6 7 8]]


# Ravel()--> it will convert multi dimentional into single dimensional
# if we done any modification in ravel variable / new var will also affect the original var/ old var 

# import numpy as np
# d=np.array([[100,200,300],[400,500,600]])
# print(d)

# o/p-->

# [[100 200 300]
#  [400 500 600]]

# print()
# r=d.flatten(order="C")
# print(r)                      #-->[100 200 300 400 500 600]

# print()

# c=d.flatten(order="F")
# print(c)                      #-->[100 200 300 400 500 600]

# print()

# print("Modiffication in flatten")

# r[1]=50                        #-->Modiffication in flatten
# print(r)                       #-->[100  50 300 400 500 600]
# print()
# print(d)              

# o/p--> 
# [[100 200 300]
#  [400 500 600]]

# print()
# print(c)                      #--> [100 400 200 500 300 600]

# import numpy as np
# x=np.array([[100,200,300],[400,500,600]])
# print(x)
# o/p-->
# [[100 200 300]
#  [400 500 600]]

# print()

# --> new_var=old_var.ravel()

# s=x.ravel()
# print(s)                   #-->[100 200 300 400 500 600]
# print()
# s=x.ravel(order="C")    #--> Row wise Arrangemnet
# print(s)                   #-->[100 200 300 400 500 600]
# print()  
# s=x.ravel(order="F")    #--> Column wise Arrangemnet
# print(s)                      #-->[100 400 200 500 300 600]
# print()


# import numpy as np
# x=np.array([[100,200,300],[400,500,600]])
# print(x)
# o/p-->
# [[100 200 300]
#  [400 500 600]]

# print()
# m=x.ravel() 
# print(m)                  #--> [100 200 300 400 500 600]
# print()
# print("RAVEL VARIABLE MODIFICATION")

# print()
# m[4]=1000
# print(m)                  #--> [ 100  200  300  400 1000  600]
# print()
# print(x)

# o/p-->
# [[ 100  200  300]
#  [ 400 1000  600]]

# 3 METHODS--> FLATTEN()--(WE CAN'T CHANGE OREDR AND POSITION --> RESHAPE(-1)-->RAVEL()--> WE CAN DO MODIFICATION ORDER AND POSITION WISE

# import numpy as np
# x=np.array([[100,200,300],[400,500,600]])
# print(x)

# O/P-->
# [[100 200 300]
#  [400 500 600]]

# print()
# print(x.reshape(-1))       #[100 200 300 400 500 600]
# print()
# p=x.flatten()
# print(p)                   #[100 200 300 400 500 600]
# print()
# a=x.ravel()
# print(a)                   #[100 200 300 400 500 600]

# arange()-->   to print squence of no. 
# it will get the o/p in the form of array
#  it work on float num 
# don't use looping
# syntax--> New_var=np.array(si:ei:sv)         #-- si--0, ei-- value+1, sv-- by default 1

# range()-->   to print squence of no. , it don't work on float num
# Use looping like --> fir i in range(si:ei:sv) 
# not work on decimal num --> is use decimal num it will show error
# syntax--> for i in range(si:ei:sv):


# import numpy as np

# k=np.arange(5)
# print(k)                      #--> [0 1 2 3 4]
# print()

# y=np.arange(1,11,1)
# print(y)                      #--> [ 1  2  3  4  5  6  7  8  9 10]

# print()
# p=np.arange(1.1,6.1,1.1)
# print(p)                      #--> [1.1 2.2 3.3 4.4 5.5]

# o=np.arange(10.1,15.1,1.1)
# print(o)                        #-->[10.1 11.2 12.3 13.4 14.5]

# linspace()--> 
# we want to print squence of num in equal formate use linspace

# syntac--> new_var=np.linspace(start:stop:num) 
# if we  use only start any stop  , it will generate 50 default num
# we can also mention te specific num value to display

# import numpy as np

# n=np.linspace(1,10)
# print(n)
# print()

# o/p-->

# [ 1.          1.18367347  1.36734694  1.55102041  1.73469388  1.91836735
#   2.10204082  2.28571429  2.46938776  2.65306122  2.83673469  3.02040816
#   3.20408163  3.3877551   3.57142857  3.75510204  3.93877551  4.12244898
#   4.30612245  4.48979592  4.67346939  4.85714286  5.04081633  5.2244898
#   5.40816327  5.59183673  5.7755102   5.95918367  6.14285714  6.32653061
#   6.51020408  6.69387755  6.87755102  7.06122449  7.24489796  7.42857143
#   7.6122449   7.79591837  7.97959184  8.16326531  8.34693878  8.53061224
#   8.71428571  8.89795918  9.08163265  9.26530612  9.44897959  9.63265306
#   9.81632653 10.        ]

# p=np.linspace(1,10,5)      #--> (start:1, stop:10, num:5)
# print(p)                   #--> [ 1.    3.25  5.5   7.75 10.  ]

# print()

# z=np.linspace(1,10,5, retstep=True)
# print(z)

# o/p--> (array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ]), np.float64(2.25))

''' 
# start--> 1

# next--> Start_num +Difference_number
                # 1 + 2.25---> 3.25

'''

# n=np.linspace(1,10,retstep=True)
# print(n)
# print()

# o/p-->
# (array([ 1.        ,  1.18367347,  1.36734694,  1.55102041,  1.73469388,
#         1.91836735,  2.10204082,  2.28571429,  2.46938776,  2.65306122,
#         2.83673469,  3.02040816,  3.20408163,  3.3877551 ,  3.57142857,
#         3.75510204,  3.93877551,  4.12244898,  4.30612245,  4.48979592,
#         4.67346939,  4.85714286,  5.04081633,  5.2244898 ,  5.40816327,
#         5.59183673,  5.7755102 ,  5.95918367,  6.14285714,  6.32653061,
#         6.51020408,  6.69387755,  6.87755102,  7.06122449,  7.24489796,
#         7.42857143,  7.6122449 ,  7.79591837,  7.97959184,  8.16326531,
#         8.34693878,  8.53061224,  8.71428571,  8.89795918,  9.08163265,
#         9.26530612,  9.44897959,  9.63265306,  9.81632653, 10.        ]), np.float64(0.1836734693877551))


# import numpy as np

# y=np.linspace(5,10,2)
# print(y)                                  #--> [ 5. 10.]
# print()

# y=np.linspace(5,10,2,retstep=True)
# print(y)                                  #--> (array([ 5., 10.]), np.float64(5.0))


# zeros()---->  to print zero num only,--> by default it will give float / decimal num o/p
# ones()-->     to print one num only , --> float output
# full()-->     to print full num only 

# import numpy as np

# x=np.zeros(3)
# print(x)                   #---> [0. 0. 0.]


# y=np.zeros(3,dtype=int)
# print(y)                   #[0 0 0]


# To change the Single dimension to multi--dimension

# u=np.zeros((3,3),dtype=complex)
# print(u)

# o/p-->
# [[0.+0.j 0.+0.j 0.+0.j]
#  [0.+0.j 0.+0.j 0.+0.j]
#  [0.+0.j 0.+0.j 0.+0.j]]

# u=np.zeros((3,3))
# print(u)

# # o/p-->
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]


# ones()-->     to print one num only 

# import numpy as np

# p=np.ones(2)
# print(p)          #--> [1. 1.]--> by default float datatype

# a=np.ones((6,2),dtype=int)
# print(a)

# o/p-->
# [[1 1]
#  [1 1]
#  [1 1]
#  [1 1]
#  [1 1]
#  [1 1]]


# full()-->

# import numpy as np

# l=np.full((2,2),"python")
# print(l)

# o/p-->

# [['python' 'python']
#  ['python' 'python']]

# -----------------------------------------------------------------------------------------------------

# eye()-------> N_V=np.eye(N,M,K)    OR   # N_V=np.eye(row,column, k=value) --->N-->ROWS, M--->COLUMN, K---->DIGONAL
# we can use rows
# we can use both rows as well as columns
# we can shift diagonal
# we can create rectangle as well as square



# import numpy as np
# x=np.eye(3)                 #3---> Rows
# print(x)

# o/p-->
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# ------------------------------------------------------------------------------------------------------

# import numpy as np

# c=np.eye(4,6)                 #----> 4-->ROWS, 6---> COLUMNS
# print(c)

# O/p->
# [[1. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0.]]

# ------------------------------------------------------------------------------------------

# import numpy as np

# c=np.eye(3,3)                 #----> 3-->ROWS, 3---> COLUMNS
# print(c)

# o/p-->
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# ----------------------------------------------------------------------------------------

# Rectangle Matrix-->

# import numpy as np

# c=np.eye(5,10)                 #----> 5-->ROWS, 10---> COLUMNS
# print(c)

# o/p-->
# [[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]]

# --------------------------------------------------------------------------------------------

# import numpy as np

# c=np.eye(3,3,k=1)                 #----> 3-->ROWS, 3---> COLUMNS, k---> digonal
# print(c)

# o/p-->

# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# -----------------------------------------------------------------------------------------------------


# import numpy as np

# c=np.eye(5,5,k=1)                 #----> 5-->ROWS, 5---> COLUMNS
# print(c)

# o/p-->

# [[0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]
#  [0. 0. 0. 0. 0.]]

# ----------------------------------------------------------------------------------------------

# k=(-1)----> It will shift right to left 

# import numpy as np

# s=np.eye(5,5,k=-1)
# print(s)

# o/p-->
# [[0. 0. 0. 0. 0.]
#  [1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]]

# ------------------------------------------------------------

# import numpy as np

# s=np.eye(2,2,k=-1)
# print(s)
# print()

# o/p-->

# [[0. 0.]
#  [1. 0.]]

# ----------------------------------------------------------------------------

# import numpy as np

# s=np.eye(5,5,k=-2)
# print(s)

# o/p-->
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]


# ---------------------------------------------------------------------

# Identity()--> Only we can create diagonal number , we con't shift diagonal, 
# we can't use column, only use rows
# only create squre, not create rectangle
# syntax--> N_V=np.identity(N)      m#N--> row only

# import numpy as np

# s=np.identity(2)
# print(s)

# o/p-->
# [[1. 0.]
#  [0. 1.]]

# ----------------------------------------------------------------------------------------------


# import numpy as np

# s=np.eye(4)
# print(s)

# o/p-->

# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# ----------------------------------------------------------------------------------------------

# print()
# import numpy as np

# s=np.identity(4)
# print(s)

# o/p-->
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# -----------------------------------------------------------------

# Joining Array--->
# stack()
# vstack()
# hstack()
# dstack()
# columnstack()
# rowstack()

# ----------------------------------------------------------------------------------------------

# import numpy as np

# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)

# o/p-->
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# -------------------------------------------------------------------

# Diag()---> Only to print diagonal number
# syntax--. N_V=np.diag(list/variable)

# print()

# y=np.diag(x)
# print(y)
# print()

# o/p-->  #[1 5 9]

# ----------------------------------------------------------------------------------------------

# y=np.diag([10,20,30])
# print(y)
# print()

# o/p-->

# [[10  0  0]
#  [ 0 20  0]
#  [ 0  0 30]]


# -------------------------------------------------------------------------

# y=np.diag([1,5,9])
# print(y)
# print()

# o/p-->
# [[1 0 0]
#  [0 5 0]
#  [0 0 9]]

# ----------------------------------------------------------------------------------------------

# Joining Array--->
# stack()
# vstack()
# hstack()
# dstack()
# columnstack()
# rowstack()

# ----------------------------------------------------------------------------------------------

'''
concatenate()---> new=np.concatenate((var1,var2),axis=0/1) ------> #0--> row , 1--> column

import numpy as np

x=np.array([10,20,30,40])
y=np.array([1,2,3,4])

z=np.concatenate((x,y))
print(z)                      #-----> [10 20 30 40  1  2  3  4]

print()
z=np.concatenate((x,y),axis=0)          #axis=0---> row wise
print(z)                      #----->  [10 20 30 40  1  2  3  4]
print()

z=np.concatenate((x,y),axis=1)          #axis=0---> row wise
print(z)                         #--> numpy.exceptions.AxisError: axis 1 is out of bounds for array of dimension 1

''' 

# ----------------------------------------------------------------------------------------------

'''
import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])

z=np.concatenate((x,y))
print(z)
print()

# o/p-->

# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

z=np.concatenate((x,y),axis=0)
print(z)
print()

# o/p-->
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

z=np.concatenate((x,y),axis=1)                   #axis=1--> 1--> column
print(z)

# o/p-->
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

''' 
# ----------------------------------------------------------------------------------------------

# stack()-------------> # use 1 diamensional , it will create automatically new dimension,
# axis=1 it will work for 1 dimesional array also 

''' 
1--> Dimensional 

import numpy as np

x=np.array([10,20,30,40])
y=np.array([1,2,3,4])

z=np.stack((x,y))
print(z)                  
print()

# o/p-->
# [[10 20 30 40]
#  [ 1  2  3  4]]


z=np.stack((x,y), axis=0)
print(z)
print()

# o/p-->
# [[10 20 30 40]
#  [ 1  2  3  4]]

z=np.stack((x,y), axis=1)
print(z)
print()

# o/p-->
# [[10  1]
#  [20  2]
#  [30  3]
#  [40  4]]


''' 
# ----------------------------------------------------------------------------------------------

# 2 dimensional-->

''' 
import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])

z=np.stack((x,y))
print(z)
print()

# o/p-->

# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]

z=np.stack((x,y),axis=0)
print(z)
print()

# o/p-->
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]


z=np.stack((x,y),axis=1)
print(z)
print()


# o/p-->


# [[[ 1  2  3]
#   [ 7  8  9]]

#  [[ 4  5  6]
#   [10 11 12]]]


''' 
# ----------------------------------------------------------------------------------------------

# Vstack()---> Vertical create
# it will arrange row wise only 
# we can't use axis, it will show error

'''
import numpy as np

x=np.array([10,20,30,40])
y=np.array([1,2,3,4])

z=np.vstack((x,y))
print(z)                  
print()

# o/p-->
# [[10 20 30 40]
#  [ 1  2  3  4]]

z=np.vstack((x,y),axis=0)
print(z)                         #-->TypeError: vstack() got an unexpected keyword argument 'axis'       
print()

''' 

# hstack()-- Horizontal , column wise

# 1--> Dimensional

# import numpy as np

# x=np.array([10,20,30,40])
# y=np.array([1,2,3,4])

# z=np.hstack((x,y))
# print(z)                            #--->[10 20 30 40  1  2  3  4]             
# print()

''' 
# 2 dimensional 

import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])

z=np.hstack((x,y))
print(z)
print()

# o/p-->
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

z=np.hstack((x,y),axis=0)
print(z)                       #TypeError: hstack() got an unexpected keyword argument 'axis'
print()

'''

# dstack()-- Depth stack, working on 1 D automatically it will creating it will creating into 3 dimensional


# 1--> Dimensional

'''
import numpy as np

x=np.array([10,20,30,40])
y=np.array([1,2,3,4])

z=np.dstack((x,y))
print(z)                             
print()

# o/p-->
# [[[10  1]
#   [20  2]
#   [30  3]
#   [40  4]]]


z=np.dstack((x,y),axis=0)
print(z)                                #TypeError: dstack() got an unexpected keyword argument 'axis'                 
print()
''' 

# 2 dimensional 

''' 

import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])

z=np.dstack((x,y))
print(z)
print()


# o/p-->
# [[[ 1  7]
#   [ 2  8]
#   [ 3  9]]

#  [[ 4 10]
#   [ 5 11]
#   [ 6 12]]]

z=np.dstack((x,y),axis=0)
print(z)                              #--> TypeError: dstack() got an unexpected keyword argument 'axis'
print()
''' 



# column_stack()-->


# 1--> Dimensional

'''
import numpy as np

x=np.array([10,20,30,40])
y=np.array([1,2,3,4])

z=np.column_stack((x,y))
print(z)                             
print()

# o/p-->
# [[10  1]
#  [20  2]
#  [30  3]
#  [40  4]]

z=np.column_stack((x,y),axis=0)
print(z)                                  #-->TypeError: column_stack() got an unexpected keyword argument 'axis'                       
print()
''' 

# 2 dimensional 

'''
import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])

z=np.column_stack((x,y))
print(z)
print()

# o/p-->
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

z=np.column_stack((x,y),axis=0)
print(z)                           #-->TypeError: column_stack() got an unexpected keyword argument 'axis'
print()
'''

# hstack () -- 1--> Dimensional

# import numpy as np

# x=np.array([10,20,30,40])
# y=np.array([1,2,3,4])

# z=np.hstack((x,y))
# print(z)                            #--->[10 20 30 40  1  2  3  4]             
# print()



# column_stack()-->

# 1--> Dimensional


# import numpy as np

# x=np.array([10,20,30,40])
# y=np.array([1,2,3,4])

# z=np.column_stack((x,y))
# print(z)                             
# print()

# o/p-->

# [[10  1]
#  [20  2]
#  [30  3]
#  [40  4]]


'''
# hstack()-->

# 2 dimensional 

import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])

z=np.hstack((x,y))
print(z)
print()

# o/p-->
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

# column_stack()

# 2 dimensional 


import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])

z=np.column_stack((x,y))
print(z)
print()

# o/p->
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
''' 

# Searching Array Elements

# where()
# argmax()
# argmin()
# search_sort()


# where()---> wher the condition satisfy it will give the output as a index position, else it will show blank space
# syntax-> new=np.where(condition,"working","not working")
# we can pass condional statement also like "working", "not working"

''' 
import numpy as np

x=np.array([10,15,20,30,40,50])
y=np.where(x>30)
print(y)

# o/p-->
# (array([4, 5]),)

# 10>30--False
# 15>30--False
# 20>30--False
# 30>30--False
# 40>30--True
# 50>30--True

x=np.array([10,15,20,30,40,50])
y=np.where(x>30,"Working","Not working")
print(y)


# o/p-->
# (array([4, 5]),)
# ['Not working' 'Not working' 'Not working' 'Not working' 'Working'
#  'Working']

'''

# argmax()--> It will show position of the maximum number position 

'''
import numpy as np

x=np.array([10,15,20,30,40,50])

print(x.argmax())

# o/p->
# 5

# 2 dimensional 

import numpy as np

x=np.array([[1,2,3],[4,5,6]])
print(x.argmax())
print()

# o/p-->

# 5
# 5

import numpy as np

x=np.array([[10,15,20],[35,56,78]])
print(x.argmax())                                #-->5
print()
print(x.argmax(axis=0))                          #-->[1 1 1]
print()
print(x.argmax(axis=1))                          #-->[2 2]
print()


import numpy as np

x=np.array([[10,15,20],[35,56,78],[100,200,300]])
print(x.argmax())                                #-->8
print()
print(x.argmax(axis=0))                          #-->[2 2 2]
print()
print(x.argmax(axis=1))                          #-->[2 2 2]
print()
''' 

# argmin()--> It will show position of the minimum number position 

# import numpy as np

# x=np.array([10,15,20,30,40,50])

# print(x.argmin())
# print()

# o/p->
# 0

# 2 dimensional 

# import numpy as np

# x=np.array([[1,2,3],[4,5,6]])
# print(x.argmin())
# print()

# o/p-->

# 0

# import numpy as np

# x=np.array([[10,15,20],[35,56,78]])
# print(x.argmin())                                #-->5
# print()
# print(x.argmin(axis=0))                          #-->[1 1 1]
# print()
# print(x.argmin(axis=1))                          #-->[2 2]
# print()


# import numpy as np

# x=np.array([[10,15,20],[35,56,78],[100,200,300]])
# print(x.argmin())                                #-->8
# print()
# print(x.argmin(axis=0))                          #-->[2 2 2]
# print()
# print(x.argmin(axis=1))                          #-->[2 2 2]
# print()


#

# nonzero()---> it will give the output of non zero position 

# import numpy as np
# t=np.array([0,1,2,0,3,4,0,7])
# e=np.nonzero(t)
# print(e)                            #(array([1, 2, 4, 5, 7]),)


# import numpy as np
# t=np.array([0,1,2,0,3,4,0,7])
# e=np.count_nonzero(t)
# print(e)                                 # ---> 5


# searchsorted()-----> it will give the sorted list backside and give values position will get out put


# import numpy as np

# p=np.array([10,500,200,100])
# print(p.searchsorted(500))         #----> backside 1st it will sort the list then give the index position of the specified element


# import numpy as np

# l=np.array([10,20,30,40])
# print(l.searchsorted(40))        #---->3

# print()
# print(l.searchsorted(15))            #--> 1 --> 15 present in between the 10[0] and 20 [1]

# print()
# print(l.searchsorted(8))             #--->0--> 8 is present befor 10 [0]

# print()
# print(l.searchsorted(20.5))            #-->2 --> presnet after 20 [1]

# import numpy as np

# p=np.array([400,500,200,100])
# print(p.searchsorted(200))           #0

# print()
# print(p.searchsorted(50))

# import numpy as np
# x=np.array([45,89,100,5,12,3])
# n=np.sort(x)
# print()
# print(n.searchsorted([22.5,55.4,35.35]))                #--> [3 4 3]


# import numpy as np
# x=np.array([[11,34,56],[78,90,100]])
# print(x)

# o/p-->
# [[ 11  34  56]
#  [ 78  90 100]]

# print()
# a=x.flatten()
# print(a)                                           #-->[ 11  34  56  78  90 100]

# k=np.sort(a)
# print(k)
# print()
# print(k.searchsorted(35))                           #--> 2

# split()
# array_split()

# import numpy as np
# a=np.array([10,20,30,40,50,60,70,80])
# print(a)                                      #--> [10 20 30 40 50 60 70 80]
# print()

#split()    --> New_var=np.split(array_name,section)
# If you want to sepearate the array in equal manner  use split

# t=np.split(a,2)
# print(t)                                      #--> [array([10, 20, 30, 40]), array([50, 60, 70, 80])]


# array_split()--> New_var=np.array_split(array_name,section)
# If you want to sepearate the array in equal manner/ unqual manner use split
#  if we pass num over index number it will won't show any error , it show all possible groups and remaining all remains empty

# import numpy as np
# a=np.array([10,20,30,40,50,60,70,80])
# print(a)                                      #--> [10 20 30 40 50 60 70 80]
# print()

# y=np.array_split(a,4)                         #--> [array([10, 20]), array([30, 40]), array([50, 60]), array([70, 80])]
# print(y)
# print()
# y=np.array_split(a,3)        
# print(y)                                      #--> [array([10, 20, 30]), array([40, 50, 60]), array([70, 80])]


# y=np.array_split(a,10)            #[array([10]), array([20]), array([30]), array([40]), array([50]), array([60]), array([70]), array([80]), array([], dtype=int64), array([], dtype=int64)]
# print(y)

# --------------------------------------------------

# Mathmatical operation
# add()--> #New_var=np.add(var1,var2)
# substract()--> #New_var=np.substract(var1,var2)
# multiply()--> #New_var=np.multiply(var1,var2)
# divide()--> #New_var=np.divide(var1,var2)
# power()--> #New_var=np.power(var1,var2)
# mod()--> #New_var=np.mod(var1,var2)
# remainder() --> #New_var=np.remainder(var1,var2)
# sqrt()--> #New_var=np.sqrt(var)
# square()--> #New_var=np.square(var)
# cbrt()--> #New_var=np.cbrt(var1)
# abs()-->  #New_var=np.abs(var1)
# sign()--> #New_var=np.sign(var1)



# -------------------------------------------------------------------

# add()--> #New_var=np.add(var1,var2)

'''
import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,5,6,7])

z=np.add(x,y)
print(z)                  #--> [ 5  7  9 11]
print()

# substract()--> #New_var=np.substract(var1,var2)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,5,6,7])

z=np.subtract(x,y)
print(z)                   #--> [-3 -3 -3 -3]
print()

# multiply()--> #New_var=np.multiply(var1,var2)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,5,6,7])

z=np.multiply(x,y)
print(z)                   #--> [ 4 10 18 28]
print()

# divide()--> #New_var=np.divide(var1,var2)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,5,6,7])

z=np.divide(x,y)
print(z)                   #--> [0.25       0.4        0.5        0.57142857]
print()

# power()--> #New_var=np.power(var1,var2)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,5,6,7])

z=np.power(x,y)
print(z)                   #--> [    1    32   729 16384]
print()

# mod()--> #New_var=np.mod(var1,var2)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,5,6,7])

z=np.mod(x,y)
print(z)                   #--> [1 2 3 4]
print()

# remainder() --> #New_var=np.remainder(var1,var2)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,5,6,7])

z=np.remainder(x,y)
print(z)                   #--> [1 2 3 4]
print()

# sqrt()--> #New_var=np.sqrt(var)

import numpy as np
x=np.array([4,25,16,36,49])
print("sqet")
z=np.sqrt(x)
print(z)                   #--> [2. 5. 4. 6. 7.]
print()

# square()--> #New_var=np.square(var)


import numpy as np
x=np.array([4,25,16,36,49])

z=np.square(x)
print(z)                   #--> [  16  625  256 1296 2401]
print()


# cbrt()--> #New_var=np.cbrt(var1)

import numpy as np
x=np.array([4,25,16,36,49])

z=np.cbrt(x)
print(z)                   #-->[1.58740105 2.92401774 2.5198421  3.30192725 3.65930571]
print()


# abs()-->  #New_var=np.abs(var1)


import numpy as np
x=np.array([4,25,16,36,49])

z=np.abs(x)
print(z)                   #--> [ 4 25 16 36 49]
print()


# sign()--> #New_var=np.sign(var1)

import numpy as np
x=np.array([4,25,16,36,49])

z=np.sign(x)
print(z)                   #--> [1 1 1 1 1]
print()

''' 

# cbrt()--> #New_var=np.cbrt(var1)

# import numpy as np
# x=np.array([8,27,64,125])

# z=np.cbrt(x)
# print(z)                   #-->[2. 3. 4. 5.]
# print()


# abs()-->  #New_var=np.abs(var1)
# ---> convert negative num to positive num


# import numpy as np
# x=np.array([-12,67,-90,-100,-345,678])

# z=np.abs(x)
# print(z)                   #--> [ 12  67  90 100 345 678]
# print()

# o=np.absolute(x)
# print(o)                     # --> [ 12  67  90 100 345 678]


# sign()--> #New_var=np.sign(var1)
# positive num to --> 1
# negative number to --> -1
# zero number to --> 0

# import numpy as np
# #          [ 1 -1  0  -1  -1  1  0  1]
# x=np.array([10,-90,0,-23,-45,100,0,200])

# z=np.sign(x)
# print(z)                   #--> [ 1 -1  0 -1 -1  1  0  1]
# print()


# ------------------------------------------------------------------------------------------------------

# exp()--> Value of e is fixed = 2.718281828
# new_var=np.exp(var1)
# e**elements/values=o/p

# import numpy as np

# x=np.array([1,2,3,4])
# y=np.exp(x)
# print(y)                    #--> [ 2.71828183  7.3890561  20.08553692 54.59815003]


# ------------------------------------------------------------------------------------------------------

# Unique() ---> it will return only unique element

'''
import numpy as np

s=np.array([10,20,30,10,20,80,90,80])
print(s)
print()

p=np.unique(s)
print(p)                           #--> [10 20 30 80 90]

print()

p=np.unique(s,return_index=True)           # --> (array([10, 20, 30, 80, 90]), array([0, 1, 2, 5, 6])) it will return index position 
print(p)

print()

p=np.unique(s,return_counts=True)           # --> (array([10, 20, 30, 80, 90]), array([2, 2, 1, 2, 1])) 
print(p)

''' 
# -----------------------------------------------------------------------------------------

# isin()---> in 2 array what are the common elements is present it will show 

# import numpy as np

# r=np.array([1,2,3,4,5])
# t=np.array([4,7,2,3,9])

# j=np.isin(r,t)
# print(j)                       # [False  True  True  True False]

# i=np.isin(t,r)
# print(i)                       # [ True False  True  True False]


# -------------------------------------------------------------------------------------------------

# Union1d()-----> both array combining and give unique array( choice only unique elemenst)
'''
import numpy as np

x=np.array([11,11,12,13,14,11,15,11])
y=np.array([21,79,90,100,13,12])

z=np.union1d(x,y)
print(z)                           #--> [ 11  12  13  14  15  21  79  90 100]
print()

# -------------------------------------------------------------------------------------------------

# intersect1d()-->  common elements from both the array and make 
p=np.intersect1d(x,y)
print(p)                           #--> [12 13]
print()

# -------------------------------------------------------------------------------------------------
 
# setxor1d()-->  uncommon elements from both array
p1=np.setxor1d(x,y)
print(p1)                          #--> [ 11  14  15  21  79  90 100]
print()

# -------------------------------------------------------------------------------------------------

e=[11,12,14,13]
e1=[21,34,11,13]

a=np.array(e)
b=np.array(e1)

c=np.setdiff1d(a,b)
print(c)                            #----> [12 14]

print()
d=np.setdiff1d(b,a)
90098 
print(d)                            # ---> [21 34]yf4re

'''

# -----------------------------------------------------------------------------------------

# Indexing
# Slicing

'''
import numpy as np

x=np.array([100,200,300,400,500])

print("Array_Data------->",x)          #Array_Data-------> [100 200 300 400 500]
print()

print("Indexing----->", x[2])          #Indexing-----> 300
print()

print("Indexing----->", x[3])          #Indexing-----> 400
print()

print("Indexing----->", x[4])          #Indexing-----> 500
print()

print("Slicing----->", x[::])          #Slicing-----> [100 200 300 400 500]
print()

print("Slicing----->", x[:3:])         #Slicing-----> [100 200 300]
print()

print("Slicing----->", x[::2])         #Slicing-----> [100 300 500]
print()

print("2D ARRAY OPERATION")
print()

z=np.array([[1,2,3],[4,5,6]])
print("2D ARRAY---->", z)               #2D ARRAY----> [[1 2 3] [4 5 6]]
print()

print("Indexing---->",z[0][2])          #Indexing----> 3
print()

print("Indexing---->",z[0][0])          #Indexing----> 1
print()

print("Indexing---->",z[0][1])          #Indexing----> 2
print()

print("Slicing----->", z[0][::])        #Slicing-----> [1 2 3]
print()

print("Slicing----->", z[0][0])          #Slicing-----> 1
print()

print("Slicing----->", z[0][1])          #Slicing-----> 2
print()

print("Slicing----->", z[0][0:2:1])       #Slicing-----> [1 2]
print()

print("Slicing----->", z[1][0:2:1])        #Slicing-----> [4 5]
print()

print("Slicing----->", z[1][::])           #Slicing-----> [4 5 6]
 
''' 

# --------------------------------------------------------------------------

# Scalar Operation --------- Vector in 1D format  by using scalar operation and matrix present in 2D format

# addition
# substraction
# multiplication 
# dividion 
# floar division
# power
# modulus

''' 

import numpy as np
s=np.array([10,12,13,14,15])
print("Original Array---------->",s)      #Original Array----------> [10 12 13 14 15]
print()

res=s+5
print("Scalar_opr in addition -------->", res)                    #Scalar_opr in addition --------> [15 17 18 19 20]
print()

res=s-5
print("Scalar_opr in Substraction -------->", res)                #Scalar_opr in Substraction --------> [ 5  7  8  9 10]
print()

res=s*5
print("Scalar_opr in Multiplication -------->", res)              #Scalar_opr in Multiplication --------> [50 60 65 70 75]
print()

res=s/5
print("Scalar_opr in Division -------->", res)                    #Scalar_opr in Division --------> [2.  2.4 2.6 2.8 3. ]
print()

res=s//5
print("Scalar_opr in Floor_Division -------->", res)             #Scalar_opr in Floor_Division --------> [2 2 2 2 3] 
print()

res=s**5
print("Scalar_opr in Power -------->", res)                        #Scalar_opr in Power --------> [100000 248832 371293 537824 759375]

print()

res=s%5
print("Scalar_opr in modulas -------->", res)                     #Scalar_opr in modulas --------> [0 2 3 4 0]
'''

# 2D array called as Matrix --->

'''
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print("2D ARRAY----->",x)                      #2D ARRAY-----> [[1 2 3] [4 5 6]]

print()
y=np.array([[7,8,9],[10,11,12]])
print("2D ARRAY------>", y)                    #2D ARRAY------> [[ 7  8  9][10 11 12]]
print()

print("Addition-->",x+y)                       #Addition--> [[ 8 10 12][14 16 18]]
print()

print("Substarction -->",x-y)                  #Substarction --> [[-6 -6 -6][-6 -6 -6]]
print()

print("Multiplication-->",x*y)                 #Multiplication--> [[ 7 16 27][40 55 72]]
print()

print("Division-->",x/y)                       #Division--> [[0.14285714 0.25       0.33333333] [0.4        0.45454545 0.5       ]]
print()

print("Floor Division-->",x//y)                #Floor Division--> [[0 0 0] [0 0 0]]             
print()

print("Power-->",x**y)                         #Power--> [[         1        256      19683] [   1048576   48828125 2176782336]]

print()

print("Moduls-->",x%y)                         #Moduls--> [[1 2 3] [4 5 6]]

''' 

# import numpy as np

# x=np.array([[1,2,3],[4,5,6]])
# print("2D x ARRAY-----> ", x)                 #2D x ARRAY----->  [[1 2 3] [4 5 6]]
# print()
# y=np.array([[1,4,5],[2,5,3]])
# print("2D y ARRAY-----> ", y)                 #2D y ARRAY----->  [[1 4 5] [2 5 3]]
# print()

# print()



# dot()----------> using for multiplication 
# matmul()
# var1@var2

'''
import numpy as np

x=np.array([1,2,3])
print("1D x ARRAY-----> ", x)                 #1D x ARRAY----->  [1 2 3] 
print()
y=np.array([4,5,6])
print("1D y ARRAY-----> ", y)                 #1D y ARRAY----->  [4 5 6]
print()

print(np.dot(x,y))                            #--------> 32---> 1*4+2*5+3*6

print()
print(np.matmul(x,y))                         #--------> 32---> 1*4+2*5+3*6

print()
print(x@y)                                    #--------> 32---> 1*4+2*5+3*6


''' 
# Dot for 2 d array----> 1  st row multiply to 1st column of another  column then addition of all value
# 1st array 2nd row connect 2nd array 1st column again 2nd array

''' 
Rules --
Rule 1--> 1st array first row is connected to second array first column'
          First array first row is connected to second array second column.
Rule 2 -> First array second row is connected to second array first column,
          First array seconf row is coonected to seconf array second column.

'''

# import numpy as np

# a=np.array([[1,2],[4,5]])
# b=np.array([[6,7],[8,9]])

# print(" 2D a array---->", a)              # 2D a array----> [[1 2] [4 5]]
# print()
# print("2D b ARRAY------->", b)            #2D b ARRAY-------> [[6 7] [8 9]]
# print()
# print(np.dot(a,b))                        #[[22 25] [64 73]]--> (1*6)+(2*8)=22
# print()

# #[[22 25] [64 73]]--> (1*6)+(2*8)=22 , (4*6)+(5*7)=24+35=

# print()
# print(np.matmul(a,b))                      #[[22 25] [64 73]]

''' 
Comparison Function
equal()
not_equal()
greater()
greater_equal()
less()
less_equal()


 Random module-------
 randint()

'''
'''
import numpy as np

x=np.array([10,20,30,40,50])
y=np.array([15,25,30,40,60])

print("1D x Array-------->",x)            #1D x Array--------> [10 20 30 40 50]
print()
print("1D y Array------->",y)             #1D y Array-------> [15 25 30 40 60]
print()
print(x==y)                               #equals------->[False False  True  True False]---> using symbal
print()
z=np.equal(x,y)
print(z)                                  #equals------->[False False  True  True False]
print()
print("Greater----->",x>y)                #Greater----->[False False False False False]
print()
z=np.greater(x,y)
print(z)                                  #Greater----->[False False False False False]
print()
print("Greater than equal--->", x>=y)     #Greater than equal---> [False False  True  True False]
print()
z=np.greater_equal(x,y)
print(z)                                  #Greater than equal---> [False False  True  True False]
print()
print("Less--->",x<y)                     #Less---> [ True  True False False  True]
print()
z=np.less(x,y)
print("Less--->",z)                       #Less---> [ True  True False False  True]
print()
print("Less_equal---->",x<=y)             #Less_equal----> [ True  True  True  True  True]
print()
z=np.less_equal(x,y)
print("Less_equal----->",z)               #Less_equal-----> [ True  True  True  True  True]
print()
print("Not_Equals---->",x!=y)             #Not_Equals----> [ True  True False False  True]
print()
z=np.not_equal(x,y)
print("Not_Equals---->",z)                #Not_Equals----> [ True  True False False  True]
''' 
# All Method---> Whenever we are using all method all number should be postive then only it will return True, if we are using 0 or -ve it will return false
#  any method--> opposite to all method, any 1 number is positive it will return true

# all()---->

# import numpy as np

# x=np.array([10,20,30,40])
# print("1D Array--->",x)
# print()
# print(x.all())                   #True

# y=np.array([-10,0,2,4,3])
# print(y.all())                   #False


# Any()---->

# import numpy as np

# x=np.array([10,20,30,40])
# print("1D Array--->",x)
# print()
# print(x.any())                   #True

# y=np.array([-10,0,2,4,3])           
# print(y.any())                   #True
# print()
# z=np.array([0,-1,-2,-3])
# print(z.any())                   #True
# print()
# z=np.array([-1,-2,-3])
# print(z.any())

# Rand()

# import numpy as np

# x=np.array([10,20,30,40])
# print("1D Array--->",x)        #1D Array---> [10 20 30 40]
# print()

# n=np.random.rand(2,3)
# print(n)                       #[[0.25755918 0.4784699  0.9012555 ] [0.97880824 0.37279306 0.16329789]]
# print()

# n=np.random.random(2)
# print(n)                       #[0.5772149  0.88365023]
# print()

# Random module-----> To work on random modul we need to import random in it.

# types of random modul 
# randit()------> It is a type of random module 
# to parameters are use in randit low(included) and high(excluded), if we use size as 3rd parameter it will give []array output, Size we can pass as(2,2) row and column


# import numpy as np
# x=np.random.randint(1,5)
# print(x)                     #--> o/p random element in between 1-4

# import numpy as np
# x=np.random.randint(1,5,size=3)
# print(x)                            #--> [2 4 3]--> 1D array

# import numpy as np
# x=np.random.randint(1,5,(3,3))
# print(x)                             #--> 
# [2 3 1]
# [[3 4 3]
#  [1 3 1]
#  [1 3 3]]

# Rand()-->  It will always give the out put in positive

# import numpy as np
# y=np.random.rand()
# print(y)                          #-->0.39556064762427345
# print()

# y=np.random.rand(1,3)                
# print(y)                          #--> [[0.70670992 0.2137411  0.70079478]]

# print()

# y=np.random.rand(3,3)                
# print(y)

# o/p-->

# [[0.92074256 0.48447778 0.70387534]
#  [0.57822347 0.12758926 0.04463471]
#  [0.50644358 0.47959124 0.4556731 ]]

# Randn()--> Random out put
# integer

# import numpy as np
# z=np.random.randn()                    #---> if we don't pass any element in paranthesis it eill take it as 1 by default
# print(z)                               #--> -1.1730429169203496

# print()
# z1=np.random.randn(3,3)       #-->0/+ve/-ve
# print(z1)

# o/p-->
# [[ 0.66804881 -0.80195873  1.79802512]
#  [ 2.00429339  0.19461947  1.82641021]
#  [-0.54778226  0.12687215 -0.3948111 ]]

# Random()--> Inbetween 
# to print 2D it will give inner paranthesis ((,))

# import numpy as np
# s=np.random.random()
# print(s)                    #0.6794479856543292


# print()
# s1=np.random.random((2,2))     #--> it will accept 1 argument
# print(s1)

# o/p-->
# [[0.02041368 0.11668529]
#  [0.91142998 0.69655061]]


# uniform()-----> It will give output in decimal

'''
import numpy as np
a=np.random.uniform(1)
print(a)                       #--> 1.0

print()
a=np.random.uniform(1,5)       
print(a)                       #--> 2.670619201474988

print()

a=np.random.uniform(1,5,size=2)       
print(a)                        #--> [1.11244425 3.97391989]

print()
a=np.random.uniform(1,5,(2,2))       
print(a)          

# o/p-->
# [[3.63031757 2.60529924]
#  [3.37181544 3.48736522]]
''' 

# choice()--> amone specified elements it will take any random inbetween that elements
'''
import numpy as np

x=[10,20,4.1,True,40,30]
s=np.random.choice(x)
print(s)                     #--> 4.1

print()
s1=np.random.choice(x,3)
print(s1)                    #--> [20. 40. 30.]
print()

l=np.random.choice(x,(3,3))
print(l)

# o/p-->
# [[ 4.1 10.  10. ]
#  [ 4.1  4.1  1. ]
#  [10.  30.   1. ]]
'''

# Shuffle()---> however we print that variable it will shuffle the position every time

# import numpy as np

# x=[10,20,4.1,True,40,30]

# np.random.shuffle(x)        #--> if we print new_var it will give None as out put
# print(x)                    #--> [20, 4.1, 40, 10, True, 30]


# degree--> radian=degree*pay(TT)/180
# Radian output--> 0.5233333333333333 (30*pay/180)

# degree to radian 

# 0.523333*180/3.14(payvalue)             #30 degree o/p    #--> radian to degeer

# import numpy as np
# x=np.deg2rad(30)
# print(x)                                  #--> 0.5235987755982988
# print()

# y=np.rad2deg(x)                           #--> convert-->radiant to degree
# print(y)                                  #--> 29.999999999999996
# print()

# x=np.deg2rad(40)
# print(x)                                  #--> 0.6981317007977318
# print()
# y=np.rad2deg(x)                           #--> convert-->radiant to degree
# print(y)
# print()                                   #--> 40.0

# ----------------------------------------------------

# cor
# sin 
# cos

