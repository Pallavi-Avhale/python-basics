''' 
Searching Algorithams--->
IN THE GIVEN ITERABLE IF WE WANT TO FINDOUT THE ELEMENT

DRAWBACK --> WHAT ELEMENT WE ARE SEARCHING NO MATTER WHETHER THE ELEMENT IS PRESENT OR NOT 
             WE NEED TO SEARCH THE ELEMENT FROM ZROTH (0TH) POSITION 
             TO AVOID THIS WE NEED TO USE BINARY SEARCHING ALGORITHMS.

Q. WHAT IS THE TIME C OF SEARCHING ALGORITHMS?????
TIME COMPLEXITY
1) BEST TC--> FINDING THE ELEMENT IN THE 1ST IETERATION ( POSITIVE/ ALWAYS GET OUTPUT)-----> O(1)--> 1ST IETERATION
2) AVERAGE TC--> IT WILL PRESENT IN BETWEEN BEST AND WORST ( ALWAYS IT WILL GET THE OUTPUT)----> O(N) ---> N IS NUMBER OF IETERATION
3) WORST TC--> IN 2ND AND 3RD IERATION IF WE GET THE OUT PUT / RESULT ( POSITIVE/NEGATIVE), 
               IF THE ELEMENT IS PRESENT WE WILL GET THE OUTPUT(POSITIVE)/ 
               IF THE ELEMENT IS NOT PRESENT NOT GET ANY OUTPUT (NEGATIVE) 
               O(N) ---> N IS NUMBER OF IETERATION

1) linear Serach Algoritham-->

--> It is a part of searching algorithms.
--> It will work on the bases of sequence manner

STEPS->
1 STEP--> WE HAVE THE COLLECT ONE COLLECTION 

2 STEP--> IN THE GIVEN COLLECTION WHAT ELEMENT WE HAVE TO FIND OUT ( TARGETED ELEMENT)

3 STEP--> WE HAVE TO SEARCH FROM THE ZEROTH POSITION TO LAST POSITION 

4 STEP--> ONCE WE FIND THE ELEMENT HAVE TO RETURN THE POSITION 

'''

# EXAMPLE
# key/ target= 40

#  0    1   2   3   4  5
# x=[10, 20, 30, 40, 50, 60]      #STEP 1--> COLLECTION

# if key==x[0] ----> FLASE
# if key==x[1] ----> FLASE
# if key==x[2] ----> FLASE
# if key==x[3] ----> True

# for loop 

x=[10, 20, 30, 40, 50, 60] 
key=50

for i in range(len(x)):

    # print(i)            #print position -- 0 1 2 3 4 5
    if x[i]==key:         #x[i]------> var_name[position]
        print(i)          # position---> 4

print()
# -------------------------------------------------------------------------------------------------------

def searching_element(x,key):
    for i in range (len(x)):
        if x[i]==key:
            return i
a=searching_element([10, 20, 30, 40, 50, 60],20)

print(a)                  #position----> 20--> 1

print()
# -------------------------------------------------------------------------------------------------------

def searching_element(x,key):
    for i in range (len(x)):
        if x[i]==key:
            return i
a=searching_element([10, 20, 30, 40, 50, 60],200)

print(a)                  #position----> 200--> None

print()
# -------------------------------------------------------------------------------------------------------

def searching_element(x,key):
    for i in range (len(x)):
        if x[i]==key:
            return i
    return "key is not present"
a=searching_element([10, 20, 30, 40, 50, 60],200)

print(a)                  # If the element is not present we can return the message ---> key is not present


print()
# -------------------------------------------------------------------------------------------------------

#     1  2  3  4  5  6---->i
# e= "P  Y  T  H  O  N"---> j

# indexing -----> var_name[Position]
                    # e[0]=P
                    # e[1]=Y

# if e[i]==key

# HERE  WE HAVE TO SEARCH ELEMENT FROM 0TH POSITION TO LAST
# if P==n-----> False
# if Y==n-----> False
# if T==n-----> False
# if H==n-----> False
# if O==n-----> False
# if N==n-----> TRUE
    

e="PYTHON"

key="N"

for i,j in enumerate(e):
    # print(i,j, end=" ")       # ---> 0 P 1 Y 2 T 3 H 4 O 5 N 
    if e[i]==key:               # var_name[Position] e[i]-->P
        print(i)                # N--------> 5

print()
# -------------------------------------------------------------------------------------------------------

x=(100, "Hello", "Python", "Java", "SQL", "Walmart")
key="SQL"

for i in range(len(x)):
    if x[i]==key:
        print(i)               #----> "SQL"--> 4

print()

for i, j in enumerate(x):
    if x[i]==key:
        print(i)

print()
# -------------------------------------------------------------------------------------------------------

Y={"Name":"Ravi","age":24, "salary":60000}
key="age"

for i, j in enumerate(Y):
    if j==key:
        print(i)        #---> 1

print()


# -------------------------------------------------------------------------------------------------------

z={"EID": "E123", "DEPT": "HR", "YOP": 5, "CName":"TY"}
key="TY"

for i in z:
    if z[i]==key:
        print(z[i])              #----> TY 

print()        
# -------------------------------------------------------------------------------------------------------

# HOW TO FIND OUT MULTIPLE ELEMENTS



#   0   1    2     3     4    5    6     7
x=(10, 20, "abc", 5.5, 7+8j, 100, 200, "xyz")
keys=["abc",100,"xyz"]

# Take empty list

l=[]
for i in keys:            #all targeted elements store in i   ---->abc 100 xyz--> outer loop
   for j in range(len(x)):     # j is pointing to the position of the elements---> inner loop
       if x[j]==i:             # i is pointing to the all targeted elements
           l.append(j)
print(l)                  #position --->abc 100 xyz --->[2, 5, 7]


# ------------------------------------------------------------------------------

# HOW TO PRINT BOTH MULTI ELEMENTS WITH THERE POSITION USE DICTIONARY

#   0   1    2     3     4    5    6     7
x=(10, 20, "abc", 5.5, 7+8j, 100, 200, "xyz")
keys=["abc",100,"xyz"]

l={}
for i in keys:            #all targeted elements store in i   ---->abc 100 xyz--> outer loop
   for j in range(len(x)):     # j is pointing to the position of the elements---> inner loop
       if x[j]==i:             # i is pointing to the all targeted elements
           
           l[j]=i                  #---->{2: 'abc', 5: 100, 7: 'xyz'}   
        #    l[i]=j                # key value syntax----> var_name[key]=value
        
        # l.update({j:i})          #------>{2: 'abc', 5: 100, 7: 'xyz'}
        # l.update({i:j})          #------->{'abc': 2, 100: 5, 'xyz': 7}
print(l)                           #------>{'abc': 2, 100: 5, 'xyz': 7}

print()
# ------------------------------------------------------------------------------

# How to count the occurance of the particular elements
 
d=[1,2,3,4,2,2,7]

key=2

count=0

for i in range(len(d)):     # here i is pointinf to the element position
    if d[i]==key:
        count+=1
print(count)                #--------->3


print()

count=0
for i in d:                 # Here i is pointing to directly element
    if i==key:
        count+=1
print(count)               #---------->3

print()

# ------------------------------------------------------------------------------

e=[1000, 457, 900, 45.56, "Hello","abc"]
key=[45.56, 900]

d={}

for i in key:
    for j in range(len(e)):
        if e[j]==i:
            d[j]=i
print(d)                      #---------->{3: 45.56, 2: 900}


print()

# ------------------------------------------------------------------------------

# Searching Algorithm


# 1.Linear Search algorithm


# It is a searching algorithm ,which works on a principle called
# Sequential searching where control will traverse through each and every value present in a collection one after the other sequentially to check whether key is present or not

# STEPS

# 1.Consider a collection and key to check
# 2.Start Comparing the value from oth index till len of collection
# 3.after getting the value same as key return its index
# 4 if key is not present then ignore

# ------------------------------------------------------------------------------

k=[34,67,1,89,100,200,12]
key=100

for i in range(len(k)):
    if k[i] == key:
        print(i)                #--------->4


print()

k=[34,67,1,89,100,200,12]
key=100

for i, j in enumerate(k):
    if k[i]==key:
        print(i)               #------------> 4

print()    
# ------------------------------------------------------------------------------
print()


t=(1,7,90,3.4,7+8j,"Hii",120)
keys=[7+8j,"Hii",90]

l=[]

for i in keys:
    for j in range(len(t)):
        if t[j]==i:
            l.append(i)
print(l)                       #-----------> [(7+8j), 'Hii', 90]

print()

# ------------------------------------------------------------------------------

# Assignment Questions


# 1.Teacher checks attendance register sequentially to find a roll number.
#                0    1    2    3    4
roll_numbers = [101, 102, 103, 104, 105]
key = 104

for i in range(len(roll_numbers)):
    if roll_numbers[i]==key:
        print("key--->",i)                #----------> key---> 3

print()

# ------------------------------------------------------------------------------

# 2.Searching a contact name in phone contacts one by one.
contacts = ["Ravi", "Amit", "Sita", "John"]
search_name = "Sita"

for i in range(len(contacts)):
    if contacts[i] == search_name:
        print("search_name-->", i)         #--------> search_name--> 2

print()

# --------------------------------------------------------------------------


# 3.A user searches for a category (Electronics, Fashion, Grocery). Check if the category exists.
categories = ["Electronics", "Fashion", "Grocery"]
search_category = "Fashion"

for i in range(len(categories)):
    if categories[i]== search_category:
        print("search_category--->", i)             #------->search_category---> 1

print()
# ------------------------------------------------------------------------------

# 4.An app stores discount coupon codes. Verify whether a coupon code is valid.
coupon_codes = ["SAVE10", "WELCOME50", "FESTIVE20"]
user_coupon = "WELCOME50"

for i in range(len(coupon_codes)):
    if coupon_codes[i]==user_coupon:
        print("user_coupon--->", i)                  #user_coupon---> 1


print()

# ------------------------------------------------------------------------------

# 5.Search if a customer email ID exists in the registered users list.
registered_users = [
    "mailto:user1@gmail.com",
    "mailto:user2@yahoo.com",
    "mailto:admin@shop.com"]
search_email = "mailto:admin@shop.com"

for i in range(len(registered_users)):
    if registered_users[i]==search_email:
        print("search_email---> ", i)              #---> search_email--->  2


print()

# ------------------------------------------------------------------------------

# 6.A product review system stores ratings. Search whether a specific rating value exists.
ratings = [5, 4, 3, 5, 2]
search_rating = 3

for i in range(len(ratings)):
    if ratings[i]==search_rating:
        print("search_rating ---->", i)        #---------> search_rating ----> 2


print()

# ------------------------------------------------------------------------------

# 7.Search whether a payment method (UPI, Card, COD) is supported.
payment_methods = ["UPI", "Card", "COD"]
method = "UPI"

for i in range(len(payment_methods)):
    if payment_methods[i] == method:
        print("method ---->", i)                #---------> method ----> 0

print()

# ------------------------------------------------------------------------------

''' 
x=[10,20,30,10]
key=10
count=0

last=-1

for i in range(len(x)):
    if x[i]==key:
        count+=1
        last=i
print("Total Key Count--> ", count)
print("Position -->", last)

# o/p-->
# Total Key Count-->  2
# Position --> 3

print()

x=[10,20,30,10]
key=10

for i in range(len(x)):
    if x[i]==key:
        print(i)
        break            #--> position ---> 0

print()

x=[10,20,30,10]
key=10

last=-1

for i in range(len(x)):
    if x[i]==key:
        
        last=i

print("Position -->", last)             #-----------> Position --> 3

print()

x=[10,20,30,10]
key=10
count=0



for i in range(len(x)):
    if x[i]==key:
        count+=1
        
print("Total Key Count--> ", count)          #----------> Total Key Count-->  2
'''

