'''
DataFrame:
-------------
-Combination of Series and rows
OR
-Combination of Rows and Columns

-It is 2D

HOW TO CREATE DATAFRAME:
way1--->By the help of dictionary
way2--->By the help of List

NOTE: better to go for dictionary

Syntax-->import pandas as pd
        new_var=pd.DataFrame(dictionary)

        ::DataFrame-->is an inbuilt class


'''

# 1️⃣ DataFrame Properties
# | Property  | Meaning                | Syntax       | Example Output                |
# | --------- | ---------------------- | ------------ | ----------------------------- |
# | `shape`   | Returns rows & columns | `df.shape`   | `(4,3)`                       |
# | `ndim`    | Number of dimensions   | `df.ndim`    | `2`                           |
# | `size`    | Total elements         | `df.size`    | `12`                          |
# | `columns` | Column names           | `df.columns` | `Index(['Name','Age','Sal'])` |
# | `index`   | Row labels             | `df.index`   | `RangeIndex(0,4)`             |
# | `axes`    | Row & column labels    | `df.axes`    | `[Index, Columns]`            |
# | `dtypes`  | Datatype of columns    | `df.dtypes`  | object, int64                 |
# | `values`  | Data as NumPy array    | `df.values`  | `[['A',22,20000]...]`         |
# | `empty`   | Check empty dataframe  | `df.empty`   | `False`                       |
# | `T`       | Transpose dataframe    | `df.T`       | Rows ↔ Columns                |

# 2️⃣ Basic DataFrame Methods

# | Method       | Meaning             | Syntax          | Example          |
# | ------------ | ------------------- | --------------- | ---------------- |
# | `head()`     | First 5 rows        | `df.head()`     | `df.head()`      |
# | `head(n)`    | First n rows        | `df.head(2)`    | First 2 rows     |
# | `tail()`     | Last 5 rows         | `df.tail()`     | Last rows        |
# | `tail(n)`    | Last n rows         | `df.tail(2)`    | Last 2 rows      |
# | `sample()`   | Random row          | `df.sample()`   | Random record    |
# | `sample(n)`  | Random n rows       | `df.sample(2)`  | 2 random rows    |
# | `info()`     | Dataset information | `df.info()`     | Memory, datatype |
# | `describe()` | Statistical summary | `df.describe()` | Mean, min, max   |

# 3️⃣ Selection Methods
# | Syntax                    | Meaning          | Example            |
# | ------------------------- | ---------------- | ------------------ |
# | `df.loc[0]`               | Single row       | First row          |
# | `df.loc[0:2]`             | Multiple rows    | Rows 0 to 2        |
# | `df.loc[0:2,"Name"]`      | Row + column     | Names from row 0–2 |
# | `df.loc[:, "Name"]`       | Entire column    | Name column        |
# | `df.loc[:, "Name":"Sal"]` | Multiple columns | Name to Sal        |


# iloc() → Position Based
# 
# | Syntax             | Meaning        | Example    |
# | ------------------ | -------------- | ---------- |
# | `df.iloc[0]`       | First row      | Row 0      |
# | `df.iloc[0,2]`     | Single value   | 20000      |
# | `df.iloc[0:3,0:2]` | Rows & columns | Slice data |
# | `df.iloc[[0,2]]`   | Specific rows  | Row 0 & 2  |



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


'''
Dictionary representation in DataFrame
--->{key:value}
In key part we have to mention column_name
In value part we have to mention variable name
'''
# way1--->using dictionary
import pandas as pd
name=['A','B','C','D']
age=[23,30,28,40]  #if we are passing two list then both list length should be same..otherwise it will give ValueError
sal=[10000,15000,20000,13000]
id=['A1','B1','C1','D1']
details={"NAME":name,"AGE":age,"SAL":sal,"ID":id}
#       ColName:var, ColName:var,......
x=pd.DataFrame(details)
print(x)

#   NAME  AGE    SAL  ID
# 0    A   23  10000  A1
# 1    B   30  15000  B1
# 2    C   28  20000  C1
# 3    D   40  13000  D1
print()

# OR
data=pd.DataFrame({"Name":['A','B','C','D'],"AGE":[23,30,28,40],"SAL":[10000,15000,20000,13000]})
print(data)
#   Name  AGE    SAL
# 0    A   23  10000
# 1    B   30  15000
# 2    C   28  20000
# 3    D   40  13000
print()

# way2--->using list
y=pd.DataFrame([["A",18,10000,"A1"],["B",22,20000,"B2"],["C",24,12000,"C2"]],columns=["NAME","AGE","SAL","ID"])
print(y)

#   NAME  AGE    SAL  ID
# 0    A   18  10000  A1
# 1    B   22  20000  B2
# 2    C   24  12000  C2
print("----------------------")

#ex1: using list
x=pd.DataFrame([['PY',10,"D",70],["SQL",15,"C",80],["Web",20,"B",90],["PB",30,"A",75]],columns=["SUB","MARKS","GRADE","TOTAL"])
print(x)

#    SUB  MARKS GRADE  TOTAL
# 0   PY     10     D     70
# 1  SQL     15     C     80
# 2  Web     20     B     90
# 3   PB     30     A     75
print()

#ex2: 
sub1=['M1','ML','DSA','DL','M2','PY','JAVA','SQL','DB','CD']
sub2=['Web','M2','sql','mongodb','TOC','M1','C','Cpp','DL','softSkills']
sub3=['M1','SQl','softskills','ML','DL','CC','Manual','java','M2','COD']
grade=['A','B','E','F','A','C','D','A','A','D']
total=[87,98,65,56,76,88,99,81,71,90]
clg_data=pd.DataFrame({"SUB1":sub1,"SUB2":sub2,"SUB3":sub3,"GRADE":grade,"TOTAL_MARKS":total})
print(clg_data)

#    SUB1        SUB2        SUB3 GRADE  TOTAL_MARKS
# 0    M1         Web          M1     A           87
# 1    ML          M2         SQl     B           98
# 2   DSA         sql  softskills     E           65
# 3    DL     mongodb          ML     F           56
# 4    M2         TOC          DL     A           76
# 5    PY          M1          CC     C           88
# 6  JAVA           C      Manual     D           99
# 7   SQL         Cpp        java     A           81
# 8    DB          DL          M2     A           71
# 9    CD  softSkills         COD     D           90

print()
#shape
print(clg_data.shape)  #(10, 5)
print()
#ndim
print(clg_data.ndim)  #2

print()

#size
print(clg_data.size)  #50
print()

#columns--->print only columns list
print(clg_data.columns)
# Index(['SUB1', 'SUB2', 'SUB3', 'GRADE', 'TOTAL_MARKS'], dtype='str')
print()

print(clg_data.index)  #RangeIndex(start=0, stop=10, step=1)
print(clg_data.axes)   
#[RangeIndex(start=0, stop=10, step=1), Index(['SUB1', 'SUB2', 'SUB3', 'GRADE', 'TOTAL_MARKS'], dtype='str')]
print()

# dtypes
# in each column what dat type we are using-->use var.dtypes
print(clg_data.dtypes)

# SUB1             str
# SUB2             str
# SUB3             str
# GRADE            str
# TOTAL_MARKS    int64
# dtype: object
print()

# T---->transform-->var.T
print(clg_data.T)

#                0    1           2        3    4   5       6     7   8           9
# SUB1          M1   ML         DSA       DL   M2  PY    JAVA   SQL  DB          CD
# SUB2         Web   M2         sql  mongodb  TOC  M1       C   Cpp  DL  softSkills
# SUB3          M1  SQl  softskills       ML   DL  CC  Manual  java  M2         COD
# GRADE          A    B           E        F    A   C       D     A   A           D
# TOTAL_MARKS   87   98          65       56   76  88      99    81  71          90
print()

# values
print(clg_data.values)

# [['M1' 'Web' 'M1' 'A' 87]
#  ['ML' 'M2' 'SQl' 'B' 98]
#  ['DSA' 'sql' 'softskills' 'E' 65]
#  ['DL' 'mongodb' 'ML' 'F' 56]
#  ['M2' 'TOC' 'DL' 'A' 76]
#  ['PY' 'M1' 'CC' 'C' 88]
#  ['JAVA' 'C' 'Manual' 'D' 99]
#  ['SQL' 'Cpp' 'java' 'A' 81]
#  ['DB' 'DL' 'M2' 'A' 71]
#  ['CD' 'softSkills' 'COD' 'D' 90]]
print()

# empty-->if there is no data o/p should  be True else False
print(clg_data.empty)  #False
print()

'''METHODS'''

# head()--->work top to bottom..by default it will create 5 rows..else we can give no. of rows
print(clg_data.head())

#   SUB1     SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1      Web          M1     A           87
# 1   ML       M2         SQl     B           98
# 2  DSA      sql  softskills     E           65
# 3   DL  mongodb          ML     F           56
# 4   M2      TOC          DL     A           76
print()

print(clg_data.head(3))
#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web          M1     A           87
# 1   ML   M2         SQl     B           98
# 2  DSA  sql  softskills     E           65
print()

# tail()
print(clg_data.tail())
#    SUB1        SUB2    SUB3 GRADE  TOTAL_MARKS
# 5    PY          M1      CC     C           88
# 6  JAVA           C  Manual     D           99
# 7   SQL         Cpp    java     A           81
# 8    DB          DL      M2     A           71
# 9    CD  softSkills     COD     D           90
print()

print(clg_data.tail(4))
#    SUB1        SUB2    SUB3 GRADE  TOTAL_MARKS
# 6  JAVA           C  Manual     D           99
# 7   SQL         Cpp    java     A           81
# 8    DB          DL      M2     A           71
# 9    CD  softSkills     COD     D           90
print()

# sample()-->random rows will get the output
print(clg_data.sample())

#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 2  DSA  sql  softskills     E           65

print()

# or-->var.sample(no. of rows)
print(clg_data.sample(6))

#   SUB1     SUB2  SUB3 GRADE  TOTAL_MARKS
# 3   DL  mongodb    ML     F           56
# 8   DB       DL    M2     A           71
# 5   PY       M1    CC     C           88
# 1   ML       M2   SQl     B           98
# 0   M1      Web    M1     A           87
# 7  SQL      Cpp  java     A           81
print()

# describe()
print(clg_data.describe())

#        TOTAL_MARKS
# count    10.000000
# mean     81.100000
# std      14.082692
# min      56.000000
# 25%      72.250000
# 50%      84.000000
# 75%      89.500000
# max      99.000000
print()

# if we want to calculate character column then use
print(clg_data.describe(include="object"))

#        SUB1 SUB2 SUB3 GRADE
# count    10   10   10    10
# unique   10   10   10     6
# top      M1  Web   M1     A---->top element of the column
# freq      1    1    1     4------->to element how many times it will repeating
print()

print(clg_data.describe(include="all"))

#        SUB1 SUB2 SUB3 GRADE  TOTAL_MARKS
# count    10   10   10    10    10.000000
# unique   10   10   10     6          NaN
# top      M1  Web   M1     A          NaN
# freq      1    1    1     4          NaN
# mean    NaN  NaN  NaN   NaN    81.100000
# std     NaN  NaN  NaN   NaN    14.082692
# min     NaN  NaN  NaN   NaN    56.000000
# 25%     NaN  NaN  NaN   NaN    72.250000
# 50%     NaN  NaN  NaN   NaN    84.000000
# 75%     NaN  NaN  NaN   NaN    89.500000
# max     NaN  NaN  NaN   NaN    99.000000
print()

print(clg_data.describe(include="number"))
#        TOTAL_MARKS
# count    10.000000
# mean     81.100000
# std      14.082692
# min      56.000000
# 25%      72.250000
# 50%      84.000000
# 75%      89.500000
# max      99.000000
print()

# info-->display all info about the table
clg_data.info()

# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 5 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   SUB1         10 non-null     str  
#  1   SUB2         10 non-null     str  
#  2   SUB3         10 non-null     str  
#  3   GRADE        10 non-null     str  
#  4   TOTAL_MARKS  10 non-null     int64
# dtypes: int64(1), str(4)
# memory usage: 532.0 bytes
print()
'''
"""
understanding Loc(stop index included)
******************************************
data_frame.loc[row_number]
data_frame.loc[row_number,[column_name,,,,,,]]
data_frame.loc[start:stop]
data_frame.loc[start:stop,"column_name"]
data_frame.loc[start:stop,["column_1,column_2...."]]
data_frame.loc[start:stop,"column_1":"column_n"] 
'''

# loc()--->stop index is included...accept position as well as character
# if i want to display selected rows--->var.loc[row_number]
print(clg_data.loc[4])

# SUB1            M2
# SUB2           TOC
# SUB3            DL
# GRADE            A
# TOTAL_MARKS     76
# Name: 4, dtype: object
print()

# if we want to display selected row with it's selected column then use:
# data_frame.loc[row_number,[column_name,...]]
print(clg_data.loc[3,['SUB1','GRADE']])
# SUB1     DL
# GRADE     F
# Name: 3, dtype: str
print()

# slicing-->ei will be included
# print 0-2 rows
print(clg_data.loc[0:2])

#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web          M1     A           87
# 1   ML   M2         SQl     B           98
# 2  DSA  sql  softskills     E           65
print()


# slicing for single column
# var.loc[si:ei:sv,["column_name"]]
print(clg_data.loc[0:2,"SUB1"])

# 0     M1
# 1     ML
# 2    DSA
# Name: SUB1, dtype: str
print()

# slicing for multiple column-->var.loc[si:ei:sv,['col1,col2,...]]
print(clg_data.loc[0:2,["SUB1","GRADE"]])

#   SUB1 GRADE
# 0   M1     A
# 1   ML     B
# 2  DSA     E
print()

# print single column--->var["col_name"]
print(clg_data["SUB2"])

# 0           Web
# 1            M2
# 2           sql
# 3       mongodb
# 4           TOC
# 5            M1
# 6             C
# 7           Cpp
# 8            DL
# 9    softSkills
# Name: SUB2, dtype: str
print()

# to print multiple columns--->var[['col1','col2',..]]
print(clg_data[['SUB2','SUB3','TOTAL_MARKS']])

#          SUB2        SUB3  TOTAL_MARKS
# 0         Web          M1           87
# 1          M2         SQl           98
# 2         sql  softskills           65
# 3     mongodb          ML           56
# 4         TOC          DL           76
# 5          M1          CC           88
# 6           C      Manual           99
# 7         Cpp        java           81
# 8          DL          M2           71
# 9  softSkills         COD           90
print()

# slicing for particular rows and at particular column range
# data_frame.loc[start:stop,"column_1":"column_n"] 
print(clg_data.loc[0:1:1,'SUB1':"SUB3"])

#   SUB1 SUB2 SUB3
# 0   M1  Web   M1
# 1   ML   M2  SQl
print()

print("------------------------------------")

"""
understanding iloc(stop index excluded)
****************************************************
data_frame.iloc[row_number,column_number]
data_frame.iloc[row_start:row_stop,col_start:col_stop]
data_frame.iloc[start:stop,column_number]
data_frame.iloc[[row_1,row_2,......]]
""" 

# iloc--->ei is excluded....will accept only positions... not characters
# fetch particular row-->var.iloc[row_number]
print(clg_data.iloc[3])

# SUB1                DL
# SUB2           mongodb
# SUB3                ML
# GRADE                F
# TOTAL_MARKS         56
# Name: 3, dtype: object
print()

# print multiple rows---.var.iloc[[row1,row2,..]]
print(clg_data.iloc[[0,1,2,3]])

#   SUB1     SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1      Web          M1     A           87
# 1   ML       M2         SQl     B           98
# 2  DSA      sql  softskills     E           65
# 3   DL  mongodb          ML     F           56
print()

# slicing
print(clg_data.iloc[0:2:1])

#   SUB1 SUB2 SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web   M1     A           87
# 1   ML   M2  SQl     B           98
print()

print(clg_data.loc[0:2:1])

#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web          M1     A           87
# 1   ML   M2         SQl     B           98
# 2  DSA  sql  softskills     E           65
print()

# for loc-->var.loc[si:ei:sv,[column_name]]
print(clg_data.loc[0:3:1,['GRADE']])
#   GRADE
# 0     A
# 1     B
# 2     E
# 3     F

# var.iloc[si:ei:sv,[column_number]]
print(clg_data.iloc[0:3:1,[3]])
#   GRADE
# 0     A
# 1     B
# 2     E
print()

# var.iloc[row_number,[column_number]]
print(clg_data.iloc[2,[3]])
# GRADE    E
# Name: 2, dtype: str
print()

# var.iloc[row_start:row_stop,colstart:col_stop]
print(clg_data.iloc[0:4,2:3])
#          SUB3
# 0          M1
# 1         SQl
# 2  softskills
# 3          ML
print()

print("----------------------")
'''
name=["A","B","C","D"]
age=[21,30,40,45]
sal=[7000,8000,9000,10000]
id=["A1",'B1',"C1","D1"]
x={"NAME":name,"AGE":age,"SAl":sal,"ID":id}
data=pd.DataFrame(x)
print(data)

#   NAME  AGE    SAl  ID
# 0    A   21   7000  A1
# 1    B   30   8000  B1
# 2    C   40   9000  C1
# 3    D   45  10000  D1

print()

# CREATING ROWS....without using inbuilt function

# Creating new row--->var.loc[row_number]=["val",'val',..]
data.loc[4]=['E',42,8700,'E1']
print(data)

#   NAME  AGE    SAl  ID
# 0    A   21   7000  A1
# 1    B   30   8000  B1
# 2    C   40   9000  C1
# 3    D   45  10000  D1
# 4    E   42   8700  E1
print()

# CREATING COLUMNS...without using inbuilt function

# creating column--->var['column_name']=default_value
# data['Loc']=100
# print(data)

#   NAME  AGE    SAl  ID  Loc
# 0    A   21   7000  A1  100
# 1    B   30   8000  B1  100
# 2    C   40   9000  C1  100
# 3    D   45  10000  D1  100
# 4    E   42   8700  E1  100
print()

# to create multiple columns--->var[['colname1','colname2',....]]=[default_value1,default_value2,...]
data[["LOC1","LOC2"]]=[1,2]
print(data)

#   NAME  AGE    SAl  ID  LOC1  LOC2
# 0    A   21   7000  A1     1     2
# 1    B   30   8000  B1     1     2
# 2    C   40   9000  C1     1     2
# 3    D   45  10000  D1     1     2
# 4    E   42   8700  E1     1     2
print()

# CREATING MULTIPLE COLUMNS USING INBUILT FUNCTION----->assign()
# var.assign(colname1=[val1,val2,..],colname2=[[val1,val2,...]])
print(data.assign(manager1=["D","A","B","E","C"],manager2=["B1","C1","D1","E1","A1"]))

#   NAME  AGE    SAl  ID  LOC1  LOC2 manager1 manager2
# 0    A   21   7000  A1     1     2        D       B1
# 1    B   30   8000  B1     1     2        A       C1
# 2    C   40   9000  C1     1     2        B       D1
# 3    D   45  10000  D1     1     2        E       E1
# 4    E   42   8700  E1     1     2        C       A1
print()

# INSERTING NEW COLUMN IN BETWEEN EXISTING TWO COLUMNS
# --->usee insert() method
# var.insert(position,column_name,[values])
data.insert(1,"GENDER",['M','F','F','F','M'])
print(data)

#   NAME GENDER  AGE    SAl  ID  LOC1  LOC2
# 0    A      M   21   7000  A1     1     2
# 1    B      F   30   8000  B1     1     2
# 2    C      F   40   9000  C1     1     2
# 3    D      F   45  10000  D1     1     2
# 4    E      M   42   8700  E1     1     2
print()
'''

sname=['ditya','riya',None,'John',None]
marks=[None,70,80,None,90]
sub=['Py',None,'SQL',None,'PB']
sdata=pd.DataFrame({"STUDENT_NAME":sname,"MARKS":marks,"SUBJECT":sub})
print(sdata)

#   STUDENT_NAME  MARKS SUBJECT
# 0        ditya    NaN      Py
# 1         riya   70.0     NaN
# 2          NaN   80.0     SQL
# 3         John    NaN     NaN
# 4          NaN   90.0      PB
print()

# fillna()--->var.fillna(data)
# print(sdata.fillna(1000))

#   STUDENT_NAME   MARKS SUBJECT
# 0        ditya  1000.0      Py
# 1         riya    70.0    1000
# 2         1000    80.0     SQL
# 3         John  1000.0    1000
# 4         1000    90.0      PB
print()

'''
# now we have two syntax for fillna
# 1. ffill()--->forward fill
        -Always working for top to bottom
        -In the place of None to value will be replace
        -If None is present at the top most row then it will print as it is None value


2.bfill()--->backward fill
        -working from bottom to top
        -In place of None it will replace with it's bottom value
        -If None is placed at the bottom most row then it will print as it is None value

'''

# ffill()
print(sdata.ffill())

#   STUDENT_NAME  MARKS SUBJECT
# 0        ditya    NaN      Py
# 1         riya   70.0      Py
# 2         riya   80.0     SQL
# 3         John   80.0     SQL
# 4         John   90.0      PB
# print()

# backward fill()
# print(sdata.bfill())

#   STUDENT_NAME  MARKS SUBJECT
# 0        ditya   70.0      Py
# 1         riya   70.0     SQL
# 2         John   80.0     SQL
# 3         John   90.0      PB
# 4          NaN   90.0      PB
# print()

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


# -----------------------------------------------------------D_N--------------------------------------------------------------------

'''
DataFrame:
-------------
-Combination of Series and rows
OR
-Combination of Rows and Columns

-It is 2D

HOW TO CREATE DATAFRAME:
way1--->By the help of dictionary
way2--->By the help of List

NOTE: better to go for dictionary

Syntax-->import pandas as pd
        new_var=pd.DataFrame(dictionary)

        ::DataFrame-->is an inbuilt class


'''


'''
Dictionary representation in DataFrame
--->{key:value}
In key part we have to mention column_name
In value part we have to mention variable name
'''
# way1--->using dictionary
import pandas as pd
name=['A','B','C','D']
age=[23,30,28,40]  #if we are passing two list then both list length should be same..otherwise it will give ValueError
sal=[10000,15000,20000,13000]
id=['A1','B1','C1','D1']
details={"NAME":name,"AGE":age,"SAL":sal,"ID":id}
#       ColName:var, ColName:var,......
x=pd.DataFrame(details)
print(x)

#   NAME  AGE    SAL  ID
# 0    A   23  10000  A1
# 1    B   30  15000  B1
# 2    C   28  20000  C1
# 3    D   40  13000  D1
print()

# OR
data=pd.DataFrame({"Name":['A','B','C','D'],"AGE":[23,30,28,40],"SAL":[10000,15000,20000,13000]})
print(data)
#   Name  AGE    SAL
# 0    A   23  10000
# 1    B   30  15000
# 2    C   28  20000
# 3    D   40  13000
print()

# way2--->using list
y=pd.DataFrame([["A",18,10000,"A1"],["B",22,20000,"B2"],["C",24,12000,"C2"]],columns=["NAME","AGE","SAL","ID"])
print(y)

#   NAME  AGE    SAL  ID
# 0    A   18  10000  A1
# 1    B   22  20000  B2
# 2    C   24  12000  C2
print("----------------------")

#ex1: using list
x=pd.DataFrame([['PY',10,"D",70],["SQL",15,"C",80],["Web",20,"B",90],["PB",30,"A",75]],columns=["SUB","MARKS","GRADE","TOTAL"])
print(x)

#    SUB  MARKS GRADE  TOTAL
# 0   PY     10     D     70
# 1  SQL     15     C     80
# 2  Web     20     B     90
# 3   PB     30     A     75
print()

#ex2: 
sub1=['M1','ML','DSA','DL','M2','PY','JAVA','SQL','DB','CD']
sub2=['Web','M2','sql','mongodb','TOC','M1','C','Cpp','DL','softSkills']
sub3=['M1','SQl','softskills','ML','DL','CC','Manual','java','M2','COD']
grade=['A','B','E','F','A','C','D','A','A','D']
total=[87,98,65,56,76,88,99,81,71,90]
clg_data=pd.DataFrame({"SUB1":sub1,"SUB2":sub2,"SUB3":sub3,"GRADE":grade,"TOTAL_MARKS":total})
print(clg_data)

#    SUB1        SUB2        SUB3 GRADE  TOTAL_MARKS
# 0    M1         Web          M1     A           87
# 1    ML          M2         SQl     B           98
# 2   DSA         sql  softskills     E           65
# 3    DL     mongodb          ML     F           56
# 4    M2         TOC          DL     A           76
# 5    PY          M1          CC     C           88
# 6  JAVA           C      Manual     D           99
# 7   SQL         Cpp        java     A           81
# 8    DB          DL          M2     A           71
# 9    CD  softSkills         COD     D           90

print()
#shape
print(clg_data.shape)  #(10, 5)
print()
#ndim
print(clg_data.ndim)  #2

print()

#size
print(clg_data.size)  #50
print()

#columns--->print only columns list
print(clg_data.columns)
# Index(['SUB1', 'SUB2', 'SUB3', 'GRADE', 'TOTAL_MARKS'], dtype='str')
print()

print(clg_data.index)  #RangeIndex(start=0, stop=10, step=1)
print(clg_data.axes)   
#[RangeIndex(start=0, stop=10, step=1), Index(['SUB1', 'SUB2', 'SUB3', 'GRADE', 'TOTAL_MARKS'], dtype='str')]
print()

# dtypes
# in each column what dat type we are using-->use var.dtypes
print(clg_data.dtypes)

# SUB1             str
# SUB2             str
# SUB3             str
# GRADE            str
# TOTAL_MARKS    int64
# dtype: object
print()

# T---->transform-->var.T
print(clg_data.T)

#                0    1           2        3    4   5       6     7   8           9
# SUB1          M1   ML         DSA       DL   M2  PY    JAVA   SQL  DB          CD
# SUB2         Web   M2         sql  mongodb  TOC  M1       C   Cpp  DL  softSkills
# SUB3          M1  SQl  softskills       ML   DL  CC  Manual  java  M2         COD
# GRADE          A    B           E        F    A   C       D     A   A           D
# TOTAL_MARKS   87   98          65       56   76  88      99    81  71          90
print()

# values
print(clg_data.values)

# [['M1' 'Web' 'M1' 'A' 87]
#  ['ML' 'M2' 'SQl' 'B' 98]
#  ['DSA' 'sql' 'softskills' 'E' 65]
#  ['DL' 'mongodb' 'ML' 'F' 56]
#  ['M2' 'TOC' 'DL' 'A' 76]
#  ['PY' 'M1' 'CC' 'C' 88]
#  ['JAVA' 'C' 'Manual' 'D' 99]
#  ['SQL' 'Cpp' 'java' 'A' 81]
#  ['DB' 'DL' 'M2' 'A' 71]
#  ['CD' 'softSkills' 'COD' 'D' 90]]
print()

# empty-->if there is no data o/p should  be True else False
print(clg_data.empty)  #False
print()

'''METHODS'''

# head()--->work top to bottom..by default it will create 5 rows..else we can give no. of rows
print(clg_data.head())

#   SUB1     SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1      Web          M1     A           87
# 1   ML       M2         SQl     B           98
# 2  DSA      sql  softskills     E           65
# 3   DL  mongodb          ML     F           56
# 4   M2      TOC          DL     A           76
print()

print(clg_data.head(3))
#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web          M1     A           87
# 1   ML   M2         SQl     B           98
# 2  DSA  sql  softskills     E           65
print()

# tail()
print(clg_data.tail())
#    SUB1        SUB2    SUB3 GRADE  TOTAL_MARKS
# 5    PY          M1      CC     C           88
# 6  JAVA           C  Manual     D           99
# 7   SQL         Cpp    java     A           81
# 8    DB          DL      M2     A           71
# 9    CD  softSkills     COD     D           90
print()

print(clg_data.tail(4))
#    SUB1        SUB2    SUB3 GRADE  TOTAL_MARKS
# 6  JAVA           C  Manual     D           99
# 7   SQL         Cpp    java     A           81
# 8    DB          DL      M2     A           71
# 9    CD  softSkills     COD     D           90
print()

# sample()-->random rows will get the output
print(clg_data.sample())

#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 2  DSA  sql  softskills     E           65

print()

# or-->var.sample(no. of rows)
print(clg_data.sample(6))

#   SUB1     SUB2  SUB3 GRADE  TOTAL_MARKS
# 3   DL  mongodb    ML     F           56
# 8   DB       DL    M2     A           71
# 5   PY       M1    CC     C           88
# 1   ML       M2   SQl     B           98
# 0   M1      Web    M1     A           87
# 7  SQL      Cpp  java     A           81
print()

# describe()
print(clg_data.describe())

#        TOTAL_MARKS
# count    10.000000
# mean     81.100000
# std      14.082692
# min      56.000000
# 25%      72.250000
# 50%      84.000000
# 75%      89.500000
# max      99.000000
print()

# if we want to calculate character column then use
print(clg_data.describe(include="object"))

#        SUB1 SUB2 SUB3 GRADE
# count    10   10   10    10
# unique   10   10   10     6
# top      M1  Web   M1     A---->top element of the column
# freq      1    1    1     4------->to element how many times it will repeating
print()

print(clg_data.describe(include="all"))

#        SUB1 SUB2 SUB3 GRADE  TOTAL_MARKS
# count    10   10   10    10    10.000000
# unique   10   10   10     6          NaN
# top      M1  Web   M1     A          NaN
# freq      1    1    1     4          NaN
# mean    NaN  NaN  NaN   NaN    81.100000
# std     NaN  NaN  NaN   NaN    14.082692
# min     NaN  NaN  NaN   NaN    56.000000
# 25%     NaN  NaN  NaN   NaN    72.250000
# 50%     NaN  NaN  NaN   NaN    84.000000
# 75%     NaN  NaN  NaN   NaN    89.500000
# max     NaN  NaN  NaN   NaN    99.000000
print()

print(clg_data.describe(include="number"))
#        TOTAL_MARKS
# count    10.000000
# mean     81.100000
# std      14.082692
# min      56.000000
# 25%      72.250000
# 50%      84.000000
# 75%      89.500000
# max      99.000000
print()

# info-->display all info about the table
clg_data.info()

# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 5 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   SUB1         10 non-null     str  
#  1   SUB2         10 non-null     str  
#  2   SUB3         10 non-null     str  
#  3   GRADE        10 non-null     str  
#  4   TOTAL_MARKS  10 non-null     int64
# dtypes: int64(1), str(4)
# memory usage: 532.0 bytes
print()
'''
"""
understanding Loc(stop index included)
******************************************
data_frame.loc[row_number]
data_frame.loc[row_number,[column_name,,,,,,]]
data_frame.loc[start:stop]
data_frame.loc[start:stop,"column_name"]
data_frame.loc[start:stop,["column_1,column_2...."]]
data_frame.loc[start:stop,"column_1":"column_n"] 
'''

# loc()--->stop index is included...accept position as well as character
# if i want to display selected rows--->var.loc[row_number]
print(clg_data.loc[4])

# SUB1            M2
# SUB2           TOC
# SUB3            DL
# GRADE            A
# TOTAL_MARKS     76
# Name: 4, dtype: object
print()

# if we want to display selected row with it's selected column then use:
# data_frame.loc[row_number,[column_name,...]]
print(clg_data.loc[3,['SUB1','GRADE']])
# SUB1     DL
# GRADE     F
# Name: 3, dtype: str
print()

# slicing-->ei will be included
# print 0-2 rows
print(clg_data.loc[0:2])

#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web          M1     A           87
# 1   ML   M2         SQl     B           98
# 2  DSA  sql  softskills     E           65
print()


# slicing for single column
# var.loc[si:ei:sv,["column_name"]]
print(clg_data.loc[0:2,"SUB1"])

# 0     M1
# 1     ML
# 2    DSA
# Name: SUB1, dtype: str
print()

# slicing for multiple column-->var.loc[si:ei:sv,['col1,col2,...]]
print(clg_data.loc[0:2,["SUB1","GRADE"]])

#   SUB1 GRADE
# 0   M1     A
# 1   ML     B
# 2  DSA     E
print()

# print single column--->var["col_name"]
print(clg_data["SUB2"])

# 0           Web
# 1            M2
# 2           sql
# 3       mongodb
# 4           TOC
# 5            M1
# 6             C
# 7           Cpp
# 8            DL
# 9    softSkills
# Name: SUB2, dtype: str
print()

# to print multiple columns--->var[['col1','col2',..]]
print(clg_data[['SUB2','SUB3','TOTAL_MARKS']])

#          SUB2        SUB3  TOTAL_MARKS
# 0         Web          M1           87
# 1          M2         SQl           98
# 2         sql  softskills           65
# 3     mongodb          ML           56
# 4         TOC          DL           76
# 5          M1          CC           88
# 6           C      Manual           99
# 7         Cpp        java           81
# 8          DL          M2           71
# 9  softSkills         COD           90
print()

# slicing for particular rows and at particular column range
# data_frame.loc[start:stop,"column_1":"column_n"] 
print(clg_data.loc[0:1:1,'SUB1':"SUB3"])

#   SUB1 SUB2 SUB3
# 0   M1  Web   M1
# 1   ML   M2  SQl
print()

print("------------------------------------")

"""
understanding iloc(stop index excluded)
****************************************************
data_frame.iloc[row_number,column_number]
data_frame.iloc[row_start:row_stop,col_start:col_stop]
data_frame.iloc[start:stop,column_number]
data_frame.iloc[[row_1,row_2,......]]
""" 

# iloc--->ei is excluded....will accept only positions... not characters
# fetch particular row-->var.iloc[row_number]
print(clg_data.iloc[3])

# SUB1                DL
# SUB2           mongodb
# SUB3                ML
# GRADE                F
# TOTAL_MARKS         56
# Name: 3, dtype: object
print()

# print multiple rows---.var.iloc[[row1,row2,..]]
print(clg_data.iloc[[0,1,2,3]])

#   SUB1     SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1      Web          M1     A           87
# 1   ML       M2         SQl     B           98
# 2  DSA      sql  softskills     E           65
# 3   DL  mongodb          ML     F           56
print()

# slicing
print(clg_data.iloc[0:2:1])

#   SUB1 SUB2 SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web   M1     A           87
# 1   ML   M2  SQl     B           98
print()

print(clg_data.loc[0:2:1])

#   SUB1 SUB2        SUB3 GRADE  TOTAL_MARKS
# 0   M1  Web          M1     A           87
# 1   ML   M2         SQl     B           98
# 2  DSA  sql  softskills     E           65
print()

# for loc-->var.loc[si:ei:sv,[column_name]]
print(clg_data.loc[0:3:1,['GRADE']])
#   GRADE
# 0     A
# 1     B
# 2     E
# 3     F

# var.iloc[si:ei:sv,[column_number]]
print(clg_data.iloc[0:3:1,[3]])
#   GRADE
# 0     A
# 1     B
# 2     E
print()

# var.iloc[row_number,[column_number]]
print(clg_data.iloc[2,[3]])
# GRADE    E
# Name: 2, dtype: str
print()

# var.iloc[row_start:row_stop,colstart:col_stop]
print(clg_data.iloc[0:4,2:3])
#          SUB3
# 0          M1
# 1         SQl
# 2  softskills
# 3          ML
print()

print("----------------------")
'''
name=["A","B","C","D"]
age=[21,30,40,45]
sal=[7000,8000,9000,10000]
id=["A1",'B1',"C1","D1"]
x={"NAME":name,"AGE":age,"SAl":sal,"ID":id}
data=pd.DataFrame(x)
print(data)

#   NAME  AGE    SAl  ID
# 0    A   21   7000  A1
# 1    B   30   8000  B1
# 2    C   40   9000  C1
# 3    D   45  10000  D1

print()

# CREATING ROWS....without using inbuilt function

# Creating new row--->var.loc[row_number]=["val",'val',..]
data.loc[4]=['E',42,8700,'E1']
print(data)

#   NAME  AGE    SAl  ID
# 0    A   21   7000  A1
# 1    B   30   8000  B1
# 2    C   40   9000  C1
# 3    D   45  10000  D1
# 4    E   42   8700  E1
print()

# CREATING COLUMNS...without using inbuilt function

# creating column--->var['column_name']=default_value
# data['Loc']=100
# print(data)

#   NAME  AGE    SAl  ID  Loc
# 0    A   21   7000  A1  100
# 1    B   30   8000  B1  100
# 2    C   40   9000  C1  100
# 3    D   45  10000  D1  100
# 4    E   42   8700  E1  100
print()

# to create multiple columns--->var[['colname1','colname2',....]]=[default_value1,default_value2,...]
data[["LOC1","LOC2"]]=[1,2]
print(data)

#   NAME  AGE    SAl  ID  LOC1  LOC2
# 0    A   21   7000  A1     1     2
# 1    B   30   8000  B1     1     2
# 2    C   40   9000  C1     1     2
# 3    D   45  10000  D1     1     2
# 4    E   42   8700  E1     1     2
print()

# CREATING MULTIPLE COLUMNS USING INBUILT FUNCTION----->assign()
# var.assign(colname1=[val1,val2,..],colname2=[[val1,val2,...]])
print(data.assign(manager1=["D","A","B","E","C"],manager2=["B1","C1","D1","E1","A1"]))

#   NAME  AGE    SAl  ID  LOC1  LOC2 manager1 manager2
# 0    A   21   7000  A1     1     2        D       B1
# 1    B   30   8000  B1     1     2        A       C1
# 2    C   40   9000  C1     1     2        B       D1
# 3    D   45  10000  D1     1     2        E       E1
# 4    E   42   8700  E1     1     2        C       A1
print()

# INSERTING NEW COLUMN IN BETWEEN EXISTING TWO COLUMNS
# --->usee insert() method
# var.insert(position,column_name,[values])
data.insert(1,"GENDER",['M','F','F','F','M'])
print(data)

#   NAME GENDER  AGE    SAl  ID  LOC1  LOC2
# 0    A      M   21   7000  A1     1     2
# 1    B      F   30   8000  B1     1     2
# 2    C      F   40   9000  C1     1     2
# 3    D      F   45  10000  D1     1     2
# 4    E      M   42   8700  E1     1     2
print()
'''

sname=['ditya','riya',None,'John',None]
marks=[None,70,80,None,90]
sub=['Py',None,'SQL',None,'PB']
sdata=pd.DataFrame({"STUDENT_NAME":sname,"MARKS":marks,"SUBJECT":sub})
print(sdata)

#   STUDENT_NAME  MARKS SUBJECT
# 0        ditya    NaN      Py
# 1         riya   70.0     NaN
# 2          NaN   80.0     SQL
# 3         John    NaN     NaN
# 4          NaN   90.0      PB
print()

# fillna()--->var.fillna(data)
# print(sdata.fillna(1000))

#   STUDENT_NAME   MARKS SUBJECT
# 0        ditya  1000.0      Py
# 1         riya    70.0    1000
# 2         1000    80.0     SQL
# 3         John  1000.0    1000
# 4         1000    90.0      PB
print()

'''
# now we have two syntax for fillna
# 1. ffill()--->forward fill
        -Always working for top to bottom
        -In the place of None to value will be replace
        -If None is present at the top most row then it will print as it is None value


2.bfill()--->backward fill
        -working from bottom to top
        -In place of None it will replace with it's bottom value
        -If None is placed at the bottom most row then it will print as it is None value

'''

# ffill()
# print(sdata.ffill())

#   STUDENT_NAME  MARKS SUBJECT
# 0        ditya    NaN      Py
# 1         riya   70.0      Py
# 2         riya   80.0     SQL
# 3         John   80.0     SQL
# 4         John   90.0      PB
print()

# backward fill()
# print(sdata.bfill())

#   STUDENT_NAME  MARKS SUBJECT
# 0        ditya   70.0      Py
# 1         riya   70.0     SQL
# 2         John   80.0     SQL
# 3         John   90.0      PB
# 4          NaN   90.0      PB
print()

print("----------------")

y=pd.DataFrame({"NAME":["A",None,"B",None],"AGE":[None,70,None,0],"SAL":[1000,None,7000,None]})
print(y)

#   NAME   AGE     SAL
# 0    A   NaN  1000.0
# 1  NaN  70.0     NaN
# 2    B   NaN  7000.0
# 3  NaN   0.0     NaN
print()

# ffill() according to row-->var.ffill(axis=1)
# ---->it will work from left to right....wheverver None is present it will replace with it's left value
print(y.ffill(axis=1))

#   NAME   AGE     SAL
# 0    A     A  1000.0
# 1  NaN  70.0    70.0
# 2    B     B  7000.0
# 3  NaN   0.0     0.0
print()

# bfill() according to row....it will work from right to left row wise
# -->wherever None is present it will replace it with it's right value
print(y.bfill(axis=1))

#    NAME     AGE     SAL
# 0     A  1000.0  1000.0
# 1  70.0    70.0     NaN
# 2     B  7000.0  7000.0
# 3   0.0     0.0     NaN
print()

# rename()--->use to rename the column name
# syntax-->var.rename(column={'old_column_name':'new_col_name'})
print(y.rename(columns={"NAME":"N1"}))

#     N1   AGE     SAL
# 0    A   NaN  1000.0
# 1  NaN  70.0     NaN
# 2    B   NaN  7000.0
# 3  NaN   0.0     NaN
print()

# rename multiple column names--->var.rename(column={'old':'new','old1':'new1',....})
print(y.rename(columns={'AGE':'A1',"SAL":"s1","NAME":"N1"}))

#     N1    A1      s1
# 0    A   NaN  1000.0
# 1  NaN  70.0     NaN
# 2    B   NaN  7000.0
# 3  NaN   0.0     NaN
print()

# if we want to change the index
# var.rename(index={old_index:"new_index",old_index:"new_index",...})
print(y.rename(index={0:"a",1:"b"}))

#   NAME   AGE     SAL
# a    A   NaN  1000.0
# b  NaN  70.0     NaN
# 2    B   NaN  7000.0
# 3  NaN   0.0     NaN

# NOTE if i am calling the table then it showing the original tableoutput only...i.e. whatever changes we are doing it is not applied to table
# it will not show the modified table...so to get modified table as a output then use property inplace=True

print(y)
#   NAME   AGE     SAL
# 0    A   NaN  1000.0
# 1  NaN  70.0     NaN
# 2    B   NaN  7000.0
# 3  NaN   0.0     NaN
print()


# y.rename(index={0:"a",1:"b"},inplace=True)

# drop()-->we can remove rows as well as columns
# Remove rows-->var.drop(rows_number)
# OR
# var.drop([row_number1,row2])

print(y.drop(1))
#   NAME  AGE     SAL
# 0    A  NaN  1000.0
# 2    B  NaN  7000.0
# 3  NaN  0.0     NaN
print()

# removing multiple rows
print(y.drop([0,2]))

#   NAME   AGE  SAL
# 1  NaN  70.0  NaN
# 3  NaN   0.0  NaN
print()

# print(y)  #original table..if we want modified table output then use removing multiple rows print(y.drop([0,2],inplace=True))

# Deleting columns--->var.drop(labels="column_name",axis=1)
# -->for drop we have to use axis=1 for deleting columns
print(y.drop(labels="AGE",axis=1))

#   NAME     SAL
# 0    A  1000.0
# 1  NaN     NaN
# 2    B  7000.0
# 3  NaN     NaN
print()

# removing multiple columns
print(y.drop(labels=["AGE","SAL"],axis=1))

#   NAME
# 0    A
# 1  NaN
# 2    B
# 3  NaN
print()

# sort_values()-----> 
# sort particular column--->var["col_name"].sort_values()
print(y["AGE"].sort_values())

# 3     0.0
# 1    70.0
# 0     NaN
# 2     NaN
# Name: AGE, dtype: float64

print()

# sorting single column desceding to ascending-->var['column_name'].sort_values(ascending=False)
print(y["AGE"].sort_values(ascending=False))

# 1    70.0
# 3     0.0
# 0     NaN
# 2     NaN
# Name: AGE, dtype: float64
print()

# sorting multiple columns--->var.sort_values(by=['col_name1','col_name2',...])
print(y.sort_values(by=["NAME","SAL"]))

#   NAME   AGE     SAL
# 0    A   NaN  1000.0
# 2    B   NaN  7000.0
# 1  NaN  70.0     NaN
# 3  NaN   0.0     NaN
print()


print(y.sort_values(by=["NAME","SAL"],ascending=[0,1]))  #0 ans 1 row will get swapped

#   NAME   AGE     SAL
# 2    B   NaN  7000.0
# 0    A   NaN  1000.0
# 1  NaN  70.0     NaN
# 3  NaN   0.0     NaN
print("---------------------------")


# isnull()-->None values then it will show True
print(y)

#   NAME   AGE     SAL
# 0    A   NaN  1000.0
# 1  NaN  70.0     NaN
# 2    B   NaN  7000.0
# 3  NaN   0.0     NaN
print()

# print(y.isnull())

#     NAME    AGE    SAL
# 0  False   True  False
# 1   True  False   True
# 2  False   True  False
# 3   True  False   True

print()

# notnull()--->if None is present it will show False
# print(y.notnull())

#     NAME    AGE    SAL
# 0   True  False   True
# 1  False   True  False
# 2   True  False   True
# 3  False   True  False
print()

# dropna()-->var.dropna()

print(y)

# print(y.dropna())




# values_count()
y=pd.DataFrame({"NAME":["A","B","C","A"],"AGE":[20,23,20,30],"SAL":[1000,2000,3000,1000]})

print(y["NAME"].value_counts())
# NAME
# A    2
# B    1
# C    1
# Name: count, dtype: int64
print()

# unique()-->display the unique elements
print(y["NAME"].unique())

# <StringArray>
# ['A', 'B', 'C']
# Length: 3, dtype: str
print()

# nunique()--->display the count of unique elements
print(y["NAME"].nunique())  #3
print()

# astype()--->to convert one data type to another
# var.astype({"column_name":"datatype_to be changed"})
print(y.astype({"SAL":float,"NAME":bool,"AGE":float}))

#    NAME   AGE     SAL
# 0  True  20.0  1000.0
# 1  True  23.0  2000.0
# 2  True  20.0  3000.0
# 3  True  30.0  1000.0
print()

# replace--->var.replace({old_value:new_value,old_value:new_value})
print(y.replace({3000:8000,"A":"Z"}))

#   NAME  AGE   SAL
# 0    Z   20  1000
# 1    B   23  2000
# 2    C   20  8000
# 3    Z   30  1000
print()

# duplicated()
print(y["NAME"].duplicated())   #boolean output

# 0    False
# 1    False
# 2    False
# 3     True--------------->duplicate element A
# Name: NAME, dtype: bool
print()

print(y[y["NAME"].duplicated()])  #direct duplicated elements output

#   NAME  AGE   SAL
# 3    A   30  1000
print()


# drop_duplicates()
print(y["NAME"].drop_duplicates())

# 0    A
# 1    B
# 2    C
# Name: NAME, dtype: str
print()

# AGGREGATION FUNCTION
# ---->if we have to use all the aggregated function at a time(mean,median,mode,..) the use agg()
print(y["AGE"].agg(["mean","median","max","min","sum"]))  #mode will not work

# mean      23.25
# median    21.50
# max       30.00
# min       20.00
# sum       93.00
# Name: AGE, dtype: float64
print()


# STATISTICAL METHODS

# sum--->var['number_col].sum()
print("sum",y["AGE"].sum())  #93

# mean()-->var['number_col].mean()
print("mean",y["AGE"].mean())  #23.25

# median()-->var['number_col].median()
print("median",y["AGE"].median())  #21.5

# mode()--->var['number_col].mode()
print("mode",y["AGE"].mode())
# 0    20
# Name: AGE, dtype: int64

# max()-->var['number_col].max()
print("max",y["AGE"].max())  #30

# min()--->var['number_col].min()
print("min",y["AGE"].min())  #20

# count()--->var['number_col].count()
print(y["AGE"].count())  #4

# sum 93
# mean 23.25
# median 21.5
# mode 0    20
# Name: AGE, dtype: int64
# max 30
# min 20
# 4
print()

# MERGE
# merge()--->join two tables .here we have parameters--->on and how
# on--->in multiple table if we have same column_name we store in this parameter
# how--->here we do joins....by default itw ill consider inner join
# -->how='inner',   how='left'    how='right'   how='outer'   how='cross'

# table1
p=pd.DataFrame({"ID":[0,1,2,3],"NAME":["A","B","C","D"]})
print(p)

#    ID NAME
# 0   0    A
# 1   1    B
# 2   2    C
# 3   3    D
print()

# table2
q=pd.DataFrame({"ID":[2,3,4,5],"MARKS":[70,80,87,35]})
print(q)

#    ID  MARKS
# 0   2     70
# 1   3     80
# 2   4     87
# 3   5     35
print()


x=pd.merge(p,q,on=["ID"])    #by default inner join 
print(x)

#    ID NAME  MARKS
# 0   2    C     70
# 1   3    D     80
print()


# inner-->in both table it will consider common/matching rows
x=pd.merge(p,q,on=["ID"],how='inner')
print(x)
#    ID NAME  MARKS
# 0   2    C     70
# 1   3    D     80

# indicator parameter-->shows the tracking of the joins
x=pd.merge(p,q,on=["ID"],how='inner',indicator=True)  #ID-->common column name
print(x)

#    ID NAME  MARKS _merge
# 0   2    C     70   both
# 1   3    D     80   both
print()

# Left join---->it will consider matching rows from the table as well as the matching elements from the left table if not then it will show it as NOne
# will display whole left table and unmatching records from right table
x=pd.merge(p,q,on=["ID"],how='left')
print(x)

#    ID NAME  MARKS
# 0   0    A    NaN
# 1   1    B    NaN
# 2   2    C   70.0
# 3   3    D   80.0

print()

x=pd.merge(p,q,on=["ID"],how='left',indicator=True)
print(x)

#    ID NAME  MARKS     _merge
# 0   0    A    NaN  left_only
# 1   1    B    NaN  left_only
# 2   2    C   70.0       both
# 3   3    D   80.0       both
print()

# right join--->will check matching record of both tables...and will check the matching records from right table and will if not matched then will display None
# display right whole table and unmatching records from right table
x=pd.merge(p,q,on=["ID"],how='right')
print(x)

#    ID NAME  MARKS
# 0   2    C     70
# 1   3    D     80
# 2   4  NaN     87
# 3   5  NaN     35
print()

x=pd.merge(p,q,on=["ID"],how='right',indicator=True)
print(x)

#    ID NAME  MARKS      _merge
# 0   2    C     70        both
# 1   3    D     80        both
# 2   4  NaN     87  right_only
# 3   5  NaN     35  right_only
print()

# outer--->will display unmatched as well as matched data from both the tables
x=pd.merge(p,q,on=["ID"],how='outer')
print(x)

#    ID NAME  MARKS
# 0   0    A    NaN
# 1   1    B    NaN
# 2   2    C   70.0
# 3   3    D   80.0
# 4   4  NaN   87.0
# 5   5  NaN   35.0

print()

x=pd.merge(p,q,on=["ID"],how='outer',indicator=True)
print(x)

#    ID NAME  MARKS      _merge
# 0   0    A    NaN   left_only
# 1   1    B    NaN   left_only
# 2   2    C   70.0        both
# 3   3    D   80.0        both
# 4   4  NaN   87.0  right_only
# 5   5  NaN   35.0  right_only
print()

# cross join/cartesian join---->all possible matching data is displayed...al possible combination
# in cross join we cannot use on parameter that is commom columns
# LHS table 1st row is matching all the rows of right table,and so on 

# if we use we will get the error as:  raise MergeError(
# pandas.errors.MergeError: Can not pass on, right_on, left_on or set right_index=True or left_index=True

x=pd.merge(p,q,how='cross')
print(x)

#     ID_x NAME  ID_y  MARKS
# 0      0    A     2     70
# 1      0    A     3     80
# 2      0    A     4     87
# 3      0    A     5     35
# 4      1    B     2     70
# 5      1    B     3     80
# 6      1    B     4     87
# 7      1    B     5     35
# 8      2    C     2     70
# 9      2    C     3     80
# 10     2    C     4     87
# 11     2    C     5     35
# 12     3    D     2     70
# 13     3    D     3     80
# 14     3    D     4     87
# 15     3    D     5     35


print()

x=pd.merge(p,q,how='cross',indicator=True)
print(x)

#     ID_x NAME  ID_y  MARKS _merge
# 0      0    A     2     70   both
# 1      0    A     3     80   both
# 2      0    A     4     87   both
# 3      0    A     5     35   both
# 4      1    B     2     70   both
# 5      1    B     3     80   both
# 6      1    B     4     87   both
# 7      1    B     5     35   both
# 8      2    C     2     70   both
# 9      2    C     3     80   both
# 10     2    C     4     87   both
# 11     2    C     5     35   both
# 12     3    D     2     70   both
# 13     3    D     3     80   both
# 14     3    D     4     87   both
# 15     3    D     5     35   both

print()

'''
if we don't have any common column in two tables
then we need to follow the syntax--->

new_var=pd.merge(table1,table2,Lefton='left_table_col_name',RightOn='right_table_col_name')
'''

# table1
t1=pd.DataFrame({"EID":[0,1,2,3],"NAME":["A","B","C","D"]})
print(t1)

#    EID NAME
# 0    0    A
# 1    1    B
# 2    2    C
# 3    3    D


# table2
t2=pd.DataFrame({"ID":[2,3,4,5],"MARKS":[70,80,87,35]})
print(t2)

#    ID  MARKS
# 0   2     70
# 1   3     80
# 2   4     87
# 3   5     35
print()

w=pd.merge(t1,t2,left_on="EID",right_on="ID")
print(w)

#    EID NAME  ID  MARKS
# 0    2    C   2     70
# 1    3    D   3     80

print()

w=pd.merge(t1,t2,left_on="EID",right_on="ID",how="left")
print(w)

#    EID NAME   ID  MARKS
# 0    0    A  NaN    NaN
# 1    1    B  NaN    NaN
# 2    2    C  2.0   70.0
# 3    3    D  3.0   80.0
print()

w=pd.merge(t1,t2,left_on="EID",right_on="ID",how="left",indicator=True)
print(w)

#    EID NAME   ID  MARKS     _merge
# 0    0    A  NaN    NaN  left_only
# 1    1    B  NaN    NaN  left_only
# 2    2    C  2.0   70.0       both
# 3    3    D  3.0   80.0       both
print()


'''
if all column names are same in both the tables



left1=pd.DataFrame({"ID":[1,2,3],"NAME":["A","B","C"]})
print(left1)

#    ID NAME
# 0   1    A
# 1   2    B
# 2   3    C
print()

right1=pd.DataFrame({"ID":[2,3],"NAME":["D","E"]})
print(right1)

#    ID NAME
# 0   2    D
# 1   3    E
print()

# r=pd.merge(left1,right1)
# print(r)
'''

print("-----------------------------------------")

'''CONVERSION:
 -----------------

 Normal element converting to date-time
'''

data=pd.DataFrame({"Date_Time":["2026-05-26 9:30","2025-04-27 10:00"]})
print(data)

#           Date_Time
# 0   2026-05-26 9:30
# 1  2025-04-27 10:00
print()

# if i want to create separate separate columns as year column separate,month separate,date,hour,minute,seconds...
# directly it is not possible ...1st we need to convert to date-time
data['Date_Time']=pd.to_datetime(data['Date_Time'])

#             Date_Time
# 0 2026-05-26 09:30:00
# 1 2025-04-27 10:00:00

# now creating column manually
data["YEAR"]=pd.to_datetime(data["Date_Time"]).dt.year    #dt is property

#             Date_Time  YEAR
# 0 2026-05-26 09:30:00  2026
# 1 2025-04-27 10:00:00  2025

# now printing month
data["MONTH"]=pd.to_datetime(data["Date_Time"]).dt.month

#             Date_Time  YEAR  MONTH
# 0 2026-05-26 09:30:00  2026      5
# 1 2025-04-27 10:00:00  2025      4

data["MINUTE"]=pd.to_datetime(data["Date_Time"]).dt.minute

#             Date_Time  YEAR  MONTH  MINUTE
# 0 2026-05-26 09:30:00  2026      5      30
# 1 2025-04-27 10:00:00  2025      4       0

# seconds

data["SECOND"]=pd.to_datetime(data["Date_Time"]).dt.second

#             Date_Time  YEAR  MONTH  MINUTE  SECOND
# 0 2026-05-26 09:30:00  2026      5      30       0
# 1 2025-04-27 10:00:00  2025      4       0       0
print(data)


data["MONTH_NAME"]=pd.to_datetime(data["Date_Time"]).dt.month_name()
print(data)

#             Date_Time  YEAR  MONTH  MINUTE  SECOND MONTH_NAME
# 0 2026-05-26 09:30:00  2026      5      30       0        May
# 1 2025-04-27 10:00:00  2025      4       0       0      April
print()

# day name
data["DAY_NAME"]=pd.to_datetime(data["Date_Time"]).dt.day_name()
print(data)

#             Date_Time  YEAR  MONTH  MINUTE  SECOND MONTH_NAME DAY_NAME
# 0 2026-05-26 09:30:00  2026      5      30       0        May  Tuesday
# 1 2025-04-27 10:00:00  2025      4       0       0      April   Sunday
print()

# week day
data["WEEK DAY"]=pd.to_datetime(data["Date_Time"]).dt.weekday
print(data)

#             Date_Time  YEAR  MONTH  MINUTE  SECOND MONTH_NAME DAY_NAME  WEEK DAY
# 0 2026-05-26 09:30:00  2026      5      30       0        May  Tuesday         1
# 1 2025-04-27 10:00:00  2025      4       0       0      April   Sunday         6
print()