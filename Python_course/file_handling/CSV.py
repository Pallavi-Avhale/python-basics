'''
CSV FILE:
(comma separated value)
csv is a module name

while using csv it is mandatory to use 
step1>  import csv

There are two ways in csv:
1. Reading into csv file

   In reading we have two ways:
   i)reader()----------->[]
   ii)dictreader()---------->{}

2. Writing into csv files

  Writing in csv has two ways:
  i)writer()--->it will accept only 1 argument
                In writer we have 2 methods:-writerow() for single row insertion
                                            -writerows() for multiple row insertion
  ii)dictwriter()



'''

#writer()
import os
print(os.getcwd())
os.chdir(r"C:\Users\LENOVO\Desktop\Data")
print(os.getcwd())

'''
WITH CONTEXT MANAGER

with open("filename.extension","mode")as file:
    new_var=csv.writer(file)
    new_var.writerow([])
    new_var.writerows([[],[],[],..])


'''
#ex1

# with open("Day.csv","x"):
#     pass

# os.popen("Day.csv")

'''
#ex2
import csv
with open("pen.csv","w",newline="")as file:    #to avoid the empty space between two row use newline=""
    x=csv.writer(file)
    # x.writerow([" XYZ","Python class"])
    x.writerows([["abc","Sql","Manual"],["xyz","SQL"],['pqr',"manual","Python"]])
os.popen("pen.csv")'''

'''
import csv
with open("pen.csv","a",newline="")as file:    #to avoid the empty space between two row use newline=""
    x=csv.writer(file)
    # x.writerow([" XYZ","Python class"])
    x.writerows([["abc","Sql","Manual"],["xyz","SQL"],['pqr',"manual","Python"]])
os.popen("pen.csv")
'''

'''
dictwriter()

it will accept two argument...one is file object
                              another is 

'''

'''
import csv
with open("new.csv","w",newline="")as file:
    y=csv.DictWriter(file, ["NAME","AGE"])
    y.writeheader()
    # y.writerow({"NAME":"divyaa","AGE":21})
    y.writerows([{"NAME":"sakshii",'AGE':21},
                 {"NAME":"Pallavi","AGE":23},
                 {"NAME":"ANU","AGE":20}])
os.popen("new.csv")
'''

'''
import csv
with open("pen.csv","r")as file:
    z=csv.reader(file) 
    # print(z)   #<_csv.reader object at 0x000001B1AC45E380> do typecasting or looping
    # print(list(z))  #[['abc', 'Sql', 'Manual'], ['xyz', 'SQL'], ['pqr', 'manual', 'Python']]
    for i in z:
        print(i)
# ['abc', 'Sql', 'Manual']
# ['xyz', 'SQL']
# ['pqr', 'manual', 'Python']
'''

'''
import csv
with open("new.csv","r")as file:
    k=csv.DictReader(file)
    # print(list(k)) #[{'NAME': 'sakshii', 'AGE': '21'}, {'NAME': 'Pallavi', 'AGE': '23'}, {'NAME': 'ANU', 'AGE': ''}]
    for i in k:
        print(i)   
#{'NAME': 'sakshii', 'AGE': '21'}
# {'NAME': 'Pallavi', 'AGE': '23'}
# {'NAME': 'ANU', 'AGE': ''}

'''
'''
import csv
# with open("pythonData.csv","a")as file:
#     w=csv.writer(file)
#     # w.writerow(["Core Python","OOPS","Library"])
#     w.writerows([["Python","Loops","Functions","Data Types"],["OOPS","Inheritance","Polymorphism"]])
# os.popen("pythonData.csv")

with open("pData.csv","a")as file:
    q=csv.DictWriter(file,["Python","OOPS"])
    q.writeheader()
    # q.writerow({"Python":"Data Types","OOPS":"Inheritance"})
    q.writerows([{"Python":"Functions","OOPS":"Polymorphism"},
                 {"Python":"Looping","OOPS":"Abstraction"},
                 {"Python":"Patter ","OOPS":"Encapsulation"}])
os.popen("pData.csv")
'''

'''
tell() and seek() method
------------------------------
tell()---will show where the cursor point will be present
         it will not accept any argument

seek()------it will navigate the cursor where we want to take the cursor
           it will accept one argument that is (position)


'''
import os
print(os.getcwd())

# file=open("Day.txt","w")
# file.writelines(["python\n","java\n","sql\n"])
# os.popen("Day.txt")


# file=open("Day.txt","r")
# print(file.tell())   #0
# print(file.readline())   #python

# print(file.tell())    #8
# print(file.seek(3))   #3
# print(file.readline())  #hon

# print(file.seek(9))  #9
# print(file.readline())  #ava

# print(file.tell())   #14
# os.popen("Day.txt")

#NOTE this methods don't work properly sometimes....

'''
pickles/pickling/serialization
----------------------------------

if we are using pickle then the data is store permanently.
it is module--->no need to mention pickle.py
filename.pkl is extension for pickle file

it is called as conversion also called it as Parsing
it will convert python object to byte stream--->serialization/Pickling

The process of converting Byte stream to Python object is known as Deserializatin/Unpickling


To perform all the operation we need to do 
step1--> import pickle

methods to perform pickle :
1. Load()---support for file handling
-it will convert byte stream to python object
syntax:
with open("filename.extensionn)","mode") as file:
    new=pickle.load(file)
    print(new)

2.dump()---support for file handling
-it will convert python object to byte stream

syntax:
with open("filename.extensionn)","mode") as file:
    new=pickle.dump(file,iterable)
    print(new)


3.Loads()---without filehandling
-Byte stream to python object

syntax: new_var=pickle.loads(previous_var_name)

4.dumps()---without filehandling
-python object to byte stream
syntax-->new_var=pickle.dumps(iterable)


'''
'''
#dumps() and load()
import pickle
# new_var=pickle.dumps(iterable)
x=[10,20,30,40,50,60]   #pyhon object

#dumps(): python to byte stream
a=pickle.dumps(x)
# print(a)   #b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00]\x94(K\nK\x14K\x1eK(K2K<e.'   

#loads():byte stream obj  to python data
w=pickle.loads(a)
print(w)   #[10, 20, 30, 40, 50, 60]


y="Hello"
p=pickle.dumps(y)
# print(p)  #b'\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00\x8c\x05Hello\x94.'

#loads()
q=pickle.loads(p)
print(q)  #Hello

print()
'''

'''
NOTE in pickle files we are dealing with binary files so the modes in the binary types of file
we use rb--->read binary instead of r
       wb-->write binary instead of w
'''
#load() and dump() with file handling only

'''
import os
import pickle
with open("Hii.pkl","wb")as file:
    data=pickle.dump(["abc",11,67,"Hellooo"],file)
    # print(data)
# os.popen("Hii.pkl") #耄错   ]鐨调慢掔䬋䭃谇䡥汬潯澔攮

with open("Hii.pkl","rb")as file:
    data1=pickle.load(file)
    print(data1)    #['abc', 11, 67, 'Hellooo']
# os.popen("Hii.pkl")


file=open("Day.txt","r")
count=0
for i in file:
    # print(i)
    count+=1
print(count)  #3
'''

"""
1.Create a file and write "Hello Python" into it

2.Read and display entire file content

3.Count total number of lines in a file

4.Count total words in a file

5.Count total characters in a file

6.Count number of uppercase letters

7.Count number of lowercase letters

8.Count digits in file

9.Create CSV file of student data (DictWriter)

""" 
# 1.Create a file and write "Hello Python" into it
# import os
# print(os.getcwd())
# with open("Task.txt","r")as file:
#     # file.write("Hello Python \n")
#     print(file.read())
# # os.popen("Task.txt")

