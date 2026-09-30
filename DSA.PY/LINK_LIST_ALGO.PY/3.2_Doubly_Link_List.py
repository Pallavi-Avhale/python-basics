'''
DOUBLY LINKED LIST

------------------------------------------------------------------------------

IT WILL MOVE FORWARD AS WELL AS BACKWARD
IT USE [ PREV | DATA | NEXT ]
IT WILL USE MORE OR HUGE MEMORY




'''

class Node:
    def __init__(self,data):
        self.Prev=None
        self.data=data
        self.Next=None
n1=Node(1)        #------[None | 1 | None]
n2=Node(2)        #------[None | 2 | None]
n3=Node(3)        #------[None | 3 | None]
n4=Node(4)        #------[None | 4 | None]
n5=Node(5)        #------[None | 5 | None]

class Doubly_Linked_List:
    def __init__(self):
        self.head=None

    def Display(self):
        if self.head is None:
            print("Empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data, "<------>", end=" ")
                temp=temp.Next
            print("None")


d=Doubly_Linked_List()

n1=Node(1)
d.head=n1

n2=Node(2)
n1.Next=n2
n2.Prev=n1

n3=Node(3)
n2.Next=n3
n3.prev=n2

n4=Node(4)
n3.Next=n4
n4.prev=n3

n5=Node(5)
n4.Next=n5
n5.prev=n4

d.Display()

print()

# -----------------------------------------------------------------------------------------------------------


class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.Next=None

n1=Node(100)        #------[None | 1 | None]
n2=Node(200)        #------[None | 2 | None]
n3=Node(300)        #------[None | 3 | None]
n4=Node(400)        #------[None | 4 | None]
n5=Node(500)        #------[None | 5 | None]

class D_L_L:
    def __init__(self):
        self.head=None

    def Insert_First(self,data):
        N=Node(data)
        N.next=self.head
        self.head.prev=N
        self.head=N

    def Display(self):
        if self.head is None:
            print("Empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data, "<------>", end=" ")
                temp=temp.Next
            print("None")


l=D_L_L()
l.head=n1

n1.Next=n2
n2.prev=n1

n2.Next=n3
n3.prev=n2

n3.Next=n4
n4.prev=n3

n4.Next=n5
n5.prev=n4

l.Insert_First(50)

l.Display()

# -------------------------------------------------------------------------------------------
#ex2
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

class DLL:
    def __init__(self):
        self.head=None

    # inserting new node at beginning
    def Insert_first(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head.prev=nb
        self.head=nb


    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
            print("None")
d=DLL()
d.head=n1

n1.next=n2
n2.prev=n1

n2.next=n3
n3.prev=n2

n3.next=n4
n4.prev=n3

n4.next=n5
n5.prev=n4  #10 <--> 20 <--> 30 <--> 40 <--> 50 <--> None

d.Insert_first(5)
# 5 <--> 10 <--> 20 <--> 30 <--> 40 <--> 50 <--> None


d.display()

print()

# ----------------------------------------------------------------------------------------------

# Insert_First_Node------------------------>

class Node:
    def __init__(self,data):
        self.Prev=None
        self.data=data
        self.Next=None
n1=Node(1)        #------[None | 1 | None]
n2=Node(2)        #------[None | 2 | None]
n3=Node(3)        #------[None | 3 | None]
n4=Node(4)        #------[None | 4 | None]
n5=Node(5)        #------[None | 5 | None]

class Doubly_Linked_List:
    def __init__(self):
        self.head=None


    def First(self,data):
        N=Node(data)
        temp=self.head
        temp.prev=N
        N.Next=temp
        self.head=N


    def Display(self):
        if self.head is None:
            print("Empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data, "<------>", end=" ")
                temp=temp.Next
            print("None")


d=Doubly_Linked_List()

n1=Node(1)
d.head=n1

n2=Node(2)
n1.Next=n2
n2.Prev=n1

n3=Node(3)
n2.Next=n3
n3.prev=n2

n4=Node(4)
n3.Next=n4
n4.prev=n3

n5=Node(5)
n4.Next=n5
n5.prev=n4

d.First(90)
d.Display()

# 90 <------> 1 <------> 2 <------> 3 <------> 4 <------> 5 <------> None
print()



# ----------------------------------------------------------------------------------------------

# Insert_First_Node------------------------>

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.Next=None
n1=Node(1)        #------[None | 1 | None]
n2=Node(2)        #------[None | 2 | None]
n3=Node(3)        #------[None | 3 | None]
n4=Node(4)        #------[None | 4 | None]
n5=Node(5)        #------[None | 5 | None]

class Doubly_Linked_List:
    def __init__(self):
        self.head=None


    def First(self,data):
        N=Node(data)
        temp=self.head
        temp.prev=N
        N.Next=temp
        self.head=N

    def Last(self,data):
        L=Node(data)
        temp=self.head
        while temp.Next is not None:     #----> Stop
            temp=temp.Next               
        temp.Next=L                      #---> connecting to New Last Node
        L.prev=temp                      #---> Connecting to Previous Node address
        


    def Display(self):
        if self.head is None:
            print("Empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data, "<------>", end=" ")
                temp=temp.Next
            print("None")


d=Doubly_Linked_List()

n1=Node(1000)
d.head=n1

n2=Node(1500)
n1.Next=n2
n2.prev=n1

n3=Node(2000)
n2.Next=n3
n3.prev=n2

n4=Node(2500)
n3.Next=n4
n4.prev=n3

n5=Node(3000)
n4.Next=n5
n5.prev=n4

d.First(500)        #--------> 500 <------> 1000 <------> 1500 <------> 2000 <------> 2500 <------> 3000 <------> None
# d.Last(5000)      #--------> 500 <------> 1000 <------> 1500 <------> 2000 <------> 2500 <------> 3000 <------> 5000 <------> None
d.Display()

print()

# ------------------------------------------------------------------------------------

class Train:
    def __init__(self,data):
        self.Prev=None
        self.data=data
        self.Next=None

class Express:
    def __init__(self):
         self.head=None

    def Show(self):
        if self.head is None:           #------> if 1st node is not 
            print("Empty")

        else:
            temp=self.head
            while temp:
                print(temp.data,"<---->",end=" ")
                temp=temp.Next
            print("None")

e=Express()
p1=Node(99)
e.head=p1

p2=Node(88)
p1.Next=p2
p2.prev=p1

e.Show()

# ----------------------------------------------------------------------------------------------


class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.Next=None

n1=Node(100)        #------[None | 1 | None]
n2=Node(200)        #------[None | 2 | None]
n3=Node(300)        #------[None | 3 | None]
n4=Node(400)        #------[None | 4 | None]
n5=Node(500)        #------[None | 5 | None]

class D_L_L:
    def __init__(self):
        self.head=None

    def Insert_First(self,data):
        N=Node(data)
        N.Next=self.head
        self.head.prev=N
        self.head=N

    def Last(self, data):
        NL=Node(data)
        temp=self.head
        temp=temp.Next
        while temp.Next is not None:
            temp=temp.Next
        temp.Next=NL
        NL.prev=temp


    def Display(self):
        if self.head is None:
            print("Empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data, "<------>", end=" ")
                temp=temp.Next
            print("None")


l=D_L_L()
l.head=n1

n1.Next=n2
n2.prev=n1

n2.Next=n3
n3.prev=n2

n3.Next=n4
n4.prev=n3

n4.Next=n5
n5.prev=n4

l.Insert_First(50)
# 50 <------> 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> None
l.Last(30) 
#50 <------> 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> 30 <------> None
l.Display() 
# 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> None

print()
# ----------------------------------------------------------------------------------------------------------

#INSERT AT PARTICULAR POSIITON-------->

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.Next=None

n1=Node(100)        #------[None | 1 | None]
n2=Node(200)        #------[None | 2 | None]
n3=Node(300)        #------[None | 3 | None]
n4=Node(400)        #------[None | 4 | None]
n5=Node(500)        #------[None | 5 | None]

class D_L_L:
    def __init__(self):
        self.head=None

    def Insert_First(self,data):
        N=Node(data)
        N.Next=self.head
        self.head.prev=N
        self.head=N

    def Last(self, data):
        NL=Node(data)
        temp=self.head
        temp=temp.Next
        while temp.Next is not None:
            temp=temp.Next
        temp.Next=NL
        NL.prev=temp

    def Insert_pos(self, pos, data):
        NP=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.Next              #---> stop before the position insert ---> pos=2---> (3-1)--> iteration ----> 0,1
        next_node=temp.Next             #--> next_node=temp.Next=200, temp---> 100, temp.Next=200 ---> stop
        NP.Next=next_node               #--> NP-->45, 45---> 300  
        NP.prev=temp                    #-->  45-----> 200
        temp.Next=NP                    #-->  200 ---> 45
        next_node.prev=NP               #-->  300 -----> 45

    def Display(self):
        if self.head is None:
            print("Empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data, "<------>", end=" ")
                temp=temp.Next
            print("None")


l=D_L_L()
l.head=n1

n1.Next=n2
n2.prev=n1

n2.Next=n3
n3.prev=n2

n3.Next=n4
n4.prev=n3

n4.Next=n5
n5.prev=n4

# l.Insert_First(50)
# 50 <------> 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> None
# l.Last(30) 
#50 <------> 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> 30 <------> None

l.Insert_pos(2,45)
l.Display() 
# 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> None

print()

# ----------------------------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class double:
    def __init__(self):
        self.head=None

    def Insert_First(self,data):
        NB=Node(data)
        temp=self.head
        temp.prev=NB
        NB.next=temp
        self.head=NB

    def Insert_Last(self,data):
        NL=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=NL
        NL.prev=temp

    def Insert_Position(self,POS,data):
        NP=Node(data)  #15
        temp=self.head
        for i in range(POS-1):
            temp=temp.next
        next_node=temp.next  
        NP.next=next_node
        NP.prev=temp
        temp.next=NP
        next_node.prev=NP

    def Delete_First(self):
        self.head=self.head.next
        self.head.prev=None


    def display(self):
        if self.head is None:
            print("its empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data,"<-------->",end=" ")
                temp=temp.next
            print("None")

d=double()
n1=Node(10)
d.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
# d.Insert_First(5)
# d.Insert_Last(50)
# # d.Insert_Position(1,11)
# d.Insert_Position(3,100)
d.Delete_First()
d.display()
print()

# ----------------------------------------------------------------------------------------

# DELETE AT FIRST


class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.Next=None

n1=Node(100)        #------[None | 1 | None]
n2=Node(200)        #------[None | 2 | None]
n3=Node(300)        #------[None | 3 | None]
n4=Node(400)        #------[None | 4 | None]
n5=Node(500)        #------[None | 5 | None]

class D_L_L:
    def __init__(self):
        self.head=None

    def Insert_First(self,data):
        N=Node(data)
        N.Next=self.head
        self.head.prev=N
        self.head=N

    def Last(self, data):
        NL=Node(data)
        temp=self.head
        temp=temp.Next
        while temp.Next is not None:
            temp=temp.Next
        temp.Next=NL
        NL.prev=temp

    def Insert_pos(self, pos, data):
        NP=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.Next              #---> stop before the position insert ---> pos=2---> (3-1)--> iteration ----> 0,1
        next_node=temp.Next             #--> next_node=temp.Next=200, temp---> 100, temp.Next=200 ---> stop
        NP.Next=next_node               #--> NP-->45, 45---> 300  
        NP.prev=temp                    #-->  45-----> 200
        temp.Next=NP                    #-->  200 ---> 45
        next_node.prev=NP               #-->  300 -----> 45


    def Delete_F(self):
        self.head=self.head.Next
        self.head.prev=None

    def Delete_Last(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next            
        temp.next=None

    def Delete_Particular_Pos(self,Pos):
        temp=self.head

        if Pos==0:                     #-----> delete pos 0 --> self.head
            self.head=self.head.Next   #-----> Change self.head position 
            return                     #-----> return remaining element
        temp=self.head                 #-----> if condition is not true ---> self,head store in temp 
        for i in range(Pos-1):         #-----> for to take upto particular position (3-1)---> 2---> excluded ---> iterations are 0, 1 ---> delete 2nd position 
            temp=temp.Next             #-----> check 0 
        temp.Next=temp.Next.Next
        temp.Next.Prev=temp


    def Display(self):
        if self.head is None:
            print("Empty List")

        else:
            temp=self.head
            while temp:
                print(temp.data, "<------>", end=" ")
                temp=temp.Next
            print("None")


l=D_L_L()
l.head=n1

n1.Next=n2
n2.prev=n1

n2.Next=n3
n3.prev=n2

n3.Next=n4
n4.prev=n3

n4.Next=n5
n5.prev=n4

# l.Insert_First(50)
# 50 <------> 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> None
# l.Last(30) 
#50 <------> 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> 30 <------> None

# l.Insert_pos(2,45)

l.Delete_F()   #-------> 200 <------> 300 <------> 400 <------> 500 <------> None
l.Display() 
# 100 <------> 200 <------> 300 <------> 400 <------> 500 <------> None


print()


'''
DELETE FIRST AND LAST NODE 

def Delete_First(self):
    self.head=self.head.next
    self.head.prev=None

def Delete_Last(self):
    temp=self.head
    while temp.next.next:
        temp=temp.next

    temp.next=None

'''
# ----------------------------------------------------------------------------


# class Char:
#     def __init__(self,Value):
#         self.Prev=None
#         self.Value=Value
#         self.Next=None

# class Alpha:
#     def __init__(self):
#         self.head=None

#     def Insert_F(self, Value):
#         NF=Char(Value)
#         NF.Next=self.head
#         self.head.prev=NF
#         self.head=NF

#     def Insert_L(self, Value):
#         Nl=Char(Value)
#         temp=self.head
#         temp=temp.Next

#         while temp.Next is not None:
#             temp=temp.Next
#         temp.Next=Nl
#         Nl.Prev=temp.Next
        
#     def Show(self):
#         if self.head is None:
#             print("EMPTY NODE")

#         else:
#             blank=self.head
#             while blank:
#                 print(blank.Value, "<--->", end=" ")
#                 blank=blank.Next
#             print("None")

# a1=Char("B")
# a2=Char("C")
# a3=Char("D")

# a=Alpha()
# a.head=a1

# a1.Next=a2
# a2.Prev=a1

# a2.Next=a3
# a3.prev=a2

# a.Insert_F("a")         #-------> a <---> B <---> C <---> D <---> None

# a.Insert_L("z")         #-------> a <---> B <---> C <---> D <---> z <---> None
# a.Show()       #--> B <---> C <---> D <---> None


# -------------------------------------------------------------

