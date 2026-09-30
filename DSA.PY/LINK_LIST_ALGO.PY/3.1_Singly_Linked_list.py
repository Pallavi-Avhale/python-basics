''' 
LINKED_LIST:

# Create a Node class
class Node:

    # Constructor: Runs automatically when a new node is created
    def __init__(self, data):

        # Store the value (data) inside the node
        self.data = data

        # Initially, the node is not connected to any other node
        self.next = None


# Create a Singly Linked List class
class Singly_linked_list:

    # Constructor: Creates an empty linked list
    def __init__(self):

        # Head points to the first node.
        # Initially there are no nodes, so head is None.
        self.head = None


    # Function to display all nodes of the linked list
    def display(self):

        # Check whether the linked list is empty
        if self.head is None:

            # If head is None, no node exists
            print("Singly_linked_list will be empty")

        else:

            # Create a temporary variable to traverse the list.
            # We use temp so that the original head is not changed.
            temp = self.head

            # Continue until temp becomes None
            while temp:

                # Print the current node's data
                print(temp.data, "-------->", end=" ")

                # Move temp to the next node
                temp = temp.next

            # After the last node, print None
            print("None")


# Create an object of the linked list
s = Singly_linked_list()

# Create the first node with data 10
n1 = Node(10)

# Make n1 the first node (head) of the linked list
s.head = n1

# Create the second node with data 20
n2 = Node(20)

# Connect first node to second node
n1.next = n2

# Create the third node with data 30
n3 = Node(30)

# Connect second node to third node
n2.next = n3

# Create the fourth node with data 40
n4 = Node(40)

# Connect third node to fourth node
n3.next = n4

# Call the display function to print the linked list
s.display()


------------------------>

Step-by-step visualization

Initially:

head
 │
 ▼
None

After creating n1:

head
 │
 ▼
[10 | None]

After n1.next = n2:

head
 │
 ▼
[10 | • ] ───► [20 | None]

After n2.next = n3:

head
 │
 ▼
[10 | • ] ───► [20 | • ] ───► [30 | None]

After n3.next = n4:

head
 │
 ▼
[10 | • ] ───► [20 | • ] ───► [30 | • ] ───► [40 | None]
Why do we use temp = self.head?

We use:

temp = self.head

because we want to traverse (visit) all nodes without changing the head.

If we wrote:

self.head = self.head.next

inside the loop, the head would keep moving forward and eventually become None, causing us to lose the entire linked list.

Using a temporary variable keeps the head safe:

head
 │
 ▼
10 → 20 → 30 → 40 → None
 ▲
temp (moves)

After every iteration:

Iteration 1:
temp → 10

Iteration 2:
temp → 20

Iteration 3:
temp → 30

Iteration 4:
temp → 40

Iteration 5:
temp → None (loop stops)
Output
10 --------> 20 --------> 30 --------> 40 --------> None
''' 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Singly_linked_list:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Singly_linked_list will be empty")

        else:
            temp=self.head
            while temp:  #while self.head
                print(temp.data,"-------->",end=" ")
                temp=temp.next
            print("None")

s=Singly_linked_list()
n1=Node(10)
s.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s.display()
'''

"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(10)  first Node
n2=Node(20)   second Node
n3=Node(30)   Third Node
n4=Node(40)    Fourth Node


class Singly_linked_list:
    def __init__(self):
        self.head=None'
        

node------> | data | next|

node-------> None ----------> [data|next]


if self.head is None :------>???
  empty list


How to create Node----->??
n1=Node(10)  first Node

How To connect singlylinkedlist-----> Node

first-----> we have to create object of singlylinkedlist class

object=className()
s=singlylinkedlist()

s.head=n1-------->  n1--->Node  head---> self.head

s.self.head=10----->  output---> [10---->None]

n2=Node(20)   second Node

n1.next=n2------->[10------>20------>None]


n3=Node(30)   Third Node
n2.next=n3----->[10------>20------>30------->None]


n4=Node(40)
n3.next=n4----->[10------>20------>30------->40---->None]
"""









class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(5)
n2=Node(6)
n3=Node(7)
n4=Node(8)

class Linked_list:
    def __init__(self):
        self.head=None


    def Insert_First(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def display(self):
        if self.head is None:
            print("empty--->data")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--------->",end=" ")
                temp=temp.next
            print("None")
l=Linked_list()
l.head=n1   #l.self.head=5---->[5]
n1.next=n2
n2.next=n3
n3.next=n4
l.Insert_First(3)
l.Insert_First(13)
l.display()


'''
class Node:
    def __init__(self,data):
        self.data=data             #---> Node[data|next]---> self.data & self.next
        self.next=None 
class Singly_linked_list:          #----> To link with node create one another class
    def __init__(self):
        self.head=None             #---->not pass any value 

    def display(self):
        if self.head is None:      
            print("Singly_linked_list will be empty") 

        else:
            temp=self.head              
            while temp:
                print(temp.data,"------------>", end=" ")
                temp=temp.next        # ---> To connect with next value( If there is no next value is present it will show the none )
                print("None")
n1=Node(5)
n2=Node(3)
n3=Node(6)

s=Singly_linked_list()
s.display()
s.head=n1          #------> s.self.head=5------>[5]
n1.next=n2
n2.next=n3


'''
NB.next=n2
n1.head=NB

self.head=Nb 
Nb.next=slf.head
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(5)
n2=Node(6)
n3=Node(7)
n4=Node(8)

class Linked_list:
    def __init__(self):
        self.head=None


    def Insert_First(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def display(self):
        if self.head is None:
            print("empty--->data")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--------->",end=" ")
                temp=temp.next
            print("None")
l=Linked_list()
l.head=n1   #l.self.head=5---->[5]
n1.next=n2
n2.next=n3
n3.next=n4
l.Insert_First(3)
l.Insert_First(13)
l.display()

'''
create Node[data|next]
class Node:
    def __init__

    |
craete a class Link Node to singly linlked
    |
    To insert the value before the node[head]N1
    |
create a function display the node
    |
create object to display the class information
'''

class Node:
    def __init__(self,data):
        self.data=data           #--->[data | next]   
        self.next=None           #--->[data | next]

n1=Node(2)          #--> [2 | None]
n2=Node(4)          #--> [4 | None]
n3=Node(6)          #--> [6 | None]
n4=Node(8)          #--> [8 | None]

class Link:
    def __init__(self):
        self.head=None          #--> Still not passing any value --> It will be Empty [None]

    def display(self):
        if self.head is None:             #--->[head | None] Check the self.head is None or not
            print("Link is Empty")

        else:
            a=self.head                  #--> insted of moving head value we craete new variable it will move to check another values        
            while a:
                print(a.data,"----->", end=" ")
                a=a.next

            print("None")

l=Link()       #--> object Creation to add the value to head
l.head=n1      #-->[ 2 ----> None]  
n1.next=n2     #-->[ 2 ----> 4 -----> None]
n2.next=n3     #-->[ 2 ----> 4 -----> 6 -----> None]
n3.next=n4     #-->[ 2 ----> 4 -----> 6 -----> 8 -----> None]
l.display()    #---->2 -----> 4 -----> 6 -----> 8 -----> None

print()

# Insert at the Begining 
class N:
    def __init__(self,value):
        self.value=value
        self.add=None

n1=N(10)
n2=N(20)
n3=N(30)
n4=N(40)
n5=N(50)

class Connect:
    def __init__(self):
        self.head=None

    def insert_first(self,value):      #
        New=N(value)             #--> New Node is Created
        New.add=self.head        #--> [New | Address] connect to head --> [ value | address ]
        self.head=New            #--> ? 

    def Show(self):
        if self.head is None:
            print("NO VALUE IS PRESENT")
        else:
            place=self.head
            while place:
                print(place.value, "--->>", end=" ")
                place=place.add

            print("Empty")

o=Connect()
o.head=n1
n1.add=n2
n2.add=n3
n3.add=n4
n4.add=n5
o.insert_first(5)       #5 --->> 10 --->> 20 --->> 30 --->> 40 --->> 50 --->> Empty
o.Show()          #10 --->> 20 --->> 30 --->> 40 --->> 50 --->> Empty

print()

# ----------------------------------------------------------------------------

class Train:
    def __init__(self, value):
        self.value=value
        self.add=None

c1=Train(0)
c2=Train(2)
c3=Train(4)

class Coach:
    def __init__(self):
        self.engine=None


    def Insert_First(self,value):
        p=Train(value)
        p.add=self.engine
        self.engine=p          #--->?

    def Insert_Last(self,value):
        NL=Train(value)
        temp=self.engine

        while temp.add:             #---> It will run untill the value get become None / Zero
            temp=temp.add

        temp.add=NL                 #----> where the while condition is stop it will connect again to the last element

    def Track(self):
        if self.engine is None:
            print(" Train is Empty")

        else:
            temp=self.engine
            while temp:
                print(temp.value, "--->>", end=" ")
                temp=temp.add
            print("None")

c=Coach()
c.engine=c1
c1.add=c2
c2.add=c3
c.Insert_First(0.5)
c.Insert_Last(10)
c.Track()           #------> 0.5 --->> 0 --->> 2 --->> 4 --->> 10 --->> None

print()

# ----------------------------------------->


class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None           #-->[ data | Next ] --> Declare Both

class Singly_Link_List:
    def __init__(self):
        self.head=None

    def Insert_F(self,data):
        F=Node(data)
        F.Next=self.head
        self.head=F

    def Insert_L(self,data):
        L=Node(data)
        temp=self.head
        
        while temp.Next:
            temp=temp.Next
        temp.Next=L

    def show(self):
        if self.head is None:
            print("Empty")

        else:
            temp=self.head
            while temp:
                print(temp.data,"--->>",end=" ")
                temp=temp.Next
            print("None")

p=Node(30)
p2=Node(40)
p3=Node(50)
p4=Node(60)

s=Singly_Link_List()
s.head=p
p.Next=p2
p2.Next=p3
p3.Next=p4

s.Insert_F(10)
s.Insert_L(100)

s.show()     #----> 10 --->> 30 --->> 40 --->> 50 --->> 60 --->> 100 --->> None

print()

# ---------------------------------------------->

''' 
# Insert at Particular position
two things req -->
POS   --> Particular Position 
Data  --> Element 

Insert in between  1  and 2 position 

def pos(3--> self, pos, data):
    Np=Node(data)      -------> Create node
    temp=self.head     -------> Start from beginning
    for i in range(pos-1):  -----> check position by squence
        temp=temp.next      -----> check where next part is empty or none ---> if true then stop the iteration 
    Np.next=temp.next       -----> np.next=temp.next ---> added next element memory addres to the collection
    temp=temp.next          -----> adding to the previous node 

    Np=Node(data)
    temp=self.head
       
if pos==0:
    NB.next=self.head
    self.head=NB
    return

temp=self.head
for i in range(pos-2):
    temp=temp.next


'''
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None           #-->[ data | Next ] --> Declare Both

class Singly_Link_List:
    def __init__(self):
        self.head=None

    def Insert_F(self,data):
        F=Node(data)
        F.Next=self.head
        self.head=F

    def Insert_L(self,data):
        L=Node(data)
        temp=self.head
        
        while temp.Next:
            temp=temp.Next
        temp.Next=L

    def Insert_Loc(self,Pos,data):
        Node_Pos=Node(data)
        Np=Node(data)
        temp=self.head

        if pos==0:
            NB.next=self.head
            self.head=NB
        return

        temp=self.head
        for i in range(pos-2):
        temp=temp.next

    def show(self):
        if self.head is None:
            print("Empty")

        else:
            temp=self.head
            while temp:
                print(temp.data,"--->>",end=" ")
                temp=temp.Next
            print("None")

p=Node(30)
p2=Node(40)
p3=Node(50)
p4=Node(60)

s=Singly_Link_List()
s.head=p
p.Next=p2
p2.Next=p3
p3.Next=p4

s.Insert_F(10)
s.Insert_L(100)

s.show()     #----> 10 --->> 30 --->> 40 --->> 50 --->> 60 --->> 100 --->> None

print()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(2)
n2=Node(4)
n3=Node(6)
n4=Node(8)

class Link:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Link is Empty")

        else:
            a=self.head
            while a:
                print(a.data,"----->", end=" ")
                a=a.next

            print("None")

l=Link()
l.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
l.display()             #---->2 -----> 4 -----> 6 -----> 8 -----> None

print()

class N:
    def __init__(self,value):
        self.value=value
        self.add=None

n1=N(10)
n2=N(20)
n3=N(30)
n4=N(40)
n5=N(50)

class Connect:
    def __init__(self):
        self.head=None

    def insert(self,value):
        New=N(value)
        New.add=self.head
        self.head=New

    def Show(self):
        if self.head is None:
            print("NO VALUE IS PRESENT")
        else:
            place=self.head
            while place:
                print(place.value, "--->>", end=" ")
                place=place.add

            print("Empty")

o=Connect()
o.head=n1
n1.add=n2
n2.add=n3
n3.add=n4
n4.add=n5
o.insert(5)       #5 --->> 10 --->> 20 --->> 30 --->> 40 --->> 50 --->> Empty
o.Show()          #10 --->> 20 --->> 30 --->> 40 --->> 50 --->> Empty

'''   
'''

    0                1                2                3               4
[10 | 1000] ---> [20 | 2000] ---> [30 | 3000] ---> [40 | 4000] ---> [5 | 5000]
                                      |                |
                                      ------------------


def delete_first(self):
    temp=self.head
    self.head=temp.next
    temp.next=None

def delete_first(self):
    self.head=self.head.next         #-------> head part is shifting to the next


------------->
DELETE LAST NODE

temp=self.head

while temp.next.next:
    temp=temp.next
temp.next=None

tracing

temp=self.head ----> 10 

iteration 1-->
temp=10
temp.next(head.next)--> 20
temp.next.next---> 30

iteration 2
temp=20
temp.next---> 30 
temp.next.next---> 40 

iteration 3 
temp=30
temp.next---> 40
temp.next.next----> 50 --------> 40 no is holdding the 50 so, break the connection between 40 to 50 ( temp.next=None)


'''      

class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None


class Link_list:
    def __init__(self):
        self.head=None


    def Insert_F(self, data):
        New_Node=Node(data)
        New_Node.Next=self.head
        self.head=New_Node


    def Insert_last(self,data):
        Last_Node=Node(data)
        temp=self.head

        while temp.Next:
            temp=temp.Next
        temp.Next=Last_Node
        

    def display(self):
        if self.head is None:
            print("Empty")

        else:
            temp=self.head

            while temp:
                print(temp.data, "-------->", end=" ")
                temp=temp.Next

            print("None")

N1=Node(30)
N2=Node(40)
N3=Node(50)

l=Link_list()
l.head=N1
N1.Next=N2
N2.Next=N3
l.Insert_F(10)          #----->10 --------> 30 --------> 40 --------> 50 --------> None
l.Insert_last(99)       #-----> 10 --------> 30 --------> 40 --------> 50 --------> 99 --------> None
l.display()

print()

# ------------------------------------------------------------------------------------------------------------


class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None


class Link_list:
    def __init__(self):
        self.head=None


    def Insert_F(self, data):
        New_Node=Node(data)
        New_Node.Next=self.head
        self.head=New_Node


    def Insert_last(self,data):
        Last_Node=Node(data)
        temp=self.head

        while temp.Next:
            temp=temp.Next
        temp.Next=Last_Node
        



    def display(self):
        if self.head is None:
            print("Empty")

        else:
            temp=self.head

            while temp:
                print(temp.data, "-------->", end=" ")
                temp=temp.Next

            print("None")

N1=Node(30)
N2=Node(40)
N3=Node(50)

l=Link_list()
l.head=N1
N1.Next=N2
N2.Next=N3
l.Insert_F(10)          #----->10 --------> 30 --------> 40 --------> 50 --------> None
l.Insert_last(99)       #-----> 10 --------> 30 --------> 40 --------> 50 --------> 99 --------> None
l.display()


'''

def delete_first(self):
    temp=self.head
    self.head=temp.next
    temp.next=None

def delete_first(self):
    self.head=self.head.next         #-------> head part is shifting to the next


------------->
DELETE LAST NODE

temp=self.head

while temp.next.next:
    temp=temp.next
temp.next=None

tracing

temp=self.head ----> 10 

iteration 1-->
temp=10
temp.next(head.next)--> 20
temp.next.next---> 30

iteration 2
temp=20
temp.next---> 30 
temp.next.next---> 40 

iteration 3 
temp=30
temp.next---> 40
temp.next.next----> 50 --------> 40 no is holdding the 50 so, break the connection between 40 to 50 ( temp.next=None)

---------------------------------------------------------------------------------------------------------------------------------->

def Delete_particular_pos(self, Pos):
    if Pos==0:                        #-------> OPTIONAL 
        self.head=self.head.next
        return

    temp=self.head
    for i in range(Pos-1):
        
        temp=temp.next
    temp.next=temp.next.next




'''