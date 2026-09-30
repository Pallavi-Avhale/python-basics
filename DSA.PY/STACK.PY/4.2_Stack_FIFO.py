'''
QUEUE

---------------------------------------------------------------------------------------------------------------

FIFO
FIRST IN FIRST OUT

----------------------------------------------------------------------------------------------------------------

NORMAL LIST
COLLECTION (DEQUE)
SINGLY LINKED LIST
DOUBLY LINKED LIST
CIRCULAR LINKED LIST

-----------------------------------------------------------------------------------------------

FIFO
1. FRONT
2. REAR
------------------------------------------------------------------------------------------------

ENQUEUE ---------> ADDING THE ELEMENT 
DEQUE   ---------> DELETE THE ELEMENT
PEEK    ---------> TOP
Size    ---------> ELEMENT PRESENT IN COLLECTION 
--------------------------------------------------------------------------------------------------

50       ---------------> REAR/ LAST
40
30
20
10       ---------------> TOP/ FRONT

-----------------------------------------------------------------------------------------------------

'''

# queue=[]
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.append(5)
# print("All Elements-----> ", queue)          #---> All Elements----->  [1, 2, 3, 4, 5]
# print("First Element----> ", queue.pop(0))   #---> First Element---->  1
# print("Front Element----> ", queue[0])       #---> Front Element---->  2
# print("Rare Element-----> ", queue[-1])      #---> Rare Element----->  5

# print()

# #SECOND WAY USE---------> COLLECTION MODULE

# from collections import deque
# x=deque()                    #-----> create object  -------> deque is a inbuild class ---> x=New_var

# x.append(1)
# x.append(2)
# x.append(3)
# x.append(4)
# x.append(5)

# print("All Elements-----> ", x)          #--------> All Elements----->  deque([1, 2, 3, 4, 5])
# print("Front Element deleted---->", x.popleft())
# print("Front Element----> ",x[0])        #--------> Front Element---->  1
# print("Rare Element-----> ",x[-1])       #-------->Rare Element----->  5  

# print()

# # SINGLY_LINKED_LIST
# '''

# FRONT/TOP ---> 10 ----> RARE USE TO ADD THE OTHER ELEMENTS (ENQUEUE/DEUQUE)
# ----------------------------------------------------------------------------------------------------------
# New_Begining.next=self.front---------> is will be working but not recommended

# '''

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.Next=None

# class Queue:
#     def __init__(self):
#         self.Front=None                  # --> No Front element is present
#         self.Rare=None                   # --> No Rare element is present 

#     def Enqueue(self,data):
#         NB=Node(data)
#         if self.Front is None:           #----> while adding First Element there is no element is present
#             self.Front=NB                #----> Front ---> 10 ------> Rare ---> if we add any another element after front or 10 element it will place in rare part 
#             self.Rare=NB

#         else:                            #-----> when the TOP Rare element is already present this block will execute --> It will continue to add the next 
#             self.Rare.Next=NB            #-----> 10=self.Front = self.Rare  , self.Rare=10, self.Rare.Next=20
#             self.Rare=NB                 #-----> 20---> New node/ element 

#     def Dequeue(self):
#         if self.Front is None:
#             print("Front is Empty")
#             return

#         data=self.Front.Next              #----> self.Front---> 10, self.FRont.Next=20 ----> Data should be Start from 20 
#         self.Front=self.Front.Next        #----> 10 no. or head is pointing to the next 20 element---> after deleting 10 self.front = 20 
#         if self.Front is None:            # ----> self.front is not empty so it will show the remaining part from 20 element ---> if we not use this tow lines also it will be working 
#             self.Rare=None
#         return data

#     def PEEK(self):
#         if self.Front is None:
#             print(" Queue is empty")

#         else:
#             temp=self.Front
#             print("TOP ELEMENT---->", temp.data)

#     def SIZE(self):
#         temp=self.Front
#         Count=0
#         while temp:
#             Count=Count+1
#             temp=temp.Next
#         print("Total Element", Count)

#     def display(self):
#         if self.Front is None:
#             print("Queue is Empty")
#             return

#         else:
#             temp=self.Front
#             while temp:
#                 print(temp.data,"---->", end=" ")
#                 temp=temp.Next
#             print("None")

# q=Queue()

# q.Enqueue(10)       #----> 10 ----> None
# q.Enqueue(20)       #----> 10 ----> 20 ----> None
# q.Enqueue(30)       #----> 10 ----> 20 ----> 30 ---->  None
# q.Enqueue(40)       #----> 10 ----> 20 ----> 30 ----> 40 ----> None
# q.Enqueue(50)       #----> 10 ----> 20 ----> 30 ----> 40 ----> 50 ----> None

# q.PEEK()            #----> BEFORE DELETING TOP ELEMENT----> 10

# q.SIZE()            #----> Before deleting Total Element 5
# q.Dequeue()         #----> 20 ----> 30 ----> 40 ----> 50 ----> None

# q.PEEK()            #----> AFTER DELETING TOP ELEMENT----> 20

# q.SIZE()            #----> After Deleting Total Element 4


# q.display()


# print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.Next=None

# class Q:
#     def __init__(self):
#         self.Front=None
#         self.Rare=None

# -----------------------------------------------------------------------------------------------------------------------

print()

class Node:
    def __init__(self,data):
        self.Prev=None
        self.data=data
        self.Next=None

class Queue:
    def __init__(self):
        self.Front=None
        self.Rare=None

    def Enqueue(self,data):
        NB=Node(data)
        if self.Front is None:           # while adding First Element there is no element is 
            self.Front=NB                #----> Front ---> 10 ------> Rare ---> if we add any another element after front or 10 element it will place in rare part 
            self.Rare=NB

        else:
            self.Rare.Next=NB            #-----> 10=self.Front =self.Rare  , self.Rare=10, self.Rare.Next=20
            self.Prev=self.Rare          #-----> To connecting with the backword
            self.Rare=NB                 #-----> 20---> New node/ element 

    def Dequeue(self):
        if self.Front is None:            # if the element this line won't work 
            print("Front is Empty")
            return

        data=self.Front.Next              #----> self.Front---> 10, self.FRont.Next=20 ----> Data should be Start from 20 
        self.Front=self.Front.Next        #----> 10 no. or head is pointing to the next 20 element---> after deleting 10 self.front = 20 
        self.Front.Prev=None
        if self.Front is None:            # ----> self.front is not empty so it will show the remaining part from 20 element ---> if we not use this tow lines also it will be working 
            self.Rare=None
        return data

    def PEEK(self):
        if self.Front is None:
            print(" Queue is empty")

        else:
            temp=self.Front
            print("TOP ELEMENT---->", temp.data)

    def SIZE(self):
        temp=self.Front
        Count=0
        while temp:
            Count=Count+1
            temp=temp.Next
        print("Total Element", Count)

    def display(self):
        if self.Front is None:
            print("Queue is Empty")
            return

        else:
            temp=self.Front
            while temp:
                print(temp.data,"---->", end=" ")
                temp=temp.Next
            print("None")

q=Queue()

q.Enqueue(10)       #----> 10 ----> None
q.Enqueue(20)       #----> 10 ----> 20 ----> None
q.Enqueue(30)       #----> 10 ----> 20 ----> 30 ---->  None
q.Enqueue(40)       #----> 10 ----> 20 ----> 30 ----> 40 ----> None
q.Enqueue(50)       #----> 10 ----> 20 ----> 30 ----> 40 ----> 50 ----> None

q.PEEK()            #----> BEFORE DELETING TOP ELEMENT----> 10

q.SIZE()            #----> Before deleting Total Element 5
q.Dequeue()         #----> 20 ----> 30 ----> 40 ----> 50 ----> None

q.PEEK()            #----> AFTER DELETING TOP ELEMENT----> 20

q.SIZE()            #----> After Deleting Total Element 4


q.display()


print()

