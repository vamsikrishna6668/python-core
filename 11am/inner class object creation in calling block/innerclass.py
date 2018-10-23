class Tamilnadu:
    def __init__(self,a,b):
        self.a ='gunidy'
        self.b ='Tambaram'
        print('This is a Default constructor')
    def kelambakam(self,c,d):
        self.c ='thomus mount'
        self.d ='egmore'
        print(self.a)
        print(self.b)
    def thirusur(self):
        print(self.c)
        print(self.d)
    class chennai:
        def __init__(self):
            print('This is a constructor')
        def thirusulam(self,e):
            self.e ='This is a thirusulam'

        def pondy(self):
            print(self.e)
#calling block
s = Tamilnadu(10,68)
s.kelambakam(66,68)
s.thirusur()
inn =s.chennai()
inn.thirusulam(90)
inn.pondy()