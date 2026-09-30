'''
NESTED FOR LOOP--->
for loop inside another for loop
SYNTAX:
-----------------------------
for outer in iterable:
    statement
    for inner in outer:
        statement
-----------------------------



'''

#3days 3times meals
for days in range(1,4):
    for meals in range(1,4):
        print("days",days,"meals", meals)

#way2:
for days in range(1,4):
    print("days", days)
    for meals in range(1,4):
        print("meals",meals)

#examples:
# for i in range(1,6):
#     print(i)
#     for j in range(1,6):
#         print(j)
'''
output is outer will execute 1time and inner will execute after it.
again the next outer loop will execute once and the followed by inner all loops.
'''

shirts=["red","yellow","black"]
pants=["white","gray","blue"]
for i in shirts:
    for j in pants:
        print(i,j)


# for i in range(1,4):
    # for j in range(1,4):
        # print(i,j)
        # print(j,i)


total=0
o_total=0
for i in range(1,5):
    o_total=o_total+1
    for j in range(1,5):
        # total=total+1
        # pass
        None
print(total)
print(o_total)
print()
print()

s=[[1,2,3,4],[5,6,7],[8,9,10]]
for i in s:
    print(i)

for i in s:
    for j in i:
        if j%2==0:
            print(j)

for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print('\n')


student={"A":{"Name":"Kiran","age":45},
         "B":{"Name":"rock","age":55}}
for i in student.items():
    print(i)

for i in student:
    for j in student[i]:
        print("keys",i,"|",j,":",student[i][j])

print()

total=0
for i in range(1,11):
    for j in range(1,11):
        if(i+j)%2==0:
            total=total+1
print("total count of even no. =", total)

print()

#wap to print longest word in a sentence
st=""
max_len=0
s='life is full of surprises and miracles'
for i in s.split():
    if len(i)>max_len:
        max_len=len(i)
        st=i
print(st)

# 1.Wap to Count total vowels in each 
#  word using nested loop.
words = ["python", "loop", "data"]
for i in words:
    total=0
    for j in i:
        if j in "aeiouAEIOU":
            total=total+1
    print(i,total)

# 2.wap to Find Common Elements in Two Lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
x=[]
for i in a:
    if i in b:
        x.append(i)
print(x)

# 3.wap to Count Matching Characters
# Between Two Strings
s1 = "abc"
s2 = "bcd"

total=0
for i in s1:
    if i in s2:
        total=total+1
print(total)

# 4.Flatten 2D List (convert 2d to 1d)
l = [[1, 2], [3, 4], [5, 6]]
flat=[]
for i in l:
    for j in i:
        flat.append(j)
print(flat)


# wap to get output aaaa bbb ccccc
x='a4b3c5'
res=''
for i in range(len(x)):          #for position purpose
    if x[i].isalpha():            #if it is alpha
        y=x[i]                     #store into variable
    else:
        res=res+y*int(x[i])          #if not alpha then 0=0+a*4=aaaa
                                     # aaaab=aaaab*3=aaaabbb
                                     #aaaabbbc=aaaabbbc*5
print(res)




#5.  You have a dictionary of students and 
# their subject marks Print total marks of 
# each student.

students = {
    "A": {"math": 80, "science": 70},
    "B": {"math": 60, "science": 90},
    "C": {"math": 75, "science": 85}
}
for i in students:
    total=0
    for j in students[i]:
        total=total+students[i][j]
    print("key",i,"total marks",total)



#wap to sort the list without using sorted method
x=[72,3,33,14,5,21,0.5,1,7]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]<x[j]: #descending
            # x[i]>x[j] ----ascending order
            x[i],x[j]=x[j],x[i] #---swapping
print(x)
''''
iteration1---> 72>3(true) then swap---> [3,72,...]
iteration2---> 3>72 false
iteration3---> 3>33 false
iteration4----> 3>14 false
iteration5---> 3>5 false
iteration6----> 3>21 fasle
iteration6----> 3>0.5 true then swap --->[0.5,72,33,14,5,21,3,1,7]
now 0.5 is smallest now compare with 72 with all
iteration1--->72>33 true then swap ---> [0.5,33,72,14,5,21,3,1,7]
iteraion2---> 33>72 false
iteration3--->33>14 true then swap--->[0.5,14,72,33,5,21,3,1,7]
now compare with 14 will all
14>72 false
14>33 false
14>5 true then swap---->[0.5,5,72,33,14,21,3,1,7]
now compare 5 withh all
5>72 false
5>33 false
5>14 false
5>21 false
5>3 true then swap--->[0.5,3,72,33,14,21,5,1,7]
3>72 false
3>33 false
3>14 false
3>21 false
3>21 false
3>5 false
3>1 true the swap--->[0.5,1,72,33,14,21,5,3,7]
72>33 true then swap--->[0.5,1,33,72,14,21,5,3,7]
33>72 false
33>14 true then swap--->[0.5,1,14,72,33,21,5,3,7]
14>72 false
14>33 false
14>21 false
14>5 true then swap--->[0.5,1,5,72,33,21,14,3,7]
5>72 false
5>33 false
5>21 false
5>14 false
5>3 true then swap--->[0.5,1,3,72,33,14,5,7]


'''

#print AaBbCcDd...Zz
x=ord('A')
y=ord('a')
for i in range(0,26):
    print(chr(x+i),chr(y+i))


#wap to Count Total Elements in 2D List
l = [[1,2,3],[4,5],[6,7,8]]
for i in l:
    count=0
    for j in i:
        count=count+1
    print(i,"-->",count)

#wap to Find Sum of All Elements in 2D List
x = [[1,2,3],[4,5],[6,7,8]]
sum=0
for i in x:
    for j in i:
        sum=sum+j
print(sum)

#wap to Count Words Starting with Same Letter
words = ["apple","ant","bat","ball"] 
count=0
for i in range(len(words)):
    for j in range(i+1,len(words)):
        words[i][0]==words[j][0]
        count=count+1
print(count)


words = ["apple","ant","bat","ball"]
for w in words:
    count = 0
    for j in words:
        if w[0] == j[0]:
            count += 1
    print(f"{w} --> {count}")




