def maxCSubArray(nums, mid):
    s=0
    ls=rs=float('-inf')
    for i in range(mid-1,-1,-1):
        if nums[i] == "1":
            break
        else:
            s+=1
        ls=max(ls,s)
    s=0
    for i in range(mid,len(nums)):
        if nums[i] == "1":
            break
        else:
            s+=1
        rs=max(rs,s)
    return ls+rs
    

def maxSubArray(nums):
    if len(nums)==1:
        if nums[0] == "1":
            return 0
        else:
            return 1

    if not nums:
        return 0
    mid=len(nums)//2
    ls=maxSubArray(nums[:mid])
    rs=maxSubArray(nums[mid:])
    cs=maxCSubArray(nums,mid)
    return max(ls,rs,cs)

print(maxSubArray("10000001100001"))