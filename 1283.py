class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def issmallestdevisor(mi):
            sumq=0
            for i in nums:
                sumq=sumq+1+(i-1)//mi
                if sumq>threshold:
                    return False
            return True
        l,r=1,max(nums)
        while l<r:
            mi=l+(r-l)//2
            if issmallestdevisor(mi):
                r=mi
            else:
                l=mi+1
        return l
#m2
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def issmallestdevisor(mi):
            return sum((num - 1) // mi + 1 for num in nums) <= threshold
        l,r=1,max(nums)
        while l<r:
            mi=l+(r-l)//2
            if issmallestdevisor(mi):
                r=mi
            else:
                l=mi+1
        return l