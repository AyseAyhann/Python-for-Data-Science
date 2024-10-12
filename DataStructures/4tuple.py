#unchangeable

t=("Aysh","Matte",1,2)
type(t)
dir(t)
t[0]
t[0:3]

#the way to change the tupple, firstly convert to the list
t=list(t)
t[0]=99
t=tuple(t)
print(t)