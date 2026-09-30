'''
----> Panda is one of the open source library it will use anyone easily.
----> Working follow also easy
----> attribute error if we mention Pandas.py directlu=y for file 

----> step 1. Import
               |
               |
      Import pandas as pd    

to check current version 
import pandas 
print(pandas.__version__)            #Pandas.double_version_double 

--> 2nd way

import pandas as pd 
print(pd.__version__)

'''

# import pandas 
# print(pandas.__version__)              #2.3.1

# 2nd way to check version installed in system

# import pandas as pd 
# print(pd.__version__)                    #2.3.1

''' 
-------------------------Typaes of Pandas-------------------

1. series --> here we can create only one column
---> series is a 1D (Dimensional)
---> First letter should be Uppercase while using name Series ( if mention lowercase is will throe error)

---> syntax: 
New_var=pd.Series(iterable)

--> Table: Combination of Rows and Column
      |
      |
2. Data Frame--> To craete multiple rows and columns 
---> Combination of Series and Rows
---> Data Frame is a 2D(Dimensional)
'''

# import pandas as pd

# x=[100,200,300,400,500]                    #iterable--list is Collection data type

# y=pd.Series(x)                             #x=iterable name

# print(y)

# o/p:
# 0    100
# 1    200
# 2    300
# 3    400
# 4    500
# dtype: int64          --->   here int64 - shows Integer

# print(type(y))          #---> <class 'pandas.core.series.Series'>

# print(y.dtype)          #---> int64

''' To change the index Number of above column
syntax: 
index=[]

new_var=pd.Series(iterable_name,index=["char1","char2"...])


'''

# y=pd.Series(x,index=['a','b','c','d','e'])   
# print(y)

#o/p--->
# a    100
# b    200
# c    300
# d    400
# e    500
# dtype: int64

''' 
Type and dtype

1. type function---> It is a function.
It will give complete information about the table 

2. dtype--> 
It is a property
It will give information present inside the column

'''

# Now if we want to change column Name:

# To create column Name

''' 
syntax:

new_var=pd.Series(iterable_name,name="column_name")

'''
'''
import pandas as pd

x=[100,200,300,400,500]                    #iterable--list is Collection data type

y=pd.Series(x)                             #x=iterable name


y=pd.Series(x,index=['a','b','c','d','e'])   
y=pd.Series(x,)
'''

# | Name                    | Type     | Meaning / Definition             | Syntax                               | Example Output     |
# | ----------------------- | -------- | -------------------------------- | ------------------------------------ | ------------------ |
# | size                    | Property | Returns total number of elements | `print(var.size)`                    | `5`                |
# | shape                   | Property | Returns structure of Series      | `print(var.shape)`                   | `(5,)`             |
# | count()                 | Method   | Counts non-null values           | `print(var.count())`                 | `5`                |
# | type()                  | Function | Shows type of object             | `print(type(var))`                   | `<class 'Series'>` |
# | dtype                   | Property | Shows data type inside Series    | `print(var.dtype)`                   | `int64`            |
# | values                  | Property | Returns all values               | `print(var.values)`                  | `[10 20 30]`       |
# | ndim                    | Property | Returns dimension                | `print(var.ndim)`                    | `1`                |
# | index                   | Property | Returns index labels             | `print(var.index)`                   | `RangeIndex(...)`  |
# | name                    | Property | Returns Series name              | `print(var.name)`                    | `Marks`            |
# | is_unique               | Property | Checks all values unique or not  | `print(var.is_unique)`               | `True / False`     |
# | hasnans                 | Property | Checks missing values            | `print(var.hasnans)`                 | `True / False`     |
# | nbytes                  | Property | Returns memory used              | `print(var.nbytes)`                  | `40`               |
# | is_monotonic            | Property | Checks sorted order              | `print(var.is_monotonic)`            | `True / False`     |
# | is_monotonic_increasing | Property | Checks increasing order          | `print(var.is_monotonic_increasing)` | `True / False`     |
# | is_monotonic_decreasing | Property | Checks decreasing order          | `print(var.is_monotonic_decreasing)` | `True / False`     |
# | head()                  | Method   | Shows first 5 rows               | `print(var.head())`                  | First rows         |
# | tail()                  | Method   | Shows last 5 rows                | `print(var.tail())`                  | Last rows          |
# | sample()                | Method   | Returns random rows              | `print(var.sample(2))`               | Random values      |
# | nunique()               | Method   | Counts unique values             | `print(var.nunique())`               | `4`                |
# | value_counts()          | Method   | Counts frequency of values       | `print(var.value_counts())`          | Frequency table    |
# | empty                   | Property | Checks if Series is empty        | `print(var.empty)`                   | `True / False`     |


# sort--> 
# Properties → size, shape, dtype, index, name, values, ndim, is_unique, hasnans, nbytes, is_monotonic, is_monotonic_increasing, is_monotonic_decreasing, empty

# Functions/Methods → type(), count(), head(), tail(), sample(), nunique(), value_counts()

# to check size:
# is a property.. how many elements are present in the column for that we use size property
# syntax:
# print(new_var.size)

# Shape: To check shape:
# -- it will give the output in the form of tuple as (no. of rows, column)

# syntax:
# print(new_var.shape)

#Count:
# ---Count is a method 
# -- it will give the no. of elements present in the column
# print(new_var.count())

# value count:
# -- It will display hoe many times the elements are repeated
# print(new_var.value_count())

# print(y.value_count())


# ndim--> it is a property 
# print(new_var.ndim)

# ---------------------------------------------------------------------------------------------
# Example

# import pandas as pd

# x=[10,20,30,40,50,60]

# data=pd.Series(x)

# print(data)

# o/p-
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# 5    60
# dtype: int64

# print(type(data))                 #o/p-<class 'pandas.core.series.Series'>

# data=pd.Series(x,index=['a','b','c','d','e','f'])

# print(data)

# o/p:
# a    10
# b    20
# c    30
# d    40
# e    50
# f    60
# dtype: int64

# data=pd.Series(x,index=['P','Q','R','S','T','U'],name='Number')
# print(data)

# o/p:
# P    10
# Q    20
# R    30
# S    40
# T    50
# U    60
# Name: Number, dtype: int64>

# print("Size",data.size)                         #Size 6

# print("Shape",data.shape)                       #Shape (6,)

# print("dtype",data.dtype)                       #dtype int64

# print("Count",data.count)                       #Count <bound method Series.count of P 

# print("Ndim",data.ndim)                         #Ndim 1

# print("Values",data.values)                     #Values [10 20 30 40 50 60]

# print(type(data))                               #<class 'pandas.core.series.Series'>

# ----------------------------------------------------------------------------------

# import pandas as pd

# x=pd.Series([11,12,13,14],name='Marks')

# print(x)
# print(x.index)                      #index - Return the index(lables) of the series

# o/p:RangeIndex(start=0, stop=4, step=1)

# print(x.name)                        #None

# o/p-
# 0    11
# 1    12
# 2    13
# 3    14
# Name: Marks, dtype: int64
# RangeIndex(start=0, stop=4, step=1)

# --------------------------EMPTY-----------------------

# import pandas as pd

# y=pd.Series([])

# print(y.empty)                  #o/p-True


# import pandas as pd

# y=pd.Series([1])

# print(y.empty)                     #o/p-False     

# ---------------------------------UNIQUE-------------------------------------

# import pandas as pd 

# y=pd.Series([1,2,3,4])

# print(y)
# print(y.is_unique)                  

# o/p-
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
# True

# -------------------------Hasnans----------------
# is a property is used when  the series contain any none value or missing values the o/p should be true, else False

# import pandas as pd 

# y=pd.Series([1,2,3,4])

# print(y)

# print(y.hasnans)


# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
# False


# import pandas as pd 

# y=pd.Series([1,None,3,None,5,6])

# print(y)

# print(y.hasnans)

# 0    1.0
# 1    NaN
# 2    3.0
# 3    NaN
# 4    5.0
# 5    6.0
# dtype: float64
# True

# -----------------------------------nbytes------
# how much the memory that series takes

# import pandas as pd 

# y=pd.Series([1,2,3,4])

# print(y)

# print()

# print("nbytes",y.nbytes)                             #nbytes 32 (1----> 8bytes)

# ----------------------------is_monotonic----------------
# is_monotonic_increasing----
# is_monotonic_decreasing----

# import pandas as pd 

# y=pd.Series([10,15,20,25,30])

# print(y)

# print()

# print(y.is_monotonic_increasing)

# o/p--

# 0    10
# 1    15
# 2    20
# 3    25
# 4    30
# dtype: int64

# True


# import pandas as pd 

# y=pd.Series([10,15,11,25,30])

# print(y)

# print()

# print(y.is_monotonic_increasing)

# o/p--
# 0    10
# 1    15
# 2    11
# 3    25
# 4    30
# dtype: int64

# False

# import pandas as pd 

# y=pd.Series([30,20,10])

# print(y)

# print()

# print(y.is_monotonic_decreasing)

# o/p--
# 0    30
# 1    20
# 2    10
# dtype: int64

# True

# import pandas as pd 

# y=pd.Series([30,11,5,20,10,1])

# print(y)

# print()

# print(y.is_monotonic_decreasing)

# o/p--
# 0    30
# 1    11
# 2     5
# 3    20
# 4    10
# 5     1
# dtype: int64

# False


# ---------------------------------head------------------------
# withount passing head()--- by default it show 5 rows head
# print(var_name.head())
# print(var_name.head(Numberofrows))

# import pandas as pd

# x=pd.Series([10,20,30,40,50,60,70,80,90,10])

# print(x)

# # print(x.head())

# print(x.head(10))

# ---------------------------tail-----------------------------
# print(var_name.tail())--- by default is show tail 5 rows
# print(var_name.tail(numberofrows))

# import pandas as pd

# x=pd.Series([10,20,30,40,50,60,70,80,90,10])

# print(x)

# print(x.tail())

# print(x.tail(10))

# o/p-
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# 5    60
# 6    70
# 7    80
# 8    90
# 9    10
# dtype: int64

# -------------------------------------sample()----------------------------------------
# working randomly (not as head or tail)
# if not pass anything it will show 1  1 row 
# if pass 2 it ramdomly show 2 rows

# import pandas as pd

# x=pd.Series([10,20,30,40,50,60,70,80,90,10])

# print(x)

# print()

# print(x.sample())                         #3    40  dtype: int64

# print(x.sample(4))   

# o/p:
# 9    10
# 6    70
# 0    10
# 8    90
# dtype: int64


# unique

# import pandas as pd

# x=pd.Series([10,20,30,40,50,60,70,80,90,10])

# print(x)

# print()

# print(x.unique())                   #[10 20 30 40 50 60 70 80 90]


#unique on duplicate 

# import pandas as pd

# x=pd.Series([10,20,10,40,20,60,50,80,90,10])

# print(x)

# print()

# print(x.unique())                      #[10 20 40 60 50 80 90]


# ----------------n_unique------------

# import pandas as pd

# x=pd.Series([10,20,10,40,20,60,50,80,90,10])

# print(x)

# print()

# print(x.nunique())                       #7

# import pandas as pd

# x=pd.Series([10,20,30,40,50,60,70,80,90,100])

# print(x)

# print()

# print("count_unique",x.nunique())                    #count_unique 10


# ------------------------------values count-----------------------------------

# import pandas as pd

# x=pd.Series([10,20,30,40,50,60,70,80,90,100])

# print(x)

# print()

# print("Values",x.values)                      #Values [ 10  20  30  40  50  60  70  80  90 100]

# import pandas as pd 

# x=pd.Series([10,20,10,40,20,80,80,80,90,100])

# print(x.value_counts())

''' 
import pandas as pd 
x=pd.Series((1,2,3,4,5,6),index=['a','b','c','d','e','f'],name='Series')
print(x)
print()
print("SIZE",x.size)
print()
print("SHAPE",x.shape)
print()
print('values',x.values)
print()
print("index",x.index)
print()
print("dtype",x.dtype)
print()
print("Name",x.name)
print()
print("Unique",x,x.is_unique)
print()
print("unique",x.unique)
print()
print("Count",x.count)
print()
print("Hasanan",x.hasnans)
print()
print("Empty",x.empty)
print()
print("NDIM",x.ndim) 
print()
print("NBYTE",x.nbytes)
print()
print("type",type(x))
print()
print("Count",x.count())
print()
print("VALUE_COUNT",x.value_counts())
print()
print("Head",x.head())
print()
print("Head",x.head(3))
print()
print("Tail",x.tail())
print()
print("Tail", x.tail(3))
print()
print("Increasing",x.is_monotonic_increasing)
print()
print("Decrising", x.is_monotonic_decreasing)
print()
print("Sample",x.sample())
print()
print("Sample",x.sample(3))

'''
'''
sort_values()
sort_index()
max()
min()
sum()
mean()
median()
mode()
idmax()
idmin()
astype()

'''
'''
import pandas as pd

x=pd.Series([11,4,7,2,3,1,15,6])

print(x)

print()

print(x.sort_values())                         #ascending=True ------>A------>D

# # o/p:
# 5     1
# 3     2
# 4     3
# 1     4
# 7     6
# 2     7
# 0    11
# 6    15
# dtype: int64

print()

print(x.sort_values(ascending=False))        #desending ------->ascending

# o/p:
# 6    15
# 0    11
# 2     7
# 7     6
# 1     4
# 4     3
# 3     2
# 5     1
# dtype: int64

'''  

# import pandas as pd

# y=pd.Series([11,12,13,14])

# print(y)

# 0    11
# 1    12
# 2    13
# 3    14
# dtype: int64

# print()

# print(y.sort_index())                  #not change previous output

# 0    11
# 1    12
# 2    13
# 3    14
# dtype: int64


# import pandas as pd
# y=pd.Series([11,12,13,14],index=[3,1,0,2])

# print(y)

# 3    11
# 1    12
# 0    13
# 2    14
# dtype: int64

# print()

# print(y.sort_index())

# 0    13
# 1    12
# 2    14
# 3    11
# dtype: int64

# print(y.sort_index(ascending=False))

# 3    11
# 2    14
# 1    12
# 0    13
# dtype: int64


# import pandas as pd

# y=pd.Series([11,12,13,14,15])

# print(y)

# print()

# print("max", y.max())                                  #max 15

# print()

# print("min",y.min())                                   #min 11

# print()

# print("Sum",y.sum())                                  #Sum 65

# print()

# print("mean",y.mean())                                #mean 13.0

# ------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

''' 
import pandas as pd

e=pd.Series([11,7,13,1,2,14,3])

print(e)
print()
print(e.median())        #sort_list=[1,2,3,7,11,12,13]   #0/0---> 7.0

'''

# import pandas as pd

# x=pd.Series([10,20,30,40])

# print(x)

# print()

# print("median",x.median())               #20+30/2   #median 25.0       #median always use sorted list if list not sorted internally median convert the list then give median value

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# mode---------> display repeted elements frequently, if no element repeated complete column will display ascending to descending

# import pandas as pd

# s=pd.Series([10,20,10,20,30,40])

# print(s.mode())

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
''' 
idxmax & idxmin----> it show max element index number and min element index number

import pandas as pd
              0   1   2   3   4
a=pd.Series([100,200,500,250,70])

print(a)
print(a.idxmax())   #2
print(a.idxmin())   #4

'''
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# astype----> used to convert 1 data type to another data type print(n_var.astype("datatype"))

# import pandas as pd

# x=pd.Series([100,200,500,250,70])

# print(x)

# print(x.astype("float"))
# print(x.astype("complex"))
# print(x.astype("bool"))

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Drop----> to delete the specific number from the list mention the index number of that element print(n_var.drop(number))

# import pandas as pd

# x=pd.Series([100,200,500,250,70])
# print(x.drop(2))

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# pop-----> to delete the element from the element and return type delete element

# import pandas as pd

# x=pd.Series([100,200,500,250,70])

# print(x.pop(0))                #100


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# del----->in series if we want to delete any row thier is 3 way drop(position), pop(position),  and del variable[position]

# import pandas as pd

# x=pd.Series([100,200,500,250,70])

# del x[3]

# print(x)

# o/p-

# 0    100
# 1    200
# 2    500
# 4     70
# dtype: int64

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# fillna() ----> to fill the empty space in a given list , it will accept 1 argument, it will arrange/replace same 
# number at all empty space, to replace different values at different place use dictionary fillna{k:v} in key part mention index position & value part mention value 

# import pandas as pd

# d=pd.Series([10, None, 60, None, 80])

# print(d)

# o/p-->
# 0    10.0
# 1     NaN
# 2    60.0
# 3     NaN
# 4    80.0
# dtype: float64

# print()
# print(d.fillna("*"))

# o/p--->
# 0    10.0
# 1       *
# 2    60.0
# 3       *
# 4    80.0
# dtype: object

# print(d.fillna({1:1000,3:"#"}))

# 0    10.0
# 1    1000
# 2    60.0
# 3       #
# 4    80.0
# dtype: object

# dropna---------->to delete/remove none value

# print(d.dropna())

# 0    10.0
# 2    60.0
# 4    80.0
# dtype: float64


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# duplicated()) ----> if duplicate elements are present in list it show True at 2nd accurance, 
# if we need to set duplicate 1 st accurance 

# import pandas as pd
#          #    f  f  f  t  f  f  t  f  t
# c=pd.Series([11,12,10,11,13,20,11,21,13])

# print(c.duplicated())

# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5    False
# 6     True
# 7    False
# 8     True
# dtype: bool

# print(c.duplicated(keep="first"))            # first accurance 

# print(c.duplicated(keep="last"))              #by default it give we not mention keep="last" 


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------


# import pandas as pd

# s=pd.Series([1,2,3,1,2,3])

# print(s.duplicated(keep="first"))
# print(s.duplicated(keep="last"))

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# drop_duplicate---> delete the duplicate element depending on first accurance and last/ second accurance

# import pandas as pd

# s=pd.Series([1,2,3,1,2,3])

# print(s.drop_duplicates(keep="first"))                  #it delete sencond/last accurance

# print(s.drop_duplicates(keep="last"))                    # it keep last/ second and delete first 

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------


# Replace----> replace the present value with new value for single value , for replace multiple values use dictionary 

# import pandas as pd

# l=pd.Series([1,2,3,4,5])

# print(l.replace(2,'hiii'))                   #single value replace 
# print(l.replace({3:300,5:500,1:"hii"}))    #multivalue replace


#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# index rename-----> rename the selected index position 

# import pandas as pd

# l=pd.Series([1,2,3,4,5])

# print(l.rename({0:"a",4:400}))

#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# between---> 

# import pandas as pd

# x=pd.Series()

#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# 22/05/2026--->

# max 2 largest number----new_var.nlargerst(number)  if we not pass anything it will consider by default 5 rows 
# 1. nlargest (number) 
# 2. nsmallest (number)
# 3. take([position])                 #take only accept position or numbers , it won't accept character like 'a','b'
# 4. get()
# 5. indexing (only single index can pass) , if pass multiple it show keyerror
# 6. slicing(variable[startvalue:endvalue+1:stepvalue])
# 7. LOC[poaition]   --> work only on position loc[si:ei:sv]  --> endindex in loc included
# 8. iloc[si:ei+1:sv]
# 9. isnull()--> True if none value is present , else false
# 10. notnull() --> True if value should be present not none
# 11. where(condition,default value) --> wherever condition is satisfied only that number display, other all show NaN, in place of NaN we can pass Defualt value also
# 12. mask() --> opposite to where
# 13. info()--> Complete information of table
# 14. describe()--> it jst describe complete calculation
# 15. cumsum()-->
# 16. cumprod() -->



# import pandas as pd

# z=pd.Series([100,70,200,300,400,11,3])

# print(z.nlargest(2))                                 # 400 300

# print()

# print(z.nsmallest(3))                                # 3  11  70

# print(z.take([3]))                                     #single row by take method

# print(z.take([2,0,6]))                                   #for multiple rows 

# print(z[0])                                               # indexing

# print(z[0:4+1:2])                                          #slicing

# print(z.get(0))                                             #get

# print(z.get([0]))                                             #get [] also work

# print(z.get([0,2,4]))                                            #multiple also work

#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------


# import pandas as pd

# y=pd.Series([11,12,13],index=['a','b','c'])

# print(y)

# print()
# print(y.take(['a']))                     #won't support ERROR
# print(y.take([0]))

# print(y.get(['x','key not found']))                #None

# print(y.get('x','key not found'))                    #key not found

# print(y.loc(1))                                       #not work, use []

# print(y.iloc('a'))                                    # #not work use []

# print(y.loc['a'])                                     #working 11      #fetch single element

# print(y.iloc[0:2+1:1])                                         #fetching multiple elements

# print(y.iloc['a'])                       #only work on position or numbers not characters like 'a' , #TypeError: Cannot index by location index with a non-integer key


#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# import pandas as pd

# p=pd.Series([300,100,200,400])

# print(p.isnull())

# print()

# import pandas as pd

# p=pd.Series([300,100,None, 200, None,400, None])

# print(p.isnull())

# print()

# import pandas as pd

# p=pd.Series([300,100,200,400])

# print(p.notnull())

# print()

# import pandas as pd

# p=pd.Series([300,100,None, 200, None,400, None])

# print(p.notnull())


#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# import pandas as pd

# x=pd.Series([10,20,30,40,50])

# print(x.where(x>30,0))                         # 0 is a default value to avoid NaN  O/P--> NaN NaN NaN 40 50 / 0 0 0 40 50

# print(x.mask(x>30))                          # opposite to where o/p---> 10 20 30 NaN NaN


#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# info() -->

# import pandas as pd

# p=pd.Series([300,100,200,400])

# print(p)

# print()

# print(p.tolist())                      #[300, 100, 200, 400]

# print(p.info())

# o/p-->
#  4 non-null      int64
# dtypes: int64(1)
# memory usage: 164.0 bytes
# None                                # none due to use print function use it without print

#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# describe--> it describe only calculate column / number data

# import pandas as pd

# p=pd.Series([300,100,200,400])

# print(p.describe())

# o/p-->
# count      4.000000
# mean     250.000000
# std      129.099445
# min      100.000000
# 25%      175.000000
# 50%      250.000000
# 75%      325.000000
# max      400.000000
# dtype: float64

#  -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# cumsum()--> start number print as it is next number will added to previous number
# cumprod()--> start 1st number as it is print next number multiply with previous one 

# import pandas as pd
# x=pd.Series([1,2,3,4,5])
# print(x)

# o/p--> 
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# print()
# print(x.cumsum()) 

# o/p-->
# 0     1
# 1     3
# 2     6
# 3    10
# 4    15
# dtype: int64

# print()
# print(x.cumprod())

# o/p-->

# 0      1
# 1      2
# 2      6
# 3     24
# 4    120
# dtype: int64

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# sum(), prod(), cumsum(), cumprod()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# additionscalar()
# addition()
# substraction()
# multiplication()
# devision()

# import pandas as pd

# x=pd.Series([1,2,3])
# y=pd.Series([2,3,4])

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# T()
# axes() ---> [Range]

# import pandas as pd
# x=pd.Series([1,2,3,4,5])
# print(x.index)                 #RangeIndex(start=0, stop=5, step=1)
# print(x.axes)                  #[RangeIndex(start=0, stop=5, step=1)]


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# import pandas as pd
# x=pd.Series([1,2,3,4,5])

# print(x.T)                         #won't trasfer row to column and column to row coz series is 1 dimensional 


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# DATAFRAME
# import pandas as pd
# x=pd.DataFrame({"Name":["A","B","C","D"], "Age":[20,24,22,35]})
# print(x)
# print()
# print(x.T())

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

#DATAFRAME :(2 dimensional data structure)
# combination of series and rows
# combination of columns and rows

#in single we cant store data but in dataframe we can store data in rows and columns
# we can store data in the form of list, dict, series, array, tuple

#how to create dataframe:
#1) dictionary
#2) list


#import pandas as pd
#new_variable = pd.DataFrame(dictionary) #empty dataframe

'''
import pandas as pd
#creating dataframe using dictionary
data = {"name": ["sachin", "virat", "dhoni"],   
        "age": [45, 35, 40], 
        "country": ["india", "india", "india"]}
df = pd.DataFrame(data)
print(df)'''

#OR

'''import pandas as pd

name=['shrey','ram','atharva']
age=[20,21,22]
country=['india','india','india']

details = {"Name": name, "Age": age, "Country": country}
df = pd.DataFrame(details)
print(df)'''

#OR
#LIST : we pass row wise 
'''
import pandas as pd
y=pd.DataFrame([["shrey",20,"india"],["ram",21,"india"],["atharva",22,"india"]],columns=["Name","Age","Country"])
print(y)'''


'''import pandas as pd
x=pd.DataFrame([["python",100,'d',70],["java",80,'c',60],["c++",90,'c++',80]],columns=["Language","Marks","Grade","Percentage"])
print(x)'''

#-----------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# x=pd.DataFrame([["python","sql","javascript","A",95],["java","sql","javascript","B",85],["c++","sql","javascript","C",75],["excel","sql","javascript","D",65]],columns=["Subject1","Subject2","Subject3","Grade","Percentage"])
# print(x)

#shape:
# print(x.shape) #4 rows and 5 columns
# print(x.ndim) #2 dimensional
# print(x.size) #20 values (total number of values in the dataframe)
# print(x.columns) #column names (index values)
# print(x.index) #index values (range of index values)
# print(x.axes) #index and column names(form of list)
# print(x.dtypes) #data types of each column
# print(x.T) #transpose of dataframe (swap rows and columns)
# print(x.empty) #check if dataframe is empty (False means not empty)
# print(x.values) #values of dataframe in form of array


#methods:
# print(x.head(2)) #first 5 rows of dataframe (top to bottom)+
# print()
# print(x.tail(2)) #last 5 rows of dataframe (bottom to top)
# print()
# print(x.sample()) #random row from dataframe
# print()
# print(x.sample(2)) #random 2 rows from dataframe
# print()
# print(x.describe()) #statistical summary of numerical columns (count, mean, std, min, 25%, 50%, 75%, max)
# print(x.describe(include="object")) #statistical summary of categorical columns (count, unique, top, freq) #check only character columns
# print(x.describe(include="all")) #statistical summary of all columns (numerical and categorical)#both numerical and categorical columns
# print()
#x.info() #summary of dataframe (data types, non null values, memory usage)
#print()

#understanding loc(stop index inclued and start index included)
# print(x.loc[2]) #rows from index 0 to 2 (stop index included) #particular row
# print()
#print(x.loc[2, "Subject3"]) #particular value from particular row --> syntax : (dataframe.loc[row index, column name])
#print()
#print(x.loc[0:2]) #rows from index 0 to 2 (stop index included) #multiple rows
#print()
#print(x.loc[0:2, "Subject1"]) #particular column from particular rows
#print()
#print(x.loc[:, "Subject1"]) #particular columns from particular rows
# print(x.loc[:, "Subject1":"Subject2"]) #particular column from all rows
#print()


''' 
understanding Loc(stop index included)
******************************************
data_frame.loc[row_number]
data_frame.loc[row_number,[column_name,,,,,,]]
data_frame.loc[start:stop]
data_frame.loc[start:stop,"column_name"]
data_frame.loc[start:stop,["column_1,column_2...."]]
data_frame.loc[start:stop,"column_1":"column_n"] 
fetch single column single list --- v_N=["C_N"]
fetch multiple column multiple list --- V_n=[["C_N","C_N"]]
''' 
''' 
understanding iloc(stop index excluded)
****************************************************
data_frame.iloc[row_number,column_number]
data_frame.iloc[row_start:row_stop,col_start:col_stop]
data_frame.iloc[start:stop,column_number]
data_frame.iloc[[row_1,row_2,......]]

''' 


# import pandas as pd
# x=pd.DataFrame([["A",21,10000,"A-1"],["B",23,25000,"B-2"],["C",28,7600,"C-3"],["D",33,22000,"D-4"],["E",21,29800,"E-5"]],columns=["Name","age","sal","batch"])
# print(x)

#   Name  age    sal batch
# 0    A   21  10000   A-1
# 1    B   23  25000   B-2
# 2    C   28   7600   C-3


# print(x.iloc[2])

# Name        C
# age        28
# sal      7600
# batch     C-3
# Name: 2, dtype: object

# print(x.iloc[0,2])

# print(x.loc[0:2:1])                      #loc[st:ei:sv] ---ei--->included
# print(x.loc[0:2:1,["age"]])                 #loc[[st:ei:sv],[column_name/column_no]]

# print(x.iloc[[0:2:1]])**                     #iloc[st:ei+1:sv] ---ei--->excluded

# print(x.iloc[0:2:1],[0])                   #iloc=[st:ei+1:sv],[column_number]]

##################
# slicing  by rows as well as columns

# data_frame.iloc[row_start:row_stop,col_start:col_stop]
# data_frame.loc[row_start:row_stop,col_start:col_name]

# print(x)
# print(x.loc[0:3:1,"Name":"sal"])


# ----------------------------------------------------------------------------------------


# import pandas as pd
# x=pd.DataFrame([["A",21,10000,"A-1"],["B",23,25000,"B-2"],["C",28,7600,"C-3"],["D",33,22000,"D-4"],["E",21,29800,"E-5"]],columns=["Name","age","sal","batch"])
# print(x)

# o/p-->
#   Name  age    sal batch
# 0    A   21  10000   A-1
# 1    B   23  25000   B-2
# 2    C   28   7600   C-3
# 3    D   33  22000   D-4
# 4    E   21  29800   E-5

# print(x.iloc[2,3])***************not working


# import pandas as pd
# data=pd.DataFrame([["A",21,10000,"A-1"],["B",23,25000,"B-2"],["C",28,7600,"C-3"],["D",33,22000,"D-4"]],columns=["Name","age","sal","batch"])
# print(data)

# o/p-->
#     Name age  sal   batch
# 0    A   21  10000   A-1
# 1    B   23  25000   B-2
# 2    C   28   7600   C-3
# 3    D   33  22000   D-4

#add the row ---> V_N.loc[Row_number]=["column1","column2",..........]
# data.loc[4]=["E",26,23440,"E-5"]       #add the row
# print(data)

# o/p-->
#   Name  age    sal batch
# 0    A   21  10000   A-1
# 1    B   23  25000   B-2
# 2    C   28   7600   C-3
# 3    D   33  22000   D-4
# 4    E   26  23440   E-5


# ------------create a new column in existing one , add new column in existing table

# data["Total"]=True
# print(data)

# ----Var_name[['Col1','Col2','Col3']]=[default_value,default]------->CREATE MULTIPLE COLUMNS / ADD MULTIPLE COLUMNS -->

# data[["Total1","Total2","Total3"]]=[10,2,300]
# print(data)


#   Name  age    sal batch  Total1  Total2  Total3
# 0    A   21  10000   A-1      10       2     300
# 1    B   23  25000   B-2      10       2     300
# 2    C   28   7600   C-3      10       2     300
# 3    D   33  22000   D-4      10       2     300

# Adding column by in build method
# ------Assign_method   
#  Var_Name.assign(Column_name[value1.value2....])
# print(data.assign(y1=[10,20,30,40],y2=['a','b','c','d']))
#
# # o/p-->
#   Name  age    sal batch  y1 y2
# 0    A   21  10000   A-1  10  a
# 1    B   23  25000   B-2  20  b
# 2    C   28   7600   C-3  30  c
# 3    D   33  22000   D-4  40  d

#adding column at a specific coulmn postion  #ex--> add column after Name column 
# Var_name("column_name/position",(position,col_name,value))
# data.insert(1,"Loc",("pune","mumbai","delhi","pune"))
# print(data)
# -----------------------------------------------------------------------------------------------------------

# import pandas as pd

# Student_name=["Joy","Max",None,"Kiran",None]
# marks=[None,70,80,None,90]
# Sub=["pyhton",None,"SQL",None,"PowerBI"]

# tab=pd.DataFrame({"Nmae":Student_name,"Marks":marks,"Sub_name":Sub})
# print(tab)

# o/p-->     
#      Nmae  Marks Sub_name
# 0    Joy    NaN   pyhton
# 1    Max   70.0     None
# 2   None   80.0      SQL
# 3  Kiran    NaN     None
# 4   None   90.0  PowerBI

#fillna

# ffill()--> Forward fill (Top--  bottomn)
# dfill()--> Backword fill (Bottom -- top)

# print(tab.ffill())

# o/p-->
#     Nmae  Marks Sub_name
# 0    Joy    NaN   pyhton
# 1    Max   70.0   pyhton
# 2    Max   80.0      SQL
# 3  Kiran   80.0      SQL
# 4  Kiran   90.0  PowerBI

# print(tab.bfill())

# # o/p-->
#     Nmae  Marks Sub_name
# 0    Joy   70.0   pyhton
# 1    Max   70.0      SQL
# 2  Kiran   80.0      SQL
# 3  Kiran   90.0  PowerBI
# 4   None   90.0  PowerBI

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# import pandas as pd

# Student_name=["Joy","Max",None,"Kiran",None]
# marks=[None,70,80,None,90]
# Sub=["pyhton",None,"SQL",None,"PowerBI"]

# tab=pd.DataFrame({"Nmae":Student_name,"Marks":marks,"Sub_name":Sub})
# print(tab)

# o/p->
#     Nmae  Marks Sub_name
# 0    Joy    NaN   pyhton
# 1    Max   70.0     None
# 2   None   80.0      SQL
# 3  Kiran    NaN     None
# 4   None   90.0  PowerBI

# print()
# print(tab.ffill(axis=1))            #axis=1(-----> (work like wise row move(left to right)))

# o/p-->
#     Nmae  Marks Sub_name
# 0    Joy    Joy   pyhton
# 1    Max   70.0     70.0
# 2   None   80.0      SQL
# 3  Kiran  Kiran    Kiran
# 4   None   90.0  PowerBI

# print()
# print(tab.bfill(axis=1))         #axis=1(<----- (work like wise row moving right to left))

# o/p-->

#     Nmae   Marks  Sub_name
# 0    Joy  pyhton   pyhton
# 1    Max    70.0     None
# 2   80.0    80.0      SQL
# 3  Kiran    None     None
# 4   90.0    90.0   PowerBI

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Rename--> To rename the column
# var_name.rename(column={"Name":"N1"}) -------------> single
# var_name.rename(column={"old":"New","old":"New", "old":"New",...... })

# import pandas as pd

# Student_name=["Joy","Max",None,"Kiran",None]
# marks=[None,70,80,None,90]
# Sub=["pyhton",None,"SQL",None,"PowerBI"]

# x=pd.DataFrame({"Name":Student_name,"Marks":marks,"Sub_name":Sub})
# print(x)


# print()
# Rename--> To rename the column
# print(x.rename(columns={"Name":"N1","Marks":"A1"}))

# print()

# rename the index 
# print(x.rename(index={0:"A",3:900}))

#       Name  Marks Sub_name
# A      Joy    NaN   pyhton
# 1      Max   70.0     None
# 2     None   80.0      SQL
# 900  Kiran    NaN     None
# 4     None   90.0  PowerBI

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Drop--- remove rows as well as remove columns
# var_n.drop(row number)
# inplace=True----> modification permanantly , always show updated
# inplace=Flase--> modification temprary , show previous one
# labels , axis=1
# import pandas as pd

# df={"Name":["A","B","C","D"], "Age":[22,20,25,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# o/p-->
#   Name  Age    Sal
# 0    A   22  20000
# 1    B   20  30000
# 2    C   25  22000
# 3    D   38  40000

# print()

# print(x.drop([1,2]))                      

# o/p-->
#   Name  Age    Sal
# 0    A   22  20000
# 3    D   38  40000

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Sort_values()---> 

# import pandas as pd

# df={"Name":["A","B","C","D"], "Age":[22,20,25,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)
# print()

# print(x["Age"].sort_values())

# o/p-->
# 1    20
# 0    22
# 2    25
# 3    38
# Name: Age, dtype: int64

# print()


# print(x["Sal"].sort_values())

# o/p-->
# 0    20000
# 2    22000
# 1    30000
# 3    40000
# Name: Sal, dtype: int64

# print()

#sorting multiple columns
# print(x.sort_values(by=["Name","Age"],ascending=[0,1]))                   #0--> for Name column, 1--> for Age

# o/p-->
#   Name  Age    Sal
# 3    D   38  40000
# 2    C   25  22000
# 1    B   20  30000
# 0    A   22  20000

# print(x.sort_values(by=["Name","Age"],ascending=[1,0]))                     #opposite

# o/p-->
#   Name  Age    Sal
# 0    A   22  20000
# 1    B   20  30000
# 2    C   25  22000
# 3    D   38  40000

# ---------------------------------------------------------------------------------------

# import pandas as pd

# df={"Name":["A","B","C","D"], "Age":[22,20,25,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# print()

# print(x.isnull())

# o/p-->
#     Name    Age    Sal
# 0  False  False  False
# 1  False  False  False
# 2  False  False  False
# 3  False  False  False

# print()

# print(x.notnull())                      #no null value ---> if not none value is present-- show TRUE

# o/p-->

#    Name   Age   Sal
# 0  True  True  True
# 1  True  True  True
# 2  True  True  True
# 3  True  True  True

# -------------------------------------

# import pandas as pd

# df={"Name":["A","B","C","D"], "Age":[22,20,None,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# print()
# print(x.isnull())

# o/p-->

#     Name    Age    Sal
# 0  False  False  False
# 1  False  False  False
# 2  False   True  False
# 3  False  False  False


# Dropna---> remove whole row if none value is present in row 
# print(x.dropna())

#   Name   Age    Sal
# 0    A  22.0  20000
# 1    B  20.0  30000
# 3    D  38.0  40000


# -----------------------------------------------------------

# import pandas as pd

# df={"Name":["A","A","C","D"], "Age":[22,20,None,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# o/p--> 
#    Name   Age    Sal
# 0    A  22.0  20000
# 1    A  20.0  30000
# 2    C   NaN  22000
# 3    D  38.0  40000

# print()

# print(x["Name"])

# o/p-->
# 0    A
# 1    A
# 2    C
# 3    D
# Name: Name, dtype: object

# print()

#VALUES_COUNT()----> count the no of element present in a table

# print(x["Name"].value_counts())

# o/p-->

#     Name
# A    2
# C    1
# D    1
# Name: count, dtype: int64

# print()
# unique()
# print(x["Name"].unique())             #o/p-->['A' 'C' 'D']

# print()
# nunique()

# print(x["Name"].nunique())              #o/p--> 3


# ------------------------------------------------------------

# astype()--->Datatype change like int to float

# import pandas as pd

# df={"Name":["A","A","C","D"], "Age":[22,20,None,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# print()

# print(x.astype({"Age":float,"Sal":complex,"Name":bool}))

# o/p-->
#    Name   Age               Sal
# 0  True  22.0  20000.0+    0.0j
# 1  True  20.0  30000.0+    0.0j
# 2  True   NaN  22000.0+    0.0j
# 3  True  38.0  40000.0+    0.0j

# ---------------------------------------------------------------------------------
# Replace ----> To replace the element

# import pandas as pd

# df={"Name":["A","A","C","D"], "Age":[22,20,None,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# print()

# print(x.replace({30000:15000}))

# o/p->
#   Name   Age    Sal
# 0    A  22.0  20000
# 1    A  20.0  15000
# 2    C   NaN  22000
# 3    D  38.0  40000

# print()

# print(x.replace({"C":"python",22:11}))

# o/p-->

#      Name   Age    Sal
# 0       A  11.0  20000
# 1       A  20.0  30000
# 2  python   NaN  22000
# 3       D  38.0  40000

# ------------------------------------------------

# Duplicate()--> fetch duplicate element

# import pandas as pd

# df={"Name":["A","A","C","D"], "Age":[22,20,None,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# print()

# print(x["Name"])

# o/p-->

# 0    A
# 1    A
# 2    C
# 3    D
# Name: Name, dtype: object

# print()

# print(x["Name"].duplicated())

# o/p-->

# 0    False
# 1     True
# 2    False
# 3    False
# Name: Name, dtype: bool

# print()
# not need boolen o/p

# print(x[x["Name"].duplicated()])          #direct_duplicate_data  

# o/p-->
#    Name   Age    Sal
# 1    A  20.0  30000


# print()


#drop_duplicate---> directly remove the duplicate element row
# print(x["Name"].drop_duplicates())

# o/p->
# 0    A
# 2    C
# 3    D
# Name: Name, dtype: object

# -------------------------------------------------

# Aggreegate  (agg())-->


# import pandas as pd

# df={"Name":["A","A","C","D"], "Age":[22,20,33,38],"Sal":[20000,30000,22000,40000]}

# x=pd.DataFrame(df)
# print(x)

# # o/p-->
#   Name  Age    Sal
# 0    A   22  20000
# 1    A   20  30000
# 2    C   33  22000
# 3    D   38  40000

# print(x["Age"].agg(['mean','median','sum','min','max','mode']))

# ---------------------- STATISTICAL METHOD--------------------------------

# df.sum()--> var_name['number_column'].sum()
# df.mean()-->var_name['number_column'].mean()

# print()

# print(x["Age"].sum())                  #o/p--> 113

# print()

# print(x["Age"].mean())                 #o/p-->28.25

# print()

# print(x["Age"].median())               #o/p-->27.5

# print()

# print(x["Age"].mode())                 

#o/p-->          
# 0    20
# 1    22
# 2    33
# 3    38
# Name: Age, dtype: int64

# print()
# print(x["Age"].max())          #o/p-->38

# print()

# print(x["Age"].min())           #o/p-->20

# print()

# print(x["Age"].count())         #o/p-->4


# -------------------------------------------------
# -------------------------------------------------

# SQL RELATED ---------> 

# merge()--------> if we want to join multiple table.

# parameters are ---1. on and 2. how

# on---> in multiple table if we have same column_name we store in this parameter
# how--> type of join/ indicator tracking
# inner 
# left
# right
# outer
# cross


# import pandas as pd 
# a=pd.DataFrame({"Id":[0,1,2,3],"Name":["A","B","C","D"]})             # tab:1
# b=pd.DataFrame({"Id":[2,3,4,5],"Marks":[77,56,90,35]})                # tab:2
# print(a)
# print()
# print(b)
# print()

# o/p-->

#    Id Name
# 0   0    A
# 1   1    B
# 2   2    C
# 3   3    D

#    Id  Marks
# 0   2     77
# 1   3     56
# 2   4     90
# 3   5     35

# c=pd.merge(a,b,on=["Id"])
# print(c)

# o/p-->                              # it will consider by default inner join (inner join--- take only common elements from both tables)
#    Id Name  Marks
# 0   2    C     77
# 1   3    D     56

# print()
# c=pd.merge(a,b,on=["Id"],how="inner")

# print()
# c=pd.merge(a,b,on=["Id"],how="inner",indicator=True)
# print(c)

# o/p-->
#    Id Name  Marks _merge
# 0   2    C     77   both
# 1   3    D     56   both

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# import pandas as pd 
# a=pd.DataFrame({"Id":[0,1,2,3],"Name":["A","B","C","D"]})             # tab:1
# b=pd.DataFrame({"Id":[2,3,4,5],"Marks":[77,56,90,35]})                # tab:2
# print(a)
# print()
# print(b)
# print()
# o/p-->

#    Id Name
# 0   0    A
# 1   1    B
# 2   2    C
# 3   3    D

#    Id  Marks
# 0   2     77
# 1   3     56
# 2   4     90
# 3   5     35

# c=pd.merge(a,b,on="Id")
# print(c)

# o/p->
#    Id Name  Marks
# 0   2    C     77
# 1   3    D     56
# print()

# left join-->check matching elements , if elements are matched it show it as it is , otherwise it is show None
# s=pd.merge(a,b,on="Id",how="left")
# print(s)

# o/p->
#    Id Name  Marks
# 0   0    A    NaN
# 1   1    B    NaN
# 2   2    C   77.0
# 3   3    D   56.0

# print()

# Right join--> opposite to left 

# d=pd.merge(a,b,on="Id",how="right")
# print(d)

# o/p-->
#    Id Name  Marks
# 0   2    C     77
# 1   3    D     56
# 2   4  NaN     90
# 3   5  NaN     35

# print()

# Outer Join---> It will consider everything matching as well as unmatched elements

# w=pd.merge(a,b,on="Id",how="outer")
# print(w)

# o/p-->
#    Id Name  Marks
# 0   0    A    NaN
# 1   1    B    NaN
# 2   2    C   77.0
# 3   3    D   56.0
# 4   4  NaN   90.0
# 5   5  NaN   35.0

# print()

# Cross Join--> 1st row matching to all rows of another table , it will happen all possible elemsnts
# here we cann't use on parameter coz it consider all elements
# automatically it will create  NEW column

# x=pd.merge(a,b,how="cross")
# print(x)

# o/p-->
#     Id_x Name  Id_y  Marks
# 0      0    A     2     77
# 1      0    A     3     56
# 2      0    A     4     90
# 3      0    A     5     35
# 4      1    B     2     77
# 5      1    B     3     56
# 6      1    B     4     90
# 7      1    B     5     35
# 8      2    C     2     77
# 9      2    C     3     56
# 10     2    C     4     90
# 11     2    C     5     35
# 12     3    D     2     77
# 13     3    D     3     56
# 14     3    D     4     90
# 15     3    D     5     35

print()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# when we don't have any common column 

# syntax ---> 
# N_var=pd.merge(a,b,left_on="EId",right_on="Id")
# print(N_var)


# import pandas as pd 
# a=pd.DataFrame({"EId":[0,1,2,3],"Name":["A","B","C","D"]})             # tab:1
# b=pd.DataFrame({"Id":[2,3,4,5],"Marks":[77,56,90,35]})                # tab:2
# print(a)
# print()
# print(b)
# print()

# o/p-->
#    EId Name
# 0    0    A
# 1    1    B
# 2    2    C
# 3    3    D

#    Id  Marks
# 0   2     77
# 1   3     56
# 2   4     90
# 3   5     35

# p=pd.merge(a,b,left_on="EId",right_on="Id")            #by default it consider as inner join
# print(p)

# o/p-->
#    EId Name  Id  Marks
# 0    2    C   2     77
# 1    3    D   3     56

# print()
# l=pd.merge(a,b,left_on="EId",right_on="Id",how="inner")
# print(l)

# o/p-->

#    EId Name  Id  Marks
# 0    2    C   2     77
# 1    3    D   3     56

# print()
# a=pd.merge(a,b,left_on="EId",right_on="Id",how="left")
# print(a)

# o/p-->
#    EId Name   Id  Marks
# 0    0    A  NaN    NaN
# 1    1    B  NaN    NaN
# 2    2    C  2.0   77.0
# 3    3    D  3.0   56.0

# print()
# b=pd.merge(a,b,left_on="EId",right_on="Id",how="right")
# print(b)

# o/p-->
#    EId Name  Id_x  Marks_x  Id_y  Marks_y
# 0  2.0    C   2.0     77.0     2       77
# 1  3.0    D   3.0     56.0     3       56
# 2  NaN  NaN   NaN      NaN     4       90
# 3  NaN  NaN   NaN      NaN     5       35

# print()
# -------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------


# import pandas as pd 
# a=pd.DataFrame({"EId":[0,1,2,3],"Name":["A","B","C","D"]})             # tab:1
# b=pd.DataFrame({"Id":[2,3,4,5],"Marks":[77,56,90,35]})                # tab:2
# print(a)
# print()
# print(b)
# print()

# o/p-->
#    EId Name
# 0    0    A
# 1    1    B
# 2    2    C
# 3    3    D

#    Id  Marks
# 0   2     77
# 1   3     56
# 2   4     90
# 3   5     35

# p=pd.merge(a,b,left_on="EId",right_on="Id",indicator=True)            #by default it consider as inner join
# print(p)

# o/p-->
#    EId Name  Id  Marks _merge
# 0    2    C   2     77   both
# 1    3    D   3     56   both

# print()
# l=pd.merge(a,b,left_on="EId",right_on="Id",how="inner",indicator=True)
# print(l)

# o/p-->
#    EId Name  Id  Marks _merge
# 0    2    C   2     77   both
# 1    3    D   3     56   both

# print()
# a=pd.merge(a,b,left_on="EId",right_on="Id",how="left",indicator=True)
# print(a)

# o/p-->
#    EId Name   Id  Marks     _merge
# 0    0    A  NaN    NaN  left_only
# 1    1    B  NaN    NaN  left_only
# 2    2    C  2.0   77.0       both
# 3    3    D  3.0   56.0       both

# print()
# b=pd.merge(a,b,left_on="EId",right_on="Id",how="right",indicator=True)
# print(b)

# o/p-->
#    EId Name  Id  Marks      _merge
# 0  2.0    C   2     77        both
# 1  3.0    D   3     56        both
# 2  NaN  NaN   4     90  right_only
# 3  NaN  NaN   5     35  right_only

# print()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

''' 

import pandas as pd

Data=pd.DataFrame({"Date_Time":["2026-05-27 9:39","2025-04-27 10:20"]})
# print(Data)

# o/p-->
#           Date_Time
# 0   2026-05-27 9:39
# 1  2025-04-27 10:20

print()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# to convert complete table into single columns
# To craete new seperate one or more column
# manual as well as normal way to create table is also the way 

Data["Date_Time"]=pd.to_datetime(Data["Date_Time"])

Data["YEAR"]=pd.to_datetime(Data["Date_Time"]).dt.year

print(Data)

# o/p-->
#             Date_Time  YEAR
# 0 2026-05-27 09:39:00  2026
# 1 2025-04-27 10:20:00  2025

print()

Data["MONTH"]=pd.to_datetime(Data["Date_Time"]).dt.month
print(Data)

# # o/p-->
#             Date_Time  YEAR  MONTH
# 0 2026-05-27 09:39:00  2026      5
# 1 2025-04-27 10:20:00  2025      4
print()


Data["DAY"]=pd.to_datetime(Data["Date_Time"]).dt.day
print(Data)

# o/p--
#             Date_Time  YEAR  MONTH  DAY
# 0 2026-05-27 09:39:00  2026      5   27
# 1 2025-04-27 10:20:00  2025      4   27

print()

Data["HOUR"]=pd.to_datetime(Data["Date_Time"]).dt.hour
Data["MINUTE"]=pd.to_datetime(Data["Date_Time"]).dt.minute
Data["SECOND"]=pd.to_datetime(Data["Date_Time"]).dt.second
Data["MONTH_NAME"]=pd.to_datetime(Data["Date_Time"]).dt.month_name()
Data["DAY_NAME"]=pd.to_datetime(Data["Date_Time"]).dt.day_name()
print(Data)

# o/p-->

#             Date_Time  YEAR  MONTH  DAY  HOUR  MINUTE  SECOND  MONTH_NAME   DAY_NAME
# 0 2026-05-27 09:39:00  2026      5   27     9      39       0        May   Wednesday
# 1 2025-04-27 10:20:00  2025      4   27    10      20       0      April     Sunday

''' 

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

#first cell 

# import pandas as pd

# x=pd.read_csv("file_name/Dataset_name")
# print(x)

# OR 
# print(x.to_csv("file_name/Dataset_name.extension(csv)"))     #------------> convert to csv
# print(x.to_excel("file_name/Dataset_name.xlxs"))

#next cell perfom all the oprations 
# like  x.head() --> to print 1st 5 rows 

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

'''
# Group By----> split the data based on department/ data will split according to category

import pandas as pd
data=pd.DataFrame({"Name":['A','B','C','D','E','F'],
                   "Dept":['IT','HR','HR','IT','Finance','Analysis'],
                   "sal":[10000,7000,8000,15000,17000,20000]})
print(data)
print()

# o/p-->
#   Name      Dept    sal
# 0    A        IT  10000
# 1    B        HR   7000
# 2    C        HR   8000
# 3    D        IT  15000
# 4    E   Finance  17000
# 5    F  Analysis  20000




# print(data.groupby("Dept"))         #.....<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000018AAD190BC0> it show 

print(data.groupby("Dept")["sal"].sum())       # addition of  departments--
print()

# # O/P-->
# Dept
# Analysis    20000
# Finance     17000
# HR          15000
# IT          25000
# Name: sal, dtype: int64


print(data.groupby("Dept")["sal"].max())
print()
# o/p-->

# Dept
# Analysis    20000
# Finance     17000
# HR           8000
# IT          15000
# Name: sal, dtype: int64


print(data.groupby("Dept")["sal"].min())
print()

# o/p-->

# Dept
# Analysis    20000
# Finance     17000
# HR           7000
# IT          10000
# Name: sal, dtype: int64

print(data.groupby("Dept")["sal"].mean())
print()

# o/p-->

# Dept
# Analysis    20000.0
# Finance     17000.0
# HR           7500.0
# IT          12500.0
# Name: sal, dtype: float64

print(data.groupby("Dept")["sal"].agg(["sum","min","max","mean"]))
print()

# o/p-->

#             sum    min    max     mean
# Dept                                  
# Analysis  20000  20000  20000  20000.0
# Finance   17000  17000  17000  17000.0
# HR        15000   7000   8000   7500.0
# IT        25000  10000  15000  12500.0

#count()
#size
#shape

''' 
'''
import pandas as pd

x=pd.DataFrame({"SUB_NAME":["Python","JAVA","sql","web","Manual","testing"]})

print(x)
print()


#convert all the elements into uppercase use str.upper()


print(x["SUB_NAME"].str.upper())
print()

# o/p--
# 0     PYTHON
# 1       JAVA
# 2        SQL
# 3        WEB
# 4     MANUAL
# 5    TESTING
# Name: SUB_NAME, dtype: object

print(x["SUB_NAME"].str.lower())
print()

# o/p-->

# 0     python
# 1       java
# 2        sql
# 3        web
# 4     manual
# 5    testing
# Name: SUB_NAME, dtype: object

print(x["SUB_NAME"].str.swapcase())
print()

# o/p-->
# 0     pYTHON
# 1       java
# 2        SQL
# 3        WEB
# 4     mANUAL
# 5    TESTING
# Name: SUB_NAME, dtype: object


print(x["SUB_NAME"].str.startswith("P"))
print()

# o/p-->
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# Name: SUB_NAME, dtype: bool

print(x["SUB_NAME"].str.endswith("g"))
print()

# O/P-->
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5     True
# Name: SUB_NAME, dtype: bool

print(x["SUB_NAME"].str.split())               #if any space space is present in given words it split that word like ['pyt', 'hon']
print()

# o/p->
# 0     [Python]
# 1       [JAVA]
# 2        [sql]
# 3        [web]
# 4     [Manual]
# 5    [testing]
# Name: SUB_NAME, dtype: object


print(x["SUB_NAME"].str.title())
print()

# o/p-->
# 0     Python
# 1       Java
# 2        Sql
# 3        Web
# 4     Manual
# 5    Testing
# Name: SUB_NAME, dtype: object

print(x["SUB_NAME"].str.capitalize())
print()

# o/p-->

# 0     Python
# 1       Java
# 2        Sql
# 3        Web
# 4     Manual
# 5    Testing
# Name: SUB_NAME, dtype: object

print(x["SUB_NAME"].str.contains("P"))               #contains--> if the letter present it will show true else false
print()

# o/p-->

# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# Name: SUB_NAME, dtype: bool

print(x["SUB_NAME"].str.replace("P","*"))
print()

# o/p--<

# 0     *ython
# 1       JAVA
# 2        sql
# 3        web
# 4     Manual
# 5    testing
# Name: SUB_NAME, dtype: object
''' 


# | Function / Method / Property | Meaning                               | Syntax                     | Example                             | Output           |
# | ---------------------------- | ------------------------------------- | -------------------------- | ----------------------------------- | ---------------- |
# | `rank()`                     | Assign rank based on sorted values    | `s.rank()`                 | `df["Marks"].rank()`                | 35→1, 90→5       |
# | `rank(ascending=True)`       | Rank from lowest to highest (default) | `s.rank(ascending=True)`   | `df["Marks"].rank(ascending=True)`  | Lowest rank = 1  |
# | `rank(ascending=False)`      | Rank from highest to lowest           | `s.rank(ascending=False)`  | `df["Marks"].rank(ascending=False)` | Highest rank = 1 |
# | `rank(method="average")`     | Average rank for duplicates (default) | `s.rank(method="average")` | `[90,99,85,90,65]`                  | 90 gets rank 3.5 |
# | `rank(method="dense")`       | No gaps in ranking                    | `s.rank(method="dense")`   | `[90,99,85,90,65]`                  | 90 gets rank 3   |
# | `rank(method="first")`       | Rank according to appearance order    | `s.rank(method="first")`   | Duplicate 90s                       | Rank 3,4         |
# | `rank(method="max")`         | Highest rank assigned to duplicates   | `s.rank(method="max")`     | Duplicate 90s                       | Rank 4           |
# | `rank(method="min")`         | Lowest rank assigned to duplicates    | `s.rank(method="min")`     | Duplicate 90s                       | Rank 3           |
# | `rank(pct=True)`             | Percentage ranking                    | `s.rank(pct=True)`         | `df["Marks"].rank(pct=True)`        | 0.2–1.0          |
# | `rank(pct=True)*100`         | Percentage rank in %                  | `s.rank(pct=True)*100`     | Same                                | 20%–100%         |

# Rank()------> always we will consider sorted_elements
# it will work on the basis of elements positions---------> output should be position of the element
# It will give  the output in the form of float and by default it will consider as a mean 
# taking unsorted elements ---> then o/p range in sorted manner give the ranking , 
# it will arrange in asending to decending lower no [0-->index position but rank is 1] to higher[5]
# rank always starts from 1 

# rank--> asending=True
# asending= False
# method-> max,min,first, dense, arverage
# percentage--> pct=True, (pct=True)*100
'''
import pandas as pd

x=pd.DataFrame({"Name":['A','B','C','D','E'],"Marks":[35,90,85,45,70]})
print(x)
print()

# o/p-->
#   Name  Marks
# 0    A     35
# 1    B     90
# 2    C     85
# 3    D     45
# 4    E     70

print("Ranking information")
print()



print(x.rank())
print()

# o/p-->
# Ranking information

#    Name  Marks
# 0   1.0    1.0
# 1   2.0    5.0
# 2   3.0    4.0
# 3   4.0    2.0
# 4   5.0    3.0

print("Ranking information------->Bigger to  ---------->Lower")
print()
print(x.rank())

# o/p->
# Ranking information------->Bigger to  ---------->Lower

#    Name  Marks
# 0   1.0    1.0
# 1   2.0    5.0
# 2   3.0    4.0
# 3   4.0    2.0
# 4   5.0    3.0

print()
print(x["Marks"].rank(ascending=True))     #--> ascending=True  --> by default lower to higher

# o.p-->

# 0    1.0         #35
# 1    5.0          #90
# 2    4.0          #85
# 3    2.0          #45
# 4    3.0          #70
# Name: Marks, dtype: float64

print()
print(x["Marks"].rank(ascending=False))                   #descending---> higher to lower

# 0    5.0      #35
# 1    1.0      #90
# 2    2.0      #85
# 3    4.0      #45
# 4    3.0      #70
# Name: Marks, dtype: float64
''' 

# Note---> if we have duplicate value the avrage value of the duplicate values (mean of the given elements) --> by default 

'''
import pandas as pd 

y=pd.DataFrame({"Name":['A','B','C','D','E'],"Marks":[90,99,85, 90,65]})
print(y)

# o/p-->
#   Name  Marks
# 0    A     90
# 1    B     99
# 2    C     85
# 3    D     90
# 4    E     65

print()
print(y["Marks"].rank())

# o/p-->

# 0    3.5        #90
# 1    5.0        #99
# 2    2.0        #85
# 3    3.5        #90
# 4    1.0        #65
# Name: Marks, dtype: float64

print()

print(y["Marks"].rank(ascending=True))

# o/p-->

# 0    3.5      #90
# 1    5.0      #99
# 2    2.0      #85
# 3    3.5      #90
# 4    1.0      #65
# Name: Marks, dtype: float64

print()

print(y["Marks"].rank(ascending=False))

# o/p-->
# 0    2.5      #90
# 1    1.0      #99
# 2    4.0      #85
# 3    2.5      #90
# 4    5.0      #65
# Name: Marks, dtype: float64

print()
print(y["Marks"].rank(method="average"))

# o/p-->

# 0    3.5      #90
# 1    5.0      #99
# 2    2.0      #85
# 3    3.5      #90
# 4    1.0      #65
# Name: Marks, dtype: float64

print()

# method="dense"---> Always it will consider, their will be no gap , it just arrange in order formate.

print(y["Marks"].rank(method="dense"))

# o/p-->

# 0    3.0       #90
# 1    4.0       #99
# 2    2.0       #85
# 3    3.0       #90
# 4    1.0       #65
# Name: Marks, dtype: float64

print()

# method=Firts--->  it will won't consider any mean value just it will arranging the rank  (#1,2,3,4,5 ) 
# for duplicate values asldo it will jst pass the rank 

print(y["Marks"].rank(method="first"))

# o/p->

# 0    3.0        #90
# 1    5.0        #99
# 2    2.0        #85
# 3    4.0        #90 
# 4    1.0        #65
# Name: Marks, dtype: float64

print()

#(method=MAX)---> Round up to the next num
print(y["Marks"].rank(method="max"))


# o/p-->
# 0    4.0      #90 
# 1    5.0      #99
# 2    2.0      #85
# 3    4.0      #90 
# 4    1.0      #65
# Name: Marks, dtype: float64

print()

# method="min"----> it will round up to previous num
print(y["Marks"].rank(method="min"))

# o/p-->
# 0    3.0
# 1    5.0
# 2    2.0
# 3    3.0
# 4    1.0
# Name: Marks, dtype: float64

print()

# percentage---pct=true--- always it will sort the elements 

print(y["Marks"].rank(pct=True))

# o/p-->
# 0    0.7
# 1    1.0
# 2    0.4
# 3    0.7
# 4    0.2
# Name: Marks, dtype: float64

print()

print(y["Marks"].rank(pct=True)*100)

# o/p-->

# 0     70.0
# 1    100.0
# 2     40.0
# 3     70.0
# 4     20.0
# Name: Marks, dtype: float64

''' 

# import pandas as pd

# p=pd.DataFrame({"Marks":[10,20,30,40,50]})
# print(p)

# o/p--->
#    Marks
# 0     10
# 1     20
# 2     30
# 3     40
# 4     50

# print()

# Rank divided by total num of element

# print(p["Marks"].rank(pct=True))

# o/p-->

# 0    0.2     #10
# 1    0.4     #20
# 2    0.6     #30
# 3    0.8     #
# 4    1.0
# Name: Marks, dtype: float64


# ------------------------------------------------------------------------

# rolling--- Calculate the number row by row
# the rolling Window size should be greater than 1 
# each row consider/holding  2 2 numbers 
# Current row + Previous row     rolling(2)
# in first row their will be no previous value so it should be None.
# windows change 

# import pandas as pd

# p=pd.DataFrame({"Marks":[10,20,30,40,50]})
# print(p)
# print()

# print(p.rolling(2).sum())
# print()

# o/p-->

#    Marks
# 0    NaN     
# 1   30.0      ----> 10+20
# 2   50.0      ----> 20+30
# 3   70.0      ----> 30+40
# 4   90.0      ----> 40+50

# Note ---> if we pass 3 (current + previous 2 values)

# print(p.rolling(3).sum())

# print()

# o/p-->
#    Marks
# 0    NaN      #10
# 1    NaN      #10+20
# 2   60.0      #10+20+30  
# 3   90.0      #20+30+40
# 4  120.0      #20+30+40+50

# -------------------------------------------------------
# expanding ()---> it will work from start row to end row 

''' 
import pandas as pd

p=pd.DataFrame({"Marks":[10,20,30,40,50]})
print(p)
print()

# o/p-->

#    Marks
# 0     10
# 1     20
# 2     30
# 3     40
# 4     50


print(p.expanding().sum())

# o/p-->
#    Marks
# 0   10.0
# 1   30.0
# 2   60.0
# 3  100.0
# 4  150.0

print()

print(p.expanding().mean())

# o/p-->
#    Marks
# 0   10.0
# 1   15.0
# 2   20.0
# 3   25.0
# 4   30.0


print()

# max--> not chnge in output

print(p.expanding().max())

print()

# o/p-->
#    Marks
# 0   10.0
# 1   20.0
# 2   30.0
# 3   40.0
# 4   50.0

print(p.expanding().min())
print() 

# o/p-->

#    Marks
# 0   10.0
# 1   10.0
# 2   10.0
# 3   10.0
# 4   10.0

'''

# cumsum---->

'''
import pandas as pd

p=pd.DataFrame({"Marks":[10,20,30,40,50]})
print(p)
print()

#    Marks
# 0     10
# 1     20
# 2     30
# 3     40
# 4     50

print(p.cumsum())
print()

# o/p-->

#    Marks
# 0     10
# 1     30
# 2     60
# 3    100
# 4    150


print(p.cummax())
print()

# o/p-->
#    Marks
# 0     10
# 1     20
# 2     30
# 3     40
# 4     50

print(p.cummin())
print()

# o/p-->
#    Marks
# 0     10
# 1     10
# 2     10
# 3     10
# 4     10

print(p.cumprod())
print()

# o/p-->
#       Marks
# 0        10
# 1       200
# 2      6000
# 3    240000
# 4  12000000

''' 
# difference between pivot & pivot table?




# pivot---> used to rearrage the table or rearrange the table

# import pandas as pd 
# data=pd.DataFrame({"Name":['A','B','C'],"Sub":["Python","java","SQL"],"Marks":[77,90,100]})
# print(data)
# print()

# o/p-->

#   Name     Sub  Marks
# 0    A  Python     77
# 1    B    java     90
# 2    C     SQL    100

# print(data.pivot(index="Name",columns="Sub",values="Marks"))
# print()

# o/p-->
# Sub   Python    SQL  java
# Name                     
# A       77.0    NaN   NaN
# B        NaN    NaN  90.0
# C        NaN  100.0   NaN



# --------------------------------------------------------------------------

# pivot_table---> 

'''
import pandas as pd 
data=pd.DataFrame({"Name":['A','B','C','D'],"Sub":["Python","java","Python","java"],"Marks":[77,100,100,77]})
print(data)
print()

# O/P--
#   Name     Sub  Marks
# 0    A  Python     77
# 1    B    java    100
# 2    C  Python    100
# 3    D    java     77

print(data.pivot(index="Name",columns="Sub",values="Marks"))
print()

# O/P-->

# Sub   Python   java
# Name               
# A       77.0    NaN
# B        NaN  100.0
# C      100.0    NaN
# D        NaN   77.0

print(data.pivot_table(index="Name",columns="Sub",values="Marks", aggfunc=['sum','max','min','mean']))
print()

# o/p-->
#         sum           max           min          mean       
# Sub  Python   java Python   java Python   java Python   java
# Name                                                        
# A      77.0    NaN   77.0    NaN   77.0    NaN   77.0    NaN
# B       NaN  100.0    NaN  100.0    NaN  100.0    NaN  100.0
# C     100.0    NaN  100.0    NaN  100.0    NaN  100.0    NaN
# D       NaN   77.0    NaN   77.0    NaN   77.0    NaN   77.0

''' 
# 1. Pivot_Table
# 2. query()--- filter
# 3. apply()
# 4. Join()
# 5. concat()


# Difference Between pivot() and pivot_table()
# | Point                 | `pivot()`                | `pivot_table()`                 |
# | --------------------- | ------------------------ | ------------------------------- |
# | Definition            | Reshapes/rearranges data | Reshapes + summarizes data      |
# | Aggregation           | ❌ Not allowed            | ✅ Allowed                       |
# | Duplicate Values      | ❌ Error occurs           | ✅ Handles duplicates            |
# | Default Aggregation   | Not applicable           | `mean()`                        |
# | Missing Values        | Shows NaN                | Can replace using `fill_value`  |
# | Multiple Aggregations | ❌ No                     | ✅ Yes                           |
# | Margins (Grand Total) | ❌ No                     | ✅ Yes (`margins=True`)          |
# | Suitable For          | Clean unique data        | Real-world data with duplicates |
# | Speed                 | Faster                   | Slightly slower                 |
# | Output                | Simple table             | Summary table                   |

# ---------------------------------------------------------------------------------------


# pivot_table()-> pivot_table() by default take mean as aggregation function if we not mention print(x.pivot_table(index="Name",values="Marks"))

'''

import pandas as pd


x=pd.DataFrame({"Name":['x','x','y','y','x','y'],
                "Sub":['py','py','sql','sql','py','sql'],
                "Marks":[55,78,90,88,99,45]})

print(x)
print()

# o/p-->
#   Name  Sub  Marks
# 0    x   py     55
# 1    x   py     78
# 2    y  sql     90
# 3    y  sql     88
# 4    x   py     99
# 5    y  sql     45

print(x.pivot_table(index="Name",values="Marks"))

# o/p-->
#           Marks
# Name           
# x     77.333333
# y     74.333333

print()
print(x.pivot_table(index="Name",values="Marks",aggfunc="sum"))

# o/p-->
#       Marks
# Name       
# x       232
# y       223

print()
print(x.pivot_table(index="Name",values="Marks",aggfunc="max"))

# o/p-->
#       Marks
# Name       
# x        99
# y        90

print()
print(x.pivot_table(index="Name",values="Marks",aggfunc="min"))

# o/p-->
#       Marks
# Name       
# x        55
# y        45

print()
print(x.pivot_table(index="Name",values="Marks",aggfunc=["sum", "mean", "max","min","count"]))

# o/p-->

#        sum       mean   max   min count
#      Marks      Marks Marks Marks Marks
# Name                                   
# x      232  77.333333    99    55     3
# y      223  74.333333    90    45     3

print()
print(x.pivot_table(index="Name",values="Marks",aggfunc=["sum", "mean", "max","min","count"],margins_name="all",margins="True"))

# o/p-->
#        sum       mean   max   min count
#      Marks      Marks Marks Marks Marks
# Name                                   
# x      232  77.333333    99    55     3
# y      223  74.333333    90    45     3
# all    455  75.833333    99    45     6

print()
print(x.pivot_table(index="Name",values="Marks", columns="Sub",aggfunc=["sum", "mean", "max","min","count"],margins_name="all",margins="True"))

# o/P-->
#         sum                   mean                         max             min           count         
# Sub      py    sql  all         py        sql        all    py   sql all    py   sql all    py  sql all
# Name                                                                                                   
# x     232.0    NaN  232  77.333333        NaN  77.333333  99.0   NaN  99  55.0   NaN  55   3.0  NaN   3
# y       NaN  223.0  223        NaN  74.333333  74.333333   NaN  90.0  90   NaN  45.0  45   NaN  3.0   3
# all   232.0  223.0  455  77.333333  74.333333  75.833333  99.0  90.0  99  55.0  45.0  45   3.0  3.0   6


print()
print(x.pivot_table(index="Name",values="Marks", 
                    columns="Sub",aggfunc=["sum", "mean", "max","min","count"],
                    margins_name="all",
                    margins="True", fill_value=0))

# o/p-->
#       sum                 mean                       max         min         count        
# Sub    py  sql  all         py        sql        all  py sql all  py sql all    py sql all
# Name                                                                                      
# x     232    0  232  77.333333   0.000000  77.333333  99   0  99  55   0  55     3   0   3
# y       0  223  223   0.000000  74.333333  74.333333   0  90  90   0  45  45     0   3   3
# all   232  223  455  77.333333  74.333333  75.833333  99  90  99  55  45  45     3   3   6


print()
print(x.pivot_table(index="Name",values="Marks", columns="Sub" ,aggfunc=["sum","mean","max","min","count"]
                    ,margins_name="calculation"
                    ,margins=True,fill_value=0))


# o/p-->
#              sum                        mean                        max                 min                 count                
# Sub           py  sql calculation         py        sql calculation  py sql calculation  py sql calculation    py sql calculation
# Name                                                                                                                             
# x            232    0         232  77.333333   0.000000   77.333333  99   0          99  55   0          55     3   0           3
# y              0  223         223   0.000000  74.333333   74.333333   0  90          90   0  45          45     0   3           3
# calculation  232  223         455  77.333333  74.333333   75.833333  99  90          99  55  45          45     3   3           6

''' 

# QUERIES---> v_n.query(condition)

'''
import pandas as pd

y=pd.DataFrame({"Name":['A','B','c','X','Y'], 
                "sal":[1000,2000,3000,4000,5000], 
                "age":[23,45,70,65,19]})

print(y)

print()

# o/p-->
#   Name   sal  age
# 0    A  1000   23
# 1    B  2000   45
# 2    c  3000   70
# 3    X  4000   65
# 4    Y  5000   19

print(y["sal"])

print()

# o/p-->
# 0    1000
# 1    2000
# 2    3000
# 3    4000
# 4    5000
# Name: sal, dtype: int64

print(y["sal"]>2000)
print()

# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
# Name: sal, dtype: bool


print(y[y["sal"]>2000])
print()

# o/p-->

#   Name   sal  age
# 2    c  3000   70
# 3    X  4000   65
# 4    Y  5000   19

print(y.query("sal>2000"))

# o/p-->
#   Name   sal  age
# 2    c  3000   70
# 3    X  4000   65
# 4    Y  5000   19

print()

print(y.query("age>45"))

# o/p-->
#   Name   sal  age
# 2    c  3000   70
# 3    X  4000   65

print()
print(y.query("sal>3000 and age>45"))

# o/p-->
#   Name   sal  age
# 3    X  4000   65

print()
print(y.query("Name=='A'"))

# o/p-->

#   Name   sal  age
# 0    A  1000   23

print()
print(y.query("sal<2000 and age<45"))

# o/p-->
#   Name   sal  age
# 0    A  1000   23

print()
print(y.query("sal<2000 or age<45"))


# o/p-->

#   Name   sal  age
# 0    A  1000   23
# 4    Y  5000   19

''' 

# -----------------------------------------------------------------------
'''
import pandas as pd

x=pd.DataFrame({"ID":[11,12,13,14],"Sal":[100,200,300,400]})
y=pd.DataFrame({"Name":["Ram","Kiran","Ravi","Mahii"]})

print(x)
print()

# o/p>

#    ID  Sal
# 0  11  100
# 1  12  200
# 2  13  300
# 3  14  400

print(y)

# o/p-->
# 
#     Name
# 0    Ram
# 1  Kiran
# 2   Ravi
# 3  Mahii

print()
print("Both Table Joining")
print()
print(x.join(y))

# o/p-->
# Both Table Joining

#    ID  Sal   Name
# 0  11  100    Ram
# 1  12  200  Kiran
# 2  13  300   Ravi
# 3  14  400  Mahii

print()
print(x.join(y,how="inner"))

# o/p--.
#    ID  Sal   Name
# 0  11  100    Ram
# 1  12  200  Kiran
# 2  13  300   Ravi
# 3  14  400  Mahii

print()
print(x.join(y,how="left"))

# o/p--.
#    ID  Sal   Name
# 0  11  100    Ram
# 1  12  200  Kiran
# 2  13  300   Ravi
# 3  14  400  Mahii

print()
print(x.join(y,how="right"))

# o/p-->
#    ID  Sal   Name
# 0  11  100    Ram
# 1  12  200  Kiran
# 2  13  300   Ravi
# 3  14  400  Mahii

print()
print(x.join(y,how="cross"))

# o/p-->
#    ID  Sal   Name
# 0   11  100    Ram
# 1   11  100  Kiran
# 2   11  100   Ravi
# 3   11  100  Mahii
# 4   12  200    Ram
# 5   12  200  Kiran
# 6   12  200   Ravi
# 7   12  200  Mahii
# 8   13  300    Ram
# 9   13  300  Kiran
# 10  13  300   Ravi
# 11  13  300  Mahii
# 12  14  400    Ram
# 13  14  400  Kiran
# 14  14  400   Ravi
# 15  14  400  Mahii
''' 

import pandas as pd

x=pd.DataFrame({"ID":[11,12,13,14],"Sal":[100,200,300,400]})
y=pd.DataFrame({"Name":["Ram","Kiran","Ravi","Mahii"]})

print(x)
print()

# o/p-->/
#    ID  Sal
# 0  11  100
# 1  12  200
# 2  13  300
# 3  14  400

print(y)
print()

# o/p-->
#     Name
# 0    Ram
# 1  Kiran
# 2   Ravi
# 3  Mahii

r=pd.concat([x,y])
print(r)

# o/p-->

#      ID    Sal   Name
# 0  11.0  100.0    NaN
# 1  12.0  200.0    NaN
# 2  13.0  300.0    NaN
# 3  14.0  400.0    NaN
# 0   NaN    NaN    Ram
# 1   NaN    NaN  Kiran
# 2   NaN    NaN   Ravi
# 3   NaN    NaN  Mahii


print()
r=pd.concat([x,y],ignore_index=True)
print(r)

# o/p-->

#      ID    Sal   Name
# 0  11.0  100.0    NaN
# 1  12.0  200.0    NaN
# 2  13.0  300.0    NaN
# 3  14.0  400.0    NaN
# 4   NaN    NaN    Ram
# 5   NaN    NaN  Kiran
# 6   NaN    NaN   Ravi
# 7   NaN    NaN  Mahii

print()
r=pd.concat([x,y],ignore_index=False)
print(r)

# o/p-->
#      ID    Sal   Name
# 0  11.0  100.0    NaN
# 1  12.0  200.0    NaN
# 2  13.0  300.0    NaN
# 3  14.0  400.0    NaN
# 0   NaN    NaN    Ram
# 1   NaN    NaN  Kiran
# 2   NaN    NaN   Ravi
# 3   NaN    NaN  Mahii

print()
r=pd.concat([x,y],ignore_index=True,axis=1)                 #ignore_index=True------> continuous index 
print(r)

# o/p-->
#     0    1      2
# 0  11  100    Ram
# 1  12  200  Kiran
# 2  13  300   Ravi
# 3  14  400  Mahii

print()
r=pd.concat([x,y],ignore_index=False,axis=1)
print(r)

# o/p-->
#    ID  Sal   Name
# 0  11  100    Ram
# 1  12  200  Kiran
# 2  13  300   Ravi
# 3  14  400  Mahii

print()
r=pd.concat([x,y],axis=1,keys=["First","Second"])
print(r)

# o/p-->
#   First      Second
#      ID  Sal   Name
# 0    11  100    Ram
# 1    12  200  Kiran
# 2    13  300   Ravi
# 3    14  400  Mahii

print()
r=pd.concat([x,y],axis=1,keys=["First_tab","Second_tab"])
print(r)

# o/p-->

#   First_tab      Second_tab
#          ID  Sal       Name
# 0        11  100        Ram
# 1        12  200      Kiran
# 2        13  300       Ravi
# 3        14  400      Mahii

# merge=> column
# join=> tables
# concat=> N num of tables

