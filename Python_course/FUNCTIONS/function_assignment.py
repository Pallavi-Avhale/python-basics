'''#1. wap to iterate over a string in reverse direction
str1=input('enter a string:')
def reverse_str(str1):
    for i in str1[::-1]:
        print(i,end=" ")
reverse_str(str1)
# o/p:enter a string:'divya'
# ' a y v i d ' 


print()


#2. wap to print index as well as character of the string 
st=input('enter a string: ')
def index(st):
    for i in enumerate(st):
        print(i,end=" ")
index(st)
# enter a string: Divya
# (0, 'D') (1, 'i') (2, 'v') (3, 'y') (4, 'a')

print()

#3. wap to print fibonacci series
def fibonacci(n):
    n1=0
    n2=1
    for i in range(n):
        print(n1,end=" ")
        b=n1+n2
        n1=n2
        n2=b
    print(f'{n}th fibonacci value is {n1}' )
a=int(input('enter a no. '))
fibonacci(a)

#4. armstrong no.
def armstrong_no():
    n=153
    res=n
    l=len(str(n))
    sum=0
    while n!=0:
        rem=n%10
        sum+=rem**l
        n=n//10
    print(sum)
    if res==sum:
        print('armstrong no.')
    else:
        print('not a armstrong no. ')
armstrong_no()

print()

# 5.wap to check how many words are present in the given sentence
def word_count():
    s='helooo hiii'
    total=0
    for i in s.split():
        total=total+1
    print(f'Total no. of words are {total}')
word_count()

print()

#6. finding the len of string
st="Divya"
def Length(s):
    cnt=0
    for i in s:
        cnt+=1
    print(cnt)
Length(st)'''

'''assignment2'''
'''
# 1.write a function to print the below output
# func("TRACXN",1)
# #should print RCN

def funcs(s):
    print(s[1::2])

funcs("TRACXN")

# 2.write a function to print the below output
# func("TRACXN",0)
# #should print TAX

def func(s):
    print(s[::2])
func("TRACXN")

# 3.A function take variable number of positional arguments
#    as input. how to check if the arguments are more than 5.

def num(a):
    if a>5:
        return "more than 5"
print(num(10))    

or 

def checklen(*args):
    if len(args)>5:
        print('arguments are more than 5')
checklen(55,66,77,54,32,12)

# 4.Write a Function to reverse any iterable without using reverse function:
def rev(a):
    r=''
    for i in a:
        r=i+r
    print(r)
rev("ram")

# 5.write a function to return a dictionary with characters and ascii value pair:
def char(a):
    result = {}
    for i in a:
        result[i] = ord(i)
    return result
print(char("shyam"))'''

# 6.write a function to reverse a iterable if you are passing string or list or tuple else print type of the data:

input=eval(input("enter the type of function"))
def func(a):
    if type(a) in (str,list,tuple):
        return a[::-1]
    else:
        return type(a) 
print(func(input))








