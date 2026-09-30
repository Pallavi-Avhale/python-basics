''' 
GRAPH

-------------------------------------------------------------------

---> GRAPH IS A LINER DATA STRUCTURE 

---> THE GRAPH SHOWS VERTECIS (VERTIX) AND EDGES 
---> IT WILL WORK ON THE V & E CONNECTION
---> NOTE -> TREE IS THE PART OF THE GRAPH
---> TE SHOW ADJANCEY ----> BETWEEN TO 2 NODE (A-B, A-C, B-C)

                   A
                 /   \ 
                B --- C


----------------------------------------------------------------------------------------------------------------------------

Formula/notation:

G=(V,E)

where V = set of vertices and E = set of edges.

-----------------------------------------------------------------------------------------------------------------------------
----> A graph contains:

----> Vertices (V) → Nodes/points
----> Edges (E) → Connections between vertices

----> The mathematical representation is:

G=(V,E)

----> Where:

----> V = Set of vertices
----> E = Set of edges
------------------------------------------------------------------------------------------------------------------------------------

Here:

Vertices = {A, B, C}
Edges = {A-B, A-C, B-C}

----------------------------------------------------------------------------------------------------------------------------------

TYPES OF GRAPHS 

1. DIRECT GRAPH  -------------> THE GRAPH MOVE ONLY IN FORWARD DIRECTION THEIR IS NO BACKWORD DIRECTION 
2. UNDIRECT GRAPH -------------> THE GRAPH MOVE IN FORWARD DIRECTION AS WELL AS BACKWORD DIRECTION 
3. WEIGHTED GRAPH   ---------> IN BTWEEN 2 NODES THE VALUES IS PRESENT 
4. UNWEIGHTED GRAPH   ---------> IN BTWEEN 2 NODES DON'T HVAE ANY VALUES IS PRESENT 
5. CYCLIC GRAPH       ----------> THE GRAPH FORMING THE CYCLE BETWEEN VERTEX (CONTINUOS CONNECTION IS PRESENT ) 
6. ACYCLIC GRAPH      ----------> THE GRAPH NOT FORMING THE CYCLE BETWEEN VERTEX (CONTINUOS CONNECTION IS PRESENT ) 


------------------------------------------------------------------------------------------------------------------------------------

TYPES OF GRAPHS

1. DIRECTED GRAPH

→ The graph moves only in the specified direction. There is no backward direction unless a separate edge is given.

A ─────→ B

A → B means we can move from A to B.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


2. UNDIRECTED GRAPH

→ The graph can move in both directions: forward as well as backward.

A ───── B

We can move:

A → B
B → A

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. WEIGHTED GRAPH

→ A value/weight is present between two nodes.

The value can represent distance, cost, time, etc.

A ───10─── B

Here, 10 is the weight.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


4. UNWEIGHTED GRAPH

→ There is no value/weight associated with the edge between two nodes.

A ─────── B

There is only a connection between A and B.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


5. CYCLIC GRAPH

→ A graph in which a cycle is formed between vertices.

In other words, we can start from a vertex and come back to the same vertex through connected edges.

     A
    / \
   B---C

Cycle:

A → B → C → A

Continuous closed connection = Cycle

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


6. ACYCLIC GRAPH

→ A graph in which no cycle is formed between vertices.

     A
    / \
   B   C
  /
 D

There is no closed/continuous path that returns to the starting vertex.

No cycle = Acyclic

⭐ VERY EASY REVISION
DIRECTED GRAPH
→ Direction is present


UNDIRECTED GRAPH
→ Both directions are possible


WEIGHTED GRAPH
→ Value/weight is present


UNWEIGHTED GRAPH
→ No value/weight is present


CYCLIC GRAPH
→ Cycle is present


ACYCLIC GRAPH
→ Cycle is NOT present

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


QUICK REVISION
Type	Main Feature	Symbol/Example
Directed	Edge has direction	A → B
Undirected	No direction	A — B
Weighted	Edge has value	A —10— B
Unweighted	No edge value	A — B
Cyclic	Contains cycle	A → B → C → A
Acyclic	No cycle	A — B — C
Easy Memory Trick
DIRECTED   → Direction
UNDIRECTED → No Direction


WEIGHTED   → Weight
UNWEIGHTED → No Weight


CYCLIC     → Cycle Present
ACYCLIC    → Cycle Absent
-------------------------------------------------------------------------------------------------------------------------------------

----> Important Graph Terminology

| Term              | Meaning                                      |
| ----------------- | -------------------------------------------- |
| Vertex / Node     | A point in the graph                         |
| Edge              | Connection between two vertices              |
| Adjacent vertices | Two vertices directly connected by an edge   |
| Degree            | Number of edges connected to a vertex        |
| Path              | Sequence of vertices connected by edges      |
| Cycle             | Path that starts and ends at the same vertex |
| Connected graph   | Every vertex is reachable from another       |
| Weighted graph    | Edges have values/costs                      |
| Unweighted graph  | Edges do not have weights                    |
| Directed graph    | Edges have a direction                       |
| Undirected graph  | Edges have no direction                      |
| Loop / Self-loop  | Edge from a vertex to itself                 |

---------------------------------------------------------------------------------------------------------------------------------

---> Vertex

A vertex is a node or point in a graph.

Example:

A ---- B

A and B are vertices.

We can write:

V = {A, B}

------------------------------------------------------------------------------------------------------------------------------------

----> Edge

An edge represents a connection between two vertices.

A -------- B

Here:

A-B is an edge.

For the graph:

      A
     / \
    B---C

Edges are:

E = {AB, AC, BC}

----------------------------------------------------------------------------------------------------------------------

THEIR ARE 2 IMPLEMENTATION IN GRAPH

1. ADJANCEY MATRIX
2. ADJANCEY LIST


1. ADJANCEY MATRIX

An Adjacency Matrix represents a graph using a 2D matrix (2D array).

It shows whether there is an edge/connection between two vertices.

      A  B  C
   -----------
A |  0  1  1
B |  1  0  1
C |  1  1  0


--------------------------------------------------------------------------------------------------------------

2. ADJACENCY LIST

An Adjacency List represents a graph by storing the list of neighboring vertices for each vertex.

A → B, C
B → A, C
C → A, B



-----------------------------------------------------------------------------------------------------------------

X----->A           Node ---->  X Y Z A B C
|      |
|      |           EDGES ----> X ----> ( X, Y ) (X, A)
^      ^           EDGES ----> Y ----> ( Y, B ) ( Y, Z)
Y----->B           EDGES ----> Z ----> ( Z, C )
|      |           EDGES ----> A ----> ( A, B )
|      |           EDGES ----> B ----> ( B, C )
^      ^           EDGES ----> C ----> ( 0 )
Z----->C

..... Adjacency Matrix

For a directed graph:

1 → edge exists / DIRECT CONNECTION 
0 → edge does not exist / NO CONNECTION

|       | X | Y | Z | A | B | C |
| ----- | - | - | - | - | - | - |
| **X** | 0 | 1 | 0 | 1 | 0 | 0 |
| **Y** | 0 | 0 | 1 | 0 | 1 | 0 |
| **Z** | 0 | 0 | 0 | 0 | 0 | 1 |
| **A** | 0 | 0 | 0 | 0 | 1 | 0 |
| **B** | 0 | 0 | 0 | 0 | 0 | 1 |
| **C** | 0 | 0 | 0 | 0 | 0 | 0 |

       X  Y  Z  A  B  C
    ---------------------
X  |   0  1  0  1  0  0
Y  |   0  0  1  0  1  0
Z  |   0  0  0  0  0  1
A  |   0  0  0  0  1  0
B  |   0  0  0  0  0  1
C  |   0  0  0  0  0  0

-----------------------------------------------------------------------------------------------------------------------------


NODE -----> X Y Z A B C

EDGES -----> X         Y          Z          A           B               C
             |         |          |          |           |               |
            (X,A)      (Y, B)    (Z,C)      (A,B)       (B,C)           (C, Z)
            (X,Y)      (Y, Z)    (Z,Y)      (A,X)       (B,Y)           (C, B)

       X  Y  Z  A  B  C
    ---------------------
X  |   0  1  0  1  0  0
Y  |   1  0  1  0  1  0
Z  |   0  1  0  0  0  1
A  |   1  0  0  0  1  0
B  |   0  1  0  1  0  1
C  |   0  0  1  0  1  0

AD


'''
'''

nodes = ['X', 'Y', 'Z', 'A', 'B', 'C']

matrix = [
    [0, 1, 0, 1, 0, 0],  # X
    [1, 0, 1, 0, 1, 0],  # Y
    [0, 1, 0, 0, 0, 1],  # Z
    [1, 0, 0, 0, 1, 0],  # A
    [0, 1, 0, 1, 0, 1],  # B
    [0, 0, 1, 0, 1, 0]   # C
]

print("   ", nodes)

for i in range(len(nodes)):
    print(nodes[i], matrix[i])
''' 
# --------------------------------------------------------------------------------------------------------------------------------------------

''' 

a={ "X": ["A", "Y"],
    "Y": ["X", "B", "Z"], 
    "Z": ["Y", "C"],
    "A": ["X", "B"],
    "B": ["A", "Y", "C"],
    "c": ["B", "Z"]}

print( "  X  Y  Z  A  B  C")
for node in a:
    print(node, "---->", a[node])

# --------------------------------------------------------------------------------------------------------------------------------------------

nodes = ['X', 'Y', 'Z', 'A', 'B', 'C']

matrix = [
    [0, 1, 0, 1, 0, 0],  # X
    [1, 0, 1, 0, 1, 0],  # Y
    [0, 1, 0, 0, 0, 1],  # Z
    [1, 0, 0, 0, 1, 0],  # A
    [0, 1, 0, 1, 0, 1],  # B
    [0, 0, 1, 0, 1, 0]   # C
]

print("   X  Y  Z  A  B  C")               # ----> TO PRINT COLUMN 

for i in range(len(nodes)):
    print(nodes[i], matrix[i])             # VARIABLE_NAME[Position]

# O/P--->

#    X  Y  Z  A  B  C
# X [0, 1, 0, 1, 0, 0]
# Y [1, 0, 1, 0, 1, 0]
# Z [0, 1, 0, 0, 0, 1]
# A [1, 0, 0, 0, 1, 0]
# B [0, 1, 0, 1, 0, 1]

# ---------------------------------------------------------------------------------------------------------------------------------

Node=[ "A" , "B", "C", "D"]

M=[[0, 1, 1, 0], 
   [1, 0, 1, 0],
   [1, 1, 0, 1], 
   [0, 0, 1, 0]]

print( "   A  B  C  D")

for i in range(len(Node)):
    print(Node[i], M[i])

# o/p---------->

#    A  B  C  D
# A [0, 1, 1, 0]
# B [1, 0, 1, 0]
# C [1, 1, 0, 1]
# D [0, 0, 1, 0]

# ---------------------------------------------------------------------------------------------------------------------------------

''' 

''' 

TYPES OF GRAPH

1. DIRECTED GRAPH 

vertex : edge
  |       |
Node      Edge


'''

# DIRECT GRAPH -----> EXAMPLE --> 1

class Graph:
    def __init__(self):
        self.graph={}


    def Add_vertex(self,Node):
        self.graph[Node]=[]       # ----> var_name[key]=value    # -----> {'A': [], 'B': [], 'C': [], 'D': []}


    def Add_edges(self, N1, N2):        # -----> To connect the Node 1 to Node 2 
        self.graph[N1].append(N2)       # -----> A → B → C → D
        
    def Display(self):
        for i in self.graph:
            print(i, "----->", self.graph[i])

g=Graph()
g.Add_vertex("A")
g.Add_vertex("B")
g.Add_vertex("C")
g.Add_vertex("D")

g.Add_edges("A", "B")
g.Add_edges("B", "C")
g.Add_edges("C", "D")

print(g.graph)               # ----> g = object , graph = empty dictionary  # ---> o/p ---->{'A': ['B'], 'B': ['C'], 'C': ['D'], 'D': []}
g.Display()

# o/p ---> 
# A -----> ['B']
# B -----> ['C']
# C -----> ['D']
# D -----> []

print()

# -------------------------------------------------------------------------------------------------------------------------------------------------

# UNDEIRECTED GRAPH

class Graph:
    def __init__(self):
        self.graph={}


    def Add_vertex(self,Node):
        self.graph[Node]=[]       # ----> var_name[key]=value    # -----> {'A': [], 'B': [], 'C': [], 'D': []}


    def Add_edges(self, N1, N2):        # -----> To connect the Node 1 to Node 2 
        self.graph[N1].append(N2)       # -----> A → B → C → D
        self.graph[N2].append(N1)       # -----> D → C → B → A


    def Display(self):
        for i in self.graph:
            print(i, "----->", self.graph[i])

g=Graph()
g.Add_vertex("A")
g.Add_vertex("B")
g.Add_vertex("C")
g.Add_vertex("D")

g.Add_edges("A", "B")
g.Add_edges("B", "C")
g.Add_edges("C", "D")

print(g.graph)               # ----> g = object , graph = empty dictionary  # ---> o/p ----> {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C']}

g.Display()

# o/p ---> 
# A -----> ['B']
# B -----> ['A', 'C']
# C -----> ['B', 'D']
# D -----> ['C']

print()
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DIRECT GRAPH -----> EXAMPLE --> 2

class Graph:
    def __init__(self):
        self.graph={}


    def Add_vertex(self,Node):
        self.graph[Node]=[]       # ----> var_name[key]=value    # -----> {'A': [], 'B': [], 'C': [], 'D': []}


    def Add_edges(self, N1, N2):        # -----> To connect the Node 1 to Node 2 
        self.graph[N1].append(N2)       # -----> A → B → C → D
        
    def Display(self):
        for i in self.graph:
            print(i, "----->", self.graph[i])

g=Graph()
g.Add_vertex("A")
g.Add_vertex("B")
g.Add_vertex("C")
g.Add_vertex("D")
g.Add_vertex("E")
g.Add_vertex("F")



g.Add_edges("A", "C")
g.Add_edges("C", "B")
g.Add_edges("C", "D")
g.Add_edges("C", "F")
g.Add_edges("E", "F")
g.Add_edges("D", "E")




print(g.graph)               # ----> g = object , graph = empty dictionary  # ---> o/p ----> {'A': ['C'], 'B': [], 'C': ['B', 'D', 'F'], 'D': ['E'], 'E': ['F'], 'F': []}
g.Display()

# o/p ---> 
# A -----> ['C']
# B -----> []
# C -----> ['B', 'D', 'F']
# D -----> ['E']
# E -----> ['F']
# F -----> []

print()

# -------------------------------------------------------------------------------------------------------------------------------------------------

# UNDIRECT GRAPH -----> EXAMPLE --> 2

class Graph:
    def __init__(self):
        self.graph={}


    def Add_vertex(self,Node):
        self.graph[Node]=[]       # ----> var_name[key]=value    # -----> {'A': [], 'B': [], 'C': [], 'D': []}


    def Add_edges(self, N1, N2):        # -----> To connect the Node 1 to Node 2 
        self.graph[N1].append(N2)       # -----> A → B → C → 
        self.graph[N2].append(N1)      
        
        
    def Display(self):
        for i in self.graph:
            print(i, "----->", self.graph[i])      # -----> A B C D E F , self.graph[i] -----> A - [C] , B- [C] -----

g=Graph()
g.Add_vertex("A")
g.Add_vertex("B")
g.Add_vertex("C")
g.Add_vertex("D")
g.Add_vertex("E")
g.Add_vertex("F")



g.Add_edges("A", "C")
g.Add_edges("C", "B")
g.Add_edges("C", "D")
g.Add_edges("C", "F")
g.Add_edges("E", "F")
g.Add_edges("D", "E")




print(g.graph)               # ----> g = object , graph = empty dictionary  # ---> o/p ----> {'A': ['C'], 'B': ['C'], 'C': ['A', 'B', 'D', 'F'], 'D': ['C', 'E'], 'E': ['F', 'D'], 'F': ['C', 'E']}
g.Display()

# o/p ---> 
# A -----> ['C']
# B -----> ['C']
# C -----> ['A', 'B', 'D', 'F']
# D -----> ['C', 'E']
# E -----> ['F', 'D']
# F -----> ['C', 'E']

print()

# -------------------------------------------------------------------------------------------------------------------------------------------------
''' 
# manually done

# UNDIRECT GRAPH -----> EXAMPLE --> 2
class Graph:
    def __init__(self):
        self.graph={}


    def Add_vertex(self,Node):
        self.graph[Node]=[]       # ----> var_name[key]=value    # -----> {'A': [], 'B': [], 'C': [], 'D': []}


    def Add_edges(self, N1, N2):        # -----> To connect the Node 1 to Node 2 
        self.graph[N1].append(N2)       # -----> A → B → C → D
        
    def Display(self):
        for i in self.graph:
            print(i, "----->", self.graph[i])

g=Graph()
g.Add_vertex("A")
g.Add_vertex("B")
g.Add_vertex("C")
g.Add_vertex("D")
g.Add_vertex("E")
g.Add_vertex("F")



g.Add_edges("A", "C")
g.Add_edges("B", "C")
g.Add_edges("C", "B")
g.Add_edges("C", "A")
g.Add_edges("C", "D")
g.Add_edges("C", "F")
g.Add_edges("E", "F")
g.Add_edges("E", "D")
g.Add_edges("D", "E")
g.Add_edges("D", "C")
g.Add_edges("F", "E")
g.Add_edges("F", "C")





print(g.graph)               # ----> g = object , graph = empty dictionary  # ---> o/p ----> {'A': ['C'], 'B': ['C'], 'C': ['B', 'A', 'D', 'F'], 'D': ['E', 'C'], 'E': ['F', 'D'], 'F': ['E', 'C']}

# # o/p ---> 
# A -----> ['C']
# B -----> ['C']
# C -----> ['B', 'A', 'D', 'F']
# D -----> ['E', 'C']
# E -----> ['F', 'D']
# F -----> ['E', 'C']


print()

# -----------------------------------------------------------------------------------------------------------------------------------------------

'''

# Excercise -- 1


class G:
    def __init__(self):
        self.graph={}

    def Vertex(self,Node):
        self.graph[Node]=[]      #nar_name[key]=value ----> key value syntax

    def Edge(self, N1, N2):
        self.graph[N1].append(N2)

    def Show(self):
        for i in self.graph:
            print(i, "-----", self.graph[i])

a=G()
a.Vertex("P")
a.Vertex("Q")
a.Vertex("R")
a.Vertex("S")

a.Edge("P","Q")
a.Edge("Q", "R")
a.Edge("R","S")

a.Show()

# P ----- ['Q']
# Q ----- ['R']
# R ----- ['S']
# S ----- []

print()
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# WEIGHTED DIRECT GRAPH -----> EXAMPLE --> 1

class Graph:
    def __init__(self):
        self.graph={}


    def Add_vertex(self,Node):
        self.graph[Node]=[]       # ----> var_name[key]=value    # -----> {'A': [], 'B': [], 'C': [], 'D': []}


    def Add_edges(self, N1, N2, value):        # -----> To connect the Node 1 to Node 2 
        self.graph[N1].append((N2,value))       
    def Display_Connection(self):
        for i in self.graph:
            print(i, "----->", self.graph[i])       # ----> {'A': [('B', 20)], 'B': [('C', 30)], 'C': [('D', 40)], 'D': []}

g=Graph()
g.Add_vertex("A")
g.Add_vertex("B")
g.Add_vertex("C")
g.Add_vertex("D")

g.Add_edges("A", "B", 20)
g.Add_edges("B", "C", 30)
g.Add_edges("C", "D", 40)




print(g.graph)               # ----> g = object , graph = empty dictionary  # ---> o/p ----> {'A': [('B', 20)], 'B': [('C', 30)], 'C': [('D', 40)], 'D': []}
g.Display_Connection()

# o/p ---> 

# A -----> [('B', 20)]
# B -----> [('C', 30)]
# C -----> [('D', 40)]
# D -----> []

print()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# WEIGHTED UNDIRECT GRAPH -----> EXAMPLE --> 2

class Graph:
    def __init__(self):
        self.graph={}


    def Add_vertex(self,Node):
        self.graph[Node]=[]       # ----> var_name[key]=value    # -----> {'A': [], 'B': [], 'C': [], 'D': []}


    def Add_edges(self, N1, N2, value):        # -----> To connect the Node 1 to Node 2 
        self.graph[N1].append((N2,value))
        self.graph[N2].append((N1,value))       

    def Display_Connection(self):
        for i in self.graph:
            print(i, "----->", self.graph[i])       # ----> {'A': [('B', 20)], 'B': [('C', 30)], 'C': [('D', 40)], 'D': []}

g=Graph()
g.Add_vertex("A")
g.Add_vertex("B")
g.Add_vertex("C")
g.Add_vertex("D")

g.Add_edges("A", "B", 20)
g.Add_edges("B", "C", 30)
g.Add_edges("C", "D", 40)




print(g.graph)               # ----> g = object , graph = empty dictionary  # ---> o/p ----> {'A': [('B', 20)], 'B': [('A', 20), ('C', 30)], 'C': [('B', 30), ('D', 40)], 'D': [('C', 40)]}
g.Display_Connection()

# o/p ---> 


# A -----> [('B', 20)]
# B -----> [('A', 20), ('C', 30)]
# C -----> [('B', 30), ('D', 40)]
# D -----> [('C', 40)]

print()

# --------------------------------------------------------------------------------------------------------------------------------------------------

# weighted direct Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2,values):
        self.graph[n1].append((n2,values))

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B",20)
g.add_edges("B","C",30)
g.add_edges("C","D",40)

g.Display_connections()

print()

"""
"""
#weighted undirect Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2,values):
        self.graph[n1].append((n2,values))
        self.graph[n2].append((n1,values))

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B",20)
g.add_edges("B","C",30)
g.add_edges("C","D",40)

g.Display_connections()
print()

# -----------------------------------------------------------------------------------------------------------------------------------------------

''' 
 PRABHU SIR NOTES 

 '''
#Directed Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
#Undirected Graph---->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
# directed Graph----->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()

'''

'''
#undirected Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()
'''




'''
#Directed Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
#Undirected Graph---->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
# directed Graph----->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()

'''

'''
#self looping /self connection
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edges("A","B")
g.add_edges("B","B")
g.Display_connections()
'''


'''
#Directed Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
#Undirected Graph---->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
# directed Graph----->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()

'''

'''
#undirected Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()
'''


'''
#Directed Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
#Undirected Graph---->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
# directed Graph----->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()

'''

'''
#undirected Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()
'''




'''
#Directed Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
#Undirected Graph---->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
# directed Graph----->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()

'''

'''
#self looping /self connection
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edges("A","B")
g.add_edges("B","B")
g.Display_connections()
'''


'''
#Directed Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
#Undirected Graph---->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
# directed Graph----->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()

'''

'''
#undirected Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()
'''






'''
#Directed Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
#Undirected Graph---->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B")
g.add_edges("B","C")
g.add_edges("C","D")

g.Display_connections()
'''

'''
# directed Graph----->
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()

'''

'''
#undirected Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edges("A","C")
g.add_edges("C","B")
g.add_edges("C","D")
g.add_edges("C","F")
g.add_edges("D","E")
g.add_edges("E","F")

g.Display_connections()
'''




"""
weighted direct Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2,values):
        self.graph[n1].append((n2,values))

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B",20)
g.add_edges("B","C",30)
g.add_edges("C","D",40)

g.Display_connections()

print()

"""
"""
#weighted undirect Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2,values):
        self.graph[n1].append((n2,values))
        self.graph[n2].append((n1,values))

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B",20)
g.add_edges("B","C",30)
g.add_edges("C","D",40)

g.Display_connections()
"""



'''
#Directed Graph
# class Graph:
#     def __init__(self):
#         self.graph={}

#     def add_vertex(self,node):
#         self.graph[node]=[]   #var_name[key]=value

#     def add_edges(self,n1,n2):
#         self.graph[n1].append(n2)

#     def Display_connections(self):
#         for i in self.graph:
#             print(i,"------->",self.graph[i])

# g=Graph()
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")

# g.add_edges("A","B")
# g.add_edges("B","C")
# g.add_edges("C","D")

# g.Display_connections()
'''

'''
#Undirected Graph---->
# class Graph:
#     def __init__(self):
#         self.graph={}

#     def add_vertex(self,node):
#         self.graph[node]=[]   #var_name[key]=value

#     def add_edges(self,n1,n2):
#         self.graph[n1].append(n2)
#         self.graph[n2].append(n1)

#     def Display_connections(self):
#         for i in self.graph:
#             print(i,"------->",self.graph[i])

# g=Graph()
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")

# g.add_edges("A","B")
# g.add_edges("B","C")
# g.add_edges("C","D")

# g.Display_connections()
'''

'''
# directed Graph----->
# class Graph:
#     def __init__(self):
#         self.graph={}

#     def add_vertex(self,node):
#         self.graph[node]=[]   #var_name[key]=value

#     def add_edges(self,n1,n2):
#         self.graph[n1].append(n2)

#     def Display_connections(self):
#         for i in self.graph:
#             print(i,"------->",self.graph[i])

# g=Graph()
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")
# g.add_vertex("E")
# g.add_vertex("F")

# g.add_edges("A","C")
# g.add_edges("C","B")
# g.add_edges("C","D")
# g.add_edges("C","F")
# g.add_edges("D","E")
# g.add_edges("E","F")

# g.Display_connections()

'''

'''
#undirected Graph
# class Graph:
#     def __init__(self):
#         self.graph={}

#     def add_vertex(self,node):
#         self.graph[node]=[]   #var_name[key]=value

#     def add_edges(self,n1,n2):
#         self.graph[n1].append(n2)
#         self.graph[n2].append(n1)

#     def D_connections(self):
#         for i in self.graph:
#             print(i,"------->",self.graph[i])

# g=Graph()
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")
# g.add_vertex("E")
# g.add_vertex("F")

# g.add_edges("A","C")
# g.add_edges("C","B")
# g.add_edges("C","D")
# g.add_edges("C","F")
# g.add_edges("D","E")
# g.add_edges("E","F")

# g.D_connections()
'''




"""
weighted direct Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2,values):
        self.graph[n1].append((n2,values))

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B",20)
g.add_edges("B","C",30)
g.add_edges("C","D",40)

g.Display_connections()

print()

"""
"""
#weighted undirect Graph
class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,node):
        self.graph[node]=[]   #var_name[key]=value

    def add_edges(self,n1,n2,values):
        self.graph[n1].append((n2,values))
        self.graph[n2].append((n1,values))

    def Display_connections(self):
        for i in self.graph:
            print(i,"------->",self.graph[i])

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A","B",20)
g.add_edges("B","C",30)
g.add_edges("C","D",40)

g.Display_connections()
"""

'''

''' 

BFS 
BREADTH FIRST SEARCH -------> IT WILL WORK LEVEL TO LEVEL 

         A            ----> LEVEL 0
       /   \
      B     C           ----> LEVEL 1
    /  \     |
    D   E    F           ----> LEVEL 2

    A B C D E F


'''
print()

class Graph:
    def __init__(self):
        self.graph={}

    def nodes(self, node):
        self.graph[node]=[]

    def add_edges(self, n1, n2):
        self.graph[n1].append(n2)


    def Display(self):
        for i in self.graph:
            print(i, "-------->", self.graph[i])

d=Graph()
d.nodes("A")
d.nodes("B")
d.nodes("C")
d.nodes("D")
d.nodes("E")
d.nodes("F")

d.add_edges("A","B")
d.add_edges("A","C")
d.add_edges("B","D")
d.add_edges("B","E")
d.add_edges("C","F")

d.Display()

# o/p--->

# A --------> ['B', 'C']
# B --------> ['D', 'E']
# C --------> ['F']
# D --------> []
# E --------> []
# F --------> []

'''
BFS Vs DFS
--------------
Breadth First serach(BFS)--->it will work level to level

ex-    A                LEVEL 0
      / \
     B   C             LEVEL 1
    /\    /
   D  E   F            LEVEL 2

--> A B C D E F

'''        

# IMPLEMENTING BFS USING CLASS

'''
from collections import deque
class BFS:
   def __init__(self):
      self.graph={}
   def add_nodes(self,nodes):
      self.graph[nodes]=[]
   def add_edge(self, n1,n2):
      self.graph[n1].append(n2)
   # def Display(self):
   #    for i in self.graph:
   #       print(i,"------>",self.graph[i])

   def breadt_first_search(self,start):
      s=set()     #what element we are starting we have to store this in set (no need to store duplicated then use set)
      queue=deque()                #what element we are storing in dequeue first that element we have to remove (FIFO)
      s.add(start)                    #{A}                                                 #{B, C}               
      queue.append(start)             #[A]                                                 #[B, C]


      while queue:
         new=queue.popleft()          # new=[A].popleft()                                   #new=queue.popleft(B)
         print(new,end=" ")
         for i in self.graph[new]:          #i means visited self.graph[A]                  # self.graph[B]
            if i not in s:               #if element is not present then add in the set     #
               s.add(i)                     # {A,B,C}                                       #{B,C}
               queue.append(i)              #[B,C]           
                                              #[C,D,E]


g=BFS()
g.add_nodes('A')
g.add_nodes('B')
g.add_nodes('C')
g.add_nodes('D')
g.add_nodes('E')
g.add_nodes('F')

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('C','F')
# g.Display()

# A ------> ['B', 'C']
# B ------> ['D', 'E']
# C ------> ['F']
# D ------> []
# E ------> []
# F ------> []

g.breadt_first_search('A')   #A B C D E F 
'''
print()

# ----------------------------------------


# LEVEL-WISE IF WE HAVE TO PRINT THE BFS THEN 
'''
from collections import deque
class BFS:
   def __init__(self):
      self.graph={}
   def add_nodes(self,nodes):
      self.graph[nodes]=[]
   def add_edge(self, n1,n2):
      self.graph[n1].append(n2)
   # def Display(self):
   #    for i in self.graph:
   #       print(i,"------>",self.graph[i])

   def breadt_first_search(self,start):
      s=set()     #what element we are starting we have to store this in set (no need to store duplicated then use set)
      queue=deque()                #what element we are storing in dequeue first that element we have to remove (FIFO)
      s.add(start)                    #{A}                                                               
      queue.append(start)             #[A]                                           

      level=0

      while queue:
         size=len(queue)
         for i in range(size):
            print("LEVEL",level,end="--- ")
            new=queue.popleft()          # new=[A].popleft()                          
            print(new,end=" ")
            for i in self.graph[new]:                       
               if i not in s:                   
                  s.add(i)                                                   
                  queue.append(i)    
         print()
         level=level+1                   
                                              


g=BFS()
g.add_nodes('A')
g.add_nodes('B')
g.add_nodes('C')
g.add_nodes('D')
g.add_nodes('E')
g.add_nodes('F')

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('C','F')

g.breadt_first_search("A")
# o/p-->
# LEVEL 0--- A 
# LEVEL 1--- B LEVEL 1--- C 
# LEVEL 2--- D LEVEL 2--- E LEVEL 2--- F 
'''
print()

# ------------------------------------------


# CALCULATING TOTAL NO. OF NODES IN BFS 

from collections import deque
class BFS:
   def __init__(self):
      self.graph={}
   def add_nodes(self,nodes):
      self.graph[nodes]=[]
   def add_edge(self, n1,n2):
      self.graph[n1].append(n2)

   # def Display(self):
   #    for i in self.graph:
   #       print(i,"------>",self.graph[i])

   def breadt_first_search(self,start):
      s=set()                      # what element we are starting we have to store this in set (no need to store duplicated then use set)
      queue=deque()                # what element we are storing in dequeue first that element we have to remove (FIFO)
      s.add(start)                    #{A}                                                               
      queue.append(start)             #[A]                                           

      count=0

      while queue:
         new=queue.popleft()
         count=count+1
         print(new,end=" ")
         for i in self.graph[new]:
            if i not in s:
               s.add(i)
               queue.append(i)
      print()
      print("TOTAL NUMBER OF COUNT_--->",count)

g=BFS()
g.add_nodes('A')
g.add_nodes('B')
g.add_nodes('C')
g.add_nodes('D')
g.add_nodes('E')
g.add_nodes('F')

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('C','F')

g.breadt_first_search("A")
# o/p--->
# A B C D E F 
# TOTAL NUMBER OF COUNT_---> 6

print(" ------------------------------------------------------------------------------------------------------ ")

from collections import deque            # --> Double Ended Queue.
class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    # def Display(self):
    #     for i in self.graph:
    #         print(i,"------->",self.graph[i])

    def BFS(self,start):
        s=set()
        queue=deque()
        s.add(start)    #{A}
        queue.append(start)   #[A]
        while queue:
            new=queue.popleft()  #new=[A].popleft()
            print(new,end=" ")
            for i in self.graph[new]: #B
                if i not in s:
                    s.add(i)   #{A,B,C}
                    queue.append(i)# [A,B,C]
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C","F")
g.BFS("A")

print() 
print(" ------------------------------------------------------------------------------------------------------ ")


#wap to Print element level by level

from collections import deque
class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def BFS(self,start):
        s=set()
        queue=deque()
        s.add(start)  #{A}
        queue.append(start)  #[A]
        level=0
        while queue:   #[A]
            size=len(queue)  #size=len([A])  --->1
            for i in range(size):
                print("Level",level,end=" ")
                new=queue.popleft()  #new=[A].popleft()
                print(new,end=" ")
                for i in self.graph[new]: #B
                    if i not in s:
                        s.add(i)   #{A,B,C}
                        queue.append(i)# [A,B,C]
            print()
            level=level+1

g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C","F")
g.BFS("A")

print()
print(" ------------------------------------------------------------------------------------------------------ ")


#wap to find out Total Number of Node
from collections import deque
class Graph:
    def __init__(self):
        self.graph={}
    def add_nodes(self,nodes):
        self.graph[nodes]=[]
    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
    def BFS(self,start):
        s=set()
        queue=deque()
        s.add(start)
        queue.append(start)
        count=0
        while queue:
            new=queue.popleft()
            count=count+1
            print(new,end=" ")
            for i in self.graph[new]:
                if i not in s:
                    s.add(i)
                    queue.append(i)
        return "Total Number of Node",count
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C","F")
print(g.BFS("A"))

'''
Prabhu sir code 
'''

print()
print(" ------------------------------------------------------------------------------------------------------ ")

from collections import deque
class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    # def Display(self):
    #     for i in self.graph:
    #         print(i,"------->",self.graph[i])

    def BFS(self,start):
        s=set()
        queue=deque()
        s.add(start)    #{A}
        queue.append(start)   #[A]
        while queue:
            new=queue.popleft()  #new=[A].popleft()
            print(new,end=" ")
            for i in self.graph[new]: #B
                if i not in s:
                    s.add(i)   #{A,B,C}
                    queue.append(i)# [A,B,C]
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C","F")
g.BFS("A")

print(" ------------------------------------------------------------------------------------------------------ ")
print()


#wap to Print element level by level

from collections import deque
class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def BFS(self,start):
        s=set()
        queue=deque()
        s.add(start)  #{A}
        queue.append(start)  #[A]
        level=0
        while queue:   #[A]
            size=len(queue)  #size=len([A])  --->1
            for i in range(size):
                print("Level",level,end=" ")
                new=queue.popleft()  #new=[A].popleft()
                print(new,end=" ")
                for i in self.graph[new]: #B
                    if i not in s:
                        s.add(i)   #{A,B,C}
                        queue.append(i)# [A,B,C]
            print()
            level=level+1

g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C","F")
g.BFS("A")

print(" ------------------------------------------------------------------------------------------------------ ")
print()

#wap to find out Total Number of Node
from collections import deque
class Graph:
    def __init__(self):
        self.graph={}
    def add_nodes(self,nodes):
        self.graph[nodes]=[]
    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
    def BFS(self,start):
        s=set()
        queue=deque()
        s.add(start)
        queue.append(start)
        count=0
        while queue:
            new=queue.popleft()
            count=count+1
            print(new,end=" ")
            for i in self.graph[new]:
                if i not in s:
                    s.add(i)
                    queue.append(i)
        return "Total Number of Node",count
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C","F")
print(g.BFS("A"))

print(" ------------------------------------------------------------------------------------------------------ ")


''' 

1. First understand BFS in very simple words

BFS = Breadth First Search

Think about a building.

Suppose:

             A
           /   \
          B     C
         / \     \
        D   E     F

If we want to visit all rooms starting from A, BFS says:

First visit A, then all rooms directly connected to A, then their next rooms.

So the order is:

A → B → C → D → E → F

This is called level-by-level traversal.

LEVEL 0 :       A

LEVEL 1 :     B   C

LEVEL 2 :   D  E   F
2. Important concepts before the code
A. Graph

A graph contains nodes and connections.

Here:

A, B, C, D, E, F

are nodes.

Connections are:

A → B
A → C
B → D
B → E
C → F

So:

             A
           /   \
          B     C
         / \     \
        D   E     F
3. deque — what is it?

Your code contains:

from collections import deque

deque means Double Ended Queue.

For BFS, we mainly use it like a normal queue.

Queue means:

First In → First Out

FIFO:

First person entering the line leaves first.

Example:

Queue:

[A, B, C]

A entered first
A will leave first

That's why BFS uses:

queue.append()

to add something at the back and:

queue.popleft()

to remove the first element.

4. set — why do we need it?

The code uses:

s=set()

The set stores the nodes that we have already visited.

Why?

Imagine:

A → B
A → C
B → C

When we visit A:

A visited

Then B:

B visited

B may again point to C.

Without a set, we might add C again.

So:

if i not in s:

means:

"If this node has NOT already been visited..."

Then:

s.add(i)

means:

"Mark this node as visited."

5. First BFS program

Your first program starts with:

from collections import deque

class BFS:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edge(self,n1,n2):
        self.graph[n1].append(n2)

These lines create and store the graph.

Line 1
from collections import deque
Simple meaning:

We are bringing the deque tool from Python.

We need it to create our queue.

Think:

Python
  ↓
Bring Queue tool
  ↓
deque
6. Creating the class
class BFS:
Meaning:

We are creating a class called BFS.

You can think of a class as a blueprint.

For example:

Class = Blueprint
Object = Actual thing created from blueprint

Later:

g=BFS()

creates an actual BFS object.

7. Constructor
def __init__(self):
    self.graph={}
__init__

This is the constructor.

It automatically runs when we create:

g=BFS()
self.graph={}

This creates an empty dictionary.

Initially:

graph = {}

We will store our graph inside this dictionary.

Eventually it becomes:

{
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

This means:

A is connected to B and C

B is connected to D and E

C is connected to F
8. Adding nodes
def add_nodes(self,nodes):
    self.graph[nodes]=[]

Suppose we execute:

g.add_nodes('A')

Then:

self.graph['A']=[]

Our dictionary becomes:

{
    'A': []
}

Then:

g.add_nodes('B')

becomes:

{
    'A': [],
    'B': []
}

Eventually:

{
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}
9. Adding an edge
def add_edge(self,n1,n2):
    self.graph[n1].append(n2)

This creates a connection.

For example:

g.add_edge('A','B')

means:

A → B

So:

self.graph['A'].append('B')

Dictionary becomes:

{
    'A': ['B'],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

Then:

g.add_edge('A','C')

becomes:

{
    'A': ['B','C'],
    ...
}
10. Complete graph after adding edges

Your code adds these edges:

A → B
A → C
B → D
B → E
C → F

Therefore:

             A
           /   \
          B     C
         / \     \
        D   E     F

Dictionary representation:

A → [B, C]
B → [D, E]
C → [F]
D → []
E → []
F → []
11. Now the MAIN BFS function

The important function is:

def breadt_first_search(self,start):

It receives the starting node.

When we call:

g.breadt_first_search('A')

we are saying:

"Start BFS from A."

The function's main code is:

def breadt_first_search(self,start):

    s=set()

    queue=deque()

    s.add(start)

    queue.append(start)

    while queue:

        new=queue.popleft()

        print(new,end=" ")

        for i in self.graph[new]:

            if i not in s:

                s.add(i)

                queue.append(i)

Now let's understand every line.

12. Create visited set
s=set()

Initially:

s = {}

It will store visited nodes.

13. Create queue
queue=deque()

Initially:

queue = []

It is empty.

14. Add starting node to visited set
s.add(start)

Since:

start='A'

we get:

s = {A}

Meaning:

A has been marked as visited.

15. Add A to queue
queue.append(start)

So:

queue = [A]

Now:

Visited Set = {A}

Queue = [A]
16. while queue
while queue:

Meaning:

Keep working as long as the queue is NOT empty.

If:

queue = [A]

then queue has something, so continue.

When:

queue = []

the loop stops.

17. Remove first element
new=queue.popleft()

Currently:

queue = [A]

popleft() removes A.

So:

new = A
queue = []
18. Print the node
print(new,end=" ")

Output:

A

end=" " means don't move to the next line.

So output continues on the same line:

A B C D E F
19. Find A's neighbours
for i in self.graph[new]:

Currently:

new = A

Therefore:

self.graph[A]

is:

[B,C]

So the loop runs:

i = B
i = C
20. Check whether B was visited
if i not in s:

Currently:

s = {A}

B is not inside the set.

Therefore:

B not in {A}

is TRUE.

21. Add B to visited set
s.add(i)

Now:

s = {A,B}
22. Add B to queue
queue.append(i)

Now:

queue = [B]

Then the loop moves to C.

C is also not visited.

So:

s = {A,B,C}
queue = [B,C]
23. COMPLETE BFS TRACING

This is the most important part.

Initial:

Graph:

             A
           /   \
          B     C
         / \     \
        D   E     F

Start:

g.breadt_first_search('A')
STEP 1

Initially:

Visited = {}
Queue = []

Add A:

Visited = {A}
Queue = [A]
STEP 2

Remove A:

new = queue.popleft()

So:

new = A
Queue = []

Print:

A

A has:

B, C

Add B:

Visited = {A,B}
Queue = [B]

Add C:

Visited = {A,B,C}
Queue = [B,C]
STEP 3

Remove B.

Queue = [B,C]

After:

popleft()

we get:

new = B
Queue = [C]

Print:

B

B has:

D,E

Add D:

Visited = {A,B,C,D}
Queue = [C,D]

Add E:

Visited = {A,B,C,D,E}
Queue = [C,D,E]
STEP 4

Remove C:

Queue = [C,D,E]

After removing:

new = C
Queue = [D,E]

Print:

C

C has:

F

Add F:

Visited = {A,B,C,D,E,F}
Queue = [D,E,F]
STEP 5

Remove D:

new = D
Queue = [E,F]

Print:

D

D has no neighbours:

D → []

Nothing is added.

STEP 6

Remove E:

new = E
Queue = [F]

Print:

E

E has no neighbours.

STEP 7

Remove F:

new = F
Queue = []

Print:

F

F has no neighbours.

STEP 8

Now:

Queue = []

Therefore:

while queue:

becomes FALSE.

BFS stops.

FINAL TRACE TABLE
Step	Removed	Queue After Removal	Newly Added	Visited
1	A	[]	B, C	A B C
2	B	[C]	D, E	A B C D E
3	C	[D,E]	F	A B C D E F
4	D	[E,F]	None	A B C D E F
5	E	[F]	None	A B C D E F
6	F	[]	None	A B C D E F

Therefore:

OUTPUT:

A B C D E F

Your file also gives this expected BFS order.

24. Why BFS gives A B C D E F

Look at the levels:

LEVEL 0
        A

LEVEL 1
      B   C

LEVEL 2
    D  E   F

BFS goes:

A
↓
B C
↓
D E F

Therefore:

A B C D E F
Easy memory trick:

BFS = First complete the current level, then go to the next level.

25. LEVEL-WISE BFS

Your second program adds:

level=0

Then:

size=len(queue)

and:

for i in range(size):

This is used to print nodes level by level.

Why level=0?

We start at:

A

So:

Level 0 = A

Then:

Level 1 = B C

Then:

Level 2 = D E F
26. Why size=len(queue)?

Suppose:

Queue = [A]

Then:

size=len(queue)

gives:

size = 1

So:

for i in range(size):

runs one time.

We process only Level 0.

After processing A, queue becomes:

[B,C]

Now:

size = 2

Therefore we process exactly:

B and C

That's how the program knows which nodes belong to the same level.

27. Level-wise tracing
Initial
level = 0

Queue = [A]
Level 0
size = 1

Process:

A

Add:

B,C

Queue:

[B,C]

Print:

LEVEL 0--- A

Increase:

level=level+1

Now:

level = 1
Level 1

Queue:

[B,C]

Therefore:

size = 2

Process B and C.

B adds:

D,E

C adds:

F

Queue becomes:

[D,E,F]

Output:

LEVEL 1--- B LEVEL 1--- C
Level 2
Queue = [D,E,F]
size = 3

Process:

D
E
F

No new nodes.

Output:

LEVEL 2--- D LEVEL 2--- E LEVEL 2--- F

Queue becomes empty.

Stop.

Your file shows the same expected level-wise output.

28. Why do we need range(size)?

This is a very important exam/interview point.

Suppose:

Queue = [B,C]

Both B and C belong to Level 1.

So:

size=len(queue)

gives:

size = 2

Then:

for i in range(2):

means:

Process B
Process C

Only after both are processed do we move to Level 2.

29. BFS WITH NODE COUNT

Your third version adds:

count=0

Then:

count=count+1

every time a node is removed from the queue.

The important part is:

count=0

while queue:

    new=queue.popleft()

    count=count+1

    print(new,end=" ")
Tracing count

Initially:

count = 0

A removed:

count = 1

B removed:

count = 2

C removed:

count = 3

D removed:

count = 4

E removed:

count = 5

F removed:

count = 6

Therefore:

TOTAL NUMBER OF COUNT ---> 6

Your source gives the expected result of 6.

30. Another version: return instead of print

Later in your file, you have:

def BFS(self,start):

and at the end:

return "Total Number of Node",count

The BFS itself is almost the same.

The difference is:

Earlier:
print("TOTAL NUMBER...",count)

The function itself prints the answer.

Later:
return "Total Number of Node",count

The function sends the answer back.

That's why we use:

print(g.BFS("A"))

The print() outside the function displays the returned value.

Output:

A B C D E F
('Total Number of Node', 6)
31. print() vs return

This is important.

print
print(count)

means:

Show the value on the screen.

return
return count

means:

Send the value back to whoever called the function.

Example:

x = function()

If function has:

return 6

then:

x = 6
32. Why are there so many repeated BFS programs?

Your file contains multiple versions of essentially the same program.

They demonstrate different tasks:

Version 1
Basic BFS

Output:

A B C D E F
Version 2
Level-wise BFS

Output:

Level 0 → A
Level 1 → B C
Level 2 → D E F
Version 3
BFS + Count

Output:

A B C D E F
Total count = 6
Later version
BFS + return total node count

Output includes:

Total Number of Node, 6

The file repeats these versions again under the "Prabhu sir code" section.

33. One very important tracing diagram

For your graph:

                  A
                /   \
               B     C
              / \     \
             D   E     F

Think of the queue as a waiting line.

Start
Queue
[A]
A comes out
[A] → remove A

Queue:
[]

A sends B and C:

[B,C]
B comes out
[B,C] → remove B

Queue:
[C]

B sends D and E:

[C,D,E]
C comes out
[C,D,E] → remove C

Queue:
[D,E]

C sends F:

[D,E,F]
D comes out
[D,E,F] → D

Queue:
[E,F]
E comes out
[E,F] → E

Queue:
[F]
F comes out
[F] → F

Queue:
[]

Queue empty → STOP

34. The most important 5 lines of BFS

If you remember only these lines, remember:

s=set()

queue=deque()

s.add(start)

queue.append(start)

while queue:

And inside:

new=queue.popleft()

for i in self.graph[new]:

    if i not in s:

        s.add(i)

        queue.append(i)
In simple English:
1. Create visited list
2. Create queue
3. Mark starting node visited
4. Put starting node in queue
5. Until queue becomes empty:
      Remove first node
      Print it
      Find its neighbours
      If neighbour is new:
          Mark visited
          Put it into queue
35. Super-simple real-life example

Imagine students standing in a line.

A
↓
B C
↓
D E F

BFS says:

First meet A.

Then:

Meet everyone directly connected to A → B and C.

Then:

Meet everyone connected to B and C → D, E and F.

So:

A → B → C → D → E → F

The queue is the waiting line.

The set is your notebook saying:

"I have already met this person."

36. Exam-ready definitions
BFS

Breadth First Search (BFS) is a graph traversal technique that visits nodes level by level, starting from a given node. It uses a queue to process nodes in FIFO order.

Queue

A queue follows FIFO — First In First Out.

Set

A set is used in BFS to keep track of already visited nodes and avoid visiting the same node again.

append()
queue.append(x)

Adds x at the end of the queue.

popleft()
queue.popleft()

Removes the first element from the queue.

level

level keeps track of which level of the graph we are currently processing.

count

count stores the number of nodes processed during BFS.

37. Final memory trick

Remember BFS as:

BFS
 ↓
QUEUE
 ↓
FIFO
 ↓
LEVEL BY LEVEL

And the complete flow:

START
  ↓
PUT START IN QUEUE
  ↓
REMOVE FIRST NODE
  ↓
PRINT NODE
  ↓
CHECK ITS NEIGHBOURS
  ↓
IF NOT VISITED
  ↓
MARK VISITED
  ↓
PUT IN QUEUE
  ↓
QUEUE EMPTY?
  ↓
NO ─────→ Repeat
  ↓
YES
  ↓
STOP

One-line shortcut for exams:

BFS uses a Queue and visits the graph level by level, while a Set keeps track of already visited nodes.

'''

print()

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_nodes(self, nodes):
        self.graph[nodes] = []

    def add_edges(self, n1, n2):
        self.graph[n1].append(n2)

    def BFS(self, start):

        s = set()              # visited nodes
        queue = deque()        # BFS queue

        s.add(start)           # {A}
        queue.append(start)    # [A]

        while queue:

            new = queue.popleft()

            print(new, end=" ")

            for i in self.graph[new]:

                if i not in s:

                    s.add(i)

                    queue.append(i)


g = Graph()

g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")

g.add_edges("A", "B")
g.add_edges("A", "D")

g.add_edges("B", "A")
g.add_edges("B", "C")

g.add_edges("C", "B")
g.add_edges("C", "D")

g.add_edges("D", "C")
g.add_edges("D", "A")

g.BFS("A")

# ----------------------------------------------------------------------------------------------------------------------------

''' 
# DFS ---- DEPTH FIRST SEARCH




'''

from collections import deque
class graph:
    def __init__(self):
        self.graph={}

    def add_node(self,node):
        self.graph[node]=[]

    def add_edges(self, n1, n2):
        self.graph[n1].append(n2)


    def level_and_nodes(self, start, Target):
        queue=deque(start)
        level=0
        while queue:
            if level == Target:
                print(list(queue))
                return len(queue)

            for i in range(len(queue)):             #len(queue)=1 ---> here 1 is excluded ---> result ---> 0 level
                node=queue.popleft()
                for i in self.graph[node]:
                     queue.append(i)
            level=level+1
            
        return 0
        


g=graph()

g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_node("F")
g.add_node("G")
g.add_node("H")

g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C", "F")
g.add_edges("C", "G")

g.add_edges("D","H")

print(g.graph)

print("----------------------LEVEL 0--------------------------------------------")
print(g.level_and_nodes("A", 0))
# ['A']
# 1

print("----------------------LEVEL 1--------------------------------------------")
print(g.level_and_nodes("A", 1))
# ['B', 'C']
# 2

print("----------------------LEVEL 2--------------------------------------------")
print(g.level_and_nodes("A", 2))
# ['D', 'E', 'F', 'G']
# 4

print("----------------------LEVEL 3--------------------------------------------")
print(g.level_and_nodes("A", 3))
# ['H']
# 1

print(" -------------------------------------NEW---------------------------------------------")

''' 
from collections import deque
# deque = Double Ended Queue
# It allows us to add/remove elements from both ends.
# Here, we use it as a QUEUE for BFS.


class graph:
    # Creating a class named graph

    def __init__(self):
        # Constructor
        # It runs automatically when an object of the class is created.

        self.graph = {}
        # Creating an empty dictionary.
        #
        # We will store the graph like this:
        #
        # {
        #   "A": ["B", "C"],
        #   "B": ["D", "E"],
        #   "C": ["F", "G"],
        #   "D": ["H"],
        #   "E": [],
        #   "F": [],
        #   "G": [],
        #   "H": []
        # }


    def add_node(self, node):
        # Function used to add a node into the graph.

        self.graph[node] = []
        # Create the node as a key in dictionary.
        # Initially, it has no connected nodes.
        #
        # Example:
        # add_node("A")
        #
        # becomes:
        # {"A": []}


    def add_edges(self, n1, n2):
        # Function used to connect two nodes.
        #
        # n1 = starting node
        # n2 = destination node

        self.graph[n1].append(n2)
        # Add n2 into the list of n1.
        #
        # Example:
        # add_edges("A", "B")
        #
        # means:
        # A ---> B
        #
        # Dictionary becomes:
        # {"A": ["B"]}


    def level_and_nodes(self, start, Target):
        # This function finds all nodes present at a particular level.
        #
        # start  = starting node
        # Target = level that we want to find

        queue = deque(start)
        # Create a queue.
        #
        # If start = "A"
        #
        # deque("A")
        #
        # becomes:
        # deque(['A'])

        level = 0
        # Starting node is always considered LEVEL 0.


        while queue:
            # Continue the loop while queue is NOT empty.


            if level == Target:
                # Check whether current level is the level requested by user.

                print(list(queue))
                # Convert deque into a normal list and print it.
                #
                # Example:
                # deque(['B', 'C'])
                #
                # becomes:
                # ['B', 'C']

                return len(queue)
                # Return number of nodes at this level.
                #
                # ['B', 'C'] contains 2 nodes
                # Therefore return 2.


            for i in range(len(queue)):
                # Process ONLY the nodes currently present in the queue.
                #
                # VERY IMPORTANT:
                #
                # len(queue) tells us how many nodes are
                # currently present at this level.
                #
                # Example:
                # queue = ['B', 'C']
                # len(queue) = 2
                #
                # range(2) gives:
                # 0, 1
                #
                # So the loop executes 2 times.


                node = queue.popleft()
                # Remove the FIRST node from the queue.
                #
                # FIFO:
                # First In → First Out
                #
                # Example:
                # queue = ['B', 'C']
                #
                # popleft() removes B
                #
                # node = B
                # queue = ['C']


                for i in self.graph[node]:
                    # Visit every neighbour/child of the current node.
                    #
                    # Example:
                    # node = B
                    # self.graph["B"] = ["D", "E"]
                    #
                    # So this loop processes D and E.

                    queue.append(i)
                    # Add the neighbour to the END of the queue.
                    #
                    # Example:
                    # queue = ['C']
                    #
                    # append D:
                    # queue = ['C', 'D']
                    #
                    # append E:
                    # queue = ['C', 'D', 'E']


            level = level + 1
            # After processing ALL nodes of the current level,
            # move to the next level.
            #
            # Example:
            # level = 0
            # becomes:
            # level = 1


        return 0
        # If the requested level doesn't exist,
        # return 0.

'''

# FIND OUT SHORTEST PATH 


from collections import deque
class graph:
    def __init__(self):
        self.graph={}

    def add_node(self,node):
        self.graph[node]=[]

    def add_edges(self, n1, n2):
        self.graph[n1].append(n2)


    def level_and_Path(self, start, Path):
        queue=deque(start)
        level=0
        while queue:
            for i in range(len(queue)):                 # len (queue) = 1 (excluded) ----> level 0
                node=queue.popleft()
                if node == Path:                        # Path -----> level = 1 
                    return level
                for i in self.graph[node]:
                    queue.append(i)
            level=level+1

        return 0



g=graph()

g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_node("F")
g.add_node("G")
g.add_node("H")

g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("C", "F")
g.add_edges("C", "G")
g.add_edges("D","H")

print(g.graph)

print("_____________________________________________________________________________")
print()

print(g.level_and_Path("A","H"))              # ------> 3

print("_____________________________________________________________________________")
print()

print(g.level_and_Path("A","D"))              # ------> 2

print("_____________________________________________________________________________")
print()

print(g.level_and_Path("A","B"))              # ------> 1

print("_____________________________________________________________________________")
print()

print(g.level_and_Path("A","P"))              # ------> 0


print("_____________________________________________________________________________")
print()

# -----------------------------------------------------------------------------------------------------------------------------------


# | Feature                           | BFS                                 | DFS                                 |
# | --------------------------------- | ----------------------------------- | ----------------------------------- |
# | Full form                         | Breadth First Search                | Depth First Search                  |
# | Approach                          | Level by level                      | Depth first                         |
# | Data structure                    | Queue                               | Stack                               |
# | Queue/Stack rule                  | FIFO                                | LIFO                                |
# | Goes                              | Wide first                          | Deep first                          |
# | Shortest path in unweighted graph | ✅ Yes                               | ❌ Not guaranteed                    |
# | Memory                            | Can use more memory for wide graphs | Can use less for some graphs        |
# | Common use                        | Shortest path, level order          | Backtracking, maze, cycle detection |
# | Tree traversal                    | Level Order                         |Check all levels at left side then come back and check right back  |
# | Tree traversal                    | Level Order                         | Preorder/Inorder/Postorder          |


# ------------------------------------------------------------------------------------------------------------------------------

# BFS and Shortest Path
# A → B → D → H

# &

# A → C → F → G

# ---------------------------------------------------------------------------------------------------------------------------------------

# BFS searches:

# Level 0: A

# Level 1: B, C

# Level 2: D, F, E, G

# Level 3: H

# BFS vs DFS in One Diagram

#                     A
#                   /   \
#                  B     C
#                 / \   / \
#                D   E F   G
#               /
#              H
# ------------------------------------------------------------------------------------------------------------
# BFS:
# A
# ↓
# B C
# ↓
# D E F G
# ↓
# H

# Level → Level → Level

# --------------------------------------------------------------------------------------------------------------------
# DFS:
# A
# ↓
# B
# ↓
# D
# ↓
# H

# Then backtrack:

# H
# ↑
# D
# ↑
# B
# ↓
# E

# Then continue with C.

# Deep → Backtrack → Deep → Backtrack
# --------------------------------------------------------------------------------------------------------------------------------


# BFS → LEVEL BY LEVEL → QUEUE → FIFO
# DFS → DEPTH FIRST → STACK/RECURSION → LIFO

# --------------------------------------------------------------------------------------------------------------------------------

#  DFS 

class Graph:
    def __init__(self):
        self.graph={}


    def Add_Nodes(self,Nodes):
        self.graph[Nodes]=[]

    def Add_Edges(self, N1, N2):
        self.graph[N1].append(N2)

    def DFS(self, start):
        stack=[start]        # A
        visited=set()        # empty set 
        while stack:               # while [A]       -----> true A is present inside the stack
            new=stack.pop()       # node=[A].pop()  
            if new in visited:    # A in set () ---------> false
                continue          # skip the current iterration 
            visited.add(new)      # {A}
            print(new, end=" ")

            for i in self.graph[new]:     # Search neighbour element  ---> i in A----> A : ['B', 'C']
                stack.append(i)           # appened ['B', 'C']


g=Graph()

g.Add_Nodes("A")
g.Add_Nodes("B")
g.Add_Nodes("C")
g.Add_Nodes("D")
g.Add_Nodes("E")
g.Add_Nodes("F")


g.Add_Edges("A","B")
g.Add_Edges("A","C")
g.Add_Edges("B","D")
g.Add_Edges("B","E")
g.Add_Edges("D","F")

print(g.graph)       # o/p----> {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': [], 'D': ['F'], 'E': [], 'F': []}


g.DFS("A")           # o/p ----> A C B E D F 

'''

def DFS(self, start):
        stack=[start]        # A
        visited=set()        # empty set 
        while stack:               # while [A]       -----> true A is present inside the stack
            new=stack.pop()       # node=[A].pop()  
            if new in visited:    # A in set () ---------> false ----> SET () IS EMPTY
                continue          # skip the current iterration 
            visited.add(new)      # {A}
            print(new, end=" ")   # A

            for i in self.graph[new]:     # Search neighbour element  ---> i in A----> A : ['B', 'C']
                stack.append(i)           # appened ['B', 'C']

                
def DFS(self, start):
        stack=[start]        # [B, C]
        visited=set()        # {A} 
        while stack:               # while [B, C]       -----> true [B,C] is present inside the stack
            new=stack.pop()       # node=[B, C].pop()
            # new = c  
            if new in visited:    # [B,C] in set () ---------> false
                continue          # skip the current iterration 
            visited.add(new)      # {A, C}
            print(new, end=" ")    # C

            for i in self.graph[new]:     # Search neighbour element  ---> i in A----> A : ['B', 'C']
                stack.append(i)           # appened ['B', 'C']

def DFS(self, start):
        stack=[start]        # [B]
        visited=set()        # {A, C} 
        while stack:               # while [B]       -----> true [B] is present inside the stack
            new=stack.pop()       # node=[B].pop()
            # new = B 
            if new in visited:    # [B] in set () ---------> false
                continue          # skip the current iterration 
            visited.add(new)      # {A, C, B}
            print(new, end=" ")    # B

            for i in self.graph[new]:     # Search neighbour element  ---> i in B----> B : ['D', 'E']
                stack.append(i)           # appened B : ['D', 'E']


def DFS(self, start):
        stack=[start]        # [D,E]
        visited=set()        # {A, C, B} 
        while stack:               # while [D,E]      -----> true [D, E] is present inside the stack
            new=stack.pop()       # node=[D,E].pop()
            # new = E 
            if new in visited:    # E in set () ---------> false
                continue          # skip the current iterration 
            visited.add(new)      # {A, C, B, E}
            print(new, end=" ")    # E

            for i in self.graph[new]:     # Search neighbour element  ---> i in E----> E : [] ---> E IS EMPTY 
                stack.append(i)           # E : []

def DFS(self, start):
        stack=[start]        # [D]
        visited=set()        # {A, C, B, E} 
        while stack:               # while [D]      -----> true [D] is present inside the stack
            new=stack.pop()       # node=[D].pop()
            # new = D 
            if new in visited:    # D in set () ---------> false
                continue          # skip the current iterration 
            visited.add(new)      # {A, C, B, E, D}
            print(new, end=" ")    # D

            for i in self.graph[new]:     # Search neighbour element  ---> i in D----> D : [F] 
                stack.append(i)            # [F]      

def DFS(self, start):
        stack=[start]        # [F]
        visited=set()        # {A, C, B, E, D} 
        while stack:               # while [F]      -----> true [F] is present inside the stack
            new=stack.pop()       # node=[F].pop()
            # new = F 
            if new in visited:    # F in set () ---------> false
                continue          # skip the current iterration 
            visited.add(new)      # {A, C, B, E, D, F}
            print(new, end=" ")    # F

            for i in self.graph[new]:     # Search neighbour element  ---> i in F----> F : [] 
                stack.append(i)            # F: []     
'''

# DFS = Depth First Search
# DFS goes as deep as possible before coming back.
# We use STACK to implement DFS.

# class Graph:

#     def __init__(self):
#         # Create an empty dictionary.
#         # Dictionary will store each node and its neighbours.
#         self.graph = {}


#     def Add_Nodes(self, Nodes):
#         # Add a node to the graph.
#         # Initially, this node has no neighbours.
#         self.graph[Nodes] = []


#     def Add_Edges(self, N1, N2):
#         # Add N2 as a neighbour of N1.
#         # Example: Add_Edges("A", "B")
#         # means A is connected to B.
#         self.graph[N1].append(N2)


#     def DFS(self, start):

#         # Create a stack and put the starting node inside it.
#         # Initially: stack = [A]
#         stack = [start]

#         # Create an empty set.
#         # It will store nodes that we have already visited.
#         visited = set()

#         # Continue until the stack becomes empty.
#         while stack:

#             # Remove the LAST element from the stack.
#             # pop() removes the last element.
#             new = stack.pop()

#             # Check whether this node was already visited.
#             if new in visited:

#                 # If already visited, skip this iteration.
#                 continue

#             # Add the current node to visited.
#             visited.add(new)

#             # Print the current node.
#             print(new, end=" ")

#             # Find all neighbours of the current node.
#             for i in self.graph[new]:

#                 # Add each neighbour to the stack.
#                 stack.append(i)


# # Create an object of Graph class.
# g = Graph()


# # Add nodes.
# g.Add_Nodes("A")
# g.Add_Nodes("B")
# g.Add_Nodes("C")
# g.Add_Nodes("D")
# g.Add_Nodes("E")
# g.Add_Nodes("F")


# # Add edges.
# g.Add_Edges("A", "B")
# g.Add_Edges("A", "C")
# g.Add_Edges("B", "D")
# g.Add_Edges("B", "E")
# g.Add_Edges("D", "F")


# # Display the graph.
# print(g.graph)

# # Start DFS from A.
# g.DFS("A")

''' 

Understanding the Graph First

After these statements:

g.Add_Edges("A","B")
g.Add_Edges("A","C")
g.Add_Edges("B","D")
g.Add_Edges("B","E")
g.Add_Edges("D","F")

The graph becomes:

        A
       / \
      B   C
     / \
    D   E
    |
    F

The dictionary is:

{
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': ['F'],
    'E': [],
    'F': []
}
Meaning:
A → B, C
B → D, E
C → nothing
D → F
E → nothing
F → nothing
3. Most Important Concept: STACK

Your DFS uses:

stack = [start]

A stack follows:

LIFO = Last In, First Out

Think of a pile of plates:

   C    ← comes out first
   B
   A

If we do:

stack.append("B")
stack.append("C")

we get:

[B, C]

Then:

stack.pop()

removes C.

So:

[B, C]
    ↑
   POP

C comes out

This is the main reason your DFS gives:

A C B E D F

instead of:

A B C D E F

-----> 4. DFS TRACING STEP-BY-STEP

Let's start:

g.DFS("A")

-----> STEP 1 — DFS starts

This line executes:

stack = [start]

Since:

start = "A"

we get:

STACK   = [A]
VISITED = {}

Then:

while stack:

Is stack empty?

[A]

No.

Therefore:

while stack → TRUE

-----> STEP 2 — pop()

This line:

new = stack.pop()

Stack:

[A]

pop() removes A.

Therefore:

new = A
stack = []

Now:

if new in visited:

means:

Is A inside visited?

Currently:

visited = {}

So:

A in {} → FALSE

Therefore continue is NOT executed.

-----> STEP 3 — Add A to visited
visited.add(new)

Since:

new = A

we get:

visited = {A}

Then:

print(new, end=" ")

Output:

A

Current situation:

STACK   = []
VISITED = {A}

OUTPUT = A

-----> 5. Find A's Neighbours

Now this loop executes:

for i in self.graph[new]:

Since:

new = A

we look at:

self.graph["A"]

which is:

['B', 'C']

So:

A has two neighbours:

B
C
Add B

First:

i = B

Then:

stack.append(B)

Stack becomes:

[B]
Add C

Next:

i = C

Then:

stack.append(C)

Stack becomes:

[B, C]

So after processing A:

STACK   = [B, C]
VISITED = {A}

OUTPUT = A
Very important:

Although B was added first, C is at the top of the stack.

[B, C]
    ↑
    |
   TOP

Therefore C will come out first.

-----> 6. STEP 4 — C Comes Out

Again:

while stack:

Stack:

[B, C]

Not empty.

Therefore:

TRUE

Now:

new = stack.pop()

pop() removes C.

new = C
stack = [B]

Check:

if C in visited:

Visited:

{A}

Therefore:

C in {A} → FALSE

Add C:

visited.add(C)

Now:

visited = {A, C}

Print:

C

Output:

A C

-----> 7. Check C's Neighbours

This line:

for i in self.graph[new]:

Here:

new = C

So:

self.graph["C"]

is:

[]

C has no neighbours.

Therefore nothing is appended.

Stack remains:

[B]

Current status:

STACK   = [B]
VISITED = {A, C}

OUTPUT = A C

-----> 8. STEP 5 — B Comes Out

Stack:

[B]

Execute:

new = stack.pop()

Therefore:

new = B
stack = []

Check:

if B in visited:

Visited:

{A, C}

B is not there.

Therefore:

B in {A,C} → FALSE

Add B:

visited.add(B)

Now:

visited = {A, C, B}

Print B:

A C B

-----> 9. Check B's Neighbours

B has:

self.graph["B"]

which is:

['D', 'E']

First:

i = D
stack.append(D)

Stack:

[D]

Then:

i = E
stack.append(E)

Stack:

[D, E]

So:

STACK   = [D, E]
VISITED = {A, C, B}

OUTPUT = A C B

Again, E is on top.

Therefore E will come first.

-----> 10. STEP 6 — E Comes Out

Stack:

[D, E]

Execute:

new = stack.pop()

Therefore:

new = E
stack = [D]

Check:

if E in visited:

Visited:

{A, C, B}

E is not present.

So:

FALSE

Add E:

visited = {A, C, B, E}

Print E:

A C B E
E has no neighbours
self.graph["E"]

gives:

[]

Therefore:

nothing is added

Stack remains:

[D]

-----> 11. STEP 7 — D Comes Out

Stack:

[D]

Execute:

new = stack.pop()

Therefore:

new = D
stack = []

Check:

if D in visited:

Visited:

{A, C, B, E}

D is not present.

Therefore:

FALSE

Add D:

visited = {A, C, B, E, D}

Print:

A C B E D

-----> 12. Check D's Neighbour

D has:

self.graph["D"]

which gives:

['F']

Therefore:

stack.append(F)

Stack becomes:

[F]

Current:

STACK   = [F]
VISITED = {A, C, B, E, D}

OUTPUT = A C B E D

-----> 13. STEP 8 — F Comes Out

Stack:

[F]

Execute:

new = stack.pop()

Therefore:

new = F
stack = []

Check:

if F in visited:

Visited:

{A, C, B, E, D}

F is not present.

Therefore:

FALSE

Add F:

visited = {A, C, B, E, D, F}

Print F:

A C B E D F

-----> 14. F Has No Neighbours
self.graph["F"]

gives:

[]

Therefore nothing is added.

Stack remains:

[]

-----> 15. Final while Check

Now:

while stack:

But:

stack = []

An empty list is considered False in Python.

Therefore:

while [] → FALSE

The loop stops.

DFS is complete.

Final Output
A C B E D F

-----> 16. Complete Trace Table

This is the most important table for remembering the tracing:

Step	new	Stack after processing	Visited	Output
Start	—	[A]	{}	—
1	A	[B,C]	{A}	A
2	C	[B]	{A,C}	A C
3	B	[D,E]	{A,C,B}	A C B
4	E	[D]	{A,C,B,E}	A C B E
5	D	[F]	{A,C,B,E,D}	A C B E D
6	F	[]	{A,C,B,E,D,F}	A C B E D F
End	—	[]	{A,C,B,E,D,F}	A C B E D F

------> 17. Why C Comes Before B?

This is the most important question in your program.

A has:

A : ['B', 'C']

Your loop does:

for i in self.graph[new]:
    stack.append(i)

So:

First B is added
stack = [B]
Then C is added
stack = [B,C]

But:

stack.pop()

always removes the last item.

Therefore:

[B,C]
   ↑
   C comes out

So:

A → C

happens before:

A → B

That's why the output starts:

A C B

---> 18. One-Line Memory Trick

For your DFS code, remember these 5 steps:

1. PUT start node into STACK
             ↓
2. POP the last node
             ↓
3. CHECK visited
             ↓
4. ADD node to visited + PRINT
             ↓
5. ADD its neighbours to STACK
             ↓
        Repeat

In your program:

A
↓
put B,C
↓
C comes out
↓
C has nothing
↓
B comes out
↓
put D,E
↓
E comes out
↓
E has nothing
↓
D comes out
↓
put F
↓
F comes out
↓
STACK EMPTY
↓
STOP
Final DFS:
A → C → B → E → D → F

'''

print("__________________________________________________________________________________________________________________________")
print()

#  DFS 

class Graph:
    def __init__(self):
        self.graph={}


    def Add_Nodes(self,Nodes):
        self.graph[Nodes]=[]

    def Add_Edges(self, N1, N2):
        self.graph[N1].append(N2)

    def DFS(self, start):
        stack=[start]        # A
        visited=set()        # empty set 
        count=0
        while stack:               # while [A]       -----> true A is present inside the stack
            new=stack.pop()       # node=[A].pop()  
            if new in visited:    # A in set () ---------> false
                continue          # skip the current iterration 
            visited.add(new)      # {A}
            count=count+1
            # print(new, end=" ")

            for i in self.graph[new]:     # Search neighbour element  ---> i in A----> A : ['B', 'C']
                stack.append(i)           # appened ['B', 'C']

        return "Total Node Count", count


g=Graph()

g.Add_Nodes("A")
g.Add_Nodes("B")
g.Add_Nodes("C")
g.Add_Nodes("D")
g.Add_Nodes("E")
g.Add_Nodes("F")


g.Add_Edges("A","B")
g.Add_Edges("A","C")
g.Add_Edges("B","D")
g.Add_Edges("B","E")
g.Add_Edges("D","F")

print(g.graph)              # o/p----> {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': [], 'D': ['F'], 'E': [], 'F': []}

print()

print(g.DFS("A"))           # o/p ----> ('Total Node Count', 6)

print("__________________________________________________________________________________________________________________________")
print()

# FIND OUT TARGET ELEMENT 


class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)


    def DFS(self,start,Target_element):
        stack=[start]
        visited=set()
        while stack:
            new=stack.pop()
            if new in visited:
                continue
            visited.add(new)
            if new==Target_element:
                return True
            for i in self.graph[new]:
                stack.append(i)
        return False
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("D","F")
print(g.graph)                 # -----> {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': [], 'D': ['F'], 'E': [], 'F': []}
print()
print(g.DFS("A","B"))          # ----> True
print(g.DFS("A","C"))          # ----> True
print(g.DFS("A","D"))          # ----> True
print(g.DFS("A","E"))          # ----> True
print(g.DFS("A","U"))          # ----> false    





print("__________________________________________________________________________________________________________________________")
print()

# UNDIRECTED DFS 

class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def DFS(self,start,Target_element):
        stack=[start]
        visited=set()
        while stack:
            new=stack.pop()
            if new in visited:
                continue
            visited.add(new)
            if new==Target_element:
                return True
            for i in self.graph[new]:
                stack.append(i)
        return False
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("D","F")
print(g.graph)                 # -----> {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A'], 'D': ['B', 'F'], 'E': ['B'], 'F': ['D']}
print()
print(g.DFS("A","B"))          # ----> True
print(g.DFS("A","C"))          # ----> True
print(g.DFS("A","D"))          # ----> True
print(g.DFS("A","E"))          # ----> True
print(g.DFS("A","U"))          # ----> false    





print("__________________________________________________________________________________________________________________________")
print()

''' 
Q-TALK ---> 

class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def DFS(self,start):
        stack=[start]   #[F]
        visited=set()  #{A,C,B,E,D}
        while stack:  #while [F]
            node=stack.pop()  #node=[F].pop()
            #node---->F
            if node in visited: # A in set()
                continue
            visited.add(node)   #{A,C,B,E,D,F}
            print(node,end=" ")  #F
            for i in self.graph[node]:
                stack.append(i)
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("D","F")
print(g.graph)
print()
g.DFS("B")
'''

'''
class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def DFS(self,start):
        stack=[start]
        visited=set()
        count=0
        while stack:
            node=stack.pop()
            if node in visited:
                continue
            visited.add(node)
            # print(node,end=" ")
            count=count+1
            for i in self.graph[node]:
                stack.append(i)
        return "Total Node Count",count
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("D","F")
print(g.graph)
print()
print(g.DFS("A"))

'''

'''
class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)

    def DFS(self,start):
        stack=[start]   #[F]
        visited=set()  #{A,C,B,E,D}
        while stack:  #while [F]
            node=stack.pop()  #node=[F].pop()
            #node---->F
            if node in visited: # A in set()
                continue
            visited.add(node)   #{A,C,B,E,D,F}
            print(node,end=" ")  #F
            for i in self.graph[node]:
                stack.append(i)
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("D","F")
print(g.graph)
print()
g.DFS("B")
'''
'''

class Graph:
    def __init__(self):
        self.graph={}

    def add_nodes(self,nodes):
        self.graph[nodes]=[]

    def add_edges(self,n1,n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def DFS(self,start,Target_element):
        stack=[start]
        visited=set()
        while stack:
            node=stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node==Target_element:
                return True
            for i in self.graph[node]:
                stack.append(i)
        return False
g=Graph()
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_nodes("F")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("B","E")
g.add_edges("D","F")
print(g.graph)
print()
print(g.DFS("A","B"))

'''

# UNDIRECTED---->

# A<----10---->B
# ^            ^ 
# |            |
# 40          20
# |            |
# ^            ^
# D<----30---->C

# ============================================================
#          UNDIRECTED GRAPH + DFS
# ============================================================

# Graph:
#
#          10
#     A <-------> B
#     ^           ^
#     |           |
#   40|           |20
#     |           |
#     D <-------> C
#          30
#
# A <----> B = 10
# B <----> C = 20
# C <----> D = 30
# D <----> A = 40


class Graph:

    def __init__(self):
        # Empty dictionary to store the graph
        self.graph = {}


    def Add_Nodes(self, node):
        # Add a node to the graph
        # Initially, node has no neighbours
        self.graph[node] = []


    def Add_Edges(self, N1, N2, weight):
        # Because this is an UNDIRECTED graph,
        # we have to add the connection in BOTH directions.

        # N1 -> N2
        self.graph[N1].append((N2, weight))

        # N2 -> N1
        self.graph[N2].append((N1, weight))


    def DFS(self, start):

        # Create a stack.
        # Start node is placed inside the stack.
        stack = [start]

        # Empty set to keep track of visited nodes.
        visited = set()

        # Continue until stack becomes empty.
        while stack:

            # Remove the LAST element from stack.
            new = stack.pop()

            # If node is already visited,
            # skip it.
            if new in visited:
                continue

            # Add node to visited set.
            visited.add(new)

            # Print the current node.
            print(new, end=" ")

            # Visit all neighbours of current node.
            for neighbour, weight in self.graph[new]:

                # Add only the neighbour to stack.
                # Weight is not required for DFS traversal.
                if neighbour not in visited:
                    stack.append(neighbour)


# ============================================================
# CREATE GRAPH
# ============================================================

g = Graph()


# Add nodes
g.Add_Nodes("A")
g.Add_Nodes("B")
g.Add_Nodes("C")
g.Add_Nodes("D")


# Add UNDIRECTED edges
g.Add_Edges("A", "B", 10)
g.Add_Edges("B", "C", 20)
g.Add_Edges("C", "D", 30)
g.Add_Edges("D", "A", 40)


# Display graph
print("GRAPH-->")
print(g.graph)        # ----> {'A': [('B', 10), ('D', 40)], 'B': [('A', 10), ('C', 20)], 'C': [('B', 20), ('D', 30)], 'D': [('C', 30), ('A', 40)]}


# ============================================================
# DFS
# ============================================================

print()
print("DFS TRAVERSAL")      # -----> A D C B

g.DFS("A")


print("____________________________________________________________________________________________________________________")
print()

# searching 

def Search(self, start, target):

    # Stack contains the starting node
    stack = [start]

    # Set to remember already visited nodes
    visited = set()

    # Continue while stack is not empty
    while stack:

        # Remove the last element
        new = stack.pop()

        # If already visited, skip it
        if new in visited:
            continue

        # Mark the node as visited
        visited.add(new)

        # Check whether current node is target
        if new == target:
            return True

        # Add neighbours to stack
        for neighbour, weight in self.graph[new]:

            # Add only unvisited neighbours
            if neighbour not in visited:
                stack.append(neighbour)

    # Target was not found
    return False


g = Graph()


# Add nodes
g.Add_Nodes("A")
g.Add_Nodes("B")
g.Add_Nodes("C")
g.Add_Nodes("D")


# Add UNDIRECTED edges
g.Add_Edges("A", "B", 10)
g.Add_Edges("B", "C", 20)
g.Add_Edges("C", "D", 30)
g.Add_Edges("D", "A", 40)


# Display graph
print("GRAPH")
print(g.graph)                  # ----> {'A': [('B', 10), ('D', 40)], 'B': [('A', 10), ('C', 20)], 'C': [('B', 20), ('D', 30)], 'D': [('C', 30), ('A', 40)]}



print("_-------------------------------------------------------------------------_")
print()


class Graph:

    def __init__(self):
        self.graph = {}


    def Add_Nodes(self, node):
        # Add node with an empty neighbour list
        self.graph[node] = []


    def Add_Edges(self, N1, N2, weight):

        # Undirected graph
        # N1 → N2
        self.graph[N1].append((N2, weight))

        # N2 → N1
        self.graph[N2].append((N1, weight))


    def Number_Of_Elements(self):

        # Count total number of nodes
        return len(self.graph)


    def Search(self, start, target):

        # Start DFS using stack
        stack = [start]

        # Empty visited set
        visited = set()

        while stack:

            # Remove last node
            new = stack.pop()

            # If already visited, skip
            if new in visited:
                continue

            # Mark as visited
            visited.add(new)

            # Check target
            if new == target:
                return True

            # Add neighbours
            for neighbour, weight in self.graph[new]:

                if neighbour not in visited:
                    stack.append(neighbour)

        # Target not found
        return False


# Create Graph
g = Graph()


# Add Nodes
g.Add_Nodes("A")
g.Add_Nodes("B")
g.Add_Nodes("C")
g.Add_Nodes("D")


# Add Edges
g.Add_Edges("A", "B", 10)
g.Add_Edges("B", "C", 20)
g.Add_Edges("C", "D", 30)
g.Add_Edges("D", "A", 40)


# Number of elements
print("NUMBER OF ELEMENTS --->", g.Number_Of_Elements())    # ----> NUMBER OF ELEMENTS ---> 4


# Searching
print("SEARCH C --->", g.Search("A", "C"))  # ---> SEARCH C ---> True
print("SEARCH D --->", g.Search("A", "D"))  # ---> SEARCH D ---> True
print("SEARCH E --->", g.Search("A", "E"))  # ---> SEARCH E ---> False