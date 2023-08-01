class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithMaxKDistinct(k):
            c=defaultdict(int)
            if k==0:return 0
            l=0
            ans=0
            for r,n in enumerate(nums):
                c[n]=c[n]+1
                while len(c)>k and r>l:
                    c[nums[l]]-=1 
                    if c[nums[l]]==0:
                        del c[nums[l]]
                    l=l+1
                ans=ans+r-l+1
            return ans
        return subarraysWithMaxKDistinct(k)-subarraysWithMaxKDistinct(k-1)