''' 
STATISTICS METHODS

----------------------------------------------------------------------------------------------------------------------

A. AVERAGE

1. MEAN
2. MIDDEN
3. MODE
4. STD
5. VARIANCE
 . RNAGE   --------> THW DIFFERENCE B/W MAXIMUM VALUE AND MINIMUM VALUE 

B. OTHER WAY

import statistics 

import ---> keyword
statistics ---> module

import statistics as s

s ----> alias name


'''

import statistics as s

x=[1,2,3,4,5,6,7,8,9,10]

print(s.mean(x))          # o/p----> 5.5

print()

print(s.median(x))           # o/p----> 5.5

print()

print(s.mode(x))            #O/P ----> 1

# --> IF WE HAVE SINGLE VALUE DATA THERE IS NO REPETED VALUE IT CONSIDER ALWAYS ----------> 1ST OCCURANCE
# --> IF WE HAVE REPETED VALUE IT CONSIDER ALWAYS ----------> 2ND OCCURANCE

print()

import statistics as s

a=[1,2,3,4,5,6,7,8,9,10,7]
print(s.mode(a))              # o/p -----> 7
# --> IF WE HAVE REPETED VALUE IT CONSIDER ALWAYS ----------> 2ND OCCURANCE

print()

import statistics as s

p=[1,2,3,4,5,6,7,8,9,10,7,10]
print(s.multimode(p))          # o/p ----> [7, 10]
# IF WE HAVE MULTIPLE DUPLICATE ELEMENTS IT WILL GIVE ALWAYS ALL THE DUPLICATE ELEMENTS 

print()

import statistics as s

d=[10,18,7,45,30,5,25]

print(s.variance(d))                   # 208