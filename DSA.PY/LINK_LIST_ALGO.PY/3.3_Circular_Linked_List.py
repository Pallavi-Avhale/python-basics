'''

CIRCULAR LIKED LIST

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None

class Circular_Singly_List:
    def __init__(self):
        self.head=None

    def Display(self):
        if self.head is None:
            print("Empty")

        else:
            temp=self.head
            while temp.Next!=self.head:          #----> if condition become true --------> head always pointing to tail <-----> tail pointing to head
                print(temp.data,"------>", end=" ")
                temp=temp.Next
            print(temp.data)

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)         

c=Circular_Singly_List()
c.head=n1
n1.Next=n2               #n1.Next=n1------> if not it show Attribute Error -------> then after connection ----> n1.Next=n2
n2.Next=n3               #n2.Next=n1------> if not it show Attribute Error -------> then after connection ----> n2.Next=n3               #n2.Next=n1 -------> then after connection ----> n2.Next=n3
n3.Next=n4               #n3.Next=n1------> if not it show Attribute Error -------> then after connection ----> n3.Next=n4
n4.Next=n1               #n4.Next=n1------> if not it show Attribute Error -------> then after connection ----> n4.Next=n1

c.Display()

# temp=10
# temp.Next=20
# 20!=10 ------> true

print()

# -------------------------------------------------------------------------------

class New:
    def __init__(self,data):
        self.data=data
        self.Next=None

class CSl:
    def __init__(self):
        self.head=None

    def Show(self):
        if self.head is None:
            print("Empty")

        else:
            temp=self.head
            while temp.Next!=self.head:          #----> if condition become true --------> head always pointing to tail <-----> tail pointing to head
                print(temp.data,"------>", end=" ")
                temp=temp.Next
            print(temp.data)
n1=New("@")
n2=New("*")
n3=New("<>")
n4=New("#")
n5=New("$")

t=CSl()
t.head=n1
n1.Next=n2
n2.Next=n3
n3.Next=n4
n4.Next=n5
n5.Next=n1

t.Show()           # o/p ---> @ ------> * ------> <> ------> # ------> $

print()

# ------------------------------------------------------------------------------------------------

# INSERT_FIRST_ELEMENT

#[ 100 | 2000] ---> [ 200 | 3000] ---> [ 300 | 4000] ---> [ 400 | 1000]

#[  5  | 1000] ---> [ 100 | 2000] ---> [ 200 | 3000] ---> [ 300 | 4000] ---> [ 400 | 1000]
    
class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None

class Circular_Singly_List:
    def __init__(self):
        self.head=None

    def Insert_F(self,data):
        NB=Node(data)
        temp=self.head
        while temp.Next!=self.head:
            temp=temp.Next
        NB.Next=self.head
        self.head=NB
        temp.Next=NB            

    def Insert_L(self,data):
        NL=Node(data)
        temp=self.head
        while temp.Next!=self.head:
            temp=temp.Next
        temp.Next=NL
        NL.Next=self.head                    # 5<------ 30   head <------ tail


    def Insert_Particular_Pos(self, Pos, data):
        NP=Node(data)
        temp=self.head
        for i in range(Pos-1):           # 4-1 = 3
            temp=temp.Next               # temp=5 , temp.next=100
        NP.Next=temp.Next
        temp.Next=NP
        
    
    def Display(self):
        if self.head is None:
            print("Empty")

        else:
            temp=self.head
            while temp.Next!=self.head:          #----> if condition become true --------> head always pointing to tail <-----> tail pointing to head
                print(temp.data,"------>", end=" ")
                temp=temp.Next
            print(temp.data)

n1=Node(100)
n2=Node(200)
n3=Node(300)
n4=Node(400)         

c=Circular_Singly_List()
c.head=n1
n1.Next=n2               #n1.Next=n1------> if not it show Attribute Error -------> then after connection ----> n1.Next=n2
n2.Next=n3               #n2.Next=n1------> if not it show Attribute Error -------> then after connection ----> n2.Next=n3               #n2.Next=n1 -------> then after connection ----> n2.Next=n3
n3.Next=n4               #n3.Next=n1------> if not it show Attribute Error -------> then after connection ----> n3.Next=n4
n4.Next=n1               #n4.Next=n1------> if not it show Attribute Error -------> then after connection ----> n4.Next=n1


c.Insert_F(5)            #5 ------> 100 ------> 200 ------> 300 ------> 400
c.Insert_L(30)           #5 ------> 100 ------> 200 ------> 300 ------> 400 ------> 30
c.Insert_Particular_Pos(3, 150)
c.Display()

print()