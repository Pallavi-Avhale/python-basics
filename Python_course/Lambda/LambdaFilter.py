'''
Map                                            Filter
-is a inbuilt function                         -also inbuilt function

-Map object address---->Typecasting            -Filter object address----->Typecasting
                        looping                                              Looping

Map will display both True as well              -True   False
as False value                                   always it will display True condition output

-map will accept two or more arguments         -filter will accept two arguments only
(function name and multiple iterables)           (function name and one iterable)




syntax of filter:   def func_name(Parameter):
                        statement
                    newvar=filter(func_name,iterable)          #only one iterable allowed
                    print(newvar) ---->filter object address
                    #avoid the object address two ways --->typecasting and looping
                    #looping
                    for var in newvar:
                        print(var)
                    
                    #typecasting
                    print(list(newvar))


syntax for lambda:  newvar=lambda arg1:expression
                    print(list(filter(newvar,iterable)))
'''

#ex
x=[10,11,12,13,14,15,16]
#map
def Map_data(x):
    return x%2==1
    # return "even" if x%2==0 else "odd"
e=map(Map_data,x)
print(list(e))
# [False, True, False, True, False, True, False]

#filter
x=[10,11,12,13,14,15,16]
def Filter_data(x):
    return x%2==1
f=filter(Filter_data,x)
print(list(f))
# [11, 13, 15]   will show only true statements

#lambda filter
x=[10,11,12,13,14,15,16]
w=lambda x:x%2==1
print(list(filter(w,x)))   #[11, 13, 15]
print(list(map(w,x)))    #[False, True, False, True, False, True, False]

#remove -ve no.
s=[-1,7,89,46,-21,-4]
def Data(s):
    return s if s>0 else 0
w=map(Data,s)
print(list(w))  #[0, 7, 89, 46, 0, 0]

s=[-2,45,837,-9,-5]
def Data(s):
    return s if s>0 else 0
w=filter(Data,s)
print(list(w))  #[45, 837]
print()

#1.Filter even numbers
n=[1,2,3,4,5,6]
def Filter(n):
    return n%2==0
w=filter(Filter,n)
print(list(w)) #[2, 4, 6]
print()


#2.filter odd numbers
y=[10,11,12,13,14]


#3.Remove empty strings
data=["apple","","banana","","cherry"]
def Remove(data):
    return data!=""
w=filter(Remove,data)
print(list(w)) #['apple', 'banana', 'cherry']
print()


#4.Keep Positive numbers
x=[-5,-2,10,3,7]
def Positive(x):
    return x>0
w=filter(Positive,x)
print(list(w))  #[10, 3, 7]
print()

#5.Filter Truthy values
s=[0,False," ",None,"Hii",6]
def Data(s):
    return bool(s)
w=filter(Data,s)
print(list(w)) #[' ', 'Hii', 6]
print()
'''whenever we are using empty values it is falsy values
whenever we are using values then it is truthy values'''


#6.Keep strings starting with “a”
words = ["apple", "banana", "avocado", "cherry"]
def Data(words):
    return words.startswith("a")
w=filter(Data,words)
print(list(w))  #['apple', 'avocado']
print()


#7.Keep only digits from a string
s="a1b2c3d4"
def Digit(s):
    return s.isdigit()
w=filter(Digit,s)
print("".join(w))  #1234
print()


#8.Keep only alphabets from a string
s1= "p3y4t5h6o7n"
def Alpha(s1):
    return s1.isalpha()
w=filter(Alpha,s1)
print("".join(w))  #python
print()


#9.Filter students who passed (marks ≥ 50)
marks = {"Ann": 45, "Ben": 70, "Cat": 55}
def Mark(marks):
    return marks[1]>=50
w=filter(Mark,marks.items())
print(list(w))  #[('Ben', 70), ('Cat', 55)]
print()


#10.Keep numbers divisible by 3
nums = [3, 6, 8, 10, 12, 15]
def Div(nums):
    return nums%3==0
w=filter(Div,nums)
print(list(w))  #[3, 6, 12, 15]
print()

#11.Keep words longer than 4 letters
words = ["cat", "elephant", "dog", "tiger"]
def Data(words):
    return len(words)>4
w=filter(Data,words)
print(list(w)) #['elephant', 'tiger']
print()

#12.Keep palindromes
words = ["madam", "python", "level", "world"]
def Palin(words):
    return words==words[::-1]
w=filter(Palin,words)
print(list(w))   #['madam', 'level']
print()

#13.Keep uppercase words
words = ["HELLO", "world", "PYTHON", "code"]
def Upper(words):
    return words.isupper()
w=filter(Upper,words)
print(list(w)) #['HELLO', 'PYTHON']
print()


#14.Filter names that end with “n”
names = ["Arun", "Kiran", "Deepak", "Sohan"]
def End(names):
    return names.endswith("n")
w=filter(End,names)
print(list(w)) #['Arun', 'Kiran', 'Sohan']
print()


#15.Keep numbers within a range (10–20)
nums = [5, 10, 15, 20, 25]
def Number(nums):
    return 10<=nums<=20
w=filter(Number,nums)
print(list(w))   #[10, 15, 20]
print()


#16.Filter emails containing “@gmail.com”
emails = ["mailto:abc@gmail.com", "mailto:xyz@yahoo.com", "mailto:test@gmail.com"]
def Mail(emails):
    return emails.endswith("@gmail.com")
w=filter(Mail,emails)
print(list(w))
print()

#17.Keep tuples where sum > 10
pairs = [(1,2), (5,6), (3,4), (7,8)]
def Sum(pairs):
    return sum(pairs)>10
w=filter(Sum,pairs)
print(list(w)) #[(5, 6), (7, 8)]
print()


#18.wap to return a list having only flowers

l=["sun flowers","banana tree","lily flowers","lotus flower","marigold flowers"]
def Flower(l):
    return "flowers" in l
w=filter(Flower,l)
print(list(w))  #['sun flowers', 'lily flowers', 'marigold flowers']
print()



