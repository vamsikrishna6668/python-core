class p:
    def __init__(self):
        print("p's cons")
        super().__init__()
class a(p):
    def __init__(self):
        print("a's cons")
        super().__init__()
class b:
    def __init__(self):
        print("b's cons")
        super().__init__()
class x(a,b):
    def __init__(self):
        print("x's cons")
        super().__init__()
class q:
    def __init__(self):
        print("q's cons")
        super().__init__()
class r:
    def __init__(self):
        print("r's cons")
        super().__init__()
class m(q,r):
    def __init__(self):
        print("m's cons")
        super().__init__()
class y(m):
    def __init__(self):
        print("y's cons")
        super().__init__()
class z(x,y):
    def __init__(self):
        print("z's cons")
        super().__init__()
#calling block
f =z()
print(z.mro())