'''
EXCEPTION HANDLING:
--------------------

-It is an event trigers ocur suddenly while execution of the program.
                          
                          OR

-Unwanted and unexcepted event happen suddenly while execution of the program.

-------------------------------------------------------------------------------------
TYPES OF ERROR IN ALL LANGUAGES(COMMON ERROR):
1.Syntax Error---------->we can't handle syntax error (human error)
2.Runtime Error-------->we can handle Runtime error by the help of try and except block
                        ::here try and except both are keywords
---------------------------------------------------------------------------------------

'''

#ex
a=[1,2,3,4,5]
#normal code
# print(a[10])
# output--->IndexError: list index out of range

#using exception handling
try:                #store the error line
    print(a[10])    #This is known as risky code
except:             #handles the runtime errors---handling/resolved block
    print("Error handling")
# output--------->Error handling
print()

#NOTE: if i am using try block then it is mandatory to use except block
#When we are executing the program suddenly we will get the error ,
#  that error line we store in the try block, 
# and for handling the error we handle it in the except block
# When we don't have any error in try block then except block will not execute

'''
In Python, commonly we have mainly two types of error:

1. PRE-DEFINED ERROR(Inbuilt error)
  -Internally error will be present, we can't change the error name 
  -We can handle the error by try and except block.
  -Ex: Indentation Error, Syntax Error, Type Error

2. USER- DEFINED ERROR
  -If we want to raise the error by our own, we are the user and we are creating the error
  -we can give our own error name 

'''

'''
TYPES OF EXCEPT BLOCK:
-----------------------
1. Default Except Block:
2. Specific Except block:
3. Generic Except block:
4. Multiple Except block:
------------------------------

1. Default Except Block:
Syntax:  try:
            Error line(statement)
            .
            .
        except:
            statement(handling statement)

-When we don't know what type of error will occur then we go for Default exceot block

----------------------------------------------------------------------------
2. Specific Except block:
Syntax: try:
            Error line(statement)
        except Exception_name:
            statement(handling statement)

-When we know what error will occur then we go for Specific except block
-We need to mention the error name here
--------------------------------------------------------------------------


'''
a="welcome"
# print(a.append("e"))    #AttributeError: 'str' object has no attribute 'append'
#default
try:
    print(a.append("e"))
except:
    print("handle")
# output--->handle
print()

#specific
try:
    print(a.append("e"))
except AttributeError:
    print("specific error handling")
# output--->specific error handling

print("-------------------------")

#ex3
a=10
b=0
# print(a/b)   #ZeroDivisionError: division by zero

#default
try:
    print(a/b)
except:
    print("zero Division error handled")
#output---->zero Division error handled

#specific
try :
    print(a/b)
except ZeroDivisionError:
    print("handled")
# Output---->handled
print("----------------")

#ex3
a=10
b=5
# print(a/c)   #NameError: name 'c' is not defined
'''
#default 
try:
    print(a/c)
except:
    print("exception handling")

#specific
try:
    print(a/c)
except NameError:
    print("exception handling")

#when there is no error in try block then except block will not execute
try:
    print(a/b)
except:
    print("handle ")  #2.0
'''

'''
3. Generic Except Block:
 --if we want to get the reason of the error we go for generic except block
 -why i am getting the error to know that we use generic 

 ---------------------------------------------------------------------
 Syntax: try:
            Error line
        except Exception as Message:     #message: Alias Name
            print(message)
            statement
------------------------------------------------------------------------


'''
#Generic   ex1
a="Helllo"
# print(a.add("h"))
try:
    print(a.add("h"))
except Exception as msg:
    print("Error handling")
    print(msg)
# Error handling
# 'str' object has no attribute 'add'
print("----------------")

a="Helllo"
# print(a.add("h"))
# AttributeError: 'str' object has no attribute 'add'
try:
    print(a.add("h"))
except BaseException as msg:
    print("Error handling")
    print(msg)             #print('msg')--->do not use this 
# Error handling
# 'str' object has no attribute 'add'
print("---------------")

#NOTE : BaseException is part of Exception only.... we will get the same output with Exception and BaseException

#ex2 
# file=open("Pen.txt","r")
# print(file.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'Pen.txt'

try:
    file=open(file.read())
except Exception as x:
    print(x)    #name 'file' is not defined

'''
4. Multiple Except Block:
  -If we want to check multiple errors at a time we go for multiple except block
  -By using single try block we can check multiple errors by the help of except block

  --------------------------------------
  Syntax01:   try:
                error line
            except Exception_Name:
                statement
            except Exception_name:
                statement
            except Exception_name:
                statement
            .
            .
            .
(If the error line is matching the 1st except block it will stop futher execution)
(If not, then go to the 2nd except block...and so on)
(If it doesnot match till last except then it will show the error )
-----------------------------------------

Syntax 2: 
---> try:
        errror line
    except (Exception1,exception2,..):
        statement

'''

#ex1 multiple
a=10
b=2
# print(a/c)
try:
    print(a/c)
except ZeroDivisionError:
    print("error handling 1")
except TypeError:
    print("error handling 2")
except NameError:
    print("error handling 3")
except AttributeError:
    print("error handling 4")
# error handling 3

#syntax 2
try:
    print(a/c)
except(TypeError,AttributeError,NameError):
    print("Name error handling")
# Name error handling

#NOTE: if there is no error in try block then try block executes and ignores except block
try:
    print(a/b)
except(TypeError,AttributeError,NameError):
    print("Name error handling")
# 5.0
print("----------------")

'''
5. Finally Block:
   --------------

Finally is a keyword
-No matter whether the error is present or not the finally block will execute
-For code cleanup purpose we use finally block

syntax: try:
            error line
        except Exception_name:
            statement
        finally:
            statement
'''

x=[1,2,3]
# print(x.remove(14))
# ValueError: list.remove(x): x not in list
try:
    print(x.remove(14))
except ValueError:
    print("error handling")
finally:
    print("finally block")
print()
# error handling
# finally block


x=[1,2,3,4]
try:
    print(x.remove(1))
except ValueError:
    print("error handling")
finally:
    print("finally block")
print()
# None
# finally block

'''
Combination of try block & except block & else block & finally block:
---------------------------------------------------------------------

Syntax:
----------------------------------------
try:
    statement

except Exception_Name:
    statement

else:
    statement

finally:
    statement
----------------------------------------

NOTE:
-------> Whenever we have error in try block then  except block and finally block will be executing
-------> Whenever we don't have error in try block then try block, else block and finally block will execute
'''

#ex1      when there is no error try,else,finally
x=[1,2,3,4,5]
try:
    x.remove(4)
    print(x)
except ValueError:
    print('error handling')
else:
    print('else working')
finally:
    print('finally working')
print()
# [1, 2, 3, 5]
# else working
# finally working


#ex1 when there is error --->except,finally
x=[1,2,3,4,5]
try:
    x.remove(40)
    print(x)
except ValueError:
    print('error handling')
else:
    print('else working')
finally:
    print('finally working')
print()
# error handling
# finally working

'''
Nested try-except Block:
------------------------

syntax:
---------------------------------
try:
    statement(error line)

    try:
        statement(error line)

    except:
        statement(handling line)

except:
    statement(handling line)
---------------------------------
--->in 1st try block we don't have any error then it will enter the nested try block and except block
--->In 1st try block there is error then directly outside except block will execute

    
'''

#ex1
a=10
b=5
c=0
try:
    print(a/b)
    try:
        print(a/c)
    except ZeroDivisionError:
        print("inner error handling")
except:
    print("outer error handling")
print()
# output-->2.0
#         inner error handling

print("----------------------------------")

'''
USER DEFINED ERROR:
-------------------

We will create the error by our own
To do this, we use 'raise' keyword

syntax:
class userdefinedError(Exception or BaseException):
    pass 
    ...
'''
# def Number(num):
#     if num>0:
#         print("+ve")
#     else:
#         raise "negative error"
# Number(-10)
#In normal function if we are creating the error, then will generate the error but 
#it will give inbuilt error also so to avoid this we need to follow the above syntax

# raise "negative error"
# TypeError: exceptions must derive from BaseException

#ex1
# class NegativeError(Exception):
#     ...
# def Number(n):
#     if n>0:
#         print("positive no.")
#     else:
#         raise NegativeError
# Number(-8)
#output:
#     raise NegativeError
# NegativeError

#ex2
class Length_MissMatch(BaseException):
    pass
def Data(n):
    if len(n)>5:
        print("Its greater")
    else:
        raise Length_MissMatch
try:
    Data("hiii")
except:
    print("User defined Error Handling done")
print()

#     raise Length_MissMatch
# Length_MissMatch

class PalindromeError(Exception):
    pass
def Palindrome(s):
    if s==s[::-1]:
        print('is a palindrome')
    else:
        raise PalindromeError
try:
    Palindrome("sql")
except:
    print("palindrome error handled")
print()

'''
#1 Write a program to divide two numbers and handle divide-by-zero error.
try:
    n1=int(input("enter the number 1:"))
    n2=int(input("enter the number 2:"))
    print(n1/n2)
# except ZeroDivisionError:
#     print("error handling")

#2.Take integer input from user and handle invalid input.
try:
    a=int(input("enter the number"))
    print(a)
except ValueError as msg:
    print(msg)
    print("value error handling")

# enter the number'hii'
# value error handling

# enter the number'hi'
# invalid literal for int() with base 10: "'hi'"
# value error handling


#3. Access invalid list index and handle exception.
a=[1,2,3,4,5]
try:
    print(a[8])
except IndexError:
    print('index error handling')
#index error handling


#4. Access missing dictionary key safely.
y={11:12,7:9,'a':'b'}
try:
    print(y[22])
except KeyError:
    print("key error handling")


#5. Convert "abc" to integer and handle error.
try:
    a=int(input("enter a number"))
    print(a)
except ValueError:
    print('value error handling')


#6. Import non-existing module and handle exception.
try:
    import Pen
except ModuleNotFoundError:
    print("ModuleNotFoundError error handled")

# ModuleNotFoundError error handled


# 7. Open missing file and handle error.
try:
    file=open("file.txt")
except FileNotFoundError:
    print("FileNotFoundError handle")

#FileNotFoundError handle


#8. Add string + integer and handle exception.
try:
    a=int(input("enter a no."))
    b=input("enter a sring")
    print(a+b)
except TypeError:
    print("error handle")

# enter a no.20
# enter a sring'hi'
# error handle


#9. Create a program to safely print tuple index.
t=(10,20,45,36)
try:
    index=int(input("enter the index of tuple:"))
    print(t[index])
except IndexError:
    print("error handled")

# enter the index of tuple:7
# error handled


#10. Take user age input and handle wrong datatype
try:
    age=int(input("enter a age:"))
except ValueError:
    print("error handling")

# enter a age:[23]
# error handling
'''
print("-----------------------")

#ASSIGNMENT

# default excute block
# 1) Division by Zero
a=10
b=0
try:
    print(a/b)
except:
    print('Error Handling')    

# 2) Invalid List Index
a=[1,2,3,4]
try:
   print(l[5])
except:
    print('Error Handling')         
    
# 3) Error is not present
a=16
b=8
try: 
  print(a/b)  
except:
    print('Error')  
    
# 4) Undefined Variable
try:
    print(x)
except:
    print('Error Done')               
    
# 5) File Not Found
try:
   file=open('Demo.txt')
except:   
   print('FileNotFound')   
   
   
   
   
# specific excute block
# 1) Division by Zero
a=10
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print('Error Handling 1')    

# # 2) Invalid List Index
a=[1,2,3,4]
try:
   print(l[5])
except NameError:
    print('Error Handling 2')         
    
# # 3) Error is not present
a=16
b=8
try: 
  print(a/b)  
except NameError:
    print('Error')  
    
# # 4) Undefined Variable
try:
    print(x)
except NameError:
    print('Error Done')               
    
# # 5) File Not Found
try:
   file=open('Demo.txt')
except FileNotFoundError:   
   print('FileNotFound') 
   
   

# Genric excute block  
# 1) Division by Zero
a=10
b=0
try:
    print(a/c)
except Exception as e:
    print(e)
    print('Error Handling 1')    

# 2) Invalid List Index
a=[1,2,3,4]
try:
   print(l[5])
except Exception as a:
    print(a)
    print('Error Handling 2')         
# name 'l' is not defined
# Error Handling 2  
    
# 3) Error is not present
a=16
b=8
try: 
  print(a/b)  
except Exception as s:
    print(s)  
    print('Error')  
# 2.0  
    
# 4) Undefined Variable
try:
    print(x)
except Exception as b:
    print(b)
    print('Error Done')               
# name 'x' is not defined
# Error Done
    
# 5) File Not Found
try:
   file=open('Demo.txt')
except Exception as w:
    print(w)   
    print('FileNotFound') 
# [Errno 2] No such file or directory: 'Demo.txt'
# FileNotFound  



# Multiple exception block
a=10
b=0
try:
    print(a/b)
except AttributeError:
    print('Error Handling 1') 
except TypeError:
    print('Error Handling 2') 
except ZeroDivisionError:
    print('Error Handling 3')
# Error Handling 3

# 2) Invalid List Index
a=[1,2,3,4]
try:
   print(l[5])
except AttributeError:
    print('Error Handling 1') 
except TypeError:
    print('Error Handling 2') 
except NameError:
    print('Error Handling 3')
except IndexError:
    print('Error Handling 4') 
# Error Handling 3  

# 3) Error is not present
a=16
b=8
try: 
  print(a/b)  
except NameError:
    print('Error Handling 1') 
except AttributeError:
    print('Error Handling 2') 
except TypeError:
    print('Error Handling 3')
except IndexError:
    print('Error Handling 4') 
# 2.0

# 4) Undefined Variable
try:
    print(x)
except NameError:
    print('Error Handling 1') 
except AttributeError:
    print('Error Handling 2') 
except TypeError:
    print('Error Handling 3')
except IndexError:
    print('Error Handling 4') 
# Error Handling 1

# 5) File Not Found
try:
   file=open('Demo.txt')
except NameError:
    print('Error Handling 1') 
except AttributeError:
    print('Error Handling 2') 
except TypeError:
    print('Error Handling 3')
except FileNotFoundError:
    print('Error Handling 4')   
# FileNotFoundError: [Errno 2] No such file or directory: 'Demo.txt'



# finally 
# a) error will be present
a=10
b=0
try:
    print(a/c)
except ZeroDivisionError:
    print('Error Handling 1') 
finally:
    print('Error Handling 2')
# Error Handling 2
# NameError: name 'c' is not defined    

# b) error will not present
a=10
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print('Error Handling 1') 
finally:
    print('Error Handling 2') 
# Error Handling 1
# Error Handling 2             



# Combination try block , except block , else block and finally block
# a) error is not present
a=10
b=5
try:
    print(a/b)
except NameError:
    print('NameError')
else:
    print('Error Done')
finally:
    print('Error Handling') 
# 2.0
# Error Done
# Error Handling           

# b) error is present 
a=10
b=5
try:
    print(a/b)
except ZeroDivisionError:
    print('Zero division  Error')
else:
    print('Error Done')
finally:
    print('Error Handling')   
# Name Error
# Error Handling    


# Nested Block
# a) error is not present
a=10
b=5
try:
    print(a/b)
    try:
        print('Output')
    except:
        print('Done')
except:
    print('Error Handling')            
# 2.0
# Output

# b) error is present
a=10
b=5
try:
    print(a/c)
    try:
        print('Output')
    except:
        print('Done')
except:
    print('Error Handling')
# Error Handling


# undefined variable  
try:
    print(x)
    try:
       print('Variable is present') 
    except:
        print('Done')
except:
    print('Variable is not present')     
    
    
       
# user defined
# 1) User Defined Exception for Divide by Zero
class DivisionError(Exception):
    pass
try:
    a = int(input('Enter First Number : '))
    b = int(input('Enter Second Number : '))
    if b == 0:
        raise DivisionError
    print('Division :', a / b)
except DivisionError as e:
    print(e)
    print('Error Handling')          
           

# 2) Passwword Length
class PasswordError(Exception):
    pass
try:
    password=input('Enter a password : ')  
    if len(password) < 8:
        raise PasswordError('Password 8 Character/number')
    print('Valid Password')
except PasswordError as s:
    print(s) 
    print('Error Handling')

class PasswordError(BaseException):
    pass
class ValidPass(BaseException):
    pass
try:
    def password(pwd):
        if len(pwd)>6:
            if pwd.isalnum():
                print("valid password")
            else:
                raise ValidPass
        else:
            raise PasswordError
    password("abdgh#2426@")
except:
    print("error handling")
print("--------------------")

# class isPalindromeError(Exception):
#     pass
# try:
#     def Palindrome(n):
#         if n==n[::-1]:
#             print("it is palindrome")
#         else:
#             raise isPalindromeError
#     Palindrome("levels")
# except:
#     print("error handling")