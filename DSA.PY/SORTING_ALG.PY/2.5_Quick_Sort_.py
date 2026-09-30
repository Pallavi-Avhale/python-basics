'''
QUICK SORT ---------->

--------------------------------------------------------------------------------------------------S
1.consider a list collection


2.Initialise three variables i,e pivot as values
present at oth position ,i as 1 and j as len(collect)-1


3.check whether i<=j or not,if condition is true
then check for following condition


4.if collection[i]<pivot and i<=j then increment the
value of i by 1


5.if collection[j]>pivot and i<=j then decrement the
value of j by 1


6.if i<=j then swap collection[i] with collection[j]


7.if i<=j false then swap pivot element with jth
element and return the value of j.

'''

'''
x=[5,8,4,3,6,7,1]

0   1   2   3   4   5    6
5   8   4   3   6   7    1


1   3   4   5   6   7    8
|           |            |
low ele     pv          High value/ele
i                        j  

'''
"""
1.consider a list collection


2.Initialise three variables i,e pivot as values
present at oth position ,i as 1 and j as len(collect)-1


3.check whether i<=j or not,if condition is true
then check for following condition


4.if collection[i]<pivot and i<=j then increment the
value of i by 1


5.if collection[j]>pivot and i<=j then decrement the
value of j by 1


6.if i<=j then swap collection[i] with collection[j]


7.if i<=j false then swap pivot element with jth
element and return the value of j.
"""

z = [4, 3, 2, 1]


def Sorted_data(z, low, high):
    P = z[low]
    i = low + 1
    j = high
    while i <= j:
        while i <= j and z[i] < P:
            i = i + 1
        while i <= j and z[j] > P:
            j = j - 1
        if i <= j:
            z[i], z[j] = z[j], z[i]
            i = i + 1
            j = j - 1
    z[low], z[j] = z[j], z[low]
    return j  #3


print(Sorted_data(z, 0, len(z) - 1))
print(z)
print()
def QuickSORT(z, low, high):
    if low >= high:
        return
    j = Sorted_data(z, low, high)  #3
    QuickSORT(z, low, j - 1)
    QuickSORT(z, j + 1, high)
QuickSORT(z, 0, len(z) - 1)
print(z)


print()

x=[5,8,4,3,6,7,1]

def Sorted_data(x, low, high):
    P = x[low]
    i = low + 1
    j = high
    while i <= j:
        while i <= j and x[i] < P:
            i = i + 1
        while i <= j and x[j] > P:
            j = j - 1
        if i <= j:
            x[i], x[j] = x[j], x[i]
            i = i + 1
            j = j - 1
    x[low], x[j] = x[j], x[low]
    return j  #3


print(Sorted_data(x, 0, len(x) - 1))
print(x)            #---> [3, 1, 4, 5, 6, 7, 8]
print()
def QuickSORT(z, low, high):
    if low >= high:
        return
    j = Sorted_data(x, low, high)  
    QuickSORT(x, low, j - 1)
    QuickSORT(x, j + 1, high)
QuickSORT(x, 0, len(x) - 1)
print(x)                #----> [1, 3, 4, 5, 6, 7, 8]


