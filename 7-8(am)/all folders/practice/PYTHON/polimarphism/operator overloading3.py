class sample:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({},{})".format(self.x,self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return (x, y)
s=sample()
