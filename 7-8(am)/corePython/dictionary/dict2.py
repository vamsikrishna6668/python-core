dict={'k1':'ismail','k2':'anji','k3':'sai',12:'number','sal':12500000}
print(dict)
dict['k3']='sai teja'
print(dict)
print('------------------------------------------------------------------')
dict1={'ismail':850000,'kali':'wwe','batista':'wwe','big show':'wwf'}
print(dict1)
dict1['johncena']='wwf'
print(dict1)
print('------------------------------------------------------------------------')
dict2={'f1':123,'f2':25,'f3':36}
print(dict2)
dict2['f4']=68
print(dict2)
print('----------------------------------------')
dict3={'r1':'ismail','r2':'anji','r3':'satish'}
print(dict3.get('r1'))
print(dict3)
print('-----------------------------------------------')
dict4={'l1':15,'l2':123,'l3':6866,'l4':9769}
print(dict4.keys())
print(dict4)
print('----------------------------------------------------')
dict5={'n1':123,'n2':2568,'n3':6866,'n4':68978}
print(dict5.values())           # output:   dict_values([123, 2568, 6866, 68978])
print(dict5.keys())             # output:   dict_keys(['n1', 'n2', 'n3', 'n4'])
print(dict5.get('n1'))          # output:   123
print(dict5.items())            # output:   dict_items([('n1', 123), ('n2', 2568), ('n3', 6866), ('n4', 68978)])
print(dict5.popitem())          # output:   ('n4', 68978) It has removed last item from the list.
print(dict5)                    # output:   {'n1': 123, 'n2': 2568, 'n3': 6866}
print(dict5.pop('n2'))          #output:    2568
print(dict5.values())            #output:   dict_values([123, 6866])
print(dict5.setdefault('n5'))    #output:   None
print(dict5.clear())             #output:   None
dict6={'m1':123,'m2':456,'m3':6668}   # try this
print(dict5.copy(dict6))
