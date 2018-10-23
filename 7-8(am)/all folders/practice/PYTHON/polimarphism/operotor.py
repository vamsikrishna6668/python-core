class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
        if self.age>other.age:
            return True
        else:
            return False
class person1(person):
    def __abs__(self):
        return abs(self.age)
    def __iadd__(self, other):
        return self.age+other.age
#calling block
nick=person1('prasad',20)
angela=person1('ramu',22)
print(nick>angela)

