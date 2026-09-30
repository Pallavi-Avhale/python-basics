'''
FUNCTION--> 
A set of statement / Block of code it will execute whenever we are calling, 
without calling function name it will won't execute it will show blank space.

Syntax 1. Without using Return Keyword- 
def Function_name(Parameter):                 #function_declaration 
    statement1
    statment2
    

Function_name(argument)                       #Function_Callling

Syntax 2. with return key word
def Function_name(Parameter):                 #function_declaration 
    statement1
    statment2
    return 

print(Function_name(argument))                       #Function_Callling

'''


'''
if we use print function_name inside 
if we pass function_name in print like , print(Great), 

Great()--> Fun_Calling
Great--> Normal word
print(Great)--> Function Object address
Print(Greate())--> function 
None

'''

# example

# def even_odd(x):
#     if x%2==0:
#         print("Even")
    
#     else:
#         print("Odd")

# even_odd(10)                  #Even
# even_odd(11)                  #Odd


# def even_data(x):
#     for i in x:
#         if i%2==0:
#             print(i,end=' ')
# even_data([1,2,3,4,5,6,7,8,9,10])             #2 4 6 8 10 
# even_data([11,12,14,17,19,13])                  #12 14



# def palindrom(x):
#     if x==x[::-1]:
#         print("pal")

#     else:
#         print("Not pal")
# palindrom("mom")                            #pal                               
# palindrom("Hey")                            #Not pal

#user_input:

# def palindrom():
#     s=input('enter a element')
#     if s==s[::-1]:
#         print('palimdrom')
#     else:
#         print("it's not pal")

# palindrom()

# def palindrom(y):
#     for i in y:
#         if i in 'aeiouAEIOU':
#             print(i,end=' ')
# palindrom("Educations")                                      #E u a i o 


# While calling arguments

# 1. positional argument
# 2. keyword argument
# 3. variable positional argument (*args)
# 4. variable keyword argument (**kwargs)
# 5. combination of * argus and **kwargs
# 6. only positional(/)
# 7. only keywords(*)
# 8. combination of only positional and only keword argument


