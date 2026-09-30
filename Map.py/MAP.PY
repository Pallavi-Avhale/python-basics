'''MAP & FILTER
MAP	FILTER

Map is a inbuilt function	Filter is in built function
Map object address

	Typecasting
	Looping	Filter object address

	Typecasting
	Looping
Def function(parameter):
       Statement
New_var_name=map(Func_name, iterable1,iterable2,….)

Print(New_var_name)Map object address

1)	Typecasting print(list(New_var_name)
2)	For i in  New_var_name:
                   Print(i)
	Def function(parameter):
       Statement
New_var_name=filter(function_name,iterable)
Print(New_var_name)Filter object address

1)	Typecasting print(list(New_var_name)
2)	For i  in New_var_name:
        Print(i)
Work on True as well as False Output	It will get always True output'''

# Example of map:
# x=[10,11,12,13,14,15,17,16]

# def map_data(x):
#     return x%2==1
# e=map(map_data,x)
# print(list(e))                               #o/p-->[False, True, False, True, False, True, True, False]

# EXAMPLE OF FILTER---->

# x=[10,11,12,13,14,15,17,16]

# def filter_data(x):
#     return x%2==1
# e=filter(filter_data,x)
# print(list(e))                                #o/p--> [11, 13, 15, 17]


# print()

# w=lambda x:x%2==1
# print(list(filter(w,x)))                      #o/p-->[11, 13, 15, 17]
# print(list(map(w,x)))                         #o/p-->[False, True, False, True, False, True, True, False]

# r=lambda x: [i for i in x if i%2==1]
# print(r(x))                                   #o/p-->[11, 13, 15, 17]


# EXAMPLE--2-->

# s=[-1,7,-8,-10,11,56,-90]


#1.Filter even numbers
n=[1,2,3,4,5,6]

def Show(n):
    return n%2==0
f=filter(Show,n)
print(list(f))                  #o/p--> [2, 4, 6]

#2.filter odd numbers
y=[10,11,12,13,14]

def Odd(y):
    return y%2==1
x=filter(Odd,y)
print(list(x))                    #o/p--> [11, 13]

#3.Remove empty strings
data=["apple","","banana","","cherry"]

def Check(data):
    return data!=""
p=filter(Check,data)
print(list(p))               #o/p--> ['apple', 'banana', 'cherry']


#4.Keep Positive numbers
# x=[-5,-2,10,3,7]

def Pos(x):
    return x>0
z=filter(Pos,x)
print(list(z))                #o/p--> [10, 3, 7]


def Data(x):
    return x>0
a=filter(Data,x)
print(list(a))                    #o/p--> [10, 3, 7]

#5.Filter Truthy values
# s=[0,False,"",None,"Hii",6]



#6.Keep strings starting with “a”
words=["apple", "banana", "avocado", "cherry"]

def Display(words):
    return words.startswith("a")
a=filter(Display,words)
print(list(a))                         #o/p--> ['apple', 'avocado']


#7.Keep only digits from a string
s="a1b2c3d4"

def Digit(s):
    return s.isdigit()
d=filter(Digit,s)
print(list(d))                         #o/p-->['1', '2', '3', '4']

# 8.Keep only alphabets from a string
s1= "p3y4t5h6o7n"

def Alpha(s1):
    return s1.isalpha()
a=filter(Alpha,s1)
print(list(a))                         #o/p--> ['p', 'y', 't', 'h', 'o', 'n']

#9.Filter students who passed (marks ≥ 50)
marks= {"Ann": 45, "Ben": 70, "Cat": 55}

# def Score(marks):
#     retrun marks[1]>=50
# t=filter(Score,marks.items())
# print(list(t))

def demo(marks):
    return marks[1]>=50
f=filter(demo,marks.items())
print(list(f))                          #o/p--> [('Ben', 70), ('Cat', 55)]


#10.Keep numbers divisible by 3

nums = [3, 6, 8, 10, 12, 15]

def divisible(nums):
    return nums%3==0
d=filter(divisible,nums)
print(list(d))                           #o/p--> [3, 6, 12, 15]

#11.Keep words longer than 4 letters

words=["cat", "elephant", "dog", "tiger"]

def letter(words):
    return len(words)>4
l=filter(letter,words)
print(list(l))                            #o/p--> ['elephant', 'tiger']

#12.Keep palindromes

words = ["madam", "python", "level", "world"]

def palindrom(words):
    return words==words[::-1]
p=filter(palindrom,words)
print(list(p))                               #['madam', 'level']

#13.Keep uppercase words

words= ["HELLO", "world", "PYTHON", "code"]

def Upper(words):
    return words.isupper()
u=filter(Upper,words)
print(list(u))                               #['HELLO', 'PYTHON']

#14.Filter names that end with “n”

names= ["Arun", "Kiran", "Deepak", "Sohan"]

def aplha(names):
    return names.endswith("n")
a=filter(aplha,names)
print(list(a))                                #o/p--> ['Arun', 'Kiran', 'Sohan']

#15.Keep numbers within a range (10–20)

nums = [5, 10, 15, 20, 25]

def range(nums):
    return nums>=10 and nums<=20
r=filter(range,nums)
print(list(r))                                #o/p--> [10, 15, 20]


#16.Filter emails containing “@gmail.com”

# emails = ["mailto:abc@gmail.com", "mailto:xyz@yahoo.com", "mailto:test@gmail.com"]

# def End()

#17.Keep tuples where sum > 10
# pairs = [(1,2), (5,6), (3,4), (7,8)]




#18.wap to return a list having only flowers

# l=["sun flowers","banana tree","lily flowers","lotus flower","marigold flowers"]