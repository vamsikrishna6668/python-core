# 2. W.A.P for class student and with a static variables and static method and create a method of details and
#  print the static variables in details Method ?

class student:
    stdidno=6668
    stdname='Lakshmi'
    @staticmethod
    def details():
        print("Iam details Method ")
        print(student.stdidno)
        print(student.stdname)
# call

print(student.stdidno)
print(student.stdname)
print(student.details())
print("======================================")
student.details()
"""
Output :
6668
Lakshmi
Iam details Method 
6668
Lakshmi
None
======================================
Iam details Method 
6668
Lakshmi

Process finished with exit code 0



"""