'''
lambda function   / anonymous function

lambda function also we can call it as a nameless program /(no need to give name)
In lambda function insted of def keyword   we are using > lambda keyword 
lamda functions also we can call it as single line function
 
---------------------------------------------------------------------------
*DRAWBACKS
1)  no looping statement  (because lambda only accept only expression)
                          we can use for loop fun but it will act as comprehension
2)  no elif and nested if else program 
3)  we can't use return keyword
4)  break ,pass ,continue not supporrt 
5)  we can't do increament and decreament  (i++,i--)
----------------------------------------------------------------------------
SYNTAX  
new v_n=   lamda ardument1,argument2,an=rgument n .........:expression  
  |          |       |                                           |                                          
    char   kw     input(para)                                condition 

expression  : directly we cant write multiple condition if we write it will show error  to avoid errer use ()


whenever we have if condition
syntax
newv_n=lambda argu: TSB if condition else FSB

'''
#through fun
def greet():
    print("good mornig")
greet()

#through lamda
x=lambda :"good morning"
print(x)
#o/p 

#if am not passing  parameter it will show lambda object address
#to avoid use ()
x=lambda :"good morning"
print(x())

#wap to perform adding operationning"
def add(a,b):
    print(a+b)
add(2,3)

#throgh lambda
q=lambda a,b: a+b
print(q(1,4))

#square
z=lambda e: e**2
print(z(2))

#square ,cube
z=lambda e:(e*2,e*3)
print(z(2))

                         # SINGLE ARGUMENT #
#  1)WAP A LAMBDA FUN TO ADD 1 TO A NUMBER
a=lambda x : x+1
print(a(7))

#2)WAP A LAMBDA FUN TO MULTIPLY A NUM BY 2
y=lambda b: b*2
print(y(10))

#3) wap a lambda fun to find the square of number
s=lambda a: a**2
print(s(2))

#4) wap a lambda fun to check whether num is even or add
# 1 way
'''
whenever we have if condition
syntax
newv_n=lambda argu: TSB if condition else FSB
'''
#normal
x=10
if x%2==0:
    print("even")
else:
    print("odd")

#through fun
def even_odd(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
x=even_odd(10)

#through lambda 
#without print stmt it will show output in boolean format
q=lambda x: x%2==0
print(q(10))

#other way
q1=lambda x: "even numbeer" if x %2==0 else 'odd  number'
print(q1(7))

#5) wap lambda fun to perforn interger division by 2
x=lambda p: p/2
print(x(3))

#6)Write a lambda function to subtract 3 from a number.
a=lambda p: p -3
print(a(5))

# 7)Write a lambda function to find the cube of a number.
a=lambda c : c **3
print(a(3))

# 8)Write a lambda function to find the absolute value of a number
#absolut will conver negative ti posi
q=lambda b :abs(b)
print(q(-22))

# 9)rite a lambda function to add 10 to a number.
t=lambda a: a+10
print(t(10))

#10)Write a lambda function to divide a number by 5.
w=lambda a : a%5==0
print(w(50))

                                                                        # MULTI argument #

#Multiple Arguments operations


#Write a lambda function to add two numbers.
add = lambda a, b: a + b
print(add(3, 5))   

#Write a lambda function to multiply two numbers.
mul=lambda a,b: a*b
print(mul(2,4))

#Write a lambda function to subtract two numbers.
sub=lambda a ,b :a-b
print(sub(5,4))

#Write a lambda function to divide two numbers.
div=lambda a,b : a/b
print(div (25,5))


#Write a lambda function to find modulus of two numbers.
mod=lambda a,b :a%b
print(mod(10,3))

#Write a lambda function to find power (a**b).
pow=lambda a,b :a**b
print(pow(2,3))

#Write a lambda function to find maximum of two numbers.
max=lambda a,b : a if a >b else b
print(max(3,2))

#Write a lambda function to find minimum of two numbers.
min=lambda a,b : a if a < b else b
print(min (4,3))

#Write a lambda function to check if two numbers are equal.
equ=lambda a,b :a==b
print(equ(2,2))

#Write a lambda function to check if first number is greater than second
gre=lambda a,b : a if a > b else b
print(gre(2,1))

#Write a lambda function to check whether a number is Positive or Negative.
x= lambda a:"+ve number" if a>0 else "-ve number"
print(x(-8))
print('-----')

#Write a lambda function to check Pass or Fail (>=35 Pass).
x= lambda a:"Pass" if a>=35 else "Fail"
print(x(30))
print('------')

#Write a lambda function to return number if greater than 10, otherwise 0.
q=lambda num:num if num>10 else 0
print(q(12))
print('------')

#Write a lambda function to check if number is divisible by 5, else return -1.
q=lambda x:"divisible by 5" if x%5==0 else -1
print(q(15))
print('-----')

#Write a lambda function to check Adult or Minor (>=18 Adult).
x=lambda age:"adult" if age>=18 else "Minor"
print(x(19))
print('------')

#Write a lambda function to check if number is present in list [1,2,3].
x=lambda i: "present" if i in [1,2,3] else "Not present in list"
print(x(9))

#Write a lambda function to check whether a character is uppercase or lowercase.
x=lambda c:"uppercase" if 65<=ord(c)<=90 else "Lowercase"
print(x('g'))
print('--------')

#Write a lambda function to find the length of a string.
x=lambda a: len(a)
print(x("hii"))
print()

#Write a lambda function to reverse a string.
x=lambda a:a[::-1] 
print(x('hello'))
print()

# wap to find square and cube of given number
x=lambda a:(a**2,a**3)
print(x(3))
print()

# wap to check the given number is palindrome or not
x=lambda num:"Palindrome" if str(num) == str(num)[::-1] else "Not a palindrome"
print(x(123))
print()

#wap to return the key of a dictionary
a={"hello":"Sony","How":"are","you":"bye"}
x=lambda a: a.keys() 
print(x(a))
print()

# wap which returns first element of a sequence
a=lambda x:x[0] if isinstance(x,(str,tuple,list)) else "not sequence data type"
print(a(["hii","helllo"]))
print(a((1,2,3)))
print()

# wap which returns length of any iterable
x=lambda a:len(a) if isinstance(a,(str,tuple,list,set,dict)) else "not iterable"
print(x([33,54,11,2,4,3]))
print(x((2,3)))
print(x({"a":10}))
print()

#wap which returns the list of squares of numbers in a list
l=[2,3,4,5,6]
x=lambda i: [i**2 for i in l]
print(x(l))
print()

#wap to check list elements are palindrome or not
l=["nayana","kayak","mom","school","bag","dad"]
x=lambda a: "palindrome" if a==a[::-1] else "not palindrome "
result=[x(i) for i in l]
print(result)
print()

#wap to print the numbers present in a list with their corresponding indices pair
l=[100,200,300,400,500]
x=lambda a:[i for i in enumerate(l)]
print(x(l))
# [(0, 100), (1, 200), (2, 300), (3, 400), (4, 500)]

z=lambda l: [(i,l[i]) for i in range(len(l))]
print(z(l))
print()

#wap to check a data is sequence if it is sequence then return length pair else type pair
l=['hi','hello',2]
x=lambda a:[(a,len(a)) if isinstance(a,(str,tuple,list)) else (a,type(a)) for a in l]
print(x(l))
print()

# wap to check given number is divisible by 5 and 3
x=lambda a: "divisible by 5 and 3" if a%5==0 and a%3==0 else "not divisible"
print(x(15))
print()

#wap to check a data is sequence if it is sequence then return length pair else type pair


# wap to check given number is divisible by 5 and 3

#wap to check even or odd,if it is even return square of that value else square root of thavalue

#wap to check len of given string ,if length is even return as it is else return reverse of that string

#wap to check length of given string and return value and length in tuple and dictionary
q=lambda e: ((e,len(e)),{e:len(e)})
print(q("Python"))
# (('Python', 6), {'Python': 6})
print()


#wap to return if no is divisible by 5 then increment with 5 else decrement with 5
x=lambda a:a+5 if a%5==0 else a-5
print(x(45))







