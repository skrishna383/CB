class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        ans=0
        z=0
        for r in range(len(nums)):
            z=z+(nums[r]==0)
            while z>1:
                z=z-(nums[l]==0)
                l=l+1
            ans=max(ans,r-l)
        return ans