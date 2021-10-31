a,b,result = input().split()

a = int(a)
b = int(b)
result = int(result)

if ((a == 0 and b == 0) or (a != 0 and b == 0) or (a == 0 and b != 0)) and result == 0:
    print('AND')

if a == 0 and result == 0:
    print('OR')

if a == 0 and b == 0 or a != 0 and b != 0 and result == 0:
    print('XOR')

#UNSOLVED