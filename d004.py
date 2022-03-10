a,b = map(int,input().split())

num = b - a + 1

while num > 0:
    print(a,end=" ")
    a += 1
    num -= 1