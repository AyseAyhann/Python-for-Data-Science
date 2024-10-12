#1
z=8j+18
print(type(z))

#2
text="The goal is to turn data into information, and information insight."
new_text=""
for char in text:
    new_text+=char.upper()

print(new_text)

words=new_text.split() #list type
print(words)

#3
lst=['D','A','T','A','S','C','I','E','N','C','E']
print(len(lst))
print(lst[0])
print(lst[10])
my_list=lst[0:4]
print(my_list)
lst.remove(lst[8])
print(lst)
lst.append('P')
print(lst)
lst.insert(8,'N')
print(lst)

#4
dict={'Christian':["America",18],
      'Daisy':["England",12],
      'Antonio':["Spain",22],
      'Dante':["Italy",25]}

print(dict.keys())
print(dict.values())

dict['Daisy']=["England",13]
dict.update({"Daisy": ["England",13]})
print(dict)

dict["Ahmet"]=["Turkey",24]
print(dict)

dict.pop('Antonio')
print(dict)


#5
l=[2,13,18,93,22]
def dividelist(list):
    even=[]
    odd=[]
    for l in list:
        if l%2==0:
            even.append(l)
        else:
            odd.append(l)

    return even,odd

print(dividelist(l))


#6
students=["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index, student in enumerate(students):
    if index<3:
     print(f"Faculty of Engineering {index+1}. student: "+student)
    else:
     print(f"Faculty of Medical {index-2}. student: "+student)




#7
code=["CMP1005","PSY1001","HUK1005","SEN2204"]
credit=[3,4,2,4]
student_limit=[30,75,150,25]

zipped=zip(code,credit,student_limit)
print(list(zipped))


#8
set1=set(["data","python"])
set2=set(["data","function","qcut","lambda","python","AI"])

def calculateSet(s1,s2):
    if s1.issuperset(s2) :
        print(s1.intersection(s2))
    else:
        print(s2.difference(s1))


calculateSet(set1,set2)



