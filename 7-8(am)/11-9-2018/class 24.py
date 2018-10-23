# 24. W.A.P for class name as a employee and method names as a assign with a default parameter and display method and magic method as a del
# create a object with a refered object and unreffered object for a class ?
class Employee:
    def assign(self,idno=980,name='Ismail'):
        self.idno=idno
        self.name=name
        print("Iam assign Method")
    def display(self):
        print(self.idno)
        print(self.name)
        print("Iam Display")
    def __del__(self):
        print("Iam a destructor")

# call
""" 
e1=Employee()
e1.assign()
e1.display()
e1.assign(680)

output:
Iam assign Method
980
Ismail
Iam Display
Iam assign Method
Iam a destructor
Process finished with exit code 0

"""
print("==================================================")
Employee().assign(idno=1040,name='Prav')
# Employee().display()   # Error
"""
Iam assign Method
Iam a destructor

"""
# ===============================================
#
# Process finished with exit code 0

print("===============================================")
"""

print(Employee().assign())
print(Employee().display())
"""



"""
Output :


"""