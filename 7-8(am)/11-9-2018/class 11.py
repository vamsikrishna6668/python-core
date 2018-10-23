# 11. W.A.P for class employee and method name as a sample without any instance variables and create a object without a reference variable
# and with a reference variable?
class Employee:
    def sample(self):
        print("Iam sample")

# call
e1 =Employee()
e1.sample()
print("=========================================")
Employee().sample()
print("=========================================")
print(Employee().sample())


"""
output :
Iam sample
=========================================
Iam sample
=========================================
Iam sample
None

Process finished with exit code 0
"""
