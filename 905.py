class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        ans=[0]*len(nums)
        for i in nums:
            if i%2:
                ans[r]=i
                r=r-1
            else:
                ans[l]=i
                l=l+1
        return ans