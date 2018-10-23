class test:
    def add(self,*args):
        results=0

        for i in args:
            results+=i

        print(results)
t=test()
t.add(10,20)
t.add(10,20,30)
t.add(1,2,3,4,5,6,7,8,9,0)
t.add(-1,34)

