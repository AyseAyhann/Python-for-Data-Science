#set
#changeable, unique

set1=set([1,3,7])
set2=set([1,2,3,4,5])
set3=set1.union(set2)

print(set1.difference(set2))  #set1-set2
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set3.issuperset(set2))
print(set1.isdisjoint(set2))