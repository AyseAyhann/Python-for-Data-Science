#lambda
new_sum=lambda a,b: a+b
print(new_sum(4,5))

#map & lambda  map(func, list)
salaries=[1000,2000,3000,4000,5000]

def calculateSalaries(sal):
    return sal+ (sal*20)/100


for salary in salaries:
    print(calculateSalaries(salary))

#traverse on list object without loop
list(map(calculateSalaries,salaries))
print(list(map(calculateSalaries,salaries)))


print(list(map(lambda x: x*20/100+x,salaries)))

print(list(map(lambda x: x**2,salaries)))


#filter
list_store=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2==0, list_store)))

#reduce
from functools import reduce
list_store=[1,2,3,4]
print(reduce(lambda a,b: a+b,list_store))



