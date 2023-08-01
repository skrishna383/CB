class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        ans=0
        o=0
        c=0
        for r in range(len(nums)):
            if nums[r]%2==1:
                o=o+1
                c=0
            while o==k:
                if nums[l]%2==1:
                    o=o-1
                c=c+1
                l=l+1
            ans=ans+c
        return ans




