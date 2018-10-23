class employee:
    def __init__(self,empno,sal):
        self.empno=empno
        self.sal=sal
    def __gt__(self, other):
        if self.empno>self.sal:
            return True
        else:
            return False
e1=employee(1111,6000)
e2=employee(2222,7000)
print(e1>e2)

