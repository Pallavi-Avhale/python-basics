# Lmbada:--------->

# Newvar_name=lambda arg1,arg2,arg3,........,:(Expression)

# NewVar_name=lambda arg1,arg2,arg3,........:TSB if condition else: FSB statment


#condition Based operations

#Write a lambda function to check whether a number is Even or Odd.





#Write a lambda function to check whether a number is Positive or Negative.

#Write a lambda function to check Pass or Fail (>=35 Pass).
Y=lambda marks:"pass" if marks>=35 else"fail"
print(Y(40))             #o/p-------------Pass
print(Y(29))             #o/p-------------Fail


#Write a lambda function to return number if greater than 10, otherwise 0.
A=lambda num:"greater than 10" if num>10 else "0"
print(A(12))                #o/p---------------> greater than 10
print(A(4))                 #o/p---------------> 0   


#Write a lambda function to check if number is divisible by 5, else return -1.


#Write a lambda function to check Adult or Minor (>=18 Adult).
Z=lambda age:"Adult" if age>=18 else "Minor"
print(Z(27))                 #o/p---->Adult
print(Z(17))                 #o/p---->Minor

#Write a lambda function to check if number is present in list [1,2,3].
L=lambda a:"True" if a in [1,2,3] else "False"
print(L(7))                   #o/p----> False
print(L(2))                   #o/p----> True
print(L(6))                   #o/p----> False


#Write a lambda function to check whether a character is uppercase or lowercase.
# st="MORNING"
S=lambda st:"true is upper case" if st.isupper else "False is lower"
print(S("MORNING"))                        #o/p----> true is upper case
print(S("MORNINg"))

#Write a lambda function to find the length of a string.
a=lambda st:len(st) 
print(a("HELLO"))                   #o/p----->5
print(a("PALLAVI"))                 #o/p----->7

#Write a lambda function to reverse a string.
b=lambda st:st[::-1]
print(b("HELLO"))                 #o/p----->OLLEH
print(b("Pallavi"))               #o/p----->ivallaP

# wap to find square and cube of given number
z=lambda num:num**3
print(z(2))                #o/p--->8
print(z(4))                #o/p---->64

# wap to check the given number is palindrome or not
x=121

d=lambda x: str(x)==str(x)[::-1]
print(d(x))                   #o/p--->True

a=lambda n:"pal" if str(n)==str(n)[::-1] else "not pal"
print(a(121))        #o/p---> pal        


#wap to return the key of a dictionary
a={"hello":"Sony","How":"are","you":"bye"}
d=lambda a: a.keys()
print(d(a))             #o/p---> dict_keys(['hello', 'How', 'you'])

p=lambda s:(s.items(),s.keys(),s.values())
print(p(a))           #o/p----->(dict_items([('hello', 'Sony'), ('How', 'are'), ('you', 'bye')]), dict_keys(['hello', 'How', 'you']), dict_values(['Sony', 'are', 'bye']))

# wap which returns first element of a sequence


# wap which returns length of any iterable


#wap which returns the list of squares of numbers in a list
l=[2,3,4,5,6]
k=[]
for i in l:                     #for looping
    k.append(i**2)
print(k)                 #o/p---> [4, 9, 16, 25, 36]

print([i**2 for i in l])      #o/p--> [4, 9, 16, 25, 36]         #comprehension (expression for loop)

m=lambda i:[i**2 for i in l]
print(m(l))                        #o/p--> [4, 9, 16, 25, 36] 

m=lambda l:[i**2 for i in l]
print(m(l))                          #o/p--> [4, 9, 16, 25, 36] 


#wap to check list elements are palindrome or not
l=["nayana","kayak","mom","school","bag","dad"]

#for loop

for i in l:
    if i==i[::-1]:
        print(i,"it's palindrom")
    else:
        print(i,"Not palindrom")

# o/p--->
# nayana Not palindrom
# kayak it's palindrom
# mom it's palindrom
# school Not palindrom
# bag Not palindrom
# dad it's palindrom

n=lambda l:[i[0]==i[-1] for i in l]
print(n(l))                 #o/p----> [False, True, True, False, False, True]

#wap to print the numbers present in a list with their corresponding indices pair
l=[100,200,300,400,500]

z=lambda l:[i for i in enumerate(l)]
print(z(l))                            #o/p----> [(0, 100), (1, 200), (2, 300), (3, 400), (4, 500)]


#by range

z1=lambda l:[(i,l[i]) for i in range(len(l))]
print(z1(l))                          #o/p---> [(0, 100), (1, 200), (2, 300), (3, 400), (4, 500)]

#wap to check a data is sequence if it is sequence then return length pair else type pair

a=lambda s: (s,len(s)) if isinstance(s,(str,list,tuple,set,dict)) else type(s)
print(a("HELLO"))                      #o/p---> ('HELLO', 5)
print(a({1,2,3,4}))                     #o/p--->({1, 2, 3, 4}, 4)

# wap to check given number is divisible by 5 and 3

#wap to check even or odd,if it is even return square of that value else square root of thavalue

#wap to check len of given string ,if length is even return as it is else return reverse of that string


#wap to check length of given string and return value and length in tuple and dictionary

a=lambda e:((e,len(e)),{e:len(e)})
print(a("PYTHON"))                   #o/p---> (('PYTHON', 6), {'PYTHON': 6})

#wap to return if no is divisible by 5 then increment with 5 else decrement with 5