'''

INSERATION SORT
-----------------------------------------------------------------------------------

IT IS THE TYPE OF SORTING ALGORITHM WHERE THE CURRENT VALUE WILL GET COMPARED WITH 
IT'S PREVIOUS VALUE FOR SORTING PURPOSE

ONLY LIMITED CODE IT WILL WORK ---> IT WON'T WORK ON COMPLEX AND LARGE DATA SET
0TH OF N SQUARE --> BEST --> AVERAGE (TIME COMPLEXCITY)

STEPS
------------------------------------------------------------------------------------

STEP 1---> CONSIDER A LIST COLLECTION TO BE SORTED 

STEP 2---> START PASSES FROM 1 BECAUSE AT 0TH PASS THERE WILL BE NO PREVIOUS VALUE FOR COMPARISION 

STEP 3---> CHECK WHETHER i IS NOT EQUAL TO ZERO OR NOT IF TRUE THEN WHETHER 
           THE CURRENT VALUE IS LESS THAT ITS PREVIOUS VALUE 

STEP 4---> IF THE ABOVE CONDITION IS ALSO TRUE THEN SWAP BOTH THE VALUES AND DECREMENT VALUE OF i BY 1



---------------------------------------------------------------------------------------------

EXAMPLE

A=[10,3,8,7,1]

      ||

10  3  8  7  1   ------> OTH ELEMENT POSITION IS ALREADY IN LEAST POSITION SO NEED TO CONSIDER WE NEED TO CONSIDER 1TH ( FOR 0TH POSITION WE DON'T HAVE ANY PREVIOUS ELEMENT TO SWAP)
0   1  2  3  4

A[1]<A[0]         --------> BACKWORD DIRECTION 
  3  <  10 -------> TRUE 

  i=i-1  -----------> DECREMENT BY 1

IF THE CONDITION BECOMES TRUE SWAP THE POSITION A[1],A[0] 

UPDATED LIST

0  1   2  3  4
3  10  8  7  1


--> A[2] < A[1]
-->  8   < 10   ----> TRUE
-->  SWAP (A[2],A[1])
-->  i=i-1               ----> DECREMENT i VALUE
-->   = 2-1
-->   = 1

--> A[1]  < A[0]
--> 8     <  3  ---> FLASE (STOP )

UPD LIST 

3  8 10  7  1




'''

# w=[10, 13, 2, 14, 5, 7, 1]

''' 

0    1    2    3    4    5   6
10   13   2    14   5    7   1


i=1
w[1]< w[0]  ----> 13 < 10  ---> false ----> stop

Updated List ---> [10, 13, 2, 14, 5, 7, 1]

i=2
w[2] < w[1]  ----> 2 < 13  ---> True ----> swap
swap(w[2], w[1])
i=i-1
 =2-1
 =1

[10, 2, 13, 14, 5, 7, 1]

i=1
w[1] < w[0]
2 < 10   -----------> True
swap ( w[1],w[0])
i=i-1
 =1-1
 =0

Updated list

[2, 10, 13, 14, 5, 7, 1]

i=3

'''

# x=[7,3,11,5,2,6,1]
# for a in range(1, len(x)): #----> 1 2 3 4 5 6 
#     i=a                  #------------> use new_var to store all the data--> all passing numbers i=1, i=2, i=3, i=4, i=5, i=6
#     while i!=0 and x[i]<x[i-1]: #x[3] < x[7]  ---> i=1 x[i-1]
#         x[i], x[i-1] = x[i-1], x[i]
#         i=i-1

# print("Final Output---->",x)     #-----> Final Output----> [1, 2, 3, 5, 6, 7, 11]


print()


s=[11,17,5,1,6,0.5]

for i in range(1, len(s)):
    p=i
    while p!=0 and s[p]<s[p-1]:   #x[p]---> x[1] , x[p-1]----> x[1-1]---> x[0]
        s[p], s[p-1] = s[p-1], s[p]
        p=p-1

print("Last_sort----->", s)             #------------>Last_sort-----> [0.5, 1, 5, 6, 11, 17]

