print("a","b",sep="**")
help(print)

def multipleTwo(a):
    a=a*2
    return a

print(multipleTwo(8))


#Docstring
def calculate(arg1,arg2):
    """
    exp. of numbers

Args:
    :param arg1: int, float
    :param arg2: int, float
Returns:
    int,float

    """
    result=arg1**arg2
    #return result
    print(result)


#print(calculate(4,3))
calculate(4,3)
calculate(arg1=5,arg2=4)



#function which adds input values to the list
list_store=[]
def appendList(a):
    list_store.append(a)
    return list_store


print(appendList(8))
print(appendList([1,2,3,4]))


list_store2=[]
def add_element(a,b=2):
    c=a*b
    list_store2.append(c)
    return list_store2
    #print(list_store2)

a=add_element(4,5)
print(a)

print(add_element(4,5))
print(add_element(4))



