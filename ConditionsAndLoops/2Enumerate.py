#Enumerate: Counter/indexer

students=["John","Bob","Sam","Jane"]

for index, student in enumerate(students):
    print(index,student)


for index, student in enumerate(students,1):
    print(index,student)



even_list=[]
odd_list=[]

for index, student in enumerate(students):
    if index%2==0:
        even_list.append(student)
    else:
        odd_list.append(student)

print(even_list)
print(odd_list)
