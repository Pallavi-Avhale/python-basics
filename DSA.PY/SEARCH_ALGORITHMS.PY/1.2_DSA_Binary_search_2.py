''' 
BINARY SEARCH --->

IT IS A SEARCHING ALGORITHM , WHERE IT WILL WORK ON SORTED ELEMENTS

HERE WE NEED TO PASS ALWAYS SORTED ELEMENTS/DATA

WHY USE?-->
IT WILL PRINT LEFT TO RIGHT or right to left any diretion 
IF WE WANT TO CODE INSCRESE EFFICIENCY AND REDUCE CODE
 
---------------------------------------------------------------------->
STEPS

1. COSIDER A COLLECTION AND KEY TO CHECK

2. INITIALISE LEAST INDEX AS 0 AND HEIGHEST INDEX AS LEN(COLLECTION)-1 

3. WHILE CONDITION CHECK WHETHER LI<=HI (LEAST INDEX LESS THAN EQUAL TO HIGHEST INDEX---> IF IT'S TRUE GOING TO NEXT) 
   IF THE 

4. CALCULATE MID INDEX USING MID= (LI + HI)//2 FOR MUL 

5. CHECK WHETHER KEY==COLLECTION [MIDDLE] IF TRUE RETURN MID  IF IT IS FALSE JUMP TO NEXT STEP ELIF
-->ELIF CHECK KEY > COLLECTION [MID] IF TRUE CHANGE LI = MID+1 (RIGHT OF THE LEFT)
-->ELSE  CHECK KEY < COLLECTION [MID] IF TRUE CHANGE HI = MID+1

6. REPEAT ALL THE POINTS FROM 3 TO 5 UNTIL YOU GET INDEX OF KEY 
0////67
 
--------------------------------------------------------------------->

TIME COMPLEXITY OF BINARY SEARCH---->

BEST--> 1
AVERAGE--> 0 (LOG N)
WORST--> 0 (LOG N)


---------------------------------------------------------------------->

TRACING PART

X=[10,20,30,40,50,60,70,80]              # COLLECTION
KEY = 60                                 # SEARCHING ELEMNT
    
    0  1  2  3  4  5  6  7
X=[10,20,30,40,50,60,70,80]              # CHECKING LEAST INDEX (LI) 0--> 10 AND LAST INDEX (HIGHEST INDEX) 7--> 80   # STEP--> 2 (LEN(X)-1)=8-1=7

0<=7                            # TRUE GO NEXT     #USE EUAL TO IS MANDATORY TO INCLUDE LAST ELEMENT IF WE NOT MENTION = TO LAST ELEMENT WILL BE EXCLUDED               #--> STEP--3

MID=(LI+HI)//2                  #-------> we need to consider position of the element
MID=(0+7)//2
MID=7/2--> 3.5 --> TO AVOID DECIMAL USE FLOOR DIVISION
MID=7//2--> 3  --> HERE 3 IS THE POSITION OF THE MIDDLE ELEMENT       #--> STEP--> 4       


5. IF KEY == X [MID]
       60 == 40          ----> FLASE    #--> WE NEED TO CHANGE THE MID VALUE

6. elif Key > collection [mid]
        60  > 40         ----> TRUE

        
   0  1  2  3  4  5  6 7     
  10 20 30 40 50 60 70 80     0 INDEX---> 10  AND HIGHEST INDEX ---> 80 (7)  AND MID INDEX ---> 40 (3)

  LI = MID + 1
     =  3  + 1 
     =  4
     = INDEX 4TH ELEMENT = 50

 LI < = HI
 4 < = 7  ---------------> TRUE  ----> SO FIND MID VALUE 

 MID=( LI + HI)//2
    = ( 4 + 7 ) // 2
    = 5

MID = 5TH INDEX ---> 60 

'''


x=[10,20,30,40,50,60,70,80]

key=60

def linear_search(x, key):                     # collection + search element
    li=0                                       # least index
    hi=len(x)-1                                # Highest index

    while li <= hi:
        mid=(li + hi)//2                       #-------> we need to consider position of the element
        if x [mid] == key:                     # 40 == 60 ---> condition false --> moving to next step/ loop
            return mid
        elif key > x[mid]:                     # elif for checking multiple condition
            li = mid + 1

        else:
            hi = mid - 1
print(linear_search(x,key))                    #---> 5 

print()
# ---------------------------------------------------------

# IF SPECIFIED ELEMENT IS NOT PRESENT IT WILL SHOW NONE / ELSE WE WILL PASS COMMENT ANYTHING BELOW THE WHILE LOOP ( RETURN)

x=[10,20,30,40,50,60,70,80]

key=60

def linear_search(x, key):                     # collection + search element
    li=0                                       # least index
    hi=len(x)-1                                # Highest index

    while li <= hi:
        mid=(li + hi)//2                       #-------> we need to consider position of the element
        if x [mid] == key:                     # 40 == 60 ---> condition false --> moving to next step/ loop
            return mid
        elif key > x[mid]:                     # elif for checking multiple condition
            li = mid + 1

        else:
            hi = mid - 1
print(linear_search(x,700))                    #---> None

print()

# ---------------------------------------------------------

x=[10,20,30,40,50,60,70,80]

key=60

def linear_search(x, key):                     # collection + search element
    li=0                                       # least index
    hi=len(x)-1                                # Highest index

    while li <= hi:
        mid=(li + hi)//2
        if x [mid] == key:                     # 40 == 60 ---> condition false --> moving to next step/ loop
            return mid
        elif key > x[mid]:                     # elif for checking multiple condition
            li = mid + 1

        else:
            hi = mid - 1
    return -1
print(linear_search(x,700))                    #---> -1


print()
# ---------------------------------------------------------

# x=[1,2,3,4,5,6,7,]
# key=3

#    0 1 2 3 4 5 6
# x=[1,2,3,4,5,6,7]

# li=1 element
# hi=7 element

# li = 0
# hi = len(x)-1 = 7-1 = 6

# 0 <= 6 -----> true

# mid=(li + hi)//2                     #-------> we need to consider position of the element

#     =(0 + 6) // 2
    #   =6//2
    #  3       -----> middle index

# index 3---> 4=
# mid== key
# 4 == 3           -----> false

#  next elif

# elif key > x [ mid ]

    #   3 > 4         --> false
    # li = mid + 1    --> 4+1

# ------------------------------------------------------------------------------------

x=[1,2,3,4,5,6,7,]
key=3

def l_s(x, key):
    li=0
    hi=len(x)-1

    while li <= hi:
        mid=(li + hi)//2
        if x [mid] == key:                     # 40 == 60 ---> condition false --> moving to next step/ loop
            return mid
        elif key > x[mid]:                     # elif for checking multiple condition
            li = mid + 1

        else:
            hi = mid - 1

print(l_s(x,key))                              #----> 2 ------> key element position is 2

print()
# --------------------------------------------------------------------------------

# 1ST OCCURANCE
# 2ND OCCURANCE
# LAST OCCURANCE
# NTH OCCURANCE

# -----------------------------------------------------------------------------
#   0   1   2   3   4
d=[100,150,200,300,350]     #collection

key = 200                  # find out 200 

def Binary_searching(d,key):
    li=0
    hi=len(d)-1

    while li<=hi:
        mid=(li+hi)//2
        if key == d[mid]:
            return mid
        
        elif key>d[mid]:
            li=mid+1

        else:
            hi=mid-1
    return -1

print(Binary_searching(d,key))

print()

# -----------------------------------------------------------------------------------------
# HOW TO FIND OUT FIRST OCCURANCE?  ------------> from mid index position we need to move mid to left backword


# x=[10,20,20,20,30,40,50]

# key= 20

# Index

# 0    1   2   3   4   5   6
# 10  20  20  20  30  40  50


# least index= 0
# Highest index= len(x)-1= 7-1= 6


# while least_index <= highest_index:
#       mid=(li+hi)//2
#       if key==x[mid]:
#             first=mid
#             first=3           ---. to findout first occurance we need to go backword
#             highest_index = mid-1
#             highest_index = 3-1         ---->  3 is mid and -1 
#             highest_index = 2
#       li<=hi         -----> check 
#       0<=2           -----> True
#       mid=(li+hi)//2
# 
# 


# ------------------------------------------------------------------
#  IF THE SPECIFIED ELEMENT IS NOT PRESENT IN GIVEN ITERABLE IT WILL GIVE NONE TO AVOID WE CAN RETURN  ANY COMMENT OR RETURN -1
#  OR POS=-1 (NEW_VAR=-1) BUT IF THE GIVEN ELEMENT IS PRESENT TO UPDATE THAT ELEMENT POSITION USE POS=-1(NEW_VAR=-1)
#  FOR THE LAST OCCURANCE WE NEED TO USE LI= MID+1 ( TO MOVE FORWARD DIRECTION FROM THE MID INDEX POSITION)

#   0  1  2  3  4  5  6
x=[10,20,20,20,30,40,50]

key= 20

def Searching_data(x,key):
    li=0
    hi=len(x)-1
    first=-1

    while li<=hi:
        mid=(li+hi)//2
        if key == x[mid]:
            first=mid
            hi=mid-1

        elif key > x[mid]:
            li=mid+1

        else:
            hi=mid-1
    return first

print(Searching_data(x,key))            #-----> 1

print()
# ------------------------------------------------------------------

# How to Find last occurance----------->

#   0  1  2  3  4  5  6
x=[10,20,20,20,30,40,50]

key= 20

def Searching_data(x,key):
    li=0
    hi=len(x)-1
    last=-1

    while li<=hi:
        mid=(li+hi)//2
        if key == x[mid]:
            last=mid
            hi=mid-1
            li=mid+1

        elif key > x[mid]:
            li=mid+1

        else:
            hi=mid-1
    return last

print(Searching_data(x,key))            #-----> 3

print() 
# -----------------------------------------------------------------------------

# LAST OCCURANCE

#   0  1  2  3  4  5  6
x=[10,20,20,20,30,40,50]

key= 20

def Searching_data(x,key):
    li=0
    hi=len(x)-1
    first=-1

    while li<=hi:
        mid=(li+hi)//2
        if key == x[mid]:
            first=mid
            hi=mid-1

        elif key > x[mid]:
            li=mid+1

        else:
            hi=mid-1
    return first

data=Searching_data(x,key)
print("First occurance--->", data)               #------------>First occurance---> 1


if data!=-1 and data + 1 < len(x) and x[data+1] == key:
    print("Second_Occurance----->", data+1)      #------------>Second_Occurance---> 2

else:
    print("Value Is Not Present")


print()

# ------------------------------------------------------------------------


# First Occurance

r=(2,5,8,10,99,105,105,105,200)

key=105

# index

#    0  1  2   3  4    5    6    7    8
# r=(2, 5, 8, 10, 99, 105, 105, 105, 200)


def First_Occurance(r,key):
    li=0
    hi=len(r)-1
    first=-1

    while li<=hi:                      #0<=8 -------------> True
        mid = (li+hi)//2               #(0+8)//2 ------------> 4  ------> mid= 99(4)
        if key == r[mid]:
            first=mid
            hi=mid-1
        
        elif key > r[mid]:
            li=mid+1

        else:
            hi=mid-1

    return first

print(First_Occurance(r,key))         #--------> 105---> 5

print()

# ----------------------------------------------------------------------------------


# LAST OCCURANCE



r=(2,5,8,10,99,105,105,105,200)

key=105

# index

#    0  1  2   3  4    5    6    7    8
# r=(2, 5, 8, 10, 99, 105, 105, 105, 200)


def Last_Occurance(r,key):
    li=0
    hi=len(r)-1
    last=-1

    while li<=hi:                      #0<=8 -------------> True
        mid = (li+hi)//2               #(0+8)//2 ------------> 4  ------> mid= 99(4)
        if key == r[mid]:
            last=mid
            hi=mid-1
            li=mid+1
        
        elif key > r[mid]:
            li=mid+1

        else:
            hi=mid-1

    return last

print(Last_Occurance(r,key))         #--------> 105---> 7

# ----------------------------------------------------------------------------

#SECOND OCCURANCE
print()

p=(First_Occurance(r,key))
print("First_Occurance----->", p)                #---> First_Occurance-----> 5

if p!=-1 and p + 1 < len(r) and key == r[p+1]:
    print("Second_Occurance--->", p+1)           #--->Second_Occurance---> 6

else:
    print("Value Is Not Present")


