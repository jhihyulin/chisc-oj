from sys import stdin
 
def fn(a,b,c):
    if a+b <= c:return 0
    if(a*a)+(b*b) < (c*c):return 1
    if(a*a)+(b*b) == c*c:return 2
    if(a*a)+(b*b)>c*c: return 3
r=["NO","Obtuse","Right","Acute"]
a,b,c=sorted([int(x) for x in stdin.readline().split()])
v=fn(a,b,c)
print(a,b,c)
print(r[v])