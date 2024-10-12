#Interview question
#alternating a string
#even indexes are upper, odd indexes are lower
#traverse the indexes of the given string
my_str="hi my name is john and i am learning python"

#1
def alternateString(str):
  result=[]
  for i,s in enumerate(str):
    if i%2==0:
      result.append(s.upper())
    else:
      result.append(s.lower())
  return ''.join(result)  #converts list to string

print(alternateString(my_str))


#2
print(range(len("python")))

def alternating(str):
  new_str=""
  for i in range(len(str)):
    if i%2==0:
      new_str+=str[i].upper()  #appends
    else:
      new_str+=str[i].lower()

  return new_str

print(alternating(my_str))


