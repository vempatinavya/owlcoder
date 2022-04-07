
from math import *
def isprime():
    l,pre=[],[]
    for i in range(51):
        l.append(True)
    l[0],l[1]=False,False
    sq=int(sqrt(51))
    for i in range(2,sq+1):
        if l[i]==True:
            for j in range(i*i,51,+i):
                l[j]=False
               
    for i in range(51):
        pre.append(0)
    pre[0]=l[0]
    for i in range(1,51):
        pre[i]=pre[i-1]+l[i]
    return pre
    #return l
l1=isprime()
q=int(input())
for _ in range(q):
    k=int(input())
    print(l1[k])

"""
from math import *
def isprime():
    l=[]
    for i in range(100):
        l.append(i)
    sq=int(sqrt(100))
    for i in range(2,sq+1):
        for j in range(i*i,100,i):
            l[j]=i
    return l
         
r=isprime()
print(r)
"""
"""
from math import *
def isprime(s):
    sq=int(sqrt(s))
    for k in range(2,sq+1):
        if s%k==0:
            return False
    return True
"""
"""
n=int(input())
n=[int(i) for i in str(n)]
s=0
for i in n:
    if isprime(i):
        s+=i
if s:
    print(s)
else:
    print("0")
"""

    
