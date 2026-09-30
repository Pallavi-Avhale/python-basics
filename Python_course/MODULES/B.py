# import A
# A.Spam()
# print(A.Add(2,3))
# A.Test()

# import A as new
# new.Test()

from A import Test,Add
print(Add(2,2))
Test()
# Demo()   #nameerror

from A import *
print(Add(5,5))
Test()
Demo()