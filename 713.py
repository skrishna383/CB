class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        ans=0
        p=1
        if k==0:
            return 0
        for r in range(len(nums)):
            p=p*nums[r]
            while p>=k and l<=r:
                p=p/nums[l]
                l=l+1
            ans=ans+r-l+1
        return ans