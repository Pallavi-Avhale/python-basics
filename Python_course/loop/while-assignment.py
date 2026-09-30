# 5.wap to extract only individual data types from the list and sum all the individual data types

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
total=0
for i in l:
    if  isinstance(i,(int,float,complex,bool)):
         print(i)
         total=total+i
print(total)

print()

# 6.wap to print the count of alphabets and numbers and space in the given string
s="india got the independence in the year 1947"
alphabet=0
number=0
space=0
for i in s:
     if i.isalpha():
          alphabet=alphabet+1
     elif i.isdigit():
          number=number+1
     else:
          space=space+1
print(f'total alphabet is {alphabet}')
print(f'total number is {number}')
print(f'total space is {space}')

# 7.wap to check how many words are present in the given sentence
s="hello world sentence"
words=s.split()
count=len(words)
print(f'no. of word are {count}')

# or
total=0
for i in s.split():
     total=total+1
print(f'Total no. of words are {total}')

# 8.wap to create a dictionary and print the characters
# # and its Ascii value pair
# s="hello world
# output:--> {"h":ascii value,"e":ascii value........}
s="hello world"
e={}
for i in s:
     e[i]=ord(i)
print(e)
     

# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it
# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}
names=["apple","google","yahoo","microsoft","gmail","walmart"]
d={}
for i in names:
     if len(i)%2==0:
          d[i]=i
     else:
          d[i]=i[::-1]
print(d)

# 10.wap to print series of factorial(take user input)
num=int(input('enter a no.='))
fact=1
for i in range(1,num+1,1):
     # print(i)
     fact=fact*i
print(fact)

# 11.wap to create a dictionary with element and its count pair
# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# output:-->
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}

# 15.wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
x=s.split()
print(x)
for i,j in enumerate(x):
     d[i]=j
print(d)
e={}
for i,j in enumerate(s.split()):
     e[i]=i
print(e)

#or
a={}
y=s.split()
for i in range(0,len(y),1):
     a[i]=y[i]
     a.update({i:y[i]})
print(a)

# 16.wap to create a dictionary words and its length pair
s="tomorrow is weekend and non-veg special"
e={}
t=s.split()
for i in t:
     e[i]=len(i) #e.update({i:len(i)})
print(e)

# 17.wap to create a dictionary characters and its corresponding upper case characters
s="sunday"
q={}
for i in s:
     q[i]=i.upper()
print(q)

# 18.wap to create a dictionary Ascii and character pair
l=[89,51,111,77,108,120]
p={}
for i in l:
     p[i]= chr(i)
print(p)

# 19.wap to  create a list of characters and its Ascii value pair
s="sunday"
v=[]
for i in s:
     v.append((i,ord(i)))
print(v)

# 20.wap to create a dictionary with words and its length pair and ends with vowel
s="Today is Tuesday and attending python session"
e={}
for i in s.split():
     if i[-1] not in "aeiouAeiou":
          e[i]=len(i)
print(e)

#wap to create dict wit letter and its words starting with that letter pair
s="hi hello good morning welcome to python session" 
d={}
for i in s.split():
     if i[0] not in d:
          d[i[0]]=[i]
     # else:
          # a[i[0]]+=[i]
print(d)

#or
y={}
for i in s.split():
     y.setdefault(i[0], []).append(i)
print(y)

#wap to create dict of characters and its indices pair
# s1="hello python"
# e={}
# for i in s1.split():
#      if i[0] not in e:
#           e[i[0]]=s[i]
# print(e)

s1 = "hello python"
e = {}

for i in range(len(s1)):
    if s1[i] not in e:
        e[s1[i]] = [i]
    else:
        e[s1[i]].append(i)

print(e)

#wap to create an dict word and reverse word pair
s="tomorrow is weakend and non-veg special"
d={}
for i in s.split():
     d[i]=i[::-1]
print(d)

#wap reverse a list without using any built-in functions and slicing
l=[1,2,3,4]
a=[]
for i in l:
     a=[i]+a
print(a)

#wap to sum of no.'s
s="Sony12India567pvt21ltd"
total=0
for i in s:
     if i.isdigit():
          total=total+int(i)
print(total)

#27.WAP to remove duplicates from the
# list without using inbuilt function
d=[1,2,3,4,5,6,7,1,2,3,4]
y=[]
for i in d:
     if i not in y:
          y.append(i)
print(y)

#28.wap to print first and last char of each name in the list
a=["Sunil","anil","Suresh","Mahesh","Dinesh"]
for i in a:
     print(i[0],i[-1])


#29.wap to create a new list as square of each number of below list
b=[2,4,5,6,7,1]
x=[]
for i in b:
     x.append(i**2)
print(x)

#30.wap if number is even the print its square else print its cube
c=[2,4,5,3,7,9]
even=[]
odd=[]
for i in c:
     if i%2==0:
          even.append(i**2)
     else:
          odd.append(i**3)
print(even)
print(odd)

#31.wap to create a list with square and cube of each numbers
d=[2,4,5,1,8,9,10]
k=[]
for i in d:
     k.append((i**2,i**3))
print(k)

#32.wap to create a new list of reversing each name from the list
names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
y=[]
for i in names:
     y=i[::-1]
print(y)

#33.wap to create a new list, of individual and collection data type from list
data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]
single=[]
double=[]
for i in data:
     if isinstance(i,(int,float,complex,bool)):
          single.append(i)
     else:
          double.append(i)
print(single)
print(double)

#34.wap to print author name in books dictionary
books={"love story":["Harish",30],"biography":["padam",150],"animals":["vimala",75]}
for i in books.values():
     print(i[0])

     #or
for i in books:
     print(books[i][0])

print()


#35.wap to group fruit name and country pair
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
for i in zip(d.keys(),p.values()):
     print(i)


#36.# 4.wap to replace all the character with "-" if the characters occurs more than once in a string
s="hellohai"
for i in s:
     if s.count(i)>1:
          s=s.replace(i,'_')
print(s)
          
print()

#37.# 10.wap to group fruit name and
# country pair only if a fruit is even length
d={"apple":45,"mango":67,"cherry":90,"berry":23}


p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
for i in zip(d.keys(),p.values()):
     if len(i[0])%2==0:
          print(i)


# 38.wap to using this list get the below output
l = ['sun flower', 'Lilly flower', 'Marigold flower','lion animal', 'tiger animal', 
     'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
d={}
for i in l:
     res=i.split()
     if res[1] not in d:
          d[res[1]]=[res[0]]
     else:
          d[res[1]]+=[res[0]]
print(d)


