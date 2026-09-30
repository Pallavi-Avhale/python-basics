# #1.wap to print the number Table by using data given by user (take user input)
# #expected output:-->2*1=2  2*2=4............2*10=20
# num=eval(input('enter a no. '))
num=9
i=1
while i<=10:
    num*i
    print(f'{num}*{i} ={num*i} ')
    i+=1


print()

# #2.wap to print the names only if the length of the names is even
l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]
i=0
while i< len(l):
    if len(l[i])%2==0:
        print(l[i])
    i+=1

print()



# #3.wap to print the elements which in tuple,print only the if it is collection data types
values=(10,2.5,[10,20],"hero",True,(3,4,5),{2,7},{90:"super"})
i=0
while i<len(values):
    if type(values[i]) in (list,tuple,set,dict):
        print(values[i])
    i+=1


print()


# #4.wap to print the name which is starting with vowel in the given list
names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
i=0
while i<len(names):
    if names[i][0] in "AEIOUaeiou":
        print(names[i])
    i+=1

print()


# #5.wap to print sum of numbers in the list
l=[2,4,6,7,8,9]
sum=0
i=0
while i<len(l):
    sum+=l[i]
    i+=1
print(sum)


# #6.wap to extract only vowels and digits from the given string
s="hellopython123"
i=0
while i<len(s):
    if s[i] in "AEIOUaeiou" or s[i].isdigit():
        print(s[i],end=",")
    i+=1

print()

# #7.wap to iterate inside the list check if it is having nested list if yes merge it

list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
for i in range(len(list1)):
    if isinstance(list1[i],list):
        list1.extend(list1.pop(i))
print(list1)

print()

# #excepted output:-->list1=["hello",10,20.55,True,False,"hai","bye",False,"goodnight","enjoy the holiday"]


# #8.wap to print a number which are divisible by 5 from a list
l=[63,20,67,55,85,31]
i=0
while i<len(l):
    if l[i]%5==0:
        print(l[i])
    i+=1

print()

#if s=aaabbbcccddaa output should be abcda
s='aaabbbcccddaa'
ch=s[0]
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        ch+=s[i]
print(ch)

#strong number
'''
ex-145
fact(1)+fact(4)+fact(5)=number
then it is strong no.
'''
num=145
sum=0
for n in str(num):
    fact=1
    for i in range(1,int(n)+1):
        fact=fact*i
    sum+=fact
if sum==num:
    print('strong no.')
else:
    print('not a strong no.')

print()

#converting decimal no. to binary no.
num=12
st=""
while num!=0:
    if num%2 !=0:
        st="1"+st
    else:
        st="0"+st
    num=num//2
print(st)
        
print()

#converting the binary no. into decimal no.
n=1110
i=0
sum=0
while n!=0:
    rem=n%10
    if rem==1:
        sum+=2**i
    i+=1       #updation
    n=n//10   #number updation
print(sum)

'''
tracing:
sum=0  |  i=0  |  n=1110  |  while n!=0  |  r=n%10     |  if rem==1  |  sum+=2**i  |  i+=1  |  n=n//10
----------------------------------------------------------------------------------------------------
0      |   0   |  n=1110  |   True       |   1110%10=0 |   False     |             | i=1    |   n=1110//10=111
                  n=111   |   True       |   111%10=1  | true        | 2**1=2      | i=2    |   n=111//10=11
                  n=11    |   true       |   11%10=1   |  true       | 2**2=6      | i=3    |   n=11//10=1
                  n=1     |   True       |   1%10=1    |  true       | 2**3=8      | i=4    |   n=1//10=0
                  n=0     |   false  
'''

print()

#wap  to take one string from user and convert all the uppercase character into lowercase and then return the string
s="HeLLo"
i=0
st=""
while i<len(s):
    if 'A' <= s[i] <= 'Z':
        st=st+ chr(ord(s[i])+32)
    else:
        st= st+ s[i]
    i+=1
print(st)

print()

#wap to take one string from user and count no. of special characters present in the string 
# st=eval(input('enter a string'))
st="hii@22"
count=0
i=0
while i<len(st):
    if not('A'<= st[i]<='Z' or 'a'<=st[i]<='z' or '0'<=st[i]<='9'):
        count+=1
    i+=1
print(count)


print()

#find the hcf of the two numbers
n1=12
n2=18
i=1
hcf=0
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        hcf=i
    i+=1
print(f'hcf of {n1} and {n2} is {hcf}')


print()

#find lcm of the number
n1=int(input('enter a no.'))
n2=int(input('enter 2nd no.'))
if n1>n2:
    max_num=n1
else:
    max_num=n2
while True:
    if max_num%n1==0 and max_num%n2==0:
        lcm=max_num
        break
    max_num+=1
print(lcm)









