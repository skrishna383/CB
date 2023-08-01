class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums=sorted(set(nums))
        ans=n
        for i ,start in enumerate(nums):
            rip=bisect_right(nums,start+n-1)
            ans=min(ans,n-rip+i)
        return ans
