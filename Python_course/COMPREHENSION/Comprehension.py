'''comprehension is a short and easy way to create a iterable or collection 

Disadvantage:-we cannot use intermediate termination(break,continue and pass).
             -we cannot use while loop because we cannot initialize or update our looping variable.
             -we cannot use argument assignment operations.
             -Also we cannot use Assignment operator also.
             -we cannot handle our exception in comprehension.

-Supports for:List,set and dict
(does not support str because it will consider complete expression as string)
(does not support for the tuple because it will generate generator object not tuple object)

comprehension is of three types:
1. List comprh.
---> it is an elegant way of writing and creating a new list based upon the existing iterable

Advantages of list compr:
it is easy to read
reduces time and space complexity

-------------------------------------------------
syntax 1: when we don't have any conditions
-----> varname=[expression for var in iterable]
-------------------------------------------------

::expression- means main task we have to perform

-----------------------------------------------------------
syntax2:when we have only if condition
-----> varname=[expression for var in iterable if condition]
-----------------------------------------------------------

--------------------------------------------------------------------
syntax3: when we have both if and else condition:
----> varname=[expression(TSB) if condition else FSB for var in iterable]
---------------------------------------------------------------------

2. Set comprh.
-->  


3. Dictionary Comprh.


'''

#list comprehension
#without any condition
print([i for i in range(1,6)])
'''
using only for loop
l=[]
for i in range(1,6):
    l.append(i)
print(l)'''

ll=['jaggu','sizuka','nobita']
# o/p=['JAGGU','SIZUKA','NOBITA']
'''normal way
lst=[]
for i in ll:
    lst.append(i.upper())
print(lst)'''

#using list comprehension
print([i.upper() for i in ll])

#syntax2: using condition
'''printing even no. from 5 to 15

for i in range(5,16):
    if i%2==0:
        print(i,end=",")
        '''
#using list compr
print([i for i in range(5,16) if i%2==0])

#syntax3: with if else
'''if no. is odd from1-10 store the no. as it is, if no. is even then store cube of the no.
for i in range(1,11):
    if i%2==1:
        print(f'{i}',end=",")
    else:
        print(f'{i**3}',end=",")'''

print([i if i%2==1 else i**3 for i in range(1,11)])

#odd-cube,even-square
l=[2,3,5,1,7,2,3]
print([i**2 if i%2==0  else i**3 for i in l])

#wap to take two lists as input and add that elements and return a single lists
# l1=eval(input('enter a list1'))
# l2=eval(input('enter a list2'))
# for i,j in zip(l1,l2):
#     print(i+j)

# print([i+j for i,j in zip(l1,l2)])

#wap to check length of str present in tuple, if leb is eve-append it as it is , else reverse it and append
l=('hey','hello','good','evenings','python')
print([i if len(i)%2==0 else i[::-1] for i in l])


#wap to craete a list containing tuples having two elements that is index and value of list
l=('hey','hello','good','evenings','python')
print([(i,j) for i,j in enumerate(l)])
'''
assignment
1. Extract Digits from String
s = "a1b2c3d4"
Output ['1','2','3','4']

2. Replace negative numbers with 0
l = [5,-3,7,-2,9]
Output [5,0,7,0,9]

3. Get length of words greater than 3
l = ['hi','python','java','c','django']
Output [6,4,6]

4. Remove spaces from string
s = "p y t h o n"
Output ['p','y','t','h','o','n'] 
'''

# 1. Extract Digits from String
s = "a1b2c3d4"
print([i  for i in s if i.isdigit()])

# 2. Replace negative numbers with 0
l = [5,-3,7,-2,9]
print([0 if i<0 else i for i in l])

# 3. Get length of words greater than 3
l = ['hi','python','java','c','django']
print([len(i) for i in l if len(i)>3])

# 4. Remove spaces from string
s = "p y t h o n"
print([i for i in s if not(i.isspace())])

#5.extract only even no. and int data type
t=(99,25,6.2,'Hello',(2+5j))
'''
l=[]
for i in t:
    if isinstance(i,int):
        l.append(i)
print(l)
'''
print([i for i in t if isinstance(i,int)])
print([i for i in t if type(i)==int])

'''
2. SET COMPREHENSION
---> we cannot store immutable data type as a element in the set
---> it is an elegant way of writing and creating a new set based 
upon the existing iterable


-------------------------------------------------
syntax 1: when we don't have any conditions
-----> varname={expression for var in iterable}
-------------------------------------------------

::expression- means main task we have to perform

-----------------------------------------------------------
syntax2:when we have only if condition
-----> varname={expression for var in iterable if condition}
-----------------------------------------------------------

--------------------------------------------------------------------
syntax3: when we have both if and else condition:
----> varname={expression(TSB) if condition else FSB for var in iterable}
---------------------------------------------------------------------

'''

#SET comprh. example
#1. remove duplicate elements from the list and create a set
l=[22,58,99,22,65,58]
print({i for i in l})

#2. fetch only even element and store in set
print({i for i in l if i%2==0})

#3. extract only consonant character and store in the set
st='Doraemon'
print({i for i in st if i not in "AEIOUaeiou"})

#4. even-cube,odd-square
t=(5,9,2,7,6)
print({i**3 if i%2==0 else i**2 for i in t})

'''
DICTIONARY COMPREHENSION
---> it is an elegant way of writing and creating a
 new dict  based upon the existing iterable

-------------------------------------------------
syntax 1: when we don't have any conditions
-----> varname={key:value for var in iterable}
-------------------------------------------------

-----------------------------------------------------------
syntax2:when we have only if condition
-----> varname={key:value for var in iterable if condition}
-----------------------------------------------------------

----------------------------------------------------------------------------------
syntax3: when we have both if and else condition:
----> varname={key:value if condition else False-expression for var in iterable}
-----------------------------------------------------------------------------------

'''

#DICT COMPRH. example
#1. make the value as sqaure of the key in dict.
print({i:i**2 for i in range(1,6)})

#2, wap to create dict of values and index pair
l=['google','apple','python','orange']
print({l[i]:i for i in range(len(l))})

#3. even-as it is, odd-reverse
print({i:i if len(i)%2==0 else i[::-1] for i in l})

#4. wap to check elements is palindrome key and value 
# should be same else value is reverse of key
l=['banana','malayalam','madam','sir','mom','dad']
print({i:i if i==i[::-1] else i[::-1] for i in l})

'''NESTED COMPREHENSION
-->whenever we are using more than 1 for loop in comprehension then
 it is called nested comprehension

-------------------------------------------------
syntax 1: when we don't have any conditions
-----> varname={expression for var1 in iterable1  for var2 in iterable2}
                          ---------------------  {inner for loop}
                          {outer for loop}
-------------------------------------------------

-----------------------------------------------------------
syntax2:when we have only if condition
-----> varname={expression for var1 in iterable1 for var2 in iterable2 if condition}
                           {outer loop}           {inner loop}

                        ----------------------
                           for outer loop:
                            for inner loop:
                                if cond:
                                    statment
                        ---------------------------

                           OR

-----> [expression for outer loop if condition for inner loop if condition]
                   ------------------------------
                        for outer loop:
                            if condition:
                                for inner loop:
                                    statement
                    --------------------------------
-----------------------------------------------------------

----------------------------------------------------------------------------------
syntax3: when we have both if and else condition:
----> varname={key:value if condition else False-expression for var in iterable}
-----------------------------------------------------------------------------------

'''

#1. l=['Hi','Bye']   o/p: ['H','i','B','y','e']
'''normal way
ll=['Hi','Bye']
l=[]
for i in ll:
    for j in i:
        l.append(j)
print(l)'''

ll=['Hi','Bye']
print([j for i in ll for j in i])

#2. store character of the word whose len is even 
t=('chutki','Dholu','tuntun','Bheem','Indu')
print([j for i in t for j in i if len(i)%2==0])
print([j for i in t if len(i)%2==0 for j in i])

print([j for i in t if len(i)%2==0 for j in i if j in "AEIOUaeiou"])

'''
NESTED LIST COMPREHENSION:

------------------------------------------------------------------
syntax 1: when we don't have any conditions
-----> varname=[expression for var in iterable1 for var in iterable2]
                           {Outer for loop  }    {inner for loop   }

                           --------------------------------------
                           for var in iterable1:
                                for var in iterable2:
                                    expression
                           ----------------------------------
--------------------------------------------------------------

---------------------------------------------------------------------
syntax2:when we have only if condition
-----> varname=[expression for var in iterable1 for var in iterable2 if condition]
                           {outer for loop    } {inner for loop    }

                           ----------------------------------------
                           for var in iterable1:
                                for var2 in iterable2:
                                    if condition:
                                        expression
                            ---------------------------------------
---------------------------------------------------------------------

----------------------------------------------------------------------------------
syntax3: when we have both if and else condition:
----> varname=[TSB if condition else FSB for var in iterable1 for var in iterable2]
                                          {outer for loop   } {inner for loop     }

                                          -------------------------------------------
                                          for var iterable1:
                                                for var2 in iterable2:
                                                if condition:
                                                    tsb
                                                else:
                                                    fsb
                                        ---------------------------------------------
-------------------------------------------------------------------------------------


'''

'''
NESTED SET COMPREHENSION

------------------------------------------------------------------
syntax 1: when we don't have any conditions
-----> varname={expression for var in iterable1 for var in iterable2}
                           {Outer for loop  }    {inner for loop   }

                           --------------------------------------
                           for var in iterable1:
                                for var in iterable2:
                                    expression
                           ----------------------------------
--------------------------------------------------------------

---------------------------------------------------------------------
syntax2:when we have only if condition
-----> varname={expression for var in iterable1 for var in iterable2 if condition}
                           {outer for loop    } {inner for loop    }

                           ----------------------------------------
                           for var in iterable1:
                                for var2 in iterable2:
                                    if condition:
                                        expression
                            ---------------------------------------
---------------------------------------------------------------------

----------------------------------------------------------------------------------
syntax3: when we have both if and else condition:
----> varname={TSB if condition else FSB for var in iterable1 for var in iterable2}
                                          {outer for loop   } {inner for loop     }

                                          -------------------------------------------
                                          for var iterable1:
                                                for var2 in iterable2:
                                                if condition:
                                                    tsb
                                                else:
                                                    fsb
                                        ---------------------------------------------
-------------------------------------------------------------------------------------
'''

'''
NESTED DICTIONAY COMPREHENSION

------------------------------------------------------------------
syntax 1: when we don't have any conditions
-----> varname={Key:value for var in iterable1 for var in iterable2}
                           {Outer for loop  }    {inner for loop   }

                           --------------------------------------
                           for var in iterable1:
                                for var in iterable2:
                                    expression
                           ----------------------------------
--------------------------------------------------------------

---------------------------------------------------------------------
syntax2:when we have only if condition
-----> varname={key:value for var in iterable1 for var in iterable2 if condition}
                           {outer for loop    } {inner for loop    }

                           ----------------------------------------
                           for var in iterable1:
                                for var2 in iterable2:
                                    if condition:
                                        expression
                            ---------------------------------------
---------------------------------------------------------------------

----------------------------------------------------------------------------------
syntax3: when we have both if and else condition:
----> varname={key:value(of if condition) if condition else value(of else part) for var in iterable1 for var in iterable2}
                                                                                 {outer for loop   } {inner for loop     }

                                          ---note: key will be as it is

                                          -------------------------------------------
                                          for var iterable1:
                                                for var2 in iterable2:
                                                if condition:
                                                    tsb
                                                else:
                                                    fsb
                                        ---------------------------------------------
-------------------------------------------------------------------------------------
'''

#nested dictionary
#1.l=[1,2,3,4,5]     o/p:{1:'odd',2:'even',3:'odd',4:'even',5:'odd'}
# o/p:{(1, 'a'): 'a', (1, 'b'): 'b', (2, 'a'): 'a', (2, 'b'): 'b'}
l=[1,2,3,4,5]
print({i:'even' if i%2==0 else 'odd' for i in l})

#2. num=[1,2]  char=['a','b']
# o/p:{(1, 'a'): 'a', (1, 'b'): 'b', (2, 'a'): 'a', (2, 'b'): 'b'}
num=[1,2]
char=['a','b']
print({(i,j):j for i in num for j in char})

# 3. store only pairs whose sum is even
# o/p: {(0, 0): 0, (0, 2): 2, (1, 1): 2, (2, 0): 2, (2, 2): 4}
a=[0,1,2]
b=[0,1,2]
print({(i,j):i+j for i in a for j in b if (i+j)%2==0 })

# 4.l=['hi','py']    o/p: {'hi': ['h', 'i'], 'py': ['p', 'y']}
l=['hi','py']
print({i:[i[0],j] for i in l for j in i})
# OR
print({i:[j for j in i] for i in l })

# 5. {(0, 0): 'even', (0, 1): 'odd', (0, 2): 'even', (1, 0): 'odd', (1, 1): 'even',
#  (1, 2): 'odd', (2, 0): 'even', (2, 1): 'odd', (2, 2): 'even'}
a=[0,1,2]
b=[0,1,2]
print({(i,j):'even' if (i+j)%2==0 else 'odd' for i in a for j in b})







