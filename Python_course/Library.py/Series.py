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
# 7. LOC[position]   --> work only on position loc[si:ei:sv]  --> endindex in loc included
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


# import pandas as pd
# s = pd.Series([10, 20, 30, 40])

# print(s.iloc[1])     # element at position 1
# print(s.iloc[1:3])
