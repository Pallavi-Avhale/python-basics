#wap to check among three no which no. is greater
# x=eval(input('enter 1sst no.'))
# y=eval(input('enter 2nd no.'))
# z=eval(input('enter 3rd no.'))
# if x>y and x>z:
#     print('x is greater than y and z')
# elif y>x and y>z:
#     print('y is grater the  x and z')
# else:
#     print('z is greater than x and y')   

#wap to check among three no which no. is greater
# x=eval(input('enter 1sst no.'))
# y=eval(input('enter 2nd no.'))
# z=eval(input('enter 3rd no.'))
# if x<y and x<z:
#     print('x is smaller than y and z')
# elif y<x and y<z:
#     print('y is smaller the  x and z')
# else:
#     print('z is smaller than x and y')           


#calculator program
# num1= int(input('enter number 1='))
# num2= int(input('enter number 2='))
# operator= input('enter a symbol:')  #take operator from user
# if operator == '+':
#     print('add the operator',num1+num2)
# elif operator == '-':
#     print('sub the numbers', num1-num2)
# elif operator == '*':
#     print('multiply the numbers',num1*num2)
# elif operator == '/':
#     print('divide the numbers',num1/num2)
# elif operator == '//':
#     print('floor divide the no.',num1//num2)
# elif operator == '%':
#     print('modulus of no.',num1%num2)
# elif operator == '**':
#     print('power of ', num1**3)
# else:
#     print('invalid symbol')   


# wap to print the days in week
# day=int(input('enter the day no.'))
# if day == 1:
#     print('monday') 
# elif day==2:
#     print('tuesday') 
# elif day==3:
#     print('wednesday')                                    
# elif day==4:
#     print('Thursday')   
# elif day==5:
#     print('Friday') 
# elif day==6:
#     print('Saturday')  
# else:
#     print('invalid day')  


# wap to check the 1st char is uppercase/ lowercase/ digit/special character
# x='@Python.com'
# if ord("A")<=ord(x[0])<=ord("Z"):
#     print('starts with upper_case')
# elif ord("a")<=ord(x[0])<=ord("z"):
#     print("starts with lower_case")
# elif ord("0")<=ord(x[0])<=ord("9"):
#     print('starts with digits')
# else:
#     print('starts with special character')    

#wap to take marks of 5 subs, calculate avg if avg is between 90-100 print distinction
# if 75-89 then print first class& if it is 60-74 -->2nd class
# 50-59 --> 3rd class 
# below 50 --> fail
# m1=int(input('enter the marks of English:'))
# m2=int(input('enter the marks of Maths:'))
# m3=int(input('enter the marks of Science:'))
# m4=int(input('enter the marks of Hindi:'))
# m5=int(input('enter the marks of Social:'))
# avg= (m1+m2+m3+m4+m5)/5
# print(avg)
# if 90<=avg<=100:
#     print("distinction")
# elif 75<=avg<=89 :
#     print('First Class')  
# elif 60<=avg<=74:
#     print('Second class')
# elif 50<=avg<=59:
#     print('Third class')  
# else:
#     print('fail')    


# age is between 0-17----> child marriage 
# 18----> legal marriage..... 18-30----> arrange marraige 
# 30-35---> illegal marriage......35-40--->GO TO HELL
# age=  int(input('enter the age :'))
# if age<18:
#     print('Child marriage')
# elif age==18:
#     print('Legal marriage')
# elif 18<age<30:
#     print('Arrange marriage')
# elif 30<age<35:
#     print('Illegal marriage')
# elif 35<age<40:
#     print('GO TO HELL') 
# else:
#     print('none')               
              
         
# wap to check a data is sequence/iterable/individaul data type
# way 1--->
a= eval(input('enter the input:'))
if isinstance(a, (int,float,complex,bool)):
    print('Individual Data type')   
elif isinstance(a,(set,dict)) :
    print('iterable')   
elif isinstance(a,(str,list,tuple)):
    print('sequence')    
else:
    ('none')    




# way 2--->
a=eval(input('enter input'))
if type(a) in (int,float,complex,bool):
    print('SVD')
elif type(a) in (str,list,tuple):
    print('SEQUENCE')
elif type(a) in (set,dict):
    print('iterable')    
 