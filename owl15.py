n=int(input())
l=list(map(int,input().split()))
ls=[]
for i in range(len(l)):
    k=0
    for j in range(len(l)):
        k+=abs(l[i]-l[j])
    ls.append(k)
print(ls)
