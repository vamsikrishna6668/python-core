#7. W.A.P to assign different values for instance variables for every object and class name as Employee and two methods as assign and display
#  and create two static varibles and two instance variables and print the static variables in display method and create two objects for the class ?
class Employee:
    comp_location='Hyd'
    comp_branch ="Hi-tech"
    def assign(self,idno,name,sal):
        self.idno=idno
        self.name=name
        self.sal=sal
        print("Iam assign")
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.sal)
        print(Employee.comp_location)
        print(Employee.comp_branch)
        print("Iam Display")
#calling
e1= Employee()
e1.assign(idno=101,name='chanti',sal=157899)
e1.display()
print(Employee.comp_location)
print(Employee.comp_branch)
print("==============================================")
e2=Employee()
e2.assign(idno=1025,name='Udhabav suri',sal=45789789456478)
e2.display()
"""
Output :
Iam assign
101
chanti
157899
Hyd
Hi-tech
Iam Display
Hyd
Hi-tech
==============================================
Iam assign
1025
Udhabav suri
45789789456478
Hyd
Hi-tech
Iam Display

Process finished with exit code 0

"""