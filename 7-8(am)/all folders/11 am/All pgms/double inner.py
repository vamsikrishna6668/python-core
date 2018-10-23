def hello(s):
    def world():
        return 'SATISH'
    return 'Hello {} '.format(s,world())
#calling block
s =hello('SATISH')
print(s)
