class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isfeesable(n):
            splits=1
            maxsum=0
            for i in nums:
                maxsum+=i
                if maxsum>n:
                    maxsum=i
                    splits+=1
                    if splits>k:
                        return False
            return True


        for i in range(k):
            pass
        l,r=max(nums),sum(nums)
        while l<r:
            m=l+(r-l)//2
            if isfeesable(m):
                r=m
            else:
                l=m+1
        return l