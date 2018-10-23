class tambaram:
    def gunidy(self,q,w):
        print(q+w)
class kelambakam:     # Method over riding in different class with a same method name & same parameters
    def gunidy(self,q,w):
        print(q-w)
#calling block
kela  =kelambakam()
kela.gunidy(1,2)