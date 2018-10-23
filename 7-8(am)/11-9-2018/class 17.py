# 17. W.A.P for method overloading class name as a assign and write four methods names as a assign create a object with a reference variable for a class ?
class assign:
    def assign(self):
        print("Iam Assign 1")
    def assign(self,idno):
        self.idno=idno
        print(self.idno)
        print("Iam Assign 4")

    def assign(self,idno,name):
        self.idno = idno
        print(self.idno)
        self.name=name
        print(self.name)
        print("Iam Assign 3")
    def assign(self,idno,name,sal):
        self.idno = idno
        print(self.idno)
        self.name = name
        print(self.name)
        self.sal=sal
        print(self.sal)
        print("Iam Assign 2")
# call
a1=assign()
a1.assign(102,'sathyanarayana',7897897897897589)
a1.assign(123,'ravya',12457896858988)

"""
Output :  # The method over loading will follow the stack procedure . 

102
sathyanarayana
7897897897897589
Iam Assign 2
123
ravya
12457896858988
Iam Assign 2

Process finished with exit code 0
"""