# WHILE LOOP SYNTAX:
# WHILE CONDITION:
#   STATEMENT1
#   STATEMENT2
# .....
#  UPDATION/INCREMENTATION/DECREMENTATION

#set of instructions it will execute again and again 
# until condition becomes false.
'''
i=0
while i<=10:
    print(i,end=' ')
    i+=1
print()

i=10
while i>=5:
    print(i)
    i-=1

#wap to take string as a input and print 
# the elements of the string one by one 

st=input('enter a string:')
i=0
l=len(st)-1
while i<=l:
    print(st[i])
    i+=1

#print elements of the lis
lst=eval(input('enter a list:'))
i=0
while i<=len(lst)-1:
    print(lst[i])
    i+=1 

#print only vowels in string
st=input('enter a string:')
i=0
l=len(st)-1
while i<=l:
    if st[i] in'AEIOUaeiou':
        print(st[i],i)
    i+=1      

wap to take one list from user and print only the even elements 
lst=eval(input('enter a list'))
i=0
l=len(lst)-1
while i<=l:
    if lst[i]%2==0:
        print(lst[i],i)
    i+=1 
    


#wap print the value of odd count and even count
l=[11,23,44,21,52]
ec=0
oc=0
i=0
while i<len(l):
    ele=l[i]
    if ele%2==0:
        ec+=1
    else:
        oc+=1
    i+=1
print(oc)
print(ec)  
'''

#wap to print sum of element
l=[11,23,44,21,52]
sum=0
i=0
while i<len(l):
    ele=l[i]
    sum+=ele
    i+=1
print(sum)

'''
#wap to 
num=int(input('enter a num:'))
n=10
while num>=1:
    if num==3 or n==5:
        n-=1
        continue
    print(n)
    n-=1
   '''

#if the element is int skip the element 
l=[99,27.8,(8+5j),23]
res=[]
for i in l:
    if isinstance(i,int):
        continue
    res.append(i)
print(res)    

 #reversing the number
num=982
rev=0
while num!=0:
    rem= num %10
    rev= rev*10+rem
    num=num//10
print(rev)

'''
tracing

rev  |  num=982 | while n!=0  | rem=n%10  |  rev=rev*10+rem | num=num//10
-----------------------------------------------------------------------
0       982       true         982%10=2      0=0*10+2=>2      982//10==98
2        98       true         98%10==8      2*10+8=> 28       98//10==9
28       9        true         9%10==9       28*10+9==>289     9//10==0
289        0      false
'''



#palindrome no.
num=eval(input('enter a no.'))
res=num
rev=0
while num!=0:
    rev=rev*10+num%10
    num=num//10
print(f'reverse no is {rev}')
if res==rev:
    print('palindrome no.')
else:
    print('not a palindrome no.')

#armstrong no.
'''
if n=153
d=3  3^lenth+ 5^length + 3^length
---->3^3+5^3+3^3
---->153
'''

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

#fibonacci series for 1st 5 numbers from 0
n=eval(input('enter a no. of iterations:'))
a=0
b=1
while n>0:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    n-=1

n=eval(input('enter no. of iterations'))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a,b=b,c










