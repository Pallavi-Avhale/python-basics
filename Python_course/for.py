'''num=eval(input('enter a num:'))
a=num+1
if str(a)==str(a)[::-1]:
    print('palindrom adding 1')
else:
    print('does not') 
      
    
#**#for loop extra 150 questions#**#

#wap to traverse throught a string and print each character
str1=input()
for i in str1:
    print(f'character present in the string:{a}')


#wap to travers through a dictionary
d={'a':'hello','b':100,'c':45.55,'d':True}
for i in d:
    print(d[i])
    
    
#wap to traverse through an iterable and fetch each element(all:list,tuple,set)
iter1=[10,20,30,40]
for i in iter1:
    print(i)  
    
    
#wap to iterate over a string in reverse direction
str1=input()
for i in str1[::-1]:
    print(i)  
    
    
#wap to print index as well as character of the string 
str1=input()
for i in range(0,len(str1)):
    print(i,str1[i]) 

str1='sakshi'
for i in enumerate(str1):
    print(i,end=' ') 
    

#wap to access dict key and values using enumereate and other methods
d={1:100,2:200,3:300,4:400}
for key,values in d.items():
    print(key)
    print(values) 
    
d={1:100,2:200,3:300,4:400}
for i in d.key():
    print(i)  
    
d={1:100,2:200,3:300,4:400}
for i in d.values():
    print(i)   
    
#wap to create a dict of character and its ASCII value paire by taking string as input
a='sakshi'
b={}
for i in a:
    b[ord(i)]=i 
print(b) 

#wap to create a dict of word and its length pair from a string
s='python is an easiest programming language'
d={}
for i in s.split():
    d[i]=len(i)
    print(d) 
    
d={}
word=s.split()
for i in word:
    d[i]=len(i)
    print(d) 
    
#wap to create  a dictionary of index and character pair of a string
a='good morning'
d={}
for i in a:
    d[i]=a.index(i)  
print(d) 

a='good marning'
d={}
for i,j in enumerate(a):
    d[i]=j
print(d)  


#wap to create a dict with word and its count pair from the given sentence
a='my day is good day or bad day or just a day'
b=a.split()
d={}
for i in b:
    d[i]=b.count(i)
print(d)  


#wap to print fibonacci series
n1=0
n2=1
a=10
for i in range(a):
    print(n1,end='')
    b=n1+n2
    n1=n2 
    n2=b
print(f'10 fibonacci value is:{n1}')

n1=0
n2=1
for i in range(1,11):
    print(n1,end='')
    b=n1+n2
    n1=n2 
    n2=b
print(f'10 fibonacci value is:{n1}') 

#wap to print index and character of string in tuples
a='hello world'
for i in enumerate(a):
    print(i,end='')
 
#demonstrate packing and unpacking of different iterables using zip 
l=[10,20,30]
s='hai'
for i in zip(l,s):
    print(i)  
    
#wap to create new list as square of each num of below list
l=[2,4,5,1,9,7,3]  
a=[]
for i in l:
    a.append(i**2)  
print(a)  

#wap if num is even the print its square else print ita cube
l=[2,4,5,1,9,7,3]
a=[] 
for i in l:
    if i%2==0:
       print(f'the square of{i} is:{i**2}')
    else:
       print(f'the square of{i} is:{i**3}')

l=[2,4,5,1,9,7,3]
a=[] 
for i in l:
    if i%2==0:
       a.append(i**2)
    else:
       a.append(i**3) 
print(a) 

#wap to create a new list of separate even number and odd number
l=[2, 4, 5, 1, 9, 7, 3]
eve=[]
odd=[]
for i in l:
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)
print(eve)
print(odd)        
  
#wap to create a list with square and cube of each number
l = [2, 4, 5, 1, 6, 9, 7, 3]
a=[]
for i in l:
    a.append((i**2,i**3))
print(a) 

#wp to create a new list of reversing each name from the list.
names = ["sunil", "dinga", "penga", "harsha", "manga"]
a=[]
for i in names:
    a.append(i[::-1])
print(a)  
                                                                 
#wp to create a new list of individual and collection data type from list
datas = [20.12, True, [10, 20], {1, 2}, 2+6j, {"a":10}, 100]
individual=[]
collection=[]
for i in datas:
    if isinstance(i,(int,float,complex,bool)):
        individual.append(i)
    else:
        collection.append(i)
print(individual) 
print(collection)       
    
      
#35.wp to create a list with fruit name and along with index
fruits = ["apple", "orange", "banana", "mango", "grapes"]
n=0
f=[]
for i in fruits:
    f.append((fruits,n))
    n+=1
print(f)  

#wp to find factorial of given number
n=eval(input('enter a num:'))
a=1
b=1
while a<=n:
    b=b*a
    a+=1
print(b)   

#wp to create a list if the price if the product is more than 1000 then add the product name to a list
products = {"Asian-paint":4000, "Mobile":90000, "Hen":500, "Pen":5, "Watch":2500}
a=[]
for i in products.items():
    if i[1]>1000:
        a.append(i[0])
print(a)     

#wap create a list,if a key is a individual DT then add key and data type as its value 
elemnts = {10:"Ind", "hai":"Colle", [10]:"Colction", True:"Inddual", (11,22):"Colltion"}
a=[]
for key in elemnts:
    if isinstance(key,(int,float,complex,bool)):
        a.append((key,type(key)))
print(a) 
 

#wp to print author name in books dictionary
books = {"loverstory":["Harish",30], "biography":["Padam", 150], "animals":["vimala",75], "songs":["venkat",90]}
for author,price in books.values():
    print(author)
 
 
#wp to print book name along with author
books = {"loverstory":["Harish",30], "biography":["Padam", 150], "animals":["vimala",75], "songs":["venkat",90]}
for key,val in books.items():
    print(key,val[0])
 
 
#wp to create a dictionary name and its count pair
names = ["gmail", "fb", "insta", "google", "gmail", "yahoo", "fb", "fb"]
d = {}
for i in names:
    d[i] = names.count(i)
print(d)
  
    
#wap to create a list with name and no. of occurance.
names = ["gmail", "yahoo", "fb", "google", "gmail", "yahoo", "fb", "google", "yahoo", "fb"]
a=[]
for i in names:
    a.append((i,names.count(i)))  
print(set(a))
         
         
#wp to print author name in books dictionary
books = {"loverstory":["Harish",30], "biography":["Padam", 150], "animals":["vimala",75], "songs":["venkat",90]}
for author,price in books.items():
    print(author)
print()    
for key,value in books.items():
    print(key)
    print(value)  
    

#wp to create a dictionary name and its count pair
names = ["gmail", "fb", "insta", "google", "gmail", "yahoo", "fb", "fb"]
d={}
for i in names:
    d[i]=names.count(i)       
print(d)  


#wp to create a dictionary characers and its count pair
chars = ['a', 'M', 'i', 'A', 'M', 'h', 'i', 'H', 'a', 'B']
d={}
for i in chars:
    d[i]=chars.count(i)
print(d)    
   
   
#wp to create a dictionary with mobile and its count pair with and without inbuilt function
mobiles = ["mi", "iphone", "vivo", "poco", "samsung", "iphone", "mi", "vivo", "mi", "relame"]
d={}
for i in mobiles:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
print()           
for i in mobiles:
    d[i]=mobiles.count(i)
print(d)


#wp to create a dictionary character and its count pair
chars = ['A', "s", "o", "P", "O", "O", "S", "H", "J", "A", "V", "H", "o"]
d={}
for i in chars:
    if i not in d:
        d[i]=1 
    else:
        d[i]+=1
print(d)
  
  
#wp to create a dictionary 1st character as "key" and names starts with same 1st charcter should be the value
names = ["anu", "dinesh", "abhi", "divya", "suresh", "dileep", "mahesh"]
{"a":["anu", "abhi"]}
d={}
for i in names:
    if i not in d:
        d[i[0]]=[i]
    else:
        d[i[0]].append[i]   
print(d)         
       
       
#wp to create a dictionary length as key and same length as list of value
fruits = ["apple", "grapes", "kiwi", "mango", "papaya", "bannana", "cherry", "berry"]
d={}
for i in fruits:
    if len(i) not in d:
        d[len(i)]=[i] 
    else:
        d[len(i)].append(i) 
print(d)                 

 
#wp to create a dictionary, with list of even and odd number sepratley(intially we should only add key and empty list)
numbers = [22, 34, 89, 10, 2, 4, 9, 7, 1, 56]
a={'even':[],'odd':[]}
for i in numbers:
    if i%2==0:
        a['even'].append(i)
    else:
        a['odd'].append(i) 
print(a)           
     
     
#word and length pair
sentence = "python is a programming language"
words = sentence.split()
d={}
for i in words:
    d[i]=len(i)
print(d)    
       
       
#index and element pair
a='hello'
b=a.split()
d={}
for i,j in enumerate(a):
    d[i]=j
print(d)


#word and its count pair
sentence = "hai hello hai world hai good morning world hello hello"
words = sentence.split()
d={}
for i in sentence:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)            


#character and count pair
s = "helloall"
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)    
    
    
#create a dictionary with character and ascii value pair
s = "hello"
d={}
for i in s:
    d[i]=d.get(i,ord(i))
print(i) 
      
    
create a dictionary with character and count pair, with only repeated character
s = "hello all... good morning... welcome all..."
        
        
##**Assignment**##

#wap to create a dictionary with character and index value
s='python'
d={}
for i in range(len(s)):
    d[s[i]]=i
print(d)  


#2.wap to sort the characters of the string (alphabets followed by digits)

s=input('enter a string:')
aplhabets=''
digits=''
for i in s:
    if i.isaplha():
        aplhabets+=i
    elif i.isdigit():
        digits+=i
alphabets = sorted(alphabets)
digits = sorted(digits)        
result=   

 
#3.wap to print a character repeatedly as many times as mentioned in consecutive digit( i/p: a4b3c2   o/p: aaaabbbcc)
a='a4b3c2'
d=''
for i in range(len(a)):
    if a[i].isalpha():
        b=a[i]
    else:
        d+=b*int(a[i])
print(d)            


#4. wap to perform the following (i/p: a4k3b2  o/p: aeknbd)
s='a4k3b2'


#5. wap to remove duplicate characters from the given string.
a='sakshii'
b=''
for i in a:
    if i not in b:
        b+=i
print(b)        


6. wap to find number of occurances of each character present in the given string.

#7. wap to display unique vowels present inside the given string.
s = "programming"
a= "aeiou"
b= ""

for i in s:
    if i in a and i not in b:
        b += i

print("Unique vowels:", b)
        


#8. wap to read a tuple from the user and print its sum and average.
t=input('enter a list:')
sum=0
for i in t:
    sum+=i
print(sum)    


#9. wap to eliminate duplicates present in the list by reading list from user.
l=input('enter a list:')  #1 2 3 4 2 3 4 
a=l.split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)                 #['1', '2', '3', '4']


10. wap to read dictionary from user and find the sum of values if they are integer.
d={}


#11. write a program to create a dictionary to get only the duplicate items and
 #the number of times the item is repeated in the list. 
Names = ["apple", "yahoo", "google", "apple", "yahoo",
         "facebook", "apple", "gmail", "gmail", "gmail"]
d={}
for i in Names:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)        #{'apple': 3, 'yahoo': 2, 'google': 1, 'facebook': 1, 'gmail': 3}      


#wap pgm to find the sum of digits of a given num o/p:10
n = 1234
sum = 0
while n > 0:
    digit = n % 10      # get last digit
    sum += digit        # add digit to sum
    n = n // 10         # remove last digit

print("Sum of digits:", sum) 
'''

#12. write a program to get the indices of each item in the below list.
#o/p should be in dictionary with name and value list pair. 
# Names=[“apple”, “google”, “apple”,  “yahoo”, “yahoo”, “facebook”,
# 	 “apple”, “gmail”, “gmail”, “gmail”]

  
'''  
13. sort the list based on last character of each element.
	names = ["steve", "eve", "adani", "bob", "birla", "ambani"]
 
14. sort the dictionary based on keys.

15. sort the dictionary based on length of the keys.

16. sort the dictionary based on first character of the keys

17. sort the dictionary based on last character of keys.
 	d = {"walmart": 7, "gmail": 5, "google": 6, "flipkart": 8}
  
18. sort the dictionary based on its values.

19. sort the elements from the given list. check if they are anagrams and 
	group them into a dictionary
	items = ["eat", "ate", "listen", "silent", "stressed", "tea", "desserts", "hai",
			 "hello"]
 
 
20. wap to get indexes of each item from the list given.
 	names = ["apple", "google", "apple", "yahoo", "google",  "gmail", "gmail"]
'''


'''
#wap to 
num=int(input('enter a num:'))
n=10
while num>=1:
    if num==3 or n==5:
        n-=1
        continue
    print(n)
    n-=1
   '''

#if the element is int skip the element 
l=[99,27.8,(8+5j),23]
res=[]
for i in l:
    if isinstance(i,int):
        continue
    res.append(i)
print(res)    

 #reversing the number
num=982
rev=0
while num!=0:
    rem= num %10
    rev= rev*10+rem
    num=num//10
print(rev)

'''
tracing

rev  |  num=982 | while n!=0  | rem=n%10  |  rev=rev*10+rem | num=num//10
-----------------------------------------------------------------------
0       982       true         982%10=2      0=0*10+2=>2      982//10==98
2        98       true         98%10==8      2*10+8=> 28       98//10==9
28       9        true         9%10==9       28*10+9==>289     9//10==0
289        0      false
'''



#palindrome no.
num=eval(input('enter a no.'))
res=num
rev=0
while num!=0:
    rev=rev*10+num%10
    num=num//10
print(f'reverse no is {rev}')
if res==rev:
    print('palindrome no.')
else:
    print('not a palindrome no.')

#armstrong no.
'''
if n=153
d=3  3^lenth+ 5^length + 3^length
---->3^3+5^3+3^3
---->153
'''
