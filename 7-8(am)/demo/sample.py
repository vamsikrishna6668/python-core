# 12. W.A.P for class employee and global variable and create a function name as fun1 with two parameters and return that two parameters.
# And with a static method, static method name as a show in static  method print the static variable and create two instance methods name
# as a assign with one parameter  and another instance method name as a display and import the class ---------- ?


a=50000
print("The golbal Variable value before a function:" ,a)
def fun1(b,c):
    b=1020
    c=10
    return b+c
class Employee:
    empsalincrement=300000
    empsalyearlybonus=20000
    @staticmethod
    def show():
        print(Employee().empsalincrement)
        print(Employee().empsalyearlybonus)
        print("Iam Show of Employee class")
    def assign(self,empaddress):
        self.empaddress=empaddress
        print("Iam assign of a Employee")
    def display(self):
        print(self.empaddress)
        print("Iam Display")


