'''RECURSION
-It is the process of calling the function itself again and again 
by dividing the problem into smaller parts.

-In recursion we need to have :
1. Base case
-(stop condition)

2. Recursive case
-(calling func. itself by dividing problem into smaller problems/units )

HOW WE USE RECURSION IN THE PROBLEMS:
ex-
def counting

'''
'''
#1. ex print 5-1
def counting(num):
    if num==0:           #base case
        return 0
    else:
        print(num)
    return counting(num-1)   #recursive case
counting(5)

tracing:                else
(num)      if num==0      print(num)    counting(num-1)   
---------------------------------------------------------
5           False           5            4
4           False           4            3
3           False           3            2
2           False           2            1
1           False           1            0
0           True            -            -  

Call Stacks:
-----------------------------------
def counting(num):                  
    if num==0:               
        return 0
    return counting(num-1)   
-----------------------------------
In the RAM, compiler will create multiple blocks of 
this function to perform the operations.


#2. print 1-5
def counting(num):
    if num==6:
        return 0
    else:
        print(num)
    return counting(num+1)
counting(1)
'''

#3. print sum of all natural no. from 1-5
def sum(num):
    if num==6:
        return 0
    return num+sum(num+1)
print(sum(1))

'''Tracing:
num             if num==6           num+sum(num+1)          print(sum(1))
--------------------------------------------------------------------------



callstack:
------------------------
def sum(num):
    if num==6:
        return 0
    return n+sum(num+1)
---------------------------
'''

#4. print factorial of no.
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print(fact(5))
'''
callstack1:
def fact(5):
    if num==0:
        return 1
    return 5*fact(5-1= 4)                   24*5=120
fact(4)


callstack2:
def fact(4):
    if num==0:
        return 1
    return 4*fact(4-1= 3)                  4*6=24            
fact(3)

callsatck3:
def fact(3):
    if num==0:
        return 1
    return 3*fact(3-1= 2)                   3*2=6
fact(2)

callstack4:
def fact(2):
    if num==0:
        return 1
    return 2*fact(2-1= 1)                   2*1=2
fact(1)

callstack5:
def fact(1):
    if num==0:
        return 1                           1
    return 1*fact(1-1= 0)
fact()

'''

#in python it will allow 1024 call stack
#if we exceed the limits then we will get Recursion error 

import sys
print(sys.getrecursionlimit())
#o/p----1000

def calling(num):
    if num==999:
        return 0
    return calling(num+1)
print(calling(1))

#we can exceed the recursion limit by 
# print(sys.getrecursionlimit(2000))   it increases the no. of stack call 
# print(sys.getrecursionlimit())       for fetching the total no. of stack possiblities

#count digit program, print enen number from 1 to 10 using recusion 

#printing count of even no.
def evencount(num):
    if num==11:
        return 0
    if num%2==0:
        return 1+evencount(num+1)
    else:
        return evencount(num+1)
count=evencount(1)
print(count)

'''Tracing

callstack1:
num=1
def evencount(num):  
    if num==11:
        return 0  false
    if num%2==0:  false
        return 1+evencount(num+1) 
    else:
        return evencount(num+1)   (2)
count=evencount(1) 
print(count)

callstack2:
num=2
def evencount(num): 2
    if num==11:  false
        return 0
    if num%2==0: --->2%2==0 true
        return 1+evencount(num+1)--->1+ec(2+1=3)
    else:
        return evencount(num+1)
count=evencount(1)
print(count)

evencount(1)
Call num	Even?	Action
 1	1	    F	    evencount(2)
 2	2	    T	    1 + evencount(3)
 3	3	    F	    evencount(4)
 4	4	    T	   1 + evencount(5)
 5	5	    F	   evencount(6)
 6	6	    T	   1 + evencount(7)
 7	7	    F	   evencount(8)
 8	8	    T	  1 + evencount(9)
 9	9	    F	  evencount(10)
 10	10	    T	   1 + evencount(11)
 11	11	    —	   return 0  (base case)
'''
#printing even no.
def even(num):
    if num==11:
        return 0
    if num%2==0:
        print(num)
    return even(num+1)
even(1)

print()

# count the digit
def count_digit(num):
    if num==0:
        return 0
    return 1+count_digit(num//10)
print(count_digit(254))
#o/p-->3

'''Tracing-->

callstack1:
num=254
def count_digit(num):
    if num==0:  false
        return 0
    return 1+count_digit(num//10)--->1+cdigit(254//10)===25
print(count_digit(254))

callstack2:
num=25
def count_digit(num):
    if num==0:   false
        return 0
    return 1+count_digit(num//10)--->2+cdigit(25//10)==2
print(count_digit(254))

callstack3:
num=2
def count_digit(num):
    if num==0:   false
        return 0
    return 1+count_digit(num//10)---->3+cdigit(2//10==0)
print(count_digit(254))

callstack4:
num=0
def count_digit(num):
    if num==0:    true
        return 0------------->3+cdigit(0)
    return 1+count_digit(num//10)
print(count_digit(254))

'''

#reverse the number
#using while loop
# rev=0
# num=254
# while num!=0:
#     temp=num%10
#     rev=rev*10+temp
#     num=num//10
# print(rev)


def rev_digit(num,rev=0):
    if num==0:
        return rev
    return rev_digit(num//10,rev*10+num%10)
print(rev_digit(254))

'''tracing:

callstack1:
num=254
def rev_digit(num,rev=0):
    if num==0:  false
        return rev
    return rev_digit(num//10,rev*10+num%10)--->254//10==25
                                                0*10+254%10==4

callstack2:
num=25
def rev_digit(num,rev=4):
    if num==0:  false
        return rev
    return rev_digit(num//10,rev*10+num%10)---->25//10==2
                                                4*10+25%10==40+5==45

callstack3:
num=2
def rev_digit(num,rev=45):
    if num==0:   false
        return rev
    return rev_digit(num//10,rev*10+num%10)----->2//10==0
                                                 45*10+2%10==450+2==452

callstack4:
num=0
def rev_digit(num,rev=452):
    if num==0:   true
        return rev           ----------------->rev=452
    return rev_digit(num//10,rev*10+num%10)
'''

#Palindrome usig the reverse number program
def isPalindrome(num):
    if num==rev_digit(num):
        print(f'{num} is palindrome')
    else:
        print(f'{num} is not palindrome')
isPalindrome(151)

#multiplication but in the way (5*3=15) can be also (5+5+5=15)
#num=5 and n=3(no. of iterations)
def multiply(num,n):
    if n==0:
        return 0
    return num + multiply(num,n-1)
print(multiply(5,3))

'''Tracing:

callstack1:
num=5, n=3
def multiply(num,n):
    if n==0:  false
        return 0
    return num + multiply(num,n-1)--->5+mul(5,2)

callstack2:
def multiply(num=5,n=2):
    if n==0:
        return 0
    return num + multiply(num,n-1)----->10+mul(5,1)

callstack3:
def multiply(num=5,n=1):
    if n==0:
        return 0
    return num + multiply(num,n-1)--->15+mul(5,0)

callstack4:
def multiply(num,n=0):
    if n==0:
        return 0   ---------------->15
    return num + multiply(num,n-1)
'''

#power
def power(num,n):
    if n==0:
        return 1
    return num*power(num,n-1)
print(power(5,3))

#n=3
#3 2 1 2 3
# def prog(num):
#     print(num,end=" ")
#     if num==1:
#         return 1
#     # print(num,end=" ")
#     prog(num-1)
#     # if num!=1:
#     print(num,end=" ")
# prog(3)


def prog(num):
    if num==0:
        return 0
    print(num,end=" ")
    prog(num-1)
    if num!=1:
        print(num,end=" ")
prog(3)
'''Tracing

callstack1:
num=3
def prog(num=3):
    if num==0:
        return 0
    print(num,end=" ")--->3
    prog(num-1)--->prog(2)
    if num!=1:
        print(num,end=" ")
prog(2)

callstack2:
def prog(num=2):
    if num==0:
        return 0
    print(num,end=" ")------->2
    prog(num-1)--->prog(1)
    if num!=1:
        print(num,end=" ")
prog(1)

callstack3:
num = 1
def prog(num=1):
    if num==0:  false
        return 0
    print(num,end=" ")  ----> 1
    prog(num-1)  ----> prog(0)
    if num!=1:
        print(num,end=" ")  ----> (skipped)
prog(1)

callstack4:
def prog(num=0):
    if num==0:   true
        return 0-------------->return
    print(num,end=" ")
    prog(num-1)
    if num!=1:
        print(num,end=" ")
prog(3)
'''

    
    












