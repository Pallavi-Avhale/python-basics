"""Inbuilt function
1.reversed(): 
reverse()only support for list data type
    - show attribute error using this data type (str,dict,tuple1)
But reversed() supports all the iterables
when we want to reverse the selected iterable we go for reversed
-Syntax---> reversed(iterable)    
-also we can use ---> 1.String(directly)
                    2.list(directly)
                    3.tuple  (directly)     
                    4.set (not directly)   
                    5.Dict(not directly)

- when we use reversed function to reverse any iterable then  we will get the output as OBJECT ADDRESS:
-to avoid the object address we have two methods---->
1. Typecasting (use list,tuple,set
don't go for string--->will give the output as the object address, and dict--->it will not support)

2. Looping
-->syntaxt for looping for reversed function
---------------------------------------------
for variable in iterable:
    statement
---------------------------------------------



                    
"""
a="welcome"
print(reversed(a)) #it will give object address and no output
#typecasting
print(list(reversed(a)))
print(tuple(reversed(a)))
print(set(reversed(a)))
# print(dict(reversed(a)))
print(str(reversed(a)))   # will give object address
# print(dict(reversed(a)))

#looping reversed 
k=[10,20,33,43,55]
print(k)
for i in reversed(k):
    print(i,end=" ")

print()


for i in reversed(range(1,6,1)):
    print(i,end=",")

print()
#reverse the string
#method1:
s="Python Class"
for i in s[::-1]:
    print(i,end="")
print()

#method2:
for i in range(-1,-13,-1):
    print(s[i],end=" ")

print()    

#method 3:
for i in reversed(range(0,12,1)):
    print(s[i],end=" ")
print()

#method 4:
for i in reversed(s):
    print(i,end=" ")
print()

#method 5: without using inbuilt function( using concatination)
res=" "
for i in s:
    res=i+res
print(res) 

"""enumerate()
when we want to print element/character as well as its position
 in iterable we go for enumerate(without using  range function)
return type is tuple
the output will be Object address here
to avoid this we do
1.typecasting
-works with list,tuple,dict
2. looping

----->syntax
-----------------------
1. enunerate(iterable)
---------------------------------------
2. for variable in enumerate(iterable):
        statement

---------------------------------------
methods------>
1. typecasting:
ex-
y='After'
print(enumerate(y))--->object address
print(list(enumerate(y)))----->[(0, 'A'), (1, 'f'), (2, 't'), (3, 'e'), (4, 'r')]

----don't go for set it will give unorder output
ex-print(set(enumerate(y)))------>{(0, 'A'), (1, 'f'), (2, 't'), (3, 'e'), (4, 'r')}

2.Looping:
ex-for i in enumerate(y):
    print(i)------------------>
(0, 'A')
(1, 'f')
(2, 't')
(3, 'e')
(4, 'r')



"""

y='After'
print(enumerate(y)) #object address
#to avoid object address
#1.typecasting
print(list(enumerate(y)))
print(tuple(enumerate(y)))
print(dict(enumerate(y)))
print(set(enumerate(y)))

#2.looping
for i in enumerate(y):
    print(i)   #we will get output in packed format

#use char and position as i and j
#will get the output without boundary condition
for i,j in enumerate(y):
    print(i,j) 
print()  

#start the indexing with 1position--->start part is optional
e="SQL"
for i in enumerate(e,start=1):
    print(i)

# ----------------------------------
# example2

d=[1,2,3,4,5]
#1.typecasting
print(enumerate(d))
print(list(enumerate(d)))

#2.looping
for i in enumerate(d):
    print(i)
    #we will get o/p in tuple but if want in unpacked format then we go for :

for i,j in enumerate(d):
    print(i,j)


for i in enumerate(d,start=2):
    print(i)

# for i,j in enumerate(d):
#     print(i,j,start=3)-----(cannot do this )

""""zip()---->
is inbuilt function
directly if we done any operation it will display object address
-when we want to match poistion to position then we go for zip function
----> syntax:
----------------------------------------
zip(iterable1,iterable2,iterable3,...)
-----------------------------------------
we can pass any type of iterable but the iterable length should be same, 
if length is different data loss will happen.
ex- x=[1,2,3,4]
y=[11,12]
output=== will get only 2 elements,2elements of x will be loss
 to avoid data loss we go for zip_longest

"""

#zip
a=[11,12,13,14,15]
b='python'
print(list(zip(a,b)))
print(tuple(zip(a,b)))
print(dict(zip(a,b)))
print(set(zip(a,b)))

x=(20,30,40,50,60)
y="HI"
z={1,2,3}
e=[11,12]
print(list(zip(x,y,z,e)))
for i in zip(x,y,z,e):
    print(i)

""""zip_longest():(in zip data loss happens to avoid data loss we go for zip_longest)
-by default it will take value none, 
from itertools import zip_longest
---->syntax:
-----------------------------------
from itertools import zip_longest
print(zip_longest(iterable1,iterable2,,...)) #object address
--------------------------------------------------------------
to avoid object address go for typecasting(list, tuple,set,dict)
--> print(list(zip_longest(iterable1,iterable2,....)))
--> print(tuple(zip_longest(iterable1,iterable2,....)))
--> print(set(zip_longest(iterable1,iterable2,....)))
--> print(dict(zip_longest(iterable1,iterable2,....)))

or go for looping:
looping syntax--->
---------------------------------------------------
for i in zip_longet(iterable1,iterable2,....):
    statement

NOTE- return type is tuple

"""

a='pen'
b=[1,2]
c=(10,)
from itertools import zip_longest
print(list(zip_longest(a,b,c)))
print()

#looping
for i in zip_longest(a,b,c):
    print(i)
print()

for i in zip_longest(a,b,c,fillvalue=100):
    print(i)

    '''
    SORTED AND SORT(pending)
    '''


s='Good day wasted'
x={}
for i in s:
    x.update({i:ord(i)})
print(x)

for i in s:
    x[i]=ord(i)
print(x)

a=[1,2,3,4]
b=[11,12,13,14,15]
print(list(enumerate(a)))
print()

for i,j in enumerate(b):
    print(i,j)
print()

print(list(reversed(a)))
print(tuple(reversed(a)))
print(set(reversed(a)))  #not working
# print(dict(reversed(a)))#Typeerror

for i in reversed((1,2,3)):
    print(i)

print()
print(sorted(b,reverse="True"))
# print(sorted(b,key="len"))

s="Heyyy guyzz"
for i in s:
    ...
print(i)

s="helloo hiii"
print(s.split())
print(s.split("l"))
print(s.split("o",-7))

a=(1,2,3,2)
print(a.index(2,2))

d={"a":10,"b":20,"c":30}
print(d.get("e"))  #none
print(d.get("f","not found"))
# print(d["d"]) #keywrror

print(d.values())
d.update({"d":40,"e":50})
# print(d)
d["f"]=60
print(d)

print(d.setdefault("z",100))
print(d)

print(d.fromkeys("Hey",1000))
print(d)
print(d.pop("w","not found"))
print(d.popitem())

print(0.1+0.2==0.3)