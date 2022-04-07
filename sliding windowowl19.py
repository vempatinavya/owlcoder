def isanagram(frqp,frqw):
    #for i in range(26):
        if frqp[i]!=frqw[i]:
            return Flase
        return True
s=input()
p=input()
frqp=[0]*26
frqw=[0]*26
#print(frqp,frqw)
size1=len(s)
size2=len(p)
if size1<size2:
    print(p)
else:
    for i in range(size2):
        frqp[ord(p[i])-ord('a')]+=1
        frqw[ord(s[i])-ord('a')]+=1
    l=[]
    left=0
    right=size1
    while right<size2:
        if isanagram(frqp,frqw):
            l.append(left)
        frqw[ord(s[left])]-=1
        left+=1
        if right<size2:
            right+=1
print(l)
            
        

        
        









                
