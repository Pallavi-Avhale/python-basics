'''
BINARY SEARCH TREE

Y=[40,35,10,70,80,25,13,7,75,85]

#BINARY SEARCH TREE CREATION RULES
       /          \
SMALLER NUM      BIGGER NUM       


             40
         /         \
        35         70
      /               \
    10                 80
   /   \              /  \
  7    25(B)         75   85
        /
       131

'''
# x=[70,35,11,7,45,90,100,1,85,23,11]

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

# root=Node(70)
# root.left=Node(35)
# root.left.left=Node(11)
# root.left.left.left=Node(7)
# root.left.left.left.left=Node(1)
# root.left.right=Node(45)
# root.left.left.right=Node(23)
# root.left.left.right.left=Node(11)
# root.right=Node(90)
# root.right.left=Node(85)
# root.right.right=Node(100)  

'''
x=[70,35,11,7,45,90,100,1,85,23,11]

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Insert_data(root,data):
    if root is None:
        return Node(data)

    if data < root.data:                       # The left side always pass lower element
        root.left=Insert_data(root.left,data)

    else:                                      # If the element is bigger than root passing right side
        root.right=Insert_data(root.right,data)
    return root

root=None
for i in x:              #--> Starting root is None---> i is pointing to -----> 70 ---> root
    root=Insert_data(root,i)

root=Insert_data(root,65)              #-------> to add new element inside the root -->1 7 11 11 23 35 45 65 70 85 90 100 
root=Insert_data(root,0.5)             #-------> adding extra elemnt (outside (root=Insert_data(root,data))--0.5 1 7 11 11 23 35 45 65 70 85 90 100 

def In_order(root):
    if root is None:
        return
    In_order(root.left)
    print(root.data, end=" ")
    In_order(root.right)

In_order(root)                #----> 1 7 11 11 23 35 45 70 85 90 100  

print()
''' 
'''
# ------------------------------------------------------------------------------------------------------------

d=[66,90,23,11,0.5,45,10,900,1,1.5]

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Insert_value(root,data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left=Insert_value(root.left, data)

    else:
        root.right=Insert_value(root.right, data)

    return root

root=None
for i in d:
    root=Insert_value(root,i)

def In_order(root):
    if root is None:
        return

    
    In_order(root.left)
    print(root.data, end=" ")
    In_order(root.right)

In_order(root)                     #------> 0.5 1 1.5 10 11 23 45 66 90 900 


print()

# -------------------------------------------------------------------------------------


# FIND OUT SMALLER ELEMENT IN GIVEN CODE (LEFT)

a=[66,90,23,11,0.5,45,10,900,1,1.5]

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def small_value(root):
    if root is None:
        return None

    while root.left is not None:
        root=root.left

    return root.data
print(small_value(root))                 #--->SMALLER_ELEEMNT---> 0.5

print()

# -----------------------------------------------------------------------------

# FIND OUT SMALLER ELEMENT IN GIVEN CODE (LEFT)

a=[66,90,23,11,0.5,45,10,900,1,1.5]

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Bigger_value(root):
    if root is None:
        return None

    while root.right is not None:
        root=root.right

    return root.data
print(Bigger_value(root))                  #-->BIGGER_ELEMENT---> 900

print()


# -----------------------------------------------------------------------

# ---> TO SEARCH THE SPECIFIC ELEMENT-------------->

def Searching_Data(root,data):
    if root is None:                   # ---> If root is empty----> return False , If the root having data ---> moving to next if condition 
        return False

    if root.data==data:                 # 0.5==112 ----> false , 1==1 ----> True
        return True

    if data < root.data:                # data < root.data , 112 < 0.5 ------> 
        return Searching_Data(root.left, data)
    else:
        return Searching_Data(root.right, data)       # data > root.data, 112 > 900 ----> 

print(Searching_Data(root,9))                  #---> False


print()

# -----------------------------------------------------------------------------

# ----> Total_SUM_Node -----> 

def Total_Sum_Node(root):
    if root is None:
        return 0

    return root.data + Total_Sum_Node(root.left) + Total_Sum_Node(root.right)

print("TOTAL_SUM_NODES----->", Total_Sum_Node(root))             #----->TOTAL_SUM_NODES-----> 1148.0

print()

# --------------------------------------------------------------------------------------

# ----> Total_Node -----> 

def Total_Node(root):
    if root is None:
        return 0

    return 1 + Total_Node(root.left) + Total_Node(root.right)

print("TOTAL_NODES----->", Total_Node(root))             #----->TOTAL_NODES-----> 10

print()

# --------------------------------------------------------------------------------------
# TOTAL NON LEAF CODE

def Total_Non_Leaf(root):
    if root is None:
        return 0 

    if root.left is None and root.right is None:
        return 0 

    return ( 1 + Total_Non_Leaf(root.left) + Total_Non_Leaf(root.right))

print("TOTAL_NON_LEAF---->", Total_Non_Leaf(root))                #----> TOTAL_NON_LEAF----> 7

print()

# -------------------------------------------------------------------------------------


# TOTAL LEAF NODE

def Total_Leaf(root):
    if root is None:
        return 0 

    if root.left is None and root.right is None:
        return 1

    return Total_Leaf(root.left) + Total_Leaf(root.right)

print("TOTAL_LEAF---->", Total_Leaf(root))                #----> TOTAL_LEAF----> 3

print()

# ---------------------------------------------------------------------------------------------------------------------------------

# ----> EVEN NODES ---->

def Even_Data(root):
    if root is None:
        return

    if root.data % 2==0:
        print( root.data, end=" ")

    Even_Data(root.left)
    Even_Data(root.right)

Even_Data(root)           # ----> EVEN NODES ----> 66 10 90 900     

print()

# --------------------------------------------------------------------------------

# ----> ODD NODES ---->

def ODD_Data(root):
    if root is None:
        return

    if root.data % 2 !=0:
        print( root.data, end=" ")

    ODD_Data(root.left)
    ODD_Data(root.right)

ODD_Data(root)          # ----> ODD NODES ----> 23 11 0.5 1 1.5 45 

print()

# --------------------------------------------------------------------------------------------------------------------------
'''

'''

17-08-2026


               1            ---------> level -- 0 -- 1
         /          \
        2             3       ---------> level -- 1 -- 2, 3
      /  \           /  \
    4     5         6    7         ---------> level -- 2 -- 4, 5, 6, 7.
  

Level = position of a node from the root.
Root 1 is at Level 0.
Children 2, 3 are at Level 1.
Children 4, 5, 6, 7 are at Level 2.


-------------------------------------------------------------------------------------------------------

# We are importing deque from collections.
#
# deque is a special type of queue.
# Queue follows:
#
# FIRST IN ---> FIRST OUT
#
# Example:
# Queue = [1, 2, 3]
#
# First 1 will come out.
# Then 2.
# Then 3.

from collections import deque

# ============================================================
# NODE CLASS
# ============================================================

# Node means one element of the tree.

class Node:

    # __init__() runs automatically when we create a Node.
    #
    # data = value stored inside the node.

    def __init__(self, data):

        # Store the given value inside the node.
        self.data = data

        # Initially left side is empty.
        self.left = None

        # Initially right side is empty.
        self.right = None


# ============================================================

# CREATE THE TREE
# ============================================================

# Create the root node.
#
# Tree currently:
#
#        1
#
root = Node(1)


# Create the left child of 1.
#
# Tree:
#
#        1
#       /
#      2

root.left = Node(2)


# Create the right child of 1.

#
# Tree:
#
#        1
#       / \
#      2   3

root.right = Node(3)


# Create the left child of node 2.
#
# Tree:
#
#        1
#       / \
#      2   3
#     /
#    4

root.left.left = Node(4)


# Create the right child of node 2.

#
# Tree:
#
#        1
#       / \
#      2   3
#     / \
#    4   5

root.left.right = Node(5)


# Create the left child of node 3.
#
# Tree:
#
#        1
#       / \
#      2   3
#     / \ /
#    4  5 6

root.right.left = Node(6)

# Create the right child of node 3.
#
# Final Tree:
#
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

root.right.right = Node(7)


# ============================================================
# LEVEL ORDER TRAVERSAL
# ============================================================

# Level Order means:
#
# Visit nodes level by level.
#
# Level 0 ---> 1
# Level 1 ---> 2, 3
# Level 2 ---> 4, 5, 6, 7

#
# Output:
#
# 1 2 3 4 5 6 7


def Level_of_ORDER(root):

    # If root does not exist,
    # there is no tree to process.

    if root is None:
        return


    # Create an empty queue.

    
    #
    # Initially:
    #
    # queue = []

    queue = deque()


    # Add the root node into the queue.
    #
    # queue = [1]

    queue.append(root)


    # Continue the loop while the queue
    # contains something.
    #
    # When queue becomes empty,
    # while loop will stop.

    while queue:


        # Remove the FIRST node from the queue.

        #
        # popleft() means:
        # remove from the LEFT / FRONT side.
        #
        # Store the removed node inside y.

        y = queue.popleft()


        # Print the data of the removed node.

        print(y.data, end=" ")


        # Check whether the current node
        # has a left child.

        if y.left is not None:

            # If left child exists,
            # add it into the queue.

            queue.append(y.left)

        # Check whether the current node
        # has a right child.

        if y.right is not None:

            # If right child exists,
            # add it into the queue.

            queue.append(y.right)


# Call the function.
Level_of_ORDER(root)


print()


'''

# from collections import deque
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)


# def Level_of_ORDER(root):
#     if root is None:
#         return

#     queue=deque()          #--> deque( [ ] )
#     queue.append(root)     #--> deque([ 1 ])

#     while queue:                      # --> It will get stop when queue is empty
#         # queue[2, 3].popleft
#         y=queue.popleft()             # --> New_Variable ---> To store the removed element
#         print(y.data, end=" ")

#         if y.left is not None:          # ----> 1.left ---> root.left ---> Not none --->     
#             queue.append(y.left)

#         if y.right is not None:
#             queue.append(y.right)

# Level_of_ORDER(root)


'''

queue----> deque([])
queue.append(root)
queue--> [1]
y=queue.popleft()    ----------> 1 remove ----> level 0 ----> remove level zero element ---> now go left as well as right
print(y)

       1
     /   \
    2     3
  left    right

if y.left is not none:
queue[]
queue.append(y.left)
queue[2]

if y.right is not none:
queue[]
queue.append(y.right)
queue[3]

queue[2, 3]                              --------> level 1
y=queue.popleft() -------> 2 remove

queue[3,4,5]

y=queue.popleft() --------> 3 remove

queue[4,5,6,7]                        

if 4 have child 8 9 so first, it will check if y.left is not none ---> append(y.left)

after adding 8 9 --> then 4 get remove first 



'''

# print()

# # ---> TOTAL NUMBER OF NODE ---->

# def Total_Node(root):
#     if root is None:
#         return 0

#     return 1 + Total_Node(root.left) + Total_Node(root.right)

# print("Total_Node------->", Total_Node(root))   # ---> Total_Node-------> 7


# print()


''' 

# ============================================================
# TOTAL NUMBER OF NODES
# ============================================================

# This function counts how many nodes
# are present in the complete tree.

def Total_Node(root):

    # If root is None,
    # there is no node.
    #
    # Therefore return 0.

    if root is None:
        return 0


    # Count the current node as 1.
    #
    # Then count:
    #
    # 1. Left subtree
    # 2. Right subtree

    # Finally add all three values.

    return 1 + Total_Node(root.left) + Total_Node(root.right)

# Call Total_Node().
#
# Our tree has:
#
# 1, 2, 3, 4, 5, 6, 7
#
# Therefore answer = 7

print("Total_Node------->", Total_Node(root))


print()


'''
# ---> TOTAL NUMBER OF NODE ---->

# def Total_Edges(root):
#     Node=Total_Node(root)         # --> 7
#     return Node-1

# print("Total_Edges---->", Total_Edges(root))              # ----> Total_Edges----> 6


# print()

''' 

# ============================================================
# TOTAL NUMBER OF EDGES
# ============================================================

# An edge means the connection between
# two nodes.
#
# Example:
#
#       1
#      /
#     2
#
# The line connecting 1 and 2 is one edge.


def Total_Edges(root):

    # First find the total number of nodes.

    Node = Total_Node(root)

     # In a tree:
    #
    # Number of Edges = Number of Nodes - 1
    #
    # Here:
    #
    # Nodes = 7
    # Edges = 7 - 1
    #       = 6

    return Node - 1


# Call Total_Edges().

print("Total_Edges---->", Total_Edges(root))


print()


'''

# ---> FIND OUT HEIGHT ---->   To find out height always we have to start with leaf node

# def Height_Node(root):
#     if root is None:
#         return -1

#     left_side=Height_Node(root.left)
#     right_side=Height_Node(root.right)
#     if left_side > right_side:
#         return left_side + 1

#     else:
#         return right_side + 1

# print(Height_Node(root))  

# print()


''' 

# ============================================================
# FIND HEIGHT OF TREE
# ============================================================

# Height means the longest path
# from root to leaf.
#
#
#              1
#            /   \
#           2     3
#          / \   / \
#         4   5 6   7
#
#
# Longest path:
#
# 1 ---> 2 ---> 4
#
# OR
#
# 1 ---> 2 ---> 5

# OR
#
# 1 ---> 3 ---> 6
#
# OR
#
# 1 ---> 3 ---> 7
#
# Number of EDGES in the longest path = 2
#
# Therefore height = 2


def Height_Node(root):

    # If root is None,
    # there is no node.
    #
    # We return -1.
    #
    # Why -1?
    #
    # Because we are calculating height
    # based on NUMBER OF EDGES.

    if root is None:
        return -1

    
    # Find the height of the left subtree.

    left_side = Height_Node(root.left)


    # Find the height of the right subtree.

    right_side = Height_Node(root.right)


    # Compare left height and right height.
    #
    # We take the larger height.
    #
    # Then add 1 for the current node/level.

    if left_side > right_side:

        return left_side + 1
    
     else:

        return right_side + 1


# Call Height_Node().

print("Height------->", Height_Node(root))


def High_Node(root(4))   #----> root----> 4

    if root is none:     # ----> 4 is leaf node ---> It won't hold any child
        return -1        # ----> it will return -1 ----> 4 is a leaf node

    left=High_Node(root.left)  # -----> 4.left ----> -1 
    right=High_Node(root.right)  # -----> 4.right ----> -1 

    if left > right:             # ----> -1 > -1  ----> False
        retrun left + 1

    else:                        # ---> when if condition is false 
        retrun right + 1         # ---> -1 + 1 ----> (-) + (+) ----> - ----> 0



def High_Node(root(5))   #----> root----> 5

    if root is none:     # ----> 5 is leaf node ---> It won't hold any child
        return -1        # ----> it will return -1 ----> 5 is a leaf node

    left=High_Node(root.left)  # -----> 5.left ----> -1 
    right=High_Node(root.right)  # -----> 5.right ----> -1 

    if left > right:             # ----> -1 > -1  ----> False
        retrun left + 1

    else:                        # ---> when if condition is false 
        retrun right + 1         # ---> -1 + 1 ----> (-) + (+) ----> - ----> 0



def High_Node(root(6))   #----> root----> 6

    if root is none:     # ----> 6 is leaf node ---> It won't hold any child
        return -1        # ----> it will return -1 ----> 6 is a leaf node

    left=High_Node(root.left)  # -----> 6.left ----> -1 
    right=High_Node(root.right)  # -----> 6.right ----> -1 

    if left > right:             # ----> -1 > -1  ----> False
        retrun left + 1

    else:                        # ---> when if condition is false 
        retrun right + 1         # ---> -1 + 1 ----> (-) + (+) ----> - ----> 0


        

def High_Node(root(7))   #----> root----> 7

    if root is none:     # ----> 7 is leaf node ---> It won't hold any child
        return -1        # ----> it will return -1 ----> 7 is a leaf node

    left=High_Node(root.left)  # -----> 7.left ----> -1 
    right=High_Node(root.right)  # -----> 7.right ----> -1 

    if left > right:             # ----> -1 > -1  ----> False
        retrun left + 1

    else:                        # ---> when if condition is false 
        retrun right + 1         # ---> -1 + 1 ----> (-) + (+) ----> - ----> 0


        

def High_Node(root(2))   #----> root----> 2

    if root is none:     # ----> 2 is leaf node ---> It hold child ---> False
        return -1        # ----> Not return

    left=High_Node(root.left)  # -----> 4.left ----> 0 
    right=High_Node(root.right)  # -----> 4.right ----> 0

    if left > right:             # ----> 0 > 0  ----> False
        retrun left + 1

    else:                        # ---> when if condition is false 
        retrun right + 1         # ---> 0 + 1  ----> 1




'''

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

# root=Node("A")
# root.left=Node("B")
# root.left.left=Node("D")
# root.left.right=Node("E")
# root.left.right.left=Node("F")
# root.left.right.right=Node("G")
# root.left.right.right.left=Node("H")
# root.left.right.right.right=Node("I")
# root.left.right.right.right.left=Node("L")
# root.left.right.right.right.left=Node("M")
# root.right=Node("C")
# root.right.left=Node("J")
# root.right.right=Node("K")

# def Order(root):

#     if root is None:
#         return

    

# Binary---> 0 , 1, 2 ---> Child 
# Full/complete Binary ----> 0, 2 ----> CHILD ----> 1 not Use
# Perfect Binary Tree ----> Each node holding 2 childern ----> leaf node level should be equal 


''' 

DEPTH

CHECK FROM TOP TO BOTOOM 


'''   

# DETH 

# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.left=None
#         self.right=None

# root=Node(100)
# root.left=Node(200)
# root.left.left=Node(400)
# root.left.right=Node(500)
# root.left.left.left=Node(600)
# root.left.left.right=Node(700)
# root.right=Node(300)
# root.right.left=Node(800)
# root.right.right=Node(900)

# def DEPTH(root,value):              # ---> value  ----> Upto where we have to search the value in given treee
#     if root is None:
#         return -1                   # ---> their is no root value is present or it's empty return -1

#     if root.data==value:            # ---> If it's matching return 0 # ---> root element is matching with value 
#         return 0 

#     left= DEPTH(root.left, value)
#     if left!=-1:
#         return left + 1

#     right= DEPTH(root.right, value)
#     if right !=-1:
#         return right + 1
#     return -1

# print(" DEPTH ------> ", DEPTH(root,500))    # ---->   DEPTH ------>  2

# print()

''' 

def DEPTH(root,100):                       
    if root is None:
        return -1       # ---> root.data == value ----> 100 == 600 ---> false ---> stop  -----> if the root/value/given element is not present return -1 
    if root.data==value:       
        # 100 == 600 -----> false   
        # 200 == 600 ---> false    
        # 400 == 600 ---> false
        # 600 == 600 ---> True
        return 0 

    left= DEPTH(root.left, value)             # ---> Bottom to Top
    # (200, 600) = 200 == 600 ---> false      ---> retrun to previous line to check condition 
    # (400, 600) = 400 == 600 ---> false      ---> retrun to previous line to check condition 
    # (600, 600) = 600 == 600 ---> True      it will move previous part ( if root.data == value -----> return 0 ) ----> Bcoz recursion 

    if left!=-1:                
        return left + 1  

        # ---> 0 != -1 ----> True       
        # ---> left = 0 ( left + 1) = 0 + 1 = 1 ---> 600 ---> 400 
        # ---> 1 != -1 ----> True 
        # ---> left = 1 ( left + 1) = 1 + 1 = 2 ---> 600 ---> 200   ( 2 connection )
        # ---> 2 != -1 ----> True 
        # ---> left =  2( left + 1) = 2 + 1 = 3 --> 600 ---> 100   ( 3 connection )

        Stop ---> left ----> coz value not present after root ---> after 100 

        so move to right side to check the all elemnt connection 


    right= DEPTH(root.right, value)          # ---> if the previous if left != -1 ---> false ---> it will check this line 
    if right !=-1:                    
        return right + 1

    retrun -1

print(" DEPTH ------> ", DEPTH(root,600)


'''

# def Height_N(root):
#     if root is None:
#         return -1

#     left=Height_N(root.left)
#     right=Height_N(root.right)
#     if left > right:
#         return left + 1

#     else:
#         return right + 1

# print(Height_N(root))  

# print()


# -------------------------------------------------------------------------------------------------

# 1. Student Marks Management 

# A college wants to store student marks in a BST.
# The marks are:
# 75, 50, 90, 40, 60, 80, 95

# Tasks:
# Create the BST.
# Display the tree using in order traversal.
# Find the lowest mark.
# Find the highest mark.

# 75, 50, 90, 40, 60, 80, 95
#           75
#         /    \
#       50      90
#      /  \    /  \
#    40   60  80   95


x=[75, 50, 90, 40, 60, 80, 95]

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

root=Node(75)
root.left=Node(50)
root.right=Node(90)
root.left.left=Node(40)
root.left.right=Node(60)
root.right.left=Node(80)
root.right.right=Node(95)


def Insert_data(root,data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left=Insert_data(root.left, data)

    else:
        root.right=Insert_data(root.right, data)

    return root

root=None

for i in x:
    root=Insert_data(root, i )

def In_order(root):
    if root is None:
        return
    In_order(root.left)
    print(root.data, end=" ")
    In_order(root.right)

In_order(root)                #---->    40 50 60 75 80 90 95 

print()

def Small_value(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root.data


def Bigger_value(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.data

print("Lowest Marks ----> ", Small_value(root))       # -----> Lowest Marks ---->  40
print("Biggest Marks ----> ", Bigger_value(root))     # -----> Biggest Marks ---->  95


print()

# ---------------------------------------------------------------------------------------------------------------

# 2.Employee Salary System 
# A company stores employee salaries:
# 50000, 30000, 70000, 20000, 40000, 60000, 80000

# Tasks:
# Create the BST.
# Search for salary 60000.
# Search for salary 90000.
# Display salaries in ascending order.

v=[50000, 30000, 70000, 20000, 40000, 60000, 80000]

    #                  50000
    #              /          \
    #         30000           70000
    #        /     \            /     \  
    #  20000       40000      60000   80000


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(5000)
root.left=Node(30000)
root.right=Node(70000)
root.left.left=Node(20000)
root.left.right=Node(4000)
root.right.left=Node(6000)
root.right.right=Node(8000)

def Inorder(root):
    if root is None:
        return
    In_order(root.left)
    print(root.data, end=" ")
    In_order(root.right)

In_order(root)                # ------> 20000 30000 4000 5000 6000 70000 8000 

print()




# -------------------------------------------------------------------------------------------------------------------

# 3.Employee ID Search 
# A company stores employee IDs:
# 50, 30, 70, 20, 40, 60, 80
# An HR employee enters an ID.
# If the ID exists: "Employee Found"

# Otherwise: "Employee Not Found"

# Tasks: Write a BST search function.





# -----------------------------------------------------------------------------------------------------------------------


# 4.New Employee Joining 
# A company already has:
# 50, 30, 70, 20, 40
# A new employee with ID 35 joins.
# Tasks:
# Insert 35.
# Draw the updated BST.
# Display in order traversal.





# ---------------------------------------------------------------------------------------------------------------------------------


# 5.in the Below complete Binary Tree find out level of nodes and Hight and depth
#                     11
#                  /     \
#               12          13
#             /   \       /
#            14     15     16



# -------------------------------------------------------------------------------------------------------------------------------------


''' 

HOW TO DELETE THE NODE IN BST

3 ----> RULES FOR TO DELETE THE NODE

1. 0 NODE ------> leaf node ---> their is no child present 
2. NODE HAVE ONLY 1 CHILD
3. NODE HAVE 2 CHILD 

S



'''


x=[50,35,75,25,45,60,65,80]

'''
                    50
                  /    \
                35      75
              /   \     / \
             25   45   60   80
                          \
                          65
               

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(50)
root.left=Node(35)
root.right=Node(75)
root.left.left=Node(25)
root.left.right=Node(45)
root.right.left=Node(60)
root.right.right=Node(80)
root.right.left.right=Node(65)

def Inorder(root):
    if root is None:
        return

    Inorder(root.left)
    print(root.data, end=" - ")
    Inorder(root.right)

Inorder(root)                        # ----> 25 - 35 - 45 - 50 - 60 - 65 - 75 - 80 

# 25 - 35 - 45 () - 50 - 60 - 65 - 75 - 80 

# ---> delete 25 

print()

def DELETE_NODE(root,value):

    if root is None:
        return None

    # left
    if value < root.data:             # ----> 25 < 50 ----> True ----> move to left
        root.left=DELETE_NODE(root.left, value)

    # right
    elif value > root.data:
        root.right=DELETE_NODE(root.right,value)

    else:
        if root.left is None  and root.right is None:
            return None

    return root

DELETE_NODE(root, 25)

print("after deleting elemen/ value----> ")

Inorder(root)

# after deleting elemen/ value---->
# 35 - 45 - 50 - 60 - 65 - 75 - 80 -

'''
# ---> Left side
25 < 50 ----> true ----> move to left side  ----> check the Node is none ----> false
|
25 < 35 ----> true ----> Move left side ----> check the Node is none ----> false
|
25 < 25 ----> false ----> move to the right side

# ---> left side of right side 

25 > 45 ----> 


'''

print()


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(50)
root.left=Node(35)
root.right=Node(75)
root.left.left=Node(25)
root.left.right=Node(45)
root.right.left=Node(60)
root.right.right=Node(80)
root.right.left.right=Node(65)

def Inorder(root):
    if root is None:
        return

    Inorder(root.left)
    print(root.data, end=" - ")
    Inorder(root.right)

Inorder(root)                        # ----> 25 - 35 - 45 - 50 - 60 - 65 - 75 - 80 

# 25 - 35 - 45 () - 50 - 60 - 65 - 75 - 80 

# ---> delete 25 

print()

def DELETE_NODE(root,value):

    if root is None:
        return None

    # left
    if value < root.data:             # ----> 25 < 50 ----> True ----> move to left
        root.left=DELETE_NODE(root.left, value)

    # right
    elif value > root.data:
        root.right=DELETE_NODE(root.right,value)

    else:
        # Only Zero Node Delete Condition 
        if root.left is None  and root.right is None:
            return None
        
        # Only right Node Delete Condition 
        elif root.left is None:
            return root.right

        # Only left Node Delete Condition 
        elif root.right is None:
            return root.left

    return root

DELETE_NODE(root, 60)

print("after deleting element / value (60)----> ")

Inorder(root)

# after deleting element / value (60)----> 
# 25 - 35 - 45 - 50 - 65 - 75 - 80 


''' 
60
    if root is None:
        return None

    # left
    60 < 50 -------> false

    else:
        if root.left is None  and root.right is None:
            return None
    50 have child ---> this condition get becomes false  -----. move to the right side 

    # right 
    60 > 50 -------> true ----> move to right side 
    |
    right.left
    60 < 75 -------> true ----> move to left
    |
    60 < 60 -------> false 
    |
    else:
        if root.left is None  and root.right is None:
            return None

        60 ---> left side is None and 60 ---> right side is Not None
        -----> false the condition 
        -----> check elif 

        elif root.left is None:
            60.left ----> None -----> True 
            return root.right
            retrun 60.right ----> 65 

        ----> the 2nd elif condition is true ---> it won't move to the 3 rd elif condition 
        ----> It willl stop the iteration and get out of the iteration and return out side return condition 
        
        elif root.right is None:     # -----> Not execute    
            return root.left
    
    retrun root 



'''
'''
succecor ---> nearest next element ----
pre succecor ----> previous element

'''
print()


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(50)
root.left=Node(35)
root.right=Node(75)
root.left.left=Node(25)
root.left.right=Node(45)
root.right.left=Node(60)
root.right.right=Node(80)
root.right.left.right=Node(65)

def Inorder(root):
    if root is None:
        return

    Inorder(root.left)
    print(root.data, end=" - ")
    Inorder(root.right)

Inorder(root)                        # ----> 25 - 35 - 45 - 50 - 60 - 65 - 75 - 80 

# 25 - 35 - 45 () - 50 - 60 - 65 - 75 - 80 

# ---> delete 25 

print()

def DELETE_NODE(root,value):

    if root is None:
        return None

    # left
    if value < root.data:             # ----> 75 < 50 ----> True ----> move to left
        root.left=DELETE_NODE(root.left, value)

    # right
    elif value > root.data:
        root.right=DELETE_NODE(root.right,value)

    else:
        # Only Zero Node Delete Condition 
        if root.left is None  and root.right is None:
            return None
        
        # Only right Node Delete Condition 
        elif root.left is None:
            return root.right

        # Only left Node Delete Condition 
        elif root.right is None:
            return root.left

        else:
            successor=root.right      # 75.right ----> 80

            while successor.left is not None:       # 80.left ----> 
                successor=successor.left

            root.data=successor.data      # 75 = 80   
   
            root.right=DELETE_NODE(root.right, successor.data)             

    return root

DELETE_NODE(root,75)

print(" AFTER DELETING 75 --->")

Inorder(root)

# AFTER DELETING 75 --->
# 25 - 35 - 45 - 50 - 60 - 65 - 80 





print()

''' 
75 
    if root is None:
        return None

    # left
    75 < 50 -------> false

    else:
        if root.left is None  and root.right is None:
            return None
    50 have child ---> this condition get becomes false  -----. move to the right side 

    # right 
    75 > 50 -------> true ----> move to right side 
    |
    right.left
    75 < 75 -------> false ----> 
    |
    |
    else:
        if root.left is None  and root.right is None:
            return None

        
def DELETE_NODE(root, value):

    # Check whether the current node is empty
    if root is None:
        return None

    # ------------------------------------------------
    # CASE: VALUE IS SMALLER
    # Move to LEFT subtree
    # ------------------------------------------------
    if value < root.data:

        # Recursively search/delete from left subtree
        root.left = DELETE_NODE(root.left, value)

    # ------------------------------------------------
    # CASE: VALUE IS GREATER
    # Move to RIGHT subtree
    # ------------------------------------------------
    elif value > root.data:

        # Recursively search/delete from right subtree
        root.right = DELETE_NODE(root.right, value)

    # ------------------------------------------------
    # CASE: VALUE == ROOT.DATA
    # Node is FOUND
    # ------------------------------------------------
    else:

        # ==============================================
        # CASE 1: ZERO CHILDREN
        # ==============================================
        if root.left is None and root.right is None:

            # Delete this node
            return None

        # ==============================================
        # CASE 2: ONLY RIGHT CHILD
        # ==============================================
        elif root.left is None:

            # Replace current node with right child
            return root.right

        # ==============================================
        # CASE 3: ONLY LEFT CHILD
        # ==============================================
        elif root.right is None:

            # Replace current node with left child
            return root.left

        # ==============================================
        # CASE 4: TWO CHILDREN
        # ==============================================
        else:

            # Start from right child
            temp = root.right

            # Move LEFT until smallest node is found
            while temp.left is not None:
                temp = temp.left

            # Copy smallest value into current node
            root.data = temp.data

            # Delete the original duplicate node
            root.right = DELETE_NODE(root.right, temp.data)

    # Return the updated tree/subtree
    return root


'''


