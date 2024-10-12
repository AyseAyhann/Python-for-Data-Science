#square even numbers and add them to a dictionary
numbers=range(10)
new_dictionary={}
new_dict={}
for num in numbers:
    if num%2==0:
        #important
        new_dictionary[num]=num**2
    else:
        continue

print(new_dictionary)


print({num:num**2 for num in numbers if num%2==0})

