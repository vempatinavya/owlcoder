from math import *
def seiveprime():
    l=[]
    for i in range(1,51):
        l.append(True)
    l[0],l[1]=False,False
    sq=int(sqrt(50))
    for i in range(2,sq+1):
           if l[i]==True:
               for j in range(i*i,51,i):
                   l[j]=False
    print(l)
##n=int(input())
##l,r=map(int,input().split())
print(seiveprime())
