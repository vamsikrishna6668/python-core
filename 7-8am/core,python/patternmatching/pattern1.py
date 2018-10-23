str = input('enter a string:')
length =len(str)
for row  in range(length):
    for col in range(row+1):
        print(str[row],end=' ')
    print()
