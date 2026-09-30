# '''
#                                             REGULAR EXPRESSION
# if we want represent group of string according to pattern/trend
# regular exp will working  only with string datatype   (because pattern is pesent inside '   ')                                    
# we can use other datatype but that data should inside the "  "
# -also call it as Regex

# -step 1 :
# import re
#    |   |
#   kw  module
# ------------------------------------------------------------
# function :
# 1) match()
# 2) full match()
# 3) search()
# 4) finditer()
# 5) sub()
# 6) subn()
# 7) findall()
# 8)split()
# -------------------------------------------------------------------
# match()  : In given str what char is passing that char present at beggining  it will show obj adress othwise  it will show none
# SYNTAX
# newv_r=re.match('pattern',source-of-string)
#                                 |
#                              iterable name
# if element is present at the beggining then it will show object address
# otherwise it will show none
# -------------------------------------------------------------------------------------------------
# fullmatch():  we need to pass complete word  /any one char,space if missing it will show none
# SYNTAX
# newv_n=re.fullmatch('pattern,source-of-string)

# #diiference
# match / fullmatch
# ---------------------------------------------------------------------------------------------------
# search():   In search method you can search any char/word/starting part/ending part anything if it present it will show obj address otherwise none
# always it will check firse occuance of character

# *DRAWBACK
# if you have duplicate elment it will always consider first one
# SYNTAX
# newv_n=re.search('pattern,source-of-string)
# ----------------------------------------------------------------------------------------------------------------
# finditr():
# it will  find any charin the string, we can find also 1st,2nd,3rd......occurance of duplicate element
# if char is not present it will show empty list  []
# SYNTAX:
# newv_n=re.finditer('pattern,source-of-string)
# --------------------------------------------------------------------------------------------------------------
# sub() and subn()  is just working like replace() method
# sub():  return type is string
# SYNTAX
# newv-n=re.sub('pattern'.'replace char''string name',count)
#                  |             |

#               old char     
# it will not show any error /because if replacing char length is more it will ignor
# *how many char we replacing it will not  show the count
# ------------------------------- 
# subn():  return type is  tuple
# SYNTAX
# newv-n=re.sub('pattern'.'replace char''string name',count)
# it will show error if replacing char length is more
# *how many char we replacing it will show the count
# --------------------------------------------------------------------------------------------------------------------
# findall():    everthing we can serach
# SYNTAX
# newv_n=re.findall('pattern',source-of-string)

# return type is list
# if you e=want to search group of char,element then we can use list [ ] but list shoulb in string "[ ]"

# [ ]          ...if i want to match group of char
# [A-Z]        ...if i want to match uppercase
# [a-z]        ...if i want to match lowercase
# [0-9]        ...if i want to match number
# [A-Z a-z]    ...if i want to match both
# [A-Z a-z 0-9]...want to match both
# [^ abc]      ...^ apart from this char(abc) it will displaing  all char in list format
#   +          ... meta character
#  \d          ...consider only number
#  \D          ...will consider  apart from number
#  \s          ...for white space displaying
#  \S          ...apart from white space all displaying
#  \w          ...only it will accept word character
#  \W          ...only special character
#  ^           ...call it as  startwith ( if data present output in list if data not present it will show  empty[]
#  $           ...call it as  endswith  ( if data present output in list if data not present it will show  empty[]
#  a           ...not include zero(show empty space)  (exactly a)  (only single)
#  a+          ...not include zero(show empty space)               (single and group)
#  a*          ...include zero and single also                     (zero or one or group)
#  a?          ...include zero and 1                               (zero and one)
  
#  NOTE :  \\ if am using this it will avoid warning message
# '''
# #ex  x=PythonClass  want uppercase character
# #normal way by usinng for loop
# x='PythonClass'
# count=0
# for i in x:
#     if i.isupper():
#         count=count+1
# print(count)    #o/p  2

# #by using regex
# x='PythonClass'
# import re
# y=re.findall("[A-Z]",x)
# print(len(y))   #o/p  2


# # match()  :
# # newv_r=re.match('pattern',source-of-string)

# # if element is present at the beggining then it will show object address
# # otherwise it will show none

# x='Morning class' 
# import re
# y=re.match('Morning',x)
# print(y)    #o/p    y=re.match('Morning',x)


# x='Morning class' 
# import re
# y=re.match('Morning',x)
# print(y.start()) 


# x='Morning class' 
# import re
# y=re.match('Morning',x)
# print(y.end())   #o/p 7

# x='Morning class' 
# import re
# y=re.match('Morning',x)
# print(y.group())    #o/p Morning


# # if element is present at the beggining then it will show object address
# # otherwise it will show none
# x='Morning class' 
# import re
# y=re.match('ing',x)
# print(y)     #o/p None

# #FULLMATCH
# x='moring class'
# import re
# a=re.fullmatch('moring class',x)
# print(a)   #o/p <re.Match object; span=(0, 12), match='moring class'>
# print()
# b=re.fullmatch('ing',x)
# print(b)   #o/p<re.Match object; span=(0, 12), match='moring class'>
# print()
# c=re.fullmatch('class',x)
# print(c)   #o/p None

# #search()
# s='good luck'
# import re
# e=re.search('g',s)
# print(e)   #o/p <re.Match object; span=(0, 1), match='g'>
# print()
# e1=re.search('luck',s)
# print(e1)   #o/p <re.Match object; span=(5, 9), match='luck'>
# print()
# e2=re.search('o',s)
# print(e2)   #o/p  <re.Match object; span=(1, 2), match='o'>
# #always consider first one if duplicate data
# print()
# e3=re.search('v',s)
# print(e3)   #o/pNone

# #finditer()
# d='python assignment'
# import re
# d1=re.finditer('s',d)
# # for i in d:
# #     print(i)
# print(d1)
# print()
# d2=re.finditer('v',d)
# print(d2)

# #sub()
# x='good luck'
# import re
# y=re.sub('o','*',x)
# print(y)   #o/p g**d luck
# print()
# y1=re.sub('o','*',x,1000)
# print(y1)  #not  show any erreo it will replace 2 and other 998 will ignor

# #subn()
# x='good luck'
# import re
# y=re.subn('o','*',x)
# print(y) #o/p ('g**d luck', 2)
# print()
# y1=re.subn('o','$',x,300)
# print(y1)  #  y1=re.subn('o','$',x,300)

# #findall
# s='Good Luck Guys Well Come To All0123'
# import re
# x=re.findall('[a-z]',s)  #..if i missing ' 'it will show name error
# print(x)  #o/p['o', 'o', 'd', 'u', 'c', 'k', 'u', 'y', 's', 'e', 'l', 'l', 'o', 'm', 'e', 'o', 'l', 'l']
# print()
# x1=re.findall('[A-Z]',s)
# print(x1)  #o/p['G', 'L', 'G', 'W', 'C', 'T', 'A']
# print()
# x3=re.findall('[0-9]',s)
# print(x3)   #op ['0', '1', '2', '3']
# print()
# x4=re.findall('[^abc]',s)
# print(x3)
# #o/p['G', 'o', 'o', 'd', ' ', 'L', 'u', 'k', ' ', 'G', 'u', 'y', 's', ' ', 'W', 'e', 'l', 'l', ' ', 'C', 'o', 'm', 'e', ' ', 'T', 'o', ' ', 'A', 'l', 'l', '0', '1', '2', '3']
# print()
# x5=re.findall('[A-Za-z]',s)
# print(x5) #op ['0', '1', '2', '3']

# w='All all 234456 #$%^&'
# #want to print only number
# import re
# e=re.findall("\d",w)
# print(e)  #op ['2', '3', '4', '4', '5', '6']
# e1=re.findall("\d+",w)
# print(e1)  #o/p['234456']
# #to avoide erre
# e2=re.findall(r'\d',w)
# print(e2)
# print()
# '''
# ----------------------------------------------------------------------
#   /d consider only number
#  /D  will consider  apart fronm number
# ---------------------------------------------------------------------
# '''
# e=re.findall("\D",w)
# print(e)  #op ['A', 'l', 'l', ' ', 'a', 'l', 'l', ' ', ' ', '#', '$', '%', '^', '&']

# # want to take emplty string
# # two ways    :
# # 1)   " "
# #2)    /s
# e6=re.findall(" ",w)
# print(e6)  #op[' ', ' ', ' ']
# print()
# e7=re.findall('\s',w)
# print(e7)   #op [' ', ' ', ' ']

import re
x='qcvbt 1234QAWE@#$%'
y=re.findall('\\s',x)
print(y)
print()
y1=re.findall('\\S',x)
print(y1)
print()
y2=re.findall('\n',x)
print(y2)

# y='Morning good'
# import re
# e=re.findall('^Mor',y)
# print(e)     #op ['Mor']
# print()
# e1=re.findall('^or',y)
# print(e1)    #op []
# #endswith                                #  not get op cross check
# e2=re.findall('$od',y)
# print(e2)    #o/p []
# e3=re.findall("$do",y)
# print(e2)
# e4=re.findall("$good",y)
# print(e4)


# d='aaadaabbbbbbaaa'
# import re
# t=re.finditer("a",d)   #exatly only "a" data will showing
# for i in t:
#     print(i)
# #op
# # <re.Match object; span=(0, 1), match='a'>
# # <re.Match object; span=(1, 2), match='a'>
# # <re.Match object; span=(2, 3), match='a'>
# # <re.Match object; span=(4, 5), match='a'>
# # <re.Match object; span=(5, 6), match='a'>
# # <re.Match object; span=(12, 13), match='a'>
# # <re.Match object; span=(13, 14), match='a'>
# # <re.Match object; span=(14, 15), match='a'>

# d='aaadaabbbbbbaaa'
# import re
# t=re.finditer("a+",d)  #it will showing group format
# for i in t:
#     print(i)
# #op
# # <re.Match object; span=(0, 3), match='aaa'>
# # <re.Match object; span=(4, 6), match='aa'>
# # <re.Match object; span=(12, 15), match='aaa'>

# d='aaadaabbbbbbaaa'
# import re
# t=re.finditer("a*",d)  # group format output but it will include empty space' ' means it "a" not match it will show empty space
# for i in t:
#     print(i)
# #op 
# # <re.Match object; span=(0, 3), match='aaa'>
# # <re.Match object; span=(3, 3), match=''>
# # <re.Match object; span=(4, 6), match='aa'>
# # <re.Match object; span=(6, 6), match=''>
# # <re.Match object; span=(7, 7), match=''>
# # <re.Match object; span=(8, 8), match=''>
# # <re.Match object; span=(9, 9), match=''>
# # <re.Match object; span=(10, 10), match=''>
# # <re.Match object; span=(11, 11), match=''>
# # <re.Match object; span=(12, 15), match='aaa'>
# # <re.Match object; span=(15, 15), match=''>

# d='aaadaabbbbbbaaa'
# import re
# t=re.finditer("a?",d)  
# for i in t:
#     print(i)
# #o/p 
# # <re.Match object; span=(2, 3), match='a'>
# # <re.Match object; span=(3, 3), match=''>
# # <re.Match object; span=(4, 5), match='a'>
# # <re.Match object; span=(5, 6), match='a'>
# # <re.Match object; span=(6, 6), match=''>
# # <re.Match object; span=(7, 7), match=''>
# # <re.Match object; span=(8, 8), match=''>
# # <re.Match object; span=(9, 9), match=''>
# # <re.Match object; span=(10, 10), match=''>
# # <re.Match object; span=(11, 11), match=''>
# # <re.Match object; span=(12, 13), match='a'>
# # <re.Match object; span=(13, 14), match='a'>
# # <re.Match object; span=(14, 15), match='a'>
# # <re.Match object; span=(15, 15), match=''>

# #  question  :      WANT TO PRINT FILE NAME  
# d=['Python.py','java.py','sql.py','sql.pdf']
# import re
# #want only file name
# #have to apply looping /becaude all data comimg outside
# for i in d:
#     data=re.findall('[A-Za-z]',i)   #source of string is   i   here
#     print( data)
# #o/p
# # ['P', 'y', 't', 'h', 'o', 'n', 'p', 'y']
# # ['j', 'a', 'v', 'a', 'p', 'y']
# # ['s', 'q', 'l', 'p', 'y']
# # ['s', 'q', 'l', 'p', 'd', 'f']
# '''
# #NOTE    :
# join()   
# SYNTAX   "joining_char".join(iter)
# '''
# x='python' 
# '*'.join(x)
# #o/p  p*y*t*o*n

# d=['Python.py','java.py','sql.py','sql.pdf']
# import re
# #want only file name
# #have to apply looping /becaude all data comimg outside
# for i in d:
#     data=re.findall('[A-Za-z]',i)   #source of string is   i   here
#     print(" ".join (data))
# #op
# # P y t h o n p y
# # j a v a p y
# # s q l p y
# # s q l p d f

# d=['Python.py','java.py','sql.py','sql.pdf']
# import re
# #want only file name
# #have to apply looping /becaude all data comimg outside
# for i in d:
#     data=re.findall('[A-Za-z]+\.',i)   #source of string is   i   here
#     print(" ".join (data))
# #o/p
# # Python.
# # java.
# # sql.
# # sql.


# d=['Python.py','java.py','sql.py','sql.pdf']
# import re
# #want only file name
# #have to apply looping /becaude all data comimg outside
# for i in d:
#     data=re.findall('[A-Za-z]+\.[A-Za-z]',i)   #source of string is   i   here
#     print(" ".join (data))
# #o/p
# # Python.p
# # java.p
# # sql.p
# # sql.p

# ##                                        FINAL ANSWER
# d=['Python.py','java.py','sql.py','sql.pdf']
# import re
# #want only file name
# #have to apply looping /becaude all data comimg outside
# for i in d:
#     data=re.findall('[A-Za-z]+\.[A-Za-z]+',i)   #source of string is   i   here
#     print(" ".join (data))
# # o/p
# # Python.py
# # java.py
# # sql.py
# # sql.pdf

# z=['1234-4566=7890','1111-2222-3333']
# #want only 2 nd list number  ^
# import re
# for i in z:
#     r=re.findall('[0-9]{4}-[0-9]{4}-[0-9]{4}',i)
#     print(r)   #want to make so use {}
# #o/p   ['1111-2222-3333']


# #  NOTE :   REGULAR EXPRESSION DON'T SUPPORT  LIST DATA  SO WE USE FOR LOOP AND TAKE THAT DATA OUTSIDDE

# s='ABCD4567R'
# # print given  pan card number
# #   NO NEED TO APPLY FOR LOOP BECAUSE DATA in string format
# import re
# x=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',s)
# print(x)
# #o/p  ['ABCD4567R']

#                                              ASSIGNMENT
#  REGULAR EXPRESSION EXAMPLE

# # #1.matches any number between 0-9
a="The cost of the book is Rs.100"
import re
b=re.findall('[0-9]',a)
print(b)
# #o/p   ['1', '0', '0']

b=re.findall('[0-9]+',a)
print(b)
# ['100']


# # #2.matches only lower case letter and upper case letter
b="hello HOW ARE YOU"
import re
c=re.findall('[A-Za-z]',b)
print(c)
# #o/p ['h', 'e', 'l', 'l', 'o', 'H', 'O', 'W', 'A', 'R', 'E', 'Y', 'O', 'U']

c=re.findall('[A-Za-z]+',b)
print(c)
# ['hello', 'HOW', 'ARE', 'YOU']

c=re.findall('\\w',b)
print(c)
# ['h', 'e', 'l', 'l', 'o', 'H', 'O', 'W', 'A', 'R', 'E', 'Y', 'O', 'U']

c=re.findall('\\w+',b)
print(c)
# ['hello', 'HOW', 'ARE', 'YOU']



# #3.write a program to count the number of white space in a given string
c="HELLO world welcome to python Hi how are you. Hi how are you"
import re
s=re.findall(' ',c)
print(len(s))
# 12

s=re.findall('\\s',c)
print(len(s))
# 12

s=re.findall('\\W',c)  #don't use this ...it can also consider the special characters in the count
print(len(s))
# 13  

print()

# # #4.sum all the numbers in the below string
word="PYTHON12nREG567exp2"
sum=0
match=re.findall('[0-9]',word)
for i in match:
    match=re.findall('[0-9]',i)
    sum+=int(i)
print(sum)
#23
print()



# # #5.matches everything apart from numbers between 0-9
a="The cost of the book is Rs.100"
s=re.findall('[^0-9]',a)
print(s)
# ['T', 'h', 'e', ' ', 'c', 'o', 's', 't', ' ', 'o', 'f', ' ', 
# 't', 'h', 'e', ' ', 'b', 'o', 'o', 'k', ' ', 'i', 's', ' ', 'R', 's', '.']

s=re.findall('\\D+',a)
print(s)
# ['The cost of the book is Rs.']



# # #6.matches everything apart from "a","b","c","d"
b="abcdefghijklmnop"
x=re.findall('[^abcd]',b)
print(x)
# ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']



#7.matches only numbers
word="@hello12world34welcome!123"
a=re.findall('[0-9]',word)
print(a)
# ['1', '2', '3', '4', '1', '2', '3']

a=re.findall('[0-9]+',word)
print(a)
# ['12', '34', '123']


#8.extracting file with extension
s="Downloading archive.zip file to download folder python hero.py and afternoon.txt and slicing.jpeg"
a=re.findall('[A-Za-z]+\.[A-Za-z]+',s)
print(a)
# ['archive.zip', 'hero.py', 'afternoon.txt', 'slicing.jpeg']


#9.wap to extract only pincode
s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
a=re.findall(r'\b\d{6}\b',s)
print(a)
# ['560001']


print()

# # 10.wap to print the AADHAR CARD numbers
s="my aadhar number is 1234-4567-8910"
a=re.findall(r'\b\d{4}-\d{4}-\d{4}\b',s)
print(a)
# ['1234-4567-8910']



# # 11.wap to print the pan card number
a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
x = re.findall(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', a)
print(x)
# ['ABCDE1234X', 'PQRST5678W']


# # 12.How to fetch the protocols
a="https://www.google.com"
x=re.findall('[a-z]+',a)
print(x)
# ['https', 'www', 'google', 'com']

y=re.findall('.+',a)
print(y)
# ['https://www.google.com']


# # o/p--->['https', 'www', 'google', 'com'] (i want first output like this )
# # o/p--->['https://www.google.com']        (second output)


print()

# # 13.creating acronyms of the file format

file_format=["Graphic Interchange Format",
              "Advanced Audio Coding",
            "HyperText Markup Language",
             "Content Management System",
            "Windows Media,Audio",
            "Comma Separated Values"]
for i in file_format:
    x=re.findall('[A-Z]',i)
    print("".join(x),end=" ")

    
# GIF
# AAC
# HTML
# CMS
# WMA
# CSV

# # o/p-->GIF,AAC,HTML,CMS,WMA,CSV

print()

# # 14.wap to match email ids
emails=["test.user@company.gov","test_user@company.edu","123test-T.user@company.in","testing@company","pspider@company.in"]



print()

# # 15.matching phone numbers
phonenumbers=["123-345-0987","456-9832-098","800-987-4756","080-1029384727","123-345-12","900-938-0987"]
for i in phonenumbers:
    x=re.findall('[0-9]{3}-[0-9]{3}-[0-9]{4}',i)
    print(x)


# 16.replace whitespace with newline characters

s="helloworld welcome to python"
w=re.sub("\s","\n",s)
print(w)

# helloworld
# welcome
# to
# python

#17 replace all digits with **
s="hello 123 mic testing 123 123"
w=re.sub('[0-9]+','**',s)
print(w)
# hello ** mic testing ** **