n=list(map(int,input().split()))
m1=max(n)
k1=n.index(m1)
n.remove(m1)
m2=max(n)
k2=n.index(m2)
n.remove(m2)
while len(n)!=1:
    m=abs(m1-m2)
    n.insert(k2+1,m)
    
    
    
