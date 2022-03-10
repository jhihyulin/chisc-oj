a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a*b > c:
    print('Greater')
elif a*b == c:
    print('Equal')
elif a*b < c:
    print('Less')