def add(x, y, z):
        i = x + y + z
        j = x - y + z
        k = x * y * z
        print('x=', x)
        print('y=', y)
        print('z=', z)
        print('x+y+z=', x + y + z)
        print('x-y+z=', x + y + z)
        print('x*y*z=', x * y * z)

a = 123
b = 321
c = 789
add(x=b, y=a, z=c)