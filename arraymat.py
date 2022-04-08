"""
q=int(input())
l=[int(j) for j in input().split()]
for i in range(q):
    k=[]
    lf,r,x=map(int,input().split())
    for i in range(lf,r+1):
        l[i]=l[i]+x
    print(l)
"""
"""
n=list(map(int,input().split()))
p=[0]*len(n)
p[0]=n[0]
if len(n)==1:
    print(len(n))
else:
    for i in range(len(n)):
        p[i]=p[i-1]+n[i]
print(p)
k=len(p)-1
i=1
while i<=k:
    print(p[i],p[k])
    if p[k]-p[i-1]==p[i]:
        print(i+1)
        break
    i+=1
"""
"""
n=list(map(int,input().split()))
l=[]
s=0
for i in n:
    s+=i
    l.append(s)
print(l)
"""
n=list(map(int,input().split()))
m=len(n)//2
l1,l2,l3=[],[],[]
for i in range(m):
    l1.append(n[i])
for j in range(m,len(n)):
    l2.append(n[j])
"""
i=0
j=m
while j<=len(n):
    l3.append(l1[i])
    l3.append(l2[j])
    i+=1
    j+=1
print(l3)
"""
i=0
for i in range(m):
    l3.append(l1[i])
    l3.append(l2[i])
print(l3)

    





















