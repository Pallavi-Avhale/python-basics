print("hello.","this is my first program")
print("welcome")
print(10)
print(10+10)
print("Hello\nWorld")
print("Hello\rWorld")
print("\rHello world")


#variables
name="divya"
age=21
age2=age
print(name)
print(age)
print("my name is", name)
print(age2)

#printing datatypes
name1="d"
age3=22
old= False
a= None
print(type(name))
print(type(age))
print(type(old))
print(type(a))

#printing sum 
# x=10
# y=20
# sum= x+y
# print(sum)


'''
1.      Write a program to check if a given number is positive.
2.      Write a program to check if a given number is negative.
3.      Write a program to check if a number is zero.
4.      Write a program to check if a number is divisible by 5.
5.      Write a program to check if the number 88 is less than 100.
6.  Write a program to check if a number is a three-digit number.
7.  Write a program to check if a string is in lowercase.
8.  Write a program to check if a string is in uppercase.
9.  Write a program to check if a string contains a space.
10.  Write a program to check if a string starts with a capital letter.
'''

#1 +VE
# num=int(input("enter a no. :"))
# if num>0:
#     print("no. is positive")

# 4 div by 5
# num=int(input("enter a no. :"))
# if num%5==0:
#     print("Divisible by 5")

#5
num=88
if num<100:
    print("number is less than 100 ")

#6
# num=int(input("enter a no."))
# if 100<num<999:
#     print("it is 3 digit number")

#7
# s=eval(input("Enter a string"))
# if s.islower():
#     print("string is lowercase ")

'''
11.  Write a program to check if a string contains only alphabets.
12.  Write a program to check if a string contains only digits.
13.  Write a program to check if a string ends with a period ('.').
14.  Write a program to check if 'a' is present in the string s = 'apple'.
15.  Write a program to check if the first and last characters
     of a string are the same (e.g., x = 'level').
16.  Write a program to check if a character is a vowel. (e.g., a = 'I')
17.  Write a program to check if a character is uppercase. (e.g., b = 'P')
18.  Write a program to check if a character is lowercase. (e.g., c = 'k')
19.  Write a program to check if a character is a digit. (e.g., ch = '5')
20.  Write a program to check if the ASCII value of a character is greater than 100. (e.g., z = 'd')
21.  Write a program to check if 5 exists in a list. (e.g., lst = [2, 4, 5])
'''

#15
x="levels"
if x[0]==x[-1]:
    print('1st and last char are same')

#20
# ch=input("enter a character")
# print(ord(ch))
# if ord(ch)>100:
#     print("ascii value of char is greater than 100")

'''
22.  Write a program to check if the last element in a list is even. (e.g., l = [1, 2, 4])
23.  Write a program to check if the first two elements in a list are the same. (e.g., lst = [5, 5, 9])
24.  Write a program to check if the sum of a list is greater than 100. (e.g., y = [50, 40, 30])
25.  Write a program to check if a year is a leap year (simplified logic). (e.g., year = 2024)
26.  Write a program to check if a file name ends with '.txt'. (e.g., file = 'smile.txt')
27.  Write a program to check if a number is divisible by both 3 and 7. (e.g., num = 42)
28.  Write a program to check if a credit card number is 16 digits and contains only digits. (e.g., cc = '1234567812345678')
29.  Write a program to check if a student has scored 70, print 'Good Luck' (Take user input).
30.  Write a program to check which number is greater using the Condition. (e.g., a = 98, b = 67)
'''

#22
l=[1,2,4,5]
if l[-1]%2==0:
    print("last ele of list is even")

l=[50,40,30]
if sum(l)>100:
    print("sum of list is greater than 100")

# #28
# credit=(input("enter your credit card no. :"))
# if len(credit)==16 and str(credit.isdigit()):
#     print("no. is credit card no.")

#Convert uppercasr to lowercase
# ch=input("enter a character")
# if ord("A")<=ord(ch)<=ord("Z"):
#     print(chr(ord(ch)+32))

#convert lower to uppercase
# l=input("enter a character:")
# if ord("a")<=ord(l)<=ord("z"):
#     print(chr(ord(l)-32))

# 5.wap to check whether the first character
# in the given string is starting with uppercase
# or Not if it is not Then capitalize it
# s="python"

s={10,20,'hii'}
for i in enumerate(s):
    print(i)

d={'hi':10,'bye':20}
for i in enumerate(d):
    print(i)
print()
print(list(enumerate(d)))
print(tuple(enumerate(d)))
print(set(enumerate(d)))
print(dict(enumerate(d)))
print()

print(list(reversed(d)))  #['bye', 'hi']
print(reversed(dict(d)))


s="Hello"
print(reversed(s))
print(list(reversed(s)))
# ['o', 'l', 'l', 'e', 'H']

print(tuple(reversed(s)))
# ('o', 'l', 'l', 'e', 'H')

print(set(reversed(s)))
# {'e', 'o', 'H', 'l'}   unordered

# print(dict(reversed(s)))

