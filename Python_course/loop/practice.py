

w="H"
if ord("A")<=ord(w)<=ord("Z"):
    print(chr(ord(w)+32))
    print((ord(w)+32))

x="HELLO"
if x.isupper():
    print(x.lower())

y='h'
if ord("a")<=ord(y)<=ord("z"):
    print(chr(ord(y)-32))
    print(ord(y)-32)

a="python"
if type(a)==str:
    print("a is string")

b=["hiii"]
if isinstance(b,str):
    print('b is string')

# 14.  Write a program to check if 'a' is present in the string s = 'apple'.
s="apple"
if 'a' in s:
    print('a is present in string')
'''
# 15.  Write a program to check if the first and last characters
# of a string are the same (e.g., x = 'level').
st=eval(input('enter a string'))
if st[0]==st[-1]:
    print('first and last characters of string are same')

# 16.  Write a program to check if a character is a vowel. (e.g., a = 'I')
ch=input('enter a char.')
if ch in "AEIOUaeiou":
    print('char is vowel')'''

# 17.  Write a program to check if a character is uppercase. (e.g., b = 'P')
# ch=input('enter a char:')
ch='O'
if len(ch)==1:
    if ch.isupper():
        print('char is uppercase')
    else:
        print('not a upper case')

# 20.  Write a program to check if the ASCII value of a character is greater than 100. (e.g., z = 'd')
z='d'
print(ord(z))
if ord("z")>100:
    print('ascii val is greater')
else:
    print('ascii val is not greater')

# 24.  Write a program to check if the sum of a list is greater than 100. (e.g., y = [50, 40, 30])
y = [50, 40, 30]
sum=0
for i in range(len(y)):
    sum=sum+y[i]
    if sum>100:
        print('sum is greater')
print(sum)

# 34.  Write a program to check if the given string is a palindrome. (Take user input)
st=eval(input('enter a string='))
if st==st[::-1]:
    print('palindrome')
else:
    print('not palindrome')

