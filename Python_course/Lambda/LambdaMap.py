'''
MAP
----

-map is inbuilt function
-without using for loop, instead of doing the same operations again and again we use map function
-it will act same as the for loop

-We can execute map function by two ways--->
1.Function
2. Lambda


using function:
syntax-->def function_name(parameter):
            statement
        newvar=map(function_name,iterable1.itr2)     --->it will take one by one element from iterable and will give the o/p
        print(newvar) ------------------------------------>map object address
        #to avoid object address two ways --->looping and typecasting
        #looping
        for var in newvar:
            print(var)
        #typecasting
        print(list(newvar))

using lambda
syntax------>newvar=lambda arg1,arg2:expression
            print(map(newvar,arg1,arg2))----->map object address
            #to avoid obj address 
            #1.typecasting
            print(list(map(newvar,arg1,arg2)))---->we can pass n no. of iterable but the length of them should be same
                                                    (or data loss will be happen)

'''
#ex1
def demo():
    print("demo class")
x=map(demo,[1,2,3])
print(x)  #<map object at 0x000001DA74BA1BD0>

#ex   normal looping
x=[1,2,3,4]
a=[]
for i in x:
    a.append(i**2)
print(a)
print()

#using function--->don't use for loop because we are avoiding for loop in map function....go for typecasting
x=[1,2,3,4]
def Square(x):
    return x**2
q=map(Square,x)
print(q)   #<map object at 0x000001E1951F1F00>
#to avoid obj address go for typecasting
print(list(q))  #[1, 4, 9, 16]
print()

#using lambda
q=lambda x:x**2
print(list(map(q,[1,2,3,4])))

#ex2 convert [1,2,3,4,5] all the elements to float
#using function
s=[1,2,3,4,5]
def Data(s):
    return float(s)
w=map(Data,s)
print(list(w))   #[1.0, 2.0, 3.0, 4.0, 5.0]

#using lambda
s=[1,2,3,4,5]
x=lambda s:float(s)
print(list(map(x,s)))
print()

#ex3. convert string elemets to integer in list
y=['1','2']
def Data(y):
    return int(y)
w=map(Data,y)
print(list(w))  #[1, 2]
print()

#using lambda
q=lambda s:int(s)
print(list(map(q,['1','2','3']))) #[1, 2, 3]
print()

#ex4. replace -ve no. with 0
x=[1,-4,6,-7,8,-23]
def Replace(x):
    if x<0:
        return 0
    else:
        return x
w=map(Replace,x)
print(list(w))  #[1, 0, 6, 0, 8, 0]
print()

#using lambda
x=[1,-4,5,-7,89,-23]
q=lambda a:0 if a<0 else a
print(list(map(q,x)))
print()

#ex5 check if a is +ve or -ve
#function
x=[-5,10,-6,7]
def Check(x):
    if x>0:
        return 'positive no.'
    else:
        return 'negative no.'
w=map(Check,x)
print(list(w))

#lambda
w=lambda a:'positive' if a>0 else 'negative'
print(list(map(w,[1,-4,50,-4,55])))

#ex5 add 1 to all elemets
#1.Add 1 to all elements
a=[1,2,3,4]
def Add(a):
    return a+1
w=map(Add,a)
print(list(w))  #[2, 3, 4, 5]

#2.Add 5 to all numbers
b=[10,15,20]

#3.Square all numbers
c=[4,5,6,7]

#4.Cube all numbers
d=[2,3,4]

#5.Convert all integers to float
e=[1,2,3,4]

#6.Convert all floats to integers
y=[1.2,4.5,7.7,9.8]
def Convert(y):
    return int(y)
z=map(Convert,y)
print(list(z))  #[1, 4, 7, 9]

#7.Convert all strings to integers
k=["10", "20", "30"]

#8.Convert all strings to uppercase
z=["python", "java","sql","powerbi"]
def Convert(z):
    return z.upper()
w=map(Convert,z)
print(list(w))  #['PYTHON', 'JAVA', 'SQL', 'POWERBI']

#9.Convert all strings to lowercase
y=["PYTHON", "JAVA"]
def Convert(y):
    return y.lower()
w=map(Convert,y)
print(list(w))  #['python', 'java']

#10.Find length of each word
a=["apple", "banana", "cherry"]
def Length(a):
    return len(a)
x=map(Length,a)
print(list(x))  #[5, 6, 6]

#11.Multiply all elements by 2
k=[1,2,3,4,5]
def Multiply(k):
    return k*2
w=map(Multiply,k)
print(list(w))    #[2, 4, 6, 8, 10]

#12.Multiply all elements by 10
n=[1, 2, 3]
def Multiply(n):
    return n*10
w=map(Multiply,n)
print(list(w))  #[10, 20, 30]

#13.Convert numbers to strings
b=[1, 2, 3]
def Convert(b):
    return str(b)
z=map(Convert,b)
print(list(z))  #['1', '2', '3']

#14.Get absolute values of numbers
a=[-5, -10, 15]
def Convert(a):
    return abs(a)
z=map(Convert,a)
print(list(z))  #[5, 10, 15]

#15.Round off decimal numbers
data = [1.2, 2.6, 3.5]
def Convert(data):
    return round(data)
z=map(Convert,data)
print(list(z))  #[1, 3, 4]

#16,Check if each number is even or odd
s=[1,2,3,4,5]
def Check(s):
    if s%2==0:
        return 'even'
    else:
        return 'odd'
w=map(Check,s)
print(list(w))  #['odd', 'even', 'odd', 'even', 'odd']

#17.Check if number is positive or negative
a=[-5, 10, -3, 7]

def Check(a):
    return "+ve" if a>0 else "-ve"
w=map(Check,a)
print(list(w))


#18.Replace negative numbers with 0
x=[1,-4,6,-9,8,-23]
def Data(x):
    return x if x>0 else 0
e=map(Data,x)
print(list(e)) #[1, 0, 6, 0, 8, 0]



#19.Replace even numbers with 100
y=[1,2,3,4,5,6]
def Replace(y):
    if y%2==0:
        return 100
    else:
        return y
w=map(Replace,y)
print(list(w))   #[1, 100, 3, 100, 5, 100]



#20.Add prefix "Mr." to each name
names = ["John", "Rahul"]
def Prefix(names):
    return "Mr."+names
w=map(Prefix,names)
print(list(w))  #['Mr.John', 'Mr.Rahul']


#21.Add suffix "_done" to each word
words = ["task1", "task2"]
def Suffix(words):
    return words + "_done"
w=map(Suffix,words)
print(list(w))  #['task1_done', 'task2_done']

#22
a=[1,2,3,4,5]
b=[1,2,3,4,5]
d=lambda a,b:a+b
print(list(map(d,a,b)))  #[2, 4, 6, 8, 10]

def data(a,b):
    return a+b
w=map(data,a,b)
print(list(w))    #[2, 4, 6, 8, 10]


