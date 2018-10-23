# 5. W.A.P for class employee and with method name as assign and display and write a instance variables without decarling in method header ?

class Employee:
    def assign(self):
        self.idno=101
        self.name="ravi"
        print("Iam assign")

    def display(self):
        print("Iam Display")
        print(self.idno)
        print(self.name)


# call
e1=Employee()
e1.assign()
e1.display()
"""
Output :
Iam assign
Iam Display
101
ravi
Process finished with exit code 0

"""