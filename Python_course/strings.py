''' strings are immutable data types (cannot be changed) '''
str1='Divya '
str2="Choudhari \t"
str3="""DIEMS"""
#operations on string 
#concatenation
print(str1+str2+str3)
#length of string
print(len(str1))
print(len(str2))
print(len(str3))

#slicing
str4="Apna_College"
print(str4[1:4])
print(str4[ :5])
print(str4[3:len(str4)])
print(str4[ 4:])

#negative indexing
print(str4[-3:-1])
print(str4[-6:-1])

#string functions

str="I am studying python"
print(str.endswith("er"))
print(str.capitalize())
print(str.replace("I am","We are"))
print(str.find("y"))
print(str.count("am"))
print(str.find("Q")) #return -1 as Q is not in the string

#str=input("enter your first name")
#print("length of string str is",len(str))

#if-elif-else
light="green"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("wait")
else:
    print("light is broken")            
