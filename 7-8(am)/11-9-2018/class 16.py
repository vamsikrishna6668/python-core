# 16.  W.A.P for method overloading class employee and with a instance method and methods name as a assign with a three default parameters
# and display method and create a object with a reference variable and create  three objects for class ?

class Employee:
    def assign(self,emploca='bng',empidno=789758,empdob='17-01-1994'):
        self.emploca=emploca
        self.empidno=empidno
        self.empdob=empdob
        print("Iam Assign Method of a Employee")
    def display(self):
        print("Iam Display Method of a Employee")
        print(self.emploca)
        print(self.empidno)
        print(self.empdob)
# call
e1=Employee()
e1.assign()
e1.display()
print("=======================================================")
e2=Employee()
e2.assign(emploca='Hyd')
e2.display()
print("=======================================================")

e3=Employee()
e3.assign(emploca='madras',empidno=1457997889)
e3.display()
print("=============================================================")

e4=Employee()
e4.assign(empdob='1-78-1996',emploca='kerala',empidno=7689)
e4.display()


"""
Output :
 
Iam Assign Method of a Employee
Iam Display Method of a Employee
bng
789758
17-01-1994
=======================================================
Iam Assign Method of a Employee
Iam Display Method of a Employee
Hyd
789758
17-01-1994
=======================================================
Iam Assign Method of a Employee
Iam Display Method of a Employee
madras
1457997889
17-01-1994
=============================================================
Iam Assign Method of a Employee
Iam Display Method of a Employee
kerala
7689
1-78-1996

Process finished with exit code 0
"""


