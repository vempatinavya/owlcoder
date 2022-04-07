n=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(n)):
    for j in range(1,len(n)):
        #print(i,j)
        if n[i]==n[j]:
            print(n[i],n[j])
            c+=1
print(c)
