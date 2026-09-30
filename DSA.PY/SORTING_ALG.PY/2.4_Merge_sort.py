# '''
# MERGE SORT

# HERE WE NEED TO SEPERATE TO PARTS LEFT HAND SIDE AND RIGHT HAND SIDE THEN BOTH PART GET MERGE

# LEFT SIDE + RIGHT SIDE = MERGE

# LEFT = li -------> MID
# RIGHT= mid-------> hi

# x=[1,8,7,5,18, 3]

#        ||
#   0    1    2    3    4    5
#   1    8    7    5    18   3
#   li                       hi

#   li=0
#   hi=len(col)-1-----> 6-1=5
#   mid=(li+hi)//2 ---> (0+5)//2= 2

# LEFT = li -------> MID  0---->2
# RIGHT= mid-------> hi   3---->5

#   0    1    2    3    4    5
#   1    8    7    5    18   3
#         /        \
# [1  8   7]     [5  18  3]          ------> mid=(li+hi)//2 ---> find the mid
# li     hi       li     hi
#     /    \          /       \
# [1  8]    [7]     [5  18]   [3] 
# li  hi     |      li  hi      | 
# /   \      |      /    \      |
# [1] [8]    [7]  [5]   [18]   [3]

# '''

# '''
# x=[1,8,7,5,18, 3]

# def Divide(x, li, hi):
#     if li>=hi:                    #--------> once we got single element we need to stop(recursion will happen)--> condition becomes true it will stop the code or iteration 0>=0 (true, stop)
#         return 
#     mid=(li+hi)//2                #---> position of mid value is 2 
#     left=x[li :mid+1: ]           #---> mid value is inclusive so we need to take mid+1 (exclusive) ---> x[0:3]=[1,8,7] ---> left --> new_var
#     right=x[mid+1 : : ]           #---> from mid + 1 --> 3 ---> [5,18,3]--> upto last
#     print(left, right)            # left--> [1,8,7]  & right--> [5,18,3]
#     Divide(left, 0, len(left)-1)  #-----> len(left)-1 ---> 3-1=2 ---> range is 0 to 2 (left, 0 , 2)
#     Divide(right, 0, len(right)-1)

# Divide(x,0,len(x)-1)

# # o/p ---> 

# # Left side       Right side
# # [1, 8, 7]       [5, 18, 3]

# # [1, 8]  [7]     [5, 18] [3]
# # [1] [8]         [5] [18]

# #  Now Merge the left & right side both


# '''

# ''' 
# # left                       right
# 1>8 --> false           5>18----> False
# [1,8] [7]               [5,18] [3]

# 1>7--> F                 5>3 ---> T
# 8>7--> T                 swap [3,18] [5]
# swap                     3>5 ----> F
#                          18>5 ---> T (swap)
# [1,7,8]                  [3,5,18]

# x=[1,8,7,5,18,3]
# k=0

# left=[1,7,8]             right=[3,5,18]
#       0 1 2                     0 1  2   
# i=0                      j=0                       -------> # i --> left , j ---> right

# if i<len(left) and j<len(right):
#     0<3  and  0<3:                -----------> True
#     if left[i] < right[j]         -----------> left[i]=1  and right(j)=3
#         1<3  ----> true
#         x[k]=left[i]
#         k=k+1
#         i=i+1                  -------------> here we update only i valude not j 


# '''

# # x=[1,8,7,5,18,3]

# # d=[10,45,66,3,1,8,9,7]    #divide and conqure........

# '''

# x=[1,8,7,5,18,3]

# def Merge(x,L,R):
#     k=0
#     i=0
#     j=0

#     while i<len(L) and j<len(R):
#         if L[i]<R[j]:
#             x[k]=L[i]
#             i=i+1
#             k=k+1
#         else:
#             x[k]=R[j]
#             k=k+1
#             j=j+1

#     while i<len(L):
#         x[k]=L[i]
#         i=i+1
#         k=k+1
#     while j<len(R):
#         x[k]=R[j]
#         j=j+1
#         k=k+1
# def Divide(x,li,hi):
#     if li>=hi:
#         return
#     mid=(li+hi)//2  #2
#     left=x[li:mid+1:]  #[1,8,7]
#     right=x[mid+1::]  #[5,18,3]
#     print(left,right)
#     Divide(left,0,len(left)-1)
#     Divide(right,0,len(right)-1)
#     Merge(x,left,right)
# Divide(x,0,len(x)-1)
# print(x)

# '''
# '''
# a=[7,3,9,2,8,5]
# def Merge_data(a,L,R):
#     k=0
#     i=0
#     j=0
#     while i<len(L) and j<len(R):
#         if L[i]<R[j]:
#             a[k]=L[i]
#             k=k+1
#             i=i+1
#         else:
#             a[k]=R[j]
#             k=k+1
#             j=j+1
#     while i<len(L):
#         a[k]=L[i]
#         k=k+1
#         i=i+1

#     while j<len(R):
#         a[k]=R[j]
#         k=k+1
#         j=j+1
# def divide(a,low,high):
#     if low>=high:
#         return
#     mid=(low+high)//2
#     left=a[low:mid+1]
#     right=a[mid+1::]
#     print(left,right)
#     divide(left,0,len(left)-1)
#     divide(right,0,len(right)-1)
#     Merge_data(a,left,right)
# divide(a,0,len(a)-1)
# print(a) 


# print()
# ''' 
# -------------------------------------------------------------------------

x=[30,20,7,17,31,4,1]

def Divide(x, low, high):
    if low>=high:               #-> once we get single element we have to stop
        return 
    
    mid=(low+high)//2

    left=x[low:mid+1]
    right=x[mid+1:high+1]

    print("\n----------------->")
    print("Dividing_The_Data-->")

    print("LEFT_P----->", left)
    print("RIGHT_P---->", right)

    Divide(x,low,mid)
    Divide(x,mid+1,high)

print("Orignal Array")
print(x)
Divide(x,0,len(x)-1)

# o/p-->
# Orignal Array
# [30, 20, 7, 17, 31, 4, 1]

# ----------------->
# Dividing_The_Data-->
# LEFT_P-----> [30, 20, 7, 17]
# RIGHT_P----> [31, 4, 1]

# ----------------->
# Dividing_The_Data-->
# LEFT_P-----> [30, 20]
# RIGHT_P----> [7, 17]

# ----------------->
# Dividing_The_Data-->
# LEFT_P-----> [30]
# RIGHT_P----> [20]

# ----------------->
# Dividing_The_Data-->
# LEFT_P-----> [7]
# RIGHT_P----> [17]

# ----------------->
# Dividing_The_Data-->
# LEFT_P-----> [31, 4]
# RIGHT_P----> [1]

# ----------------->
# Dividing_The_Data-->
# LEFT_P-----> [31]
# RIGHT_P----> [4]

''' 
x=[30,20,7,17,31,4,1]
def Merge(x,low,mid,high):
    left = x[low:mid + 1]
    right = x[mid + 1:high + 1]
    print("\n--------------------->>>")
    print("Before Mergeing")
    print("LEFT---PART", left)
    print("RIGHT---PART", right)
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x[k]=left[i]
            k=k+1
            i=i+1
        else:
            x[k]=right[j]
            k=k+1
            j=j+1

    while i<len(left):
        x[k]=left[i]
        k=k+1
        i=i+1

    while j<len(right):
        x[k]=right[j]
        k=k+1
        j=j+1
    print("Merging List----->",x[low:high+1:1])
def Divide(x,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    left=x[low:mid+1]
    right=x[mid+1:high+1]
    print("\n--------------------->>>")
    print("dividing_The_Data")
    print("LEFT---PART",left)
    print("RIGHT---PART",right)
    Divide(x,low,mid) #Divide(left,0,len(left)-1)
    Divide(x,mid+1,high)#Divide(right,0,len(right)-1)
    Merge(x,low,mid,high)
print("Orginal Array---->")
print(x)
Divide(x,0,len(x)-1)
print("Final sorted array----->")
print(x)
'''


"""

x=[30,20,7,17,31,4,1]
def Merge(x,left,right):
    k=0
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x[k]=left[i]
            k=k+1
            i=i+1
        else:
            x[k]=right[j]
            k=k+1
            j=j+1
    while i<len(left):
        x[k]=left[i]
        k=k+1
        i=i+1

    while j<len(right):
        x[k]=right[j]
        k=k+1
        j=j+1
def Divide(x,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    left=x[:mid+1]
    right=x[mid+1::]
    print(left,right)
    Divide(left,0,len(left)-1)
    Divide(right,0,len(right)-1)
    Merge(x,left,right)
Divide(x,0,len(x)-1)
print("final data",x)
""" 

'''
x=[30,20,7,17,31,4,1]
def Merge(x,low,mid,high):
    left = x[low:mid + 1]
    right = x[mid + 1:high + 1]
    print("\n--------------------->>>")
    print("Before Mergeing")
    print("LEFT---PART", left)
    print("RIGHT---PART", right)
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x[k]=left[i]
            k=k+1
            i=i+1
        else:
            x[k]=right[j]
            k=k+1
            j=j+1

    while i<len(left):
        x[k]=left[i]
        k=k+1
        i=i+1

    while j<len(right):
        x[k]=right[j]
        k=k+1
        j=j+1
    print("Merging List----->",x[low:high+1:1])

def Divide(x,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    left=x[low:mid+1]
    right=x[mid+1:high+1]
    print("\n--------------------->>>")
    print("dividing_The_Data")
    print("LEFT---PART",left)
    print("RIGHT---PART",right)
    Divide(x,low,mid) #Divide(left,0,len(left)-1)
    Divide(x,mid+1,high)#Divide(right,0,len(right)-1)
    Merge(x,low,mid,high)
print("Orginal Array---->")
print(x)
Divide(x,0,len(x)-1)
print("Final sorted array----->")
print(x)

'''


"""

x=[30,20,7,17,31,4,1]
def Merge(x,left,right):
    k=0
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:        #---> Condition True Update i value
            x[k]=left[i]
            k=k+1
            i=i+1
        else:                       #----> False update j value
            x[k]=right[j]
            k=k+1
            j=j+1
    while i<len(left):              #--> for remaining left side values
        x[k]=left[i]
        k=k+1
        i=i+1

    while j<len(right):             #--> for remaining right side values
        x[k]=right[j]
        k=k+1
        j=j+1
def Divide(x,low,high):             
    if low>=high:
        return
    mid=(low+high)//2
    left=x[:mid+1]
    right=x[mid+1::]
    print(left,right)
    Divide(left,0,len(left)-1)
    Divide(right,0,len(right)-1)
    Merge(x,left,right)
Divide(x,0,len(x)-1)
print("final data",x)
""" 

y=[23,77,12,45,2,4,8,11,3]