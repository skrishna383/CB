class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        nums.sort()
        ans=0
        for r in range(len(nums)):
            k =k+nums[r]
            while k<nums[r]*(r-l+1) and r>l:
                k=k-nums[l]
                l=l+1
            ans=max(ans,r-l+1)
        return ans

            