# wap to create a dict with letter and its words starting with that letter pair 
#s="hi hello good morning welcome to python session"
#o/p{'h':['hi','hello'], 'g':[good]}

#s="hi hello good morning welcome to python session"
#a={}
#for i in s.split():
#    #print(i)   #without using inbuild
#    if i [0] not in a:
#        a[i[0]]=i
#    else:
#        a[i[0]]]+=[i]
#print(a)
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#s="hi hello good morning welcome to python session"
#y={}
#for i in s.split():
#    y.setdefault(i[0],[]).append(i)
#print(y)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# 22.wap to create a dictionary of
# characters and its indices pair
#s="hello python"
# o/p:-->{"h":[0,9],"e":1..........}




#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#s="hello python"
#d=[1,2,3,4,5,6,7,1,2,3,4]
#a=[]
#for i in d:
#    if i not in a:
#        a.append(i)
#    else:
#        print(i)
#print(a)
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#28.wap to print first and last char of each name in the list
#a=["Sunil","anil","Suresh","Mahesh","Dinesh"]
#s=[]
#for i in range(len(a)):
#    print(a[i][0],a[i][-1])
    
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#29.wap to create a new list as square of each number of below list
#b=[2,4,5,6,7,1]
#a=[]
#for i in b:
#    a.append(i**2)
#print(a)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#30.wap if number is even the print its square else print its cube
#c=[2,4,5,3,7,9]
#cub=[]
#sq=[]
#for i in c:
#   if i%2==0:
#        sq.append(i**2)
#    else:
#        cub.append(i**3)
#print("sq list", sq)
#print("cube List", cub)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#31.wap to create a list with square and cube of each numbers
#d=[2,4,5,1,8,9,10]
# o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]

#d=[2,4,5,1,8,9,10]
#lst=[]

#for i in d:
#    lst.append((i**2,i**3))
#print(lst)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#32.wap to create a new list of reversing each name from the list
#names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
#lst=[]

#for i in names:
#    r=i[::-1]
#    lst.append(r)
#print(lst)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#33.wap to create a new list, of individual and collection data type from list
#data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]
#s=[]
#m=[]
#for i in data:
#    if isinstance(i,(int,float,complex,bool)):
#        s.append(i)
#    else:
#        m.append(i)
#print("svd",s)
#print("mvd",m)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#34.wap to print author name in books dictionary
#books={"love story":["Harish",30],"biography":["padam",150],"animals":["vimala",75]}

#for i in books:
#    print(books[i][0])

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# #35.wap to group fruit name and country pair
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}

# a=[]
# f=list(d.keys())
# c=list(p.keys())
# for i in range(len(f)):
#     a.append((f[i],c[i]))
# print(a)

# #1. WAP to convert a word into upper case (without useing inbuilt function)
# s = 'Python@1991'
# #exp o/p: 'PYTHON@1991'

# s = 'Python@1991'
# res=' '
# for i in s:
#     if ord("a")<=ord(i)<=ord("z"):
#         res=res+chr(ord(i)-32)  #empty string(res)=empty string(res)
#     else:
#         res=res+i
    
# print(res)



# #2.WAP to count number of vowels present
# # in given string
# a = 'GooD mOrnIng'


# #3.WAP to extract & store the extensions of files in a list
# l = ['forloop.txt', 'http://python.py', 'while.pdf', 'functions.pptx',
#    'lambda.png', 'http://map.py', 'python.pdf', 'http://oops.py']

# #o/p:-['txt', 'py', 'pdf', 'pptx', 'png', 'py', 'pdf', 'py']

# l = ['forloop.txt', 'http://python.py', 'while.pdf', 'functions.pptx',
#     'lambda.png', 'http://map.py', 'python.pdf', 'http://oops.py']

# k=[]
# for i in l:
#     res=i.split(".")
#     k.append(res[1])
# print(k)

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 



# #4.WAP to extract only file names
#  w = ['forloop.txt', 'http://python.py', 'while.pdf', 'functions.pptx',
# 'lambda.png', 'http://map.py', 'python.pdf', 'http://oops.py']

# #o/p ['forloop', 'python', 'while', 'functions', 'lambda', 'map', 'python', 'oops']

#  w = ['forloop.txt', 'http://python.py', 'while.pdf', 'functions.pptx',
# 'lambda.png', 'http://map.py', 'python.pdf', 'http://oops.py']
# k=[]
# for i in l:
#     res=i.split(".")
#     k.append(res[0])
# print(k)


# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 
# 5.WAP to return a dictionary with word & its len pair
# from a string
# string = 'hello good morning how are youu'
# #exp o/p : {hello:5, guys:4, morning:7, how:3, are:3, you:4}

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 
# 6.WAP to get the given o/p
# s = 'hi hello good morning'
# #exp o/p: 'gninrom doog olleh ih'

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 

# #7. WAP to check the given number is armstrong or not
# #Armstrong : Sum of cube of the digits
# a=153
# b=str(a)   #----->'153' (string is iterable)
# c=len(b) #------> len of b is 3
# res=0
# for i in b:   #'153'
#     res=res+int(i)**c
# if res==a:g
#     print('armstrong')
# else:
#     print('not armstrong')



# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 

# #8.WAP to get below o/p:
# s = 'Hi how are you'
# # exp o/p : 'iH woh era uoy'
# s = 'Hi how are you'
# res=' '
# for i in s.split():
#     res+=i[::-1]+' '
# print(res)



# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 
# #9..WAP to count the numbers of white spaces in a given string
# s = 'hai hello how are you good to see you'
# space=0
# for i in s:
#     if i.isspace():
#         space=space+1
# print(space)
# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 
# #10.WAp to count number of capital letters in a string
# s = 'Hi How are you Welcome to Python & its Fun'

# up=0    #upper_case=0
# for i in s:
#     if i.isupper():
#         up=up+1
# print(up)

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 
# #11.WAp to sort the list which is mix of both even & odd,
# #the sorted list should have odd numbers first & then even numbers
# #in sorted order
# # #odd ->[1,3,7,9,11,13] even-> [2,4,8,12,16]
# l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]

# even=[]
# odd=[]
# for i in l:
#     if i%2==1:
#         odd.append(i)
#     else:
#         even.append(i)

# print(sorted(odd))    #arranging numbers in asc to desc use sorted 
# print(sorted(even))



# sorted----sorted(iterable)
# s="python"
# print(sorted(s))

# print(ord("P"))
# print(ord("y"))
# print(ord("t"))
# print(ord("h"))
# print(ord("o"))
# print(ord("n"))



# y=[]
# for i in sorted(y,reversed=True):
#     # print(i)

# sorted on length
# s=["abc","python", "Rock", "walmart", "a", "ab"
# ]
# print(sorted(s,key=len,reverse))


# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 
# #12..WAp to sort the list which is mix of both even & odd,
# #the sorted list should have odd numbers first & then even numbers
# #in Descending order

# l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]

# even=[]
# odd=[]
# for i in l:
#     if i%2==1:
#         odd.append(i)
#     else:
#        even.append(i)

# print(sorted(odd, reverse=True))    #arranging numbers in asc to desc use sorted 
# print(sorted(even,reverse=True))


# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
# shirt=["Red","Yellow","Black"]
# pants=["White","Grey","Blue"]
# for i in shirt:
#     for j in pants:
#         print(i,j)

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
# shirt=["Red","Yellow","Black"]
# pants=["White","Grey","Blue"]
# for i in shirt:
#     print(i)
#     for j in pants:
#         print(j)
 
# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
# total=0
# for i in range(1,5):
#     for j in range(1,5):
#         total=total+1
# print(total)
    
# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------


# total=0
# for i in range(1,5):
#     total=total+1    #total of outer for loop run (4 times)
#     for j in range(1,5):
#         ...      
# print(total)
# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------

# s=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# for i in s:
#     for j in i:
#         if j%2==0:
#             print(j)
# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------

# for i in range(1,11):
#     for j in range(1,11):
#        print(i*j, end='\t')    #\t use to give one tab space, arrange in table formate.
#     print()

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end='\t')    
#     print('/n')

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------

# student={"A": {"Name": "kiran", "age":45}, "B":{"Name": "rock", "age":55}}
# for i in student:
#     for j in student[i]:
#         print("keys",i,"|",j,":", student[i][j])

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
 
#otherway--->
# student={"A": {"Name": "kiran", "age":45}, "B":{"Name": "rock", "age":55}}
# for i in student:
#      for j in student[i]:
#          print("outer_keys",i,"inner_keys",j,":", student[i][j])

# -------------------------------------------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------------------------
  
# total=0
# for i in range(1,11):
#     for j in range(1,11):
#         if (i+j)%2==0:
#             total=total+1
# print("total count of even no.", total)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
 
# wap to print longest word in a sentence
# s='life is full of surprises and miracles'
# #exmple---- o/p: surprises

# s='life is full of surprises and miracles'
# res=' '
# max_length=0
# for i in s.split():
#     if len(i)>max_length:
#         max_length=len(i)
#         res=i
# print(res)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# for days in range(1,4):
#     print("days", days)
#     for meals in range(1,4):
#         print("meals",meals)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# for i in range(1,3):
#     print(i) #o/p-->1,2
#     for j in range(1,3):
#         print(j)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# for i in range(1,6): 
#     print(i) #o/p-->1,2,3,4,5
#     for j in (1,6):
#         print(j)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Assignment Questions
# -----------------------------------------------
# 1.Wap to Count total vowels in each 
#  word using nested loop.
# words = ["python", "loop", "data"]

# words = ["python", "loop", "data"]
# for i in words:
#     count=0
#     for j in i:
#         if j in "AEIOUaeiou":
#             count+=1
#      print(i, "vowel count", count)


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 2.wap to Find Common Elements in Two Lists
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# for i in a:
#     for j in b:
#         if i==j:
#             print("common elements", j )
    
   
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 3.wap to Count Matching Characters
# Between Two Strings

# s1 = "abc"
# s2 = "bcd"
# count=0
# for i in s1:
#     for j in s2:
#         if i==j:
#             count+=1
# print('matching count', count)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 4.Flatten 2D List (convert 2d to 1d)
# l = [[1, 2], [3, 4], [5, 6]]

# l = [[1, 2], [3, 4], [5, 6]]
# a=[]
# for i in l:
#     for j in i:
#         a.append(j)
# print(a)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# http://5.You have a dictionary of students and 
# their subject marks Print total marks of 
# each student.

# students = {
#     "A": {"math": 80, "science": 70},
#     "B": {"math": 60, "science": 90},
#     "C": {"math": 75, "science": 85}
# }

# output:->
# A Total Marks: 150
# B Total Marks: 150
# C Total Marks: 160

# students = {
#     "A": {"math": 80, "science": 70},
#     "B": {"math": 60, "science": 90},
#     "C": {"math": 75, "science": 85}
# }

# for i in students:
#     total=0
#     for j in students[i]:
#         total = total + students[i][j]
#     print(i, "total marks", total)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
#wap to Count Total Elements in 2D List
# l = [[1,2,3],[4,5],[6,7,8]]
# for i in l:
#     count=0
#     for j in i:
#         count+=1
# print(j)

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# words Starting with Same Letter
# words = ["apple","ant","bat","ball"] 
# count=0
# for i in words:
#     for j in i:
#         if i[0]==j[0]:
#             count=count+1
#             print(j, "----->", count)


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#wap to sum of Total Elements in 2D List
# l = [[1,2,3],[4,5],[6,7,8]]
# total=0
# for i in l:
#     for j in i:
#         total=total+j
# print(total)            



# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#wap to print list element in ascending formate 
# x=[72,3,33,14,5,21,0.5,1,7]
# for i in range(len(x)):
#     # print(i,end=" ")
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
# print(x)

# explaination:
# 1st number 72 compaire with each and every elements in list like
# 72>3 ----- True swap [3,72,33,14,5,21,0.5,1,7] (why we take 72 and 3 coz at 0 position 72 is present and i is pointing to the 0 position and 3 is present at 1st position j will pointing to the 3 x[i]>x[j] )
# num 3 compare with each and every elements
# 3>72-- False
# 3>33-- False
# 3>14-- false  like wise still all the list get sorted 

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#  o/p: Aa,Bb,Cc,Dd,Ee....Zz
# a=ord("A")
# b=ord("a")
# for i in range(0,26):
#      print(chr(a+i), chr(b+i), end=" ")

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# 5.You have a dictionary of students and 
# their subject marks Print total marks of 
# each student.

# students = {
#     "A": {"math": 80, "science": 70},
#     "B": {"math": 60, "science": 90},
#     "C": {"math": 75, "science": 85}
# }

# output:->
# A Total Marks: 150
# B Total Marks: 150
# C Total Marks: 160

# for i in students:
#     total=0
#     for j in students[i]:
#         total=total+students[i][j] #students of [i] is inner key, students of [j] inner key
#     print("key",i, "total marks:", total)

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# wap to print shortest word in a sentence
# s='life is full of surprises and miracles'
# res=' '
# min_length=len(s) # s is a string and min_length is aggregate function hence we need to type caste s from str to int (len(s))
# for i in s.split():
#     if len(i)<min_length:
#         min_length=len(i)
#         res=i
# print(res)

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# x='a4b3c5'
# # o/p: aaaabbbccccc
# res=' '
# for i in range(len(x)):
#     # print(i) #012345 position x[i]---> x[0]--->a
#     if x[i].isalpha(): #'a':isalpha() ---> if it is true like a.isalpha()---> true
#         y=x[i]    #--->y=x[i]-->a
#     else:
#         res=res+y*int(x[i])   #res='a'*4=aaaa 
# print(res)

