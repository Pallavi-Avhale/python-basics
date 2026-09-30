'''
REGULAR EXPRESSION:(REGEXP)
------------------
-If we want to create a pattern we can go for regular expression but it will work for string data types
-If we want to represent group of string according to pattern.

::pattern means "inside a string"

webscrapping-->the process of extracting data from website

If we want to use regular expression then 
step 1. import re


'''

#count of uppercase characters
x="Python Class"
count=0
for i in x:
    if i.isupper():
        count+=1
print(count)  #2

#using regular expr.
import re     #import is keyword, re is a module
x="Python Class"
y=re.findall("[A-Z]",x)   
print(len(y))      #2

'''functions:

1.match()
2.fullmatch()
3. search()
4.finditer()
5.sub()
6.subn()
7.findall() ***imp
8.split()
-----------------------

1.match:
syntax:  new_varname=re.match("pattern",source_of_string--i.e.iterable name)
--->in the match() the element we are passing is present in the beginning(start of the iterable)
    if the element is present at the beginnging then output should be object address
    it the element is not present in the beginning then the output should be none

'''
import re
x="Morning Class"
y=re.match("Mor",x)  #<re.Match object; span=(0, 3), match='Mor'>.
# y=re.match("orn",x)    #None
print(y) 
print(y.start())   #0 starting position
print(y.end())     #3
print(y.group())    #Mor

#NOTE we cannot use any functions if the output is None

'''
2.fullmatch():
it will check the complete word and will give the output object address if the element passed is full string
if element passed is not full string then it will give the  output None

syntax:
new_varname=re.fullmatch("pattern",source_of_string)
'''
import re
a="Helloo Good Morning"
# q=re.fullmatch("Hel",a)  #None
q=re.fullmatch("Helloo Good Morning",a)   #<re.Match object; span=(0, 19), match='Helloo Good Morning'>

print(q)
print(q.start())  #0
print(q.end())    #19
print(q.group)    #<built-in method group of re.Match object at 0x000001331335CB40>


print("--------------")

'''
search():
-In search method we can check any character in the string

-if we have duplicate elements then it will consider the first occurance of the character(drawback)
unable to find 2nd accurance of the element

syntax:  new_var=re.search("pattern",source_of_string)
'''
import re
b="Good Night"
# w=re.search("oo",b)   #<re.Match object; span=(1, 3), match='oo'>
# w=re.search("o",b)    #<re.Match object; span=(1, 2), match='o'>
# w=re.search("od Nig",b)  #<re.Match object; span=(2, 8), match='od Nig'>
w=re.search("q",b)  #None   character is not present
print(w)

print("---------------")

'''
4.finditer():

we can find any character in the string, we can also find 1st 2nd 3rd,... occurances of the duplicate elements

we cannot directly use the finditer... it will give the object address to avoid this use typecasting or looping

syntax:  new_var=re.finditer("patter",source_of_string)
'''

import re
b="Python Class"
w=re.finditer("s",b)   #<callable_iterator object at 0x0000023B7DD72D70>
# print(list(w))
#[<re.Match object; span=(10, 11), match='s'>, <re.Match object; span=(11, 12), match='s'>]
for i in w:
    print(i)
#<re.Match object; span=(10, 11), match='s'>
# <re.Match object; span=(11, 12), match='s'>
print("-----------------")

'''
sub():
------
-same as replace() method in string

syntax: new_var=re.sub("Pattern","replace_character",string_name,count)

'''
x="Good Luck"
w=re.sub("o","*",x)   #G**d Luck

w=re.sub("o","@",x,1)  #G@od Luck

w=re.sub("o","&",x,1000)  #G&&d Luck ---it will don't show any error
print(w)
print("-----")

'''
6.subn()

new_var=re.subn("pattern","replace_char",source_of_string,count)

n-->no. of characters to replace

'''
x="Good Luck"
w=re.subn("o","*",x,300)    #('G**d Luck', 2)---->here no. of characters are replacing the count will be displayed
print(w)

w=re.subn("Luck","Python",x)   #('Good Python', 1)
print(w)
print("-----------")

'''
7.findall():
-we can search any elements

syntax:  new_var=re.findall("pattern",source_of_string)

--->the return type will be in list

1.[]
--->if we want to match/search group of characters/pattern the use [] pattern

2.[A-Z]
---->if we want to match uppercase character 
here in A-Z, - is the range 

3. [a-z]
---->if we want to match lowercase character

4. [0-9]
--->if we want to match digits 

5.[A-Za-z]
--->uppercase+ lowercase

6.[A-Za-z0-9]
--->uppercase + lowercase +number

7.[^abc]
--->apart from this abc the remaining characters we will get the output

'''

s="Good luck GUYS WelCome All @1233"

#lower case character
x=re.findall('[a-z]',s)   #['o', 'o', 'd', 'l', 'u', 'c', 'k', 'e', 'l', 'o', 'm', 'e', 'l', 'l']
print(x)

#uppercase
x=re.findall('[A-Z]',s)  #['G', 'G', 'U', 'Y', 'S', 'W', 'C', 'A']
print(x)

#numbers
x=re.findall('[0-9A-Z]',s)   #['G', 'G', 'U', 'Y', 'S', 'W', 'C', 'A', '1', '2', '3', '3']
print(x)

#^   negation
x=re.findall('[^@123]',s)
print(x)
#['G', 'o', 'o', 'd', ' ', 'l', 'u', 'c', 'k', ' ', 'G',
#  'U', 'Y', 'S', ' ', 'W', 'e', 'l', 'C', 'o', 'm', 'e', ' ', 'A', 'l', 'l', ' ']

x=re.findall('[^A-Z]',s)
print(x)
# ['o', 'o', 'd', ' ', 'l', 'u', 'c', 'k', ' ', ' ', 'e', 'l', 'o', 'm', 'e', ' ',
#  'l', 'l', ' ', '@', '1', '2', '3', '3']

#uppercase+lowercase+number
x=re.findall('[a-zA-Z0-9]',s)
print(x)
#['G', 'o', 'o', 'd', 'l', 'u', 'c', 'k', 'G', 'U', 'Y', 'S', 
# 'W', 'e', 'l', 'C', 'o', 'm', 'e', 'A', 'l', 'l', '1', '2', '3', '3']
print()

#to print all number use \d
w="TO All 12345 %$$#@@!@#$%^"
e=re.findall(r"\d",w)  #['1', '2', '3', '4', '5']
e=re.findall(r"\d+",w)   #['12345']
print(e)

e1=re.findall(r"\D",w)   #apart from numbers it will give output
#['T', 'O', ' ', 'A', 'l', 'l', ' ', ' ', '%', '$', '$', '#', '@', '@', '!', '@', '#', '$', '%', '^']

e1=re.findall(r"\D+",w)
#['TO All ', ' %$$#@@!@#$%^']
print(e1)

#to find the spaces in the string
e2=re.findall(" ",w)   #[' ', ' ', ' ']


#\s
e2=re.findall(r"\s",w)   #[' ', ' ', ' ']
print(e2)   

print("----------------------")










