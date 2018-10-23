n=int(input('enter a number:'))
var =65
for i in range(1,n):
    for j in range(1,i+1):
        ch=chr(var)
        print(ch,end=' ')
        var =var+1
    print()
