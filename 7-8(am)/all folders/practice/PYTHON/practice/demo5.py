import item
from pickle import dump
x=int(input('enter how many objects you want to serilize'))
fobj=open("items.bin","wb")
for i in range(x):
    m=int(input('enter item id'))
    n=input('enter item name')
    o=int(input('enter price'))
    itemobj=item.Item(m,n,o)
    dump(itemobj,fobj)
print('serilize is completed')
fobj.close()
