# 1.add two numbers
x=lambda a,b:a+b
print("sum of two no. is :")
print(x(2,2))
print()

# 2.multiply two numbers
x=lambda a,b:a*b
print("multiplication of a and b is :")
print(x(3,3))
print()

# 3.find maximum of two numbers
x=lambda a,b:a if a>b else b
print(x(20,30))
print()

# 4.find minimum of two numbers
x=lambda a,b:a if a<b else b
print(x(30,20))
print()

# 5.square of a numbers
x=lambda a:a**2
print("square of a is :")
print(x(8))

# 6.cube of a numbers
x=lambda b: b**3
print("cube of b is :")
print(x(3))

# 7.check even number
x=lambda a: "even" if a%2==0 else "odd"
print("check even or odd")
print(x(212))
print()

# 8.Absolute value
x=lambda a:abs(a)
print("absolute value of a is")
print(x(-8))
print()

# 9.greater among three numbers
# a=10
# b=20
# c=30
x=lambda a,b,c:a if a>b and a>c else (b if b>c else c)
print(x(10,20,30))

# 10.length of a string
x=lambda s:len(s)
print("length of string is:")
print(x("Hello"))

# 11.Reverse a string
x=lambda s:s[::-1]
print("reverse of string is:")
print(x("hiii"))

# 12.Palindrome check
x=lambda a:"palindrome" if a==a[::-1] else "Not palindrome"
print(x("level"))

# find largest word in a string

s = "python is powerful"
x = lambda s: max(s.split(), key=len)
print(x(s))

# 14.Last digit of a number
s=789
x=lambda s:s%10
print(x(789))

# 15.First digit of a number
s=78
x=lambda s:int(str(s)[0])
print(x(s))

#MAP
# 1.#wap to square of the number
num=[1,2,3,4,5]
def Square(num):
    return num**2
x=map(Square,num)
print(list(x))

# 2.#wap to merge two list
a=[1,2,3]
b=[4,5,6]
def Merge(a,b):
    return a+b
x=map(lambda x:x,a+b)
print(list(x))

#3. wap to convert number to string
x=[10,20,30,40]
def Fun(x):
    return str(x)
y=map(Fun,x)
print(list(y))
