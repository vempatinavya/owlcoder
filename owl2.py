"""
n=int(input())
n=list(str(n))
s=''
for i in n:
    if i=='0':
        i='5'
    s+=i
print(s)
"""
"""
nums=[int(i) for i in input().split()]
nums.sort()
l=0
h=len(nums)-1
target=int(input())
k=[]
while True:
    if nums[mid]==target:
        p=nums.index(nums[mid])
        k.append(p)
        
    elif nums[mid]>target:
        h=mid-1
    else:
        l=mid+1
if k:
    print(k)
else:
    print("not found")

"""
"""
def binary(t,l,h,arr):
    mid=(l+h)>>1
    if l>h:
        return False
    if arr[mid]==t:
        return True
    elif arr[mid]>t:
        return binary(t,mid+1,h,arr)
    else:
        return binary(t,l,mid-1,arr)
arr=[int(i) for i in input().split()]
l=0
h=len(arr)-1
t=int(input())
if binary(t,l,h,arr):
    print("found")
else:
    print("not found")
    
"""
##nums=[int(i) for i in input().split()]
##target=int(input())
##k=nums.index(target)
##l=k
##h=len(nums)-1
##while l<h:
##    mid=(l+h)>>1
##    if nums[mid]==target:
"""
n,m=map(int,input().split())
for i in range(1,m):
    n=n//2
print(n)
"""
"""
def binaryl(arr,target):
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)>>1
        if target<=arr[mid]:
            h=mid-1
        else:
            l=mid+1
    return l
def binaryr(arr,target):
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)>>1
        if target>=arr[mid]:
            l=mid+1
        else:
            h=mid-1
    return h
arr=[int(i) for i in input().split()]
target=int(input())
l1=binaryl(arr,target)
h1=binaryr(arr,target)
l=[]
for i in range(l1,h1+1):
    if arr[i]==target:
        l.append(i)
print(l)
"""       
"""

def recyclePens(n, r, k, c):
    # Write your code here
    l=1
    h=n
    while l<=h:
        mid=l+(h-l)//2
        amt=r+((n-mid)*k)
        if((mid*c)<=amt):
            l=mid+1
        else:
            h=mid-1
    return h
n,r,k,c=map(int,input().split())
print(recyclePens(n,r,k,c))
"""

"""
n=int(input())
l=1
h=n
s=0
while l<=h:
    mid=(l+h)//2
    if mid*mid==n:
        print(mid)
        break
    elif mid*mid>n:
        h=mid-1
    else:
        l=mid+1
else:
    print(h)
"""
##n=input()
##l1=[]
##s=''
##for i in n:
##    if i.isdigit():
##        s+=i
##    elif s!='':
##        l1.append(s)
##        s=''
##l2=[]
##for i in l1:
##    i=int(i)
##    l2.append(i)
##print(max(l2))
##



##n=list(map(int,input().split()))
##m1=1
##m2=max(n)
##while m1<m2:
##    if m1 not in n:
##        n.append(m1)
##    m1+=1
##print(n)

def repeatadd(n):
    s=0
    while n>9:
        d=n%10
        n=n//10
        s=d+n
        n=s
    if n<=9:
        return n
    return s
    
n=int(input())
print(n)
print(repeatadd(n))








    

