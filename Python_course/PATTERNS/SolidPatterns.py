'''

for i in range(1,4):
    for j in range(1,6):
        print('*',end=" ")
    print()
o/p:
* * * * * 
* * * * *
* * * * *


for i in range(1,5):
    for j in range(1,3):
        print('*',end=" ")
    print()
o/p:
* * 
* *
* *
* *

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
o/p:
*
* *
* * *
* * * *
* * * * *


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
o/p:
* * * * * 
  * * * *
    * * *
      * *
        *


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
    o/p:
* * * * * 
* * * *
* * *
* *
*

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
o/p:
        * 
      * *
    * * *
  * * * *
* * * * *      



n=3
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j<=n*2 and j-i>=0:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
o/p: 
* * * * * 
  * * *
    *


n=3
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j>=4 and j-i>=-2 and j-i<=2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
    o/p:
    *     
  * * *
* * * * *


    

n=3
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j>=n+1 and j-i<=n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
    o/p:
    *     
  * * *
* * * * *

'''




 