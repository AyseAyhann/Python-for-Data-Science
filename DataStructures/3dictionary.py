#key-value

dictionary={1:'one',2:'two',3:'three',4:'four',5:'five'}

print(dictionary.get(1))
print(dictionary[1])
dictionary[1]='six'
print(dictionary)

dictionary[2]=["two","to"]
dictionary[4]=["four","for"]
print(dictionary)

dictionary.values()
dictionary.keys()
dictionary.items()
print(dir(dictionary))

dictionary.update({10:"Ten"})
print(dictionary)
#ip the update value isn't contained in dict, it adds as new