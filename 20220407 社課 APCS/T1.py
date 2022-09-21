a,b,c=map(int,input().split())

aa = [a,b,c]
aa.sort()

print(aa[0], aa[1], aa[2])

a = aa[0]
b = aa[1]
c = aa[2]

if (a+b) <= c:
    print("No")
elif (a*a) + (b*b) < (c*c):
    print("Obtuse")
elif (a*a) + (b*b) == (c*c):
    print("Right")
elif (a*a) + (b*b) > (c*c):
    print("Acute")
else:
    pass