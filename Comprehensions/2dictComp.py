# dict comprehension

dictionary={'a':1,'b':2,'c':3,'d':4}
dictionary.keys()
dictionary.values()
dictionary.items()

print({k:v**2 for k,v in dictionary.items()})
print({k.upper():v for k,v in dictionary.items()})
print({k.upper():v**2 for k,v in dictionary.items()})