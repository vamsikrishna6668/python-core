
#constructer over riding in different classes
class test:
    def __init__(self):
        print('i am a constructer of test')
class test1(test):
    def __init__(self):
        print('i am constructer of test1')
        super().__init__()

#calling block
t=test1()