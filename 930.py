class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def numSubarraysWithMaxSum(g):
            if g<0:return 0
            l=0
            ans=0
            for r in range(len(nums)):
                g=g-nums[r]
                while g<0:
                    g=g+nums[l]
                    l=l+1
                ans=ans+(r-l+1)
            return ans
        return numSubarraysWithMaxSum(goal)-numSubarraysWithMaxSum(goal-1)
