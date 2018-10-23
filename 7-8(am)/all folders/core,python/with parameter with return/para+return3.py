def div(no1,no2):
    return no1+no2
def mul(no1,no2):
    print('the div=',add(no1+no2))
    return no1-no2
def sub(no1,no2):
    print('the mul=',sub(no1-no2))
    return no1*no2
def add(no1,no2):
    print('the sub=',mul(no1*no2))
    return no1/no2
#calling block
print(add(10,2))
