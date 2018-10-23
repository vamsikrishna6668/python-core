class demo:
    x=0
    def assign(self,i):
        self.y=i
    def show(self):
        print(self.y)
        print(demo.x)
    def change(self):
        demo.x=88
#calling block
d1=demo()
d1.assign(200)
d2=demo()
d2.assign(300)
d2.change()
d1.show()
d2.show()