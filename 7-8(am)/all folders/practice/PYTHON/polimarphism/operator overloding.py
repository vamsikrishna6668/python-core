class operator:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages
    def __add__(self,other):
        print(self.name+other.name)
        print(self.pages+other.pages)

#calling block
o1=operator("python",100)
o2=operator("adv python",20)


print(o1+o2)