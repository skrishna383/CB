class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    r=r-1
                    l=l+1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                if s>0:
                    r=r-1
                if s<0:
                    l=l+1
        return ans