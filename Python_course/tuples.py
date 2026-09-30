'''Tuples in python
- bulit in data type 
-immutable sequence of values
'''

tup=(87,64,33,95,76)
#for single element tuple
tup1=(22,)
print(type(tup))
print(type(tup1))

#tuple methods

'''tuple.index
returns index of first occurance'''

print(tup.index(87))

#tuple.count
print(tup.count(33))

'''movies=[]
movies.append(input("enter first movie:"))
movies.append(input("enter second movie:"))
movies.append(input("enter third movie:"))
print(movies)'''

list1=[1,4,7]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1 ==list1):
    print("palindrome")
else:
    print("not palindrome")    


