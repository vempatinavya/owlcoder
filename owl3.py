def searchRange(nums,target):
        i=0
        j=len(nums)-1
        l1,h1=0,0
        if target not in nums:
            print([-1,-1])
        elif len(nums)==0:
            print([-1,-1])
        while l1==0 or h1==0:
            if nums[i]==target:
                if l1==0:
                    l1=i
            #print(l1)
            if nums[j]==target:
                if h1==0:
                    h1=j
            #print(h1)

            i+=1
            j-=1
        print([l1,h1])
        
nums=list(map(int,input().split()))
target=int(input())
searchRange(nums,target)
