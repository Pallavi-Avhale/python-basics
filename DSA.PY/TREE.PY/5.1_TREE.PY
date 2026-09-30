''' 
TREE

IT IS A NON-LINEAR DATA STUCTURE , IT WILL BE WORK ON HIERARCHIAL RELATIONSHIP
THEIR IS NO INTER-RELATION BETWEEN 2 CHILD  (B -- C) LIKE 

           A
         /   \
         B -- C

-----------------------------------------------------------------------------------
1. BINARY TREE
2. GENERAL TREE

------------------------------------------------------------------------------------

NODE---> WHATEVER THE ELEMENTS WE ARE PASSING IN THE TREE CALLED IT AS NODE

-----------------------------------------------------------------------------------

1. BINARY TREE
---> BINARY MEANS AT MOST 2 CHILD / 1 CHILD / 0 CHILD

---> COMPLETE BINARY 
---> FULL BINARY
---> PERFECT BINARY
---> BINARY SEARCH TREE----> PRE- OREDR ----> root---> check left then right
                       ----> POST- ORDER ---> left---> right---> root
                       ----> IN ORDER-------> Left---> Root ---> Right


BINARY SERACH TREE 
                    B S T
                     /  \ 
            SMALLER NUM  BIGGER NUM

----> ROOT.LEFT = SMALLER NUMBER 
----> ROOT.RIGHT= BIGGER NUMBER
----> IN-ORDER= ALWAYS O/P SHOULD BE IN SORTED MANNER (ASCENDING ---> DESCENDING) ---> LEFT---> ROOT---> RIGHT

-----------------------------------------------------------------------------------

2. GENERAL TREE
---> EACH NODE HOLDING N NUMBER OF CHILDES 

--------------------------------------------------------------------------------

1. WHAT IS A TREE?

A Tree is a non-linear data structure.

Meaning of Non-Linear

In a linear data structure, data is arranged one after another.

LINEAR DATA STRUCTURE

10 → 20 → 30 → 40 → 50

But in a Tree, data is arranged in a hierarchical structure.

                A
              /   \
             B     C
            / \     \
           D   E     F

Here:

A
├── B
│   ├── D
│   └── E
└── C
    └── F

So, a Tree is mainly used when data has a parent-child relationship.

Real-Life Examples
                 COMPANY
                    |
          ---------------------
          |                   |
       MANAGER             MANAGER
       /     \              /    \
   Employee Employee     Employee Employee

Other examples:

Company organization
File and folder system
Family hierarchy
HTML/XML document structure
Database indexing
Decision-making systems
2. BASIC TREE STRUCTURE

Example:

                    A
                  /   \
                 B     C
                / \   / \
               D   E F   G

Here:

A → Root
B, C → Children of A
D, E → Children of B
F, G → Children of C
B, C → Siblings
D, E, F, G → Leaf Nodes
3. NODE

Whatever element/data we store inside a Tree is called a Node.

Example:

       10
      /  \
     20   30

Here:

10 → Node
20 → Node
30 → Node

Each node generally contains:

+----------------+
|      DATA      |
+----------------+
|  LINK/CHILDREN |
+----------------+

Depending on the type of Tree, a node can contain links to one or more child nodes.

Pre-order----> Normal Function Display

In the place of root we can use any word/ letter it will be work

----------------------------------------------------------------------------------------------------

4. ROOT NODE 🌱

The topmost node of a Tree is called the Root Node.

Example:

             A
           /   \
          B     C

Here:

A = ROOT
Important Point

A Tree normally has only one root node.

             A
           /   \
          B     C

A is the starting point of the Tree.

5. PARENT NODE 👨

A node that has one or more children is called a Parent Node.

Example:

             A
           /   \
          B     C

Here:

A = Parent of B and C
6. CHILD NODE 👶

A node directly connected below another node is called its Child.

             A
           /   \
          B     C

Here:

B = Child of A
C = Child of A
7. SIBLING NODES

Nodes having the same parent are called Siblings.

Example:

             A
           / | \
          B  C  D

Here:

B, C, D = Siblings

Because all three have the same parent:

Parent = A
8. LEAF NODE 🍃

A node that does not have any child is called a Leaf Node.

Example:

             A
           /   \
          B     C
         / \
        D   E

Leaf Nodes:

C
D
E

Because they don't have any children.

C → No child
D → No child
E → No child
Other Names

Leaf Node is also called:

Terminal Node
External Node
9. INTERNAL NODE

A node that has at least one child is called an Internal Node.

Example:

             A
           /   \
          B     C
         / \
        D   E

Internal Nodes:

A
B

Because:

A → has children B, C
B → has children D, E
10. EDGE

The connection between two nodes is called an Edge.

Example:

             A
            / \
           B   C

The connections are:

A ── B    → Edge
A ── C    → Edge

So there are 2 edges.

Important Formula

For a Tree containing N nodes:

Number of Edges = N - 1

Example:

        A
       / \
      B   C
     /
    D

Nodes = 4

Therefore:

Edges = 4 - 1
      = 3
11. PATH

A sequence of connected nodes is called a Path.

Example:

             A
           /   \
          B     C
         /
        D

Path from A to D:

A → B → D

Path from A to C:

A → C
12. DEPTH

Depth represents how far a node is from the Root.

Consider:

                 A
                / \
               B   C
              / \
             D   E
            /
           F

Using Root depth = 0:

A → Depth 0
B → Depth 1
C → Depth 1
D → Depth 2
E → Depth 2
F → Depth 3

Diagram:

                 A          ← Depth 0
                / \
               B   C        ← Depth 1
              / \
             D   E          ← Depth 2
            /
           F               ← Depth 3
13. LEVEL

Nodes at the same distance from the root are generally considered to be at the same Level.

Example:

                 A          ← Level 0
                / \
               B   C        ← Level 1
              / \   \
             D   E   F      ← Level 2

So:

Level 0 → A
Level 1 → B, C
Level 2 → D, E, F

Note: Some books start Tree levels from 1 instead of 0. Always check the convention being used.

14. HEIGHT OF A TREE

The height of a Tree is the maximum number of edges from the root to a leaf.

Example:

                 A
                / \
               B   C
              /
             D
            /
           E

Longest path:

A → B → D → E

Number of edges:

A → B     = 1
B → D     = 1
D → E     = 1

Total = 3

Therefore:

Height of Tree = 3
15. DEGREE OF A NODE

The degree of a node means the number of children that node has.

Example:

                 A
              /  |  \
             B   C   D
                / \
               E   F

Degree:

A → 3 children → Degree 3

B → 0 children → Degree 0

C → 2 children → Degree 2

D → 0 children → Degree 0

E → 0 children → Degree 0

F → 0 children → Degree 0
16. DEGREE OF TREE

The degree of a Tree is the maximum degree of any node in that Tree.

Example:

                 A
              /  |  \
             B   C   D
                / \
               E   F

Degrees:

A = 3
B = 0
C = 2
D = 0
E = 0
F = 0

Maximum degree = 3

Therefore:

Degree of Tree = 3
17. TYPES OF TREES

The two basic categories are:

                    TREE
                     |
          -----------------------
          |                     |
      BINARY TREE          GENERAL TREE
18. BINARY TREE 🌳

A Binary Tree is a Tree in which each node can have at most 2 children.

                A
              /   \
             B     C
            / \
           D   E

Each node can have:

0 children
OR
1 child
OR
2 children
Binary Means
BI = TWO

Therefore:

Binary Tree → Maximum 2 children per node
Possible Cases
Case 1 — Zero Children
        A

A has:

0 children
Case 2 — One Child
        A
       /
      B

A has:

1 child
Case 3 — Two Children
        A
       / \
      B   C

A has:

2 children
Important

Binary Tree does NOT mean every node must have exactly 2 children.

It means:

Maximum = 2 children

So these are all valid:

       A             A             A
      /             / \           
     B             B   C

   1 child        2 children      0 children
19. LEFT CHILD AND RIGHT CHILD

In a Binary Tree, the two possible child positions are:

                 A
               /   \
        LEFT CHILD   RIGHT CHILD
             B           C

So:

B = Left Child
C = Right Child

This left/right distinction is very important in Binary Trees.

20. GENERAL TREE 🌳

A General Tree is a Tree where a node can have any number of children.

Example:

                    A
              /     |     \
             B      C      D
           / | \          / \
          E  F  G        H   I

Here:

A → 3 children
B → 3 children
C → 0 children
D → 2 children

There is no fixed maximum like Binary Tree.

Therefore:

General Tree
→ 0 children
→ 1 child
→ 2 children
→ 3 children
→ 4 children
→ ...
→ N children
21. BINARY TREE vs GENERAL TREE
Feature	Binary Tree	General Tree
Maximum children	2	N
Child positions	Left and Right	Any number
Children can be 0?	Yes	Yes
Children can be 1?	Yes	Yes
Children can be 2?	Yes	Yes
Children can be 3?	❌ No	✅ Yes
Children can be 4?	❌ No	✅ Yes
Simple Memory Trick
BINARY TREE
     ↓
Maximum 2 Children

GENERAL TREE
     ↓
Any Number of Children
22. IMPORTANT TREE DIAGRAM

Consider this Tree:

                         A
                      /     \
                     B       C
                   /   \      \
                  D     E      F
                       / \
                      G   H
Identify:
Root
  ↓
A
Children of A
  ↓
B, C
Parent of D
  ↓
B
Siblings
  ↓
B and C
D and E
G and H
Leaf Nodes
  ↓
D, G, H, F
Internal Nodes
  ↓
A, B, E, C
23. TREE REPRESENTATION

A Tree can be represented using:

Method 1 — Linked Representation

Each node stores:

DATA + LINK(S)

Example Binary Tree:

class Node:

    data
    left
    right

Diagram:

             [ A ]
            /     \
         [ B ]   [ C ]

Conceptually:

A
|
+---- left  → B
|
+---- right → C
24. SIMPLE BINARY TREE NODE

In Python:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

Meaning:

self.data
    ↓
Stores the value

self.left
    ↓
Stores/reference the left child

self.right
    ↓
Stores/reference the right child

Example:

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.left = n2
n1.right = n3

Diagram:

              10
             /  \
            20   30
25. TREE vs LINEAR DATA STRUCTURE
Linear
10 → 20 → 30 → 40 → 50

Data follows a single sequence.

Tree
                10
              /    \
            20      30
           / \       \
          40  50      60

Data branches into different directions.

Therefore:

LINEAR
   ↓
Sequential arrangement

TREE
   ↓
Hierarchical arrangement
26. IMPORTANT TREE TERMINOLOGY
ROOT
 ↓
Topmost node

PARENT
 ↓
Node having child/children

CHILD
 ↓
Node below a parent

SIBLING
 ↓
Nodes having same parent

LEAF
 ↓
Node having no children

INTERNAL NODE
 ↓
Node having at least one child

EDGE
 ↓
Connection between two nodes

PATH
 ↓
Sequence of connected nodes

DEPTH
 ↓
Distance from root

LEVEL
 ↓
Position/layer in Tree

HEIGHT
 ↓
Longest path from root to leaf

DEGREE OF NODE
 ↓
Number of children of that node
27. REAL-LIFE EXAMPLE — FOLDER STRUCTURE

Computer folders are a very good example of a Tree.

                    C:
                    |
          ---------------------
          |         |         |
       Program     Users    Windows
          |          |
       Python      Student
                     |
              ----------------
              |              |
            Notes           Photos

Here:

C: → Root
Users → Child of C:
Student → Child of Users
Notes → Child of Student
Photos → Child of Student

This is hierarchical data.

28. TREE TRAVERSAL

Traversal means visiting the nodes of a Tree.

Common Binary Tree traversals:

1. PREORDER
2. INORDER
3. POSTORDER
4. LEVEL ORDER

Example:

             A
            / \
           B   C
          / \
         D   E
Preorder
Root → Left → Right

Result:

A → B → D → E → C
Inorder
Left → Root → Right

Result:

D → B → E → A → C
Postorder
Left → Right → Root

Result:

D → E → B → C → A
Level Order

Visit level by level:

A → B → C → D → E
29. QUICK REVISION
TREE
 ↓
Non-Linear Data Structure
 ↓
Hierarchical Data
 ↓
Contains Nodes
 ↓
Top Node = Root
 ↓
Node above = Parent
 ↓
Node below = Child
 ↓
Same Parent = Siblings
 ↓
No Child = Leaf
 ↓
Connection = Edge

---> Main Types
                    TREE
                     |
             -----------------
             |               |
       BINARY TREE       GENERAL TREE
             |               |
       Max 2 children     N children
       per node           per node
---> Binary Tree
                 A
               /   \
              B     C
             / \
            D   E

---> Maximum children:

---> 2
---> General Tree
                 A
             /   |   |   \
            B    C   D    E

---> Maximum children:

---> No fixed limit
⭐ MOST IMPORTANT EXAM POINTS
---> Tree is a non-linear data structure.
---> Tree represents hierarchical data.
---> The topmost node is called the Root.
---> A node can have zero, one, or multiple children depending on the type of Tree.
---> Binary Tree allows at most 2 children per node.
---> Binary Tree children are called Left Child and Right Child.
---> General Tree can have any number of children.
---> A node with no children is called a Leaf Node.
---> Nodes having the same parent are called Siblings.
---> The connection between two nodes is called an Edge.
---> For a Tree with N nodes, the number of edges is N − 1.
---> The number of children of a node is called its Degree.
---> The maximum degree among all nodes is the Degree of the Tree.
---> Height represents the longest downward path from the root to a leaf, measured in edges under the common convention.
---> Tree Traversal means visiting the nodes of a Tree.
---> Common Binary Tree traversals are:
---> Preorder
---> Inorder
---> Postorder
---> Level Order
---> 🧠 EASY MEMORY TRICK
                 TREE
                  |
            HIERARCHY
                  |
                ROOT
                  |
             PARENT
                  |
               CHILD
              /     \
          SIBLING   SIBLING
                  |
             NO CHILD
                  ↓
                LEAF

And remember:

BINARY TREE
     ↓
MAXIMUM 2 CHILDREN

GENERAL TREE
     ↓
ANY NUMBER OF CHILDREN

'''

# ------------------------------------------------------------------------------------------------------------

#--> BY default it will take it as a pre-order ---> 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.left.right=Node("E")
root.right.left=Node("F")
root.right.right=Node("G")

def Display(root):
    if root is None:
        return
    print(root.data,end=" ")

    Display(root.left)
    Display(root.right)

Display(root)                 #----> A B D E C F G 

print()

# --------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.left.left.left=Node(60)
root.left.left.right=Node(70)
root.left.right.left=Node(80)
root.left.right.right=Node(90)
root.right.left=Node(100)
root.right.right=Node(110)
root.right.left.left=Node(200)
root.right.left.right=Node(300)
root.right.right.left=Node(400)
root.right.right.right=Node(500)

def Display(root):
    if root is None:
        return
    print(root.data,end=" ")

    Display(root.left)
    Display(root.right)

Display(root)            #---> 10 20 40 60 70 50 80 90 30 100 200 300 110 400 500 

print()

# ------------------------------------------------------------------------------------------------


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node("X")
root.left=Node("Y")
root.left.left=Node("P")
root.left.right=Node("Q")
root.right=Node("Z")

def Display_PRE_ORDER(root):
    if root is None:
        return
    print(root.data,end=" ")

    Display_PRE_ORDER(root.left)
    Display_PRE_ORDER(root.right)

Display_PRE_ORDER(root)                     #-----> X Y P Q Z   

print() 

# -------------------------------------------------------------------------------------------

# POST- ORDER

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node("X")
root.left=Node("Y")
root.left.left=Node("P")
root.left.right=Node("Q")
root.right=Node("Z")

def Display_POSTORDER(root):
    if root is None:
        return
    
    Display_POSTORDER(root.left)
    Display_POSTORDER(root.right)
    print(root.data,end=" ")

Display_POSTORDER(root)                        #---> P Q Y Z X 

print()

# ----------------------------------------------------------------------------------------------------


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.left.left.left=Node(60)
root.left.left.right=Node(70)
root.left.right.left=Node(80)
root.left.right.right=Node(90)
root.right.left=Node(100)
root.right.right=Node(110)
root.right.left.left=Node(200)
root.right.left.right=Node(300)
root.right.right.left=Node(400)
root.right.right.right=Node(500)

def Display(root):
    if root is None:
        return

    Display(root.left)
    Display(root.right)
    print(root.data,end=" ")

Display(root)                   #---> 60 70 40 80 90 50 20 200 300 100 400 500 110 30 10 

print()

# --------------------------------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.left.right=Node("E")
root.right.left=Node("F")
root.right.right=Node("G")

def Display(root):
    if root is None:
        return

    Display(root.left)
    Display(root.right)
    print(root.data,end=" ")

Display(root)                 #----> D E B F G C A 

print()

# ---------------------------------------------------------------------------------------------
''' 
pre-order------>
    print(root.data,end=" ")
    Display_PRE_ORDER(root.left)
    Display_PRE_ORDER(root.right)

post- order----->
    Display_POSTORDER(root.left)
    Display_POSTORDER(root.right)
    print(root.data,end=" ")

In- order------>
    Display_INORDER(root.left)
    print(root.data,end=" ")
    Display_INORDER(root.right)

    
count
def Display(root):
    if root is None:
        return 0
    return 1 + root.left + root.right      #-----> return 1----> means----> root + root.left + root.right
    
leaf node:
def Display(root):
    if root.left is None and root.right is None


'''


# IN-ORDER 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node("A")
root.left=Node("B")
root.left.left=Node("D")
root.left.right=Node("E")
root.right=Node("C")


def Show(root):
    if root is None:
        return

    Show(root.left)
    print(root.data, end=" ")
    Show(root.right)

Show(root)                            #D B E A C 

print()

# ----------------------------------------------------------------------------------

# IN-ORDER 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(8)
root.left.right.left.left=Node(12)
root.left.right.left.right=Node(13)
root.left.right.right=Node(9)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(10)
root.right.right.right=Node(11)

def Show(root):
    if root is None:
        return

    Show(root.left)
    print(root.data, end=" ")
    Show(root.right)

Show(root)                     #-----> 4 2 12 8 13 5 9 1 6 3 10 7 11  ----> left---> root ---> right

print()

# ----------------------------------------------------------------------------------------------------------

# PRE-ORDER 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(8)
root.left.right.left.left=Node(12)
root.left.right.left.right=Node(13)
root.left.right.right=Node(9)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(10)
root.right.right.right=Node(11)

def Show(root):
    if root is None:
        return
    
    print(root.data, end=" ")
    Show(root.left)
    Show(root.right)

Show(root)                       #-----> 1 2 4 5 8 12 13 9 3 6 7 10 11  ----> root---> left ---> right

print()

# ----------------------------------------------------------------------------------------------------------

# POST-ORDER 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(8)
root.left.right.left.left=Node(12)
root.left.right.left.right=Node(13)
root.left.right.right=Node(9)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(10)
root.right.right.right=Node(11)

def Show(root):
    if root is None:
        return
    
    Show(root.left)
    Show(root.right)
    print(root.data, end=" ")

Show(root)                           #--> 4 12 13 8 9 5 2 6 10 11 7 3 1 ---> left---> right---> root

print()

# -------------------------------------------------------------------------------------------------------------------

# COUNT---------->

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(8)
root.left.right.left.left=Node(12)
root.left.right.left.right=Node(13)
root.left.right.right=Node(9)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(10)
root.right.right.right=Node(11)

def Show(root):
    if root is None:
        return 0

    return 1 + Show(root.left) + Show(root.right)
    


print("Total_Element_Count--->", Show(root))                           #--> Total_Element_Count---> 13

print()

# ----------------------------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node("A")
root.left=Node("B")
root.left.left=Node("D")
root.left.right=Node("E")
root.right=Node("C")


def Show(root):
    if root is None:
        return 0

    return 1 + Show(root.left) + Show(root.right)

print("Total Count----> ",Show(root))                            # -----> Total Count---->  5

print()

# ----------------------------------------------------------------------------------------------------------------

# PRE-ORDER ----->

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
Root=Node("@")
Root.left=Node("#")
Root.left.left=Node(11)
Root.left.left.left=Node(7)
Root.left.left.left.left=Node(100)
Root.left.left.left.right=Node(200)
Root.left.left.left.right.left=Node("$")
Root.left.left.left.right.right=Node("*")
Root.right=Node("+")
Root.right.left=Node(5)
Root.right.right=Node(6)
Root.right.right.left=Node(15)
Root.right.right.right=Node(17)
Root.right.right.right.left=Node(20)
Root.right.right.right.right=Node(22)
Root.right.right.right.right.left=Node(50)
Root.right.right.right.right.right=Node(51)
Root.right.right.right.right.right.right=Node(200)

def Display(Root):
    if Root is None:
        return

    print(Root.data, end=" ")
    Display(Root.left)
    Display(Root.right)

Display(Root)                              #-------> @ # 11 7 100 200 $ * + 5 6 15 17 20 22 50 51 200 ---> ROOT---> LEFT----> RIGHT

print()

# ----------------------------------------------------------------------------------------------------------------

# POST-ORDER ----->

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
Root=Node("@")
Root.left=Node("#")
Root.left.left=Node(11)
Root.left.left.left=Node(7)
Root.left.left.left.left=Node(100)
Root.left.left.left.right=Node(200)
Root.left.left.left.right.left=Node("$")
Root.left.left.left.right.right=Node("*")
Root.right=Node("+")
Root.right.left=Node(5)
Root.right.right=Node(6)
Root.right.right.left=Node(15)
Root.right.right.right=Node(17)
Root.right.right.right.left=Node(20)
Root.right.right.right.right=Node(22)
Root.right.right.right.right.left=Node(50)
Root.right.right.right.right.right=Node(51)
Root.right.right.right.right.right.right=Node(200)

def Display(Root):
    if Root is None:
        return

    
    Display(Root.left)
    Display(Root.right)
    print(Root.data, end=" ")

Display(Root)                              #-------> 100 $ * 200 7 11 # 5 15 20 50 200 51 22 17 6 + @   ---> LEFT ---> RIGHT---> ROOT

print()

# ----------------------------------------------------------------------------------------------------------------

# IN-ORDER ----->

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
Root=Node("@")
Root.left=Node("#")
Root.left.left=Node(11)
Root.left.left.left=Node(7)
Root.left.left.left.left=Node(100)
Root.left.left.left.right=Node(200)
Root.left.left.left.right.left=Node("$")
Root.left.left.left.right.right=Node("*")
Root.right=Node("+")
Root.right.left=Node(5)
Root.right.right=Node(6)
Root.right.right.left=Node(15)
Root.right.right.right=Node(17)
Root.right.right.right.left=Node(20)
Root.right.right.right.right=Node(22)
Root.right.right.right.right.left=Node(50)
Root.right.right.right.right.right=Node(51)
Root.right.right.right.right.right.right=Node(200)

def Display(Root):
    if Root is None:
        return

    
    Display(Root.left)
    print(Root.data, end=" ")
    Display(Root.right)
    

Display(Root)                              #-------> 100 7 $ 200 * 11 # @ 5 + 15 6 20 17 50 22 51 200   ---> LEFT ---> ROOT ---> RIGHT

print()

# ----------------------------------------------------------------------------------------------------------------

# IN-ORDER ----->

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
Root=Node("@")
Root.left=Node("#")
Root.left.left=Node(11)
Root.left.left.left=Node(7)
Root.left.left.left.left=Node(100)
Root.left.left.left.right=Node(200)
Root.left.left.left.right.left=Node("$")
Root.left.left.left.right.right=Node("*")
Root.right=Node("+")
Root.right.left=Node(5)
Root.right.right=Node(6)
Root.right.right.left=Node(15)
Root.right.right.right=Node(17)
Root.right.right.right.left=Node(20)
Root.right.right.right.right=Node(22)
Root.right.right.right.right.left=Node(50)
Root.right.right.right.right.right=Node(51)
Root.right.right.right.right.right.right=Node(200)

def Display(Root):
    if Root is None:
        return 0

    return 1 + Display(Root.left) + Display(Root.right)
    

print("Total_Elements--->",Display(Root))                              #-------> Total_Elements---> 18


print()

# -----------------------------------------------------------------------------------------------------------

# Total_Element _Count 



class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
Root=Node("@")
Root.left=Node("#")
Root.left.left=Node(11)
Root.left.left.left=Node(7)
Root.left.left.left.left=Node(100)
Root.left.left.left.right=Node(200)
Root.left.left.left.right.left=Node("$")
Root.left.left.left.right.right=Node("*")
Root.right=Node("+")
Root.right.left=Node(5)
Root.right.right=Node(6)
Root.right.right.left=Node(15)
Root.right.right.right=Node(17)
Root.right.right.right.left=Node(20)
Root.right.right.right.right=Node(22)
Root.right.right.right.right.left=Node(50)
Root.right.right.right.right.right=Node(51)
Root.right.right.right.right.right.right=Node(200)

def Display(Root):
    if Root is None:
        return 0

    return 1 + (Display(Root.left)) + (Display(Root.right))
    

print("Total_Elements--->",Display(Root))                              #-------> Total_Elements---> 18


print()

# -------------------------------------------------------------------------------------------

# EVEN_ELEMENTS------> PRE

# PRE-ORDER ----->

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
Root=Node("@")
Root.left=Node("#")
Root.left.left=Node(11)
Root.left.left.left=Node(7)
Root.left.left.left.left=Node(100)
Root.left.left.left.right=Node(200)
Root.left.left.left.right.left=Node("$")
Root.left.left.left.right.right=Node("*")
Root.right=Node("+")
Root.right.left=Node(5)
Root.right.right=Node(6)
Root.right.right.left=Node(15)
Root.right.right.right=Node(17)
Root.right.right.right.left=Node(20)
Root.right.right.right.right=Node(22)
Root.right.right.right.right.left=Node(50)
Root.right.right.right.right.right=Node(51)
Root.right.right.right.right.right.right=Node(200)

def Even_Node(Root):
    if Root is None:
        return

   
    if isinstance(Root.data, int) and Root.data%2 ==0:
        print(Root.data, end=" ")
        

    Even_Node(Root.left)
    Even_Node(Root.right)

Even_Node(Root)                 #---> 100 200 6 20 22 50 200 

print()
# ----------------------------------------------------------------------------------------

# leaf _ Node

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

Root=Node("@")
Root.left=Node("#")
Root.left.left=Node(11)
Root.left.left.left=Node(7)
Root.left.left.left.left=Node(100)
Root.left.left.left.right=Node(200)
Root.left.left.left.right.left=Node("$")
Root.left.left.left.right.right=Node("*")
Root.right=Node("+")
Root.right.left=Node(5)
Root.right.right=Node(6)
Root.right.right.left=Node(15)
Root.right.right.right=Node(17)
Root.right.right.right.left=Node(20)
Root.right.right.right.right=Node(22)
Root.right.right.right.right.left=Node(50)
Root.right.right.right.right.right=Node(51)
Root.right.right.right.right.right.right=Node(200)

def leaf_N(Root):
    if Root is None:
        return 0

    if Root.left is None and Root.right is None:
        return 1

    return leaf_N(Root.left) + leaf_N(Root.right)


print("LEAF_NODE_COUNT---->", leaf_N(Root))           #----> LEAF_NODE_COUNT----> 8                     
print() 
 
# -------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)

print("--------> pre_order Traversal----> root---->left----> right")

def Pre_order(root):
    if root is None:
        return

    print(root.data, end=" ")
    Pre_order(root.left)
    Pre_order(root.right)

Pre_order(root)         #-----> 1 2 4 5 3 6 7 

'''
print()
print("------------> post_order-----> left---> right----> root")

def Post_order(root):
    if root is None:
        return

    Post_order(root.left)
    Post_order(root.right)
    print(root.data, end=" ")

Post_order(root)             #-----> 4 5 2 6 7 3 1 

print()
print("------------> In_order-----> left---> root----> right")

def IN_order(root):
    if root is None:
        return

    IN_order(root.left)
    print(root.data, end=" ")
    IN_order(root.right)
    

IN_order(root)     #---> 4 2 5 1 6 3 7 

print()

print(" Total Node------> Data")

def TotalNodeSum(root):
    if root is None:
        return 0

    return root.data + TotalNodeSum(root.left) + TotalNodeSum(root.right)        #----> root.data---> To start from beginning. 

print("TOTAL_NODES_SUM---->", TotalNodeSum(root))    #----> TOTAL_NODES_SUM----> 28


print()

print("-----> Even Number------> ")

def Only_Even_Nodes(root):
    if root is None:
        return 

    if root.data %2==0:
        print(root.data, end=" ")

    Only_Even_Nodes(root.left)
    Only_Even_Nodes(root.right)

Only_Even_Nodes(root)            #-----> Even Number------>2 4 6 

print()

print("-----> ODD Number------> ")

def Only_ODD_Nodes(root):
    if root is None:
        return 

    if root.data %2!=0:
        print(root.data, end=" ")

    Only_ODD_Nodes(root.left)
    Only_ODD_Nodes(root.right)

Only_ODD_Nodes(root)            #-----> ODD Number------> 1 5 3 7 

print()

print("-----> Even Number COUNT------> ")

def Only_Even_Nodes_Count(root):
    if root is None:
        return 0
    Count=0

    if root.data %2==0:
        Count=1

    return Count+Only_Even_Nodes_Count(root.left) + Only_Even_Nodes_Count(root.right)

print(Only_Even_Nodes_Count(root))            
print()

print("-----> ODD Number Count------> ")

def Only_ODD_Nodes_Count(root):
    if root is None:
        return 0
    Count=0

    if root.data %2!=0:
        Count=1

    return Count+Only_ODD_Nodes_Count(root.left)+Only_ODD_Nodes_Count(root.right)

print(Only_ODD_Nodes_Count(root))            

print()

print("-------> ONLY_LEFT_SIDE_EVEN-----> ")
def Only_leftside_even(root):
    if root is None:
        return 

    if root.data %2 ==0:
        print( root.data, end=" ")
    Only_leftside_even(root.left)
    Only_leftside_even(root.right)

Only_leftside_even(root.left)            #-------> ONLY_LEFT_SIDE_EVEN----->  2 4 

print()

print("-------> ONLY_RIGHT_SIDE_ODD-----> ")

def Only_rightside_Odd(root):
    if root is None:
        return 

    if root.data %2 !=0:
        print( root.data, end=" ")
    Only_rightside_Odd(root.left)
    Only_rightside_Odd(root.right)

Only_rightside_Odd(root.right)             #-------> ONLY_RIGHT_SIDE_ODD----->3 7 

print()

print("-------> ONLY_LEFT_SIDE_EVEN-----> ")
def Only_leftside_even(root):
    if root is None:
        return 0

    count=0

    if root.data %2 ==0:
        count=1

    return count + Only_leftside_even(root.left)

print(Only_leftside_even(root.left))            #-------> ONLY_LEFT_SIDE_EVEN----->  2 4 

print()

print()

print("-------> ONLY_RIGHT_SIDE_COUNT-----> ")
def Only_rightside_odd_Count(root):
    if root is None:
        return 0

    count=0

    if root.data %2 !=0:
        count=1

    return count + Only_rightside_odd_Count(root.right)

print(Only_rightside_odd_Count(root.right))            #-------> ONLY_LEFT_SIDE_EVEN----->  2 4 

print()


def Only_rightside_even(root):
    if root is None:
        return 

    if root.data %2 ==0:
        print( root.data, end=" ")

    Only_rightside_even(root.left)
    Only_rightside_even(root.right)


Only_rightside_even(root.right)            #-------> ONLY_right_SIDE_EVEN----->  6

print()



def Only_leftside_even(root):
    if root is None:
        return 

    if root.data %2 ==0:
        print( root.data, end=" ")

    Only_leftside_even(root.left)
    Only_leftside_even(root.right)


Only_leftside_even(root.left)            #-------> ONLY_LEFT_SIDE_EVEN----->  2 4 

print()
''' 
print()

# total leaf node:

def Total_Leaf_Node(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return Total_Leaf_Node(root.left) + Total_Leaf_Node(root.right)

print("---> TOTAL_LEAF_NODE--->", Total_Leaf_Node(root))        #--> ---> TOTAL_LEAF_NODE---> 4

print()

# TOTAL_NON_LEAF_NODE

def Total_Non_Leaf_Node(root):
    if root is None:
        return 0

    if root.left is None and root.right is  None:
        return 0

    return (1+Total_Non_Leaf_Node(root.left) + Total_Non_Leaf_Node(root.right))

print("--->Total_Non_Leaf_Node--->", Total_Non_Leaf_Node(root))        #--->Total_Non_Leaf_Node---> 3


print()

def Total_Sum_even(root):
    if root is None:
        return 0
    total=0
    if root.data %2 ==0:
        total+=root.data
    return (total + Total_Sum_even(root.left) +Total_Sum_even(root.right))


print(" ---->TOTAL_SUM_EVEN---->",Total_Sum_even(root))         # ---->TOTAL_SUM_EVEN----> 12         

print()


# TOTAL _SUM_ODD 
def Total_Sum_odd(root):
    if root is None:
        return 0
    total=0
    if root.data %2 !=0:
        total+=root.data

    return (total + Total_Sum_odd(root.left) +Total_Sum_odd(root.right))


print(" ---->TOTAL_SUM_ODD---->",Total_Sum_odd(root))              # ---->TOTAL_SUM_ODD----> 16  
print()