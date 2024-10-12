my_str="hi my name is john and i am learning python"

def alternating(str):
    new_str=""
    for index, s in enumerate(str):
        if index%2==0:
            new_str+=s.upper()
        else:
            new_str+=s.lower()
    print (new_str)
    return new_str

alternating(my_str)
