def mobile(x):
    def sim():
        return 'airtel'
    return 'mobile {} is inserted in to sim {}'.format(x,sim())
#calling block
n1=mobile('samsung')
print(n1)
