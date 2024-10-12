#Interview Question
students=["John","Bob","Jane","Marry"]


def divide_students(student_list):
    groups=[[],[]]
    for index, student in enumerate(student_list):
        if index%2==0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


#print(divide_students(students))
divide_students(students)

