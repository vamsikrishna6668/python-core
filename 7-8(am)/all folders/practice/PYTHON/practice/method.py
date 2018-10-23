class customer:
    def __init__(self,id,name,add):
        self.custid=id
        self.custname=name
        self.custadd=add
    
    def show(self):
        print('customer details {},{},{}'.format(self.custid,self.custname,self.custadd))
c=customer(102,'prasad','hyd')
c.show()
c1=customer(101,'naidu','bangalore')
c1.show()


