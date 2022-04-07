"""
n=list(map(int,input().split()))
k=int(input())
l=[]
l.append(k)
for i in range(len(n)):
    m=k^n[i]
    l.append(m)
    k=m
print(l)
"""
def isvalid(i,allowed):
    if allowed in i:
        return True
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
c=0
for i in words:
    if  isvalid(i,allowed):
          c+=1
print(c)
