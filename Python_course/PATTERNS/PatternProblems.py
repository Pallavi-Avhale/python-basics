'''
TYPES OF PATTERNS:
1. SOLID PATTERN-
whenever the patterns are tightly packed it is solid pattern
there are no empty spaces

2.HOLLOW PATTERN
whenever patterns are not tightly packed
we can have multiple empty spaces.
'''
#HOLLOW PATTERNS
# for i in range(1,6):
#     print('*',end=" ")

'''
now for printing the diagonals
we have two diagonals:
-primary
\
 \
  \
-secondary


for i in range(si,ei):     here i is for no. of rows
    for j in range(si,ei)    here j is for no. of columns


#primary diagonal
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#secondary diagonal
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end=" ")
        else:
            print(' ', end=" ")
    print()

#making the patterns dynamic for secondary diag.
n=eval(input('enter a no. for matrix'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

#primary diagonal dynamic and secondary and
#  primary diagonal and printing both diagonals
n=eval(input('enter no. for diagonal'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#printing the middle columns
n=eval(input('enter no. for matrix:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n//2+1 or i==n//2+1:
            print('*',end=" ")
        else:
            print('-',end=" ")
    print()

#prnting 1st and column and last row
n=eval(input('enter a no.'))
for i in range(1,n+1):
    for j in range(1,n):
        if j==1 or i==n:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

n=eval(input('enter no.'))
for i in range(1,n+1):
    for j in range(1,n):
        if i==n or j==1 or i==1 or j==n:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()


#print below pattern 
# *       * 
# * *     *
# *   *   *
# *     * *
# * * * * *
n=eval(input('enter a no.'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==1 or i==n or j==n:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()


#print the below pattern

n=eval(input('enter a no.'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i==n//2+1 or i+j==n+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

# * * * * * 
#       *
# * * * * *
#   *
# * * * * *


n=eval(input('enter the no. : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==n//2+1 or j==n//2+1 or i==j or i+j==n+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

# * * * * * * * 
# * *   *   * *
# *   * * *   *
# * * * * * * *
# *   * * *   *
# * *   *   * *
# * * * * * * *


#print the below pattern
n=eval(input('enter a no. for matrix'))
for i in range(1,n+1):
    for j in range(1,n):
        if i==n//2+1 or j==1 or j==n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

    '''

n=eval(input('enter the no. : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==n//2+1 or j==n//2+1 or i==j or i+j==n+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()