''' 
STACK
-----------------------------------------------------------------------------------
LIFO ---> LAST IN FIRST OUT -----> WHAT ELEMENT WE INSERTED AT LAST IT WILL DELETE AT FIRST

WORK ONLY IN FORWARD DIRECTION 
-----------------------------------------------------------------------------------

        ┌───────┐
        │  50   │  ← TOP
        ├───────┤
        │  40   │
        ├───────┤
        │  30   │
        ├───────┤
        │  20   │
        ├───────┤
        │  10   │  ← FIRST inserted
        └───────┘

------------------------------------------------------------------------------------

1. PUSH ---> INSERT
2. POP ----> DELETE  -----> ALWAYS DELETE TOP/LAST ELEMENT
3. TOP/PEEK ---> CHECK TOP ELEMENT
4. SIZE -------> TO CHECK HOW MANY ELEMENTS ARE PRESENT / TO CHECK THE DATA

PUSH → 10 → 20 → 30 → 40 → 50

POP  → 50 → 40 → 30 → 20 → 10

-------------------------------------------------------------------------------------

---> STACK IMPLEMENT IN PYTHON LIST AND LINKED LIST( SINGLY LINKED LIST (RECOMMENDED COZ IT TAKE LESS MEMORY / MANAGE MEMORY), DOUBLY LINKED LIST( NOT RECOMMENDED COZ IT TAKE MORE MEMORY), & CIRCULAR LINKED LIST( NOT RECOMMENDED COZ IT TAKE MORE MEMORY)
---> SINGLE POINTOER --->???????
---> [ 20 (LAST COME FIRST) |  ] ---> O/P--> [ 10 (FIRST ELEMENT) | ]
---> MANAGE MEMORY IN SINGLY LINKED LIST

--------------------------------------------------------------------------------------

stack=[] ----> insted of stack we can take any name it will be working

---------------------------------------------------------------------------------------

[10, 20, 30, 40]

┌──────────┬──────────┐
│   DATA   │   NEXT   │
└──────────┴──────────┘

For example:
┌──────┬──────┐
│  50  │  ●───┼──→
└──────┴──────┘

self.Top = None

Top
 ↓
None

Insert 10:

Top
 ↓
┌──────┬──────┐
│  10  │ None │
└──────┴──────┘

Insert 20:

Top
 ↓
┌──────┬──────┐
│  20  │  ●───┼──→ 10
└──────┴──────┘

Insert 30:

Top
 ↓
┌──────┬──────┐
│  30  │  ●───┼──→ 20
└──────┴──────┘
              ↓
             10



'''
# NORMAL IMPLEMENTATION IN PYTHON LIST

stack=[]

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)                                                #-------> [10, 20, 30, 40]

print("Before Performing Operations----->", len(stack))    #----->  Before Performing Operations-----> 4
print("Top element--->", stack.pop())                       #-----> Top element---> 40 
print("TOP ELEMENT-> ", stack[-1])                          #-----> TOP ELEMENT->  30  ------> [-1] ---> to check last element
print("All Element Information---> ", stack)                #---> All Element Information--->  [10, 20, 30]
print("After Performing Operations----->", len(stack))     #----->  After Performing Operations-----> 3

print()
# --------------------------------------------------------------------------------------------------------------------------------------------

# IMPLEMENTATION IN SINGLY LINKED LIST 

class Node:
    def __init__(self, data):
        self.data=data
        self.Next=None

class Stack:
    def __init__(self):
        self.Top=None 

    def Push(self,data):                # ---> Inserting Element
        NB=Node(data)
        NB.Next=self.Top                 #---> [ NB (TOP/HEAD) | Next ]
        self.Top=NB


    def Display(self):
        if self.Top is None:
            print("STACK IS EMPTY")

        else:
            temp=self.Top
            while temp:
                print(temp.data, )
                temp=temp.Next

s=Stack()
s.Push(10)                 #---> [ 10 (TOP/HEAD) | Next ]
s.Push(20)                 #---> [ 20 | 10 (TOP/HEAD) | Next ]   
s.Push(30)                 #---> [ 30 | 20 | 10 (TOP/HEAD) | Next ]   
s.Push(40)                 #---> [ 40 | 30 | 20 | 10 (TOP/HEAD) | Next ] 
s.Push(50)                 #---> [ 50 | 40 |30 | 20 | 10 (TOP/HEAD) | Next ]         
s.Display()

print()
# ---------------------------------------------------------------------------------------------------------

'''
# ==========================================================
# NODE CLASS
# ==========================================================

class Node:
    # Constructor of Node
    # It automatically runs whenever we create a new Node
    def __init__(self, data):

        # Store the actual value inside the node
        self.data = data

        # Store the address/reference of the next node
        # Initially there is no next node
        self.Next = None


# ==========================================================
# STACK CLASS
# ==========================================================

class Stack:
    # Constructor of Stack
    # It automatically runs when we create Stack()
    def __init__(self):

        # Top stores the reference of the TOP node
        # Initially the stack has no node
        self.Top = None


    # ======================================================
    # PUSH → INSERT
    # ======================================================

    def Push(self, data):

        # Create a new node with the given data
        # Example: Push(100) → NB = Node(100)
        NB = Node(data)

        # Connect the new node to the current TOP
        # The new node points to the old TOP
        NB.Next = self.Top

        # Make the new node the new TOP
        self.Top = NB


    # ======================================================
    # PEEK → CHECK TOP
    # ======================================================

    def PEEK(self):

        # Check whether the stack is empty
        if self.Top is None:

            # If Top is None, there is no node
            print("Stack is empty")

        else:

            # self.Top.data gives the data of the TOP node
            # PEEK only checks the TOP; it does NOT delete it
            print("TOP ELEMENT --->", self.Top.data)


    # ======================================================
    # POP → DELETE TOP
    # ======================================================

    def Pop(self):

        # Check whether the stack is empty
        if self.Top is None:

            # Nothing can be deleted
            print("Stack is empty")

            # Stop the function
            return

        # Store the current TOP node in temp
        # We keep it so that we can access the deleted value
        temp = self.Top

        # Move TOP to the next node
        # This removes the old TOP from the stack
        self.Top = self.Top.Next

        # Print the data of the removed node
        print("Removed TOP ELEMENT --->", temp.data)


    # ======================================================
    # SIZE → COUNT ELEMENTS
    # ======================================================

    def Size(self):

        # Start travelling from the TOP node
        temp = self.Top

        # Start counting from zero
        count = 0

        # Continue until temp becomes None
        while temp:

            # Increase count by 1
            count = count + 1

            # Move temp to the next node
            temp = temp.Next

        # Print the final number of nodes
        print("TOTAL ELEMENTS --->", count)


    # ======================================================
    # DISPLAY → SHOW ALL ELEMENTS
    # ======================================================

    def Display(self):

        # Check whether the stack is empty
        if self.Top is None:

            # If there is no TOP, stack is empty
            print("STACK IS EMPTY")

        else:

            # Start travelling from TOP
            # We use temp so that self.Top is not changed
            temp = self.Top

            # Continue until temp becomes None
            while temp:

                # Print current node's data
                # end=" " keeps values on the same line
                print(temp.data, end=" ")

                # Move temp to the next node
                temp = temp.Next

            # Move to a new line after displaying all elements
            print()


# ==========================================================
# CREATE STACK
# ==========================================================

s = Stack()


# ==========================================================
# PUSH → INSERT ELEMENTS
# ==========================================================

s.Push(100)
s.Push(200)
s.Push(300)
s.Push(400)
s.Push(500)


# ==========================================================
# SIZE
# ==========================================================

s.Size()


# ==========================================================
# PEEK
# ==========================================================

s.PEEK()


# ==========================================================
# POP
# ==========================================================

s.Pop()


# ==========================================================
# PEEK AGAIN
# ==========================================================

s.PEEK()


# ==========================================================
# SIZE AGAIN
# ==========================================================

s.Size()


# ==========================================================
# DISPLAY
# ==========================================================

s.Display()


class Node:

┌───────────┬───────────┐
│   DATA    │   NEXT    │
└───────────┴───────────┘

Insert 100:

┌─────┬──────┐
│ 100 │ None │
└─────┴──────┘
'''
#PUSH, POP, PEEK, SIZE-----> 

# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.Next=None

# class Stack:
#     def __init__(self):
#         self.Top=None 

#     def Push(self,data):                 #--> Insert element
#         NB=Node(data)
#         NB.Next=self.Top                 #---> [ NB (TOP/HEAD) | Next ]
#         self.Top=NB

#     def PEEK(self):                            #-------> Check Top element
#         if self.Top is None:
#             print(" It's empty part")

#         else:
#             temp=self.Top
#             print("TOP ELEMENT--->", temp.data)

#     def Pop(self):                               #---------> DELETE THE TOP ELEMENT
#         if self.Top is None:
#             print(" empty stack")
#             return

#         else:
#             temp=self.Top
#             self.Top=self.Top.Next                       #self.Top=100, self.Top.Next=200
#             print("Remove Top Element---> ", temp.data)

#     def Size(self):                               # ---------> Total count of element v bjḥñūhjj
#         temp=self.Top
#         count=0
#         while temp:
#             count=count+1
#             temp=temp.Next
#         print("Total element count is ---->", count)         #--> If we print count inside the loop it will show  1 - 1 element count


#     def Display(self):
#         if self.Top is None:
#             print("STACK IS EMPTY")

#         else:
#             temp=self.Top
#             while temp:
#                 print(temp.data )
#                 temp=temp.Next

# s=Stack()
# s.Push(100)                 #---> [ 100 (TOP/HEAD) | Next ]
# s.Push(200)                 #---> [ 200 | 100 (TOP/HEAD) | Next ]   
# s.Push(300)                 #---> [ 300 | 200 | 100 (TOP/HEAD) | Next ]   
# s.Push(400)                 #---> [ 400 | 300 | 200 | 100 (TOP/HEAD) | Next ] 
# s.Push(500)                 #---> [ 500 | 400 |300 | 200 | 100 (TOP/HEAD) | Next ] 
# s.Size()                    #--->  Befor Performing Operation ----> Total element count is ----> 5 
# s.PEEK()                    #--->  Top Element--->  500   
# s.Pop()                     #--->  Remove Top Element--->  500
# s.PEEK()                    #--->  TOP ELEMENT---> 400
# s.Size()                    #--->  After Performing Operation ----> Total element count is ----> 4
# s.Display()


# print()

# ------------------------------------------------------------------------------------------------------


# Doubly_Linked_List ---> [prev | Data | Next]

class Browser:
    def __init__(self,pages):
        self.prev=None
        self.pages=pages
        self.Next=None

class Doubly_Linked_list:
    def __init__(self):
        self.head=None

    

    def Display(self):
        if self.head is None:
            print("Node Is Empty")

        else:
            temp=self.head
            while temp:
                print(temp.pages, "<------>", end=" ")
                temp=temp.Next
            print("None")

p1=Browser("Google")
p2=Browser("YouTube")
p3=Browser("Gmail")

d=Doubly_Linked_list()

d.head=p1
p1.Next=p2
p2.prev=p1

p2.Next=p3
p3.prev=p2


d.Display()










