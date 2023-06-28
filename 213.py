class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums1=nums[0:-1]
        nums2=nums[1:]
        for i in range (len(nums1)-3,-1,-1):
            nums1[i]=nums1[i]+max(nums1[i+2:])
        for i in range (len(nums2)-3,-1,-1):
            nums2[i]=nums2[i]+max(nums2[i+2:])
        return max(max(nums1),max(nums2))
        

