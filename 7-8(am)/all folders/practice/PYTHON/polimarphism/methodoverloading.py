class sample:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
s1=sample()
s1.add(10,20)#error
s1.add(10,20,30)#if we remove the s1.add(10,20) then get results
                #the first method removed from memory and control goes second method
