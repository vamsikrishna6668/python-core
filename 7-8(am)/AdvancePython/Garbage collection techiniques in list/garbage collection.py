class x:
    def __init__(self):
        print('Iam')
    def __del__(self):
        print('Del')
#call
a =[x(1),x(2),x(3)]
print(a)
