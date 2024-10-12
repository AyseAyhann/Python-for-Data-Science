#function call inside a function

def calculate(varm, moisture, charge):
    return int((varm+moisture)/charge)

print(calculate(90,12,12)*10)



def standardization(a,p):
    return a*10/100*p*p

print(standardization(45,1))


def all_calculate(varm,moisture,charge,p):
    a=calculate(varm,moisture,charge)
    b=standardization(a,p)
    print(b*10)

def all_calculation(varm,moisture,charge,a,p):
    #a=calculate(varm,moisture,charge)
    b=standardization(a,p)
    print(b*10)


all_calculate(1,3,5,12)

all_calculation(1,3,5,8,12)