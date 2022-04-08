from math import *
def primes():
    l=[]
    n=30
    for i in range(1,n):
        l.append(i)
    l[0],l[1]=False,False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if l[i]==True:
            for j in range(i*i,n,i):
                l[i]=False
    return l
print(primes())
