'''
x=[10,20,20,20,30,40,50]

key= 20

def Binary_search(x,key):
    li=0
    hi=len(x)-1
    F=-1

    while li<=hi:
        mid=(li+hi)//2
        if key==x[mid]:
            F=mid
            hi=mid-1
            

        elif key>x[mid]:
            li=mid+1


        elif key<x[mid]:
            hi=mid-1

    return F

F=Binary_search(x,key)

count=0

if F!=-1:             
    i=F
    while i < len(x) and x[i]==key:
        count+=1
        i+=1

print("Total count----->", count)
'''

'''
F=Binary_search(x,key)

count=0

if F!=-1:             
    i=F
    while i < len(x) and x[i]==key:
        count+=1
        i+=1

print("Total count----->", count)


if 1 != -1:
    i=F
    i=1

    while i<len(x) and x[i]==key:
          1<7      and x[1]==20:      #x[1]=20
          True          20==20:

          count=0+1 = 1
          i=1+1 = 2 


    i=2

    while i<len(x) and x[i]==key:
          2<7      and x[2]==20:      #x[2]=20
          True          20==20:

          count=1+1 = 2
          i=2+1 = 3 

    i=3

    while i<len(x) and x[i]==key:
          3<7      and x[3]==20:      #x[2]=20
          True          20==20:

          count=2+1 = 3
          i=2+1 = 4


    i=4

    while i<len(x) and x[i]==key:
          4<7      and x[4]=20:      #x[4]=30
          True           30==20:  
          True and Flase 
          Stop iteration 


'''

# x=[27,10,13,4,15]

# for i in range(len(x)):
#     for j in range(len(x)-1-i):
#         if x[j]>x[j+1]:
#             x[j],x[j+1]=x[j+1],x[j]

# print(x)

# r=[27,10,13,4,15]

# for i in range(len(x)):
#     minp=i
#     for j in range(i+1, len(x)):
#         if x[j]<x[minp]:
#             minp=j
#     x[i],x[minp]=x[minp],x[i]

# print(x)

x=[27,10,13,4,15]

for i in range(1,len(x)):
    p=i
    while p!=0 and x[p]<x[p-1]:
        x[p],x[p-1]=x[p-1],x[p]
        p-=1

print("INSERTION_SORT---->",x)