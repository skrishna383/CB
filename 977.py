class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        piv=len(nums)-1
        for i in range(len(nums)):
            if nums[i]>=0 :
                piv=i
                break
        l=piv-1
        r=piv
        ans=[]
        while l!=-1 and r!= (len(nums)):
            if -nums[l]<nums[r]:
                ans.append(nums[l]*nums[l])
                l=l-1
            else:
                ans.append(nums[r]*nums[r])
                r=r+1
        if l==-1:
            while r!=(len(nums)):
                ans.append(nums[r]*nums[r])
                r=r+1
        if r==(len(nums)):
            while l!=-1:
                ans.append(nums[l]*nums[l])
                l=l-1
        return ans