class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        ans=0
        nums.sort()
        while l<=r:
            if nums[l]+nums[r]<=target:
                ans=ans+pow(2, r-l, 10**9+7)  
                l=l+1
            else:
                r=r-1
        return ans % (10**9+7)
