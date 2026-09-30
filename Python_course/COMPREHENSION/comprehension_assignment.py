
# 1. Create List of Characters from List of Strings
# Convert list of strings into list of characters.
# Input:lst = ["python","ai"]
# Output
# ['p','y','t','h','o','n','a','i']

lst = ["python","ai"]
print([j for i in lst for j in i])



# 2 .Extract Words Longer Than 3 Characters
# From nested list, extract words having length greater than 3.
# Input: lst = [["hi","hello"],["python","is"],["very","easy"]]
# Output : ['hello','python','very','easy']
lst = [["hi","hello"],["python","is"],["very","easy"]]
print([j for i in lst for j in i if len(j)>3])



# 3. Multiply Elements by 2
# Multiply every number inside nested list by 2.
# Input : lst = [[1,2],[3,4],[5,6]]
# Output : [2,4,6,8,10,12]
lst = [[1,2],[3,4],[5,6]]
print([j*2 for i in lst for j in i])


# 4. Extract Digits from Nested List of Strings
# Extract all digits from nested strings.
# Input: lst = ["a1b2","c3d4"]
# Output: ['1','2','3','4']
lst = ["a1b2","c3d4"]
print([j for i in lst for j in i if j.isdigit()==True])


# 5. Create Pairs from Two Lists
# Using nested list comprehension, create pairs.
# Input:
# l1 = [1,2,3]
# l2 = ['a','b']
# Output: [(1,'a'),(1,'b'),(2,'a'),(2,'b'),(3,'a'),(3,'b')]
l1 = [1,2,3]
l2 = ['a','b']
print([(i,j) for i in l1 for j in l2])


# 6. Flatten Nested List but Ignore Odd Numbers
# Input: lst = [[1,2,3],[4,5,6],[7,8]]
# Output: [2,4,6,8]
lst = [[1,2,3],[4,5,6],[7,8]]
print([j for i in lst for j in i if j%2==0])


# 7. Replace Even and Odd Numbers
# From a nested list, replace:
# Even → "E"
# Odd → "O"
# Input: lst = [[1,2,3],[4,5,6]]
# Output: ['O','E','O','E','O','E']
lst = [[1,2,3],[4,5,6]]
print(['E' if j%2==0 else 'O' for i in lst for j in i])


# 8. Square Even Numbers and Cube Odd Numbers
# Apply:
# Even → square
# Odd → cube
# Input: lst = [[1,2,3],[4,5]]
# Output: [1,4,27,16,125]
lst = [[1,2,3],[4,5]]
print([j**2 if j%2==0 else j**3 for i in lst for j in i ])


# 9.  Extract Characters Based on Condition
# Take characters from nested strings:
# If vowel → keep as uppercase
# Else → lowercase
# Input: lst = ["Python","AI"]
# Output: ['p','Y','t','h','O','n','A','I']
lst = ["Python","AI"]
print([j for i in lst for j in i])


# 10. Replace Numbers Greater Than 10
# Flatten the list but:
# If number >10 → "big"
# Else → number
# Input: lst = [[5,12,7],[20,3]]
# Output: [5,'big',7,'big',3]
lst = [[5,12,7],[20,3]]
print(['big' if j>10 else j for i in lst for j in i])

'''
11. Extract Words Based on Length
From nested list:
Length ≥5 → keep word
Else → ignore
Input: lst = [["hi","hello"],["python","is"],["data","science"]]
Output: ['hello','python','science']
'''
lst = [["hi","hello"],["python","is"],["data","science"]]
print([j for i in lst for j in i if len(j)>=5])

'''
list comprehensions example
***********************
1.wap to check even numbers in a list and return a list containing only even
numbers
l=[2,32,1,52,31,24,56,75]

2.wap to check elements inside the collection are even or odd,if it is even
make it square of that numbers,if it is odd make it as cube of that numbers
l=[2,3,5,1,7,2,3]

3.wap to return a list containing 10 multiples of 2
4.wap to return a list containing 10 multiples of given value(take user input)
5.wap to take two lists as input and add that elements and return a single
lists
6.wap to create a list containing tuples having two elements that is index and
value of list
l=["hey","hello","good","evening","python"]
7.wap to check length of strings present in tuple,if length is even append as
it is ,else reverse it and append
l=("hey","hello","good","evenings","python")


*******set comprehension example*******
1.wap to remove repeated values and return in set
l=[2,3,4,2,5,6,2,3]
2.wap to take two lists and return a set by adding elements present same index
l1=[2,3,4,5,6,7,8,9]
l2=[5,6,7,8,9,1,2,3] 
'''

# 1.wap to check even numbers in a list and return a list containing only even
# numbers
# o/p: [2, 32, 52, 24, 56]
l=[2,32,1,52,31,24,56,75]
print([i for i in l if i%2==0])

# 2.wap to check elements inside the collection are even or odd,if it is even
# make it square of that numbers,if it is odd make it as cube of that numbers
# o/p: [4, 27, 125, 1, 343, 4, 27]
l=[2,3,5,1,7,2,3]
print([i**2 if i%2==0 else i**3 for i in l])

# 3.wap to return a list containing 10 multiples of 2
print([2*i for i in range(1,11)])

# 4.wap to return a list containing 10 multiples of given value(take user input)
# enter a no. :5
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
num=eval(input('enter a no. :'))
print([num*i for i in range(1,11)])

'''
# 5.wap to take two lists as input and add that elements and return a single
# lists
from itertools import zip_longest
l1=eval(input('enter list 1: '))
l2=eval(input('enter a list 2: '))
print([i+j for i,j in zip_longest(l1,l2)])
# # o/p:enter list 1: [1,2,3]
# enter a list 2: [4,5,6]
# [5, 7, 9]'''

# 6.wap to create a list containing tuples having two elements that is index and
# value of list
# o/p: [(0, 'hey'), (1, 'hello'), (2, 'good'), (3, 'evening'), (4, 'python')]
l=["hey","hello","good","evening","python"]
print([(i,j) for i,j in enumerate(l)])

# 7.wap to check length of strings present in tuple,if length is even append as
# it is ,else reverse it and append
# ['yeh', 'olleh', 'good', 'evenings', 'python']--->output
l=("hey","hello","good","evenings","python")
x=[]
print([i if len(i)%2==0 else i[::-1] for i in l ])

# *******set comprehension example*******
# 1.wap to remove repeated values and return in set
l=[2,3,4,2,5,6,2,3]
print({i for i in l})



# 2.wap to take two lists and return a set by adding elements present same index
from itertools import zip_longest
l1=[2,3,4,5,6,7,8,9]
l2=[5,6,7,8,9,1,2,3] 
print({i+j for i,j in zip_longest(l1,l2)})

'''
Dict comprehensions
1.wap to create a dictionary keys by taking from list,values are square of that
key
l=[2,3,4,1,6,2,7,8,4]
2.wap to create a dictionary of values and index pair
l=["google","apple","python","orange"]
3.wap create a dictionary having first char of word and word pair if word
having even length
l=["google","apple","python","orange"]
4.wap to check length of words and create a dict having word and word pair if
it is even odd as it is else reverse and add
l=["google","apple","python","orange"]
5.wap to check elements is palindrome key and value should be same else value
is reverse of key
l=["banana","malayalam","madam","sir","mom","dad"] 
'''