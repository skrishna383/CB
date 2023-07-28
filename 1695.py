class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        ans=0
        seen=set()
        t=0
        for r in range(len(nums)):
            while nums[r] in seen and l<r:
                seen.remove(nums[l])
                t=t-nums[l]
                l=l+1
            t=t+nums[r]
            seen.add(nums[r])
            ans=max(ans,t)
        return ans
