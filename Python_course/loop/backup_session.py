'''
for-else concept--->
--------------------------------
syntax--> for var in iterable:
            statement
        else:
            FSB
--------------------------------


'''
for i in range(1,11):
    print(i)
else:
    print('number printed successfully',end=" ")

# for the list if len of the element is odd print middle element and if even len then print 1st and last index value
l=['hello','java',(2+3j),66,'chutki']
d={}
for i in l:
    if isinstance(i,str):
        if len(i)%2==0:
            d[i]=i[0]+i[-1]
        else:
            mid=len(i)//2
            d[i]=i[mid]
print(d)

print()

#print the table
'''
num=eval(input('enter a no.'))
for i in range(1,11):
    print(f'{num}*{i}={num*i}')
    '''

#prime no.
num=eval(input('enter a no.'))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print('prime no.')
else:
    print('not prime no.')

print()

#wap to print all even no. between 1-20
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1
print()

#wap to print all odd no. between 15-1
i=15
while i>=1:
    if i%2==1:
        print(i)
    i-=1

'''
difference between for loop and while loop
for                           |       while
-------------------------------------------------------------------------
-we know no. of iterations    |         we don't know no. of iterations
-initialization & updation    |        -initialization is required
is not mandatory              |
-we can do operations on      |       -we cannot do operations on set and dict
all iterables                 |
-condition checking  is no    |        -condition checking is mandatory
not mandatory                 |
-inbuilt functions can be used|       -inbuilt functions cannot be used in while loop
in for loop                   |
-we cannot make it as infinite|        -we can make infinite loop 
loop
'''

#while else
i=15
while i>=1:
    if i%2==1:
        print(i)
    i-=1
else:
    print('operation completed')    