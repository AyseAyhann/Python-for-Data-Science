#IMPORTANT
#list comprehensions

#1
salaries=[1000,2000,3000,4000,5000]
null_list=[]
def new_salary(sal):
    sal=sal+sal*20/100
    return sal

for salary in salaries:
    if salary>3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

#all of them are in one structure
print([new_salary(salary*2) if salary<3000 else new_salary(salary) for salary in salaries])
[new_salary(salary*2) if salary<3000 else new_salary(salary) for salary in salaries]


#2
students=["John","Bob","Alice","Marry"]
students_not=["John","Alice"]
new_students=[]
#for student in students:
    #if student in students_not:
       #new_students.append(student.lower())
    #else:
       #new_students.append(student.upper())

#print(new_students)

[new_students.append(student.lower() if student in students_not else student.upper()) for student in students]
#[student.upper() if students not in students_not else student.lower() for student in students]
print(new_students)
#print(students)
