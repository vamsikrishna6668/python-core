class chennai:
    def __init__(self):
        print('Iam a constructor')
    def pallavaram(self,x,y):
        print(x+y)
class thiruvanmayur:
    def __init__(self):
       print('Iam a inner constructor')
    def pallavaram(self,x,y):       # He Iam over riding a method with inner class with outer class.
       print(x*y)
#calling block
t =thiruvanmayur()
t.pallavaram(6,8)