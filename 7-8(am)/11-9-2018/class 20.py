# 20. W.A.P for  class name as a employee and Can we define multiple methods with same name and with different no of parameters
# and don't use self while printing in a method and in a single class?

class Employee:
    def show(self,idno,name):

        print(idno)
        print(name)
    def show(self,idno,name,sal):
        print(idno)
        print(name)
        print(sal)
    def show(self,idno,mobileno,comploca,domain):
        print(idno,mobileno,comploca,domain)
# call
e1= Employee()
e1.show(1022,'basha',23453422321,"Big Data")
"""
Output :
1022 basha 23453422321 Big Data

Process finished with exit code 0


"""