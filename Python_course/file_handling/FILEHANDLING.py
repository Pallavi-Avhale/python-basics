'''
FILE HANDLING

1.OS module

step 1: import OS

i)getcwd--->current working directory

syntax: import OS
print(OS.getcwd())
---------------------------------------------------------
-Now to go for desktop
ii)chdir()--->change directory
   (now i am in vs and want to change to desktop)

syntax: os.chdir('path')
------------------------------------------------------------
iii)mkdir()----->make directory

syntax:os.mkdir('folder_name)
--------------------------------------------------------



'''
#getcwd()
import os
print(os.getcwd())

#chdir
# os.chdir('C:\Users\LENOVO\Desktop\python')
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#noe to avoid special sequence in the path (\n) use raw string or replace \ to \\
os.chdir(r'C:\Users\LENOVO\Desktop\python')
print(os.getcwd())

#mkdir()
# os.mkdir('First_file')

'''if we want to create one more folder in the main folder then we 
should comment the previous folder that was created previously'''
# os.mkdir('second_file')


'''now to create nested folders'''
# os.makedirs('A\B\C\D\E')
# os.makedirs(r"E\r\k\m")

'''In my folder whatever information is present i want to check
then we use 
iv) listdir

syntax: os.listdir

v) to delete the folder we use
   rmdir()

   syntax: os.rmdir('folder_to _be_deleted')
'''
#listdir()
# print(os.listdir())  #['A', 'E', 'First_file', 'second_file']

#rmdir()
# os.rmdir("Second_file")

# os.rmdir('E')  #FileNotFoundError: [WinError 2] 
            #The system cannot find the file specified: 'Second_file'
            #because it is nested folder


#to delete the nested folder then
# os.rmdir('E\r\k\m')

'''to delete the file we have one more way
it will delete permanantly
vi)shutil

import shutil
shutil.rmtree("foler(with_nested_folders)")
'''
# import shutil
# shutil.rmtree("E")  #E\r\k\m deleted

'''
vii)popen()--->to open your file automatically
                it will work only for file not folder

syntax: os.popen("file_name")
-------------------------------------

vii)remove()
 syntax: os.remove("file_name")
 ------------------------------------

viii)remove()---->use to delete the file

syntax: os.remove('file_name')
--------------------------------------

ix)rename()

syntax: os.rename('oldfildename/folder','newfilename/foldername')
 '''
# print(os.listdir())  #['A', 'file1.txt', 'file2.txt', 'file3.txt.txt', 'First_file']

#popen()
# os.popen("file1.txt")  #do not miss the extension

#rename()
# os.rename('file1.txt','F1.txt')

#remove()
# os.remove("file3.txt.txt")

'''
x) to check the size of the file 

getsize()

print(os.path.getsize("filename"))
'''
# print(os.path.getsize("F1.txt")) #0
                               #7   if i wrote some data in the file 
                    




'''
FILE TYPES:
-------------

Two types:
1. Text file
ex:
text documents

2.Binary file
ex: Images,audio,video,mp3
'''


'''
FILEHANDLING:

we have 4 modes in filehandling

1. 'r' ---->read(only reading)
    -In r mode we can't create file
    -we can't write any data into the file

2.'w'-------->(write)
    -in write mode we can create file
    -we can write the data in file
    -we can read the file

Drawback---->it will always take the  latest one.
             overriding will happen so we go for append

3.'a'----->append
    -we can create file
    -we can write/add data 
    -we can read the file

4.'x'------------->creation
    -only file creating 
    -no operation


syntax:

with context manager:
---------------------->with open('filename','mode') as file_object:
                            pass
(we don't need to close the file manually automatically it will get closed)

                            
without context manager:
---------------------->   new_varname=open('filename','mode')
(here we need to close the file manually)
    '''

#creating the file--->without context manager
file=open('new_file1.txt')

#open the file
# os.popen("new_file1.txt")

#check that file is holding what type of mode
#if we are not using any mode by default it will take it as r mode
print(file.mode)  #r
print(file.name)   #new_file1.txt


'''
TWO BOOLEAN METHOD:

1.readable
2.writable
'''

print(file.readable())  #True-->when your file is in readble mode
print(file.writable())  #file=open('new_file1.txt')---false
print()

#i want to check file is  closed or not
print(file.closed)  #False

#NOTE if i want output true then manually we need to close the file
file.close()
print(file.closed)  #True
print()

#now i want to close this file
print(file.close())  #None


'''
1.read --->r
methods in read

i)read()---------->it will display all the data
ii)readline---------------->it will read line by line 
ii)readlines----------->it will read the data line by line and return in the form of list:[data\n data \n]
iv)read(n)----->it will display the no. of characters to read
v)readable()---->we will gget the output in boolean format
                (if my file is present in r mode it will be True
                if my file is not present in the r mode it will return False)


'''




'''write mode methods

i)write()------->we can write single line
ii)writelines()---------->we can write multiple lines
ii)writable()
'''

import os
print(os.getcwd())
os.chdir(r"C:\Users\LENOVO\Desktop\Data")
print(os.getcwd())

# file=open("morning.txt",'w')
# print(file.writable())  #True or false
# file.write("Good morning to all") #file will contain good morning to all
# file.write("python class")  #now file will contain python class
#so this drawback of write method it will always consider the latest one

# file.writelines(['python \n',"SQL\n","Manual\n"]) 
# python 
# SQL
# Manual
# os.popen("morning.txt")

'''append mode:
it will not display only the latest one, it will store all the data

i)write()
ii)writelines()


'''

# file=open("evening.txt","a")
# file.write("good evening \n")
# file.write("python class on going \n")

# file.writelines(["Apple\n","Mango\n"])
# os.popen("evening.txt")


file=open("evening.txt","r")
# print(file.read())
# good evening 
# python class on gong 
# python class on going 
# python class on going 
# Apple
# Mango
# print(file.readline())


# print(file.readlines())
# ['\n', 'good evening \n', 
# 'python class on gong \n', 'python class on going \n', 'python class on going \n', 'Apple\n', 'Mango\n']

# print(file.readable())   #True

# print(file.read(5))    #good

'''
x mode:

create the file
no operations

'''


'''
    WITH CONTEXT MANAGER:
    ------------------------

syntax:
with open("filename.extension","mode")as file_object:
    pass

'''

# with open("evening.txt","r") as data:
#     print(data.read())
# good evening 
# python class on gong 
# python class on going 
# python class on going 
# Apple
# Mango

# with open("evening.txt","r")as data:
    # print(data.readline())
    # print(data.readlines())  #['\n', 'good evening \n', 'python class on gong \n', 'python class on going \n', 'python class on going \n', 'Apple\n', 'Mango\n']
    # print(data.readable())  #True

#to do slicing
# from itertools import islice
#top to bottom
# with open("evening.txt","r")as file:
    # new=islice(file,0,5,1)    #newvar=islice(iterable,si,ei,sv)
    #['\n', 'good evening \n', 'python class on gong \n', 'python class on going \n', 'python class on going \n']
    # print(list(new))
    # for i in new:
    #     print(i)

#deque--bottom to top
# from collections import deque
# with open("evening.txt","r")as file:
#     new=deque(file,2)
#     print(new)    #deque(['Mango\n'], maxlen=1)

print("------------------")