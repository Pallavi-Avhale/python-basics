#lists
#lists are mutable(can be changed)

marks=[99.8,55,77,99]
student=["karan","delhi"]

print(marks)
print(student)
print(type(marks))
print(len(marks))
print(marks[0])
student[0]="ravi"
print(student)

#list silicing
#list_name=[starting_indx:ending-indx]-ending indx is not included
print(marks[1:4])

#list methods
#append- add element in the last index of list
marks.append(33)
print(marks)

#sort -sorts the list in ascending order
marks.sort()
student.sort()
print(marks)
print(student)

#sorting in reverse order that is descending order
marks.sort(reverse=True)
print(marks)

student.sort(reverse=True)
print(student)

#reverse method- reverses the list 
marks.reverse()
print(marks)

#insert(indx,element)- adds the element in between list
marks.insert(2,58)
print(marks)

#remove method-removes any element of the list
marks.remove(77)
print(marks)

#pop method- removes the element in list using index no.
marks.pop(4)
print(marks)

