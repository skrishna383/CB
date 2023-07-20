class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        ans,curl=0,0
        curl=0
        nums = [*set(nums)]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                curl=curl+1
            else:
                ans=max(ans,curl)
                curl=0
        ans=max(ans,curl)
        return ans+1
#M2:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        l=0
        ans=0
        for i in numset:
            if i-1 not in numset:
                l=0
                while i+l in numset:
                    l=l+1
                ans=max(ans,l)
        return ans
