class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        if target>nums[-1]:
            return len(nums)
        while l<r:
            mid=(r+l)//2
            if target>nums[mid]:
                l=mid+1
            else:
                r=mid
        return l