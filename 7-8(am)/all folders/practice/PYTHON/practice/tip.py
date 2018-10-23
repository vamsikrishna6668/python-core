amount=int(input('enter a value'))
tip1 = 0.5
tip2 = 0.20
if amount<400:
    tip1=amount*0.5
    print('tip1=',tip1)

else:
    tip2=amount*0.20
    print('tip2=',tip2)


