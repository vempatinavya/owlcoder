n=list(map(int,input().split()))
n.sort()
pre=[0]*len(n)
pre[0]=n[0]
c=0
l=[]
for i in range(len(n)):
    pre[i]=pre[i-1]+n[i]
#print(pre)
s=pre[0]
for i in range(len(pre)):
    if i!=0:
        c+=pre[i-1]
    a=pre[-1]-pre[i]
    k=a-(n[i]*((len(n)-1)-i))
    l.append(c+k)
print(min(l))
    


