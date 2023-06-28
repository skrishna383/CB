class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1=nums
        for i in range (len(nums)-3,-1,-1):
            nums1[i]=nums1[i]+max(nums1[i+2:])
        return max(nums1)