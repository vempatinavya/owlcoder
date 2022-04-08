n=list(map(int,input().split()))
k=n.count(1)
c=0
for i in n:
    if i!=0:
        c+=1
    else:
        break
print(k-c)

