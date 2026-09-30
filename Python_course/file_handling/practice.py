
# curremt directory
import os
print(os.getcwd())
os.chdir(r"C:\Users\LENOVO\Desktop\Test")
print(os.getcwd())
'''
# os.mkdir("Test1")

# os.makedirs('A\B\C')

# print(os.listdir())
# ['A', 'Test1']

# os.rmdir("A")
# import shutil
# shutil.rmtree("A\B")

# os.popen("File1.txt")
# os.rename("File1.txt","F1.txt")

# os.popen("file.txt")
# os.popen('File.txt')
# os.rename("File.txt","F1.txt")
# os.remove("file.txt.txt")
# print(os.path.getsize("F1.txt"))

file=open("Reading.txt","w")
# file.write('Hiii Helloo\n')
file.writelines(['Hellooo \n','Good morning \n'])
# os.popen('Reading.txt')

file=open("Reading.txt","r")
# print(file.read())  #Hiii Helloo
# print(file.readline())  
# print(file.read(2))    #Hi
# print(file.readable())  #True

file=open("Reading.txt","a")
# file.write("Hiii good morning\n")
# file.writelines(["This is append mode\n",'welcome \n'])
# os.popen("Reading.txt")

#with context manager
# with open("One.txt","w") as file:
    # file.write("Python class\n","hiii\n")  #TypeError: TextIOWrapper.write() takes exactly one argument (2 given)
    # file.writelines(['Welcome to python class\n','Welcome all\n'])
# os.popen("One.txt")

# with open("One.txt","a")as file:
    # file.write('One text file\n')
    # file.writelines(['welcome to\n','new file \n'])
# os.popen("One.txt")
# One text file
# welcome to
# new file 

# with open("One.txt","r")  as file:
#     print(file.read())
# os.popen("One.txt")
# One text file
# welcome to
# new file 

# with open("One.txt","r") as file:
#     print(file.readline())
# One text file

# with open("One.txt","r") as file:
#     print(file.readlines())
# ['One text file\n', 'welcome to\n', 'new file \n']

with open("One.txt","r") as file:
    print(file.read(4))
    print(file.readable())
# One 
# True

# file=open("One.txt","r")
# print(file.readlines())
# ['One text file\n', 'welcome to\n', 'new file \n']
print()
from itertools import islice
with open('One.txt',"r") as file:
    new=islice(file,0,2,1)
    print(list(new))
    # ['One text file\n', 'welcome to\n']

    for i in new:
        print(i)
# One text file

# welcome to

from collections import deque
with open("One.txt","r") as file:
    x=deque(file,1)
    print(x)
os.popen("One.txt")

'''

print(os.getcwd())
# os.mkdir('Course\SQL\Python')
# os.makedirs('Courses\Sql\Python')
# os.rmdir('Courses\Sql\Python')
# import shutil
# shutil.rmtree('Courses\Sql')
# shutil.rmtree('Course')
print(os.listdir())   #['A', 'Courses', 'F1.txt', 
                      #'One.txt', 'Reading.txt', 'Test1']


# os.popen("New.txt")
# os.rename("New.txt","New1.txt")
print(os.path.getsize("New1.txt"))  #0