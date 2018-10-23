class product:
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.price=c
    def __eq__(self, other):
        if self.name.upper()==other.name.upper() and self.price==other.price: #here upper  converting  upper to lower or
                                                                            #  lower to upper its depends upon requirement.
            return True
        else:
            return False
#calling block
p1=product(111,"mobile",8000)
p2=product(222,"Mobile",8000)
print(p1==p2)