'''
INTERMEDIATE TERMINATION IN LOOPING
----------------------------------
IT is achieved by using three different keywords 
1.break
2.continue
3.pass
---------------------------------
1.break:
  - 


break ex--print 1 to 5
for i in range(1,11):
    print(i)
    if i==5:
        break
        

print elements of list until we get the even no.
l=[1,9,4,7,2]
for i in l:
    if i%2==0:
        break
    else:
        print(i)


check username and password is valid or not
usernm="admin"
password="123"
while True:
    un=eval(input('enter username:'))
    if un==usernm:
        print('correct username')
        pwd=eval(input('enter a password'))
        if pwd==password:
            print('correct password')
            break
        else:
            print('incorrect password')
    else:
        print('incorrect un please try again')
'''

'''
randint:
---------
 it will generate the random numbers between specified range
syntax: randit(sv,ev) 
start value and end value both are inclusive

from random import randint
from-keyword
random-module
import-keyword
randint-function
'''

# from random import randint
# print(randint(1,5))
'''
from random import randint
n=randint(1,15)
while True:
    num=int(input('enter a no.='))
    if num==n:
        print('congrats...youu guessed')
        break
    elif num>n:
        print('you entered greater no.')
    else:
        print('your no. is smaller than guessed no.')
'''

#FACTORIAL PROGRAM
# fact=1
# n=5
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
'''
#factorial using while loop
fac=1
n=5
i=1
while i<=n:
    fac=fac*i
    i+=1
print(fac)

#generate the otp
from random import randint
cont=eval(input('enter contact no. '))
while True:
    otp=randint(1000,9999)
    print(f'your contact no. is {cont} and otp is {otp}')
    user_otp=eval(input('enter the otp you received:'))
    if otp==user_otp:
        print('login successfull')
        break
    else:
        print('try again....your otp is : ')


#generate the otp for 3 times
from random import randint
from time import sleep
count=0
cont=eval(input('enter contact no. '))
while True:
    if count<=3:
      otp=randint(1000,9999)
      count+=1
      print(f'your contact no. is {cont} and otp is {otp}')
      user_otp=eval(input('enter the otp you received:'))
      if otp==user_otp:
          print('login successfull')
          break
      else:
        print('try again....your otp is : ')
    else:
       print('limit exceeded, your block... try after 10sec pls...')
       sleep(10)
       count=0



2.continue:
- it is keyword use to skip the correct the iteration and control will for next iteration 
- it will not terminate the loop
- use for loop , while loop
- it will only skip the iteration go for next iteration



# 1 to 10 by skipping 4
for i in range(1,11):
    if i==4:
        continue
    print(i)    #1 2 3 5 6 7 8 9 10
    
#while loop
i=1
while i<=10:
    if i==4:
        i+=1
        continue
    print(i)
    i+=1
'''


#wap to take user input that is num and print the sequence
#  of num in dec order by skipping 3 & 5
# num=int(input('enter a num:'))
a=[]
for i in range(1,11,1):
    if i==3 and i==5:
       continue
       a[i]=i[::-1]
    print(i)

    print()

s="heyy guysss"
for i in s:
    ...
print(i)